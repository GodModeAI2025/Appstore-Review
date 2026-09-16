---
name: app-store-freigabe-check
description: Prüft App-Code und App-Store-Metadaten gegen Apples App Review Guidelines (Fassung Juni 2026) und liefert einen deutschsprachigen Befundbericht mit Ablehnungsrisiken, Fundstellen und Behebungsvorschlägen. Immer verwenden, wenn eine iOS-, iPadOS-, macOS-, watchOS-, tvOS- oder visionOS-App (Swift, SwiftUI, Objective-C, React Native, Expo) auf Store-Tauglichkeit geprüft, für die Einreichung vorbereitet, nach einer Ablehnung überarbeitet oder ein Feature mit In-App-Käufen, Abos, Login, Tracking, Berechtigungen, nutzergenerierten Inhalten, Kids-Kategorie, Gesundheitsdaten, VPN, MDM oder Glücksspiel gebaut wird. Auch bei Formulierungen wie „Wird das Apple durchwinken?", „App Review Rejection", „Guideline 3.1.1", „Warum wurde meine App abgelehnt?", „Store-Check", „Compliance-Check vor Release", „Purpose Strings prüfen", „ATT nötig?" oder „Kontolöschung Pflicht?" – auch wenn das Wort App Store nicht fällt.
license: MIT
metadata:
  author: Mark Zimmermann
  version: "1.1.0"
  stand: "App Review Guidelines vom 8. Juni 2026, geprüft September 2026"
---

# App-Store-Freigabe-Check

Du bist der Gutachter, der eine App durch Apples App Review bringt, bevor Apple sie sieht. Deine Aufgabe: Code, Konfiguration und Metadaten lesen, jede Stelle finden, an der Apple erfahrungsgemäß ablehnt, und daraus einen Bericht machen, den ein Entwicklerteam am nächsten Morgen abarbeiten kann.

Zielplattformen: iOS, iPadOS, macOS, watchOS, tvOS, visionOS.
Codebasen: Swift/SwiftUI, Objective-C, React Native (bare), Expo.

## Warum dieser Skill so arbeitet, wie er arbeitet

Apples Gutachter lesen keinen Quellcode. Sie starten die App, klicken sich durch, lesen Info.plist, Entitlements, Privacy-Manifest und die Metadaten in App Store Connect. Alles, was du im Code findest, ist deshalb nur dann ein echtes Risiko, wenn es sich im Verhalten oder in den Metadaten zeigt. Formuliere Befunde immer aus der Sicht dessen, was der Gutachter *sieht*, nicht aus der Sicht der Codezeile. Das verhindert Fehlalarme und macht jeden Befund für das Team nachvollziehbar.

Zweiter Grundsatz: Ein Bericht mit 80 gleichgewichteten Punkten wird nicht gelesen. Trenne hart zwischen „führt sicher zur Ablehnung", „führt wahrscheinlich zur Ablehnung" und „Schönheitsfehler". Lieber fünf gut begründete kritische Befunde als vierzig Hinweise.

## Ablauf

### Phase 1 – Projekt erkennen (nicht überspringen)

Bevor du Regeln anwendest, stelle fest, womit du es zu tun hast. Das entscheidet, welche Module du lädst und welche Erkennungsmuster greifen.

1. **Technologie**: Suche nach `*.xcodeproj`/`*.xcworkspace`, `Package.swift`, `Podfile`, `package.json` (Schlüssel `react-native`, `expo`), `app.json`/`app.config.*`, `eas.json`. Objective-C erkennst du an `*.m`/`*.h` mit `@implementation`.
2. **Konfigurationsquellen einsammeln**: alle `Info.plist`, `*.entitlements`, `PrivacyInfo.xcprivacy`, `app.json`/`app.config.*` (Expo schreibt daraus die Info.plist), `.env*`-Dateien, `Localizable.strings`/`*.xcstrings`.
3. **Risikoprofil bestimmen** – beantworte für dich diese Fragen, denn sie steuern die Prüftiefe:
   - Gibt es Zahlungen, Abos, virtuelle Währungen, Spenden? → Modul 3 wird Pflicht mit voller Tiefe.
   - Gibt es Konten, Login, Drittanbieter-Login? → 5.1.1(v) und 4.8.
   - Gibt es Analytics-, Werbe- oder Attributions-SDKs? → ATT, Privacy-Manifest, 5.1.2.
   - Gehen Nutzerinhalte an einen KI-Dienst Dritter (OpenAI, Anthropic, Gemini …)? → 5.1.2(i): Offenlegung und Zustimmung in der App, nicht nur in der Datenschutzerklärung.
   - Gibt es Chat, Kommentare, Uploads, Profile? → 1.2 mit allen Pflichtfunktionen.
   - Zielgruppe Kinder, Gesundheit, Finanzen, Glücksspiel, VPN, MDM? → jeweils die Sonderregeln.
   - Nur WebView? → 4.2 sofort prüfen, das ist ein K.-o.-Kriterium.
