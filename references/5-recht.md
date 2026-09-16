# Abschnitt 5 – Rechtliches (Legal)

Stand: Apple App Review Guidelines, Fassung vom 8. Juni 2026 (geprüft September 2026).
Zurück zur Übersicht: ../SKILL.md

Abschnitt 5 bündelt alles, was Apple juristisch absichern will: Datenschutz, geistiges Eigentum, Glücksspiel, VPN, Geräteverwaltung und das Verhalten des Entwicklers gegenüber Nutzern und App Review. Anders als in Abschnitt 2 oder 4 geht es hier selten um Geschmacksfragen. Ein Verstoß ist meist objektiv nachweisbar (fehlender Schlüssel, fehlender Dialog, fehlender Löschweg), und Apple reagiert entsprechend hart. Die Grundhaltung von Apple in diesem Abschnitt lautet: Der Entwickler ist für die Einhaltung lokaler Gesetze selbst verantwortlich, Apple prüft aber trotzdem stichprobenartig und lehnt ab, wenn etwas offensichtlich fehlt.

## Wo Apple aktuell besonders genau hinschaut

1. **Kontolöschung in der App (5.1.1 v)** – Apps mit Registrierung, die keinen vollständigen Löschweg innerhalb der App anbieten, werden seit Mitte 2022 konsequent abgelehnt. Ein Link auf eine Website, auf der der Nutzer sich erneut einloggen muss, reicht nicht.
2. **App Tracking Transparency (5.1.2 i)** – Werbe- oder Attributions-SDKs im Bundle, ohne dass der ATT-Dialog vor dem ersten Datenabfluss erscheint, sind der häufigste Datenschutz-Ablehnungsgrund. Apple prüft den Netzwerkverkehr, nicht nur den Code.
3. **Privacy Manifest und Required-Reason-APIs (5.1.1/5.1.2)** – Seit Frühjahr 2024 blockiert App Store Connect Uploads, wenn `PrivacyInfo.xcprivacy` fehlt oder Gründe für `UserDefaults`, Dateizeitstempel, Systemstartzeit, Speicherplatz oder aktive Tastaturen nicht deklariert sind. Das trifft React-Native-Projekte mit älteren Bibliotheken besonders.
4. **Purpose Strings (5.1.1 iv)** – Generische Texte wie „Diese App benötigt Zugriff auf die Kamera" führen zu Ablehnungen nach 5.1.1. Der Text muss sagen, wofür.
5. **Eigene Bewertungsdialoge (5.6.1)** – Selbstgebaute „Gefällt dir die App?"-Abfragen, die nur zufriedene Nutzer zum Store leiten, werden als Manipulation gewertet.
6. **Datenschutzerklärung nur in App Store Connect (5.1.1 i)** – Der Link muss zusätzlich in der App erreichbar sein. Apps ohne Einstellungsseite vergessen das regelmäßig.

## Inhalt

