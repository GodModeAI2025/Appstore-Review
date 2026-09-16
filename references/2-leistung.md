# Abschnitt 2 – Leistung (Performance)

Stand: Apple App Review Guidelines, Fassung vom 8. Juni 2026 (geprüft September 2026).
Zurück zur Übersicht: ../SKILL.md

Abschnitt 2 ist der „handwerkliche" Teil der Guidelines: Ist die App fertig, läuft sie stabil, stimmen die Angaben im Store, benimmt sie sich auf der Hardware anständig und nutzt sie nur das, was Apple offiziell freigibt? Die meisten Ablehnungen in diesem Abschnitt sind keine Grundsatzfragen, sondern vermeidbare Nachlässigkeiten – deshalb lohnt sich hier ein besonders gründlicher Code- und Konfigurations-Scan.

## Wo Apple aktuell besonders genau hinschaut

1. **2.1(a) Abstürze und Unvollständigkeit** – nach wie vor der häufigste Ablehnungsgrund überhaupt. Debug-Reste, tote Buttons, fehlende Demo-Zugänge und Backend-Umgebungen, die im Review nicht erreichbar sind.
2. **2.5.1 Private APIs** – die automatische Vorprüfung beim Upload erkennt Selektoren, Symbole und Framework-Pfade zuverlässig. Besonders Drittanbieter-SDKs und ältere React-Native-Libraries schleppen private Aufrufe ein.
3. **2.5.2 Nachgeladener Code** – OTA-Update-Mechanismen (expo-updates, CodePush) werden geduldet, solange sie nur Fehler beheben und den Charakter der App nicht verändern. Wer über OTA neue Funktionen ausrollt, riskiert die Sperre des Entwicklerkontos.
4. **2.3.6 Altersfreigabe** – der 2025 erweiterte Fragebogen (Stufen 4+, 9+, 13+, 16+, 18+) hat 2026 zusätzliche Fragen zu Social-Media-Funktionen bekommen; ab September 2026 sind sie Pflicht für jede neue Einreichung. Falsche Antworten führen zu Metadaten-Ablehnungen, bei Kinder-Apps zur Entfernung.
5. **2.5.4 Hintergrundmodi** – jeder Eintrag in `UIBackgroundModes` muss durch eine sichtbare Funktion begründet sein. Ein `audio`-Modus „für später" oder `location` ohne Standort-Feature ist ein sicheres Ablehnungskriterium.
6. **2.3.10 Plattformverweise** – Screenshots, Beschreibungen und auch In-App-Texte, die Android, Google Play oder alternative Stores erwähnen, werden ohne Diskussion zurückgewiesen.

## Inhalt

