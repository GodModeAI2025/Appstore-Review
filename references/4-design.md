# Abschnitt 4 – Design

Stand: Apple App Review Guidelines, Fassung vom 8. Juni 2026 (geprüft September 2026).
Zurück zur Übersicht: ../SKILL.md

## Wo Apple aktuell besonders genau hinschaut

- **WebView-Hüllen ohne nativen Mehrwert (4.2)** – die häufigste Ablehnung in diesem Abschnitt. Ein `WKWebView` oder `react-native-webview` als einziger Screen reicht nicht, egal wie gut die Website ist.
- **Drittanbieter-Login ohne datensparsame Alternative (4.8)** – Google-, Facebook- oder X-Login ohne Sign in with Apple (oder gleichwertige Option) wird bei jedem Einreichen bemängelt.
- **Push-Prompt beim ersten Start ohne Kontext (4.5.4)** – Systemdialog sofort nach dem Launch, dazu Werbe-Pushes ohne Einwilligung, führen regelmäßig zu Ablehnungen.
- **Template- und Generator-Apps (4.2.6, 4.3)** – viele fast identische Binaries desselben Entwickler-Accounts werden gebündelt abgelehnt, teils mit Account-Konsequenzen.
- **Mini-Apps und Chatbots ohne Altersfreigabe und IAP (4.7)** – eingebettete HTML5-Inhalte, die eigene Bezahlwege oder unmoderierte Inhalte mitbringen.

## Inhalt