- [5.1 Datenschutz](#51-datenschutz)
  - [5.1.1 Datenerhebung und -speicherung](#511-datenerhebung-und--speicherung)
  - [Tabelle: Berechtigungsschlüssel und was ein guter Purpose-String enthält](#tabelle-berechtigungsschlüssel-und-was-ein-guter-purpose-string-enthält)
  - [Exkurs: Privacy Manifest und Required-Reason-APIs](#exkurs-privacy-manifest-und-required-reason-apis)
  - [5.1.2 Datennutzung und -weitergabe](#512-datennutzung-und--weitergabe)
  - [Tabelle: Bekannte SDKs und ihre ATT-/Privacy-Manifest-Pflicht](#tabelle-bekannte-sdks-und-ihre-att--privacy-manifest-pflicht)
  - [5.1.3 Gesundheit und Gesundheitsforschung](#513-gesundheit-und-gesundheitsforschung)
  - [5.1.4 Kinder](#514-kinder)
  - [5.1.5 Standortdienste](#515-standortdienste)
- [5.2 Geistiges Eigentum](#52-geistiges-eigentum)
  - [5.2.1 Allgemein](#521-allgemein)
  - [5.2.2 Websites und Dienste Dritter](#522-websites-und-dienste-dritter)
  - [5.2.3 Audio- und Video-Downloads](#523-audio--und-video-downloads)
  - [5.2.4 Apple-Endorsements und Apple-Marken](#524-apple-endorsements-und-apple-marken)
  - [5.2.5 Nachahmung von Apple-Produkten](#525-nachahmung-von-apple-produkten)
- [5.3 Glücksspiel, Lotterien, Gewinnspiele](#53-glücksspiel-lotterien-gewinnspiele)
  - [5.3.1 Gewinnspiele vom Entwickler gesponsert](#531-gewinnspiele-vom-entwickler-gesponsert)
  - [5.3.2 Offizielle Regeln und Apple-Disclaimer](#532-offizielle-regeln-und-apple-disclaimer)
  - [5.3.3 Kein IAP für Echtgeld-Spielguthaben](#533-kein-iap-für-echtgeld-spielguthaben)
  - [5.3.4 Echtgeld-Glücksspiel und Lotterien](#534-echtgeld-glücksspiel-und-lotterien)
- [5.4 VPN-Apps](#54-vpn-apps)
- [5.5 Mobile Device Management](#55-mobile-device-management)
- [5.6 Verhaltenskodex für Entwickler](#56-verhaltenskodex-für-entwickler)
  - [5.6.1 Kundenbewertungen](#561-kundenbewertungen)
  - [5.6.2 Entwickleridentität](#562-entwickleridentität)
  - [5.6.3 Discovery-Betrug](#563-discovery-betrug)
  - [5.6.4 App-Qualität](#564-app-qualität)
  - [5.6.5 Kommunikation mit App Review](#565-kommunikation-mit-app-review)
- [Paketreferenz React Native / Expo](#paketreferenz-react-native--expo)
- [Kurz-Prüfliste für diesen Abschnitt](#kurz-prüfliste-für-diesen-abschnitt)

---

## 5.1 Datenschutz

Apple stellt dem Abschnitt voran, dass Datenschutz ein Kernversprechen der Plattform ist. Für den prüfenden Agenten bedeutet das: Jede Stelle im Code, an der Daten das Gerät verlassen, an der eine Systemberechtigung angefordert wird oder an der ein Nutzerkonto entsteht, ist ein Prüfpunkt. Die Nummern 5.1.1 bis 5.1.5 werden von Apple in App Store Connect zusätzlich durch die „Datenschutz-Nährwertkennzeichnung" (Privacy Nutrition Labels) abgesichert; Widersprüche zwischen Code und Label sind ein eigener Ablehnungsgrund.

### 5.1.1 Datenerhebung und -speicherung

Dieser Punkt ist in zehn Buchstaben unterteilt. Jeder wird einzeln behandelt, weil Apple in der Ablehnung den Buchstaben nennt.

#### 5.1.1 (i) Datenschutzerklärung

**Kern der Regel** – Jede App braucht eine Datenschutzerklärung, und zwar an zwei Stellen: als URL im Metadatenfeld in App Store Connect und leicht auffindbar innerhalb der App. Die Erklärung muss beschreiben, welche Daten die App erhebt, wie sie erhoben werden, wofür sie genutzt werden, wie lange sie aufbewahrt werden, wie der Nutzer Löschung oder Widerruf erreichen kann und welche Dritten (SDKs, Analysedienste, Werbenetzwerke) Daten erhalten. Für eingebundene Drittanbieter-SDKs muss der Entwickler sicherstellen, dass diese denselben Schutz einhalten wie die App selbst.

**Risikostufe** – Hoch. Fehlt die Erklärung in der App, wird die Einreichung nahezu sicher abgelehnt; die Behebung ist aber trivial.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Suche nach einem `Link`, `SFSafariViewController`, `UIApplication.shared.open` oder `WKWebView`-Aufruf mit einer URL, die `privacy`, `datenschutz` oder `policy` enthält.
- Einstellungs-Screens (`SettingsView`, `AboutViewController`) auf einen entsprechenden Eintrag durchsuchen.
- `Settings.bundle` mit einem `PSTitleValueSpecifier` oder Kind-Pane „Datenschutz" ist zulässig, gilt aber als versteckt; besser zusätzlich in der App.

React Native/Expo:
- `Linking.openURL(...)`, `WebBrowser.openBrowserAsync(...)` (expo-web-browser) mit Privacy-URL.
- `app.json`/`app.config.js` enthält keinen Privacy-Link; das ist nur in App Store Connect hinterlegt, nicht im Bundle.

**Typische Verstöße**

❌ Nur der Link in App Store Connect, in der App nirgends erreichbar.

❌ Onboarding zeigt einen Link, danach ist er weg – Apple erwartet dauerhaften Zugang (Einstellungen, Profil, Über-Seite).

❌ Erklärung nennt Firebase Analytics nicht, obwohl `FirebaseAnalytics` importiert ist.

✅ Einstellungen → „Datenschutzerklärung" öffnet die URL im `SFSafariViewController` bzw. `WebBrowser.openBrowserAsync`.

**Prüfliste**
- [ ] Datenschutz-URL ist in der App dauerhaft erreichbar (nicht nur Onboarding).
- [ ] Alle im Bundle gefundenen Dritt-SDKs werden in der Erklärung genannt.
- [ ] Erklärung nennt Aufbewahrungsdauer und Löschweg.

**Empfohlene Behebung** – Link in den Einstellungen; Anzeige via `expo-web-browser` (Expo) bzw. `react-native-inappbrowser-reborn` (bare) oder `SFSafariViewController` (nativ).

#### 5.1.1 (ii) Einwilligung

**Kern der Regel** – Personenbezogene Daten dürfen erst nach ausdrücklicher Zustimmung erhoben werden. Die Zustimmung muss frei sein: klar erklärt, ohne Vorauswahl, jederzeit widerrufbar. Apps dürfen Nutzer nicht zwingen, Daten freizugeben, damit die App überhaupt funktioniert, und dürfen die Funktion nicht künstlich an die Datenfreigabe koppeln. Eine Ablehnung des Nutzers darf nicht dazu führen, dass die App unbenutzbar wird oder der Dialog in einer Schleife wiederkehrt.

**Risikostufe** – Hoch. Zwangs-Zustimmung („Akzeptieren oder App beenden") wird als Manipulation gewertet.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Consent-Screens ohne Ablehnen-Pfad: `Button("Akzeptieren")` ohne zweite Option; `isPresented`-Bindings, die nur bei Zustimmung auf `false` gehen.
- `exit(0)`, `fatalError()` oder leere Views nach Ablehnung.
- Vorausgefüllte Toggles: `@State private var analyticsConsent = true`.
- Datenversand vor dem Consent-Screen: Analytics-Initialisierung in `application(_:didFinishLaunchingWithOptions:)` oder im `App.init()`, bevor der Nutzer etwas gesehen hat.

React Native/Expo:
- `Analytics.logEvent`, `Segment.track`, `mixpanel.track` in `App.tsx` auf oberster Ebene oder in einem `useEffect(() => {...}, [])` ohne Consent-Prüfung.
- `BackHandler.exitApp()` bei Ablehnung.
- `Modal`/`BottomSheet` mit `onRequestClose={() => {}}` und nur einem Button.

**Typische Verstöße**

```swift
// ❌ Analytics läuft vor jeder Zustimmung
func application(_ app: UIApplication, didFinishLaunchingWithOptions ...) -> Bool {
    FirebaseApp.configure()
    Analytics.setAnalyticsCollectionEnabled(true)
    return true
}
```

```swift
// ✅ Sammlung erst nach expliziter Zustimmung
Analytics.setAnalyticsCollectionEnabled(ConsentStore.shared.analyticsAllowed)
```

```tsx
// ❌ Kein Weg ohne Zustimmung
<Button title="Zustimmen und fortfahren" onPress={accept} />
// ✅
<Button title="Zustimmen" onPress={accept} />
<Button title="Ohne Analyse fortfahren" onPress={decline} />
```

**Prüfliste**
- [ ] Jeder Consent-Dialog hat einen gleichwertigen Ablehnen-Pfad.
- [ ] Toggles für optionale Datennutzung sind standardmäßig aus.
- [ ] Widerruf ist in den Einstellungen möglich.
- [ ] Kein Datenversand vor der Zustimmung (Analytics, Crash-Reporter mit Nutzer-ID, Attribution).

**Empfohlene Behebung** – Eigene Consent-Schicht, die SDK-Initialisierung kapselt; Firebase per `FirebaseAnalytics` `setAnalyticsCollectionEnabled(false)` bis Zustimmung, bei Expo `@react-native-firebase/analytics` `setAnalyticsCollectionEnabled(false)`; zusätzlich in `Info.plist` bzw. `app.json` `FIREBASE_ANALYTICS_COLLECTION_ENABLED = false`.

#### 5.1.1 (iii) Datenminimierung

**Kern der Regel** – Die App darf nur die Daten und Berechtigungen anfordern, die für die konkrete Funktion notwendig sind. Wer eine Notiz-App baut, braucht keine Kontakte. Berechtigungen sind erst dann anzufragen, wenn die zugehörige Funktion genutzt wird, nicht pauschal beim Start. Die Kernfunktion der App muss ohne die Freigabe optionaler Berechtigungen nutzbar bleiben.

**Risikostufe** – Hoch, wenn Berechtigungen ohne erkennbaren Zweck angefordert werden; Mittel bei bloßem „zu früh".

**Woran du es im Code erkennst**

Swift/Objective-C:
- Alle `NS…UsageDescription`-Schlüssel in `Info.plist` gegen die tatsächlich genutzten Frameworks abgleichen. Ein `NSContactsUsageDescription` ohne `import Contacts` deutet auf einen Altlasten- oder Copy-Paste-Schlüssel hin – Apple fragt dann nach dem Zweck.
- Sammelanfrage beim Start: mehrere `request…Authorization`-Aufrufe in `didFinishLaunchingWithOptions` oder in der ersten `onAppear`.
- `PHPhotoLibrary.requestAuthorization(for: .readWrite)` wo `.addOnly` oder `PHPickerViewController` (keine Berechtigung nötig) reichen würde.
- `CLLocationManager.requestAlwaysAuthorization()` wo `requestWhenInUseAuthorization()` reicht.

React Native/Expo:
- `app.json` → `ios.infoPlist` mit Schlüsseln, für die kein Expo-Modul installiert ist.
- Expo-Config-Plugins in `plugins: [...]`, die Berechtigungstexte eintragen (z. B. `expo-contacts`), ohne dass das Modul im Code importiert wird.
- `Permissions.askAsync` (veraltet) oder `request…PermissionsAsync()` mehrerer Module in einer Startsequenz.
- `expo-image-picker` mit `ImagePicker.requestMediaLibraryPermissionsAsync()` obwohl `launchImageLibraryAsync` seit iOS 14 ohne Vollzugriff funktioniert.

**Typische Verstöße**

```swift
// ❌ Alles auf einmal beim ersten Start
locationManager.requestAlwaysAuthorization()
AVCaptureDevice.requestAccess(for: .video) { _ in }
CNContactStore().requestAccess(for: .contacts) { _, _ in }
```

```tsx
// ✅ Just-in-time, an die Funktion gebunden
const onScanPressed = async () => {
  const { status } = await Camera.requestCameraPermissionsAsync();
  if (status !== 'granted') { showFallbackInput(); return; }
  navigation.navigate('Scanner');
};
```

**Prüfliste**
- [ ] Jeder UsageDescription-Schlüssel hat ein korrespondierendes, genutztes Framework/Modul.
- [ ] Berechtigungen werden im Kontext der Funktion angefragt, nicht beim Start.
- [ ] Nach Ablehnung bleibt die Kernfunktion nutzbar (Fallback vorhanden).
- [ ] Für Fotoauswahl wird `PHPickerViewController` / `expo-image-picker` ohne Vollzugriff genutzt.

**Empfohlene Behebung** – Nicht benötigte Schlüssel und Config-Plugins entfernen; `PHPickerViewController` statt `PHPhotoLibrary`; Kontaktauswahl über `CNContactPickerViewController` (keine Berechtigung nötig) bzw. `expo-contacts` `presentContactPickerAsync()`.

#### 5.1.1 (iv) Zugriff und Purpose Strings

**Kern der Regel** – Der Nutzer muss beim Systemdialog verstehen, wofür die App den Zugriff braucht. Der Text im `NS…UsageDescription`-Schlüssel muss konkret, wahrheitsgemäß und für Laien verständlich sein. Apple lehnt leere Strings, Platzhalter („TODO"), rein technische Formulierungen und Texte ab, die den tatsächlichen Zweck verschleiern. Zudem darf die App den Nutzer nicht dazu drängen, eine Berechtigung zu erteilen (kein wiederholtes Pre-Prompting, keine Belohnung für Zustimmung).

**Risikostufe** – Hoch. Ungenaue Purpose Strings sind ein Standard-Ablehnungsgrund, meist mit dem Hinweis „Guideline 5.1.1 – Legal – Data Collection and Storage".

**Woran du es im Code erkennst**

Swift/Objective-C:
- `Info.plist` vollständig durchgehen, jeden `NS…UsageDescription`-Wert prüfen (Tabelle unten).
- Lokalisierte Werte in `InfoPlist.strings` je Sprache prüfen – häufig sind nur die englischen Texte gepflegt und die deutschen leer oder Platzhalter.
- Build-Settings: `INFOPLIST_KEY_NSCameraUsageDescription` (Xcode 13+ schreibt die Werte in die `.pbxproj`).
- Berechtigungsanfragen in Schleifen oder bei jedem `viewDidAppear` ohne Prüfung des aktuellen Status.

React Native/Expo:
- `app.json` → `expo.ios.infoPlist.NS…UsageDescription`.
- Config-Plugin-Optionen wie `["expo-location", { "locationAlwaysAndWhenInUsePermission": "..." }]`, `["expo-camera", { "cameraPermission": "..." }]`, `["expo-tracking-transparency", { "userTrackingPermission": "..." }]`. Werden Optionen weggelassen, schreibt Expo einen englischen Standardtext wie „Allow $(PRODUCT_NAME) to access your camera" – das ist generisch und wird beanstandet.
- Bare RN: `ios/<App>/Info.plist` direkt.

**Typische Verstöße**

```xml
<!-- ❌ generisch -->
<key>NSCameraUsageDescription</key>
<string>This app needs camera access</string>
<!-- ✅ konkret -->
<key>NSCameraUsageDescription</key>
<string>Mit der Kamera scannst du Rechnungen, die dann automatisch als Ausgabe erfasst werden.</string>
```

```json
// ❌ Expo ohne Purpose-Option → Standardtext
"plugins": ["expo-location"]
// ✅
"plugins": [["expo-location", {
  "locationWhenInUsePermission": "Dein Standort wird genutzt, um Tankstellen in deiner Nähe anzuzeigen."
}]]
```

❌ Pre-Permission-Screen, der bei „Später" jedes Mal beim App-Start erneut erscheint.

**Prüfliste**
- [ ] Jeder Purpose-String nennt die konkrete Funktion und den Nutzen.
- [ ] Keine Platzhalter, keine leeren Strings, keine Standardtexte von Config-Plugins.
- [ ] Lokalisierte Fassungen (`InfoPlist.strings`, `expo-localization`-Plugin `infoPlist`) vollständig.
- [ ] Status wird vor erneuter Anfrage geprüft (`authorizationStatus`, `getPermissionsAsync`).

**Empfohlene Behebung** – Texte nach der Tabelle unten neu formulieren; bei Expo alle Plugin-Optionen für Berechtigungstexte setzen, bei mehrsprachigen Apps `expo-localization` mit `ios.infoPlist`-Lokalisierung oder `InfoPlist.strings` per Config-Plugin.

### Tabelle: Berechtigungsschlüssel und was ein guter Purpose-String enthält

Ein guter Purpose-String beantwortet drei Fragen: Welche Funktion? Welcher Nutzen für mich? Wann passiert es? Die Spalte „Muss enthalten" ist die Mindestanforderung, die der Agent prüft.

| Info.plist-Schlüssel | Auslösendes Framework / Expo-Modul | Muss enthalten |
|---|---|---|
| `NSCameraUsageDescription` | AVFoundation, `expo-camera`, `expo-image-picker`, `react-native-vision-camera` | Was fotografiert/gescannt wird (Belege, QR-Codes, Profilbild) |
| `NSMicrophoneUsageDescription` | AVAudioSession, `expo-av`, `expo-audio`, Video-Aufnahme | Wofür Ton aufgezeichnet wird; bei Video explizit „Ton für Videoaufnahmen" |
| `NSPhotoLibraryUsageDescription` | PHPhotoLibrary (Lesen), `expo-media-library` | Welche Bilder gelesen werden und warum (z. B. Galerie-Backup) |
| `NSPhotoLibraryAddUsageDescription` | `UIImageWriteToSavedPhotosAlbum`, `MediaLibrary.saveToLibraryAsync` | Dass nur gespeichert, nicht gelesen wird |
| `NSLocationWhenInUseUsageDescription` | CoreLocation, `expo-location` | Funktion (Karte, Umkreissuche) und dass es nur bei geöffneter App passiert |
| `NSLocationAlwaysAndWhenInUseUsageDescription` | CoreLocation (Hintergrund), `expo-location` mit `isIosBackgroundLocationEnabled` | Warum Hintergrund nötig ist (Tracking einer Laufstrecke, Geofence-Erinnerung) |
| `NSLocationAlwaysUsageDescription` | nur für iOS ≤ 10, veraltet | Sollte durch den Schlüssel darüber ersetzt sein |
| `NSLocationTemporaryUsageDescriptionDictionary` | `requestTemporaryFullAccuracyAuthorization` | Pro Zweck-Key ein Grund für Vollpräzision |
| `NSContactsUsageDescription` | Contacts, `expo-contacts`, `react-native-contacts` | Welche Kontaktfelder und wofür (Freunde einladen, Empfänger wählen) |
| `NSCalendarsFullAccessUsageDescription` | EventKit (iOS 17+), `expo-calendar` | Warum Lesen und Schreiben nötig ist |
| `NSCalendarsWriteOnlyAccessUsageDescription` | EventKit `requestWriteOnlyAccessToEvents` | Dass nur Termine angelegt werden |
| `NSCalendarsUsageDescription` | EventKit vor iOS 17 | Nur noch als Fallback für alte Deployment-Targets |
| `NSRemindersFullAccessUsageDescription` | EventKit Reminders | Welche Erinnerungen angelegt/gelesen werden |
| `NSMotionUsageDescription` | CoreMotion, `expo-sensors` (Pedometer) | Welche Bewegungsdaten (Schritte, Aktivität) |
| `NSHealthShareUsageDescription` | HealthKit lesen, `react-native-health` | Welche Datentypen gelesen werden und wofür |
| `NSHealthUpdateUsageDescription` | HealthKit schreiben | Welche Datentypen geschrieben werden |
| `NSHealthClinicalHealthRecordsShareUsageDescription` | HealthKit klinische Daten | Zweck der Nutzung klinischer Dokumente |
| `NSBluetoothAlwaysUsageDescription` | CoreBluetooth, `react-native-ble-plx`, `expo-bluetooth` (Community) | Welche Geräte gekoppelt werden (Waage, Sensor) |
| `NSBluetoothPeripheralUsageDescription` | veraltet (iOS ≤ 12) | Nur bei alten Targets |
| `NSSpeechRecognitionUsageDescription` | Speech, `expo-speech-recognition` (Community) | Dass Audio zur Erkennung an Apple gesendet werden kann |
| `NSFaceIDUsageDescription` | LocalAuthentication, `expo-local-authentication` | Wofür entsperrt wird (App-Sperre, Login) |
| `NSUserTrackingUsageDescription` | AppTrackingTransparency, `expo-tracking-transparency` | Dass Daten mit Dritten zu Werbezwecken verknüpft werden; ehrlich, kein „für ein besseres Erlebnis" |
| `NSLocalNetworkUsageDescription` | Bonjour, mDNS, `react-native-zeroconf` | Welche Geräte im Netz gesucht werden |
| `NSBonjourServices` | zusammen mit LocalNetwork | Konkrete Service-Typen (`_http._tcp`) |
| `NSHomeKitUsageDescription` | HomeKit | Welche Geräte gesteuert werden |
| `NSAppleMusicUsageDescription` | MediaPlayer, `expo-music-library` (Community) | Welche Mediathek-Daten gelesen werden |
| `NSSiriUsageDescription` | Intents/SiriKit | Welche Aktionen per Siri ausgelöst werden |
| `NSNFCReaderUsageDescription` | CoreNFC, `react-native-nfc-manager` | Welche Tags gelesen werden |
| `NSFallDetectionUsageDescription` | CMFallDetectionManager (watchOS) | Zweck der Sturzerkennung |
| `NSSensorKitUsageDescription` + `NSSensorKitUsageDetail` | SensorKit (nur mit Apple-Freigabe) | Forschungszweck, Datenarten |
| `NSVoIPUsageDescription` | CallKit/PushKit | Wofür Anrufe entgegengenommen werden |
| `NSFocusStatusUsageDescription` | Focus-Status | Warum Fokus-Status geteilt wird |
| `NSNearbyInteractionUsageDescription` | NearbyInteraction (UWB) | Welche Geräte geortet werden |
| `NSGKFriendListUsageDescription` | GameKit Freunde | Wofür Freundesliste (Ranglisten) |
| `NSIdentityUsageDescription` | Verify with Wallet (Ausweisdaten) | Welche Ausweisfelder und Prüfzweck |
| `NSWorldSensingUsageDescription` | visionOS ARKit (Scene Understanding, Planes) | Was die App über den Raum erfährt |
| `NSHandsTrackingUsageDescription` | visionOS Handtracking | Wozu Handpositionen genutzt werden |
| `NSDesktopFolderUsageDescription`, `NSDocumentsFolderUsageDescription`, `NSDownloadsFolderUsageDescription` | macOS Dateizugriff | Welche Dateien warum gelesen werden |
| `NSRemovableVolumesUsageDescription`, `NSNetworkVolumesUsageDescription` | macOS externe/Netzlaufwerke | Zweck |
| `NSAppleEventsUsageDescription` | macOS Automation anderer Apps | Welche App gesteuert wird |
| `NSSystemAdministrationUsageDescription` | macOS Admin-Rechte | Warum erhöhte Rechte |

Ergänzende Schlüssel ohne Freitext, die der Agent trotzdem prüft: `NSLocationDefaultAccuracyReduced` (true = App verlangt standardmäßig nur grobe Position, gut für 5.1.5), `NSHealthRequiredReadAuthorizationTypeIdentifiers`, `NSPhotoLibraryLimitedAccess`-Verhalten via `PHPhotoLibraryPreventAutomaticLimitedAccessAlert`.

#### 5.1.1 (v) Kontoerstellung und Kontolöschung

**Kern der Regel** – Wenn die Kernfunktion der App kein Nutzerkonto braucht, darf die App die Nutzung nicht von einer Registrierung abhängig machen. Bietet die App Kontoerstellung an, muss sie auch die Löschung des Kontos in der App anbieten (Pflicht seit 30. Juni 2022). Der Löschfluss muss das gesamte Konto samt zugehöriger Daten entfernen, nicht nur deaktivieren. Ein Verweis auf eine Website ist nur zulässig, wenn er direkt und ohne erneute Hürden zum Löschvorgang führt; ein „Schreib uns eine E-Mail" ist keine Löschung in der App. Zusätzliche Identitätsprüfung ist erlaubt, wenn sie gesetzlich nötig ist (z. B. Banken), muss aber begründet sein. Bei „Mit Apple anmelden" muss der Entwickler zusätzlich das Token über die Sign in with Apple REST API widerrufen.

**Risikostufe** – Kritisch. Apple lehnt auch Updates bestehender Apps ab, bis der Löschweg vorhanden ist.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Registrierung vorhanden? Suche nach `createUser`, `signUp`, `register`, `ASAuthorizationAppleIDProvider`, `GIDSignIn`, `Auth.auth().createUser`, `Amplify.Auth.signUp`, `SupabaseClient.auth.signUp`.
- Löschung vorhanden? Suche nach `deleteAccount`, `deleteUser`, `Auth.auth().currentUser?.delete()`, `Konto löschen`, `Account löschen`, `Delete Account`, `revokeToken`, `ASAuthorizationAppleIDRequest` mit `revoke`.
- Ein Löschweg, der nur `signOut()` aufruft oder ein Flag `isActive = false` setzt, ist keine Löschung.
- `mailto:`-Links im Konto-Bereich als einziger Löschweg.

React Native/Expo:
- Registrierung: `auth().createUserWithEmailAndPassword`, `supabase.auth.signUp`, `Auth.signUp` (Amplify), `AppleAuthentication.signInAsync` (`expo-apple-authentication`), `Clerk`, `Auth0`.
- Löschung: `auth().currentUser.delete()`, `supabase.rpc('delete_user')`, `Auth.deleteUser()`, eigener Endpoint `DELETE /users/me`; Strings `deleteAccount`, `Konto löschen`.
- Bei Apple-Login: Aufruf eines Backend-Endpoints, der `https://appleid.apple.com/auth/revoke` bedient.

**Typische Verstöße**

```swift
// ❌ "Löschen" ist nur Abmelden
@IBAction func deleteAccountTapped() {
    try? Auth.auth().signOut()
    showAlert("Dein Konto wurde gelöscht.")
}
```

```swift
// ✅ Echte Löschung inkl. Backend-Daten und Apple-Token
func deleteAccount() async throws {
    try await api.delete("/users/me")           // Backend löscht Datensätze
    try await api.post("/auth/apple/revoke")     // Sign in with Apple widerrufen
    try await Auth.auth().currentUser?.delete()
}
```

❌ Konto-Screen enthält nur „Kontakt: support@…, um dein Konto zu löschen".

❌ Registrierungszwang vor dem ersten Screen, obwohl die App nur einen Rechner anbietet (verstößt zusätzlich gegen die „nur wenn nötig"-Regel).

**Prüfliste**
- [ ] Gibt es eine Registrierung? Wenn ja: gibt es einen Lösch-Eintrag im Konto-/Einstellungsbereich?
- [ ] Löscht der Code tatsächlich (Backend-Call, Auth-Provider `delete`), nicht nur `signOut`?
- [ ] Sign in with Apple: Token-Widerruf über das Backend implementiert?
- [ ] Ist eine Web-Umleitung, wenn vorhanden, direkt und ohne erneuten Login zum Löschen?
- [ ] Ist die Kernfunktion ohne Konto nutzbar, wenn kein Konto nötig ist (Gastmodus)?
- [ ] Bei gesetzlicher Aufbewahrung: Wird das in der App erklärt (Frist, Grund)?

**Empfohlene Behebung** – Lösch-Button in den Kontoeinstellungen, Bestätigungsdialog, Backend-Endpoint, Provider-Löschung (`expo-apple-authentication` liefert das `authorizationCode` für den Revoke; bare RN: `@invertase/react-native-apple-authentication`). Nativ: `ASAuthorizationAppleIDProvider` plus Server-Revoke.

#### 5.1.1 (vi) Kein heimliches Auslesen von Passwörtern und privaten Daten

**Kern der Regel** – Apps dürfen keine Passwörter, Zugangsdaten oder private Daten heimlich abgreifen, weder aus anderen Apps, aus der Zwischenablage, aus Tastatureingaben noch über Umwege wie Screenshots oder Barrierefreiheits-Schnittstellen. Das betrifft auch das Sammeln von Zugangsdaten für Drittdienste zur „Kontoverknüpfung" außerhalb von OAuth.

**Risikostufe** – Kritisch. Hier drohen nicht nur Ablehnung, sondern Konto-Sperre.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `UIPasteboard.general.string` beim App-Start oder im `sceneDidBecomeActive` ohne Nutzeraktion (iOS zeigt den Banner, Apple fragt nach).
- Eigene Login-Masken für Fremddienste (Bank, Google, Instagram) mit `URLSession`-Posts an eigene Server statt OAuth-Flows.
- Custom Keyboard Extensions mit `RequestsOpenAccess = true` und Netzwerkzugriff.

React Native/Expo:
- `Clipboard.getStringAsync()` (expo-clipboard) im ersten `useEffect`.
- `WebView` mit `injectedJavaScript`, das `document.querySelector('input[type=password]').value` liest, oder `onMessage`, das Formularfelder von Fremdseiten weiterreicht.

**Typische Verstöße**

```tsx
// ❌ Zwischenablage automatisch beim Start lesen
useEffect(() => { Clipboard.getStringAsync().then(sendToServer); }, []);
```

```swift
// ✅ Nur auf Nutzeraktion und nur mit Mustererkennung
if UIPasteboard.general.hasStrings, userTappedPaste { handle(UIPasteboard.general.string) }
```

**Prüfliste**
- [ ] Kein automatischer Clipboard-Zugriff ohne Nutzeraktion (`detectPatterns` nutzen).
- [ ] Fremd-Logins ausschließlich über OAuth/`ASWebAuthenticationSession`.
- [ ] Kein JavaScript-Injection in WebViews von Drittseiten, das Eingaben ausliest.

**Empfohlene Behebung** – `ASWebAuthenticationSession` bzw. `expo-auth-session`; `UIPasteboard.detectPatterns` statt Vollzugriff; Paste-Button (`UIPasteControl`).

#### 5.1.1 (vii) SafariViewController

**Kern der Regel** – Wird `SFSafariViewController` genutzt, muss er sichtbar sein und Inhalte anzeigen, mit denen der Nutzer interagieren soll. Er darf nicht versteckt (0×0 Pixel, außerhalb des Bildschirms, hinter einer Overlay-View) instanziert werden, um Cookies, Tracking-Pixel oder Attributions-Weiterleitungen abzufeuern. Dasselbe gilt sinngemäß für `ASWebAuthenticationSession` und `WKWebView`.

**Risikostufe** – Hoch. Der klassische Missbrauch war Cookie-basiertes Tracking; Apple sucht aktiv danach.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `SFSafariViewController` mit `view.frame = .zero`, `alpha = 0`, `isHidden = true`, `addChild` ohne `present`.
- `WKWebView` mit Frame außerhalb `UIScreen.main.bounds`, das nur `load(URLRequest)` auf Tracking-URLs ausführt.

React Native/Expo:
- `WebView` mit `style={{ width: 0, height: 0 }}` oder `opacity: 0`.
- `WebBrowser.openBrowserAsync` sofort gefolgt von `dismissBrowser()` in einem Attributions-Helfer.

**Typische Verstöße**

```swift
// ❌ unsichtbarer Safari-Controller für Tracking
let sfvc = SFSafariViewController(url: trackingURL)
sfvc.view.alpha = 0
addChild(sfvc); view.addSubview(sfvc.view)
```

✅ `present(sfvc, animated: true)` als Vollbild für eine Seite, die der Nutzer angefordert hat.

**Prüfliste**
- [ ] Jede SafariViewController-Instanz wird sichtbar präsentiert.
- [ ] Keine unsichtbaren WebViews mit Fremd-URLs.

**Empfohlene Behebung** – Attribution über SKAdNetwork / `AdAttributionKit` statt Cookie-Tricks; Web-Inhalte über `expo-web-browser`.

#### 5.1.1 (viii) Keine Profilbildung aus fremden Quellen

**Kern der Regel** – Apps dürfen keine Profile aus Daten zusammensetzen, die sie über Kontakte, Fotos, Kalender, HomeKit, Mediathek oder andere Systemquellen erhalten, um daraus Informationen über Personen zu gewinnen, die nicht selbst Nutzer der App sind. Das Adressbuch ist kein Marketing-Rohstoff. Ebenso unzulässig ist es, personenbezogene Daten aus öffentlichen Quellen zu aggregieren (Scraping sozialer Netze), um Datenbanken über Personen zu bauen.

**Risikostufe** – Kritisch; Apps, die Kontaktbücher hochladen, verlieren häufig die Entwicklerregistrierung.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `CNContactStore.enumerateContacts` gefolgt von `JSONEncoder`/`URLSession.upload` mit allen Feldern.
- `PHAsset.fetchAssets` mit Auslesen von `location`, Gesichtserkennung via Vision auf der gesamten Mediathek.
- `HMHomeManager` mit Export von Raum-/Gerätelisten.

React Native/Expo:
- `Contacts.getContactsAsync({ fields: [...] })` mit anschließendem `fetch(..., { method: 'POST', body: JSON.stringify(contacts) })`.
- `MediaLibrary.getAssetsAsync` mit `location`-Metadaten Richtung Server.

**Typische Verstöße**

```tsx
// ❌ Ganzes Adressbuch zum Server
const { data } = await Contacts.getContactsAsync({ fields: [Fields.PhoneNumbers, Fields.Emails] });
await api.post('/contacts/sync', data);
```

```tsx
// ✅ Nur gehashte Nummern, nur zum Abgleich, nur nach Erklärung
const hashed = data.flatMap(c => c.phoneNumbers ?? []).map(p => sha256(normalize(p.number)));
await api.post('/contacts/match', { hashes: hashed });
```

**Prüfliste**
- [ ] Kontakt-/Foto-/Kalender-/HomeKit-Daten verlassen das Gerät nur für die erklärte Funktion.
- [ ] Bei Freunde-Abgleich: Hashing oder serverseitiges Löschen nach Abgleich dokumentiert.
- [ ] Keine Datenbank über Nicht-Nutzer.

**Empfohlene Behebung** – Kontaktauswahl statt Vollzugriff; Abgleich per Hash; Speicherung nur transient.

#### 5.1.1 (ix) Regulierte Bereiche: nur durch die rechtlich verantwortliche Organisation

**Kern der Regel** – Apps in stark regulierten Feldern (Banking, Finanzen, Gesundheit, Luftfahrt, Cannabis-Handel, Behörden) müssen von der juristischen Person eingereicht werden, die den Dienst tatsächlich betreibt, nicht von einem Einzelentwickler oder einer Agentur. Bei Bedarf verlangt Apple Nachweise (Lizenz, Zulassung).

**Risikostufe** – Hoch, wenn das Entwicklerkonto nicht zur Organisation passt; im Code selten sichtbar.

**Woran du es im Code erkennst**
- Bundle-Identifier, Team-ID und Copyright-Strings deuten auf eine Agentur, während die App eine Bank/Klinik repräsentiert.
- `Info.plist` → `CFBundleDisplayName` und `NSHumanReadableCopyright` mit Firmennamen abgleichen.
- Für React Native: `app.json` → `expo.owner` und `ios.bundleIdentifier`.

**Prüfliste**
- [ ] Entwicklerkonto gehört der betreibenden Organisation (oder ist ein vertraglich geklärter Publisher).
- [ ] Nachweise (Lizenz-Nummer) in den App-Review-Notizen vorbereitet.

#### 5.1.1 (x) Kontaktdaten nur freiwillig

**Kern der Regel** – Wenn die App Basis-Kontaktdaten (Name, E-Mail) abfragt, muss das optional sein, klar als optional erkennbar, und die Verweigerung darf keine Funktionen sperren, die die Daten nicht wirklich brauchen. Das ist die kleine Schwester der Kontoregel in (v): keine Pflicht-E-Mail für einen Taschenrechner.

**Risikostufe** – Mittel.

**Woran du es im Code erkennst**
- Formularvalidierung, die `email.isEmpty` als Fehler wertet, obwohl das Feld nicht für Login/Versand gebraucht wird.
- Onboarding-Screen ohne „Überspringen".
- React Native: `yup.string().email().required()` in Schemas für Newsletter-Felder.

**Prüfliste**
- [ ] Kontaktfelder ohne funktionale Notwendigkeit sind optional und so beschriftet.
- [ ] Onboarding bietet Überspringen an.

### Exkurs: Privacy Manifest und Required-Reason-APIs

Der Privacy Manifest ist formal in Abschnitt 2.5 (Software-Anforderungen) verankert, wird aber in Ablehnungen fast immer zusammen mit 5.1.1 und 5.1.2 genannt, weil er der technische Nachweis für die Datenschutzangaben ist. Deshalb steht er hier.

**Kern der Regel** – Jede App (und jedes SDK aus Apples Liste) liefert `PrivacyInfo.xcprivacy` mit vier Abschnitten: `NSPrivacyTracking` (Bool), `NSPrivacyTrackingDomains` (Domains, die nur nach ATT-Zustimmung kontaktiert werden dürfen; iOS blockiert sie sonst), `NSPrivacyCollectedDataTypes` (was gesammelt wird, verknüpft/nicht verknüpft, für Tracking ja/nein) und `NSPrivacyAccessedAPITypes` (Required-Reason-APIs mit Begründungscode). Fehlt eine Begründung, weist App Store Connect den Upload mit `ITMS-91053` ab. Die Nutzung von Required-Reason-APIs zum Fingerprinting ist unabhängig davon verboten, auch mit Zustimmung.

**Risikostufe** – Kritisch (Upload-Blocker).

**Woran du es im Code erkennst**

Swift/Objective-C:
- `PrivacyInfo.xcprivacy` im App-Target vorhanden? In jedem eigenen Framework-Target?
- Required-Reason-API-Nutzung: `UserDefaults` (Kategorie `NSPrivacyAccessedAPICategoryUserDefaults`, Grund `CA92.1`), `FileManager.attributesOfItem`, `.creationDate`, `.modificationDate`, `stat`/`fstat` (`NSPrivacyAccessedAPICategoryFileTimestamp`, `C617.1`), `ProcessInfo.systemUptime`, `mach_absolute_time` (`NSPrivacyAccessedAPICategorySystemBootTime`, `35F9.1`), `volumeAvailableCapacity`, `statfs` (`NSPrivacyAccessedAPICategoryDiskSpace`, `E174.1`/`85F4.1`), `UITextInputMode.activeInputModes` (`NSPrivacyAccessedAPICategoryActiveKeyboards`, `3EC4.1`).
- Nach dem Archivieren: Xcode „Generate Privacy Report" – ein sauberer Bericht ist ein guter Nachweis.

React Native/Expo:
- Expo SDK 51+: `app.json` → `ios.privacyManifests` mit `NSPrivacyAccessedAPITypes`; Expo trägt Standardgründe für React Native ein. Fehlt der Block bei Fremd-Bibliotheken, ergänzen.
- Bare RN: Datei `ios/<App>/PrivacyInfo.xcprivacy`; RN ≥ 0.74 legt sie in der Vorlage an. Ältere Projekte haben sie nicht.
- Bibliotheken ohne eigenen Manifest: ältere `react-native-device-info`, `react-native-fs`, `@react-native-async-storage/async-storage` (< 1.23), `react-native-mmkv` (< 2.12), `react-native-localize` (< 3.1). Versionen im `package.json` prüfen.

**Typische Verstöße**

```xml
<!-- ❌ leerer Manifest, obwohl UserDefaults genutzt wird -->
<key>NSPrivacyAccessedAPITypes</key>
<array/>
<!-- ✅ -->
<dict>
  <key>NSPrivacyAccessedAPIType</key><string>NSPrivacyAccessedAPICategoryUserDefaults</string>
  <key>NSPrivacyAccessedAPITypeReasons</key><array><string>CA92.1</string></array>
</dict>
```

❌ `NSPrivacyTracking = true`, aber `NSPrivacyTrackingDomains` leer, während `graph.facebook.com` kontaktiert wird.

❌ Systemstartzeit + Speicherplatz + aktive Tastaturen kombiniert zu einer Geräte-ID (`deviceFingerprint()`), egal ob deklariert.

**Prüfliste**
- [ ] `PrivacyInfo.xcprivacy` im App-Target und in eigenen Frameworks vorhanden.
- [ ] Alle im Code genutzten Required-Reason-APIs mit Grund deklariert.
- [ ] Tracking-Domains vollständig, wenn `NSPrivacyTracking` true.
- [ ] Keine Kombination von Systemsignalen zu einer stabilen Geräte-ID.
- [ ] Dritt-SDKs auf Apples Liste in Versionen mit Manifest und Signatur.

**Empfohlene Behebung** – Expo: `ios.privacyManifests` in `app.json`; Bibliotheken aktualisieren. Bare RN/nativ: Manifest anlegen, Xcode Privacy Report gegenprüfen.

### 5.1.2 Datennutzung und -weitergabe

#### 5.1.2 (i) Weitergabe nur mit Einwilligung, ATT

**Kern der Regel** – Nutzerdaten dürfen ohne Einwilligung nicht an Dritte gehen, und zwar auch nicht in Form von Geräte-IDs. Wer Daten aus seiner App mit Daten aus anderen Apps oder Websites Dritter verknüpft (Tracking für Werbung oder Datenhandel), muss vorher den Systemdialog von App Tracking Transparency zeigen. Bei Ablehnung darf weder die IDFA gelesen noch ein anderes Identifikationsmerkmal (Fingerprinting, E-Mail-Hashes an Werbenetze) ersatzweise genutzt werden. Die App darf die Nutzung nicht von der Zustimmung abhängig machen und darf den Nutzer nicht mit Belohnungen dazu bewegen.

**Drittanbieter-KI** – Seit der Überarbeitung vom 13. November 2025 steht in 5.1.2(i): „You must clearly disclose where personal data will be shared with third parties, including with third-party AI, and obtain explicit permission before doing so." Die App muss also offenlegen, welche Daten an welchen Anbieter gehen, und *vorher* ausdrücklich zustimmen lassen. Die Guideline sagt nicht, wo die Offenlegung stehen muss. Veröffentlichte Ablehnungen deuten aber darauf hin, dass ein Absatz in der Datenschutzerklärung nicht genügt – sicher ist ein Hinweis in der App vor dem ersten gesendeten Inhalt. Nach 5.1.1(i) muss die Datenschutzerklärung die Weitergabe an Dritte ohnehin abdecken. On-Device-Modelle wie Apples Foundation Models fallen nicht darunter, solange nichts das Gerät verlässt.

**Risikostufe** – Kritisch. Apple prüft, ob Werbe-/Attributions-SDKs im Bundle sind, und lehnt ab, wenn kein ATT-Dialog erscheint oder wenn trotz Ablehnung Tracking-Endpunkte kontaktiert werden. Bei KI-Funktionen sind Ablehnungen dokumentiert, wenn Chat-Inhalte, Fotos oder Dokumente ohne vorherigen Hinweis und Zustimmung an einen Cloud-Anbieter gehen.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `import AppTrackingTransparency`, `ATTrackingManager.requestTrackingAuthorization`, `ATTrackingManager.trackingAuthorizationStatus`.
- `import AdSupport`, `ASIdentifierManager.shared().advertisingIdentifier` – ohne vorherige Statusprüfung ist das ein Verstoß.
- `NSUserTrackingUsageDescription` in `Info.plist`.
- SDK-Imports: `FirebaseAnalytics`, `FBSDKCoreKit` (`Settings.shared.isAdvertiserTrackingEnabled`), `Adjust` (`ADJConfig`), `AppsFlyerLib` (`waitForATTUserAuthorization`), `Branch`, `GoogleMobileAds`, `AppLovinSDK`, `UnityAds`, `IronSource`, `Singular`, `Kochava`, `Tenjin`.
- Podfile / Package.swift auf diese Namen durchsuchen; das Bundle kann SDKs enthalten, die nirgends explizit importiert sind (transitiv über Firebase).
- ATT-Aufruf, der zu früh kommt: vor `applicationDidBecomeActive` erscheint der Dialog auf iOS nicht.

React Native/Expo:
- `expo-tracking-transparency`: `requestTrackingPermissionsAsync`, `getTrackingPermissionsAsync`; Plugin `["expo-tracking-transparency", { "userTrackingPermission": "..." }]`.
- Bare: `react-native-tracking-transparency` (`requestTrackingPermission`), `react-native-permissions` (`PERMISSIONS.IOS.APP_TRACKING_TRANSPARENCY`).
- IDFA: `expo-tracking-transparency` `getAdvertisingId()`, `react-native-idfa`, `react-native-device-info` `getUniqueId()` (das ist IDFV, kein Tracking, aber prüfen, wohin es geht).
- SDKs: `react-native-fbsdk-next`, `react-native-adjust`, `react-native-appsflyer`, `react-native-branch`, `react-native-google-mobile-ads`, `@react-native-firebase/analytics`, `react-native-applovin-max`, `expo-ads-admob` (veraltet).
- Fehlender Zusammenhang: `appsFlyer.initSdk()` in `App.tsx` ohne vorherigen ATT-Aufruf oder ohne `timeToWaitForATTUserAuthorization`.

Drittanbieter-KI (beide Codebasen):
- Endpunkte: `api.openai.com`, `api.anthropic.com`, `generativelanguage.googleapis.com`, `api.mistral.ai`, `api.groq.com`, `openrouter.ai`, `api.deepseek.com`, `api.perplexity.ai`; eigene Proxy-Backends, die Prompts weiterreichen.
- SDKs: Swift `import OpenAI`, `GoogleGenerativeAI`, `FirebaseAI`/`FirebaseVertexAI`; JS `openai`, `@anthropic-ai/sdk`, `@google/genai`, `@google/generative-ai`, `firebase/ai`.
- Fehlender Zusammenhang: der erste Aufruf (`chat.completions.create`, `messages.create`, `generateContent`) ist erreichbar, ohne dass vorher ein gespeicherter Einwilligungs-Status (`aiConsentGiven`, `@AppStorage`) geprüft wird.

**Typische Verstöße**

```swift
// ❌ IDFA ohne ATT
let idfa = ASIdentifierManager.shared().advertisingIdentifier.uuidString
Analytics.setUserProperty(idfa, forName: "idfa")
```

```swift
// ✅ Nur nach Zustimmung, sonst gar nicht
ATTrackingManager.requestTrackingAuthorization { status in
    guard status == .authorized else { Adjust.trackingDisabled(); return }
    Adjust.appDidLaunch(config)
}
```

```tsx
// ❌ AppsFlyer startet vor dem Dialog
useEffect(() => { appsFlyer.initSdk(options); }, []);
// ✅
useEffect(() => {
  (async () => {
    const { status } = await requestTrackingPermissionsAsync();
    appsFlyer.initSdk({ ...options, timeToWaitForATTUserAuthorization: 0,
      isDebug: false, onInstallConversionDataListener: status === 'granted' });
  })();
}, []);
```

❌ Vorschalt-Screen: „Erlaube Tracking und erhalte 100 Münzen".

❌ Chat-App sendet die erste Nachricht an OpenAI; erwähnt wird das nur in der Datenschutzerklärung.

✅ Vor der ersten Anfrage ein Sheet: „Deine Nachricht und angehängte Bilder werden an OpenAI (USA) gesendet, um die Antwort zu erzeugen" mit „Erlauben" und „Nicht jetzt"; die Entscheidung wird gespeichert und ist in den Einstellungen widerrufbar.

❌ Bei Ablehnung: `deviceFingerprint = [bootTime, diskSpace, keyboards, locale].joined()` an das Attributions-Backend.

**Prüfliste**
- [ ] Ist ein Werbe-/Attributions-/Analytics-SDK mit Tracking-Fähigkeit im Bundle? (Tabelle unten)
- [ ] Wenn ja: Wird `requestTrackingAuthorization` vor dem ersten SDK-Start aufgerufen und ist der Text ehrlich?
- [ ] Bei Ablehnung: kein IDFA-Zugriff, SDK in „limited"-Modus, keine Ersatz-IDs.
- [ ] Kein Anreiz, keine Blockade, kein wiederholtes Nachfragen (Systemdialog erscheint ohnehin nur einmal).
- [ ] Nutrition Label in App Store Connect („Daten, die zum Tracking verwendet werden") stimmt mit Code überein.
- [ ] `NSPrivacyTracking` und `NSPrivacyTrackingDomains` im Manifest gesetzt.
- [ ] Gehen Inhalte an einen KI-Dienst Dritter: In-App-Hinweis mit Datenart und Anbietername vor dem ersten Senden, ausdrückliche Zustimmung, Widerruf möglich; Anbieter auch in der Datenschutzerklärung.

**Empfohlene Behebung** – `expo-tracking-transparency` (Expo) oder `react-native-tracking-transparency` (bare); nativ `ATTrackingManager`. Attribution ohne ATT über SKAdNetwork 4 / AdAttributionKit (`SKAdNetworkItems` in `Info.plist`). Für KI-Dienste: Einwilligungs-Sheet vor dem ersten Aufruf, Status persistent speichern (`@AppStorage`, `expo-secure-store`/`AsyncStorage`), jeden Aufrufpfad über denselben Guard führen; in den Review-Notizen beschreiben, wo der Hinweis erscheint.

### Tabelle: Bekannte SDKs und ihre ATT-/Privacy-Manifest-Pflicht

„ATT nötig" bedeutet: Das SDK verknüpft standardmäßig Geräte-/Nutzerdaten mit Daten Dritter oder liest die IDFA; ohne Zustimmung muss es in einen eingeschränkten Modus geschaltet werden. „Manifest-Pflicht" bezeichnet SDKs, die auf Apples Liste stehen und selbst `PrivacyInfo.xcprivacy` plus Signatur mitbringen müssen (Versionsstand prüfen).

| SDK / Paket (nativ · React Native) | Zweck | ATT nötig? | Manifest-Pflicht (Apple-Liste) | Was der Agent prüft |
|---|---|---|---|---|
| Firebase Analytics · `@react-native-firebase/analytics` | Analytics, Attribution via Google Ads | Ja, wenn Werbe-Attribution/Audiences aktiv; ohne AdSupport-Linking nein | Ja (FirebaseCore, FirebaseAnalytics u. a.) | `GOOGLE_ANALYTICS_DEFAULT_ALLOW_AD_PERSONALIZATION_SIGNALS`, ob `AdSupport` gelinkt ist |
| Firebase Crashlytics · `@react-native-firebase/crashlytics` | Crash-Reports | Nein | Ja | Keine Nutzer-IDs vor Consent (`setUserID`) |
| Firebase Messaging · `@react-native-firebase/messaging` | Push | Nein | Ja | – |
| Facebook SDK · `react-native-fbsdk-next` | Login, App Events, Werbung | Ja | Ja (FBSDKCoreKit, FBSDKLoginKit, FBAEMKit) | `FacebookAutoLogAppEventsEnabled`, `FacebookAdvertiserIDCollectionEnabled` false bis Zustimmung |
| Google Mobile Ads (AdMob) · `react-native-google-mobile-ads` | Werbung | Ja für personalisierte Werbung | Ja | `GADApplicationIdentifier`, UMP-Consent, ATT vor `start()` |
| AppsFlyer · `react-native-appsflyer` | Attribution | Ja | Ja | `waitForATTUserAuthorization` / `timeToWaitForATTUserAuthorization` |
| Adjust · `react-native-adjust` | Attribution | Ja | Ja | `ADJConfig` erst nach ATT; `attConsentWaitingInterval` |
| Branch · `react-native-branch` | Deep Links, Attribution | Ja bei Attribution | Ja | `branch_disable_ad_network_callouts`, ATT vor `initSession` |
| Singular / Kochava / Tenjin | Attribution | Ja | Ja (teilweise) | ATT-Status an SDK übergeben |
| AppLovin MAX · `react-native-applovin-max` | Werbung | Ja | Ja | Consent-Flow-Konfiguration |
| Unity Ads, IronSource/LevelPlay, Vungle, Chartboost, InMobi | Werbung | Ja | Ja (teilweise) | ATT vor Init |
| Amplitude · `@amplitude/analytics-react-native` | Produktanalytik | Nein, solange keine IDFA-Übergabe | Ja | `trackingOptions`, kein `setAdvertisingId` |
| Mixpanel · `mixpanel-react-native` | Produktanalytik | Nein (ohne IDFA) | Ja | `MixpanelAutomaticEvents`, keine IDFA |
| Segment · `@segment/analytics-react-native` | Event-Router | Abhängig von Zielen (Facebook, AppsFlyer → ja) | Ja | Welche Destinations eingebunden sind |
| Sentry · `@sentry/react-native` | Fehlerreporting | Nein | Ja | `sendDefaultPii` false bis Consent |
| Bugsnag · `@bugsnag/react-native` | Fehlerreporting | Nein | Ja | Nutzerdaten erst nach Consent |
| OneSignal · `react-native-onesignal` | Push, Marketing | Nein für reine Push; Ja bei Werbe-Attribution | Ja | `promptForPushNotificationsWithUserResponse` nicht beim Start |
| Braze · `@braze/react-native-sdk` | Marketing-Automation | Nein (ohne IDFA); Ja mit `setGoogleAdvertisingId`/IDFA | Ja | IDFA-Übergabe |
| Intercom · `@intercom/intercom-react-native` | Support-Chat | Nein | Ja | – |
| RevenueCat · `react-native-purchases` | Abo-Backend | Nein; Attribution-Integrationen (Adjust, AppsFlyer) → ja | Ja | `collectDeviceIdentifiers()` nur nach ATT |
| Alamofire, AFNetworking | Netzwerk | Nein | Ja | Version mit Manifest |
| Kingfisher, SDWebImage | Bilder-Cache | Nein | Ja | Version mit Manifest |
| Lottie (`lottie-ios`, `lottie-react-native`) | Animation | Nein | Ja | Version mit Manifest |
| RxSwift, Realm (`realm`, `@realm/react`) | Reactive / DB | Nein | Ja | Version mit Manifest |
| GoogleSignIn · `@react-native-google-signin/google-signin` | Login | Nein | Ja | – |
| Flutter/RN-Standard-Pakete: `react-native-device-info`, `@react-native-async-storage/async-storage`, `react-native-fs`, `react-native-mmkv` | Systemzugriff | Nein | Nicht auf Apple-Liste, nutzen aber Required-Reason-APIs → Manifest im Paket oder in `ios.privacyManifests` | Version aktuell genug |

Liste nicht abschließend; Stand der Apple-SDK-Liste September 2026. Der Agent soll jedes SDK mit unbekanntem Status als „ATT prüfen" markieren, statt es durchzuwinken.

#### 5.1.2 (ii) Zweckbindung

**Kern der Regel** – Daten, die für einen Zweck erhoben wurden, dürfen nicht ohne neue Einwilligung für einen anderen Zweck verwendet werden. Die Standortdaten für die Umkreissuche werden nicht zu Bewegungsprofilen für Werbepartner. Die E-Mail für den Login wird nicht zur Marketingliste.

**Risikostufe** – Mittel; im Code schwer zu erkennen, in der Datenschutzerklärung leicht.

**Woran du es im Code erkennst**
- Ein Datenobjekt (z. B. `userLocation`, `contacts`) wird an mehr als einen Empfänger gesendet (Backend und zusätzlich Analytics/Ads).
- `Analytics.logEvent` mit Parametern, die Rohdaten aus Berechtigungen enthalten (`lat`, `lng`, `email`).
- Newsletter-Opt-in als vorausgefüllte Checkbox im Registrierungsformular.

**Prüfliste**
- [ ] Sensible Rohdaten (Standort, Gesundheit, Kontakte) tauchen nicht in Analytics-Events auf.
- [ ] Marketing-Einwilligung ist getrennt und nicht vorausgewählt.

#### 5.1.2 (iii) Keine heimlichen Profile

**Kern der Regel** – Apps dürfen keine Nutzerprofile aus gesammelten Daten bilden, wenn der Nutzer davon nichts weiß. Dazu zählen Verhaltensprofile über mehrere Apps hinweg, Gerätefingerabdrücke und das Anreichern eigener Daten mit gekauften Datensätzen.

**Risikostufe** – Hoch.

**Woran du es im Code erkennst**
- Funktionen namens `fingerprint`, `deviceSignature`, `hardwareId`, die mehrere Systemwerte kombinieren (`ProcessInfo`, `UIDevice`, Bildschirmgröße, Zeitzone, Speicher, Tastaturen).
- SDKs mit „Device Intelligence" oder „Fraud Detection" (Fingerprint Pro, Seon, Sift) – zulässig nur bei Betrugsprävention mit Offenlegung, nicht für Werbung.
- Keychain-Einträge mit `kSecAttrAccessGroup` zum App-übergreifenden Wiederherstellen einer ID nach Neuinstallation.

**Prüfliste**
- [ ] Keine Kombination von Gerätemerkmalen zu einer stabilen ID für Tracking.
- [ ] Betrugsprävention-SDKs in der Datenschutzerklärung genannt und nur dafür verwendet.

#### 5.1.2 (iv) Kontakte und Fotos nicht als Datenbank

**Kern der Regel** – Es ist verboten, aus dem Adressbuch oder der Fotomediathek eine eigene Datenbank für interne oder externe Zwecke zu bauen. Die Nutzung ist auf die Funktion beschränkt, für die der Nutzer den Zugriff gegeben hat.

**Risikostufe** – Kritisch (vgl. 5.1.1 viii).

**Woran du es im Code erkennst** – siehe 5.1.1 (viii); zusätzlich: lokale Datenbanken (`CoreData`, `Realm`, `SQLite`, `WatermelonDB`) mit Tabellen, die komplette Kontaktdaten speichern.

**Prüfliste**
- [ ] Keine persistente Speicherung fremder Kontaktdaten über die Funktion hinaus.

#### 5.1.2 (v) Nachrichten an Kontakte nur auf Nutzerwunsch

**Kern der Regel** – Die App darf keine Nachrichten (SMS, E-Mail, Push, Messenger) an Kontakte des Nutzers senden, es sei denn, der Nutzer löst jede Nachricht selbst aus und sieht, was gesendet wird. Automatische „Einladungen an alle" sind unzulässig.

**Risikostufe** – Hoch.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `MFMessageComposeViewController` mit vorbefüllten `recipients` aus dem gesamten Adressbuch.
- Backend-Calls `/invite/bulk` mit Telefonnummern.

React Native/Expo:
- `expo-sms` `SMS.sendSMSAsync(allNumbers, text)`; `expo-mail-composer` mit `recipients: contacts.map(...)`.
- `Share.share()` ist in Ordnung, weil der Nutzer Empfänger selbst wählt.

**Typische Verstöße**

```tsx
// ❌ Einladung an alle Kontakte
await SMS.sendSMSAsync(contacts.map(c => c.phoneNumbers[0].number), inviteText);
// ✅ Nutzer wählt Empfänger, sieht den Text im System-Composer
await SMS.sendSMSAsync([selectedContact.number], inviteText);
```

**Prüfliste**
- [ ] Jede Nachricht an Dritte wird vom Nutzer einzeln ausgelöst und ist sichtbar.
- [ ] Keine serverseitigen Masseneinladungen mit hochgeladenen Nummern.

#### 5.1.2 (vi) Sensible APIs nicht für Marketing

**Kern der Regel** – Daten aus HealthKit, HomeKit, ClassKit, Bewegungs- und Fitness-APIs, dem ARKit-Gesichtstracking sowie der Tiefenkamera dürfen nicht für Werbung, Marketing oder Data-Mining genutzt und nicht an Werbenetzwerke, Datenhändler oder Analysedienste weitergegeben werden. Für HealthKit gelten die Details in 5.1.3.

**Risikostufe** – Kritisch.

**Woran du es im Code erkennst**
- `HKHealthStore`-Abfragen, deren Ergebnisse in `Analytics.logEvent`, Werbe-Targeting oder Segment-Traits landen.
- `ARFaceAnchor.blendShapes` oder Tiefendaten, die an einen Server geschickt werden.
- React Native: `react-native-health` `AppleHealthKit.getSamples` → `mixpanel.track('steps', ...)`.

**Prüfliste**
- [ ] Gesundheits-, HomeKit-, Bewegungs- und Gesichtsdaten erreichen keinen Analytics-/Werbe-Endpunkt.

#### 5.1.2 (vii) Apple Pay

**Kern der Regel** – Daten aus Apple-Pay-Transaktionen (Adresse, Name, Kontakt) dürfen nur zur Abwicklung der Bestellung an Dritte (Versanddienstleister, Zahlungsabwickler) gehen; Weiterverwendung für Marketing braucht eine eigene Zustimmung.

**Risikostufe** – Mittel.

**Woran du es im Code erkennst**
- `PKPaymentAuthorizationViewController` / `@stripe/stripe-react-native` `presentApplePay`: `PKPayment.shippingContact` und `billingContact` danach an CRM/Analytics übergeben.
- `requiredShippingContactFields` breiter als nötig (z. B. `.phoneNumber` bei digitalen Gütern).

**Prüfliste**
- [ ] Nur benötigte Kontaktfelder angefordert.
- [ ] Apple-Pay-Kontaktdaten nicht in Marketing-Tools.

### 5.1.3 Gesundheit und Gesundheitsforschung

#### 5.1.3 (i) Gesundheitsdaten nicht an Dritte für Werbung

**Kern der Regel** – Daten aus HealthKit, Clinical Health Records, MovementDisorderAPI, ResearchKit, CareKit und ähnlichen Quellen dürfen nicht für Werbung, Marketing oder Data-Mining genutzt oder zu diesem Zweck weitergegeben werden. Weitergabe an Dritte ist nur zulässig, wenn sie der Gesundheitsverwaltung oder -forschung dient und der Nutzer eingewilligt hat. Speicherung in iCloud ist untersagt (HealthKit-Daten dürfen nicht in CloudKit oder iCloud Drive landen).

**Risikostufe** – Kritisch.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `import HealthKit`, `HKHealthStore.requestAuthorization`, Entitlement `com.apple.developer.healthkit` (`.entitlements`-Datei), `NSHealthShareUsageDescription`, `NSHealthUpdateUsageDescription`.
- HealthKit-Werte in `NSUbiquitousKeyValueStore`, `CKRecord`, `NSPersistentCloudKitContainer`.
- `import ResearchKit` / `CareKit` mit Datenexport an nicht-medizinische Endpunkte.

React Native/Expo:
- `react-native-health` (HealthKit-Bridge), `react-native-health-connect` (nur Android), `@kingstinct/react-native-healthkit`; Expo braucht ein Config-Plugin mit Entitlement `com.apple.developer.healthkit` in `app.json` → `ios.entitlements`.
- Health-Werte in `Analytics`, `Braze`, `OneSignal`-Tags.

**Typische Verstöße**

```swift
// ❌ Schrittzahl als Werbe-Segment
Analytics.setUserProperty("\(steps > 10000)", forName: "active_user_segment")
```

```swift
// ✅ Nur lokal/zur Funktion, kein Analytics
let summary = HealthSummary(steps: steps)   // bleibt in der App-DB, nicht in iCloud
```

**Prüfliste**
- [ ] Health-Daten gehen an keinen Analytics-/Marketing-/Werbe-Endpunkt.
- [ ] Keine Speicherung von Health-Daten in iCloud/CloudKit.
- [ ] HealthKit-Entitlement nur, wenn tatsächlich Health-APIs genutzt werden.

**Empfohlene Behebung** – Health-Daten strikt in eigener Domäne halten; Server-Sync nur mit expliziter Zustimmung und ohne Marketing-Tools.

#### 5.1.3 (ii) Keine falschen Gesundheitsdaten

**Kern der Regel** – Apps dürfen keine falschen oder ungenauen Daten in HealthKit schreiben (etwa Schätzwerte als Messwerte ausgeben, oder Blutdruck aus einem Kamerabild „berechnen") und keine Gesundheitsdaten in der Keychain oder in unsicherer Weise speichern.

**Risikostufe** – Hoch; überschneidet sich mit 1.4.1 (medizinische Fehlinformation).

**Woran du es im Code erkennst**
- `HKQuantitySample` mit `quantityType(forIdentifier: .bloodPressureSystolic)`, `.bloodGlucose`, `.oxygenSaturation` ohne Sensor-Quelle (Bluetooth-Gerät, Apple Watch).
- Health-Werte in `UserDefaults` oder `AsyncStorage` ohne Verschlüsselung; sensible Werte in `SecureStore` sind ok, aber die Guideline verbietet explizit die Keychain als Health-Datenspeicher, weil sie nicht dafür gedacht ist.

**Prüfliste**
- [ ] Geschriebene HealthKit-Werte stammen aus echten Messungen oder Nutzereingaben, klar gekennzeichnet.
- [ ] Keine Gesundheitsdaten in UserDefaults/AsyncStorage/Keychain.

#### 5.1.3 (iii) Einwilligung bei Forschung

**Kern der Regel** – Apps, die Forschung an Menschen betreiben (klinische Studien, Umfragen mit Gesundheitsbezug), müssen die informierte Einwilligung jedes Teilnehmers einholen. Dazu gehören Art, Zweck und Dauer der Studie, Verfahren, Risiken und Nutzen, Vertraulichkeit, Kontaktstelle und der Hinweis, dass die Teilnahme jederzeit ohne Nachteile beendet werden kann. Für Minderjährige ist die Zustimmung eines Erziehungsberechtigten nötig.

**Risikostufe** – Kritisch.

**Woran du es im Code erkennst**
- `ORKConsentDocument`, `ORKVisualConsentStep`, `ORKConsentReviewStep` (ResearchKit) – vorhanden und vor der Datenerhebung durchlaufen?
- React Native: es gibt keine offizielle Bridge; eigene Consent-Screens prüfen, ob die Inhalte oben abgedeckt sind und ob es einen „Studie verlassen"-Pfad gibt.
- Datenerhebung (`HKObserverQuery`, Fragebögen) beginnt vor Abschluss des Consent-Flows.

**Prüfliste**
- [ ] Informed-Consent-Flow mit allen Pflichtinhalten vor der ersten Datenerhebung.
- [ ] Widerruf/Studienausstieg in der App möglich, Daten werden dann nicht weiter erhoben.
- [ ] Altersprüfung und Elternzustimmung bei Minderjährigen.

#### 5.1.3 (iv) Ethikkommission

**Kern der Regel** – Forschungs-Apps müssen die Zustimmung einer unabhängigen Ethikkommission (IRB, Ethikkommission der Landesärztekammer) nachweisen; Apple kann den Nachweis anfordern.

**Risikostufe** – Hoch (Metadaten/Nachweis, kein Code).

**Prüfliste**
- [ ] Ethikvotum vorhanden; Referenznummer in den App-Review-Notizen.
- [ ] Studien-ID und Sponsor in der App genannt.

### 5.1.4 Kinder

**Kern der Regel** – Apps, die sich an Kinder richten oder in der Kategorie „Kinder" erscheinen, unterliegen COPPA (USA), DSGVO Art. 8 (EU, Alter je Mitgliedstaat 13–16) und vergleichbaren Gesetzen. Apple verlangt: Keine Erhebung persönlicher Daten von Kindern ohne nachweisbare Elternzustimmung; Geburtsdatum oder Elterndaten dürfen nur zur Einhaltung dieser Gesetze abgefragt werden und dürfen nicht die Nutzung sperren, sondern nur die Funktionen anpassen. In der Kinder-Kategorie sind Drittanbieter-Analytics und -Werbung grundsätzlich verboten; Ausnahmen gelten nur, wenn das SDK nachweislich keine personenbezogenen Daten von Kindern erhebt (kein IDFA, keine Standortdaten, kontextuelle Werbung mit Prüfung). Ergänzend gelten die Regeln zur Kinder-Kategorie aus 1.3.

**Risikostufe** – Kritisch; Apple prüft Kinder-Apps manuell auf Netzwerkverkehr.

**Woran du es im Code erkennst**

Swift/Objective-C:
- App Store Connect Kategorie „Kids" bzw. Altersfreigabe 4+/9+ mit Kinder-Inhalten; im Code: `Info.plist` hat keinen Marker, daher Kategorie über Metadaten prüfen.
- Jegliche Imports aus der SDK-Tabelle oben mit „ATT nötig: Ja" sind in Kinder-Apps ein Verstoß.
- Firebase in Kinder-Apps: nur mit `FIREBASE_ANALYTICS_COLLECTION_DEACTIVATED = true` oder gar nicht.
- AdMob in Kinder-Apps: `GADMobileAds.sharedInstance().requestConfiguration.tagForChildDirectedTreatment = true` und `setSameAppKeyEnabled(false)` – selbst dann kritisch.
- Geburtstagsabfrage, die bei „zu jung" die App sperrt statt Funktionen anzupassen.
- Externe Links ohne Elternschranke (Parental Gate).

React Native/Expo:
- Pakete: `react-native-google-mobile-ads` mit `tagForChildDirectedTreatment: true` in `app.json`-Plugin-Optionen; `@react-native-firebase/analytics` in Kinder-Apps; `expo-tracking-transparency` sollte in Kinder-Apps gar nicht vorkommen.
- `Linking.openURL` zu Stores/Websites ohne Parental Gate (Rechenaufgabe, langes Drücken).

**Typische Verstöße**

```tsx
// ❌ Analytics in einer Kinder-App
import analytics from '@react-native-firebase/analytics';
analytics().logEvent('level_complete', { level, childName });
```

```swift
// ❌ Sperrt Kinder komplett aus, statt Funktionen anzupassen
if age < 13 { showBlockingScreen("Diese App ist nichts für dich") }
// ✅ Funktionen einschränken
if age < 13 { features = features.subtracting([.chat, .sharing]) }
```

**Prüfliste**
- [ ] Kinder-Kategorie: keine Tracking-/Werbe-/Analytics-SDKs mit personenbezogener Erhebung.
- [ ] Altersabfrage nur zur Anpassung, nicht als Ausschluss; kein Speichern des Geburtsdatums ohne Grund.
- [ ] Elternschranke vor externen Links, Käufen, Kontaktfunktionen.
- [ ] Datenschutzerklärung erwähnt COPPA/DSGVO-K-Prozess und Elternrechte.
- [ ] Kein Sign-in-Zwang; kein Sammeln von Namen, Fotos, Standort des Kindes.

**Empfohlene Behebung** – Werbe- und Analytics-SDKs entfernen; eigene, anonyme Nutzungsstatistik ohne IDs; Parental-Gate-Komponente.

### 5.1.5 Standortdienste

**Kern der Regel** – Standortdaten dürfen nur für Funktionen genutzt werden, die für die App direkt relevant sind. Die App muss den Nutzer über die Nutzung informieren und die Einwilligung über den Systemdialog einholen; keine Umgehung über IP-Geolokation ohne Hinweis. Hintergrundstandort braucht einen klaren Grund im Purpose-String und in der App-Beschreibung. Apps, die Standortdaten für Notfälle oder Rettung versprechen (Notruf-Apps, Alleinarbeiter-Schutz), müssen deutlich darauf hinweisen, dass sie kein Ersatz für Notrufdienste sind und vom Netz abhängen. Für die Nutzung mit der Kinder-Kategorie gilt zusätzlich 5.1.4.

**Risikostufe** – Hoch, besonders bei `Always`-Berechtigung ohne sichtbaren Grund.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `CLLocationManager.requestAlwaysAuthorization()`, `allowsBackgroundLocationUpdates = true`, `UIBackgroundModes` mit `location` in `Info.plist`.
- `startMonitoringSignificantLocationChanges`, `startMonitoring(for: CLRegion)`, `CLMonitor` – jeweils Zweck in der App erkennbar?
- `desiredAccuracy = kCLLocationAccuracyBest` bei Funktionen, denen `kCLLocationAccuracyKilometer` reicht (Datenminimierung 5.1.1 iii).
- Standort in Analytics-Events oder an Werbe-SDKs (`GADRequest.setLocation` ist seit 2023 entfernt, alte Aufrufe prüfen).
- Notfall-Versprechen in Strings („Wir rufen Hilfe", „SOS") ohne Disclaimer.

React Native/Expo:
- `expo-location`: `requestBackgroundPermissionsAsync`, `startLocationUpdatesAsync` mit `expo-task-manager`, `startGeofencingAsync`; Plugin-Option `isIosBackgroundLocationEnabled: true`, `UIBackgroundModes: ["location"]` in `app.json` → `ios.infoPlist`.
- Bare: `react-native-geolocation-service`, `@react-native-community/geolocation`, `react-native-background-geolocation` (Transistorsoft) – Hintergrundmodus prüfen.
- IP-basierte Geolokation (`ipapi.co`, `ip-api.com`) als stiller Ersatz nach Ablehnung.

**Typische Verstöße**

```swift
// ❌ Always ohne Hintergrundfunktion
locationManager.requestAlwaysAuthorization()   // App zeigt nur Filialen auf einer Karte
// ✅
locationManager.requestWhenInUseAuthorization()
```

```tsx
// ❌ Hintergrund-Tracking startet beim App-Start ohne Erklärung
await Location.startLocationUpdatesAsync(TASK, { accuracy: Accuracy.Highest });
// ✅ Erst nach Erklärung und Nutzeraktion ("Laufstrecke aufzeichnen")
```

❌ „Im Notfall alarmiert die App automatisch den Rettungsdienst" ohne Hinweis auf 112 und Netzabhängigkeit.

**Prüfliste**
- [ ] Standortabfrage nur für eine erkennbare Funktion; WhenInUse bevorzugt.
- [ ] Hintergrundstandort: Purpose-String erklärt den Grund; Funktion ist für den Nutzer sichtbar (Trip, Geofence-Erinnerung).
- [ ] Reduzierte Genauigkeit angeboten, wo möglich (`NSLocationDefaultAccuracyReduced`, `Accuracy.Low`).
- [ ] Keine Standortdaten in Analytics/Werbung.
- [ ] Notfall-Funktionen mit Disclaimer.
- [ ] Kein stiller IP-Geolocation-Ersatz nach Ablehnung.

**Empfohlene Behebung** – `expo-location` mit passender Genauigkeit und nur WhenInUse; nativ `CLLocationManager` mit `requestWhenInUseAuthorization` und temporärer Vollpräzision (`requestTemporaryFullAccuracyAuthorization`) nur bei Bedarf.

---

## 5.2 Geistiges Eigentum

### 5.2.1 Allgemein

**Kern der Regel** – Die App darf nur Inhalte enthalten, die der Entwickler selbst geschaffen hat oder für die er eine Lizenz besitzt: Code, Grafiken, Musik, Schriften, Marken, Namen, Charaktere. Apple kann Nachweise verlangen; im Zweifel wird die App bis zur Klärung abgelehnt.

**Risikostufe** – Hoch; bei Beschwerden von Rechteinhabern wird die App ohne Vorwarnung entfernt.

**Woran du es im Code erkennst**
- Asset-Kataloge (`Assets.xcassets`, `assets/`) mit Markenlogos Dritter, Filmfiguren, Sport-Vereinslogos, Emoji-Sets anderer Anbieter.
- Schriften in `UIAppFonts` / `expo-font` mit kommerziellen Lizenzen (Helvetica Neue, Proxima Nova, SF-Schriften außerhalb Apple-Plattformen).
- Musik/Sound-Dateien (`.mp3`, `.m4a`) ohne Lizenzhinweis im Repository; Dateinamen wie `intro_stranger_things.mp3`.
- Copy-Paste-Code mit fremden Copyright-Headern oder GPL-Bibliotheken in einer proprietären App (Lizenzverstoß ist Apple-Thema, weil der Rechteinhaber sich bei Apple beschwert).
- Strings mit Markennamen im App-Namen oder Untertitel („Guide für Fortnite", „Netflix Tracker").

**Typische Verstöße**

❌ App-Icon in `AppIcon.appiconset` ist eine abgewandelte Version eines bekannten Markenlogos.

❌ Quiz-App mit Datenbank an Filmstills.

✅ Eigene Illustrationen, lizenzierte Stock-Assets mit Lizenzdokument im Repo, SF Symbols nur auf Apple-Plattformen.

**Prüfliste**
- [ ] Alle Assets stammen vom Entwickler oder haben eine nachweisbare Lizenz.
- [ ] Schriften mit App-Embedding-Lizenz.
- [ ] Open-Source-Lizenzen (MIT, Apache, BSD) im Lizenz-Screen genannt; keine GPL in proprietärem Code ohne Klärung.
- [ ] Keine fremden Marken in Name, Icon, Screenshots.

### 5.2.2 Websites und Dienste Dritter

**Kern der Regel** – Wer Inhalte oder Dienste Dritter nutzt (Feeds, APIs, Websites), braucht deren Erlaubnis. Inoffizielle Clients, die eine fremde Plattform ohne Zustimmung nachbauen, Scraping von Websites, das Umgehen von Paywalls oder das Anzeigen fremder Inhalte in eigenem Rahmen ohne Vereinbarung sind unzulässig.

**Risikostufe** – Hoch. Klassische Fälle: inoffizielle Reddit-, Instagram-, YouTube-Clients; Fahrplan-Apps, die ohne API-Vertrag scrapen.

**Woran du es im Code erkennst**

Swift/Objective-C:
- HTML-Parser (`SwiftSoup`, `Kanna`, `Fuzi`) mit Requests gegen fremde Domains ohne offizielle API.
- Hardcodierte `User-Agent`-Strings, die Browser imitieren; Cookie-Jar-Handling gegen Fremdseiten.
- WebViews, die eine Fremdseite laden und per `WKUserScript` Werbung oder Login entfernen.
- API-Aufrufe mit inoffiziellen Endpunkten (`/api/v1/private`, reverse-engineerte Mobile-APIs) oder mit fremden App-Schlüsseln.

React Native/Expo:
- `cheerio`, `node-html-parser`, `react-native-html-parser` in `package.json` plus `fetch('https://www.<fremd>.de/...')`.
- `WebView` mit `injectedJavaScript`, das `.ad-container` entfernt oder Paywall-Overlays ausblendet.

**Typische Verstöße**

```ts
// ❌ Scraping einer Fremdseite ohne Lizenz
const html = await (await fetch('https://www.fremdportal.de/suche?q=' + q, {
  headers: { 'User-Agent': 'Mozilla/5.0 (iPhone ...)' } })).text();
const items = cheerio.load(html)('.result').map(...);
```

✅ Offizielle API mit Schlüssel, Nutzungsbedingungen im Repo abgelegt, Attribution in der App.

**Prüfliste**
- [ ] Jede Fremd-Domain im Code hat eine offizielle API oder schriftliche Erlaubnis.
- [ ] Keine HTML-Parser gegen fremde Seiten ohne Erlaubnis.
- [ ] Keine Skripte, die Werbung/Paywalls Dritter entfernen.
- [ ] Attribution/Nutzungsbedingungen des Anbieters erfüllt.

**Empfohlene Behebung** – Offizielle APIs; bei fehlender API Anbieter kontaktieren und Vereinbarung in den App-Review-Notizen erwähnen.

### 5.2.3 Audio- und Video-Downloads

**Kern der Regel** – Apps dürfen keine Musik oder Videos von Drittquellen (YouTube, SoundCloud, Vimeo, Instagram, TikTok) herunterladen, extrahieren, konvertieren oder streamen, wenn der jeweilige Anbieter das nicht ausdrücklich erlaubt. Auch „nur für den Privatgebrauch" oder „nur Creative-Commons" schützt nicht.

**Risikostufe** – Kritisch; solche Apps werden auch nach Freigabe rückwirkend entfernt.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `XCDYouTubeKit`, `YoutubeKit`, eigene `youtube-dl`/`yt-dlp`-Ports, Requests an `googlevideo.com`, `youtubei/v1/player`, Regex auf `ytInitialPlayerResponse`.
- `AVAssetExportSession` oder `ffmpeg-kit` mit Eingabe aus Fremd-Streams.
- Strings: „Download", „MP3 konvertieren", „Video speichern" in Kombination mit Fremd-URLs.

React Native/Expo:
- Pakete `react-native-ytdl`, `ytdl-core`, `react-native-youtube-iframe` (Anzeige ist ok, Download nicht), `ffmpeg-kit-react-native` mit Fremd-Streams, `expo-file-system` `downloadAsync` auf Stream-URLs.
- Backend-Endpoint, der die Extraktion serverseitig erledigt (`/api/extract?url=`); der Code in der App ist dann harmlos, der Zweck nicht.

**Typische Verstöße**

```ts
// ❌
const info = await ytdl.getInfo(videoUrl);
await FileSystem.downloadAsync(info.formats[0].url, FileSystem.documentDirectory + 'song.mp4');
```

✅ Wiedergabe über offiziellen Player (`YouTube iFrame`, `react-native-youtube-iframe`, MusicKit) ohne Speichern.

**Prüfliste**
- [ ] Kein Download/Extraktion von Fremdplattform-Medien, weder in der App noch über eigenes Backend.
- [ ] Wiedergabe von Fremdinhalten nur über offizielle Player/SDKs.
- [ ] Metadaten enthalten keine Download-Versprechen für Fremdplattformen.

### 5.2.4 Apple-Endorsements und Apple-Marken

**Kern der Regel** – Apps dürfen nicht den Eindruck erwecken, Apple habe sie geprüft, empfohlen oder unterstütze sie; und sie dürfen Apples Marken, Logos, Produktnamen und Icons nicht in einer Weise verwenden, die Apples Trademark-Richtlinien widerspricht. Das betrifft App-Namen („iPhone Cleaner Pro"), Icons mit Apfel-Logo, Screenshots mit Apple-Produkten als Hauptmotiv, Strings wie „von Apple empfohlen", und den Gebrauch von Apple-Markennamen in Untertiteln und Keywords. Erlaubt sind sachliche Kompatibilitätshinweise („für iPhone") nach den Trademark-Regeln.

**Risikostufe** – Hoch; Apple prüft Namen und Icons in jedem Review.

**Woran du es im Code erkennst**
- `CFBundleDisplayName`, `CFBundleName`, `app.json` → `expo.name`: enthält „Apple", „iPhone", „iPad", „Mac", „Watch", „Siri", „AirPods", „Vision" als Bestandteil des Namens (nicht als Kompatibilitätszusatz).
- Icon-Assets: stilisierte Äpfel, SF-Symbol-Icons als App-Icon (Symbol-Nutzung als Icon ist untersagt), Nachbildungen von System-App-Icons (Einstellungen-Zahnrad in Grau, grünes Telefon).
- Strings/Screens: „Apple approved", „Apple Partner", „von Apple ausgezeichnet" ohne tatsächliche Auszeichnung (Apple Design Award darf genannt werden).
- Produktnamen mit Apples Schreibweise verletzt: „IPhone", „Iphone", „MacOS" statt „macOS".

**Typische Verstöße**

❌ Name „Siri Shortcuts Manager" (Siri als Markenbestandteil im App-Namen).

❌ Icon mit SF Symbol `apple.logo`.

✅ Name „ShortcutBox – kompatibel mit Siri"; eigenes Icon.

**Prüfliste**
- [ ] App-Name/Untertitel ohne Apple-Marken als Bestandteil.
- [ ] Icon ohne Apple-Logo, SF Symbols oder nachgebaute System-Icons.
- [ ] Kein Endorsement-Anspruch in Strings, Screenshots, Onboarding.
- [ ] Korrekte Schreibweise der Apple-Produktnamen.

### 5.2.5 Nachahmung von Apple-Produkten

**Kern der Regel** – Apps dürfen keine Apple-Produkte, Apple-Apps, Schnittstellen, Werbeslogans oder Icons nachbilden, mit ihnen verwechselbar sein oder vorgeben, Apple-Funktionen zu sein. Das umfasst nachgebaute Systemdialoge, gefälschte Einstellungs-Oberflächen, „Apple Music Alternative"-Klone mit identischem Layout, gefakte Apple-Stores oder Apple-Support-Chats.

**Risikostufe** – Kritisch, wenn Verwechslungsgefahr besteht; bei Support- oder Store-Nachahmung Betrugsverdacht.

**Woran du es im Code erkennst**
- Custom Views, die `UIAlertController` pixelgenau nachbauen, um z. B. Berechtigungen zu „erfragen" (siehe auch 5.1.1 iv) oder Apple-ID-Passwörter abzufragen.
- Screens mit Titeln wie „Apple ID", „Apple Support", „iCloud-Anmeldung" außerhalb der offiziellen APIs (`ASAuthorizationController`).
- Assets von System-Apps (Einstellungen, App Store, Wallet) im Bundle.
- React Native: UI-Kits, die „iOS Settings Clone" liefern, in Kombination mit Passwortfeldern.

**Prüfliste**
- [ ] Keine nachgebauten Systemdialoge mit Eingabefeldern.
- [ ] Keine Nachahmung von Apple-Apps, -Stores, -Support.
- [ ] Apple-Login ausschließlich über Sign in with Apple / `expo-apple-authentication`.

---

## 5.3 Glücksspiel, Lotterien, Gewinnspiele

### 5.3.1 Gewinnspiele vom Entwickler gesponsert

**Kern der Regel** – Gewinnspiele, Verlosungen und Wettbewerbe in einer App müssen vom Entwickler der App selbst verantwortet und gesponsert werden, nicht von einem anonymen Dritten.

**Risikostufe** – Mittel.

**Woran du es im Code erkennst**
- Gewinnspiel-Screens, Strings wie „Gewinnspiel", „Verlosung", „Raffle", „Giveaway", „Sweepstakes"; Backend-Endpoints `/contest`, `/raffle`.
- Teilnahmebedingungen nennen einen anderen Veranstalter als den Entwickler.

**Prüfliste**
- [ ] Veranstalter des Gewinnspiels ist der App-Entwickler oder klar benannter Partner mit Vertrag.

### 5.3.2 Offizielle Regeln und Apple-Disclaimer

**Kern der Regel** – Die offiziellen Regeln jedes Gewinnspiels müssen in der App einsehbar sein und ausdrücklich klarstellen, dass Apple weder Sponsor noch in irgendeiner Weise beteiligt ist. Die Regeln enthalten Teilnahmeberechtigung, Zeitraum, Gewinne, Auswahlverfahren, Ausschluss von Rechtsweg soweit zulässig und Datenschutzhinweise.

**Risikostufe** – Hoch; fehlender Apple-Disclaimer ist ein häufiger, leicht behebbarer Ablehnungsgrund.

**Woran du es im Code erkennst**
- Suche nach „Apple ist nicht Sponsor", „Apple is not a sponsor", „not affiliated with Apple" in Strings/Lokalisierungen (`Localizable.strings`, `i18n/*.json`).
- Gewinnspiel-Screen ohne Link/Modal zu Teilnahmebedingungen.
- Regeln nur auf externer Website hinter Login.

**Typische Verstöße**

❌ Push-Nachricht „Gewinne ein iPhone 17!" mit Teilnahme per Button – keine Regeln, kein Disclaimer, zudem Apple-Produkt als Werbeköder (5.2.4).

✅ Screen „Teilnahmebedingungen" mit vollständigen Regeln und Satz „Apple Inc. ist weder Sponsor noch in irgendeiner Form an diesem Gewinnspiel beteiligt."

**Prüfliste**
- [ ] Regeln in der App einsehbar (nicht nur extern).
- [ ] Apple-Disclaimer im Regeltext.
- [ ] Datenschutzhinweis zur Gewinnspieldatenverarbeitung.

### 5.3.3 Kein IAP für Echtgeld-Spielguthaben

**Kern der Regel** – In-App-Käufe dürfen nicht genutzt werden, um Guthaben oder Währung für Echtgeld-Glücksspiel zu kaufen, Lotterie- oder Tombola-Lose zu erwerben oder Geldtransfers auszulösen. Echtgeld-Einzahlungen laufen über die vom Betreiber lizenzierten Zahlungswege außerhalb von StoreKit. Umgekehrt muss Spielgeld in reinen Simulationen (Social Casino ohne Auszahlung) über IAP verkauft werden (Abschnitt 3.1.1).

**Risikostufe** – Kritisch; verstößt gleichzeitig gegen Apples Provisionsregeln und gegen Glücksspielrecht.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `StoreKit`-Produkte (`Product.products(for:)`, `SKProductsRequest`) mit IDs wie `chips_1000`, `casino_credit`, `bet_balance`, `lottery_ticket`, kombiniert mit Auszahlungsfunktionen (`withdraw`, `cashout`, `payout`).
- Umgekehrt: Social-Casino-App mit Stripe/PayPal statt IAP → Verstoß gegen 3.1.1.

React Native/Expo:
- `expo-in-app-purchases` (veraltet), `react-native-iap`, `react-native-purchases` mit Produkt-IDs, die Guthaben für Echtgeld-Spiele darstellen.
- Wallet-Screens mit „Einzahlen" über StoreKit und „Auszahlen" über Bank.

**Prüfliste**
- [ ] Echtgeld-Einzahlungen nicht über IAP.
- [ ] Keine Lose/Tickets über IAP.
- [ ] Simuliertes Glücksspiel ohne Auszahlung: Spielgeld über IAP (Abgrenzung dokumentiert).

### 5.3.4 Echtgeld-Glücksspiel und Lotterien

**Kern der Regel** – Apps mit Echtgeld-Glücksspiel (Sportwetten, Poker, Casino, Pferderennen) und Lotterie-Apps brauchen Lizenzen und Genehmigungen für jede Region, in der sie nutzbar sind, müssen per Geofencing auf diese Regionen beschränkt sein und müssen kostenlos im App Store sein. Lotterien müssen die drei Merkmale Einsatz, Zufall und Gewinn tatsächlich erfüllen und lizenziert sein; in Deutschland, Österreich und der Schweiz bedeutet das in der Praxis staatliche oder staatlich konzessionierte Anbieter. Illegale Hilfsmittel wie Kartenzähler sind verboten. Die Alters- und Standortprüfung muss echt sein: Geofencing auf Basis des tatsächlichen Gerätestandorts, nicht der Store-Region oder einer Nutzerangabe. Unter 2.5.13 ist zusätzlich die Verteilung als reine Web-Wrapper-App eingeschränkt, hier nur der Hinweis.

**Risikostufe** – Kritisch; ohne Lizenznachweis wird nicht freigegeben, bei fehlendem Geofencing rückwirkend entfernt.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Kein `CoreLocation`-Import in einer Wett-App ist bereits ein Befund.
- Geofencing-Logik: `CLLocationManager` mit `requestWhenInUseAuthorization`, Vergleich gegen erlaubte Bundesländer/Länder (`CLGeocoder.reverseGeocodeLocation`, eigene Polygon-Prüfung, Drittanbieter wie GeoComply `GCSDK`).
- Prüfung auf Standort-Spoofing: `CLLocation.sourceInformation?.isSimulatedBySoftware`, `isProducedByAccessory` (iOS 15+); Jailbreak-Erkennung.
- Altersverifikation: Identitätsprüfungs-SDK (IDnow, Jumio, Onfido, `NSIdentityUsageDescription` für Wallet-Ausweis) statt bloßem Geburtsdatum-Feld.
- Preisgestaltung: App darf kein Paid-Download sein (Metadaten).

React Native/Expo:
- `expo-location` `getCurrentPositionAsync` mit Region-Prüfung; `startGeofencingAsync` mit erlaubten Regionen; fehlt beides → Befund.
- `Localization.region` (`expo-localization`) oder Store-Land als Ersatz für echten Standort ist unzureichend.
- `react-native-device-info` `isEmulator()`/Jailbreak-Checks (`jail-monkey`) als Spoofing-Schutz.

**Typische Verstöße**

```tsx
// ❌ Region aus Geräteeinstellungen statt Standort
if (Localization.region === 'DE') enableBetting();
```

```swift
// ✅ Echter Standort, Spoofing-Check, serverseitige Freigabe
guard let loc = locations.last,
      loc.sourceInformation?.isSimulatedBySoftware == false else { blockPlay(); return }
api.checkJurisdiction(lat: loc.coordinate.latitude, lng: loc.coordinate.longitude)
```

❌ Wett-App mit Preis 0,99 €.

❌ Altersprüfung ist ein Toggle „Ich bin über 18".

**Prüfliste**
- [ ] Lizenzen je Region vorbereitet (Lizenznummer in App-Review-Notizen).
- [ ] Geofencing auf Basis des echten Gerätestandorts, serverseitig geprüft.
- [ ] Spoofing-/Jailbreak-Erkennung vorhanden.
- [ ] Altersverifikation über Identitätsprüfung.
- [ ] App kostenlos; kein IAP für Einsätze (5.3.3).
- [ ] Keine Kartenzähler oder andere Glücksspiel-Hilfsmittel.
- [ ] Lotterie: Einsatz, Zufall, Gewinn vorhanden und lizenziert.

**Empfohlene Behebung** – `expo-location` (Expo) bzw. `react-native-geolocation-service` (bare) für den Standort, serverseitige Jurisdiktionsprüfung, spezialisierte Geo-Compliance-SDKs für regulierte Märkte.

---

## 5.4 VPN-Apps

**Kern der Regel** – Apps, die VPN-Dienste anbieten, müssen die `NEVPNManager`-API (NetworkExtension, Personal VPN) verwenden und dürfen den Tunnel nicht über Umwege (Proxy-Konfiguration per Profil, Socket-Tricks) aufbauen. Sie müssen in der App und in App Store Connect klar erklären, welche Daten erhoben und wie sie verwendet werden; sie dürfen Nutzerdaten nicht an Dritte verkaufen, weitergeben oder für andere Zwecke nutzen. Das Personal-VPN-Entitlement erhält nur der Anbieter selbst; Apps dürfen VPN-Funktionen nicht zur Umgehung lokaler Gesetze anbieten und müssen in Ländern mit VPN-Lizenzpflicht (z. B. China) die Lizenz in den App-Review-Notizen nachweisen. Apps von Unternehmen für den internen Gebrauch (Enterprise-Distribution, MDM) unterliegen nicht dem App Store, dürfen aber nicht als „VPN für alle" im Store erscheinen. Kindersicherungs-, Inhaltsfilter- und Sicherheits-Apps zugelassener Anbieter dürfen `NEVPNManager` ebenfalls nutzen, müssen aber offenlegen, was gefiltert wird.

**Risikostufe** – Kritisch; VPN-Apps werden besonders genau auf Datenabfluss geprüft, und in einigen Regionen ist der Vertrieb ganz untersagt.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `import NetworkExtension`, `NEVPNManager.shared()`, `NETunnelProviderManager`, `NEPacketTunnelProvider` (Extension-Target), `NEAppProxyProvider`, `NEFilterDataProvider`.
- Entitlements: `com.apple.developer.networking.vpn.api` mit `allow-vpn`, `com.apple.developer.networking.networkextension` mit `packet-tunnel-provider`, `app-proxy-provider`, `content-filter-provider`, `dns-proxy`.
- Protokolle: `NEVPNProtocolIKEv2`, `NEVPNProtocolIPSec`; WireGuard/OpenVPN nur über Packet Tunnel Provider.
- Verstoß-Muster: Installation eines `.mobileconfig` mit VPN-Payload über Safari statt `NEVPNManager`; Proxy-Einstellungen per Konfigurationsprofil.
- Datenabfluss: Analytics-/Werbe-SDKs in einer VPN-App (Tabelle oben) sind ein Widerspruch zum „keine Weitergabe"-Versprechen; DNS-Logs an Dritte.

React Native/Expo:
- Expo Managed unterstützt keine NetworkExtension; ein VPN erfordert Bare-Workflow oder Development Build mit nativem Modul (`react-native-vpn-ipsec`, `react-native-simple-openvpn`, eigene Bridge). Prüfen: Entitlements in `app.json` → `ios.entitlements` und Extension-Target via Config-Plugin.
- „VPN"-Apps in reinem JS, die nur einen HTTP-Proxy in einer WebView setzen, erfüllen die Regel nicht.

**Typische Verstöße**

```swift
// ❌ Tunnel per Konfigurationsprofil statt API
UIApplication.shared.open(URL(string: "https://vpn.example.com/profile.mobileconfig")!)
```

```swift
// ✅ NEVPNManager
let manager = NEVPNManager.shared()
manager.loadFromPreferences { _ in
    let proto = NEVPNProtocolIKEv2(); proto.serverAddress = host
    manager.protocolConfiguration = proto; manager.isEnabled = true
    manager.saveToPreferences { _ in try? manager.connection.startVPNTunnel() }
}
```

❌ VPN-App bindet AppsFlyer und Facebook SDK ein und sendet Verbindungsereignisse mit IDFA.

**Prüfliste**
- [ ] VPN ausschließlich über `NEVPNManager` / Packet Tunnel Provider; passende Entitlements vorhanden.
- [ ] Datenschutzerklärung nennt exakt, welche Verbindungsdaten erhoben werden und wie lange (No-Log-Versprechen müssen zum Code passen).
- [ ] Keine Weitergabe an Dritte; keine Werbe-/Attributions-SDKs mit Tracking.
- [ ] Keine Installation von Konfigurationsprofilen für den Tunnel.
- [ ] Lizenznachweis für Länder mit VPN-Lizenzpflicht in den Review-Notizen; Verfügbarkeit dort ggf. abgeschaltet.
- [ ] Inhaltsfilter/Kindersicherung: Offenlegung, was gefiltert wird.

**Empfohlene Behebung** – Bare React Native mit nativem NetworkExtension-Target (kein Expo-Go-Weg); nativ `NEVPNManager` bzw. `NETunnelProviderManager`.

---

## 5.5 Mobile Device Management

**Kern der Regel** – MDM-Apps dürfen nur von Unternehmen (für eigene Mitarbeiter), Bildungseinrichtungen, Behörden und – in engen Grenzen – Anbietern von Kindersicherung stammen. Sie müssen in App Store Connect beim MDM-Entitlement angeben, welche Daten sie erheben, und dürfen diese Daten ausschließlich für den Verwaltungszweck nutzen: keine Weitergabe an Dritte, keine Nutzung für Werbung oder Marketing, kein Datenverkauf. Apps, die Konfigurationsprofile installieren oder zur Installation anleiten, müssen dieselben Regeln einhalten. Kindersicherungs-Apps sollen die dafür vorgesehenen Frameworks nutzen (Screen Time API: FamilyControls, ManagedSettings, DeviceActivity) statt MDM oder VPN-Tricks; Apple hat 2019 genau dafür zahlreiche Apps entfernt. Apps dürfen den Nutzer nicht dazu verleiten, Supervision oder MDM-Registrierung zu aktivieren, ohne die Konsequenzen zu erklären.

**Risikostufe** – Kritisch; das MDM-Entitlement wird nur nach Prüfung des Unternehmenszwecks vergeben.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Entitlement `com.apple.developer.mdm-managed-associated-domains`? Nein – relevant ist das MDM-Entitlement in App Store Connect plus `com.apple.developer.networking.networkextension` bei Kombination; im Code: `ManagedAppConfiguration` (`UserDefaults.standard.dictionary(forKey: "com.apple.configuration.managed")`), `com.apple.feedback.managed`.
- Kindersicherung: `import FamilyControls`, `AuthorizationCenter.shared.requestAuthorization(for: .child)`, `import ManagedSettings`, `import DeviceActivity`, Entitlement `com.apple.developer.family-controls` – korrekter Weg.
- Verstoß-Muster: Anleitung zur Installation eines `.mobileconfig` mit MDM-Payload bei einer Consumer-App; `NEFilterDataProvider` oder `NEVPNManager` als Kindersicherung ohne Screen-Time-API in einer Consumer-App; Ausleitung der Geräte-Inventardaten (`UIDevice.identifierForVendor`, installierte Apps, Standort) an Analytics.
- Werbe-SDKs in einer MDM-App.

React Native/Expo:
- Managed App Config: `react-native-mdm`/`react-native-managed-app-config` (`MDMAppConfig.getAppConfig()`), Expo: `expo-managed-app-config` (Community) – zulässig für verwaltete Apps.
- Screen Time API hat keine Expo-Abstraktion; nur über natives Modul in Bare-Workflow.
- WebView-Screens mit „Profil installieren"-Anleitung.

**Typische Verstöße**

❌ Consumer-Kindersicherungs-App, die ein MDM-Profil per Safari installiert, um Apps zu sperren.

✅ `FamilyControls` + `ManagedSettings` für App-Sperren; Elternzustimmung über `AuthorizationCenter`.

❌ MDM-App für Firmenkunden mit Firebase Analytics, das Geräte-Inventar als Event-Parameter sendet.

**Prüfliste**
- [ ] Zielgruppe ist Unternehmen/Bildung/Behörde oder Kindersicherung; kein Consumer-MDM.
- [ ] Erhobene Daten in App Store Connect beim Entitlement deklariert; Code entspricht dem.
- [ ] Keine Weitergabe, keine Werbung, keine Analytics mit Gerätedaten.
- [ ] Kindersicherung über Screen Time API statt MDM/VPN.
- [ ] Konfigurationsprofile nur mit klarer Erklärung; keine Verleitung zur Supervision.

**Empfohlene Behebung** – FamilyControls/ManagedSettings/DeviceActivity für Kinderschutz; Managed App Configuration statt eigener Profil-Installation; bei Firmen-Apps Custom-App-Distribution über Apple Business Manager prüfen.

---

## 5.6 Verhaltenskodex für Entwickler

Apple beschreibt den Kodex als Erwartung an respektvollen Umgang mit Nutzern, anderen Entwicklern und Apple. Wiederholtes manipulatives, betrügerisches oder missbräuchliches Verhalten führt zum Ausschluss aus dem Developer Program – unabhängig von der einzelnen App. Für den Agenten sind vor allem 5.6.1 und 5.6.3 im Code sichtbar; die übrigen Punkte betreffen Konto und Kommunikation.

### 5.6.1 Kundenbewertungen

**Kern der Regel** – Bewertungen dürfen nur über die System-API angefragt werden (`SKStoreReviewController.requestReview` bzw. `AppStore.requestReview` / `RequestReviewAction` in SwiftUI). Das System entscheidet, ob und wann der Dialog erscheint; die App darf keinen eigenen Bewertungsdialog anzeigen, darf nicht per Custom-UI zur Bewertung auffordern und darf Nutzer nicht filtern (zufriedene in den Store, unzufriedene ins Support-Formular). Anreize für Bewertungen (Belohnungen, Freischaltungen, Rabatte) sind untersagt, ebenso das Bitten um „5 Sterne". Apple erwartet außerdem, dass Entwickler auf Bewertungen respektvoll antworten und keine gefälschten oder gekauften Bewertungen einsetzen.

**Risikostufe** – Hoch; eigene Rating-Prompts sind ein sehr häufiger Ablehnungsgrund, und Bewertungsmanipulation zieht Konto-Sperren nach sich.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Zulässig: `import StoreKit`, `SKStoreReviewController.requestReview(in: windowScene)`, `AppStore.requestReview(in:)`, `@Environment(\.requestReview)`.
- Verstoß: `UIAlertController` mit Titeln wie „Gefällt dir die App?", „Bewerte uns", „Rate us"; Buttons „Ja, gerne" / „Nicht jetzt", die je nach Antwort `itms-apps://…?action=write-review` öffnen oder ein Feedback-Formular.
- Direktlinks auf `write-review` sind zulässig, wenn sie als neutrale Schaltfläche („Im App Store bewerten") in den Einstellungen liegen und nicht über ein Vorfilter-Modal.
- Belohnungslogik: `if didRate { grantCoins() }`, Strings „Bewerte uns und erhalte…".
- Eigene Rating-Frameworks: `Appirater`, `iRate`, `Armchair`, `SwiftRater` in alten Konfigurationen mit Custom-Alert statt System-API.

React Native/Expo:
- Zulässig: `expo-store-review` (`StoreReview.requestReview()`, `StoreReview.hasAction()`), bare `react-native-store-review` oder `react-native-in-app-review` (`InAppReview.RequestInAppReview()`), jeweils ohne Vorschaltdialog.
- Verstoß: `Alert.alert('Gefällt dir die App?', ..., [{ text: 'Ja' }, { text: 'Nein' }])` mit Verzweigung; `react-native-rate` mit `preferInApp: false` und eigener Vorabfrage; `Linking.openURL('itms-apps://...write-review')` nur nach Filterung.
- Belohnungen: `AsyncStorage.setItem('rated', 'true')` gekoppelt an `unlockPremium()`.

**Typische Verstöße**

```tsx
// ❌ Vorfilterung: nur zufriedene Nutzer in den Store
Alert.alert('Gefällt dir die App?', '', [
  { text: 'Nein', onPress: openSupportForm },
  { text: 'Ja', onPress: () => Linking.openURL(storeReviewUrl) },
]);
```

```tsx
// ✅ System-API ohne Vorfilter, an einen positiven Moment gebunden
if (await StoreReview.hasAction()) await StoreReview.requestReview();
```

```swift
// ❌ Belohnung für Bewertung
Button("Bewerte uns und erhalte 7 Tage Premium") { openStore(); unlockPremium() }
// ✅
Button("Im App Store bewerten") { openStoreWriteReview() }   // neutral, in den Einstellungen
```

**Prüfliste**
- [ ] Bewertungsanfrage nur über `SKStoreReviewController`/`AppStore.requestReview`/`expo-store-review`.
- [ ] Keine eigenen „Gefällt dir die App?"-Dialoge, keine Verzweigung nach Stimmung.
- [ ] Keine Anreize oder Freischaltungen für Bewertungen.
- [ ] Direktlink zum Schreiben einer Bewertung nur als neutrale Option, nicht nach Filterung.
- [ ] Anfrage nicht bei App-Start, nicht in Schleife, nicht nach Fehlern.

**Empfohlene Behebung** – `expo-store-review` (Expo) bzw. `react-native-in-app-review` (bare); nativ `AppStore.requestReview`. Feedback-Formular als eigenständige Option ohne Kopplung an die Bewertungsfrage.

### 5.6.2 Entwickleridentität

**Kern der Regel** – Die Angaben zum Entwickler (Name, Adresse, Kontaktdaten in App Store Connect und im Impressum der App) müssen echt und aktuell sein. Tarnfirmen, gefälschte Identitäten, mehrere Konten zur Umgehung von Sperren und das Verschleiern des wahren Betreibers sind verboten. In der EU müssen Apps mit Handelsbezug ein vollständiges Impressum (DSA-Trader-Status) hinterlegen, das Apple im Store anzeigt.

**Risikostufe** – Kritisch für das Konto; im Code nur indirekt sichtbar.

**Woran du es im Code erkennst**
- Impressum-/About-Screen: Firmenname, Adresse, E-Mail vorhanden und konsistent mit `NSHumanReadableCopyright` und `app.json` → `expo.owner`?
- Support-URL im Code (`support@…`, Kontaktformular) funktioniert und gehört zur genannten Organisation.
- Generische Firmennamen („App Studio LLC") mit Postfach-Adressen und Wegwerf-Mailadressen sind ein Warnsignal.

**Prüfliste**
- [ ] Impressum/Kontakt in der App vorhanden und korrekt.
- [ ] Angaben in App Store Connect, Datenschutzerklärung und App stimmen überein.
- [ ] Trader-Status (EU) korrekt hinterlegt.

### 5.6.3 Discovery-Betrug

**Kern der Regel** – Manipulation der Sichtbarkeit im App Store ist untersagt: Keyword-Stuffing im Namen oder Untertitel, irrelevante Suchbegriffe, gekaufte Downloads oder Bewertungen, Anreiz-Installationen zur Chart-Manipulation, Missbrauch von Empfehlungsprogrammen, Klon-Apps zur Belegung von Suchergebnissen, Nachahmung erfolgreicher App-Namen. Apple betrachtet auch In-App-Mechaniken kritisch, die Nutzer zu massenhaften Installationen anderer Apps des Entwicklers drängen.

**Risikostufe** – Hoch; Konto-Sperre bei Wiederholung.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `CFBundleDisplayName` mit Keyword-Ketten („Fitness Tracker Schrittzähler Kalorien Abnehmen Diät").
- Hardcodierte Referral-Mechaniken: „Installiere 5 Apps und erhalte Premium", `SKOverlay`/`SKStoreProductViewController` in Schleifen mit Belohnungen.
- Bot-artige Endpunkte `/boost`, `/fake-install` (selten, aber vorgekommen).

React Native/Expo:
- `app.json` → `expo.name` mit Keyword-Ketten.
- Referral-Screens mit Belohnung für Installation *fremder* Apps (Offerwalls können zulässig sein, wenn sie nach 3.2.2 gestaltet sind, aber nicht zur Chart-Manipulation).

**Prüfliste**
- [ ] App-Name ist ein Name, keine Keyword-Liste.
- [ ] Keine Belohnung für Installationen/Bewertungen anderer Apps.
- [ ] Keine Nachahmung bekannter App-Namen/Icons.

### 5.6.4 App-Qualität

**Kern der Regel** – Apple wertet Bewertungen, Absturzraten, Rückerstattungsquoten und Support-Beschwerden aus. Apps, die dauerhaft schlecht bewertet werden, häufig abstürzen oder deren Entwickler nicht auf Probleme reagiert, können aus dem Store entfernt werden, und das Entwicklerkonto kann verlieren, neue Apps einzureichen. Das ist keine Review-Regel im engeren Sinn, sondern eine fortlaufende Bewertung.

**Risikostufe** – Mittel für die einzelne Einreichung, Hoch für das Konto.

**Woran du es im Code erkennst**
- Crash-Reporting eingebunden (Crashlytics, Sentry, Bugsnag, MetricKit `MXMetricManager`)? Ohne Fehlerberichterstattung fehlt die Grundlage, Abstürze zu beheben.
- Unbehandelte Fehler: `try!`, `!`-Unwrapping auf Netzwerkdaten, `fatalError` in Produktionspfaden; RN: fehlende `ErrorBoundary`, unbehandelte Promise-Rejections.
- Fehlender Support-Weg in der App (siehe 5.6.2).

**Prüfliste**
- [ ] Crash-Reporting aktiv (datenschutzkonform, siehe 5.1.1 ii).
- [ ] Kritische Pfade ohne `try!`/Force-Unwrap; RN mit `ErrorBoundary`.
- [ ] Support-Kontakt erreichbar.

### 5.6.5 Kommunikation mit App Review

**Kern der Regel** – Im Umgang mit App Review gilt Ehrlichkeit: Review-Notizen, Demo-Konten und Erklärungen müssen zutreffen. Unzulässig sind Test-Accounts, die andere Funktionen zeigen als Produktions-Accounts, serverseitige Schalter, die während der Prüfung Inhalte verbergen oder anders darstellen (Review-Modus), Beschimpfungen oder Drohungen gegenüber Reviewern und das wiederholte Einreichen identischer Builds ohne Änderung nach einer Ablehnung. Wer nach einer Ablehnung anderer Meinung ist, nutzt den Appeal-Prozess oder den App Review Board.

**Risikostufe** – Kritisch für das Konto; Review-Modus-Schalter im Code sind ein sofortiger Ablehnungsgrund (siehe auch 2.3.1).

**Woran du es im Code erkennst**

Swift/Objective-C:
- Flags wie `isReviewMode`, `isAppleReview`, `reviewBuild`, `hideForReview`, gespeist aus Remote Config (`RemoteConfig.remoteConfig()["review_mode"]`), aus Datum-Vergleichen (`if Date() < releaseDate`), aus IP-Bereichen von Apple oder aus dem Demo-Account-Namen.
- Bedingte Navigation: `if user.email == "reviewer@…" { showLimitedFeatures() }`.

React Native/Expo:
- `remoteConfig().getValue('review_mode')`, `Constants.expoConfig.extra.reviewMode`, `process.env.EXPO_PUBLIC_REVIEW_MODE`, `Updates`-Kanäle, die nach der Freigabe andere JS-Bundles ausliefern als geprüft (siehe 2.5.2 – OTA-Updates dürfen den Zweck der App nicht ändern).
- `if (DeviceInfo.getCarrier() === 'Apple')` oder Geo-IP-Checks auf Cupertino.

**Typische Verstöße**

```ts
// ❌ Inhalte während der Prüfung verstecken
const reviewMode = remoteConfig().getValue('apple_review').asBoolean();
const tabs = reviewMode ? baseTabs : [...baseTabs, gamblingTab];
```

✅ Ein Build, ein Verhalten; Demo-Account zeigt dieselben Funktionen wie ein zahlender Kunde; Besonderheiten (Hardware-Zubehör, Standortbindung) im Review-Notizfeld mit Video erklärt.

**Prüfliste**
- [ ] Keine Review-Modus-Schalter (Remote Config, Datum, IP, Account-Name).
- [ ] Demo-Account voll funktionsfähig und identisch zur Produktion.
- [ ] OTA-Update-Kanäle liefern keine anderen Funktionen als der geprüfte Build.
- [ ] Review-Notizen erklären Hardware-, Standort- oder Lizenzabhängigkeiten wahrheitsgemäß.

---

## Paketreferenz React Native / Expo

| Zweck | Expo | Bare React Native |
|---|---|---|
| Datenschutzerklärung anzeigen | `expo-web-browser` (`openBrowserAsync`) | `react-native-inappbrowser-reborn` |
| App Tracking Transparency / IDFA | `expo-tracking-transparency` | `react-native-tracking-transparency`, `react-native-permissions` (`APP_TRACKING_TRANSPARENCY`) |
| Privacy Manifest | `app.json` → `ios.privacyManifests` (SDK 51+) | `ios/<App>/PrivacyInfo.xcprivacy` manuell |
| Purpose Strings setzen | Plugin-Optionen (`expo-camera`, `expo-location` …) oder `ios.infoPlist` | `ios/<App>/Info.plist`, `InfoPlist.strings` |
| Berechtigungsstatus prüfen | je Modul `get…PermissionsAsync()` | `react-native-permissions` (`check`, `request`) |
| Kamera / Fotos ohne Vollzugriff | `expo-image-picker` (`launchImageLibraryAsync`), `expo-camera` | `react-native-image-picker`, `react-native-vision-camera` |
| Kontakte per Picker | `expo-contacts` (`presentContactPickerAsync`) | `react-native-contacts` (`openContactForm` / Picker) |
| Standort (Vordergrund/Hintergrund/Geofencing) | `expo-location` + `expo-task-manager` | `react-native-geolocation-service`, `react-native-background-geolocation` |
| HealthKit | Config-Plugin + `react-native-health` / `@kingstinct/react-native-healthkit` | `react-native-health` |
| Sign in with Apple inkl. Revoke-Daten | `expo-apple-authentication` | `@invertase/react-native-apple-authentication` |
| Kontolöschung (Auth-Provider) | `@react-native-firebase/auth` (`currentUser.delete()`), `@supabase/supabase-js` (RPC/Edge Function) | identisch, plus eigener Backend-Endpoint |
| Bewertungsanfrage | `expo-store-review` | `react-native-in-app-review`, `react-native-store-review` |
| Nachrichten an Kontakte (nutzergesteuert) | `expo-sms`, `expo-mail-composer`, `Share` | `react-native-share` |
| Sichere Speicherung (nicht für Health-Daten) | `expo-secure-store` | `react-native-keychain` |
| Clipboard nur auf Nutzeraktion | `expo-clipboard` | `@react-native-clipboard/clipboard` |
| Lokale Authentifizierung (Face ID) | `expo-local-authentication` | `react-native-biometrics` |
| VPN (NetworkExtension) | nicht in Managed; Development Build mit nativem Modul | natives Packet-Tunnel-Target, `react-native-vpn-ipsec` (nur IKEv2/IPSec) |
| Managed App Configuration (MDM) | Community `expo-managed-app-config` | `react-native-mdm` |
| Screen Time API (Kinderschutz) | natives Modul in Development Build | natives Modul (FamilyControls) |
| Jailbreak-/Emulator-Erkennung (Geofencing-Schutz) | `expo-device` (`isDevice`), Community `jail-monkey` | `jail-monkey`, `react-native-device-info` |
| Werbung mit Kinder-Flag | `react-native-google-mobile-ads` (Plugin-Option `tagForChildDirectedTreatment`) | identisch |

---

## Kurz-Prüfliste für diesen Abschnitt

### 5.1.1 Datenerhebung und -speicherung
- [ ] (i) Datenschutz-URL in App Store Connect UND dauerhaft in der App; alle Dritt-SDKs genannt.
- [ ] (ii) Consent mit gleichwertigem Ablehnen-Pfad, Toggles standardmäßig aus, Widerruf möglich, kein Datenversand vor Zustimmung.
- [ ] (iii) Nur benötigte Berechtigungen; Anfrage im Funktionskontext; Kernfunktion ohne optionale Berechtigungen nutzbar; Picker statt Vollzugriff.
- [ ] (iv) Alle Purpose Strings konkret, wahr, lokalisiert; keine Plugin-Standardtexte; Status vor erneuter Anfrage geprüft.
- [ ] (v) Kontolöschung in der App vorhanden, echt (Backend + Provider), Sign-in-with-Apple-Revoke; Gastmodus wenn kein Konto nötig.
- [ ] (vi) Kein heimliches Auslesen von Zwischenablage, Passwörtern, Fremd-Logins außerhalb OAuth.
- [ ] (vii) SafariViewController/WebViews nur sichtbar; keine Tracking-Instanzen.
- [ ] (viii) Keine Profildatenbanken aus Kontakten/Fotos/Kalender/HomeKit; Abgleich per Hash.
- [ ] (ix) Regulierte Apps vom betreibenden Unternehmen eingereicht; Nachweise bereit.
- [ ] (x) Kontaktdaten optional, Onboarding überspringbar.
- [ ] Privacy Manifest vorhanden, Required-Reason-APIs deklariert, Tracking-Domains vollständig, keine Fingerprints.

### 5.1.2 Datennutzung und -weitergabe
- [ ] (i) Tracking-SDKs identifiziert; ATT-Dialog vor SDK-Start; bei Ablehnung kein IDFA, keine Ersatz-IDs; kein Anreiz; Nutrition Label passt.
- [ ] (ii) Keine Rohdaten aus Berechtigungen in Analytics; Marketing-Einwilligung getrennt.
- [ ] (iii) Keine heimlichen Profile, kein Fingerprinting.
- [ ] (iv) Keine Kontakt-/Foto-Datenbanken.
- [ ] (v) Nachrichten an Kontakte nur einzeln und nutzergesteuert.
- [ ] (vi) Health-/HomeKit-/Motion-/Gesichtsdaten nicht in Werbung/Analytics.
- [ ] (vii) Apple-Pay-Kontaktdaten nur zur Abwicklung; minimale Felder.

### 5.1.3 Gesundheit und Forschung
- [ ] (i) Health-Daten nicht an Werbung/Marketing, nicht in iCloud.
- [ ] (ii) Keine falschen HealthKit-Werte; keine Health-Daten in UserDefaults/AsyncStorage/Keychain.
- [ ] (iii) Informed Consent mit Pflichtinhalten vor Datenerhebung; Ausstieg möglich; Elternzustimmung.
- [ ] (iv) Ethikvotum vorhanden und in Review-Notizen referenziert.

### 5.1.4 Kinder
- [ ] Keine Tracking-/Werbe-/Analytics-SDKs mit personenbezogener Erhebung.
- [ ] Altersabfrage nur zur Anpassung; Parental Gate vor Links/Käufen; kein Sign-in-Zwang.

### 5.1.5 Standort
- [ ] Standort nur für erkennbare Funktion; WhenInUse bevorzugt; Hintergrund begründet.
- [ ] Reduzierte Genauigkeit wo möglich; kein Standort in Analytics/Werbung; Notfall-Disclaimer; kein IP-Ersatz.

### 5.2 Geistiges Eigentum
- [ ] 5.2.1 Assets, Schriften, Code lizenziert; Open-Source-Lizenzen genannt.
- [ ] 5.2.2 Keine Fremd-Domains ohne API/Erlaubnis; kein Scraping; keine Paywall-/Werbe-Entfernung.
- [ ] 5.2.3 Kein Download/Extraktion von Fremdplattform-Medien (auch nicht per Backend).
- [ ] 5.2.4 App-Name/Icon ohne Apple-Marken; kein Endorsement-Anspruch; korrekte Schreibweisen.
- [ ] 5.2.5 Keine nachgebauten Systemdialoge, Apple-Apps, Stores, Support.

### 5.3 Glücksspiel, Lotterien, Gewinnspiele
- [ ] 5.3.1 Gewinnspiel-Veranstalter ist der Entwickler.
- [ ] 5.3.2 Regeln in der App; Apple-Disclaimer vorhanden.
- [ ] 5.3.3 Kein IAP für Echtgeld-Einsätze/Lose/Transfers; Spielgeld ohne Auszahlung über IAP.
- [ ] 5.3.4 Lizenzen je Region; Geofencing per echtem Standort mit Spoofing-Schutz; Altersverifikation; App kostenlos; keine Kartenzähler.

### 5.4 VPN
- [ ] `NEVPNManager`/Packet Tunnel mit Entitlements; keine Profil-Installation.
- [ ] Datenerhebung exakt offengelegt; keine Weitergabe; keine Tracking-SDKs.
- [ ] Lizenznachweis für lizenzpflichtige Länder; Filter-Apps legen Filterung offen.

### 5.5 MDM
- [ ] Nur Unternehmen/Bildung/Behörde/Kinderschutz; Daten nur für Verwaltungszweck; keine Werbung/Weitergabe.
- [ ] Kindersicherung über Screen Time API; keine Verleitung zu Profilen/Supervision.

### 5.6 Verhaltenskodex
- [ ] 5.6.1 Nur System-Bewertungs-API; keine Custom-Dialoge, keine Filterung, keine Anreize.
- [ ] 5.6.2 Echte Entwickleridentität; Impressum/Kontakt konsistent; Trader-Status.
- [ ] 5.6.3 Kein Keyword-Stuffing; keine Installations-/Bewertungsanreize; keine Nachahmung.
- [ ] 5.6.4 Crash-Reporting aktiv; keine Force-Unwraps/`try!` in kritischen Pfaden; Support erreichbar.
- [ ] 5.6.5 Kein Review-Modus; Demo-Account identisch zur Produktion; OTA-Kanäle konsistent; Review-Notizen wahrheitsgemäß.