- **2.1 Vollständigkeit** – [2.1(a)](#21a-finale-version-stabilität-demo-zugang) · [2.1(b)](#21b-in-app-käufe-müssen-im-review-funktionieren)
- **2.2** – [Betatests](#22-betatests)
- **2.3 Metadaten** – [2.3.1(a)](#231a-verborgene-funktionen) · [2.3.1(b)](#231b-grobes-fehlverhalten) · [2.3.2](#232-iap-angaben-in-der-beschreibung) · [2.3.3](#233-screenshots) · [2.3.4](#234-app-vorschauen) · [2.3.5](#235-kategorie) · [2.3.6](#236-altersfreigabe) · [2.3.7](#237-name-keywords-metadaten-integrität) · [2.3.8](#238-altersgerechte-metadaten) · [2.3.9](#239-rechte-an-metadaten) · [2.3.10](#2310-plattformfokus) · [2.3.11](#2311-vorbestellungen) · [2.3.12](#2312-neue-funktionen-text) · [2.3.13](#2313-in-app-events)
- **2.4 Hardware** – [2.4.1](#241-iphone-apps-auf-dem-ipad) · [2.4.2](#242-energieeffizienz-und-gerätebelastung) · [2.4.3](#243-apple-tv-eingaben) · [2.4.4](#244-kein-neustart-keine-systemeinstellungs-manipulation) · [2.4.5](#245-mac-app-store)
- **2.5 Software** – [2.5.1](#251-nur-öffentliche-apis-aktuelle-sdks) · [2.5.2](#252-in-sich-geschlossene-bundles-kein-nachladen-von-code) · [2.5.3](#253-schadcode) · [2.5.4](#254-hintergrundmodi-nur-bei-echtem-bedarf) · [2.5.5](#255-ipv6-only) · [2.5.6](#256-browser-müssen-webkit-nutzen) · [2.5.7](#257-entfällt) · [2.5.8](#258-keine-alternativen-home-screens-oder-desktops) · [2.5.9](#259-keine-manipulation-von-standard-ui-elementen) · [2.5.10](#2510-entfällt) · [2.5.11](#2511-sirikit-und-shortcuts) · [2.5.12](#2512-callkit-sms-filter-spam-erkennung) · [2.5.13](#2513-gesichtserkennung) · [2.5.14](#2514-aufzeichnung-von-nutzeraktivität) · [2.5.15](#2515-dateiauswahl-über-system-picker) · [2.5.16](#2516-widgets-erweiterungen-benachrichtigungen-app-clips) · [2.5.17](#2517-matter-unterstützung) · [2.5.18](#2518-display-werbung)
- [Paketreferenz React Native / Expo](#paketreferenz-react-native--expo) · [Kurz-Prüfliste](#kurz-prüfliste-für-diesen-abschnitt)

---

## 2.1 Vollständigkeit der App

### 2.1(a) Finale Version, Stabilität, Demo-Zugang

**Kern der Regel** – Was eingereicht wird, muss die fertige App sein: keine Platzhaltertexte, keine „Coming soon"-Bereiche, keine toten Links, keine Abstürze, keine Testdaten. Alle Backend-Dienste müssen zum Zeitpunkt des Reviews erreichbar sein. Erfordert die App einen Login, gehört ein voll funktionsfähiger Demo-Account (oder ein Demo-Modus) in die Review-Notizen; alles, was der Prüfer nicht auf Anhieb versteht (Hardware-Zubehör, ortsgebundene Funktionen, Firmenkonten), wird dort erklärt oder per Video gezeigt.

**Risikostufe** – Kritisch. Apple lehnt hier automatisiert und ohne Kulanz ab, weil ein Absturz oder ein leerer Screen für den Prüfer das Ende der Prüfung bedeutet. Wiederholte unfertige Einreichungen verlängern die Review-Zeiten für das gesamte Konto.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Strings wie `TODO`, `FIXME`, `Lorem ipsum`, `Placeholder`, `Coming soon`, `Under construction`, `Test`, `Dummy` in Views, Storyboards, `.strings`- und `.xcstrings`-Dateien.
- `fatalError(`, `preconditionFailure(`, `assert(`, `try!`, `as!`, `!`-Unwraps in Pfaden, die zur Laufzeit nur unter Testbedingungen sicher sind.
- Hartkodierte Entwicklungs-Endpunkte: `localhost`, `127.0.0.1`, `192.168.`, `.local`, `staging.`, `dev.`, `ngrok`, `http://` ohne ATS-Ausnahme.
- `#if DEBUG`-Blöcke, deren Gegenstück im Release-Pfad leer ist (Feature existiert nur im Debug-Build).
- `NSAllowsArbitraryLoads = YES` in `Info.plist` – meist ein Indiz für ungeklärte Staging-Umgebungen.

React Native/Expo:
- `__DEV__`-Verzweigungen, in denen der Release-Zweig auf eine nicht existente Funktion zeigt.
- `console.log`, `console.warn` in Masse ohne Babel-Plugin `transform-remove-console` – kein Ablehnungsgrund an sich, aber ein Indikator für Debug-Builds; gelegentlich landen so Tokens im Log.
- `app.json`/`app.config.js`: `expo.updates.url` auf eine Dev-URL, `extra.apiUrl` mit Staging-Adressen, `developmentClient`-Pakete (`expo-dev-client`) im Production-Profil von `eas.json`.

**Typische Verstöße**

❌ Entwicklungs-Endpunkt bleibt im Release-Build:
```swift
let baseURL = URL(string: "http://192.168.1.20:8080/api")!  // nie im Store-Build
```
✅ Konfiguration über Build-Settings/xcconfig:
```swift
let baseURL = URL(string: Bundle.main.infoDictionary?["API_BASE_URL"] as! String)!
```

❌ Feature nur im Debug-Zweig vorhanden:
```js
{__DEV__ ? <ExportScreen /> : <Text>Coming soon</Text>}
```
✅ Feature entweder fertig ausliefern oder den Einstiegspunkt vollständig entfernen.

❌ Login ohne Demo-Zugang in den Review-Notizen bei einer App, die ohne Konto nichts zeigt.
✅ Test-Account mit allen freigeschalteten Rollen plus Hinweis, welche Schritte der Prüfer gehen soll.

❌ Backend antwortet im Review mit `503`, weil Staging über Nacht abgeschaltet wird.
✅ Review-Zeitraum auf produktiven oder dauerhaft laufenden Servern einplanen; IP-Whitelists berücksichtigen, dass Apple aus den USA prüft.

**Prüfliste**
- [ ] Keine Platzhalter-, Test- oder „Bald verfügbar"-Texte in Release-Ressourcen
- [ ] Keine `localhost`/Staging-/`http://`-Endpunkte im Release-Pfad
- [ ] Keine Funktionen, die nur hinter `#if DEBUG` bzw. `__DEV__` existieren
- [ ] Demo-Account bzw. Demo-Modus vorhanden, wenn ein Login nötig ist; Zugangsdaten in den Review-Notizen
- [ ] Hardware-, Standort- oder Firmenabhängigkeiten in den Review-Notizen erklärt (ggf. Video)
- [ ] Netzwerk-Stack funktioniert über IPv6-only (siehe 2.5.5)
- [ ] Crashlogs/Sentry-Daten des letzten TestFlight-Builds gesichtet, keine offenen Crashes

**Empfohlene Behebung** – Umgebungs-Konfiguration über `xcconfig`/Build-Settings bzw. `app.config.js` mit `process.env`/EAS-Secrets; Expo: `expo-constants` für den Zugriff auf `extra`; bare RN: `react-native-config`. Für Debug-Ausgaben `babel-plugin-transform-remove-console` im Production-Build.

### 2.1(b) In-App-Käufe müssen im Review funktionieren

**Kern der Regel** – Alle In-App-Produkte, die zur Einreichung gehören, müssen im Review kaufbar sein. Das heißt: Die Produkte sind in App Store Connect angelegt, dem Build zugeordnet und der Code behandelt die Sandbox-Umgebung korrekt – inklusive Wiederherstellen von Käufen.

**Risikostufe** – Hoch. Ein nicht ladendes Produkt oder ein „Kauf fehlgeschlagen" führt fast immer zur Ablehnung, weil der Prüfer die Bezahlfunktion nicht abnehmen kann.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `StoreKit`/`StoreKit 2`: `Product.products(for:)`, `SKProductsRequest`. Prüfe, ob Produkt-IDs im Code exakt mit denen in App Store Connect übereinstimmen (häufiger Tippfehler-Fall).
- Fehlende Behandlung von `Transaction.updates` bzw. `SKPaymentTransactionObserver`, fehlender `restorePurchases`-Aufruf (`AppStore.sync()`).
- Receipt-Validierung, die nur gegen `buy.itunes.apple.com` geht und den Sandbox-Fallback (`sandbox.itunes.apple.com`, Status 21007) nicht implementiert. Mit StoreKit 2 / App Store Server API ist das Thema meist erledigt, mit älterer Receipt-Validierung nicht.

React Native/Expo:
- `react-native-iap`, `expo-in-app-purchases` (veraltet), `react-native-purchases` (RevenueCat). Prüfe die Produkt-ID-Listen (`getProducts({ skus: [...] })`) und ob `initConnection()` vor dem Laden aufgerufen wird.
- RevenueCat: Prüfe, ob der Offering-Fallback greift, wenn `current` leer ist – sonst zeigt die Paywall im Review nichts an.

**Typische Verstöße**

❌ Produkt-ID-Drift:
```swift
let ids = ["com.firma.app.pro_monthly"]   // in ASC heißt es "pro.monthly"
```
✅ Produkt-IDs zentral definieren und per StoreKit-Konfigurationsdatei lokal testen.

❌ Receipt-Validierung ohne Sandbox-Fallback → im Review schlägt jeder Kauf fehl.
✅ Erst Production prüfen, bei Status 21007 gegen Sandbox wiederholen – oder auf StoreKit 2 wechseln.

**Prüfliste**
- [ ] Produkt-IDs im Code stimmen mit App Store Connect überein
- [ ] Produkte sind dem eingereichten Build zugeordnet (Status „Bereit zur Einreichung")
- [ ] Kauf, Wiederherstellen und Abo-Verwaltung sind im Sandbox-Modus getestet
- [ ] Serverseitige Validierung fällt auf Sandbox zurück (bei App-Receipts)
- [ ] Paywall zeigt auch ohne Netzwerk-Cache Produkte an (Offering-Fallback)

**Empfohlene Behebung** – StoreKit 2 mit `Transaction.currentEntitlements`; Expo/RN: `react-native-purchases` (RevenueCat) oder `react-native-iap` mit `StoreKit`-Testkonfiguration in Xcode.

---

## 2.2 Betatests

**Kern der Regel** – Der App Store ist kein Testkanal. Demos, Betas und „Early Access"-Builds gehören in TestFlight. TestFlight-Builds müssen die Guidelines ebenfalls einhalten, dürfen nur für die Prüfung der App verteilt werden und dürfen nicht an Bedingungen geknüpft sein – insbesondere darf niemand für das Testen bezahlt werden und eine TestFlight-Verteilung darf kein Ersatz für den Vertrieb sein.

**Risikostufe** – Mittel. Apple lehnt Store-Einreichungen mit „Beta"-Bezeichnung ab; TestFlight-Missbrauch (z. B. Verkauf von Beta-Zugängen) kann zur Kontosperre führen.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `CFBundleDisplayName`, `CFBundleName` oder Marketing-Strings mit `Beta`, `Alpha`, `RC`, `Preview`, `Nightly`, `Test`.
- App-Icons mit Beta-Badges in `Assets.xcassets`.
- In-App-Hinweise wie „Dies ist eine Testversion".

React Native/Expo:
- `app.json`: `expo.name` oder `ios.bundleIdentifier` mit `-beta`, `-staging`, `-dev`; `expo.version` wie `0.9.0-beta.3`.
- `eas.json`: Production-Profil, das auf ein `preview`-Channel zeigt.

**Typische Verstöße**

❌ `"name": "MeineApp Beta"` in `app.json` beim Store-Build.
✅ Beta-Bezeichnung nur im TestFlight-Build-Namen bzw. über ein separates EAS-Profil.

❌ Onboarding-Screen: „Danke, dass du unsere Beta testest!"
✅ Text entfernen oder an ein TestFlight-spezifisches Flag binden (Prüfung über den Receipt-Pfad `sandboxReceipt` oder `Bundle.main.appStoreReceiptURL`).

**Prüfliste**
- [ ] Keine Beta-/Alpha-/Test-Bezeichnungen in Name, Icon, Version oder In-App-Texten des Store-Builds
- [ ] TestFlight wird nicht als Vertriebs- oder Bezahlkanal genutzt
- [ ] Beta-Feedback-Funktionen (Shake-to-Report, Debug-Menü) im Store-Build deaktiviert

**Empfohlene Behebung** – Getrennte Build-Profile: Expo `eas.json` mit `preview` (TestFlight) und `production` (Store); bare RN/Xcode: eigene Scheme + Configuration mit unterschiedlichem `CFBundleDisplayName`.

---

## 2.3 Korrekte Metadaten

Metadaten-Verstöße blockieren zwar keinen Code, aber sie kosten Review-Runden. Apple markiert viele dieser Punkte als Kandidaten für Ablehnung ohne Nachbesserung des Binaries – also als reine Store-Connect-Änderung. Der Agent kann hier hauptsächlich Konfigurationsdateien, Strings und Assets prüfen und sollte die Store-Texte anfordern, wenn sie im Repository nicht liegen (z. B. `fastlane/metadata/`).

### 2.3.1(a) Verborgene Funktionen

**Kern der Regel** – Die App darf keine Funktionen enthalten, die dem Prüfer verborgen bleiben oder erst nach der Freigabe aktiviert werden. Alles, was die App kann, muss beschrieben und im Review sichtbar sein. Nicht offensichtliche Funktionen erklärt man in den Review-Notizen.

**Risikostufe** – Kritisch. Apple betrachtet versteckte Funktionalität als Täuschung; Feature-Flags, die im Review „aus" und danach „an" sind, führen zur Ablehnung und bei Wiederholung zur Kontosperre.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Remote-Config-Abfragen, deren Flags im Review alles Kritische abschalten: Firebase `RemoteConfig`, LaunchDarkly, eigene `/feature-flags`-Endpunkte. Suche nach Namen wie `isReviewMode`, `appleReview`, `hideForReview`, `isUnderReview`, `reviewerMode`.
- Datumsgebundene Freischaltungen: `Date() > releaseDate`, `if Calendar.current.isDate(...)`.
- Geofencing gegen Cupertino oder IP-basierte Abfragen der Region als Schalter.
- Geheime Gesten: `UILongPressGestureRecognizer` mit hoher Tap-Zahl, Shake-Events, versteckte Debug-Menüs, die Produktivfunktionen freischalten.

React Native/Expo:
- Gleiche Muster in JS: `remoteConfig().getValue('review_mode')`, `Constants.expoConfig.extra.reviewMode`, `if (Platform.OS === 'ios' && isReview)`.
- OTA-Updates, die nach der Freigabe neue Screens einspielen (siehe 2.5.2).

**Typische Verstöße**

❌
```js
const showCasino = !(await remoteConfig().getValue('apple_review').asBoolean());
```
✅ Funktionen sind entweder in der eingereichten Fassung sichtbar oder nicht Teil der App.

❌ Zeitgesteuerte Freischaltung eines Krypto-Handels-Tabs am Tag nach dem geplanten Release.
✅ Neue Funktion in einem eigenen Update einreichen.

**Prüfliste**
- [ ] Keine Feature-Flags, die auf Review-Status, Datum, Region oder Prüfer-IP reagieren
- [ ] Keine geheimen Gesten oder Debug-Menüs, die Produktivfunktionen freischalten
- [ ] Alle Funktionen sind mit den Review-Notizen und der Beschreibung abgleichbar

**Empfohlene Behebung** – Feature-Flags nur für schrittweise Rollouts freigegebener Funktionen einsetzen; unfertige Features vollständig aus dem Bundle entfernen.

### 2.3.1(b) Grobes Fehlverhalten

**Kern der Regel** – Wer Apple absichtlich täuscht – gefälschte Bewertungen, manipulierte Metadaten, bewusst falsche Angaben zur Funktion – muss mit Entfernung der App und Kündigung des Entwicklerkontos rechnen. Das gilt auch für Agenturen, die im Namen von Kunden einreichen.

**Risikostufe** – Kritisch. Hier gibt es keine zweite Chance; Apple handelt auf Kontoebene.

**Woran du es im Code erkennst**
- Bewertungs-Aufforderungen, die nur bei positiver Vorabfrage zu `SKStoreReviewController` bzw. `requestReview()` führen („Gefällt dir die App? Ja → Bewertung, Nein → Feedback-Formular") – ein Grenzfall, der 2026 zunehmend beanstandet wird.
- Incentivierte Bewertungen: Strings wie „Bewerte uns und erhalte 100 Coins".
- Expo: `expo-store-review` oder `react-native-rate` mit vorgeschalteter Stimmungsabfrage.

**Prüfliste**
- [ ] Keine Belohnung für Bewertungen
- [ ] Bewertungs-Dialog nur über die System-API, ohne Vorfilterung nach Stimmung
- [ ] Keine erfundenen Auszeichnungen oder Presse-Zitate in App oder Metadaten

### 2.3.2 IAP-Angaben in der Beschreibung

**Kern der Regel** – Enthält die App In-App-Käufe, muss das aus Beschreibung, Screenshots und Vorschauen klar hervorgehen. Nutzer dürfen nicht erst nach der Installation erfahren, dass die beworbene Hauptfunktion kostenpflichtig ist. Auf Preisangaben in Screenshots oder Texten sollte man verzichten, weil sie regional abweichen.

**Risikostufe** – Mittel. Wird meist als Metadaten-Korrektur angemahnt, kostet aber eine Review-Runde.

**Woran du es im Code erkennst**
- StoreKit-Nutzung im Code, aber keine Erwähnung von Käufen in `fastlane/metadata/*/description.txt` oder den Store-Texten.
- Screenshots (`fastlane/screenshots/`, Marketing-Ordner), die Pro-Funktionen ohne Hinweis zeigen.
- Hartkodierte Preise in Strings (`"nur 4,99 €"`) statt `product.displayPrice`.

**Prüfliste**
- [ ] Beschreibung nennt In-App-Käufe/Abos und ihren Umfang
- [ ] Screenshots/Vorschauen kennzeichnen kostenpflichtige Funktionen
- [ ] Preise kommen zur Laufzeit aus StoreKit (lokalisiert), nicht aus Strings

### 2.3.3 Screenshots

**Kern der Regel** – Screenshots zeigen die App in Benutzung, nicht nur Splash-Screen, Logo oder Login. Erklärende Overlays und Rahmen sind erlaubt, solange die eigentliche App-Oberfläche erkennbar bleibt. Für jede unterstützte Gerätekasse gehören passende Screenshots dazu; Screenshots dürfen keine Funktionen zeigen, die die App nicht hat.

**Risikostufe** – Mittel.

**Prüfliste**
- [ ] Screenshots zeigen echte App-Screens, nicht nur Marketing-Grafik
- [ ] iPad-Screenshots vorhanden, wenn die App auf dem iPad läuft (praktisch immer, siehe 2.4.1)
- [ ] Keine Geräte-Rahmen fremder Hersteller, keine Android-Statusleisten (siehe 2.3.10)
- [ ] Screenshots entsprechen der eingereichten Version (keine alten UI-Stände)

### 2.3.4 App-Vorschauen

**Kern der Regel** – Vorschau-Videos bestehen aus Bildschirmaufnahmen der App selbst. Sprecherstimme und Texteinblendungen sind erlaubt; Live-Action-Material, Hände, Schauspieler oder Aufnahmen fremder Geräte nicht (Ausnahme: iMessage-Erweiterungen dürfen die Nachrichten-App zeigen).

**Risikostufe** – Mittel.

**Prüfliste**
- [ ] Vorschauen bestehen aus Screen-Recordings der App
- [ ] Keine Fremdgeräte, Hände oder Realfilm-Szenen
- [ ] Gezeigte Inhalte entsprechen der Altersfreigabe (siehe 2.3.8)

### 2.3.5 Kategorie

**Kern der Regel** – Die Kategorie muss zum Kern der App passen. Apple darf die Kategorie korrigieren; eine bewusst „günstige" Kategorie für bessere Chart-Platzierungen ist ein Verstoß.

**Risikostufe** – Niedrig.

**Woran du es im Code erkennst**
- `LSApplicationCategoryType` in `Info.plist` (macOS/Catalyst) – muss zur Store-Kategorie passen.
- Expo: keine Entsprechung in `app.json`; Kategorie wird in App Store Connect gesetzt.

**Prüfliste**
- [ ] Primäre Kategorie beschreibt die Hauptfunktion
- [ ] Bei Kinder-Apps: Kids-Kategorie mit allen Folgeverpflichtungen (Abschnitt 1.3, 5.1.4)
- [ ] `LSApplicationCategoryType` (falls vorhanden) stimmt mit der Store-Kategorie überein

### 2.3.6 Altersfreigabe

**Kern der Regel** – Die Altersfreigabe entsteht aus dem Fragebogen in App Store Connect und muss die Realität der App widerspiegeln, damit Kindersicherung und regionale Jugendschutzregeln greifen. Seit 2025 gilt das erweiterte Stufenmodell 4+, 9+, 13+, 16+, 18+. 2026 hat Apple den Fragebogen um Fragen zu Social-Media-Funktionen ergänzt: nutzergenerierte Inhalte, Direktnachrichten, Kontakt zu Fremden, Live-Streams, algorithmische Feeds und ob es Schutzmechanismen (Meldefunktion, Blockieren, Moderation) gibt. Diese Fragen müssen ab September 2026 für jede neue Einreichung beantwortet sein; unbeantwortete Fragebögen blockieren den Upload. Zusätzlich verlangen einzelne Länder eigene Angaben – für Südkorea sind 2026 die Regeln zur Altersverifikation und zu Kennzeichnungen für Glücksspiel-ähnliche Mechaniken verschärft worden, was einen separaten Korea-Abschnitt im Fragebogen nach sich zieht.

**Risikostufe** – Hoch. Eine zu niedrige Einstufung wird spätestens beim Review der Funktionen entdeckt; bei Kinder-Apps oder Lootbox-Mechaniken führt sie zur Entfernung. Fehlende Korea-Angaben blockieren die Verfügbarkeit in diesem Store.

**Woran du es im Code erkennst**

Swift/Objective-C und RN/Expo gleichermaßen – hier zählt die tatsächliche Funktion:
- UGC-Indikatoren: Upload-Endpunkte, `UIImagePickerController`/`PHPickerViewController` mit Server-Upload, Kommentar-/Chat-Module (`MessageKit`, `Stream Chat`, `Sendbird`, `react-native-gifted-chat`), WebSocket-Chats.
- Kontakt-zu-Fremden-Indikatoren: Nutzerprofile mit Suche, Matching-Logik, öffentliche Freundeslisten.
- Live-Streaming: `HaishinKit`, `Agora`, `LiveKit`, `react-native-agora`, `react-native-webrtc`.
- Glücksspiel-Mechaniken: Zufalls-Belohnungen (`Int.random`, `Math.random` in Loot-Logik), Wahrscheinlichkeitstabellen, Gacha-Begriffe.
- Werbe-SDKs ohne Altersfilter (siehe 2.5.18): `GADMobileAds`, `AppLovin`, `IronSource` – bei Freigabe 4+/9+ muss `tagForChildDirectedTreatment` bzw. der Alters-Flag gesetzt sein.
- Kindersicherung im Code: `Family Controls`, `ManagedSettings`, `DeviceActivity` – bei Kinder-Apps ein Pluspunkt, kein Ersatz für korrekte Einstufung.
- Medizinische/Substanz-Inhalte: Strings zu Alkohol, Tabak, Cannabis, Waffen in Content-Datenbanken.

**Typische Verstöße**

❌ Chat- und Bildupload-Funktion vorhanden, Fragebogen sagt „keine nutzergenerierten Inhalte" → Einstufung 4+ statt 13+/16+.
✅ Fragebogen ehrlich beantworten, Melde- und Blockierfunktion einbauen (Abschnitt 1.2) und Einstufung entsprechend anheben.

❌ Lootbox-System ohne Wahrscheinlichkeitsanzeige, Korea-Fragen nicht beantwortet.
✅ Wahrscheinlichkeiten anzeigen (Abschnitt 3.1.1) und den Korea-Abschnitt im Fragebogen ausfüllen.

**Prüfliste**
- [ ] Fragebogen inklusive der neuen Social-Media-Fragen (UGC, Nachrichten, Fremdkontakt, Live-Stream, Feeds, Schutzmechanismen) beantwortet
- [ ] Einstufung deckt Chat, UGC, Werbung, Zufallsmechaniken und externe Web-Inhalte ab
- [ ] Korea-spezifische Angaben (Altersverifikation, Glücksspiel-Kennzeichnung) ausgefüllt, wenn die App dort verfügbar ist
- [ ] Werbe-SDKs auf altersgerechte Auslieferung konfiguriert
- [ ] Bei uneingeschränktem Web-Zugriff (`WKWebView` mit freier URL-Eingabe): Freigabe 18+ oder Einschränkung

**Empfohlene Behebung** – Funktionsinventar der App gegen den Fragebogen abgleichen; Ergebnis in den Review-Notizen begründen. Bei UGC: Melde-, Block- und Moderationspfade nachweisbar implementieren.

### 2.3.7 Name, Keywords, Metadaten-Integrität

**Kern der Regel** – Der App-Name (max. 30 Zeichen) muss eindeutig sein und darf keine Preise, Markennamen Dritter, Konkurrenz-App-Namen, Kategoriebegriffe oder Keyword-Ketten enthalten. Keywords müssen zur App passen; Untertitel und Werbetexte dürfen keine anderen Apps referenzieren. Icons, die im Bundle stecken, müssen zu den Store-Icons passen; Doppel-Einreichungen derselben App unter verschiedenen Namen sind untersagt.

**Risikostufe** – Mittel bis Hoch. Markennamen im Titel (z. B. „für WhatsApp", „Instagram Downloader") führen zuverlässig zur Ablehnung; Duplikat-Apps zur Sperre (siehe auch 4.3 Spam).

**Woran du es im Code erkennst**
- `CFBundleDisplayName` länger als 30 Zeichen oder mit Zusätzen wie `– kostenlos`, `Pro`, `Best`, `#1`.
- Fremdmarken in `CFBundleDisplayName`, `CFBundleName`, `app.json` → `expo.name`, Slug, Bundle-ID (`com.firma.instagramdownloader`).
- Mehrere App-Targets mit identischem Code und nur anderem Namen/Farbe (White-Label ohne echten Unterschied).
- `fastlane/metadata/*/keywords.txt` mit Konkurrenznamen oder Kategoriebegriffen wie „app", „kostenlos".

**Typische Verstöße**

❌ `"name": "Tracker für Instagram Follower – kostenlos & schnell"`
✅ `"name": "FollowStats"` – Fremdmarke höchstens beschreibend in der Beschreibung, nicht im Namen.

❌ Keywords: `whatsapp, telegram, signal, messenger, bester chat`
✅ Keywords, die die eigene Funktion beschreiben.

**Prüfliste**
- [ ] Name ≤ 30 Zeichen, ohne Fremdmarken, Preise, Kategorie-Füllwörter
- [ ] Keine Konkurrenznamen in Keywords, Untertitel, Werbetext
- [ ] Bundle-Icon und Store-Icon identisch
- [ ] Keine Duplikat-Targets ohne substanziellen Unterschied

### 2.3.8 Altersgerechte Metadaten

**Kern der Regel** – Icon, Screenshots und Vorschauen müssen für jedes Publikum unbedenklich sein (Maßstab 4+), auch wenn die App selbst höher eingestuft ist. Formulierungen wie „für Kinder" sind der Kids-Kategorie vorbehalten.

**Risikostufe** – Mittel.

**Prüfliste**
- [ ] Keine Gewalt-, Sex-, Drogen- oder Waffen-Darstellungen in Icon, Screenshots, Vorschauen
- [ ] „Für Kinder"/„for Kids" nur bei Apps in der Kids-Kategorie
- [ ] Alternative App-Icons im Bundle (`CFBundleAlternateIcons`) ebenfalls 4+-tauglich

### 2.3.9 Rechte an Metadaten

**Kern der Regel** – Alles, was in Icon, Screenshots, Vorschauen und Texten erscheint, muss lizenziert sein. Personenbezogene Daten in Screenshots gehören fiktiven Personen; echte Profile, Namen oder Fotos ohne Einwilligung sind tabu.

**Risikostufe** – Mittel; bei Markenbeschwerden Hoch.

**Woran du es im Code erkennst**
- Screenshot-Fixtures (`fastlane/screenshots`, Storybook-/Snapshot-Daten) mit echten Namen, E-Mail-Adressen, Telefonnummern.
- Bundle-Assets mit Logos Dritter (`apple_logo.png`, `google.png` außerhalb der offiziellen Sign-in-Buttons), Stockfotos ohne Lizenz-Hinweis im Repo.

**Prüfliste**
- [ ] Screenshot-Daten sind fiktiv
- [ ] Lizenzen für Fotos, Icons, Schriften und Musik in Vorschauen liegen vor
- [ ] Keine Fremdlogos außerhalb der zulässigen Marken-Buttons (Sign in with Apple/Google usw.)

### 2.3.10 Plattformfokus

**Kern der Regel** – Metadaten und App bleiben bei Apples Plattformen. Verweise auf Android, Google Play, Windows, alternative Marktplätze oder fremde Gerätemarken sind nicht erlaubt – weder in Texten noch in Screenshots noch in In-App-Hinweisen wie „Auch für Android verfügbar". Ausnahme sind echte plattformübergreifende Funktionen (z. B. Chat mit Android-Nutzern), sofern das für die Funktion nötig ist.

**Risikostufe** – Hoch. Die Ablehnung erfolgt ohne Interpretationsspielraum und ist bei Cross-Platform-Projekten der häufigste Metadaten-Fehler.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Strings mit `Android`, `Google Play`, `Play Store`, `Galaxy`, `Windows Phone`, `APK`, `Sideload`, `F-Droid`, `Huawei AppGallery` in `.strings`, `.xcstrings`, Storyboards, Onboarding-Texten, Hilfeseiten, Footer-Links.

React Native/Expo (besonders anfällig, weil Texte geteilt werden):
- Gemeinsame i18n-Dateien (`locales/de.json`) mit Android-Hinweisen, die auf iOS nicht per `Platform.select` ausgeblendet sind.
- `Platform.OS === 'android'`-Zweige sind in Ordnung; problematisch sind Texte, die im iOS-Pfad ankommen: „Aktiviere Benachrichtigungen in den Android-Einstellungen".
- Marketing-Komponenten mit Play-Store-Badge (`google-play-badge.png`) ohne Plattform-Weiche.

**Typische Verstöße**

❌
```json
{ "onboarding.sync": "Deine Daten werden mit der Android-App synchronisiert." }
```
✅
```json
{ "onboarding.sync": "Deine Daten werden auf allen deinen Geräten synchronisiert." }
```

❌ Screenshot mit Android-Statusleiste (drei Navigations-Tasten unten) im iOS-Store.
✅ Screenshots auf iOS-Simulator oder Gerät erzeugen.

**Prüfliste**
- [ ] Keine Android-/Play-Store-/Fremdmarken-Strings im iOS-Pfad
- [ ] Geteilte i18n-Ressourcen per `Platform.select`/`.ios.js`-Dateien getrennt
- [ ] Keine fremden Store-Badges in Bundle-Assets oder eingebetteten Web-Views
- [ ] Screenshots/Vorschauen zeigen ausschließlich Apple-Geräte

**Empfohlene Behebung** – Plattformspezifische String-Dateien (`de.ios.json`), `Platform.select()` für Texte, Sichtprüfung eingebetteter Web-Inhalte mit einem iOS-User-Agent.

### 2.3.11 Vorbestellungen

**Kern der Regel** – Wer die App zur Vorbestellung anbietet, muss die vollständige, beworbene App zum angekündigten Termin liefern. Ändert sich die App bis dahin wesentlich (Funktion, Preis, Umfang), muss die Vorbestellung neu gestartet werden, damit Kunden entscheiden können.

**Risikostufe** – Mittel.

**Prüfliste**
- [ ] Der zur Vorbestellung eingereichte Build ist vollständig (kein „Vorschau"-Build)
- [ ] Beschreibung, Preis und Kernfunktionen bleiben bis zum Release stabil
- [ ] Bei wesentlichen Änderungen: Vorbestellung neu aufsetzen

### 2.3.12 „Neue Funktionen"-Text

**Kern der Regel** – Der „Neue Funktionen"-Text beschreibt konkret, was sich im Update ändert. Nichtssagende Standardtexte („Bug fixes and improvements") sind nur akzeptabel, wenn es tatsächlich nur um Fehlerbehebungen geht. Der Text darf nichts erwähnen, was im Build nicht enthalten ist.

**Risikostufe** – Niedrig. Wird meist bei größeren Updates angemahnt, wenn Release-Notes und Binary auseinanderlaufen.

**Woran du es im Code erkennst**
- `fastlane/metadata/*/release_notes.txt` bzw. `CHANGELOG.md` gegen den tatsächlichen Diff abgleichen.
- Generische Automatismen, die jede Version mit demselben Text füllen (`changelog: "Improvements"` in `Fastfile`/EAS-Submit-Konfiguration).

**Prüfliste**
- [ ] Release-Notes nennen die tatsächlichen Änderungen
- [ ] Keine Ankündigung von Funktionen, die per OTA nachgeschoben werden sollen
- [ ] Bei reinem Bugfix-Update ist ein Standardtext zulässig

### 2.3.13 In-App-Events

**Kern der Regel** – In-App-Events in App Store Connect müssen dem angegebenen Ereignistyp entsprechen (Challenge, Live-Event, Premiere usw.), zutreffende Metadaten haben, Monetarisierung nach Abschnitt 3 abwickeln und über Deep Links direkt zum Ereignis in der App führen – nicht zur Startseite oder in ein Login ohne Kontext.

**Risikostufe** – Niedrig bis Mittel.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Universal Links: `applinks:`-Entitlement, `apple-app-site-association`, Behandlung in `application(_:continue:restorationHandler:)` oder `.onOpenURL`. Prüfe, ob der Event-Pfad geroutet wird.

React Native/Expo:
- `expo-linking`/`expo-router`-Routen; `Linking.getInitialURL()`-Behandlung; `app.json` → `ios.associatedDomains`. Fehlender Routen-Eintrag für den Event-Link ist der typische Fehler.

**Prüfliste**
- [ ] Deep Link des Events führt direkt zum Event-Inhalt
- [ ] Ereignistyp, Beschreibung und Bilder entsprechen dem Event
- [ ] Kostenpflichtige Event-Inhalte laufen über In-App-Kauf (Abschnitt 3)

---

## 2.4 Hardware-Kompatibilität

### 2.4.1 iPhone-Apps auf dem iPad

**Kern der Regel** – Eine iPhone-App soll wann immer möglich auch auf dem iPad laufen – im Kompatibilitätsmodus oder besser nativ. Apple prüft standardmäßig auf beiden Gerätekategorien; für die Fassung 2026 sind die Referenzgeräte des Reviews ein iPad Air 11" (M3) und ein iPhone 17 Pro Max. Eine App, die nur auf dem iPhone-Target gebaut ist, wird auf dem iPad im Kompatibilitätsmodus getestet und muss dort bedienbar bleiben.

**Risikostufe** – Hoch. Ein Absturz oder unbedienbares Layout auf dem iPad zählt als 2.1(a)-Ablehnung.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `TARGETED_DEVICE_FAMILY = 1` (nur iPhone) im `project.pbxproj` – erlaubt, aber dann greift der Kompatibilitätsmodus; prüfe UI-Code auf feste Breiten (`UIScreen.main.bounds.width == 390`-Logik).
- `UIRequiredDeviceCapabilities` mit Werten, die iPads ausschließen (`telephony`, `sms`) – nur zulässig, wenn die Funktion tatsächlich zwingend ist.
- Popover-APIs (`UIPopoverPresentationController`) ohne `sourceView`/`barButtonItem` → Absturz auf iPad bei `UIActivityViewController`, `UIAlertController` mit `.actionSheet`.

React Native/Expo:
- `app.json` → `ios.supportsTablet: false` (iPhone-only, Kompatibilitätsmodus) – erlaubt, aber testen.
- Share-Dialoge (`Share.share()`, `expo-sharing`) ohne iPad-Anker-Position (`anchor`-Option) → Crash auf iPad.
- Layouts mit `Dimensions.get('window')` einmalig beim Import statt `useWindowDimensions()` → falsche Größen nach Split View/Rotation.

**Typische Verstöße**

❌ ActionSheet ohne Popover-Anker (stürzt auf iPad ab):
```swift
let sheet = UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)
present(sheet, animated: true)
```
✅
```swift
sheet.popoverPresentationController?.sourceView = button
sheet.popoverPresentationController?.sourceRect = button.bounds
present(sheet, animated: true)
```

❌ `ios.supportsTablet: true` in Expo, aber alle Screens mit fixen 390-pt-Breiten → verzerrte Darstellung auf dem iPad Air 11".
✅ `useWindowDimensions()`/Flexbox verwenden und im iPad-Simulator (11" und 13") testen.

**Prüfliste**
- [ ] App startet und ist auf iPad (11" M3-Referenz) bedienbar – nativ oder im Kompatibilitätsmodus
- [ ] Keine ausschließenden `UIRequiredDeviceCapabilities` ohne zwingenden Grund
- [ ] ActionSheets/Share-Dialoge mit Popover-Anker
- [ ] Rotation und Split View (falls unterstützt) ohne Layout-Bruch
- [ ] iPad-Screenshots eingereicht, wenn `supportsTablet`/Device Family 1,2

**Empfohlene Behebung** – SwiftUI-Layouts mit Size Classes; RN: `useWindowDimensions`, `react-native-safe-area-context`; Expo: `ios.supportsTablet` bewusst setzen und iPad-Build vor Einreichung testen.

### 2.4.2 Energieeffizienz und Gerätebelastung

**Kern der Regel** – Apps dürfen das Gerät nicht unnötig belasten: kein schneller Akkuverbrauch, keine Hitzeentwicklung, keine übermäßige Beanspruchung von CPU, GPU oder Speicher. Kryptowährungs-Mining auf dem Gerät ist ausdrücklich verboten. Hintergrundprozesse, die nichts mit der sichtbaren Funktion zu tun haben (auch aus Werbe-SDKs), sind nicht erlaubt.

**Risikostufe** – Hoch für Mining und verdeckte Hintergrundlast (Entfernung); Mittel für ineffiziente Implementierungen (Ablehnung mit Nachbesserung).

**Woran du es im Code erkennst**

Swift/Objective-C:
- Mining-Bibliotheken oder Hashing-Schleifen: `xmrig`, `cryptonight`, `randomx`, `stratum+tcp`, `hashrate`, `nonce`-Schleifen in Endlosschleifen.
- Timer mit sehr kurzen Intervallen ohne Abbruch: `Timer.scheduledTimer(withTimeInterval: 0.01, repeats: true)`, `CADisplayLink` ohne `invalidate()`.
- `CLLocationManager` mit `kCLLocationAccuracyBestForNavigation` und `allowsBackgroundLocationUpdates = true` in Apps ohne Navigationsfunktion; fehlendes `pausesLocationUpdatesAutomatically`.
- `UIApplication.shared.isIdleTimerDisabled = true` global gesetzt.
- Endlos-Audiowiedergabe ohne Ton (Stille-Track), um den `audio`-Hintergrundmodus wach zu halten.

React Native/Expo:
- `setInterval` mit Intervallen unter 100 ms ohne Cleanup im `useEffect`-Return.
- `expo-location`: `Location.startLocationUpdatesAsync` mit `Accuracy.BestForNavigation` in einer Nicht-Navigations-App.
- `expo-keep-awake` / `react-native-keep-awake` dauerhaft aktiv statt nur im relevanten Screen.
- `react-native-background-actions`, `react-native-background-fetch` mit aggressiven Intervallen ohne fachlichen Grund.

**Typische Verstöße**

❌
```js
useEffect(() => { setInterval(pollServer, 50); }, []);   // kein Cleanup, 20×/s
```
✅
```js
useEffect(() => { const id = setInterval(pollServer, 30000); return () => clearInterval(id); }, []);
```

❌ Stiller Audio-Loop, um im Hintergrund Standortdaten zu senden.
✅ Entweder echte Audio-Funktion oder korrekten `location`-Hintergrundmodus mit Nutzeraufklärung (2.5.4, 5.1.1).

**Prüfliste**
- [ ] Kein Mining, keine Hash-Berechnung fremder Netzwerke
- [ ] Timer, Display-Links und Polling mit Cleanup und sinnvollen Intervallen
- [ ] Standort-Genauigkeit und Hintergrund-Updates auf das Nötige beschränkt
- [ ] Render-Loops stoppen im Hintergrund
- [ ] Keep-Awake nur in Screens, die es brauchen
- [ ] Werbe-SDKs starten keine eigenen Hintergrunddienste

**Empfohlene Behebung** – `BGTaskScheduler` statt Dauer-Timer; Expo `expo-background-task` (ersetzt `expo-background-fetch`) für periodische Arbeit; `expo-location` mit `Accuracy.Balanced` und `deferredUpdates`.

### 2.4.3 Apple-TV-Eingaben

**Kern der Regel** – tvOS-Apps müssen mit der Siri Remote (bzw. dem Apple TV Remote in der Fernbedienungs-App) vollständig bedienbar sein. Game-Controller dürfen zusätzliche Funktionen freischalten; wer einen Controller zwingend voraussetzt, muss das in App und Metadaten deutlich machen.

**Risikostufe** – Mittel (nur tvOS).

**Woran du es im Code erkennst**
- `GCSupportsControllerUserInteraction = YES` und `GCRequiresControllerUserInteraction = YES` in `Info.plist` → Controller-Pflicht muss beschrieben sein.
- Fokus-Engine: Custom Views ohne `canBecomeFocused`/`focusable`, Gesten nur über `UITapGestureRecognizer` statt `UIPressesEvent`/`UIFocus`.
- React Native tvOS (`react-native-tvos`): `TVEventHandler` vorhanden? `hasTVPreferredFocus` bei Startelementen? Touchables ohne `isTVSelectable`.

**Prüfliste**
- [ ] Alle Funktionen per Siri Remote erreichbar (Fokus-Navigation, Menü-Taste)
- [ ] Controller-Pflicht (falls vorhanden) in Metadaten und beim Start kommuniziert
- [ ] Kein Touch-only-Interface im tvOS-Target

### 2.4.4 Kein Neustart, keine Systemeinstellungs-Manipulation

**Kern der Regel** – Eine App darf den Nutzer weder zum Neustart des Geräts auffordern noch ihn dazu bringen, Systemeinstellungen zu ändern, die nichts mit der Kernfunktion zu tun haben (z. B. WLAN, VPN, Bildschirmzeit, Zugänglichkeitsfunktionen abschalten). Berechtigungsdialoge und der Sprung zu den eigenen App-Einstellungen sind natürlich erlaubt.

**Risikostufe** – Mittel.

**Woran du es im Code erkennst**
- Strings: „Starte dein iPhone neu", „Reboot", „Restart your device", „Deaktiviere VPN", „Schalte Low Power Mode aus".
- Öffnen von Settings-URLs außerhalb des eigenen Bereichs: `App-Prefs:` / `prefs:root=` (private URL-Schemata, zusätzlich ein 2.5.1-Verstoß). Erlaubt ist nur `UIApplication.openSettingsURLString` bzw. RN `Linking.openSettings()`.
- Expo: `expo-intent-launcher` ist Android-only; iOS-Code, der `Linking.openURL('App-Prefs:root=WIFI')` versucht.

**Typische Verstöße**

❌
```swift
UIApplication.shared.open(URL(string: "App-Prefs:root=WIFI")!)
```
✅
```swift
UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)
```

**Prüfliste**
- [ ] Keine Neustart-Aufforderungen
- [ ] Keine `App-Prefs:`/`prefs:`-URLs
- [ ] Keine Aufforderung, systemweite Funktionen (VPN, Stromsparmodus, Bildschirmzeit) zu ändern

### 2.4.5 Mac App Store

**Kern der Regel** – Für macOS gelten neun Zusatzregeln, die alle darauf zielen, dass eine Mac-App-Store-App sich wie eine sandboxed, selbst enthaltene, vom Store verwaltete App verhält. Die Regeln im Einzelnen:

- **(i) Sandbox** – App Sandbox ist Pflicht; Zugriff auf Nutzerdaten nur über die vorgesehenen APIs (Security-Scoped Bookmarks, Contacts-/EventKit-Framework), keine direkten Zugriffe auf `~/Library` fremder Apps.
- **(ii) Paketierung** – Gebaut, signiert und eingereicht mit Xcode-Werkzeugen; keine Drittanbieter-Installer, kein Ablegen von Dateien an geteilten Orten, ein einziges App-Bundle.
- **(iii) Autostart** – Kein Login-Item, kein Launch-Agent, kein Daemon ohne ausdrückliche Zustimmung; nach dem Beenden laufen keine Prozesse weiter; keine ungefragten Dock-Icons oder Desktop-Verknüpfungen.
- **(iv) Code-Nachinstallation** – Keine Nachinstallation von Apps, Kernel-Erweiterungen, Plugins oder Code, die den Funktionsumfang wesentlich verändern.
- **(v) Rechteausweitung** – Kein Root, kein `setuid`, keine Privileged Helper Tools, die Root-Rechte anfordern.
- **(vi) Lizenzierung** – Keine Lizenzschlüssel, keine Aktivierungsdialoge, kein Kopierschutz außerhalb des App-Store-Receipts.
- **(vii) Updates** – Updates ausschließlich über den Mac App Store; kein Sparkle, kein eigener Updater.
- **(viii) OS-Kompatibilität** – Läuft auf der aktuellen macOS-Version; keine Abhängigkeit von optionalen oder abgekündigten Technologien (Java, Rosetta als Pflicht).
- **(ix) Lokalisierung** – Alle Sprachen in einem Bundle; keine Sprachpakete zum Nachladen.

**Risikostufe** – Hoch. Die Sandbox-Prüfung ist automatisiert; Updater und Lizenzschlüssel werden im manuellen Review sofort erkannt.

**Woran du es im Code erkennst**

Swift/Objective-C (macOS, Catalyst, SwiftUI-Multiplattform):
- (i) `.entitlements`: `com.apple.security.app-sandbox` fehlt oder ist `false`; Zugriff auf `~/Library/Application Support/<fremde App>`; fehlende `com.apple.security.files.user-selected.read-write` bei Dateidialogen.
- (ii) `pkgbuild`/`productbuild`-Skripte, `.pkg`/`.dmg`-Ziele im Build-Prozess für den Store-Build; `/Library/`-Kopien im Post-Install.
- (iii) `SMAppService.loginItem`/`SMLoginItemSetEnabled` beim ersten Start ohne Opt-in; `LaunchAgents`-Plists im Bundle; `NSWorkspace`-Autostart-Tricks.
- (iv) `dlopen` auf Pfade außerhalb des Bundles, `Bundle(path:).load()` für heruntergeladene Plugins, `kext`-Dateien, `SystemExtensions` ohne Notwendigkeit.
- (v) `AuthorizationExecuteWithPrivileges`, `SMJobBless`, `setuid`-Bits, `sudo`-Aufrufe über `Process`.
- (vi) Strings `License Key`, `Serial`, `Activate`, `Trial expired`; Bibliotheken wie `Paddle`, `DevMate`, `Keygen`, `LicenseSpring`.
- (vii) `Sparkle.framework`, `SUFeedURL` in `Info.plist`, `SUUpdater`, eigene `checkForUpdates`-Endpunkte, `appcast.xml`.
- (viii) `LSMinimumSystemVersion` sehr alt und gleichzeitig `JavaVM`-Abhängigkeiten; nur-Intel-Builds ohne `arm64`-Slice.
- (ix) Sprachpakete via Download, fehlende `.lproj`-Verzeichnisse für angebotene Sprachen.

React Native/Expo (macOS via `react-native-macos` oder Catalyst): dieselben Muster gelten für das native Projekt; zusätzlich `electron-updater`-Reste in Hybrid-Projekten und `expo-updates` als Update-Kanal für macOS (Verstoß gegen vii, sofern nicht nur Bugfixes – siehe 2.5.2).

**Typische Verstöße**

❌ Sparkle-Updater im Mac-App-Store-Build:
```xml
<key>SUFeedURL</key><string>https://example.com/appcast.xml</string>
```
✅ Feed-Key entfernen, Updates dem Store überlassen; für den Direktvertrieb ein separates Target.

❌ Login-Item ohne Nachfrage:
```swift
try? SMAppService.mainApp.register()   // beim ersten Start
```
✅ Opt-in-Schalter in den Einstellungen, standardmäßig aus.

**Prüfliste**
- [ ] (i) App Sandbox aktiviert, Datenzugriff nur über Bookmarks/Framework-APIs
- [ ] (ii) Reines `.app`-Bundle aus Xcode, kein Installer, keine geteilten Orte
- [ ] (iii) Kein Autostart/Daemon ohne Opt-in, keine Nachlaufprozesse
- [ ] (iv) Kein Nachladen von Code, Plugins, Kexts
- [ ] (v) Keine Root-Anforderung, kein setuid, kein Privileged Helper
- [ ] (vi) Keine Lizenzschlüssel oder Aktivierungsdialoge
- [ ] (vii) Kein eigener Update-Mechanismus (Sparkle, Feeds)
- [ ] (viii) Läuft auf aktuellem macOS, keine Java-/Rosetta-Pflicht
- [ ] (ix) Alle Sprachen im Bundle

**Empfohlene Behebung** – Getrennte Targets für Store und Direktvertrieb (Sparkle/Lizenzierung nur im Direkt-Target); `SMAppService` mit Nutzer-Opt-in; Sandbox-Entitlements minimal und dokumentiert.

---

## 2.5 Software-Anforderungen

### 2.5.1 Nur öffentliche APIs, aktuelle SDKs

**Kern der Regel** – Apps nutzen ausschließlich öffentliche, dokumentierte APIs und laufen auf der aktuell ausgelieferten OS-Version. Abgekündigte Technologien müssen entfernt werden, und Frameworks werden nur für ihren vorgesehenen Zweck genutzt. Apple erwartet außerdem, dass Einreichungen mit einem aktuellen SDK gebaut sind – seit April 2026 ist das iOS-26-/Xcode-26-SDK die Mindestanforderung für neue Uploads.

**Risikostufe** – Kritisch. Die Private-API-Erkennung läuft bereits beim Upload automatisiert; Treffer führen zur sofortigen Ablehnung („non-public API usage"). Dritt-SDKs sind die Hauptquelle.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Dynamische Selektor-Aufrufe: `NSSelectorFromString(`, `performSelector(`, `respondsToSelector` mit verdeckten Namen, `NSClassFromString("_UI...")`, `objc_getClass("`, `method_exchangeImplementations` (Swizzling von UIKit-Internals).
- Unterstriche: Selektoren oder Klassen mit führendem `_` (`_setStatusBarHidden`, `_UINavigationBarContentView`).
- `dlopen(`/`dlsym(` auf `/System/Library/PrivateFrameworks/`, Imports wie `#import <IOKit/...>` auf iOS, `MobileGestalt`, `SpringBoardServices`, `BackBoardServices`, `AppSupport`.
- Verdeckte Strings: Base64-/XOR-kodierte Selektornamen, die zur Laufzeit zusammengesetzt werden – ein typisches SDK-Muster, das Apple inzwischen auch statisch erkennt.
- Zweckentfremdung: `CoreLocation` nur zum Wachhalten, `HealthKit` für Werbe-Segmente, `PassKit`-Tricks.
- Veraltete APIs: `UIWebView`, `UIAlertView`, `AddressBook` – `UIWebView` ist seit Jahren ein Ablehnungsgrund.
- SDK-Version: Prüfe `DTSDKName`/`DTXcode` im gebauten `Info.plist` und die Xcode-Version in CI (`fastlane`, `xcodebuild`-Aufrufe, `.github/workflows`, `eas.json` → `build.production.ios.image`).

React Native/Expo:
- Native Module in `node_modules/**/ios/*.m`, `*.mm`, `*.swift` mit den obigen Mustern – der JS-Code selbst nutzt keine privaten APIs, die Pods aber möglicherweise. Besonders ältere Pakete: `react-native-device-info` (alte Versionen mit `MobileGestalt`), Analytics-/Attribution-SDKs, Push-Provider mit Swizzling.
- Expo-SDK-Version in `package.json` gegen die aktuelle Xcode-Anforderung: Alte Expo-SDKs bauen mit alten Xcode-Images (`eas.json` → `image: "macos-sonoma-14.x"`), was seit April 2026 blockiert.
- `UIWebView`-Reste in alten Pods (`react-native-webview` < 6, `react-native-signature-capture`).
- Hermes-Bytecode (`main.jsbundle` als `.hbc`) ist unkritisch – entscheidend sind die nativen Symbole der Pods, nicht das JS-Bundle.

**Typische Verstöße**

❌
```objc
[[UIDevice currentDevice] performSelector:NSSelectorFromString(@"_setBatteryLevel:")];
```
✅ Öffentliche API `UIDevice.current.batteryLevel` nach `isBatteryMonitoringEnabled = true`.

❌ SDK lädt `libMobileGestalt.dylib` per `dlopen`, um die Geräteseriennummer zu lesen.
✅ `UIDevice.current.identifierForVendor` bzw. `DeviceCheck`/`App Attest`.

❌ `eas.json` mit Build-Image auf altem Xcode → Upload wird wegen SDK-Mindestversion abgewiesen.
✅ `"image": "latest"` und aktuelles Expo SDK.

**Prüfliste**
- [ ] Keine Selektoren/Klassen mit führendem Unterstrich, kein `dlopen` auf PrivateFrameworks
- [ ] Keine Swizzling-Ketten auf UIKit-Internals (in App und Pods)
- [ ] Kein `UIWebView`, keine abgekündigten Frameworks
- [ ] Build mit aktuellem Xcode/SDK (Xcode 26+), CI-Image aktuell
- [ ] Frameworks nur für ihren dokumentierten Zweck genutzt
- [ ] Symbol-Scan des Archives (`nm -u`, `otool -L`, `strings`) auf verdächtige Namen durchgeführt

**Empfohlene Behebung** – Verdächtige Pods aktualisieren oder ersetzen; `expo-device` statt alter Device-Info-Pakete; Archive vor Upload mit `strings`/`otool` gegen eine Blacklist privater Symbole prüfen.

### 2.5.2 In sich geschlossene Bundles, kein Nachladen von Code

**Kern der Regel** – Die App muss vollständig im Bundle enthalten sein, darf außerhalb ihres Containers weder lesen noch schreiben und darf keinen Code herunterladen, installieren oder ausführen, der Funktionen hinzufügt oder den Charakter der App verändert. Erlaubt ist Skript-Code, der über Apples eingebaute WebKit- bzw. JavaScriptCore-Laufzeit läuft, sofern er keine neuen Funktionen einführt. Lern-Apps dürfen Code zum Zweck des Programmierunterrichts nachladen, wenn der Nutzer ihn sehen und ändern kann. In der Praxis heißt das für OTA-Updates (expo-updates, CodePush, eigene Bundle-Loader): nur Fehlerbehebungen und kleine Anpassungen – keine neuen Screens, keine neuen Geschäftsmodelle, keine Änderung dessen, was im Review geprüft wurde.

**Risikostufe** – Kritisch. Nachgeladener Code, der Funktionen ändert, ist ein Kontosperr-Grund; Apple prüft nach Beschwerden auch nachträglich. OTA-Tools sind toleriert, aber nur in der beschriebenen Grauzone.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `dlopen(` mit Pfaden in `Documents`, `Caches` oder `tmp`; `Bundle(path:)` + `.load()` auf heruntergeladene Bundles; `NSBundle` aus URLs.
- `JSContext` (`JavaScriptCore`) mit `evaluateScript` auf Remote-Skripte, die App-Logik steuern – zulässig für Konfigurationslogik, kritisch, wenn Screens/Features daraus entstehen.
- Lua-/Python-/Scheme-Interpreter (`LuaJIT`, `PythonKit`) mit Remote-Skripten.
- Dateizugriffe außerhalb des Containers: `/private/var/`, `/var/mobile/Library/`, `NSHomeDirectory()`-Verlassen per `..`.

React Native/Expo:
- `expo-updates`: `app.json` → `updates.url`, `updates.enabled`, `runtimeVersion`. Prüfe die Release-Praxis: Enthält das Repo Changelogs/PRs, die neue Features nur per `eas update` veröffentlichen? Werden `runtimeVersion`-Policies (`appVersion`/`fingerprint`) genutzt, sodass native Änderungen einen Store-Build erzwingen?
- `react-native-code-push`/`appcenter`-Konfiguration: `CodePushDeploymentKey` in `Info.plist`, `codePush()`-Wrapper mit `installMode: IMMEDIATE`. Das SDK ist abgekündigt, Nachfolger (z. B. selbst gehostete Server) fallen unter dieselbe Regel.
- Eigene Loader: `fetch(bundleUrl)` + `new Function(code)`, `eval(`, `global.evalScript`, Hermes `HermesInternal`-Tricks, `require` aus heruntergeladenen Strings, `react-native-dynamic-bundle`.
- `WebView` mit `injectedJavaScript` aus Remote-Quellen, der native Bridges (`postMessage`) steuert – Grauzone; problematisch, sobald es Funktionen ersetzt, die im Review fehlten.

**Typische Verstöße**

❌ Remote-Code ausführen:
```js
const src = await (await fetch('https://cdn.example.com/logic.js')).text();
new Function(src)();
```
✅ Logik im Bundle ausliefern; variable Daten (nicht Code) per API laden.

❌ OTA-Release-Notes: „Neues Abo-Modell und Chat-Tab per `eas update` ausgerollt"
✅ Neue Funktionen als Store-Update einreichen; OTA nur für Bugfixes.

❌ CodePush mit sofortigem Neustart und ohne Kanal-Trennung:
```js
export default codePush({ installMode: codePush.InstallMode.IMMEDIATE })(App);
```
✅ Mindestens `ON_NEXT_RESTART`, Produktionskanal nur für Fehlerkorrekturen, Dokumentation der Release-Policy.

**Prüfliste**
- [ ] Kein `eval`/`new Function`/Remote-Bundle-Loader im Release-Pfad
- [ ] Kein `dlopen`/`Bundle.load` auf heruntergeladene Dateien
- [ ] JavaScriptCore/WebKit-Skripte fügen keine Funktionen hinzu
- [ ] expo-updates/CodePush nur für Bugfixes; `runtimeVersion`-Policy erzwingt Store-Builds bei nativen Änderungen
- [ ] Keine Dateizugriffe außerhalb des App-Containers
- [ ] Lern-Apps: nachgeladener Code ist sichtbar und editierbar

**Empfohlene Behebung** – `expo-updates` mit `runtimeVersion: { policy: "fingerprint" }` und dokumentierter Release-Policy; Feature-Entwicklung ausschließlich über Store-Builds; Remote-Konfiguration als Daten (JSON), nicht als Code.

### 2.5.3 Schadcode

**Kern der Regel** – Apps, die Schadsoftware verbreiten, das Betriebssystem oder die Hardware beschädigen oder andere Apps manipulieren, werden abgelehnt; Wiederholungstäter fliegen aus dem Developer Program.

**Risikostufe** – Kritisch.

**Woran du es im Code erkennst**
- Jailbreak-Erkennung ist erlaubt; Jailbreak-Ausnutzung nicht: Zugriffe auf `/Applications/Cydia.app`, `/bin/bash`, `/usr/sbin/sshd` zum Ausführen, nicht nur zum Prüfen.
- Verschleierte Payloads: große Base64-Blobs, die zur Laufzeit dekodiert und über `dlopen`/`NSTask`(macOS) gestartet werden.
- Bekannte Malware-SDK-Signaturen in Pods/`node_modules` (Supply-Chain-Fall: kompromittierte npm-Pakete mit `postinstall`-Skripten, die Binärdateien nachladen).
- Expo/RN: `package.json`-Abhängigkeiten mit Typosquatting-Namen; `postinstall`-Skripte, die aus dem Netz laden; ungewöhnliche native Module ohne Quelle.

**Prüfliste**
- [ ] Keine Exploit-Techniken, keine Manipulation fremder Apps oder des Systems
- [ ] Dependency-Audit (`npm audit`, `pod outdated`, SBOM) ohne Malware-Treffer
- [ ] Keine verschleierten Binär-Payloads im Bundle

### 2.5.4 Hintergrundmodi nur bei echtem Bedarf

**Kern der Regel** – Hintergrundausführung ist auf die vorgesehenen Zwecke beschränkt: VoIP, Audiowiedergabe, Standort, Abschluss einer begonnenen Aufgabe, lokale Benachrichtigungen und ähnliche vom System vorgesehene Fälle. Jeder aktivierte Modus muss einer sichtbaren, für den Nutzer nützlichen Funktion entsprechen.

**Risikostufe** – Hoch. `UIBackgroundModes` ist eine der ersten Dateien, die der Prüfer ansieht; ein `audio`- oder `location`-Modus ohne passende Funktion ist ein sicherer Ablehnungsgrund. Das Wachhalten der App über Stille-Audio oder Dauer-Standort ist zusätzlich ein 2.4.2-Verstoß.

**Woran du es im Code erkennst**

Swift/Objective-C – `Info.plist` → `UIBackgroundModes` mit den Werten:
- `audio` → braucht sichtbare Wiedergabe/Aufnahme (`AVAudioSession` aktiv, Now-Playing-Info).
- `location` → braucht eine Funktion, die Standortverlauf im Hintergrund benötigt (Tracking, Navigation) plus `NSLocationAlwaysAndWhenInUseUsageDescription` und Blaue-Leiste-Verhalten (`showsBackgroundLocationIndicator`).
- `voip` → nur mit `PushKit` + `CallKit`-Meldung jedes eingehenden Anrufs (sonst 2.5.12/4.x-Verstoß und Crash durch das System).
- `fetch`, `processing` → zusammen mit `BGTaskScheduler`-Registrierung und `BGTaskSchedulerPermittedIdentifiers`.
- `remote-notification` → nur, wenn stille Pushes tatsächlich Inhalte vorladen.
- `external-accessory`, `bluetooth-central`, `bluetooth-peripheral` → nur mit passenden Frameworks (`ExternalAccessory`, `CoreBluetooth`) und Hardware-Bezug in den Review-Notizen.
- `nearby-interaction`, `push-to-talk`, `network-authentication` → nur mit den zugehörigen Frameworks.

React Native/Expo:
- `app.json` → `ios.infoPlist.UIBackgroundModes` oder die Plugin-Konfiguration (`expo-location` mit `isIosBackgroundLocationEnabled`, `expo-av`/`expo-audio` mit `backgroundAudio`-Option, `expo-notifications`, `expo-background-task`, `expo-task-manager`).
- Bare RN: `ios/<App>/Info.plist` direkt prüfen; Pakete wie `react-native-track-player` (audio), `react-native-background-geolocation` (location), `react-native-voip-push-notification` (voip), `react-native-ble-plx` (bluetooth-central).
- Abgleich: Jeder Modus muss ein konsumierendes Paket und einen sichtbaren Screen haben.

**Typische Verstöße**

❌ `UIBackgroundModes = [audio, location, fetch, voip]` in einer To-do-App, weil ein Template sie mitbrachte.
✅ Nur die Modi, die eine Funktion der App tatsächlich benötigt – im Zweifel keinen.

❌ `voip`-Modus für Push-Zustellung ohne Anruffunktion.
✅ Normale APNs-Pushes (`remote-notification` nur bei echtem Vorab-Laden).

**Prüfliste**
- [ ] Jeder Eintrag in `UIBackgroundModes` hat eine sichtbare Funktion und ein konsumierendes Framework/Paket
- [ ] `voip` nur mit `PushKit` + `CallKit`
- [ ] `location` nur mit Always-Berechtigung, Nutzenbeschreibung und Hintergrund-Indikator
- [ ] `fetch`/`processing` mit `BGTaskScheduler` und erlaubten Identifiern
- [ ] Hintergrundfunktionen in den Review-Notizen erklärt

**Empfohlene Behebung** – Expo-Config-Plugins statt manueller Plist-Einträge, damit Modi an Pakete gekoppelt bleiben; nicht benötigte Modi aus `app.json`/`Info.plist` entfernen.

### 2.5.5 IPv6-only

**Kern der Regel** – Die App muss in reinen IPv6-Netzen (NAT64/DNS64, wie in vielen Mobilfunknetzen) vollständig funktionieren. Apple prüft im Review in solchen Umgebungen.

**Risikostufe** – Hoch. Ein Login, der im Review wegen IPv4-Literalen fehlschlägt, wird als 2.1(a)/2.5.5-Ablehnung gemeldet.

**Woran du es im Code erkennst**

Swift/Objective-C:
- IPv4-Literale in URLs: `http://203.0.113.10/api`, `192.168.`, `10.0.`.
- Low-Level-Sockets mit `AF_INET`, `sockaddr_in`, `inet_aton`, `gethostbyname` statt `getaddrinfo`/`Network.framework`.
- Reachability-Checks gegen IPv4-Adressen (`SCNetworkReachabilityCreateWithAddress` mit 8.8.8.8).

React Native/Expo:
- `fetch('http://1.2.3.4/...')`, Konfigurationsdateien mit IP-Literalen (`extra.apiUrl`).
- `react-native-tcp-socket`, `react-native-udp` mit `AF_INET`-Annahmen; `@react-native-community/netinfo` mit IPv4-Ping-Endpunkt (`reachabilityUrl`).

**Typische Verstöße**

❌
```swift
let url = URL(string: "http://203.0.113.10:8080/login")!
```
✅ Hostnamen verwenden; das System übersetzt über DNS64.

**Prüfliste**
- [ ] Keine IPv4-Literale in Code und Konfiguration
- [ ] Netzwerk-Code über `URLSession`/`Network.framework`/`fetch`, keine IPv4-only-Sockets
- [ ] Reachability gegen Hostnamen
- [ ] Test im NAT64-Netz (Internet-Freigabe am Mac mit „NAT64-Netzwerk erstellen") durchgeführt

**Empfohlene Behebung** – Hostnamen + `URLSession`; bei Sockets `NWConnection` (Network.framework); RN: `fetch`/`axios` mit Hostnamen, NetInfo ohne IPv4-Ping.

### 2.5.6 Browser müssen WebKit nutzen

**Kern der Regel** – Apps, die Web-Inhalte anzeigen oder einen Browser darstellen, müssen WebKit und WebKit-JavaScript verwenden. Alternative Browser-Engines sind nur mit dem entsprechenden Entitlement erlaubt, das Apple in der EU (DMA) und seit 2026 auch in Japan vergibt – und nur für Apps, die dort als Browser vertrieben werden und Apples Sicherheitsauflagen erfüllen.

**Risikostufe** – Hoch. Eine eingebettete Fremd-Engine ohne Entitlement wird sofort abgelehnt.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Frameworks: `Chromium`, `Blink`, `Gecko`, `GeckoView`, `Servo`, `Ultralight`, `CEF` in `Frameworks/` oder Pods.
- Entitlement `com.apple.developer.web-browser-engine.*` – nur mit Apple-Freigabe; Region auf EU/Japan beschränkt.
- `WKWebView` ist der Standard; `SFSafariViewController` für externe Seiten.

React Native/Expo:
- `react-native-webview` und `expo-web-browser` nutzen WebKit bzw. Safari → unkritisch.
- Auffällig: eigene JS-Engines für Web-Rendering (`react-native-quickjs` ist als Skript-Engine ohne Web-Rendering zulässig, aber im Zusammenspiel mit 2.5.2 zu prüfen), `react-native-servo`-Experimente.

**Prüfliste**
- [ ] Web-Inhalte über `WKWebView`/`SFSafariViewController`/`react-native-webview`
- [ ] Keine Fremd-Rendering-Engine ohne Entitlement
- [ ] Bei Browser-Entitlement: Verfügbarkeit auf die genehmigten Regionen begrenzt

**Empfohlene Behebung** – `expo-web-browser` (Safari-View) bzw. `react-native-webview`; Swift: `WKWebView`.

### 2.5.7 entfällt

Entfällt (von Apple gestrichen). Keine Prüfung erforderlich.

### 2.5.8 Keine alternativen Home-Screens oder Desktops

**Kern der Regel** – Apps dürfen keine Ersatz-Umgebung für den Home-Screen, den Desktop oder die Multitasking-Ansicht anbieten – keine Launcher, keine alternativen App-Umgebungen, keine Simulation des Systems.

**Risikostufe** – Hoch (Ablehnung ohne Nachbesserungsoption).

**Woran du es im Code erkennst**
- Launcher-Konzepte: Icon-Raster fremder Apps mit URL-Schemata (`LSApplicationQueriesSchemes` mit Dutzenden Einträgen), `canOpenURL`-Massenabfragen, Strings wie „Launcher", „Home Screen ersetzen", „Desktop".
- „Mini-Programme" mit eigener App-Verwaltung außerhalb der Regeln aus 4.7.
- RN/Expo: Pakete wie `react-native-app-installer` (Android-only, aber Hinweis auf das Konzept), `Linking.canOpenURL` in Schleifen über App-Listen.

**Prüfliste**
- [ ] Kein Launcher-/Desktop-Ersatz
- [ ] `LSApplicationQueriesSchemes` enthält nur Schemata mit konkretem Integrationszweck (max. ~50 Einträge, sonst Systemlimit)

### 2.5.9 Keine Manipulation von Standard-UI-Elementen

**Kern der Regel** – Hardwareschalter (Lautstärke, Ruheschalter/Action-Button) und systemeigene UI-Elemente wie Statusleiste, Multitasking-Geste, Home-Indikator oder Notification-Center dürfen weder verändert noch deaktiviert werden. Auch das Blockieren von Links, die Nutzer erwartungsgemäß in andere Apps führen, ist untersagt. Ausnahmen gelten nur, wo Apple explizite APIs dafür anbietet (z. B. `prefersHomeIndicatorAutoHidden`, Guided Access für Kiosk-Fälle).

**Risikostufe** – Hoch.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Lautstärke: `MPVolumeView`-Slider als unsichtbares Element zum Setzen der Lautstärke, `AVAudioSession.outputVolume` per KVO plus Rücksetzen (Lautstärke-Tasten als Kamera-Auslöser sind seit iOS 17.2 über `AVCaptureEventInteraction` offiziell erlaubt – Umwege darüber hinaus nicht).
- Ruheschalter: Abspielen über `.playback`-Kategorie, um den Stummschalter zu umgehen, bei Nicht-Media-Apps.
- Statusleiste: `UIStatusBarHidden` dauerhaft ohne Vollbild-Inhalt; Zugriffe auf `statusBarWindow` (privat).
- Multitasking/Home-Geste: `preferredScreenEdgesDeferringSystemGestures` auf allen Kanten dauerhaft; Versuche, `UIApplication.shared.isIdleTimerDisabled` plus Gesten-Deferral als „Kiosk" zu missbrauchen.
- Link-Blockade: `WKNavigationDelegate`, der `tel:`/`mailto:`/Universal Links von Konkurrenten abfängt und in eigene Views umleitet.

React Native/Expo:
- `react-native-volume-manager`/`react-native-system-setting` zum erzwungenen Setzen der Lautstärke.
- `expo-av`/`expo-audio` mit `playsInSilentModeIOS: true` bei UI-Sounds (Stummschalter-Umgehung).
- `react-native-webview` mit `onShouldStartLoadWithRequest`, das alle externen Links blockiert.

**Typische Verstöße**

❌ UI-Klick-Sounds trotz Stummschalter:
```js
await Audio.setAudioModeAsync({ playsInSilentModeIOS: true });   // für Button-Sounds
```
✅ `playsInSilentModeIOS` nur für echte Medienwiedergabe (Musik, Podcast, Video).

❌ Versteckter `MPVolumeView`, der die Lautstärke bei jedem Start auf 100 % zieht.
✅ Lautstärke dem Nutzer überlassen; Hinweis anzeigen, wenn sie 0 ist.

**Prüfliste**
- [ ] Keine programmatische Lautstärke-Manipulation
- [ ] Stummschalter wird respektiert (Playback-Kategorie nur für Medien)
- [ ] Statusleiste/Home-Indikator nur kontextbezogen ausgeblendet
- [ ] Keine Blockade erwartbarer Links (tel:, mailto:, Universal Links)
- [ ] Keine Kiosk-Simulation ohne Guided Access/Single App Mode

### 2.5.10 entfällt

Entfällt (von Apple gestrichen). Keine Prüfung erforderlich.

### 2.5.11 SiriKit und Shortcuts

**Kern der Regel** – Apps, die Siri, App Intents oder Shortcuts einbinden, registrieren nur Intents, die sie tatsächlich erfüllen können (i); Vokabular und Beispielphrasen beziehen sich auf die eigene App, nicht auf generische Begriffe oder Fremddienste (ii); Anfragen werden direkt erledigt, ohne Werbung oder Marketing, und Rückfragen nur, wenn die Auflösung sie wirklich braucht (iii).

**Risikostufe** – Mittel. Falsche Intent-Deklarationen fallen beim Test der Siri-Integration auf; Werbung in Intent-Antworten führt zur Ablehnung.

**Woran du es im Code erkennst**

Swift/Objective-C:
- (i) `Intents.intentdefinition`, `NSExtension` → `IntentsSupported` in der Intents-Extension, `AppIntent`-Konformitäten: Jeder Intent braucht einen `handle`/`perform`-Pfad mit echter Logik, kein `return .success` als Stub.
- (ii) `AppIntentVocabulary.plist`, `INVocabulary`-Aufrufe, `AppShortcutsProvider` mit Phrasen wie „Spiele Musik" für eine Nicht-Musik-App oder Markennamen Dritter.
- (iii) Intent-Antworten (`IntentResponse`, `ProvidesDialog`) mit Marketing-Texten („Jetzt Pro kaufen!"), unnötige `requestDisambiguation`/`needsValue`-Rückfragen.

React Native/Expo:
- Siri-Integration läuft immer über native Targets; prüfe `ios/` auf Intents-Extensions und `expo`-Config-Plugins (`expo-siri-shortcuts`, `react-native-siri-shortcut`), die `NSUserActivityTypes` deklarieren. Aktivitäten müssen im JS-Handler tatsächlich verarbeitet werden (`SiriShortcutsEvent`-Listener vorhanden).

**Typische Verstöße**

❌ `IntentsSupported` enthält `INSendMessageIntent`, obwohl die App nur einen Kalender hat.
✅ Nur Intents deklarieren, die vollständig implementiert sind.

❌ Intent-Antwort: „Erledigt! Upgrade jetzt auf Premium für mehr Funktionen."
✅ Neutrale Antwort mit dem Ergebnis.

**Prüfliste**
- [ ] (i) Alle deklarierten Intents/App Intents sind implementiert
- [ ] (ii) Vokabular und Phrasen beziehen sich auf die eigene App
- [ ] (iii) Keine Werbung in Intent-Antworten, Rückfragen nur bei echter Mehrdeutigkeit

### 2.5.12 CallKit, SMS-Filter, Spam-Erkennung

**Kern der Regel** – Anruf-Blockier- und SMS-Filter-Erweiterungen dürfen nur Nummern blockieren, die nachweislich Spam sind. Die Funktion muss in den Metadaten klar benannt sein, samt Kriterien, nach denen gefiltert wird. Die verarbeiteten Daten (Anrufer, Nachrichten) dürfen nur für den Betrieb und die Verbesserung der Funktion genutzt werden – nicht für Tracking, Profilbildung oder Verkauf.

**Risikostufe** – Hoch, weil Telefonie- und Nachrichtendaten besonders sensibel sind (Überschneidung mit 5.1).

**Woran du es im Code erkennst**
- Extension-Targets: `com.apple.callkit.call-directory` (`CXCallDirectoryProvider`), `com.apple.identitylookup.message-filter` (`ILMessageFilterExtension`), `com.apple.identitylookup.classification-report`.
- `ILMessageFilterExtensionNetworkURL` in der Extension-`Info.plist`: Nachrichten dürfen nur an diesen deklarierten Server gehen; prüfe, was dort protokolliert wird.
- Analytics-/Werbe-SDKs in der Extension (verboten, siehe auch 2.5.18).
- Blocklisten aus unklaren Quellen (`blocked_numbers.csv` ohne Herkunft).
- RN/Expo: nur über native Extension-Targets möglich; Config-Plugins wie `@bacons/apple-targets` prüfen, ob eine solche Extension existiert.

**Prüfliste**
- [ ] Blockierlogik basiert auf bestätigten Spam-Quellen
- [ ] Kriterien und Funktion in Beschreibung/Datenschutzangaben genannt
- [ ] Keine Weiterverwendung von Anruf-/Nachrichtendaten für Werbung oder Profile
- [ ] Keine Analytics-/Werbe-SDKs in der Filter-Extension

### 2.5.13 Gesichtserkennung

**Kern der Regel** – Für die Kontoauthentifizierung ist `LocalAuthentication` (Face ID/Touch ID/Optic ID) zu verwenden, nicht ARKit oder eigene Gesichtserkennung. Wo Gesichtsdaten verarbeitet werden, braucht es ausdrückliche Einwilligung und eine alternative Authentifizierung; Nutzer unter 13 Jahren müssen eine andere Methode bekommen.

**Risikostufe** – Hoch (biometrische Daten; Überschneidung mit 5.1.2 und regionalen Biometrie-Gesetzen).

**Woran du es im Code erkennst**

Swift/Objective-C:
- Eigene Gesichts-Logins über `Vision` (`VNDetectFaceRectanglesRequest`, `VNFaceObservation`), `ARFaceTrackingConfiguration`, `AVCaptureSession` + Server-Upload zum „Face Login".
- Fehlendes `LAContext.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics...)` bei „Face ID-Login"-Strings.
- `NSFaceIDUsageDescription` fehlt trotz `LocalAuthentication`-Nutzung.
- Fehlende Fallback-Option (Passwort/Code), wenn Biometrie nicht verfügbar ist oder abgelehnt wird.

React Native/Expo:
- `expo-local-authentication` bzw. `react-native-biometrics` → korrekt.
- `expo-face-detector` (abgekündigt), `react-native-vision-camera` mit Face-Detection-Plugins, `@tensorflow/tfjs-react-native` mit Face-Modellen als Login-Mechanismus → Verstoß, wenn zur Authentifizierung genutzt.
- Fehlender `NSFaceIDUsageDescription` in `app.json` → `ios.infoPlist`.

**Typische Verstöße**

❌ Selfie an einen Server senden und mit dem Profilfoto vergleichen, um einzuloggen.
✅ `LocalAuthentication`/`expo-local-authentication` plus Passwort-Fallback.

**Prüfliste**
- [ ] Authentifizierung über `LocalAuthentication`, nicht über eigene Gesichtserkennung
- [ ] `NSFaceIDUsageDescription` gesetzt
- [ ] Alternative Anmeldemethode vorhanden
- [ ] Kinder unter 13: keine Gesichtserkennung, andere Methode
- [ ] Bei sonstiger Gesichtsverarbeitung (Filter, AR): Einwilligung und Zweckbindung (5.1.2)

**Empfohlene Behebung** – `expo-local-authentication`; bare RN: `react-native-biometrics`; Swift: `LAContext`.

### 2.5.14 Aufzeichnung von Nutzeraktivität

**Kern der Regel** – Wer Kamera, Mikrofon, Bildschirm oder Nutzereingaben aufzeichnet, braucht eine ausdrückliche Einwilligung und eine dauerhaft sichtbare oder hörbare Anzeige während der Aufnahme. Das gilt auch für Session-Replay-Tools und Analytics, die Eingaben mitschneiden.

**Risikostufe** – Hoch. Session-Replay-SDKs ohne Einwilligung und Hinweis sind ein bekannter Ablehnungsgrund; Aufzeichnung ohne Anzeige gilt als Täuschung.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `ReplayKit` (`RPScreenRecorder`), `AVCaptureSession`, `AVAudioRecorder`, `CGWindowListCreateImage` (macOS) – prüfe, ob ein Aufnahme-Indikator im UI existiert und ob die Aufnahme nur nach expliziter Aktion startet.
- Session-Replay-/Heatmap-SDKs: `UXCam`, `Smartlook`, `FullStory`, `Hotjar`, `Microsoft Clarity`, `Contentsquare`, `Sentry` mit Session Replay, `PostHog` mit `sessionReplay`, `Datadog RUM` mit Replay, `LogRocket`. Ohne Opt-in und Hinweis: Verstoß.
- Keylogging-Muster: `UITextField`-Delegate, das jeden Tastendruck an einen Server sendet; Custom Keyboards mit `RequestsOpenAccess` und Netzwerkzugriff.
- Fehlende `NSCameraUsageDescription`, `NSMicrophoneUsageDescription`.

React Native/Expo:
- `expo-camera`, `expo-av`/`expo-audio` Recording, `react-native-vision-camera`, `react-native-record-screen`, `expo-screen-capture` (Erkennung ist ok, Aufnahme ohne Hinweis nicht).
- Replay-SDKs: `react-native-ux-cam`, `@smartlook/react-native-smartlook-analytics`, `posthog-react-native` mit `enableSessionReplay: true`, `@sentry/react-native` mit `replaysSessionSampleRate > 0`, `@datadog/mobile-react-native-session-replay`, `@microsoft/react-native-clarity`.
- Berechtigungstexte in `app.json` → `ios.infoPlist` bzw. Plugin-Optionen (`cameraPermission`, `microphonePermission`).

**Typische Verstöße**

❌
```js
posthog.init(key, { enableSessionReplay: true });   // ohne Opt-in, ohne Hinweis
```
✅ Replay standardmäßig aus, Aktivierung nur nach Einwilligung in den Einstellungen; sensible Felder maskiert.

❌ Hintergrund-Audioaufnahme „zur Sprachanalyse" ohne roten Indikator/Statushinweis.
✅ Aufnahme nur nach Tap, sichtbare Anzeige, Stopp beim Verlassen des Screens.

**Prüfliste**
- [ ] Jede Aufnahme (Kamera, Mikro, Bildschirm, Eingaben) startet erst nach expliziter Einwilligung
- [ ] Sichtbare/hörbare Aufnahmeanzeige während der Aufnahme
- [ ] Session-Replay-SDKs nur mit Opt-in, Maskierung sensibler Felder, Nennung in den Datenschutzangaben
- [ ] Usage-Descriptions für Kamera und Mikrofon vorhanden und ehrlich
- [ ] Keine Tastatureingaben-Protokollierung außerhalb der Kernfunktion

**Empfohlene Behebung** – Replay-Funktionen deaktivieren oder hinter einen Einwilligungs-Dialog legen (`expo-tracking-transparency` reicht dafür nicht aus – separate, klare Zustimmung); Aufnahme-Indikator als festes UI-Element.

### 2.5.15 Dateiauswahl über System-Picker

**Kern der Regel** – Apps, die Dokumente anzeigen oder auswählen lassen, sollen die Dateien-App und iCloud Drive einbinden – also die Systemauswahl (`UIDocumentPickerViewController`, `.fileImporter`, `PHPickerViewController`) statt eigener Datei-Browser, die nur den App-Container zeigen. Nutzer erwarten Zugriff auf ihre Dokumente unabhängig vom Speicherort.

**Risikostufe** – Niedrig bis Mittel.

**Woran du es im Code erkennst**
- Swift: eigener `FileManager`-Browser statt `UIDocumentPickerViewController`; fehlende `UIFileSharingEnabled`/`LSSupportsOpeningDocumentsInPlace`, wenn die App Dokumente verwaltet; `UTImportedTypeDeclarations` bei eigenen Formaten.
- RN/Expo: `expo-document-picker`, `expo-image-picker`, `react-native-document-picker` → korrekt. Auffällig: Eigenbau-Listen aus `FileSystem.documentDirectory` als einzige Auswahl.

**Prüfliste**
- [ ] Dokumentauswahl über den System-Picker (Dateien-App/iCloud erreichbar)
- [ ] Dokument-basierte Apps deklarieren `LSSupportsOpeningDocumentsInPlace`/`UIFileSharingEnabled`
- [ ] Eigene Dateiformate per UTI registriert

**Empfohlene Behebung** – `expo-document-picker`/`expo-image-picker`; bare RN: `react-native-document-picker`; Swift: `.fileImporter`/`UIDocumentPickerViewController`.

### 2.5.16 Widgets, Erweiterungen, Benachrichtigungen, App Clips

**Kern der Regel** – Widgets, Live Activities, Erweiterungen (Keyboard, Share, Action, Notification Service/Content) und Benachrichtigungen müssen mit dem Inhalt und der Funktion der Haupt-App zusammenhängen. Sie dürfen nicht als Werbefläche oder als Standalone-Produkt ohne Bezug dienen. **(a) App Clips**: Ein App Clip ist ein Ausschnitt der Haupt-App – alle seine Funktionen müssen auch im Hauptbinary existieren, er darf keine Werbung enthalten und bleibt auf die konkrete Aufgabe fokussiert (siehe auch 4.x zu Größe und Verhalten).

**Risikostufe** – Mittel; für Werbung in Widgets/App Clips Hoch (siehe 2.5.18).

**Woran du es im Code erkennst**

Swift/Objective-C:
- Widget-Targets (`WidgetKit`, `TimelineProvider`): Inhalte, die nichts mit der App zu tun haben (Wetter-Widget in einer Banking-App), Ad-Views, Deep Links ins Marketing.
- `NSExtension` → `NSExtensionPointIdentifier`: Keyboard-Extensions mit `RequestsOpenAccess` ohne Grund; Share-Extensions, die nur zum App-Download auffordern.
- Notification-Service-Extensions, die Tracking-Pixel laden oder Werbe-Pushes anreichern.
- App Clip-Target (`com.apple.developer.parent-application-identifiers`, `NSAppClip` in `Info.plist`): Prüfe, ob der Clip Funktionen hat, die in der Haupt-App fehlen, und ob Ad-SDKs verlinkt sind.
- Benachrichtigungen: Push-Payloads/Local Notifications mit reinem Werbecharakter ohne Opt-in (Verweis auf 4.5.4).

React Native/Expo:
- Widgets nur über native Targets bzw. Config-Plugins (`@bacons/apple-targets`, `react-native-widget-extension`, `expo-widgets`-Experimente). Prüfe die Swift-Dateien im Target-Ordner wie oben.
- App Clips: `expo-app-clip`-Ansätze oder manuelles Clip-Target; prüfe, ob das Clip-Bundle Ad-Pakete (`react-native-google-mobile-ads`) einbindet.
- `expo-notifications`: Kampagnen-Pushes („Nur heute 50 % Rabatt") ohne explizite Marketing-Zustimmung.

**Typische Verstöße**

❌ Widget zeigt Banner-Werbung über `GADBannerView`-Snapshot.
✅ Widget zeigt App-Inhalte (Timeline-Daten) und verlinkt in die App.

❌ App Clip enthält einen Bezahl-Flow, der in der Haupt-App nicht existiert.
✅ Alle Clip-Funktionen als Teilmenge der Haupt-App.

**Prüfliste**
- [ ] Widgets/Live Activities zeigen App-bezogene Inhalte, keine Werbung
- [ ] Erweiterungen haben einen klaren Bezug zur Haupt-App; Keyboard-Vollzugriff nur mit Grund
- [ ] Benachrichtigungen ohne Werbung, sofern kein Marketing-Opt-in (4.5.4)
- [ ] (a) App Clip: keine Werbung, alle Funktionen auch im Hauptbinary, Fokus auf eine Aufgabe

**Empfohlene Behebung** – Werbe-SDKs nur im Haupt-App-Target verlinken (Target Membership prüfen); Widget-Daten über App Groups aus der Haupt-App beziehen.

### 2.5.17 Matter-Unterstützung

**Kern der Regel** – Apps, die Matter-Geräte einbinden, müssen für das Pairing Apples Matter-Framework (`MatterSupport`) verwenden. Andere Matter-Komponenten in der App müssen von der Connectivity Standards Alliance zertifiziert sein.

**Risikostufe** – Niedrig bis Mittel (nur Smart-Home-Apps).

**Woran du es im Code erkennst**
- `import Matter`, `import MatterSupport`, `MatterAddDeviceRequest` → korrekt.
- Eigene Commissioning-Stacks: `chip-tool`-Ports, `connectedhomeip`-Bibliotheken ohne CSA-Zertifizierungsnachweis; BLE-Commissioning direkt über `CoreBluetooth` mit Matter-Payloads.
- Entitlement `com.apple.developer.matter.allow-setup-payload` bei Matter-Pairing.
- RN/Expo: `react-native-matter`-Bibliotheken – prüfe, ob sie `MatterSupport` wrappen oder einen eigenen Stack mitbringen.

**Prüfliste**
- [ ] Pairing über `MatterSupport`-Extension
- [ ] Sonstige Matter-Komponenten CSA-zertifiziert (Nachweis in den Review-Notizen)

### 2.5.18 Display-Werbung

**Kern der Regel** – Display-Werbung ist auf das Hauptbinary beschränkt: keine Anzeigen in Erweiterungen, App Clips, Widgets, Benachrichtigungen, Tastaturen oder watchOS-Apps. Werbung muss zur Altersfreigabe passen, Targeting-Angaben offenlegen und darf keine sensiblen Daten (Gesundheit, Schuldaten, Kinder) für verhaltensbasiertes Targeting nutzen. Interstitials müssen klar als Werbung erkennbar sein und einen sichtbaren Schließen-/Überspringen-Button haben. Apps mit Werbung brauchen eine Möglichkeit, unangemessene Anzeigen zu melden.

**Risikostufe** – Hoch. Werbung außerhalb des Hauptbinaries wird sofort abgelehnt; unangemessene Anzeigen für Kinder-Freigaben führen zur Entfernung.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Ad-SDKs in falschen Targets: `GoogleMobileAds`, `AppLovinSDK`, `IronSource`, `UnityAds`, `Vungle`, `Chartboost`, `Meta Audience Network` in Extension-, Widget-, Clip- oder Watch-Targets (`Pods-<Target>`-Membership, `Frameworks, Libraries and Embedded Content`).
- Interstitial-Konfiguration ohne Close-Button (`GADFullScreenContentDelegate` mit ausgeblendetem Dismiss; eigene Overlay-Ads ohne Schließen).
- Fehlende Alterskonfiguration: `GADMobileAds.sharedInstance().requestConfiguration.tagForChildDirectedTreatment`, `maxAdContentRating`; AppLovin `setIsAgeRestrictedUser`.
- Targeting mit sensiblen Daten: HealthKit-Daten oder ClassKit-Daten in Ad-Requests (`GADRequest` mit Custom-Targeting aus Gesundheitswerten).
- Meldefunktion: Kein UI-Pfad „Anzeige melden".

React Native/Expo:
- `react-native-google-mobile-ads`, `react-native-applovin-max`, `react-native-unity-ads`, `expo-ads-admob` (abgekündigt). Prüfe `app.json`-Plugin-Konfiguration (`ios_app_id`) und ob Alters-Tags gesetzt sind (`setRequestConfiguration({ maxAdContentRating, tagForChildDirectedTreatment })`).
- Werbe-Komponenten in Widget-/Clip-Targets (Swift-Dateien im Target-Ordner) oder in `expo-notifications`-Rich-Content.
- Eigene Interstitial-Modals (`<Modal>` mit Werbe-`WebView`) ohne Schließen-Button oder mit Timer > wenige Sekunden ohne Kennzeichnung.

**Typische Verstöße**

❌ Werbe-SDK im App-Clip-Target verlinkt (Podfile: `target 'AppClip' do pod 'Google-Mobile-Ads-SDK'`).
✅ Ad-SDK nur im Haupt-Target.

❌
```js
mobileAds().initialize();   // Kinder-App, kein tagForChildDirectedTreatment
```
✅
```js
await mobileAds().setRequestConfiguration({ tagForChildDirectedTreatment: true, maxAdContentRating: MaxAdContentRating.G });
```

**Prüfliste**
- [ ] Ad-SDKs und Ad-Views nur im Haupt-App-Target
- [ ] Alters-/Content-Rating-Konfiguration des Ad-SDKs passend zur Freigabe
- [ ] Kein Targeting mit Gesundheits-, Schul- oder Kinderdaten
- [ ] Interstitials klar gekennzeichnet, mit sichtbarem Schließen-Button
- [ ] Funktion zum Melden unangemessener Anzeigen vorhanden
- [ ] Keine Werbung in Widgets, Clips, Erweiterungen, Benachrichtigungen, Tastaturen, watchOS

**Empfohlene Behebung** – `react-native-google-mobile-ads` mit `setRequestConfiguration`; Swift: `GADRequestConfiguration`; Ad-Reporting-Link in den Einstellungen; Target-Membership der Ad-Pods im Podfile beschränken.

---

## Paketreferenz React Native / Expo

| Zweck | Expo | Bare React Native |
|---|---|---|
| Umgebungs-Konfiguration (2.1a) | `expo-constants` + `app.config.js`/EAS-Secrets | `react-native-config` |
| Debug-Ausgaben entfernen (2.1a) | `babel-plugin-transform-remove-console` | `babel-plugin-transform-remove-console` |
| In-App-Käufe (2.1b) | `react-native-purchases` (RevenueCat) | `react-native-iap` |
| Build-Profile Store/TestFlight (2.2) | `eas.json` (`production`/`preview`) | Xcode Schemes + Configurations |
| Remote-Konfiguration ohne Code (2.3.1a, 2.5.2) | `@react-native-firebase/remote-config` (nur Daten) | dito |
| Bewertungsdialog (2.3.1b) | `expo-store-review` | `react-native-rate` / `SKStoreReviewController` |
| Plattformspezifische Strings (2.3.10) | `Platform.select`, `.ios.ts`-Dateien | dito |
| Deep Links / Events (2.3.13) | `expo-linking`, `expo-router` | `Linking`, `react-navigation` Linking-Config |
| iPad-Layout (2.4.1) | `useWindowDimensions`, `react-native-safe-area-context` | dito |
| Hintergrundarbeit (2.4.2, 2.5.4) | `expo-background-task`, `expo-task-manager` | `react-native-background-fetch` |
| Standort (2.4.2, 2.5.4) | `expo-location` | `react-native-geolocation-service` |
| Keep-Awake (2.4.2) | `expo-keep-awake` (screenweise) | `react-native-keep-awake` |
| Einstellungen öffnen (2.4.4) | `Linking.openSettings()` | `Linking.openSettings()` |
| Geräte-Infos ohne Private APIs (2.5.1) | `expo-device`, `expo-application` | `react-native-device-info` (aktuell) |
| OTA-Updates, nur Bugfixes (2.5.2) | `expo-updates` (`runtimeVersion: fingerprint`) | selbst gehostete `expo-updates`-Server (CodePush abgekündigt) |
| Web-Inhalte (2.5.6) | `expo-web-browser`, `react-native-webview` | `react-native-webview`, `SFSafariViewController`-Wrapper |
| Audio-Modus / Stummschalter (2.5.9) | `expo-audio` (`playsInSilentMode` nur für Medien) | `react-native-track-player` |
| Siri/Shortcuts (2.5.11) | natives Target via `@bacons/apple-targets` | `react-native-siri-shortcut` |
| Biometrie (2.5.13) | `expo-local-authentication` | `react-native-biometrics` |
| Kamera/Mikro mit Hinweis (2.5.14) | `expo-camera`, `expo-audio` | `react-native-vision-camera` |
| Session Replay nur mit Opt-in (2.5.14) | `posthog-react-native`, `@sentry/react-native` (Replay aus) | dito |
| Dateiauswahl (2.5.15) | `expo-document-picker`, `expo-image-picker` | `react-native-document-picker`, `react-native-image-picker` |
| Widgets / App Clips (2.5.16) | `@bacons/apple-targets` | manuelles Xcode-Target |
| Benachrichtigungen (2.5.16) | `expo-notifications` | `@react-native-firebase/messaging`, `@notifee/react-native` |
| Werbung mit Alters-Tags (2.5.18) | `react-native-google-mobile-ads` | dito |

## Kurz-Prüfliste für diesen Abschnitt

**2.1 Vollständigkeit**
- [ ] Keine Platzhalter-, Test- oder „Bald verfügbar"-Texte in Release-Ressourcen
- [ ] Keine `localhost`/Staging-/`http://`-Endpunkte im Release-Pfad
- [ ] Keine Funktionen nur hinter `#if DEBUG`/`__DEV__`
- [ ] Demo-Account/Demo-Modus und Review-Notizen vorhanden
- [ ] Crashlogs des letzten Builds ohne offene Abstürze
- [ ] Produkt-IDs stimmen mit App Store Connect überein, IAP im Sandbox getestet, Restore vorhanden
- [ ] Receipt-Validierung mit Sandbox-Fallback

**2.2 Betatests**
- [ ] Keine Beta-/Alpha-Bezeichnungen im Store-Build
- [ ] TestFlight nicht als Vertriebskanal, keine Bezahlung von Testern
- [ ] Debug-/Feedback-Menüs im Store-Build aus

**2.3 Metadaten**
- [ ] Keine Review-/Datums-/Regions-abhängigen Feature-Flags, keine geheimen Gesten
- [ ] Keine Belohnung für Bewertungen, System-Dialog ohne Stimmungs-Vorfilter
- [ ] IAP in Beschreibung/Screenshots genannt, Preise aus StoreKit
- [ ] Screenshots zeigen echte App-Screens, iPad-Screenshots vorhanden
- [ ] Vorschauen nur aus Screen-Recordings
- [ ] Kategorie passt, `LSApplicationCategoryType` stimmig
- [ ] Altersfreigabe-Fragebogen inkl. Social-Media-Fragen (Pflicht ab September 2026) und Korea-Angaben beantwortet; Werbe-SDKs altersgerecht konfiguriert
- [ ] Name ≤ 30 Zeichen ohne Fremdmarken/Preise; Keywords ohne Konkurrenznamen; Icons identisch
- [ ] Icon/Screenshots/Vorschauen 4+-tauglich; „für Kinder" nur in Kids-Kategorie
- [ ] Screenshot-Daten fiktiv, Assets lizenziert
- [ ] Keine Android-/Play-Store-/Fremdmarken-Strings im iOS-Pfad, i18n plattformgetrennt
- [ ] Vorbestell-Build vollständig, Änderungen erzwingen Neustart der Vorbestellung
- [ ] Release-Notes beschreiben die tatsächlichen Änderungen
- [ ] In-App-Event-Deep-Links führen direkt zum Event

**2.4 Hardware**
- [ ] App auf iPad (11" M3-Referenz) bedienbar; ActionSheets/Share mit Popover-Anker; Rotation/Split View ok
- [ ] Kein Mining; Timer/Polling/Render-Loops mit Cleanup; Standortgenauigkeit minimal; Keep-Awake screenweise
- [ ] tvOS: Siri-Remote-Bedienung vollständig, Controller-Pflicht kommuniziert
- [ ] Keine Neustart-Aufforderungen, keine `App-Prefs:`-URLs, keine Aufforderung zu systemweiten Einstellungsänderungen
- [ ] macOS: Sandbox (i), reines Bundle (ii), kein Autostart (iii), kein Code-Nachladen (iv), kein Root/setuid (v), keine Lizenzschlüssel (vi), kein eigener Updater (vii), aktuelles macOS ohne Java (viii), alle Sprachen im Bundle (ix)

**2.5 Software**
- [ ] Keine Unterstrich-Selektoren, kein `dlopen` auf PrivateFrameworks, kein Swizzling von UIKit-Internals (App und Pods)
- [ ] Kein `UIWebView`; Build mit Xcode 26+/aktuellem SDK; CI-Image aktuell
- [ ] Symbol-Scan des Archives durchgeführt
- [ ] Kein `eval`/`new Function`/Remote-Bundle-Loader; kein `Bundle.load` auf Downloads
- [ ] expo-updates/CodePush nur für Bugfixes; `runtimeVersion`-Policy gesetzt; keine Container-Ausbrüche
- [ ] Dependency-Audit ohne Malware-Treffer, keine verschleierten Payloads
- [ ] Jeder `UIBackgroundModes`-Eintrag hat Funktion und konsumierendes Paket; `voip` nur mit PushKit+CallKit; `fetch`/`processing` mit BGTaskScheduler
- [ ] Keine IPv4-Literale, keine IPv4-only-Sockets, NAT64-Test durchgeführt
- [ ] Web-Inhalte über WebKit; keine Fremd-Engine ohne Entitlement (EU/Japan)
- [ ] 2.5.7 entfällt – keine Prüfung
- [ ] Kein Launcher-/Home-Screen-Ersatz; `LSApplicationQueriesSchemes` zweckgebunden
- [ ] Keine Lautstärke-Manipulation, Stummschalter respektiert, Statusleiste/Home-Indikator kontextbezogen, keine Link-Blockade
- [ ] 2.5.10 entfällt – keine Prüfung
- [ ] Siri: nur implementierte Intents, app-bezogenes Vokabular, keine Werbung in Antworten
- [ ] CallKit/SMS-Filter: bestätigte Spam-Quellen, Kriterien genannt, keine Datenweiterverwendung, keine Analytics in der Extension
- [ ] Biometrie über LocalAuthentication, Usage-Description, Fallback, keine Gesichtserkennung für unter 13
- [ ] Aufnahmen nur mit Einwilligung und sichtbarem Indikator; Session Replay nur mit Opt-in und Maskierung
- [ ] Dateiauswahl über System-Picker; Dokument-Apps deklarieren Dateifreigabe
- [ ] Widgets/Erweiterungen/Benachrichtigungen app-bezogen und werbefrei; App Clip ohne Werbung, Funktionen auch im Hauptbinary
- [ ] Matter-Pairing über MatterSupport, andere Komponenten CSA-zertifiziert
- [ ] Werbung nur im Haupt-Target, altersgerecht, ohne sensible Daten, Interstitials mit Schließen-Button, Meldefunktion vorhanden
