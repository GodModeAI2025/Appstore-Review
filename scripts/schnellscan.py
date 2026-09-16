#!/usr/bin/env python3
"""
Schnellscan für den App-Store-Freigabe-Check.

Durchsucht ein iOS-/macOS-Projekt (Swift, Objective-C, React Native, Expo) nach
Mustern, die erfahrungsgemäß mit Ablehnungen im App Review zusammenhängen, und
gibt eine Rohliste mit Fundstellen und Guideline-Bezug aus.

Die Ausgabe ist ein Startpunkt für die eigentliche Prüfung – kein Urteil.
Jeder Treffer muss im Kontext bewertet werden.

Aufruf:
    python3 scripts/schnellscan.py <projektpfad> [--json] [--max-treffer N]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

IGNORIERTE_VERZEICHNISSE = {
    ".git", "node_modules", "Pods", "build", "DerivedData", ".expo", "ios/build",
    "android", "dist", ".next", "coverage", "__pycache__", ".gradle", "vendor",
    "Carthage", ".swiftpm", ".build",
}

CODE_ENDUNGEN = {".swift", ".m", ".mm", ".h", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}
KONFIG_ENDUNGEN = {".plist", ".entitlements", ".json", ".xcprivacy", ".env", ".strings", ".xcstrings"}

# Purpose-Strings, die vorhanden sein müssen, sobald das zugehörige Framework
# oder Paket im Projekt auftaucht. Schlüssel: Info.plist-Key, Wert: Hinweise im Code.
BERECHTIGUNGEN = {
    "NSCameraUsageDescription": [r"AVCaptureDevice", r"UIImagePickerController", r"expo-camera", r"react-native-vision-camera", r"react-native-image-picker", r"expo-image-picker"],
    "NSPhotoLibraryUsageDescription": [r"PHPhotoLibrary", r"PhotosUI", r"expo-image-picker", r"expo-media-library", r"react-native-image-picker", r"@react-native-camera-roll"],
    "NSMicrophoneUsageDescription": [r"AVAudioSession", r"AVAudioRecorder", r"expo-av", r"expo-audio", r"react-native-audio"],
    "NSLocationWhenInUseUsageDescription": [r"CLLocationManager", r"expo-location", r"react-native-geolocation", r"@react-native-community/geolocation"],
    "NSContactsUsageDescription": [r"CNContactStore", r"expo-contacts", r"react-native-contacts"],
    "NSCalendarsUsageDescription": [r"EKEventStore", r"expo-calendar"],
    "NSUserTrackingUsageDescription": [r"ATTrackingManager", r"expo-tracking-transparency", r"react-native-tracking-transparency", r"ASIdentifierManager", r"advertisingIdentifier"],
    "NSHealthShareUsageDescription": [r"HKHealthStore", r"react-native-health"],
    "NSBluetoothAlwaysUsageDescription": [r"CBCentralManager", r"react-native-ble-plx", r"react-native-ble-manager"],
    "NSFaceIDUsageDescription": [r"LAContext", r"expo-local-authentication", r"react-native-biometrics"],
    "NSSpeechRecognitionUsageDescription": [r"SFSpeechRecognizer", r"@react-native-voice"],
    "NSMotionUsageDescription": [r"CMMotionManager", r"CMPedometer", r"expo-sensors"],
    "NSLocalNetworkUsageDescription": [r"NWBrowser", r"NetServiceBrowser", r"Bonjour", r"react-native-zeroconf"],
}

# Bekannte SDKs, die typischerweise Tracking auslösen oder ein Privacy-Manifest brauchen.
TRACKING_SDKS = [
    r"FacebookAds", r"FBAudienceNetwork", r"FBSDKCoreKit", r"react-native-fbsdk",
    r"GoogleMobileAds", r"react-native-google-mobile-ads", r"expo-ads-admob",
    r"AppsFlyerLib", r"react-native-appsflyer", r"Adjust", r"react-native-adjust",
    r"Branch", r"react-native-branch", r"Singular", r"Kochava", r"Tenjin",
    r"AppLovin", r"IronSource", r"UnityAds", r"Vungle", r"Chartboost", r"InMobi",
    r"Amplitude", r"Mixpanel", r"Segment", r"@segment/analytics-react-native",
]

# Required-Reason-APIs im eigenen nativen Code und die Kategorie, die dafür in
# PrivacyInfo.xcprivacy (oder Expo: ios.privacyManifests) stehen muss. Nur Swift und
# Objective-C: React-Native-Pakete bringen ihren Manifest selbst mit oder werden über
# Expo ergänzt, und JavaScript-Namen wie fs.stat() würden hier nur Fehlalarme liefern.
NATIVE_ENDUNGEN = {".swift", ".m", ".mm", ".h"}
REQUIRED_REASON_APIS = {
    "NSPrivacyAccessedAPICategoryUserDefaults": r"\b(NS)?UserDefaults\b|@AppStorage\b",
    "NSPrivacyAccessedAPICategoryFileTimestamp": r"NSFileCreationDate|NSFileModificationDate|\[\s*\.(creationDate|modificationDate)\s*\]|\.(contentModificationDateKey|creationDateKey)\b|NSURL(ContentModificationDate|CreationDate)Key|\b[fl]?stat(at)?\s*\(|\bf?getattrlist(bulk|at)?\s*\(",
    "NSPrivacyAccessedAPICategorySystemBootTime": r"\bsystemUptime\b|\bmach_absolute_time\s*\(",
    "NSPrivacyAccessedAPICategoryDiskSpace": r"volume(Available|Total)Capacity|NSFileSystem(Free)?Size|\.systemFreeSize\b|\bf?statv?fs\s*\(",
    "NSPrivacyAccessedAPICategoryActiveKeyboards": r"\bactiveInputModes\b",
}

# Muster mit Guideline-Bezug. (regex, stufe, guideline, beschreibung, nur-in)
@dataclass
class Muster:
    regex: str
    stufe: str
    guideline: str
    beschreibung: str
    endungen: set = field(default_factory=lambda: CODE_ENDUNGEN)
    flags: int = 0

MUSTER: list[Muster] = [
    # --- 2.5.1 Private APIs ---
    Muster(r"NSSelectorFromString\s*\(\s*@?\"_", "kritisch", "2.5.1", "Selector mit führendem Unterstrich – Hinweis auf private API"),
    Muster(r"performSelector\s*\(?\s*(NSSelectorFromString|@selector)\s*\(\s*@?\"?_", "kritisch", "2.5.1", "performSelector auf privaten Selector"),
    Muster(r"dlopen\s*\(|dlsym\s*\(", "kritisch", "2.5.1", "Dynamisches Laden von Symbolen – wird von Apple als Private-API-Zugriff gewertet"),
    Muster(r"/System/Library/PrivateFrameworks", "kritisch", "2.5.1", "Verweis auf PrivateFrameworks"),
    Muster(r"\bUIDevice\b.*\b_?(setBatteryLevel|_setOrientation)\b", "kritisch", "2.5.1", "Private UIDevice-Methode"),
    Muster(r"class_getInstanceMethod|method_exchangeImplementations", "hoch", "2.5.1", "Method Swizzling – im Review nur mit öffentlichen APIs unkritisch, sonst Risiko"),

    # --- 2.5.2 Nachgeladener Code ---
    Muster(r"\beval\s*\(", "kritisch", "2.5.2", "eval() – Ausführung nachgeladenen Codes"),
    Muster(r"new\s+Function\s*\(", "kritisch", "2.5.2", "new Function() – dynamische Codeausführung"),
    Muster(r"JSContext\b.*evaluateScript|evaluateScript\s*\(", "hoch", "2.5.2", "JavaScriptCore evaluateScript – prüfen, woher der Code stammt"),
    Muster(r"react-native-code-push|CodePush\.", "mittel", "2.5.2", "CodePush – OTA nur für Fehlerbehebungen, keine neuen Funktionen"),
    Muster(r"expo-updates|Updates\.(checkForUpdateAsync|fetchUpdateAsync)", "mittel", "2.5.2", "expo-updates – OTA nur für Fehlerbehebungen, keine neuen Funktionen"),

    # --- 1.6 / 5.1 Secrets ---
    Muster(r"(sk|pk)_(live|test)_[A-Za-z0-9]{8,}", "kritisch", "1.6", "Stripe-Schlüssel im Quellcode"),
    Muster(r"AKIA[0-9A-Z]{16}", "kritisch", "1.6", "AWS Access Key im Quellcode"),
    Muster(r"AIza[0-9A-Za-z\-_]{35}", "hoch", "1.6", "Google API Key im Quellcode – prüfen, ob eingeschränkt"),
    Muster(r"(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*[\"'][A-Za-z0-9_\-\.\/+=]{16,}[\"']", "hoch", "1.6", "Hartcodiertes Secret/Passwort/Token", flags=re.IGNORECASE),
    Muster(r"EXPO_PUBLIC_[A-Z_]*(SECRET|PRIVATE|PASSWORD)", "hoch", "1.6", "EXPO_PUBLIC_-Variable mit Secret – landet im JS-Bundle"),
    Muster(r"UserDefaults\.standard\.set\([^)]*(token|password|secret)", "hoch", "1.6", "Zugangsdaten in UserDefaults statt Keychain", flags=re.IGNORECASE),
    Muster(r"AsyncStorage\.setItem\(\s*[\"'][^\"']*(token|password|secret)", "hoch", "1.6", "Zugangsdaten in AsyncStorage statt SecureStore/Keychain", flags=re.IGNORECASE),
    Muster(r"NSAllowsArbitraryLoads</key>\s*<true/>", "mittel", "1.6", "ATS global deaktiviert", endungen={".plist"}),

    # --- 3.1.1 Zahlungen ---
    Muster(r"(checkout\.stripe\.com|paypal\.com/checkout|buy\.stripe\.com|paddle\.com|gumroad\.com|lemonsqueezy\.com)", "hoch", "3.1.1", "Externe Checkout-URL – kritisch, falls digitale Güter betroffen", flags=re.IGNORECASE),
    Muster(r"Linking\.openURL\([^)]*(checkout|payment|subscribe|upgrade|premium)", "hoch", "3.1.1", "Öffnet externe URL im Kaufkontext", flags=re.IGNORECASE),
    Muster(r"import\s+(Stripe|StripePaymentSheet|PayPal|Braintree|Paddle)", "mittel", "3.1.1", "Zahlungs-SDK importiert – Kaufpfad auf digitale Güter prüfen"),
    Muster(r"@stripe/stripe-react-native|react-native-paypal|braintree", "mittel", "3.1.1", "Zahlungs-SDK (RN) – Kaufpfad auf digitale Güter prüfen"),
    Muster(r"expo-in-app-purchases", "mittel", "3.1.1", "expo-in-app-purchases ist veraltet – auf expo-iap oder react-native-purchases umstellen"),

    # --- 5.6.1 Bewertungen ---
    Muster(r"(rate\s*(us|this app)|bewerte\s*(uns|die app)|5\s*sterne|5\s*stars)", "hoch", "5.6.1", "Eigener Bewertungsaufruf – nur SKStoreReviewController/StoreReview zulässig", flags=re.IGNORECASE),
    Muster(r"itms-apps://[^\"']*action=write-review", "mittel", "5.6.1", "Direktlink zur Bewertung – zulässig, aber nicht mit Anreizen oder Filterung kombinieren"),

    # --- 2.3.10 Plattformverweise ---
    Muster(r"[\"'][^\"']*\b(Android|Google Play|Play Store|Windows Phone)\b[^\"']*[\"']", "mittel", "2.3.10", "Verweis auf andere Plattform in einem String"),
    Muster(r"<string>[^<]*\b(Android|Google Play)\b[^<]*</string>", "mittel", "2.3.10", "Verweis auf andere Plattform in Ressourcen", endungen={".strings", ".plist", ".xcstrings", ".json"}),

    # --- 2.5.4 Hintergrundmodi ---
    Muster(r"<key>UIBackgroundModes</key>", "mittel", "2.5.4", "Hintergrundmodi deklariert – jeden Modus gegen echte Nutzung prüfen", endungen={".plist", ".json"}),
    Muster(r"\"UIBackgroundModes\"\s*:", "mittel", "2.5.4", "Hintergrundmodi in app.json deklariert – jeden Modus gegen echte Nutzung prüfen", endungen={".json"}),

    # --- 4.2 WebView ---
    Muster(r"WKWebView|react-native-webview|expo-web-browser|SFSafariViewController", "hinweis", "4.2", "WebView vorhanden – prüfen, ob die Kernfunktion nur aus Web besteht"),

    # --- 4.8 Login ---
    Muster(r"GoogleSignIn|GIDSignIn|@react-native-google-signin|FBSDKLoginKit|LoginManager\(\)|react-native-fbsdk-next|expo-auth-session", "hinweis", "4.8", "Drittanbieter-Login – 4.8-konforme Alternative (z. B. Sign in with Apple) muss existieren"),
    Muster(r"AuthenticationServices|ASAuthorizationAppleIDButton|expo-apple-authentication|@invertase/react-native-apple-authentication", "ok", "4.8", "Sign in with Apple vorhanden"),

    # --- 5.1.1(v) Kontolöschung ---
    Muster(r"(deleteAccount|delete_account|accountDeletion|kontoLoeschen|Konto löschen|Delete Account)", "ok", "5.1.1(v)", "Kontolöschung im Code gefunden", flags=re.IGNORECASE),
    Muster(r"(createAccount|signUp|register\(|Registrieren|Create Account)", "hinweis", "5.1.1(v)", "Kontoerstellung gefunden – Kontolöschung in der App muss existieren", flags=re.IGNORECASE),

    # --- 5.1.2 ATT ---
    Muster(r"ATTrackingManager|expo-tracking-transparency|react-native-tracking-transparency", "ok", "5.1.2", "ATT-Abfrage vorhanden"),
    Muster(r"ASIdentifierManager|advertisingIdentifier|getAdvertisingId", "hoch", "5.1.2", "IDFA-Zugriff – nur nach ATT-Einwilligung zulässig"),

    # --- 2.1 Debug-Reste ---
    Muster(r"console\.(log|debug|info)\(", "hinweis", "2.1", "console.log – vor Release entfernen oder in __DEV__ kapseln"),
    Muster(r"\bprint\(\"(DEBUG|TODO|FIXME)", "hinweis", "2.1", "Debug-Ausgabe im Swift-Code"),
    Muster(r"(TODO|FIXME|HACK|Lorem ipsum|Platzhalter|placeholder text|Coming soon|Demnächst)", "hinweis", "2.1", "Platzhalter oder unfertige Stelle", flags=re.IGNORECASE),

    # --- 1.2 UGC ---
    Muster(r"(reportUser|reportContent|blockUser|Melden|Blockieren|Report|Block)\b", "ok", "1.2", "Melde-/Blockierfunktion gefunden"),
    Muster(r"(sendMessage|postComment|uploadImage|createPost|ChatScreen|CommentList)", "hinweis", "1.2", "Nutzergenerierte Inhalte – Filter, Melden, Blockieren und Betreiberkontakt müssen vorhanden sein"),

    # --- 5.1.2(i) Drittanbieter-KI ---
    Muster(r"api\.openai\.com|api\.anthropic\.com|generativelanguage\.googleapis\.com|api\.mistral\.ai|api\.groq\.com|openrouter\.ai/api|api\.deepseek\.com|api\.perplexity\.ai", "mittel", "5.1.2(i)", "Endpunkt eines KI-Anbieters – vor dem ersten Senden in der App offenlegen, was an wen geht, und ausdrücklich zustimmen lassen", flags=re.IGNORECASE),
    Muster(r"import\s+(OpenAI|Anthropic|GoogleGenerativeAI|FirebaseVertexAI|FirebaseAI)\b|[\"'](openai|@anthropic-ai/sdk|@google/generative-ai|@google/genai|firebase/vertexai|firebase/ai)[\"']", "mittel", "5.1.2(i)", "SDK eines KI-Anbieters – vor dem ersten Senden in der App offenlegen, was an wen geht, und ausdrücklich zustimmen lassen"),

    # --- 2.4.2 Mining ---
    Muster(r"(coinhive|cryptonight|stratum\+tcp|xmrig|miner\.start)", "kritisch", "2.4.2", "Hinweis auf Krypto-Mining auf dem Gerät", flags=re.IGNORECASE),
]

# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

@dataclass
class Treffer:
    stufe: str
    guideline: str
    beschreibung: str
    datei: str
    zeile: int
    auszug: str


def dateien_sammeln(wurzel: Path):
    for pfad, verzeichnisse, dateien in os.walk(wurzel):
        verzeichnisse[:] = [v for v in verzeichnisse if v not in IGNORIERTE_VERZEICHNISSE and not v.endswith(".xcassets")]
        for name in dateien:
            p = Path(pfad) / name
            if p.suffix in CODE_ENDUNGEN or p.suffix in KONFIG_ENDUNGEN or name.startswith(".env"):
                yield p


def datei_lesen(p: Path) -> str | None:
    try:
        if p.stat().st_size > 2_000_000:
            return None
        return p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None


def scannen(wurzel: Path, max_treffer: int) -> tuple[list[Treffer], dict]:
    treffer: list[Treffer] = []
    zaehler: dict[str, int] = {}
    gesamt_text: dict[str, str] = {}
    plist_texte: list[str] = []
    appjson_texte: list[str] = []

    kompiliert = [(re.compile(m.regex, m.flags), m) for m in MUSTER]

    for p in dateien_sammeln(wurzel):
        inhalt = datei_lesen(p)
        if inhalt is None:
            continue
        rel = str(p.relative_to(wurzel))
        gesamt_text[rel] = inhalt
        if p.suffix == ".plist":
            plist_texte.append(inhalt)
        if p.name in ("app.json", "app.config.json"):
            appjson_texte.append(inhalt)

        for zeilen_nr, zeile in enumerate(inhalt.splitlines(), start=1):
            for rx, m in kompiliert:
                if p.suffix not in m.endungen and not (p.name.startswith(".env") and ".env" in m.endungen):
                    continue
                if rx.search(zeile):
                    schluessel = f"{m.guideline}|{m.beschreibung}"
                    zaehler[schluessel] = zaehler.get(schluessel, 0) + 1
                    if zaehler[schluessel] <= max_treffer:
                        treffer.append(Treffer(m.stufe, m.guideline, m.beschreibung, rel, zeilen_nr, zeile.strip()[:160]))

    # Purpose-Strings: Framework genutzt, aber Schlüssel fehlt?
    alle_konfig = "\n".join(plist_texte + appjson_texte)
    alle_code = "\n".join(t for r, t in gesamt_text.items() if Path(r).suffix in CODE_ENDUNGEN)
    fehlende_purpose = []
    for key, hinweise in BERECHTIGUNGEN.items():
        genutzt = any(re.search(h, alle_code) for h in hinweise)
        vorhanden = key in alle_konfig
        if genutzt and not vorhanden:
            fehlende_purpose.append(key)
        elif vorhanden:
            # Vage Purpose-Strings erkennen
            for text in plist_texte + appjson_texte:
                mm = re.search(rf"{key}(</key>\s*<string>|\"\s*:\s*\")([^<\"]*)", text)
                if mm:
                    wert = mm.group(2).strip()
                    generisch = re.search(r"(needs|benötigt|requires|access to|Zugriff auf|uses|verwendet)\s*(the\s*|your\s*|Ihre\s*|deine\s*)?(camera|kamera|photos?|fotos?|location|standort|microphone|mikrofon|contacts|kontakte)\s*(access|zugriff|library|roll)?\.?$", wert, re.IGNORECASE)
                    if len(wert) < 30 or generisch:
                        treffer.append(Treffer("hoch", "5.1.1(iv)", f"Purpose-String für {key} ist zu vage: „{wert}“", "Info.plist/app.json", 0, wert[:160]))

    for key in fehlende_purpose:
        treffer.append(Treffer("kritisch", "5.1.1(iv)", f"{key} fehlt, obwohl das zugehörige Framework/Paket genutzt wird", "Info.plist/app.json", 0, ""))

    # Tracking-SDKs ohne ATT
    hat_att = bool(re.search(r"ATTrackingManager|expo-tracking-transparency|react-native-tracking-transparency", alle_code))
    gefundene_sdks = sorted({s for s in TRACKING_SDKS if re.search(s, alle_code)})
    if gefundene_sdks and not hat_att:
        treffer.append(Treffer("hoch", "5.1.2", f"Tracking-/Werbe-SDKs ohne ATT-Abfrage: {', '.join(gefundene_sdks)}", "(projektweit)", 0, ""))

    # Privacy-Manifest: als Datei oder, bei Expo, als ios.privacyManifests in app.json
    hat_manifest = any(r.endswith("PrivacyInfo.xcprivacy") for r in gesamt_text) or \
        any("privacyManifests" in t for t in appjson_texte)

    # Required-Reason-APIs: im nativen Code genutzt, aber nirgends deklariert?
    # Gesucht wird in allen .xcprivacy-Dateien und in Expo-Konfigurationen, weil
    # Expo die Gründe aus app.json/app.config.* beim Prebuild in den Manifest schreibt.
    deklarationen = "\n".join(
        t for r, t in gesamt_text.items()
        if r.endswith(".xcprivacy") or Path(r).name.startswith(("app.json", "app.config."))
    )
    rr_genutzt: dict[str, str] = {}
    for kategorie, regex in REQUIRED_REASON_APIS.items():
        rx = re.compile(regex)
        for r, t in gesamt_text.items():
            if Path(r).suffix not in NATIVE_ENDUNGEN:
                continue
            for zeilen_nr, zeile in enumerate(t.splitlines(), start=1):
                if rx.search(zeile):
                    rr_genutzt[kategorie] = f"{r}:{zeilen_nr}"
                    break
            if kategorie in rr_genutzt:
                break
    rr_fehlend = sorted(k for k in rr_genutzt if k not in deklarationen)

    if not hat_manifest:
        genutzt_text = f" Im nativen Code genutzt: {', '.join(sorted(rr_genutzt))}." if rr_genutzt else ""
        treffer.append(Treffer("mittel", "5.1.1(x)", "Kein PrivacyInfo.xcprivacy gefunden – Required-Reason-APIs und Datenerhebung müssen deklariert sein." + genutzt_text, "(projektweit)", 0, ""))
    else:
        for kategorie in rr_fehlend:
            datei, _, zeile = rr_genutzt[kategorie].rpartition(":")
            treffer.append(Treffer("hoch", "5.1.1(x)", f"Required-Reason-API genutzt, aber {kategorie} ist nicht deklariert – App Store Connect weist den Upload mit ITMS-91053 ab", datei, int(zeile), ""))

    # Konto ohne Löschung
    hat_konto = bool(re.search(r"(createAccount|signUp|register\(|Registrieren|Create Account)", alle_code, re.IGNORECASE))
    hat_loeschung = bool(re.search(r"(deleteAccount|delete_account|accountDeletion|Konto löschen|Delete Account)", alle_code, re.IGNORECASE))
    if hat_konto and not hat_loeschung:
        treffer.append(Treffer("kritisch", "5.1.1(v)", "Kontoerstellung vorhanden, aber keine Kontolöschung im Code gefunden", "(projektweit)", 0, ""))

    # Drittanbieter-Login ohne Apple-Login
    hat_dritt_login = bool(re.search(r"GoogleSignIn|GIDSignIn|@react-native-google-signin|FBSDKLoginKit|react-native-fbsdk", alle_code))
    hat_apple_login = bool(re.search(r"AuthenticationServices|ASAuthorizationAppleIDButton|expo-apple-authentication|react-native-apple-authentication", alle_code))
    if hat_dritt_login and not hat_apple_login:
        treffer.append(Treffer("hoch", "4.8", "Drittanbieter-Login vorhanden, aber kein Sign in with Apple oder gleichwertige Alternative gefunden", "(projektweit)", 0, ""))

    # IAP ohne Restore
    hat_iap = bool(re.search(r"StoreKit|SKProduct|Product\.products|react-native-purchases|react-native-iap|expo-iap", alle_code))
    hat_restore = bool(re.search(r"restoreCompletedTransactions|AppStore\.sync|restorePurchases|getAvailablePurchases|Purchases\.restorePurchases", alle_code))
    if hat_iap and not hat_restore:
        treffer.append(Treffer("hoch", "3.1.1", "In-App-Käufe vorhanden, aber keine Wiederherstellung von Käufen gefunden", "(projektweit)", 0, ""))

    zusammenfassung = {
        "dateien_gescannt": len(gesamt_text),
        "purpose_strings_fehlend": fehlende_purpose,
        "tracking_sdks": gefundene_sdks,
        "att_vorhanden": hat_att,
        "privacy_manifest": hat_manifest,
        "required_reason_apis": sorted(rr_genutzt),
        "required_reason_apis_undeklariert": rr_fehlend if hat_manifest else sorted(rr_genutzt),
        "konto": hat_konto, "kontoloeschung": hat_loeschung,
        "drittanbieter_login": hat_dritt_login, "apple_login": hat_apple_login,
        "iap": hat_iap, "restore": hat_restore,
        "gekappte_muster": {k: v for k, v in zaehler.items() if v > max_treffer},
    }
    return treffer, zusammenfassung


REIHENFOLGE = {"kritisch": 0, "hoch": 1, "mittel": 2, "hinweis": 3, "ok": 4}
SYMBOL = {"kritisch": "🔴", "hoch": "🟠", "mittel": "🟡", "hinweis": "🔵", "ok": "✅"}


def ausgabe_text(treffer: list[Treffer], zusammenfassung: dict) -> str:
    zeilen = ["# Schnellscan – Rohbefunde", "",
              f"Dateien gescannt: {zusammenfassung['dateien_gescannt']}", ""]
    treffer.sort(key=lambda t: (REIHENFOLGE.get(t.stufe, 9), t.guideline, t.datei, t.zeile))
    aktuelle = None
    for t in treffer:
        if t.stufe != aktuelle:
            aktuelle = t.stufe
            zeilen.append(f"\n## {SYMBOL[t.stufe]} {t.stufe.capitalize()}\n")
        ort = f"{t.datei}:{t.zeile}" if t.zeile else t.datei
        auszug = f" – `{t.auszug}`" if t.auszug else ""
        zeilen.append(f"- [{t.guideline}] {t.beschreibung} — `{ort}`{auszug}")
    if zusammenfassung["gekappte_muster"]:
        zeilen.append("\n## Gekappte Muster (mehr Treffer als angezeigt)\n")
        for k, v in zusammenfassung["gekappte_muster"].items():
            zeilen.append(f"- {k}: {v} Treffer insgesamt")
    zeilen.append("\n---\nHinweis: Jeder Treffer ist ein Prüfauftrag, kein Urteil. Bewertung erfolgt im Kontext der Module.")
    return "\n".join(zeilen)


def main() -> int:
    ap = argparse.ArgumentParser(description="Musterbasierter Rohscan für den App-Store-Freigabe-Check")
    ap.add_argument("projekt", help="Pfad zum Projektverzeichnis")
    ap.add_argument("--json", action="store_true", help="Ausgabe als JSON")
    ap.add_argument("--max-treffer", type=int, default=15, help="Maximale Treffer pro Muster (Standard 15)")
    args = ap.parse_args()

    wurzel = Path(args.projekt).resolve()
    if not wurzel.is_dir():
        print(f"Kein Verzeichnis: {wurzel}", file=sys.stderr)
        return 2

    treffer, zusammenfassung = scannen(wurzel, args.max_treffer)
    if args.json:
        print(json.dumps({"treffer": [asdict(t) for t in treffer], "zusammenfassung": zusammenfassung}, ensure_ascii=False, indent=2))
    else:
        print(ausgabe_text(treffer, zusammenfassung))
    return 0


if __name__ == "__main__":
    sys.exit(main())