- [4.1 Nachahmer](#41-nachahmer) – (a) Klone, (b) Impersonation, (c) Marken
- [4.2 Mindestfunktionalität](#42-mindestfunktionalität) – 4.2.1 ARKit, 4.2.2 Marketing, 4.2.3 Eigenständigkeit/Downloads, 4.2.4–4.2.5 entfällt, 4.2.6 Template-Apps, 4.2.7 Remote Desktop
- [4.3 Spam](#43-spam) – (a) Duplikate/gesättigte Kategorien, (b) Bundle-IDs, Live Activities, Push, Game Center
- [4.4 Erweiterungen](#44-erweiterungen) – 4.4.1 Keyboard, 4.4.2 Safari, 4.4.3 Steuer-/Sticker
- [4.5 Apple-Websites und -Dienste](#45-apple-websites-und--dienste) – 4.5.1 Dokumentation, 4.5.2 MusicKit, 4.5.3 Spam, 4.5.4 Push, 4.5.5 Game Center, 4.5.6 Emoji
- [4.6 entfällt](#46-entfällt)
- [4.7 Mini-Apps, Streaming-Games, Chatbots, Plug-ins, Emulatoren](#47-mini-apps-mini-games-streaming-games-chatbots-plug-ins-game-emulatoren)
- [4.8 Login-Dienste](#48-login-dienste)
- [4.9 Apple Pay](#49-apple-pay)
- [4.10 Monetarisierung eingebauter Systemfunktionen](#410-monetarisierung-eingebauter-systemfunktionen)
- [Paketreferenz React Native / Expo](#paketreferenz-react-native--expo)
- [Kurz-Prüfliste für diesen Abschnitt](#kurz-prüfliste-für-diesen-abschnitt)

## 4.1 Nachahmer

### 4.1 (a) Eigene Ideen statt Klone

**Kern der Regel** – Apple erwartet, dass eine App eine eigene Idee umsetzt und nicht ein bereits im Store vorhandenes Produkt in Name, Icon, Oberfläche oder Funktionsumfang nachbaut. Wer ein erfolgreiches Spiel oder Tool sichtbar kopiert, riskiert die Ablehnung, auch wenn der Code selbst geschrieben ist.

**Risikostufe** – Hoch. Klone verwirren Nutzer und verwässern den Store; bei Wiederholung drohen Konsequenzen für den Entwickler-Account.

**Woran du es im Code erkennst**
- Swift/Objective-C: `CFBundleDisplayName`, `CFBundleName`, Asset-Katalog `AppIcon`, `Localizable.strings` mit fremden Produktnamen.
- React Native/Expo: `app.json` / `app.config.js` → `expo.name`, `expo.slug`, `expo.icon`; `package.json` → `name`.

**Typische Verstöße**
- ❌ Puzzle-App mit fünf Buchstaben, sechs Versuchen, gelb-grünem Farbschema und Name „Wordly“.
- ✅ Eigenes Konzept mit eigener Marke; Ähnlichkeiten beschränken sich auf Genre-Konventionen.

**Prüfliste**
- [ ] App-Name, Slug und Icon erinnern nicht an ein bekanntes Store-Produkt.
- [ ] UI-Assets stammen nicht erkennbar aus einer fremden App.

### 4.1 (b) Identitätsmissbrauch anderer Apps oder Marken

**Kern der Regel** – Eine App darf nicht vorgeben, von einem anderen Unternehmen, einer anderen App oder einem anderen Entwickler zu stammen. Das betrifft Name, Entwicklername, Icon, Splash-Screen und Beschreibungstexte – auch dann, wenn die App tatsächlich Daten oder Dienste der fremden Marke nutzt.

**Risikostufe** – Kritisch. Impersonation gilt als Täuschung und kann zur sofortigen Entfernung und Account-Sperre führen.

**Woran du es im Code erkennst**
- Bundle-ID mit fremdem Firmennamen (`com.instagram.*`, `de.sparkasse.*`); Strings wie „Official“/„Offiziell“ neben fremden Marken.
- React Native/Expo: `expo.ios.bundleIdentifier`, `expo.name`, `expo.description`; fremde Logos unter `assets/`.

**Typische Verstöße**
- ❌ Inoffizieller Bank-Client mit Bank-Logo als Icon und Bundle-ID `de.deutschebank.mobile2`; ✅ „Fahrplan-Helfer für DB-Daten“ mit eigenem Icon und Unabhängigkeitshinweis.

**Prüfliste**
- [ ] Bundle-ID enthält keinen fremden Firmennamen.
- [ ] Kein fremdes Logo als App-Icon, Splash oder Login-Bild.

### 4.1 (c) Marken- und Brandnutzung

**Kern der Regel** – Geschützte Marken, Logos und Namen Dritter dürfen nur mit Erlaubnis verwendet werden, und auch dann nicht so, dass der Eindruck einer offiziellen App entsteht. Das gilt ebenso für Apple-Marken und Produktnamen im App-Titel oder Icon.

**Risikostufe** – Hoch. Markeninhaber melden Verstöße direkt an Apple; die App geht dann bis zur Klärung offline.

**Woran du es im Code erkennst**
- Strings, Asset-Namen und Metadaten nach Marken durchsuchen: `iPhone`, `AirPods`, `WhatsApp`, `Spotify`, Vereinswappen, Automarken.
- Logos in `Assets.xcassets` bzw. `assets/` ohne Lizenzhinweis im Repo.

**Typische Verstöße**
- ❌ App-Name „iPhone Cleaner Pro“ oder Icon mit Apple-Logo.
- ✅ Generische Symbole, Marken nur beschreibend im Text („kompatibel mit …“).

**Prüfliste**
- [ ] Keine Apple-Produktnamen im App-Namen oder Icon.
- [ ] Für jedes fremde Logo im Asset-Katalog existiert eine Nutzungserlaubnis.

## 4.2 Mindestfunktionalität

### 4.2 Mindestfunktionalität (Grundregel)

**Kern der Regel** – Eine App muss mehr sein als eine verpackte Website, ein Werbeprospekt oder eine Linksammlung. Apple erwartet echten Nutzen oder Unterhaltung über eine native Oberfläche. Eine reine WebView-Hülle, die eine mobile Website lädt, wird als „nicht mehr als eine Website“ abgelehnt, ebenso Apps, deren einziger Inhalt Werbung oder eine Preisliste ist.

**Risikostufe** – Kritisch. Standardablehnung für Agentur- und Marketing-Apps; der Reviewer prüft explizit, ob es einen Unterschied zum Safari-Aufruf gibt.

**Woran du es im Code erkennst**
Swift/Objective-C:
- `import WebKit` und `WKWebView` im Root-ViewController oder in der einzigen SwiftUI-View; kein weiterer Controller/View mit eigener Logik.
- Kaum Model-, Netzwerk- oder Persistenzcode (`URLSession`, `CoreData`, `SwiftData` fehlen), dafür `NSAllowsArbitraryLoads` in der `Info.plist`.

React Native/Expo:
- `react-native-webview` als einzige nennenswerte Abhängigkeit; `App.tsx` rendert `<WebView source={{ uri: ... }} />` ohne Navigation.
- Kein `@react-navigation/*`, `expo-router` mit nur einer Route, keine nativen Module (Kamera, Standort, Notifications).

**Typische Verstöße**
- ❌ Swift:
  ```swift
  let web = WKWebView(frame: view.bounds)          // einziger Screen der App
  web.load(URLRequest(url: URL(string: "https://firma.de")!))
  view.addSubview(web)
  ```
- ❌ React Native:
  ```tsx
  export default function App() {
    return <WebView source={{ uri: "https://shop.example" }} />;
  }
  ```
- ✅ Native Navigation, Offline-Daten, Push, Kamera-Scan oder Widgets ergänzen die Webinhalte; WebView nur für einzelne Inhaltsseiten.

**Prüfliste**
- [ ] Mindestens ein Screen mit nativer Logik, der sich nicht auf einen WebView beschränkt.
- [ ] Erkennbarer Mehrwert gegenüber dem Aufruf der Website in Safari.

**Empfohlene Behebung** – Native Funktionen ergänzen: `expo-notifications`, `expo-camera`, `expo-location`, `expo-sqlite`; bare RN: `@notifee/react-native`, `react-native-vision-camera`, `@react-native-async-storage/async-storage`. Swift: SwiftUI-Screens, `WidgetKit`, `App Intents`.

### 4.2.1 ARKit-Apps

**Kern der Regel** – Wer ARKit einbindet, muss ein ausgereiftes AR-Erlebnis liefern. Ein einzelnes 3D-Modell auf einer erkannten Ebene oder ein AR-Modus als Marketing-Gag genügt nicht.

**Risikostufe** – Mittel. Betrifft wenige Apps, führt dann aber oft zu Nachfragen nach Demo-Videos.

**Woran du es im Code erkennst**
- Swift: `import ARKit`, `import RealityKit`, `ARView`; `UIRequiredDeviceCapabilities` enthält `arkit`. React Native/Expo: `@reactvision/react-viro`.

**Typische Verstöße**
- ❌ Button „In AR ansehen“ zeigt ein statisches USDZ ohne Interaktion – dafür reicht `QLPreviewController`.
- ✅ Platzieren, Skalieren, Vermessen oder Spielmechanik mit Tracking und Interaktion.

**Prüfliste**
- [ ] AR-Funktion bietet Interaktion über reine Anzeige hinaus.

### 4.2.2 Reine Marketing-Inhalte

**Kern der Regel** – Apps, die nur Werbung, Kataloge, Prospekte oder Produktblätter zeigen, gehören nicht in den Store. Ein Katalog braucht mindestens Bestellung, Merkliste, Verfügbarkeitsprüfung oder Personalisierung.

**Risikostufe** – Hoch. Wird zusammen mit der Grundregel 4.2 geprüft.

**Woran du es im Code erkennst**
- Nur statische JSON-/Markdown-Inhalte im Bundle, keine Interaktion außer Blättern.

**Typische Verstöße**
- ✅ Katalog mit Bestellung, Bestandsabfrage, Favoriten und Push bei Verfügbarkeit.

**Prüfliste**
- [ ] Inhalte sind interaktiv nutzbar, nicht nur konsumierbar.

### 4.2.3 Eigenständigkeit und Nachlade-Downloads

**Kern der Regel** – (i) Eine App muss ohne Zwangsinstallation einer weiteren App funktionieren; Hinweise auf Companion-Apps sind erlaubt, ein harter Blocker nicht. (ii) Lädt die App nach dem Start größere Datenmengen nach, muss das vorher offengelegt werden, und die App darf nicht mit leerem Screen hängen.

**Risikostufe** – Mittel. Reviewer scheitern beim Testen, wenn die App ohne Zweit-App nicht startet – das führt sofort zur Ablehnung.

**Woran du es im Code erkennst**
- Swift: `UIApplication.shared.canOpenURL(URL(string: "otherapp://"))` gefolgt von Blockier-Alert; `SKStoreProductViewController` beim Start; `NSBundleResourceRequest` oder `URLSessionDownloadTask` im ersten Launch ohne Hinweis.
- React Native/Expo: `Linking.canOpenURL('otherapp://')` mit Bedingung im Root; `expo-file-system` `downloadAsync` im Onboarding ohne Größenangabe.

**Typische Verstöße**
- ❌ Swift:
  ```swift
  if !UIApplication.shared.canOpenURL(URL(string: "companion://")!) {
    showBlockingAlert("Bitte zuerst die Companion-App installieren")
  }
  ```
- ✅ Companion-App optional; Download-Dialog nennt Größe, zeigt Fortschritt und bietet Abbruch.

**Prüfliste**
- [ ] Kein Start-Blocker, der eine andere App voraussetzt.
- [ ] Nachlade-Downloads werden mit Größe angekündigt; Fortschritt und Abbruch sichtbar.

### 4.2.4 und 4.2.5 (entfällt)

4.2.4 und 4.2.5 – entfällt (von Apple gestrichen). Ehemals Regeln zu Apple-Watch-Apps ohne eigenständigen Nutzen und zu iOS-Apps in macOS-Umgebungen; heute unter 2.4 und 4.2 mitbehandelt.

### 4.2.6 Template- und Generator-Apps

**Kern der Regel** – Apps aus einem App-Baukasten oder einer kommerziellen Vorlage sind nur zulässig, wenn der Inhaber der Inhalte sie unter seinem eigenen Entwickler-Account einreicht. Ein Agentur- oder Plattformkonto mit Dutzenden Kunden-Apps wird als Spam gewertet.

**Risikostufe** – Hoch. Apple prüft den Entwickler-Account und die Ähnlichkeit zu anderen Binaries desselben Accounts.

**Woran du es im Code erkennst**
- Konfigurationsdatei wie `config.json`, `tenant.json`, `brand.plist`, aus der Name, Farben und API-Endpunkt gelesen werden; Bundle-IDs nach Muster `com.agentur.kunde123`.
- React Native/Expo: `app.config.js` mit `process.env.CLIENT_ID`-Abzweigung für Name, Icon und Bundle-ID; EAS-Profile pro Kunde.

**Typische Verstöße**
- ❌ Ein Account, 40 Restaurant-Apps mit identischem Code und geänderter Speisekarte.
- ✅ Jeder Kunde reicht seine Variante unter eigenem Konto ein – oder eine Container-App zeigt Kunden als Inhalte.

**Prüfliste**
- [ ] Einreichender Account gehört dem Inhaber der Inhalte.
- [ ] Bei White-Label-Code: Kunden-Konten dokumentiert (Team-ID in `project.pbxproj` / `eas.json`).

### 4.2.7 Remote-Desktop-Clients

**Kern der Regel** – (a) Ein Remote-Desktop-Client darf sich nur mit einem Host verbinden, den der Nutzer selbst besitzt oder kontrolliert, typischerweise im lokalen Netzwerk oder über eine vom Nutzer eingerichtete Verbindung. (b) Die Software läuft auf dem Host; der Client darf keinen Katalog von Spielen oder Apps anbieten, der als Umgehung des App Stores wirkt.

**Risikostufe** – Mittel. Streng geprüft bei Cloud-Gaming- und Cloud-PC-Angeboten.

**Woran du es im Code erkennst**
- Swift: `Network.framework`, `NSBonjourServices`, `NSLocalNetworkUsageDescription`; VNC/RDP-Bibliotheken (`libvncserver`, `FreeRDP`).
- React Native/Expo: `react-native-tcp-socket`, `react-native-zeroconf`, `expo-network`.
- Verdächtig: fest verdrahtete Anbieter-Server, ein integrierter Spiele-Katalog, Bezahlfluss für Hosting-Zeit ohne IAP (Abschnitt 3).

**Typische Verstöße**
- ❌ Client zeigt Katalog gemieteter Windows-Instanzen mit vorinstallierten Spielen, Auswahl per Kachel.
- ✅ Verbindung nur zu vom Nutzer eingetragenen Hosts; Anzeige spiegelt den Host-Desktop 1:1.

**Prüfliste**
- [ ] Verbindungsziel ist nutzerdefiniert (Host-Adresse, Pairing-Code), nicht ein Anbieter-Katalog.

## 4.3 Spam

### 4.3 (a) Keine fast identischen Apps und gesättigte Kategorien

**Kern der Regel** – Ein Entwickler soll nicht mehrere Apps veröffentlichen, die sich nur in Name, Icon oder Inhalt marginal unterscheiden – lieber eine App mit Auswahl als zehn Varianten. Zusätzlich lehnt Apple neue Einreichungen in gesättigten Kategorien ab (Furz-, Rülps-, Taschenlampen-, Wahrsage-, Dating-, Kamasutra-Apps), sofern sie nichts Neues bieten.

**Risikostufe** – Hoch. Bei mehrfachen Verstößen wird der Account aus dem Developer Program entfernt.

**Woran du es im Code erkennst**
- Mehrere Targets im selben Xcode-Projekt mit identischem Code und unterschiedlichen `PRODUCT_BUNDLE_IDENTIFIER`; `xcconfig`-Dateien pro Variante.
- React Native/Expo: `app.config.js` mit `APP_VARIANT`-Switch für Namen; mehrere EAS-Profile mit unterschiedlichen `bundleIdentifier`, aber gleichem Quellcode.

**Typische Verstöße**
- ❌ `app.config.js`:
  ```js
  const variant = process.env.APP_VARIANT; // "hunde", "katzen", "pferde"
  export default { name: `${variant}-Wallpaper`, ios: { bundleIdentifier: `com.x.${variant}` } };
  ```
- ✅ Eine App mit Themen-Auswahl oder IAP-Paketen.

**Prüfliste**
- [ ] Keine Build-Varianten, die als eigenständige Store-Apps mit identischem Funktionsumfang enden.

### 4.3 (b) Keine Bundle-ID-Duplikate; kein Missbrauch von Live Activities, Push und Game Center

**Kern der Regel** – Dieselbe App darf nicht unter mehreren Bundle-IDs oder Kategorien eingestellt werden, um Sichtbarkeit zu erschleichen. Live Activities, Push-Benachrichtigungen und Game Center dürfen weder für Spam noch für Phishing oder aufdringliche Werbung eingesetzt werden.

**Risikostufe** – Hoch. Push-Spam und Phishing über Apple-Dienste gehören zu den direkten Sperrgründen.

**Woran du es im Code erkennst**
- `ActivityKit` → `Activity<Attributes>.request(...)`: bildet der Inhalt einen laufenden Vorgang ab oder ein Dauerbanner? Expo: `expo-live-activity` oder Custom Target.
- Game Center: `GKMatchmaker`, Einladungen an Freunde in Schleifen.

**Typische Verstöße**
- ✅ Live Activity zeigt Lieferstatus, Timer, Spielstand; Push nur für ereignisbezogene Inhalte.

**Prüfliste**
- [ ] Nur eine Bundle-ID pro tatsächlicher App.
- [ ] Live Activities bilden reale, zeitlich begrenzte Vorgänge ab.

## 4.4 Erweiterungen

### 4.4 Erweiterungen (Grundregel)

**Kern der Regel** – App-Erweiterungen (Widgets, Share-, Action-, Notification-, Keyboard-, Safari-Extensions) müssen den App Extension Programming Guide einhalten, dürfen kein eigenes Marketing enthalten und keine In-App-Käufe im Erweiterungs-Kontext abwickeln. Die Host-App muss klar machen, welche Erweiterungen sie mitliefert.

**Risikostufe** – Mittel. Extensions werden mitgeprüft, sobald ein Extension-Target im Binary steckt.

**Woran du es im Code erkennst**
- Xcode: `project.pbxproj` mit `productType = "com.apple.product-type.app-extension"`; Extension-`Info.plist` → `NSExtension` → `NSExtensionPointIdentifier`.
- Expo: `@bacons/apple-targets` (Ordner `targets/`), Widget-Plugins; bare RN: manuelle Targets unter `ios/`.

**Prüfliste**
- [ ] Alle `NSExtensionPointIdentifier` im Projekt erfasst.
- [ ] Kein `StoreKit`-Kaufaufruf und kein Marketing innerhalb eines Extension-Targets.

### 4.4.1 Keyboard-Erweiterungen

**Kern der Regel** – Eine Tastatur-Erweiterung muss ohne Netzwerkzugriff funktionieren, sofort tippbar sein, den Wechsel zur nächsten Tastatur ermöglichen und Zahlen- sowie Dezimaltastaturen liefern, wenn ein Textfeld sie anfordert. Tastendaten dürfen nur gesammelt werden, wenn das für die Funktion nötig ist; Marketing, Werbung oder Datensammlung als Zweck sind unzulässig.

**Risikostufe** – Hoch. Apple sieht Tastaturen als potenzielle Keylogger; `RequestsOpenAccess` ohne klaren Grund löst Nachfragen aus.

**Woran du es im Code erkennst**
- Extension-`Info.plist`: `NSExtensionPointIdentifier = com.apple.keyboard-service`, darunter `NSExtensionAttributes` → `RequestsOpenAccess` (Bool), `IsASCIICapable`, `PrimaryLanguage`.
- Swift: `UIInputViewController`, `textDocumentProxy`, `needsInputModeSwitchKey`; `hasFullAccess` in Kombination mit `URLSession` in der Extension.
- Datensammlung: `documentContextBeforeInput` wird an Analytics-SDKs übergeben; `UIPasteboard` in der Extension.
- Zahlentastatur: Umgang mit `textDocumentProxy.keyboardType == .numberPad` / `.decimalPad`.
- React Native/Expo: nicht mit JS realisierbar; nur über `@bacons/apple-targets` (`type: "keyboard"`) oder native Targets – dort dieselben Plist-Prüfungen.

**Typische Verstöße**
- ❌ `<key>RequestsOpenAccess</key><true/>` in einer reinen Emoji-Tastatur ohne Funktion, die Vollzugriff braucht.
- ✅ Wörterbuch lokal im Extension-Bundle, `RequestsOpenAccess = false`, Wechseltaste über `needsInputModeSwitchKey`.

**Prüfliste**
- [ ] Extension funktioniert ohne `hasFullAccess`.
- [ ] `RequestsOpenAccess` nur `true`, wenn zwingend nötig und in der Host-App erklärt.
- [ ] Zahlen-/Dezimal-Layout für `.numberPad`/`.decimalPad` vorhanden.
- [ ] Kein Werbe-Element; keine Weitergabe von Tastendaten an Analytics- oder Werbe-SDKs.

### 4.4.2 Safari-Erweiterungen

**Kern der Regel** – Safari-Web-Extensions dürfen nur in den Bereichen wirken, die ihr Manifest deklariert, dürfen Webseiteninhalte nicht ohne Nutzerwissen verfälschen (Affiliate-Links einschleusen, Werbung ersetzen) und dürfen Browsing-Daten nicht ohne Einwilligung sammeln oder weitergeben.

**Risikostufe** – Hoch. Content-Manipulation und heimliches Tracking führen zu sofortiger Ablehnung.

**Woran du es im Code erkennst**
- Target mit `NSExtensionPointIdentifier = com.apple.Safari.web-extension`; `manifest.json` mit `permissions` (`<all_urls>`, `tabs`, `webRequest`, `cookies`, `history`).
- `content.js`/`background.js`: DOM-Manipulation, die `href` umschreibt oder Drittskripte nachlädt; `fetch` an Tracking-Endpunkte mit `document.location`.
- React Native/Expo: nur über native Targets, Prüfung wie oben.

**Typische Verstöße**
- ❌ `document.querySelectorAll('a[href*="amazon."]').forEach(a => a.href += "&tag=meinaffiliate");`
- ✅ Minimale Host-Permissions, Verhalten in der Host-App beschrieben, Datenschutzhinweis mit Opt-in.

**Prüfliste**
- [ ] Manifest-Permissions auf das Notwendige begrenzt.
- [ ] Kein Umschreiben von Links, Preisen, Werbung oder Inhalten ohne sichtbare Nutzeraktion.
- [ ] Keine Übermittlung von URLs/Verlauf ohne Einwilligung.

### 4.4.3 Steuer- und Sticker-Erweiterungen

**Kern der Regel** – iMessage-Sticker-Packs sowie Erweiterungen mit Steuerelementen (Control Center Controls, Widgets, Shortcuts) müssen sich an Apples Dokumentation halten: Sticker müssen eigenes oder lizenziertes Bildmaterial sein, Controls dürfen nur tun, was ihr Label verspricht, und Erweiterungen sind keine Werbefläche.

**Risikostufe** – Niedrig bis Mittel. Sticker-Packs werden vor allem auf Urheberrecht (siehe 4.1) geprüft.

**Woran du es im Code erkennst**
- Sticker: Target vom Typ `messages-sticker-pack`, `Stickers.xcstickers`, `MSStickerBrowserViewController`.
- Controls/Widgets: `WidgetKit`, `ControlWidget`, `AppIntent`; Widget-Views mit Kaufaufforderung.
- Expo: `@bacons/apple-targets` mit `type: "widget"`, `"imessage"`, `"control"`.

**Typische Verstöße**
- ❌ Sticker-Pack mit bekannten Comic-Figuren ohne Lizenz; Widget zeigt dauerhaft „Upgrade auf Pro“.
- ✅ Sticker aus eigener Produktion; Widget zeigt Daten der App.

**Prüfliste**
- [ ] Sticker-Assets sind eigen oder lizenziert.
- [ ] Widgets/Controls liefern Inhalt oder Aktion, keine Werbung.

## 4.5 Apple-Websites und -Dienste

### 4.5.1 Nutzung nur laut Dokumentation

**Kern der Regel** – Apple-Dienste (App Store, Apple-Music-Katalog, Game Center, CloudKit, Push) dürfen nur wie dokumentiert genutzt werden. Das Scrapen von App-Store-Seiten, Ranglisten oder Bewertungen, das Nachbauen eines Store-Clients und das Auswerten von Store-Daten für eigene Charts sind unzulässig; zulässig sind die offiziellen RSS-Feeds und APIs.

**Risikostufe** – Mittel. Backend-Verstöße sind im App-Code selten sichtbar, Client-seitige Scraper dagegen schon.

**Woran du es im Code erkennst**
- Strings mit `apps.apple.com` in Kombination mit HTML-Parsern (`SwiftSoup`, `Kanna`, `cheerio`, `node-html-parser`); `itunes.apple.com/lookup` und `/search` sind dokumentiert und erlaubt.

**Typische Verstöße**
- ❌ `SwiftSoup.parse(html)` auf `https://apps.apple.com/de/charts/iphone`.
- ✅ Offizieller RSS-Feed-Generator oder App Store Connect API (serverseitig).

**Prüfliste**
- [ ] Keine HTML-Extraktion von Apple-Seiten im Client; Apple-Daten nur über dokumentierte Feeds/APIs.

### 4.5.2 Apple Music und MusicKit

**Kern der Regel** – Apps mit MusicKit dürfen Apple-Music-Inhalte nur zur Wiedergabe über die Bibliothek des Nutzers verwenden. Streams dürfen nicht mitgeschnitten, exportiert, hinter eigene Bezahlschranken gestellt oder mit Werbung gekoppelt werden; der Nutzer muss die Wiedergabe steuern können, und Metadaten dürfen nicht als eigene Inhalte ausgegeben werden. Nutzer ohne Abo werden auf Apple Music verwiesen, nicht ausgesperrt.

**Risikostufe** – Mittel. Apple prüft MusicKit-Apps auf Lizenzkonformität, vor allem bei Hintergrundmusik in Video- oder Fitness-Apps.

**Woran du es im Code erkennst**
- Swift: `import MusicKit`, `MusicAuthorization.request()`, `ApplicationMusicPlayer`, `SystemMusicPlayer`; älter `MPMusicPlayerController`, `SKCloudServiceController`.
- `Info.plist` → `NSAppleMusicUsageDescription`; Capability „MusicKit“ (Media Services) in der App ID; Developer Token (JWT mit `iss`, `kid`) im Code.
- React Native/Expo: `@lomray/react-native-apple-music`, Config Plugin für `NSAppleMusicUsageDescription`; `expo-music-library` (nur lokale Bibliothek).
- Verdächtig: `AVAudioEngine`-Tap oder `AVAssetExportSession` auf geschützte Items; Wiedergabe ohne sichtbare Steuerung; Play/Pause an Ads gekoppelt.

**Typische Verstöße**
- ❌ Workout-Video wird mit Apple-Music-Track exportiert und geteilt.
- ✅ Wiedergabe über `ApplicationMusicPlayer` mit Standard-Steuerung, Verweis auf Apple Music bei fehlendem Abo.

**Prüfliste**
- [ ] `NSAppleMusicUsageDescription` beschreibt den Zweck.
- [ ] Keine Aufnahme, kein Export, kein Mitschnitt von Apple-Music-Audio.
- [ ] Wiedergabesteuerung vorhanden; kein eigener Bezahlweg für Apple-Music-Inhalte.

### 4.5.3 Kein Spam über Apple-Dienste

**Kern der Regel** – Game Center, iMessage, Kontakte, Kalender oder Push dürfen nicht dazu dienen, ungefragt Nachrichten oder Einladungen an Dritte zu senden. Kontaktdaten dürfen nicht ausgelesen werden, um Werbeempfänger zu gewinnen.

**Risikostufe** – Kritisch. Verbindung zu 5.1.1/5.1.2; Massen-Einladungen sind ein klassischer Sperrgrund.

**Woran du es im Code erkennst**
- Swift: `CNContactStore.enumerateContacts` gefolgt von Upload; `MFMessageComposeViewController` mit vorbefüllten Empfängerlisten; `GKMatchmakerViewController` Auto-Invite; `EKEventStore` mit Massen-Inserts.
- React Native/Expo: `expo-contacts` → `getContactsAsync` mit anschließendem `fetch` ans Backend; `expo-sms` `sendSMSAsync` mit Kontaktliste; `react-native-contacts`.

**Typische Verstöße**
- ❌ Expo:
  ```ts
  const { data } = await Contacts.getContactsAsync({ fields: [Contacts.Fields.PhoneNumbers] });
  await SMS.sendSMSAsync(data.flatMap(c => c.phoneNumbers.map(p => p.number)), "Lade dich ein!");
  ```
- ✅ Einladung einzeln über Share-Sheet (`UIActivityViewController` / `expo-sharing`); Empfänger wählt der Nutzer.

**Prüfliste**
- [ ] Keine automatische Nachricht an mehrere Kontakte.
- [ ] Kontaktdaten verlassen das Gerät nur mit klarer Einwilligung und Zweck.

### 4.5.4 Push-Benachrichtigungen

**Kern der Regel** – Push muss optional sein: Die App bleibt ohne Push voll nutzbar, der Systemdialog ist kein Gate, und Push-Inhalte enthalten keine sensiblen oder vertraulichen Daten. Werbe- und Marketing-Pushes sind nur mit ausdrücklicher, vom Systemdialog getrennter Zustimmung erlaubt und müssen in der App abbestellbar sein. Ein Erklär-Screen vor dem Systemprompt wird empfohlen; der Prompt beim ersten Launch ohne Kontext ist ein typischer Ablehnungsgrund.

**Risikostufe** – Hoch. Push-Verstöße sind einfach zu testen und werden häufig gemeldet.

**Woran du es im Code erkennst**
Swift/Objective-C:
- `UNUserNotificationCenter.current().requestAuthorization(options:)` in `application(_:didFinishLaunchingWithOptions:)`, im `App.init()` oder im `.onAppear` der Root-View → Prompt beim ersten Start.
- `registerForRemoteNotifications()` ohne vorherigen Erklär-Screen; Blockier-Alert bei `.denied`.

React Native/Expo:
- `expo-notifications` → `Notifications.requestPermissionsAsync()` im Root-`useEffect` von `App.tsx` / `app/_layout.tsx`.
- `@react-native-firebase/messaging` → `messaging().requestPermission()` beim Start; `@notifee/react-native` `requestPermission()`.
- Kein Settings-Screen mit Toggle für Marketing-Pushes; kein Backend-Flag `marketingOptIn`.

**Typische Verstöße**
- ❌ Swift:
  ```swift
  // in application(_:didFinishLaunchingWithOptions:)
  UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { _, _ in }
  ```
- ❌ Expo: `useEffect(() => { Notifications.requestPermissionsAsync(); }, []);` in `_layout.tsx`.
- ❌ Push-Payload enthält Kontostand, Diagnose oder Passwort-Reset-Code im Klartext.
- ✅ Erklär-Screen mit „Später“, Systemdialog erst nach Aktion; Schalter „Angebote und Neuigkeiten“, Standard aus.

**Prüfliste**
- [ ] Systemdialog nicht beim ersten Start ohne Kontext.
- [ ] App bleibt bei abgelehnter Berechtigung voll nutzbar.
- [ ] Keine sensiblen Daten in Push-Inhalten.
- [ ] Marketing-Push nur mit separatem Opt-in und In-App-Abmeldung.

**Empfohlene Behebung** – Expo: `expo-notifications` mit `getPermissionsAsync()` vor `requestPermissionsAsync()`, Prompt erst nach Erklär-Screen; bare RN: `@notifee/react-native` oder `@react-native-firebase/messaging` mit gleichem Muster. Swift: Prompt erst nach Nutzeraktion, `.provisional` als sanfte Alternative; Marketing-Opt-in als eigenes Flag persistieren.

### 4.5.5 Game Center Player-IDs

**Kern der Regel** – Game-Center-Spieler-IDs dürfen weder Dritten offengelegt noch zu Profilen außerhalb des Spiels zusammengeführt werden. Anzeigenamen und Avatare anderer Spieler erscheinen nur im Spielkontext.

**Risikostufe** – Mittel. Betrifft nur Spiele mit Game Center, dann aber klar prüfbar.

**Woran du es im Code erkennst**
- Swift: `GKLocalPlayer.local.gamePlayerID`, `teamPlayerID`, veraltet `playerID`; Übergabe an Analytics (`setUserID(gamePlayerID)`), Werbenetzwerke oder CRM.
- `GKPlayer.displayName` in Leaderboards außerhalb des Spiels ohne serverseitige Signaturprüfung (`fetchItems(forIdentityVerificationSignature:)`).

**Typische Verstöße**
- ❌ `gamePlayerID` als Attribution-Key an ein Ad-SDK.
- ✅ ID nur für Spielstand-Sync und Matchmaking; Server verifiziert Signatur.

**Prüfliste**
- [ ] Player-IDs werden nicht an Dritt-SDKs übergeben.

### 4.5.6 Apple-Emoji

**Kern der Regel** – Apples Emoji-Grafiken dürfen nur so genutzt werden, wie das System sie darstellt: als Unicode-Zeichen im Text. Extrahierte Emoji-Bitmaps als Assets, Sticker, Icons, Marketing-Bilder oder App-Icons sind unzulässig.

**Risikostufe** – Mittel. Leicht erkennbar im Asset-Katalog; Emoji-Sticker-Packs und Emoji-App-Icons werden zuverlässig abgelehnt.

**Woran du es im Code erkennst**
- Assets mit Namen wie `emoji_smile.png`, `apple_emoji_*`, `1F600.png`, Ordner `emoji/` mit Apple-Glyphen; App-Icon aus Emoji gerendert.
- React Native/Expo: `assets/emoji/*.png`, `react-native-view-shot` auf Emoji-Views; `apple-color-emoji.ttf` im Bundle.

**Typische Verstöße**
- ❌ iMessage-Sticker-Pack aus Apple-Emoji-Bitmaps; App-Icon ist das 🔥-Emoji.
- ✅ Emoji als Unicode-Text in Labels; für Assets eigene Illustrationen oder lizenzierte Sets (Twemoji, Noto Emoji mit Lizenzhinweis).

**Prüfliste**
- [ ] Keine Apple-Emoji-Bitmaps im Asset-Katalog oder `assets/`.
- [ ] App-Icon und Sticker sind keine Apple-Emoji; keine Emoji-zu-Bild-Exportfunktion.

## 4.6 entfällt

4.6 – entfällt (von Apple gestrichen). Ehemals Regel zu alternativen App-Icons, heute Teil von 2.3 und 4.1.

## 4.7 Mini-Apps, Mini-Games, Streaming-Games, Chatbots, Plug-ins, Game-Emulatoren

**Kern der Regel** – Eine App darf Software anbieten, die nicht im Binary steckt: HTML5-Mini-Apps und -Spiele, gestreamte Spiele, Chatbots, Plug-ins und Retro-Spiele in Emulatoren. Bedingungen: Die Inhalte halten alle Guidelines ein (Datenschutz, Inhalte, IAP), die Altersfreigabe der Container-App entspricht dem freizügigsten eingebetteten Inhalt, es gibt Inhaltsfilter und Meldefunktion, und der Entwickler der Container-App haftet für alles, was darin läuft. Native Plattform-APIs werden nur über die Container-App bereitgestellt, nicht direkt aus eingebettetem Code. Digitale Güter in Mini-Apps unterliegen der IAP-Pflicht. Für Retro-Konsolen-Emulatoren gilt eine Ausnahme: ROMs dürfen geladen werden, das Urheberrecht bleibt Sache von Entwickler und Nutzer.

**Risikostufe** – Hoch. Container-Apps werden intensiv auf Altersfreigabe, eingebettete Bezahlwege und die Möglichkeit unmoderierter Inhalte geprüft.

**Woran du es im Code erkennst**
Swift/Objective-C:
- `WKWebView` mit `WKUserContentController.add(_:name:)`-Handlern, die JS-Aufrufe an native Funktionen (Kamera, Zahlung, Kontakte) weiterreichen; `JSContext` mit heruntergeladenen Skripten; dynamische Ladepfade mit `.js`/`.wasm` in `Caches/`.
- Emulator: Frameworks mit Namen bekannter Cores (`libretro`, `mgba`, `snes9x`, `ppsspp`), `UTImportedTypeDeclarations` für ROM-Typen (`.gba`, `.nes`, `.iso`).
- Chatbot: LLM-SDKs (`OpenAI`, `Anthropic`) ohne Moderations-Layer, Meldefunktion oder Altersfreigabe (siehe 1.2).
- Bezahlung: Bridge-Handler mit `purchase`, `checkout`, `stripe` aus dem eingebetteten Content ohne `StoreKit`.

React Native/Expo:
- `react-native-webview` mit `injectedJavaScript` und `onMessage`-Bridge zu nativen Modulen; eigene Mini-App-Loader über `expo-file-system` mit Registry-JSON und URLs.
- Dynamische Bundle-Loader („Super-App“-Frameworks), Emulator-Cores als native Module, `expo-document-picker` mit ROM-Endungen.

**Typische Verstöße**
- ❌ Swift:
  ```swift
  config.userContentController.add(self, name: "native")
  // JS: window.webkit.messageHandlers.native.postMessage({ action: "buy", sku: "coins100", url: "https://pay.example" })
  ```
  – Kauf digitaler Güter aus einer Mini-App am IAP vorbei.
- ❌ Container-App mit Freigabe 4+ hostet Mini-Games mit Glücksspielmechanik oder Gewalt.
- ❌ Mini-App greift über die Bridge auf Kontakte zu, ohne dass die Container-App die Berechtigung erklärt.
- ✅ Mini-App-Katalog mit Altersfreigabe je Inhalt, Container-Rating auf Höchstwert, Käufe über `StoreKit`/`react-native-iap`, Melde-Button in jeder Mini-App.
- ✅ Retro-Emulator: Nutzer importiert eigene ROMs per Dateiauswahl; keine vorinstallierten oder verlinkten kommerziellen ROMs.

**Prüfliste**
- [ ] Altersfreigabe der Container-App entspricht dem freizügigsten eingebetteten Inhalt.
- [ ] Filter- und Meldefunktion vorhanden; Bridge gibt keine System-APIs frei, die die Container-App nicht selbst mit Zweck anfordert.
- [ ] Digitale Güter innerhalb von Mini-Apps laufen über IAP.

**Empfohlene Behebung** – Bezahlung über `react-native-iap` (Expo Dev Client) bzw. `StoreKit 2`; Moderation über eigenes Backend plus Sperrlisten; Altersfreigabe in App Store Connect anpassen; für Chatbots Abschnitt 1.2 anwenden.

## 4.8 Login-Dienste

**Kern der Regel** – Bietet eine App einen Login über Drittanbieter (Google, Facebook, X, Microsoft, LinkedIn) zur Konto-Erstellung oder Anmeldung an, muss sie gleichwertig eine Option anbieten, die (1) nur Name und E-Mail erhebt, (2) dem Nutzer erlaubt, seine E-Mail zu verbergen (Relay-Adresse), und (3) keine Nutzerdaten für Werbe-Tracking ohne Einwilligung sammelt. Sign in with Apple erfüllt alle drei Punkte und ist der einfachste Weg; ein anderer Dienst ist zulässig, wenn er dieselben Kriterien erfüllt. Ausnahmen: ausschließlich eigenes Konto-System; Bildungs- oder Enterprise-App mit bestehendem Login; behördliche oder branchenspezifische Identitäten (eID, Bürger-ID); Client für einen bestimmten Drittanbieterdienst, dessen Login zwingend über diesen Dienst läuft.

**Risikostufe** – Hoch. Wird bei jeder Einreichung mit Social-Login-SDK geprüft; Reviewer testen den Login-Screen direkt.

**Woran du es im Code erkennst**
Swift/Objective-C:
- Drittanbieter-Imports: `import GoogleSignIn`, `import FBSDKLoginKit`, `import FacebookLogin`, `import MSAL`, `import FirebaseAuth` mit `GoogleAuthProvider`/`FacebookAuthProvider`/`OAuthProvider(providerID: "twitter.com")`.
- Fehlt dann: `import AuthenticationServices`, `ASAuthorizationAppleIDButton`, `ASAuthorizationAppleIDProvider`, `SignInWithAppleButton` (SwiftUI), Entitlement `com.apple.developer.applesignin` in `.entitlements`.
- Apple-Button kleiner, versteckt oder erst nach „Weitere Optionen“ – Apple fordert gleichwertige Platzierung.

React Native/Expo:
- Drittanbieter: `@react-native-google-signin/google-signin`, `react-native-fbsdk-next`, `expo-auth-session/providers/google` bzw. `.../facebook`, `@react-native-firebase/auth` mit `GoogleAuthProvider`, `react-native-app-auth` gegen Google/Microsoft.
- Fehlt dann: `expo-apple-authentication` (`AppleAuthentication.signInAsync`, `AppleAuthenticationButton`), bare RN `@invertase/react-native-apple-authentication`; `app.json` → `expo.ios.usesAppleSignIn: true`.
- Auth-Anbieter (Supabase, Auth0, Clerk, Firebase) mit aktivierten Social-Providern, aber ohne Apple-Provider in der Client-Konfiguration.

**Typische Verstöße**
- ❌ Swift:
  ```swift
  GIDSignIn.sharedInstance.signIn(withPresenting: self) { ... }
  LoginManager().logIn(permissions: ["email"], from: self) { ... }
  // kein ASAuthorizationAppleIDProvider im Projekt
  ```
- ❌ Expo:
  ```tsx
  import * as Google from "expo-auth-session/providers/google";
  import * as Facebook from "expo-auth-session/providers/facebook";
  // package.json ohne expo-apple-authentication, app.json ohne usesAppleSignIn
  ```
- ✅ Apple-Button gleichwertig neben Google; Backend akzeptiert `privaterelay.appleid.com`; kein Tracking-SDK-Aufruf beim Login.

**Prüfliste**
- [ ] Bei Drittanbieter-Login existiert eine datensparsame Alternative (Sign in with Apple oder gleichwertig).
- [ ] Entitlement `com.apple.developer.applesignin` bzw. `usesAppleSignIn` gesetzt.
- [ ] Apple-Option gleichwertig sichtbar (Reihenfolge, Größe, Beschriftung nach Apple-Vorgaben).
- [ ] Backend akzeptiert Relay-E-Mails und fehlenden Namen bei erneutem Login.
- [ ] Kein Tracking-Aufruf im Login-Flow ohne ATT-Einwilligung (siehe 5.1.2).
- [ ] Falls keine Apple-Option: zutreffende Ausnahme im Bericht benannt und belegt.

**Empfohlene Behebung** – Expo: `expo-apple-authentication` plus `usesAppleSignIn`; bare RN: `@invertase/react-native-apple-authentication`; Firebase: Apple-Provider mit Nonce-Handling aktivieren; Swift: `AuthenticationServices` mit `ASAuthorizationController` und `getCredentialState`.

## 4.9 Apple Pay

**Kern der Regel** – Apps mit Apple Pay müssen die Apple-Pay-Marken- und UI-Richtlinien einhalten (Button aus `PassKit`, keine selbstgezeichneten Buttons), vor der Bestätigung alle wesentlichen Kaufinformationen zeigen (Preis, Steuern, Versand; bei wiederkehrenden Zahlungen Betrag und Intervall) und dürfen Daten aus Apple-Pay-Transaktionen nicht für Tracking, Profilbildung oder Weitergabe nutzen. Apple Pay gilt für physische Güter und Dienstleistungen; digitale Güter bleiben bei IAP (Abschnitt 3).

**Risikostufe** – Mittel. Falsche Buttons und fehlende Abo-Details werden erkannt; Missbrauch von Transaktionsdaten ist ein Datenschutzverstoß mit hoher Konsequenz.

**Woran du es im Code erkennst**
- Swift: `import PassKit`, `PKPaymentAuthorizationController`, `PKPaymentRequest`, `PKPaymentButton`; Entitlement `com.apple.developer.in-app-payments` mit Merchant-IDs; `PKRecurringPaymentRequest`/`PKRecurringPaymentSummaryItem` für Abos; `UIButton` mit Bild `apple_pay.png` statt `PKPaymentButton`; `billingContact`/`shippingContact` an Analytics oder Werbe-SDKs.
- React Native/Expo: `@stripe/stripe-react-native` (`PlatformPayButton`, `confirmPlatformPayPayment`), `react-native-payments`, Braintree-/Adyen-SDKs; `expo.ios.entitlements` mit `com.apple.developer.in-app-payments`; selbstgebaute Buttons mit `require('./apple-pay.png')`; Abo ohne `recurringPaymentRequest`.

**Typische Verstöße**
- ❌ `btn.setImage(UIImage(named: "applepay_black"), for: .normal)` als Apple-Pay-Button.
- ❌ Monatliches Abo über Apple Pay, Payment Sheet zeigt nur „Gesamt 9,99 €“ ohne „monatlich“.
- ✅ `PKPaymentButton(paymentButtonType: .subscribe, paymentButtonStyle: .black)`, `PKRecurringPaymentRequest` mit Intervall, Kontaktdaten nur für die Abwicklung.

**Prüfliste**
- [ ] Apple-Pay-Button stammt aus `PassKit` bzw. dem SDK-Button, nicht aus einem Bild.
- [ ] Wiederkehrende Zahlungen nennen Betrag, Intervall und Startdatum vor der Bestätigung; Gesamtbetrag inklusive Steuern/Versand.
- [ ] Keine Weitergabe von Kontakt- oder Tokendaten außerhalb der Zahlungsabwicklung.
- [ ] Apple Pay nicht für digitale In-App-Güter (siehe 3.1.1).

## 4.10 Monetarisierung eingebauter Systemfunktionen

**Kern der Regel** – Funktionen, die Gerät oder Betriebssystem ohnehin bereitstellen, dürfen nicht als kostenpflichtiges Feature verkauft werden: Push-Benachrichtigungen, Kamera, Mikrofon, Gyroskop und andere Sensoren, Apple-Dienste wie Wallet, Continuity, Handoff, AirDrop, iCloud-Sync, Siri. Eine App darf eigene Funktionen verkaufen, die diese Fähigkeiten nutzen – aber nicht den bloßen Zugang zur Systemfunktion.

**Risikostufe** – Mittel. Wird vor allem bei „Pro“-Paywalls geprüft, die Systemfeatures als Verkaufsargument listen.

**Woran du es im Code erkennst**
- Paywall-Texte/`Localizable.strings` mit „Push-Benachrichtigungen freischalten“, „Kamera-Modus (Pro)“, „iCloud-Sync nur Premium“, „Wallet-Karte hinzufügen – Pro“; StoreKit-Produkt-IDs wie `push_unlock`, `camera_pro`, `icloud_sync`.
- Swift-Gates: `requestAuthorization` nur bei `isPro`; `AVCaptureSession`, `CMMotionManager`, `NSUbiquitousKeyValueStore`/CloudKit, `PKAddPassButton`, `NSUserActivity` (Handoff) hinter Abo-Flag.
- React Native/Expo: `react-native-purchases` / `react-native-iap` Entitlement-Checks vor `Notifications.requestPermissionsAsync()`, `expo-camera`, `expo-sensors`, `expo-sharing`.

**Typische Verstöße**
- ❌ RN-Paywall: `const features = ["Push-Erinnerungen", "Kamera-Scan", "iCloud-Backup", "Apple Wallet Pass"];`
- ❌ Swift: `guard isPro else { return }` vor `UNUserNotificationCenter.current().requestAuthorization`.
- ✅ Verkauft werden eigene Leistungen: erweiterte Erinnerungs-Logik, Auswertungen, Speicher auf eigenem Backend, zusätzliche Level.

**Prüfliste**
- [ ] Keine Paywall-Formulierung, die eine Systemfähigkeit als Kaufobjekt nennt.
- [ ] Systemfunktionen (Push, Kamera, Sensoren, Wallet, Continuity, iCloud-Sync) nicht hinter Entitlement-Flags gesperrt.

## Paketreferenz React Native / Expo

| Zweck | Expo | Bare React Native |
|---|---|---|
| WebView (nur ergänzend, nie einziger Screen) | `react-native-webview` | `react-native-webview` |
| Native Navigation als Mehrwert | `expo-router` | `@react-navigation/native` |
| Push mit Erklär-Screen und Opt-in | `expo-notifications` | `@notifee/react-native`, `@react-native-firebase/messaging` |
| Sign in with Apple | `expo-apple-authentication` (`usesAppleSignIn`) | `@invertase/react-native-apple-authentication` |
| Drittanbieter-Login (nur mit Apple-Alternative) | `expo-auth-session` | `@react-native-google-signin/google-signin`, `react-native-fbsdk-next` |
| In-App-Käufe (auch in Mini-Apps) | `react-native-iap` (Dev Client), `react-native-purchases` | `react-native-iap`, `react-native-purchases` |
| Apple Pay (physische Güter/Dienstleistungen) | `@stripe/stripe-react-native` (Config Plugin) | `@stripe/stripe-react-native`, `react-native-payments` |
| Apple Music / MusicKit | Config Plugin für `NSAppleMusicUsageDescription` + natives Modul | `@lomray/react-native-apple-music` |
| Extensions (Widget, Keyboard, Sticker, Safari) | `@bacons/apple-targets` | manuelle Xcode-Targets unter `ios/` |
| Kontakte (Einladungen nur einzeln über Share-Sheet) | `expo-contacts`, `expo-sharing` | `react-native-contacts`, `react-native-share` |
| Große Nachlade-Downloads mit Fortschritt | `expo-file-system` (`createDownloadResumable`) | `react-native-blob-util` |

## Kurz-Prüfliste für diesen Abschnitt

**4.1 Nachahmer**
- [ ] App-Name, Slug und Icon erinnern nicht an ein bekanntes Store-Produkt; UI-Assets nicht aus fremder App.
- [ ] Bundle-ID ohne fremden Firmennamen; kein fremdes Logo als Icon/Splash; Unabhängigkeit von Drittmarken klar.
- [ ] Keine Apple-Produktnamen im App-Namen; fremde Logos nur mit Erlaubnis.

**4.2 Mindestfunktionalität**
- [ ] Mindestens ein nativer Screen mit eigener Logik, kein reiner WebView-Wrapper; keine reinen Marketing-Inhalte/Kataloge.
- [ ] ARKit-Nutzung liefert ein interaktives AR-Erlebnis.
- [ ] Kein Start-Blocker für eine andere App; Nachlade-Downloads mit Größe, Fortschritt und Abbruch.
- [ ] Template-App vom Inhaber eingereicht; Remote-Desktop-Client nur zu nutzerdefinierten Hosts, kein Software-Katalog.

**4.3 Spam**
- [ ] Keine Build-Varianten als separate, fast identische Store-Apps; Kategorie nicht gesättigt oder USP belegt.
- [ ] Eine Bundle-ID pro App; Live Activities, Push, Game Center ohne Spam/Phishing.

**4.4 Erweiterungen**
- [ ] Alle Extension-Targets erfasst; kein StoreKit-Kauf und kein Marketing in Extensions.
- [ ] Keyboard: funktioniert ohne Vollzugriff, `RequestsOpenAccess` nur mit Grund, Zahlen-/Dezimal-Layout, keine Datenweitergabe.
- [ ] Safari: minimale Permissions, keine Inhaltsverfälschung, keine Verlaufsübermittlung ohne Einwilligung.
- [ ] Sticker eigen/lizenziert; Widgets und Controls liefern Inhalt statt Werbung.

**4.5 Apple-Websites und -Dienste**
- [ ] Keine HTML-Extraktion von Apple-Store-Seiten; nur dokumentierte Feeds/APIs.
- [ ] MusicKit: Zweckbeschreibung vorhanden, keine Aufnahme/Export, Steuerung sichtbar, kein eigener Bezahlweg.
- [ ] Push: kein Prompt ohne Kontext beim ersten Start; App ohne Push nutzbar; keine sensiblen Daten; Marketing nur mit Opt-in und Abmeldung.
- [ ] Keine Massen-Einladungen an Kontakte; Game-Center-IDs nicht an Dritt-SDKs; keine Apple-Emoji-Bitmaps als Assets.

**4.7 Mini-Apps, Streaming, Chatbots, Plug-ins, Emulatoren**
- [ ] Altersfreigabe entspricht dem freizügigsten eingebetteten Inhalt; Filter- und Meldefunktion vorhanden.
- [ ] Bridge gibt keine unerklärten System-APIs frei; digitale Güter in Mini-Apps über IAP.
- [ ] Emulator ohne mitgelieferte geschützte ROMs; Datenschutzerklärung deckt eingebettete Inhalte ab.

**4.8 Login-Dienste**
- [ ] Bei Drittanbieter-Login: Sign in with Apple oder gleichwertige datensparsame Option, Entitlement gesetzt, gleichwertig platziert.
- [ ] Backend akzeptiert Relay-E-Mails; kein Tracking im Login-Flow ohne Einwilligung.
- [ ] Ohne Apple-Option: zutreffende Ausnahme im Bericht benannt.

**4.9 Apple Pay**
- [ ] Button aus PassKit/SDK; wiederkehrende Zahlungen mit Betrag und Intervall; Gesamtbetrag vollständig.
- [ ] Keine Weitergabe von Transaktions-/Kontaktdaten; nicht für digitale Güter.

**4.10 Monetarisierung eingebauter Systemfunktionen**
- [ ] Keine Paywall, die Push, Kamera, Sensoren, Wallet, Continuity oder iCloud-Sync als Kaufobjekt nennt.
- [ ] Systemfunktionen nicht hinter Entitlement-Flags gesperrt.