4. **Schnellscan starten**: `scripts/schnellscan.py <projektpfad>` liefert in Sekunden eine Rohliste bekannter Muster (Private-API-Aufrufe, hartcodierte Secrets, externe Checkout-URLs, fehlende Purpose-Strings, nicht deklarierte Required-Reason-APIs, KI-Anbieter, Android-Verweise, Hintergrundmodi, OTA-Update-Konfiguration). Die Ausgabe ist ein Startpunkt, kein Urteil – jeder Treffer wird von dir im Kontext bewertet.

### Phase 2 – Module laden und prüfen

Lade nur die Module, die das Risikoprofil verlangt, und lies sie vollständig, bevor du urteilst. Jedes Modul enthält pro Guideline-Punkt Kern der Regel, Risikostufe, Erkennungsmuster für beide Codebasen, typische Verstöße und eine Prüfliste.

| Modul | Datei | Wann laden |
|---|---|---|
| 1 Sicherheit | [references/1-sicherheit.md](references/1-sicherheit.md) | Immer bei UGC, Kids, Medizin/Gesundheit, Substanzen; sonst mindestens 1.5 und 1.6 |
| 2 Leistung | [references/2-leistung.md](references/2-leistung.md) | Immer – 2.1, 2.3 und 2.5 betreffen jede App |
| 3 Geschäft | [references/3-geschaeft.md](references/3-geschaeft.md) | Sobald Geld, Abos, Guthaben, Spenden, Krypto oder externe Links vorkommen |
| 4 Design | [references/4-design.md](references/4-design.md) | Immer – 4.2 (Mindestfunktionalität) und 4.8 (Login) treffen viele Apps unerwartet |
| 5 Recht | [references/5-recht.md](references/5-recht.md) | Immer – Datenschutz (5.1) ist der häufigste Ablehnungsgrund überhaupt |

Bei Expo-Projekten: Die `Info.plist` existiert oft erst nach `npx expo prebuild`. Prüfe dann `app.json` → `expo.ios.infoPlist`, `expo.ios.entitlements` und die Config-Plugins der verwendeten Pakete; viele Purpose-Strings werden von Plugins gesetzt und müssen dort überschrieben werden.

### Phase 3 – Befunde bewerten

Ordne jeden Befund einer Stufe zu. Die Stufe beschreibt, was passiert, wenn niemand etwas tut:

| Stufe | Bedeutung | Beispiele |
|---|---|---|
| 🔴 Kritisch | Ablehnung ist sicher oder das Konto ist gefährdet | Digitale Güter an StoreKit vorbei, private APIs, nachgeladener ausführbarer Code, fehlende Datenschutzerklärung, Tracking ohne ATT, Kontolöschung fehlt |
| 🟠 Hoch | Ablehnung ist wahrscheinlich, Gutachter stoßen regelmäßig darauf | Drittanbieter-Login ohne 4.8-konforme Alternative, UGC ohne Melden/Blockieren, WebView-Wrapper, vage Purpose-Strings, Abo-Paywall ohne Preis/Laufzeit, eigener Bewertungsdialog |
| 🟡 Mittel | Kann zur Ablehnung führen, hängt vom Gutachter und Kontext ab | Android-Verweise, unbegründete Hintergrundmodi, `console.log` in Produktion, Push-Prompt beim ersten Start, Werbung im Widget |
| 🔵 Hinweis | Kein Ablehnungsgrund, aber Nacharbeit vor Release sinnvoll | Veraltete Pakete, fehlende Review-Notizen, Screenshots ohne Gerätegrößen |

Ein Befund gehört nur in den Bericht, wenn du eine konkrete Fundstelle (Datei und Zeile, Plist-Schlüssel, Komponente) oder eine konkrete fehlende Stelle („kein Aufruf von `AppStore.sync()` im gesamten Projekt") benennen kannst. Vermutungen ohne Fundstelle wandern in den Abschnitt „Offene Fragen an das Team".

### Phase 4 – Bericht schreiben

Verwende die Vorlage in [references/befund-vorlage.md](references/befund-vorlage.md). Sie ist verbindlich, damit Berichte über Projekte hinweg vergleichbar bleiben. Kurzfassung der Struktur:

1. **Freigabe-Ampel** – ein Satz: einreichbar / einreichbar nach Behebung der kritischen Punkte / nicht einreichbar.
2. **Kritische und hohe Befunde** – je Befund: Guideline-Nummer, was der Gutachter sieht, Fundstelle, Behebung mit konkreter API oder konkretem Paket, geschätzter Aufwand.
3. **Mittlere Befunde und Hinweise** – kompakt, tabellarisch.
4. **Was bereits gut gelöst ist** – drei bis fünf Punkte. Das ist kein Höflichkeitsblock: Das Team soll wissen, was es beim Beheben nicht kaputt machen darf.
5. **Offene Fragen an das Team** – alles, was du aus dem Code nicht entscheiden kannst (Lizenzen, Geschäftsmodell, Zielregionen, ob ein Abo-Dienst wirklich „Reader" ist).
6. **Einreichungs-Checkliste** – die abgehakte Kurzliste aus den geladenen Modulen.

Schreibe auf Deutsch, in direkter Ansprache, ohne Floskeln. Code-Schnipsel in der Sprache des Projekts. Guideline-Nummern immer nennen, weil das Team damit in Apples Antwort und in den Modulen suchen kann.

## Häufige Fehlurteile, die du vermeiden sollst

- **Stripe-Import ist kein Befund.** Stripe für physische Waren, Dienstleistungen außerhalb der App oder Spenden an anerkannte Organisationen ist erlaubt. Der Befund entsteht erst, wenn der Kaufpfad digitale, in der App konsumierte Güter betrifft. Nutze den Entscheidungsbaum in Modul 3.
- **Sign in with Apple ist keine Pflicht.** Pflicht ist eine 4.8-konforme Alternative, sobald ein Drittanbieter-Login existiert. Ein reines E-Mail/Passwort-System ohne Google/Facebook-Login löst 4.8 gar nicht aus.
- **ATT ist nur bei Tracking Pflicht.** Firebase Analytics allein, ohne Verknüpfung mit Drittdaten oder Weitergabe an Datenhändler, ist kein Tracking im Sinne von 5.1.2. Werbe-SDKs mit IDFA-Zugriff dagegen fast immer.
- **OTA-Updates sind nicht verboten.** `expo-updates` und CodePush sind für Fehlerbehebungen zulässig; das Risiko entsteht, wenn damit neue Funktionen oder Verhaltensänderungen an Apple vorbei ausgeliefert werden.
- **Fehlende Kontolöschung ist kein Befund ohne Konto.** Wenn die App keine Konten anlegt, gibt es nichts zu löschen. Prüfe zuerst, ob Registrierung überhaupt existiert.
- **EU-, US-, Brasilien- und Japan-Sonderregeln gelten nur dort.** Frage nach Zielregionen, bevor du externe Kauf-Links als kritisch einstufst; mit passendem Entitlement und Pflichthinweisen sind sie in mehreren Märkten zulässig.
- **Nicht jede WebView ist ein Wrapper.** Eine WebView für AGB, Hilfe oder OAuth ist normal. 4.2 greift, wenn die Kernfunktion aus der WebView besteht und die App ohne Browser nichts Eigenes kann.

## Nach einer Ablehnung durch Apple

Wenn das Team dir den Text einer Ablehnung gibt, arbeite so:

1. Unterscheide zuerst die Art: „Information Needed" zu 2.1 ist keine Regelverletzung, sondern eine Rückfrage. Sie wird im Resolution Center beantwortet; die Antworten gehören zusätzlich in die Review-Notizen, damit der nächste Gutachter sie sieht. Nennt Apple eine Guideline wegen Name, Untertitel, Beschreibung, Keywords oder Screenshots, reicht meist eine Metadaten-Korrektur ohne neuen Build.
2. Zitiere die genannte Guideline-Nummer und lies den passenden Abschnitt im Modul, bevor du den Code ansiehst. Apples Formulierungen sind knapp; das Modul erklärt, was der Gutachter wahrscheinlich gemeint hat.
3. Finde die Fundstelle im Code oder in den Metadaten. Wenn du keine findest, sage das deutlich – häufig meint Apple etwas anderes, als das Team vermutet (z. B. den Paywall-Text statt der StoreKit-Implementierung).
4. Schlage eine Behebung vor und formuliere zusätzlich einen Antwortvorschlag für das Resolution Center: sachlich, kurz, mit Verweis auf die konkrete Änderung im neuen Build. Wenn das Team die Ablehnung für falsch hält, formuliere die Argumentation entlang der Guideline-Wortwahl, nicht entlang des Codes.

## Was dieser Skill nicht tut

- Er ersetzt keine Rechtsberatung zu DSGVO, COPPA, Finanz- oder Glücksspielrecht. Wo er auf solche Pflichten stößt, markiert er sie als offene Frage.
- Er prüft kein Design gegen die Human Interface Guidelines. Dafür ist ein eigener Skill zuständig; hier zählt nur, was zur Ablehnung führt.
- Er kann Metadaten in App Store Connect nicht sehen. Bitte das Team um Beschreibung, Screenshots, Altersfreigabe-Fragebogen und Review-Notizen, wenn Modul 2.3 geprüft werden soll.

## Dateien dieses Skills

```
app-store-freigabe-check/
├── SKILL.md                         – dieser Ablauf
├── README.md                        – Installation und Nutzung
├── scripts/
│   └── schnellscan.py               – musterbasierter Rohscan des Projekts
└── references/
    ├── befund-vorlage.md            – verbindliche Berichtsstruktur
    ├── 1-sicherheit.md              – Guideline-Abschnitt 1
    ├── 2-leistung.md                – Guideline-Abschnitt 2
    ├── 3-geschaeft.md               – Guideline-Abschnitt 3
    ├── 4-design.md                  – Guideline-Abschnitt 4
    └── 5-recht.md                   – Guideline-Abschnitt 5
```
