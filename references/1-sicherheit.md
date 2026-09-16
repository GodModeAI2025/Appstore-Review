# Abschnitt 1 – Sicherheit (Safety)

Stand: Apple App Review Guidelines, Fassung vom 8. Juni 2026 (geprüft September 2026).
Zurück zur Übersicht: ../SKILL.md

Abschnitt 1 bündelt alles, was Apple unter „Nutzer vor Schaden bewahren" fasst: anstößige Inhalte, Nutzer-Communities ohne Moderation, Kinder-Apps, Gesundheitsversprechen, Sicherheit der gespeicherten Daten. Viele Regeln dieses Abschnitts gelten laut Apple ausdrücklich auch für die Notarisierung von iOS-/iPadOS-Apps, die über alternative Vertriebswege ausgeliefert werden (markiert mit „auch Notarisierung"). Das heißt: Selbst wer den App Store umgeht, kommt an diesen Punkten nicht vorbei.

## Wo Apple aktuell besonders genau hinschaut

1. **UGC ohne Melde- und Blockierfunktion (1.2)** – jede App mit Chat, Kommentaren, Profilen oder Uploads ohne sichtbare „Melden"/„Blockieren"-Aktion wird nahezu sicher abgelehnt.
2. **Kids-Kategorie mit Werbe-/Analytics-SDKs (1.3)** – Standard-SDKs von Firebase, Facebook, AppLovin und Co. im Bundle einer Kids-App führen zur Ablehnung, auch wenn sie „nicht aktiv" sind.
3. **Gesundheitsversprechen über Sensoren (1.4.1)** – Blutdruck, Blutzucker, Sauerstoffsättigung oder Temperatur „nur mit Kamera/Taschenlampe" gemessen: Ablehnung ohne Nachweis.
4. **Scherz- und Täuschungsfunktionen (1.1.6)** – Fake-Anrufe, Fake-Virenwarnungen, gefälschte Systemdialoge und KI-generierte Inhalte, die als echt ausgegeben werden.
5. **Creator-Plattformen ohne Altersschranke (1.2.1(a))** – Video-, Audio- und Artikel-Plattformen mit Erwachseneninhalten müssen Altersabfrage und -sperren nachweisen.
6. **Klartext-Secrets im Bundle (1.6)** – API-Keys in Info.plist, `.env`-Dateien im Expo-Bundle, Tokens in `UserDefaults`/`AsyncStorage`.

## Inhalt

- [1.1 Anstößige Inhalte](#11-anstößige-inhalte)
  - [1.1.1 Diffamierende und diskriminierende Inhalte](#111-diffamierende-und-diskriminierende-inhalte)
  - [1.1.2 Realistische Gewaltdarstellung](#112-realistische-gewaltdarstellung)
  - [1.1.3 Waffen und gefährliche Gegenstände](#113-waffen-und-gefährliche-gegenstände)
  - [1.1.4 Sexuelle und pornografische Inhalte](#114-sexuelle-und-pornografische-inhalte)
  - [1.1.5 Aufhetzende religiöse Kommentare](#115-aufhetzende-religiöse-kommentare)
  - [1.1.6 Falschinformationen und Scherz-Funktionen](#116-falschinformationen-und-scherz-funktionen)
  - [1.1.7 Ausnutzung aktueller Ereignisse](#117-ausnutzung-aktueller-ereignisse)
- [1.2 Nutzergenerierte Inhalte](#12-nutzergenerierte-inhalte)
  - [1.2.1 Creator-Content](#121-creator-content)
  - [1.2.1(a) Altersfreigabe und Zugangsbeschränkung](#121a-altersfreigabe-und-zugangsbeschränkung)
- [1.3 Kids-Kategorie](#13-kids-kategorie)
- [1.4 Körperliche Schäden](#14-körperliche-schäden)
  - [1.4.1 Medizin-Apps](#141-medizin-apps)
  - [1.4.2 Dosierungsrechner](#142-dosierungsrechner)
  - [1.4.3 Substanzkonsum](#143-substanzkonsum)
  - [1.4.4 DUI-Checkpoints und Fahrsicherheit](#144-dui-checkpoints-und-fahrsicherheit)
  - [1.4.5 Mutproben und gefährliche Aktivitäten](#145-mutproben-und-gefährliche-aktivitäten)
- [1.5 Entwicklerinformationen und Support-Kontakt](#15-entwicklerinformationen-und-support-kontakt)
- [1.6 Datensicherheit](#16-datensicherheit)
- [1.7 Meldung krimineller Aktivitäten](#17-meldung-krimineller-aktivitäten)
- [Paketreferenz React Native / Expo](#paketreferenz-react-native--expo)
- [Kurz-Prüfliste für diesen Abschnitt](#kurz-prüfliste-für-diesen-abschnitt)

---

## 1.1 Anstößige Inhalte

**Kern der Regel** – Apple lehnt Inhalte ab, die beleidigen, verstören oder gezielt schockieren sollen. Das betrifft eigene Inhalte der App genauso wie Inhalte, die die App aus dem Netz nachlädt oder per Generator erzeugt. Die sieben Unterpunkte konkretisieren, was Apple darunter versteht.

**Risikostufe** – Hoch. Die Regel ist Ermessenssache des Reviewers; „für Erwachsene" oder „nur Satire" hilft nur in eng umrissenen Fällen.

**Woran du es im Code erkennst**
- Statische Assets: `Assets.xcassets`, `assets/`, `res/` nach Bild- und Videodateien mit auffälligen Namen durchsuchen (`gore`, `nsfw`, `nude`, `weapon`, `blood`).
- Text-Ressourcen: `Localizable.strings`, `*.json`-Lokalisierungen, `i18n/`-Ordner auf Slurs, Hetze, drastische Formulierungen.
- Generatoren: Aufrufe von Bild-/Text-KI-APIs (`openai`, `stability`, `replicate`, `gemini`) ohne erkennbaren Content-Filter.
- Remote-Inhalte: Feeds und CMS-Endpunkte, deren Inhalte die App unmoderiert anzeigt (siehe 1.2).

### 1.1.1 Diffamierende und diskriminierende Inhalte

**Kern der Regel** – Inhalte, die Personen oder Gruppen wegen Religion, Herkunft, Geschlecht, sexueller Orientierung, Alter oder ähnlicher Merkmale herabsetzen, sind tabu. Auch Inhalte, die einzelne reale Personen bloßstellen oder verleumden, fallen darunter. Eine Ausnahme macht Apple nur für professionelle politische Satire und Humor.

**Risikostufe** – Kritisch. Verstöße führen zur Ablehnung und bei Wiederholung zum Entwicklerkonto-Ausschluss.

**Woran du es im Code erkennst**
- Swift/Objective-C: Wortlisten oder Kategorien in `Localizable.strings`, `.strings`-Dictionaries, enum-Werte wie `case slur`, `case stereotype`; Gruppen-Filter in Dating-/Community-Apps (`excludeEthnicity`, `filterByReligion`).
- React Native/Expo: `i18n/*.json`, `locales/`, Konfigurationsobjekte für Quiz-, Meme- oder Roast-Generatoren; Prompt-Templates mit Personenbezug (`roastPrompt`, `insultGenerator`).
- Beide: KI-Prompts, die Nutzer frei formulieren dürfen, ohne dass Ausgaben gefiltert werden.

**Typische Verstöße**
- ❌ „Roast-Generator", der auf Basis von Herkunft oder Aussehen beleidigende Texte generiert.
- ❌ Meme-App mit vorgefertigten Vorlagen, die Minderheiten verhöhnen.
- ❌ Dating-App mit Ausschlussfilter nach Ethnie oder Religion.
- ✅ Satire-App eines bekannten Kabarett-Formats mit klarem redaktionellem Rahmen und Impressum.

**Prüfliste**
- [ ] Keine Wortlisten, Vorlagen oder Assets mit herabsetzenden Inhalten im Bundle.
- [ ] KI-Generatoren filtern Ausgaben (Moderation-Endpoint oder eigener Klassifikator).
- [ ] Keine Filter-/Matching-Logik, die Personengruppen wegen geschützter Merkmale ausschließt.

**Empfohlene Behebung** – Moderation-API des KI-Anbieters vorschalten; eigene Blockliste (z. B. `profanity-filter`-Pakete oder serverseitiger Klassifikator); Satire-Charakter in App-Beschreibung und Review-Notes belegen.

### 1.1.2 Realistische Gewaltdarstellung

**Kern der Regel** – Realistische Darstellungen von Tötung, Folter oder Missbrauch an Menschen oder Tieren, sowie Inhalte, die zu Gewalt aufrufen, sind nicht erlaubt. In Spielen dürfen „Gegner" nicht eine reale Ethnie, Kultur, Regierung, Firma oder andere real existierende Gruppe repräsentieren. Comic- oder Fantasy-Gewalt ist zulässig, muss aber korrekt in der Altersfreigabe angegeben sein.

**Risikostufe** – Hoch. Für Spiele meist ein Altersfreigabe-Thema; bei realen Bildern oder realen Feindbildern eine harte Ablehnung.

**Woran du es im Code erkennst**
- Swift/Objective-C: Spiel-Assets mit realen Flaggen, Uniformen, Firmenlogos als Gegner-Sprites; Konfigurationsdateien (`enemies.plist`, `.json`) mit realen Länder- oder Organisationsnamen.
- React Native/Expo: `assets/enemies/`, Sprite-Sheets, Level-Definitionen in JSON; `react-native-video`-Quellen mit Nachrichten- oder Kriegsmaterial.
- Beide: `ITSAppUsesNonExemptEncryption` ist hier irrelevant, aber die Altersfreigabe in App Store Connect muss zur Gewaltstufe passen (siehe Prüfliste).

**Typische Verstöße**
- ❌ Shooter, dessen Gegnerfraktion eine reale Nation oder Religionsgemeinschaft ist.
- ❌ „Gore-Sammlung" oder echte Unfallvideos als Unterhaltung.
- ✅ Fantasy-Spiel mit fiktiven Fraktionen, Altersfreigabe „12+" korrekt gesetzt.

**Prüfliste**
- [ ] Gegner in Spielen sind fiktiv oder abstrakt, keine realen Gruppen.
- [ ] Keine realen Gewaltaufnahmen im Bundle oder als Standardfeed.
- [ ] Gewaltstufe stimmt mit der Altersfreigabe in App Store Connect überein.

**Empfohlene Behebung** – Reale Referenzen aus Assets entfernen; Altersfreigabe-Fragebogen korrigieren; für Nachrichten-Apps Warnhinweise und Nutzeropt-in vor drastischen Inhalten.

### 1.1.3 Waffen und gefährliche Gegenstände

**Kern der Regel** – Apps dürfen den illegalen oder leichtsinnigen Umgang mit Waffen nicht fördern und den Kauf von Schusswaffen oder Munition nicht vermitteln. Bauanleitungen für Waffen, Sprengsätze oder andere gefährliche Gegenstände sind ebenfalls ausgeschlossen. Informations- und Trainings-Apps (Jagd, Sportschießen, Sicherheit) sind möglich, solange sie keine Beschaffung anstoßen.

**Risikostufe** – Kritisch. Vermittlung von Waffenkäufen ist eine sofortige Ablehnung.

**Woran du es im Code erkennst**
- Swift/Objective-C: `SKProduct`-Identifier oder Warenkorb-Modelle mit Waffen-/Munitionsartikeln; Deep-Links zu Händlern (`gunbroker`, `ammo`); Anleitungen als HTML im Bundle; 3D-Druck-Dateien (`.stl`) mit Waffenteilen.
- React Native/Expo: `products.json`, `catalog.ts` mit Kategorien wie `firearms`, `ammunition`; `Linking.openURL` zu Waffenhändlern; Marktplatz-Komponenten mit Waffenkategorie.
- Beide: `WKWebView`/`react-native-webview` auf Waffen-Shops.

**Typische Verstöße**
- ❌ Marktplatz-App mit Kategorie „Schusswaffen & Munition" und Checkout.
- ❌ „Survival-Guide" mit Anleitungen zum Bau improvisierter Waffen.
- ✅ Jagd-App mit Schonzeiten, Reviergrenzen und Wetterinfos ohne Kaufvermittlung.

**Prüfliste**
- [ ] Keine Kauf-, Bestell- oder Vermittlungsfunktion für Waffen und Munition.
- [ ] Keine Anleitungen zur Herstellung von Waffen oder Sprengmitteln.

**Empfohlene Behebung** – Waffenkategorien serverseitig und im Client ausblenden; Händler-Links entfernen; Inhalt auf Information/Training reduzieren.

### 1.1.4 Sexuelle und pornografische Inhalte

**Kern der Regel** – Explizite Darstellungen, die primär erotisch stimulieren sollen, sind im App Store nicht erlaubt. Das umfasst Pornografie, „Hookup"-Apps, die auf Pornografie oder Prostitution hinauslaufen, und alles, was Menschenhandel begünstigt. Apps, die Nacktheit im medizinischen, künstlerischen oder Aufklärungskontext zeigen, müssen das klar rahmen und entsprechend altersfreigeben.

**Risikostufe** – Kritisch. Ablehnung, bei Prostitution/Menschenhandel Kontoausschluss.

**Woran du es im Code erkennst**
- Swift/Objective-C: Bild-/Video-Assets, Feed-Endpunkte (`/adult`, `/nsfw`), Freemium-Flags wie `unlockUncensored`; `NSPhotoLibraryUsageDescription` in Kombination mit Upload-Funktion ohne Moderation (siehe 1.2).
- React Native/Expo: KI-Bildgeneratoren mit Prompts wie `nude`, `nsfw`, `uncensored`; Feature-Flags `isAdultContentEnabled`; Paywalls, die „unzensierte" Inhalte freischalten.
- Beide: Dating-Apps mit Preis-pro-Treffen-Logik oder Escort-Kategorien; Location-basierte Anbieterlisten für „Dienste".

**Typische Verstöße**
- ❌ KI-Bildgenerator ohne NSFW-Filter, der explizite Bilder erzeugt.
- ❌ „Dating"-App, deren Profile Preisangaben pro Stunde enthalten.
- ❌ In-App-Kauf „Unzensierter Modus".
- ✅ Aufklärungs-App mit anatomischen Illustrationen, Altersfreigabe „17+", Bildungszweck in Beschreibung.

**Prüfliste**
- [ ] KI-Generatoren blockieren sexuelle Prompts und filtern Ausgaben.
- [ ] Keine Freischaltung sexueller Inhalte per In-App-Kauf.
- [ ] Dating-/Community-Funktionen erfüllen 1.2 (Melden, Blockieren) und 1.2.1(a).
- [ ] Nacktheit in Medizin/Kunst/Bildung klar kontextualisiert und altersfreigegeben.

**Empfohlene Behebung** – Safety-Klassifikator des KI-Anbieters aktivieren; NSFW-Erkennung serverseitig (z. B. Vision-Framework `VNClassifyImageRequest` als Vorprüfung, serverseitig ein dedizierter Klassifikator); explizite Kategorien komplett entfernen.

### 1.1.5 Aufhetzende religiöse Kommentare

**Kern der Regel** – Religiöse Themen sind erlaubt, aber aufhetzende Kommentare zu Religionen und Glaubensgemeinschaften nicht. Ebenso lehnt Apple falsche oder irreführende Zitate religiöser Schriften ab. Gebets-, Kalender- und Studien-Apps sind unproblematisch, solange sie nicht gegen andere Gruppen hetzen.

**Risikostufe** – Mittel. Selten, aber bei Hetze eine harte Ablehnung.

**Woran du es im Code erkennst**
- Swift/Objective-C: Textdatenbanken (`.sqlite`, `.plist`, `.json`) mit Zitaten ohne Quellenangabe; Push-Kampagnen mit Konfrontationsinhalt (`UNNotificationRequest`-Templates).
- React Native/Expo: `quotes.json`, `verses.ts`; KI-Prompts, die religiöse Texte „umschreiben" oder „bewerten".
- Beide: Community-Funktionen ohne Moderation (siehe 1.2).

**Typische Verstöße**
- ❌ „Zitate des Tages", die Aussagen erfinden und einer heiligen Schrift zuschreiben.
- ✅ Bibel-/Koran-/Tora-App mit ausgewiesener Übersetzung und Versreferenzen.

**Prüfliste**
- [ ] Zitate religiöser Schriften haben Quellen- und Versangabe.
- [ ] Keine hetzenden Texte, Push-Templates oder Prompts gegen Glaubensgemeinschaften.

**Empfohlene Behebung** – Zitate aus lizenzierten Übersetzungen mit Referenzen; KI-Ausgaben zu religiösen Themen moderieren oder deaktivieren.

### 1.1.6 Falschinformationen und Scherz-Funktionen

**Kern der Regel** – Apps, die falsche Gerätedaten anzeigen, Funktionen vortäuschen oder Nutzer täuschen, werden abgelehnt. Ein Hinweis „nur zur Unterhaltung" ändert daran nichts. Explizit genannt: gefälschte Ortungs- oder Überwachungs-Tools, Fake-Virenscanner, Apps für anonyme oder Scherzanrufe und -SMS. Dazu zählen auch gefälschte Systemdialoge sowie KI-generierte Bilder, Stimmen oder Texte, die als authentisch ausgegeben werden, um Personen zu täuschen. Gilt auch für die Notarisierung.

**Risikostufe** – Kritisch. Apple reagiert hart, weil hier direkter Nutzerschaden (Betrug, Belästigung) entsteht.

**Woran du es im Code erkennst**
- Swift/Objective-C:
  - Fake-Anruf-UI: Views, die `CallKit`-Optik nachbauen (`FakeCallViewController`, `IncomingCallView`), `AVAudioPlayer` mit Klingelton + Timer.
  - Fake-Scanner: Strings wie `"Viren gefunden"`, `"Ihr Gerät ist infiziert"`, Fortschrittsbalken ohne echte Prüfung, Sicherheits-Claims ohne Datenbasis.
  - Fake-Systemdialoge: `UIAlertController` mit Titeln, die iOS-Meldungen imitieren („Apple ID gesperrt"), oder komplette Nachbauten von Einstellungen.
  - Anonyme SMS: HTTP-Aufrufe an SMS-Gateways mit frei wählbarer Absendernummer (`from`, `sender_id`).
  - Gefälschte Daten: „Lügendetektor", „Fingerabdruck-Scanner", „Metalldetektor" ohne Sensorbasis.
- React Native/Expo:
  - `expo-notifications`/`react-native-push-notification` zum Auslösen eines vorgetäuschten Anrufs (`scheduleNotificationAsync` mit `categoryIdentifier: 'incomingCall'`).
  - `react-native-callkeep` mit `displayIncomingCall` ohne echte Sitzung.
  - Komponenten `FakeCallScreen.tsx`, `PrankSMS.js`, `VirusScanResult.tsx`.
  - `expo-location` in Apps, die vorgeben, andere Personen zu orten, ohne deren Zustimmung.
- Beide (KI-Täuschung): Deepfake-Generatoren (Voice-Cloning ohne Wasserzeichen/Hinweis), „Foto-Beweis"-Generatoren, Gesichtstausch mit Prominenten, Text-Generatoren, die gefälschte Screenshots von Chats oder Nachrichten erzeugen.

**Typische Verstöße**
- ❌ App „Fake Call" mit Nachbau des iOS-Anrufbildschirms als Ausrede aus Meetings.
  ```swift
  // ❌ imitiert Systemoberfläche und täuscht Dritte
  class FakeIncomingCallVC: UIViewController {
      func startPrank() { ringtone.play(); showCallKitLookalike() }
  }
  ```
- ❌ „Sicherheits-Scanner", der zufällig Bedrohungen meldet und ein Abo verkauft.
  ```tsx
  // ❌ keine echte Prüfung, nur Angstmache
  const threats = Math.floor(Math.random() * 5) + 1;
  setResult(`${threats} Bedrohungen gefunden – jetzt schützen`);
  ```
- ❌ Chat-Screenshot-Generator, der WhatsApp/iMessage-Verläufe mit realen Namen fälscht.
- ✅ Alarm-App mit eindeutig eigener Optik, die als „Erinnerung" erscheint und keinen Anruf vortäuscht.
- ✅ KI-Avatar-Generator, der Ausgaben sichtbar als „KI-generiert" kennzeichnet (z. B. C2PA-Metadaten) und nur eigene Fotos akzeptiert.

**Prüfliste**
- [ ] Keine Nachbauten von System-UI (Anruf, Sperrbildschirm, Einstellungen, Systemdialoge).
- [ ] Keine „Scanner", „Detektoren" oder Messfunktionen ohne echte technische Grundlage.
- [ ] Kein Versand von Anrufen/SMS mit gefälschter oder anonymer Absenderkennung.
- [ ] KI-generierte Medien werden gekennzeichnet; keine Deepfakes realer Personen ohne Einwilligung.
- [ ] Kein „nur zur Unterhaltung"-Disclaimer als Ersatz für echte Funktion.

**Empfohlene Behebung** – Funktion streichen oder ehrlich benennen; für echte VoIP `CallKit` mit realer Sitzung; Kennzeichnung generierter Medien (Wasserzeichen, Metadaten, sichtbares Label); Einwilligungsflow für Stimm- oder Gesichtsklone.

### 1.1.7 Ausnutzung aktueller Ereignisse

**Kern der Regel** – Apps dürfen aus aktuellen oder kürzlichen traumatischen Ereignissen keinen Profit schlagen: bewaffnete Konflikte, Terroranschläge, Epidemien, Naturkatastrophen. Informations-, Hilfs- und Spenden-Apps sind erlaubt, wenn sie seriös sind und Spenden regelkonform abwickeln (siehe Abschnitt 3.2.1).

**Risikostufe** – Hoch. Wird bei akuten Ereignissen kurzfristig sehr streng geprüft.

**Woran du es im Code erkennst**
- Swift/Objective-C: Spielmechaniken oder In-App-Käufe mit Bezug auf reale Katastrophen (`SKProduct` „Pandemie-Pack"); Push-Templates mit Ereignisbezug und Kaufaufforderung.
- React Native/Expo: Level-/Content-JSON mit realen Ereignisnamen; Paywall-Komponenten mit Katastrophen-Framing (`urgencyBanner`, `crisisOffer`).
- Beide: Spenden-Flows über In-App-Kauf statt Apple Pay/Web (Abschnitt 3).

**Typische Verstöße**
- ❌ Spiel, das einen laufenden Krieg als Kulisse mit kostenpflichtigen Fraktionen nutzt.
- ✅ Spenden-App einer anerkannten Hilfsorganisation mit Apple Pay und Impressum.

**Prüfliste**
- [ ] Kein monetarisierter Bezug auf reale Katastrophen oder Konflikte.
- [ ] Spenden laufen über zulässige Wege (Apple Pay, Web, anerkannte Organisation).

**Empfohlene Behebung** – Ereignisbezug entfernen oder auf reine Information ohne Bezahlschranke reduzieren.

---

## 1.2 Nutzergenerierte Inhalte

**Kern der Regel** – Sobald Nutzer Inhalte erzeugen und andere sie sehen (Chat, Kommentare, Profile, Bilder, Bewertungen, Livestreams), muss die App vier Dinge bieten: einen Filter für anstößiges Material, eine Meldefunktion mit zeitnaher Reaktion, eine Blockierfunktion für missbräuchliche Nutzer und veröffentlichte Kontaktdaten des Betreibers. Apps, die überwiegend für Pornografie, anonyme Zufallschats, Drohungen oder Mobbing genutzt werden, entfernt Apple ohne Vorwarnung. Der Entwickler trägt die Verantwortung: Er muss verletzende Inhalte tatsächlich entfernen und bei Beanstandungen einen Plan vorlegen, wie er die Moderation verbessert; bei groben oder wiederholten Verstößen folgt der Ausschluss aus dem Entwicklerprogramm.

**Risikostufe** – Kritisch. Fehlende Melde- oder Blockier-UI ist einer der häufigsten Ablehnungsgründe überhaupt.

**Woran du es im Code erkennst**

Swift/Objective-C:
- UGC-Indikatoren: `UITextView`/`TextField` mit Sende-Aktion, `PHPickerViewController`/`UIImagePickerController` mit Upload, Firebase Firestore/Realtime Database mit Kollektionen wie `messages`, `posts`, `comments`, `profiles`; `MessageKit`, `StreamChat`, `SendBird`, `TwilioConversations`, `Agora`/`LiveKit` für Live-Video.
- Melde-UI: Suche nach `report`, `flag`, `melden` in `UIMenu`, `UIContextMenuConfiguration`, `UIAlertController`-Actions, SwiftUI `.contextMenu`, `.swipeActions`. Fehlt sie neben Nachrichten-, Kommentar- und Profil-Views, ist das ein Verstoß.
- Blockier-UI: `block`, `mute`, `blockUser`, `blockedUsers` im Datenmodell und in der UI.
- Filter: Profanity-Listen, `NLTagger`/`NaturalLanguage`-Einsatz, serverseitige Moderations-Endpunkte, Vision `VNClassifyImageRequest` vor Upload.
- Kontakt: Support-Link in Settings/Über-Screen (siehe 1.5).
- Zufalls-Chat: Matching-Funktionen `randomMatch`, `nextStranger`, `skipPartner` ohne Registrierung.

React Native/Expo:
- UGC-Indikatoren: `react-native-gifted-chat`, `stream-chat-react-native`, `@sendbird/uikit-react-native`, `react-native-agora`, `@livekit/react-native`, Supabase/Firebase-Tabellen `messages`, `posts`; `expo-image-picker` mit Upload.
- Melde-UI: Komponenten oder Props `onReport`, `ReportModal`, `reportMessage`, `ActionSheetIOS.showActionSheetWithOptions` mit „Melden".
- Blockier-UI: `blockUser`, `BlockedUsersScreen`, Store-Slices `blocked`.
- Filter: `bad-words`, `leo-profanity`, `obscenity`-Pakete oder Moderations-API-Aufrufe vor dem Persistieren.
- EULA-Zustimmung: Screens `TermsScreen`, `AcceptEula` beim ersten Start (Apple erwartet, dass Nutzer einer Null-Toleranz-Regel zustimmen).

**Typische Verstöße**
- ❌ Chat-Komponente ohne Kontextmenü:
  ```tsx
  // ❌ Nachricht ohne Melden/Blockieren
  <GiftedChat messages={messages} onSend={send} user={me} />
  ```
  ```tsx
  // ✅ Long-Press öffnet Aktionen
  <GiftedChat messages={messages} onSend={send} user={me}
    onLongPress={(ctx, msg) => showActions(['Melden', 'Nutzer blockieren'], msg)} />
  ```
- ❌ SwiftUI-Kommentarliste, die nur „Antworten" anbietet:
  ```swift
  // ❌
  CommentRow(comment).contextMenu { Button("Antworten") { reply(comment) } }
  // ✅
  CommentRow(comment).contextMenu {
      Button("Antworten") { reply(comment) }
      Button("Melden", role: .destructive) { report(comment) }
      Button("Nutzer blockieren", role: .destructive) { block(comment.author) }
  }
  ```
- ❌ Meldung landet nur in einem Log, niemand liest sie; kein Backend-Endpunkt, keine E-Mail, keine Ticket-Erzeugung.
- ❌ Zufälliger Videochat mit Fremden (`nextStranger()`) ohne Registrierung, ohne Moderation.
- ❌ „Zufällige" NSFW-Inhalte: Feed-Algorithmus, der Inhalte anderer Nutzer ohne Freigabe- oder Alterslogik ausspielt (Apple lehnt Apps ab, in denen Nutzer unerwartet mit pornografischem Material konfrontiert werden können).

**Prüfliste**
- [ ] Jede UGC-Oberfläche (Nachricht, Kommentar, Post, Profil, Bild, Stream) hat eine erreichbare „Melden"-Aktion.
- [ ] Jede Nutzerinteraktion hat eine „Blockieren"-Aktion; blockierte Nutzer verschwinden clientseitig sofort.
- [ ] Meldungen erreichen einen Menschen oder ein System mit Reaktionszeit (Backend-Endpunkt, E-Mail, Ticket); Reaktionszeit ist in Review-Notes belegbar (Apple erwartet Bearbeitung innerhalb von 24 Stunden).
- [ ] Vor dem Veröffentlichen läuft ein Filter (Text und Bild).
- [ ] EULA/Community-Regeln mit Null-Toleranz-Klausel werden beim ersten Start akzeptiert.
- [ ] Keine anonymen Zufalls-Chats; kein Feed, der ungefilterte NSFW-Inhalte ausspielen kann.
- [ ] Bei Beanstandungen: Remediation-Plan (Moderationsprozess, Personal, Tooling) dokumentiert.

**Empfohlene Behebung** – Expo/RN: `react-native-gifted-chat` mit `onLongPress`-Aktionen, `bad-words`/`obscenity` für Textfilter, Moderations-API (OpenAI Moderation, Hive, AWS Rekognition, Google Cloud Vision SafeSearch) serverseitig; Swift: `.contextMenu`/`.swipeActions` mit Melden/Blockieren, Vision-Vorprüfung, serverseitige Moderation; Managed-Chat-SDKs (Stream, Sendbird) bringen Melden/Blockieren mit, wenn die UI-Hooks nicht deaktiviert werden.

### 1.2.1 Creator-Content

**Kern der Regel** – Plattformen, die Inhalte von Creators bündeln (Videos, Artikel, Audio, Casual Games, Kurse), gelten als UGC-Apps und müssen dieselben Moderationspflichten erfüllen wie 1.2. Zusätzlich müssen sie die Bezahlregeln aus Abschnitt 3 einhalten: digitale Creator-Inhalte werden über In-App-Kauf verkauft, physische Leistungen oder Trinkgelder folgen den dortigen Ausnahmen. Die App bleibt eine Plattform mit eigener Verantwortung; sie darf sich nicht zu einem Store für unmoderierte Mini-Apps entwickeln (siehe 4.7).

**Risikostufe** – Hoch. Kombination aus Moderation und Bezahlregeln; Verstöße gegen eines von beiden reichen.

**Woran du es im Code erkennst**
- Swift/Objective-C: Modelle `Creator`, `Channel`, `Episode`, `Course`; Mediaplayer (`AVPlayer`) mit Remote-Playlists; Abo-Logik pro Creator (`StoreKit`-Produkte `creator_sub_*`) oder externe Zahlungsseiten (`SFSafariViewController` zu Stripe/Patreon).
- React Native/Expo: `expo-av`/`expo-video`, `react-native-video` mit CMS-Feed; `react-native-purchases`/`expo-in-app-purchases` vs. `Linking.openURL` zu externen Checkouts; Mini-Game-Container (`react-native-webview` mit Creator-HTML).
- Beide: Melde-/Blockierfunktionen auf Creator-Ebene (Kanal melden, Creator ausblenden).

**Typische Verstöße**
- ❌ Podcast-Plattform ohne „Kanal melden".
- ❌ Creator-Abo nur über Stripe-Webview, kein In-App-Kauf (Abschnitt 3).
- ✅ Video-Plattform mit Melden auf Video- und Kanalebene, In-App-Abo, Altersstufen pro Inhalt.

**Prüfliste**
- [ ] Melden und Blockieren auf Inhalts- und Creator-Ebene vorhanden.
- [ ] Bezahlung digitaler Creator-Inhalte läuft über In-App-Kauf.
- [ ] Creator-Inhalte werden vor Veröffentlichung geprüft oder zumindest nachträglich moderiert.

**Empfohlene Behebung** – Moderationsprozess wie 1.2; StoreKit 2 / `react-native-purchases` für Abos; Content-Review-Queue im Backend.

### 1.2.1(a) Altersfreigabe und Zugangsbeschränkung

**Kern der Regel** – Creator-Plattformen müssen Nutzern ermöglichen, altersunangemessene Inhalte zu erkennen, und müssen den Zugang zu solchen Inhalten anhand einer verifizierten oder deklarierten Altersangabe einschränken. Das betrifft Kennzeichnung („18+", „Mature") und technische Sperren für Minderjährige. Gilt auch für die Notarisierung.

**Risikostufe** – Hoch. Seit 2025 verstärkt geprüft, weil Apple die Altersfreigaben im Store neu gestaffelt hat (4+, 9+, 13+, 16+, 18+).

**Woran du es im Code erkennst**
- Swift/Objective-C: Altersabfrage im Onboarding (`DatePicker` für Geburtsdatum, `ageGate`), Nutzung der `DeclaredAgeRange`-API (iOS 26+) zur Abfrage der von Eltern hinterlegten Altersspanne; Inhaltsmodell mit `ageRating`/`isMature`; Filterlogik, die Inhalte nach Altersgruppe ausblendet.
- React Native/Expo: `AgeGateScreen.tsx`, `birthdate` im Auth-Flow; Feld `contentRating` in Feed-Objekten; Filter im Query (`where('rating', '<=', userMaxRating)`); Native-Modul-Bridge zu `DeclaredAgeRange`.
- Beide: Kennzeichnungs-UI (Badge „18+", Blur-Overlay mit „Inhalt anzeigen").

**Typische Verstöße**
- ❌ Alterskennzeichnung existiert, wird aber nur angezeigt; jeder kann klicken.
  ```swift
  // ❌ Warnung ohne Sperre
  if video.isMature { showWarningBadge() }
  // ✅ Sperre gegen deklariertes Alter
  if video.isMature && !session.user.isAdult { showBlocked(reason: .ageRestricted) }
  ```
- ❌ Altersabfrage „Bist du über 18? [Ja]" ohne Speicherung und ohne Wirkung auf Inhalte.
- ❌ Feed-Query liefert alle Inhalte, Filterung nur clientseitig und leicht umgehbar.
- ✅ Geburtsdatum beim Registrieren, Altersstufe im Profil, serverseitig gefilterter Feed, Badge plus Blur.

**Prüfliste**
- [ ] Inhalte tragen eine Altersstufe (Datenmodell + sichtbare Kennzeichnung).
- [ ] Nutzeralter wird deklariert oder verifiziert und persistent gespeichert.
- [ ] Sperre für Minderjährige wirkt serverseitig oder mindestens zuverlässig clientseitig.

**Empfohlene Behebung** – Age-Gate im Onboarding; `DeclaredAgeRange`-API (Swift; für RN via Native-Modul) zum Abgleich mit Familienfreigabe; Inhaltsfilter im Backend; Blur-Overlay als UI-Muster.

---

## 1.3 Kids-Kategorie

**Kern der Regel** – Apps in der Kids-Kategorie richten sich ausdrücklich an Kinder und sind in drei Altersbänder eingeteilt (5 und jünger, 6–8, 9–11). Sie dürfen keine externen Links, Kaufmöglichkeiten oder andere Ablenkungen enthalten, außer hinter einer Elternschranke. Tracking, verhaltensbasierte Werbung und Weitergabe personenbezogener oder Gerätedaten an Dritte sind verboten; Analytics- oder Werbe-SDKs sind nur zulässig, wenn sie nachweislich keine identifizierenden Daten von Kindern erheben. Zusätzlich gelten weltweit die Kinderschutzgesetze (COPPA, DSGVO, u. a.). Wer die Kids-Kategorie einmal verlässt, kommt schwer zurück.

**Risikostufe** – Kritisch. Apple prüft Kids-Apps mit Binäranalyse auf eingebettete SDKs; Ablehnungen sind häufig und begründen sich oft aus Bibliotheken, die der Entwickler „nur mitgeliefert" hat.

**Woran du es im Code erkennst**

Swift/Objective-C:
- SDK-Inventar: `Podfile.lock`, `Package.resolved`, `Cartfile.resolved`, `Frameworks/`-Ordner. Verdächtig: `FirebaseAnalytics`, `FBSDKCoreKit`, `AppsFlyer`, `Adjust`, `Branch`, `Amplitude`, `Mixpanel`, `Google-Mobile-Ads-SDK`, `AppLovinSDK`, `UnityAds`, `IronSource`, `Vungle`, `Chartboost`, `Sentry` (nur mit deaktivierten PII-Optionen).
- Info.plist: `NSUserTrackingUsageDescription` darf nicht existieren (ATT in Kids-Apps ist ein Widerspruch); `SKAdNetworkItems` deutet auf Werbe-Attribution; `GADApplicationIdentifier` auf AdMob.
- Code: `ASIdentifierManager.shared().advertisingIdentifier`, `ATTrackingManager.requestTrackingAuthorization`, `UIDevice.current.identifierForVendor` als Tracking-Schlüssel an Dritte, `Analytics.logEvent` ohne kindgerechte Konfiguration.
- Elternschranke: Suche nach `ParentalGate`, `parentGate`, Rechenaufgabe/Halte-Geste vor `SFSafariViewController`, `UIApplication.shared.open`, `SKStoreProductViewController`, In-App-Kauf-Flows.
- Externe Links: `UIApplication.shared.open(`, `SFSafariViewController`, `WKWebView` mit externen URLs, Social-Share-Sheets (`UIActivityViewController`).
- Altersabfrage: `DatePicker`/`ageGate`-Screens in Kids-Apps sind selbst ein Risiko (Datenerhebung); Apple erwartet altersneutrales Design.

React Native/Expo:
- SDK-Inventar: `package.json` mit `@react-native-firebase/analytics`, `react-native-fbsdk-next`, `react-native-appsflyer`, `react-native-adjust`, `react-native-branch`, `@amplitude/analytics-react-native`, `react-native-google-mobile-ads`, `react-native-applovin-max`, `expo-tracking-transparency`, `expo-ads-admob` (veraltet), `@sentry/react-native` ohne `sendDefaultPii: false`.
- Expo-Config: `app.json`/`app.config.ts` mit `plugins: ["react-native-google-mobile-ads"]`, `ios.infoPlist.NSUserTrackingUsageDescription`, `ios.infoPlist.SKAdNetworkItems`.
- Code: `getTrackingPermissionsAsync`, `requestTrackingPermissionsAsync`, `Application.getIosIdForVendorAsync` an Analytics übergeben, `analytics().logEvent`.
- Elternschranke: Komponenten `ParentalGate`, `ParentGateModal`; `Linking.openURL`, `WebBrowser.openBrowserAsync` (expo-web-browser), `Share.share` ohne vorgeschaltete Schranke.
- Bezahlung: `react-native-purchases`, `expo-in-app-purchases` ohne Elternschranke.

**Typische Verstöße**
- ❌ Kids-Lern-App mit Firebase Analytics in Standardkonfiguration (sammelt IDFV, Geräteinfos).
  ```swift
  // ❌ Tracking-Abfrage in einer Kids-App
  ATTrackingManager.requestTrackingAuthorization { _ in }
  ```
- ❌ „Mehr Apps von uns"-Button, der ohne Schranke den App Store öffnet.
  ```tsx
  // ❌ direkter externer Link
  <Button title="Mehr Apps" onPress={() => Linking.openURL(storeUrl)} />
  // ✅ Elternschranke vor dem Link
  <Button title="Mehr Apps" onPress={() => parentalGate(() => Linking.openURL(storeUrl))} />
  ```
- ❌ Werbebanner (AdMob) ohne kindgerechte Konfiguration und ohne Kids-Zertifizierung des Netzwerks.
- ❌ Kids-App fragt Namen, Foto und Geburtsdatum des Kindes ab und schickt sie an einen eigenen Server ohne elterliche Einwilligung.
- ✅ Kids-App ohne Analytics-SDK, Elternschranke (Rechenaufgabe) vor Store-Link und Käufen, keine Kontenpflicht.

**Prüfliste**
- [ ] Kein Analytics-, Attribution- oder Werbe-SDK im Bundle, das identifizierende Daten sammelt; erlaubte Ausnahmen sind dokumentiert (kindgerechter Modus, keine Kinder-PII, Datenschutz-Nachweis).
- [ ] Kein `NSUserTrackingUsageDescription`, kein ATT-Aufruf, kein IDFA-Zugriff.
- [ ] Keine verhaltensbasierte Werbung; wenn Werbe-SDK, dann nachweislich kontextbasiert und COPPA-konform konfiguriert (z. B. `tagForChildDirectedTreatment`).
- [ ] Alle externen Links, Store-Verweise, Share-Sheets und Käufe liegen hinter einer Elternschranke.
- [ ] Keine Erhebung personenbezogener Daten des Kindes ohne verifizierbare elterliche Einwilligung.
- [ ] Altersband in App Store Connect passt zur Zielgruppe; Inhalte sind altersgerecht.

**Empfohlene Behebung** – SDKs entfernen oder durch Kids-zertifizierte Varianten ersetzen (z. B. AdMob nur mit `tagForChildDirectedTreatment` und `maxAdContentRating`, oder gar keine Werbung); eigene Elternschranke (Rechenaufgabe, Wischgeste, Halten für drei Sekunden) als wiederverwendbare Komponente; Expo: `expo-tracking-transparency` und Werbe-Plugins aus `app.json` entfernen; Bare RN: Pods bereinigen, `pod install --repo-update` nach Entfernen der Analytics-Pakete.

---

## 1.4 Körperliche Schäden

**Kern der Regel** – Apps, deren Fehlverhalten Menschen physisch schaden kann, prüft Apple besonders streng. Das betrifft Medizin- und Gesundheits-Apps, Dosierungsrechner, Apps rund um Substanzen, Fahrsicherheit und Apps, die zu riskantem Verhalten anstacheln. Alle fünf Unterpunkte gelten auch für die Notarisierung.

### 1.4.1 Medizin-Apps

**Kern der Regel** – Medizinische Apps, die falsche Daten liefern oder zur Diagnose bzw. Behandlung genutzt werden, werden besonders geprüft. Apps, die vorgeben, Röntgenbilder, Blutdruck, Körpertemperatur, Blutzucker oder Sauerstoffsättigung allein mit Gerätesensoren (Kamera, Taschenlampe, Mikrofon) zu messen, lehnt Apple ab, sofern die Genauigkeit nicht belegt ist. Medizinische Apps müssen Nutzer auf ärztliche Rücksprache hinweisen und dürfen nicht suggerieren, ärztlichen Rat zu ersetzen. Liegt eine behördliche Zulassung vor (FDA, CE/MDR o. ä.), ist der Nachweis in den Review-Notes beizulegen.

**Risikostufe** – Kritisch. Sensor-basierte Vitalwerte per Kamera sind ein Dauerbrenner unter den Ablehnungen.

**Woran du es im Code erkennst**
- Swift/Objective-C:
  - Kamera-Vitalmessung: `AVCaptureSession` mit `AVCaptureDevice.torchMode = .on` und Pixel-Analyse (PPG-Muster); Klassen `HeartRateDetector`, `BloodPressureEstimator`, `SpO2Calculator`.
  - HealthKit: `HKQuantityType(.bloodPressureSystolic)`, `.bloodGlucose`, `.oxygenSaturation`, `.bodyTemperature` als **geschriebene** Werte ohne externes Messgerät (Bluetooth/`CoreBluetooth`); `NSHealthUpdateUsageDescription`.
  - Diagnose-Claims: Strings wie „Diagnose", „erkennt Hautkrebs", „misst Blutdruck", „ersetzt den Arztbesuch"; ML-Modelle (`.mlmodel`) mit Diagnose-Labels ohne Zulassung.
  - Disclaimer: Suche nach „ärztlich", „Arzt", „medical advice", „kein Ersatz" in Onboarding/Settings.
- React Native/Expo:
  - `expo-camera`/`react-native-vision-camera` mit Frame-Processor und Torch (`torch="on"`) zur Pulsmessung; `react-native-health`/`@kingstinct/react-native-healthkit` mit `saveQuantitySample` für Blutdruck/Glukose; `expo-sensors` (Accelerometer) für „Schlafapnoe-Erkennung".
  - `app.json`: `ios.infoPlist.NSHealthShareUsageDescription`, `NSHealthUpdateUsageDescription`, `NSCameraUsageDescription` mit medizinischer Begründung.
  - Marketing-Strings in `i18n` mit Diagnose-Versprechen.
- Beide: Bluetooth-Anbindung an zugelassene Geräte (`CoreBluetooth`, `react-native-ble-plx`) ist das legitime Muster; fehlt sie bei Vitalwerten, ist das ein Warnsignal.

**Typische Verstöße**
- ❌ „Blutdruck per Fingerkamera":
  ```swift
  // ❌ PPG über Kamera → Blutdruck-Claim ohne Validierung
  device.torchMode = .on
  let systolic = estimateBP(from: redChannelSamples)
  healthStore.save(HKQuantitySample(type: .bloodPressureSystolic, ...))
  ```
- ❌ Hautscanner mit CoreML-Modell, der „Melanom-Wahrscheinlichkeit 87 %" ausgibt, ohne Zulassung und ohne Arzt-Hinweis.
- ❌ Symptom-Checker, der als Ergebnis „Sie haben Grippe" ausgibt statt „Mögliche Ursachen – bitte ärztlich abklären".
- ✅ Pulsmessung per Kamera, klar als „Schätzung, nicht medizinisch" gekennzeichnet, ohne HealthKit-Schreibzugriff auf klinische Werte, mit Arzt-Hinweis.
- ✅ Glukose-Tracker, der Werte nur von einem zugelassenen BLE-Messgerät übernimmt; CE-Zertifikat in den Review-Notes.

**Prüfliste**
- [ ] Keine Messung klinischer Werte (Blutdruck, Blutzucker, SpO2, Temperatur, Röntgen) allein über Gerätesensoren ohne belegte Genauigkeit.
- [ ] Sichtbarer Hinweis, dass die App keinen ärztlichen Rat ersetzt (Onboarding und Ergebnisansicht).
- [ ] Diagnose- oder Behandlungs-Claims nur mit Zulassung; Nachweis liegt in den Review-Notes.
- [ ] HealthKit-Schreibzugriffe auf klinische Typen nur mit externer Datenquelle.
- [ ] ML-Modelle mit medizinischen Labels sind als Unterstützung, nicht als Diagnose deklariert.

**Empfohlene Behebung** – Claims abschwächen („Wellness", „Schätzung"), Disclaimer als Pflichtscreen, `CoreBluetooth`/`react-native-ble-plx` für zugelassene Geräte, Zulassungsdokumente hochladen; bei Pulsmessung `HKQuantityType(.heartRate)` mit klarer Metadaten-Kennzeichnung der Quelle.

### 1.4.2 Dosierungsrechner

**Kern der Regel** – Rechner für Medikamentendosierungen dürfen nur von Herstellern, Krankenhäusern, Universitäten, Krankenversicherungen, Apotheken oder anderen Einrichtungen mit nachweisbarer medizinischer Kompetenz stammen und müssen von der FDA oder einer vergleichbaren Behörde freigegeben sein. Für Einzelentwickler ist diese Funktionsklasse praktisch verschlossen. Gilt auch für die Notarisierung.

**Risikostufe** – Kritisch. Apple prüft hier die Identität des Entwicklerkontos (Organisation vs. Einzelperson).

**Woran du es im Code erkennst**
- Swift/Objective-C: Funktionen `calculateDose`, `mgPerKg`, `dosage`, `insulinUnits`, `bolusCalculator`, `pediatricDose`; Datenbanken mit Wirkstoffen und Dosierungstabellen (`drugs.sqlite`, `dosing.json`).
- React Native/Expo: `DoseCalculatorScreen.tsx`, `utils/dosage.ts`, Pakete wie `medication-calc`; Formulare mit Gewicht/Alter → Milligramm-Ausgabe.
- Beide: Entwicklerkonto-Typ (Team-Name in `PRODUCT_BUNDLE_IDENTIFIER`/Signing) gegen die Anforderung „medizinische Einrichtung" abgleichen.

**Typische Verstöße**
- ❌ Indie-App „Kinderarzt-Helfer" mit Paracetamol-Dosierung nach Gewicht.
- ❌ Insulin-Bolus-Rechner in einer Diabetes-Tagebuch-App eines Einzelentwicklers.
- ✅ Dosierungs-App eines Universitätsklinikums, CE-Kennzeichnung als Medizinprodukt, Nachweis in Review-Notes.

**Prüfliste**
- [ ] Keine Dosierungsberechnung, sofern der Entwickler keine zugelassene medizinische Einrichtung ist.
- [ ] Bei berechtigten Anbietern: Zulassung (FDA/CE-MDR) und Einrichtungsnachweis in den Review-Notes.

**Empfohlene Behebung** – Funktion entfernen oder auf reine Wirkstoffinformation ohne Berechnung reduzieren; alternativ als Organisation mit Zulassung einreichen.

### 1.4.3 Substanzkonsum

**Kern der Regel** – Apps dürfen den Konsum von Tabak, Vape-Produkten, illegalen Drogen oder übermäßigen Alkoholmengen nicht fördern und diese Produkte nicht an Minderjährige vermarkten. Der Verkauf kontrollierter Substanzen über die App ist untersagt, ausgenommen lizenzierte Apotheken und – in Regionen mit legalem Rahmen – lizenzierte Cannabis-Abgabestellen. Aufklärungs-, Entwöhnungs- und Tagebuch-Apps sind erlaubt.

**Risikostufe** – Hoch. Für Cannabis-Apps ist zusätzlich die regionale Beschränkung Pflicht.

**Woran du es im Code erkennst**
- Swift/Objective-C: Shop-Modelle mit `vape`, `eLiquid`, `cannabis`, `thc`, `nicotine`; Trinkspiel-Logik (`drinkingGame`, `shotsCount`, „Wer verliert, trinkt"); Rauch-Simulatoren als Unterhaltung; Store-Links zu Vape-Shops.
- React Native/Expo: `products.json` mit Substanzkategorien; `DrinkingGameScreen.tsx`, `PartyChallenge.tsx`; Deep-Links zu Dispensaries ohne Regionsprüfung; `expo-location` zur Lieferabwicklung von Substanzen.
- Beide: Altersfreigabe der App (muss „17+" bzw. „18+" sein) und Verfügbarkeit nach Ländern in App Store Connect.

**Typische Verstöße**
- ❌ Trinkspiel-App, deren Kernmechanik das Kippen von Shots belohnt.
- ❌ Vape-Shop mit In-App-Bestellung und Lieferung.
- ❌ Cannabis-Lieferdienst ohne Lizenznachweis und ohne Beschränkung auf legale Regionen.
- ✅ Rauchstopp-App mit Tagebuch, Motivationsstatistik und Hilfsangeboten.
- ✅ Lizenzierte Apotheken-App mit Rezeptupload und Identitätsprüfung.

**Prüfliste**
- [ ] Kein Verkauf von Tabak, Vape, illegalen Drogen; kontrollierte Substanzen nur mit Lizenznachweis.
- [ ] Cannabis-Funktionen nur in Regionen mit legalem Rahmen (Geo-Beschränkung + Store-Verfügbarkeit).
- [ ] Keine Spiele oder Mechaniken, die exzessiven Alkoholkonsum fördern.

**Empfohlene Behebung** – Verkaufsfunktionen entfernen oder Lizenz dokumentieren; Regionsprüfung serverseitig und über Store-Verfügbarkeit; Alterskennzeichnung korrigieren; Trinkspiele in „alkoholfreie" Mechanik umbauen.

### 1.4.4 DUI-Checkpoints und Fahrsicherheit

**Kern der Regel** – Apps dürfen Alkoholkontrollpunkte nur anzeigen, wenn die Polizei sie selbst veröffentlicht hat. Sie dürfen nie zum Fahren unter Alkoholeinfluss oder zu anderem rücksichtslosen Verhalten im Straßenverkehr ermutigen. Navigations- und Community-Verkehrs-Apps müssen ihre Datenquellen entsprechend einschränken. Gilt auch für die Notarisierung.

**Risikostufe** – Hoch. Eng gefasst, aber eindeutig; Community-gemeldete Kontrollen führen zur Ablehnung.

**Woran du es im Code erkennst**
- Swift/Objective-C: Datenmodelle `Checkpoint`, `dui`, `policeControl`, `speedTrap` mit Nutzerquelle (`reportedBy: userId`); `MKAnnotation`-Klassen für Kontrollpunkte; Push-Kategorien „Kontrolle in der Nähe".
- React Native/Expo: `react-native-maps` mit Markern aus Community-Reports (`reports.filter(r => r.type === 'dui')`); `expo-notifications` mit Nähe-Alarmen; Feature „Kontrolle melden" im UI.
- Beide: Promille-Rechner, die als Ergebnis „Du kannst noch fahren" ausgeben; Ingame-Belohnungen für riskantes Fahren in „Real-World"-Fahr-Apps.

**Typische Verstöße**
- ❌ Community-Karte „Polizeikontrolle melden" mit Alkoholkontroll-Kategorie.
- ❌ Promille-Rechner mit Freigabe-Ausgabe:
  ```tsx
  // ❌ ermutigt zum Fahren
  <Text>{bac < 0.5 ? 'Du darfst noch fahren' : 'Lieber warten'}</Text>
  // ✅ keine Fahr-Freigabe, Hinweis auf Alternativen
  <Text>Diese Schätzung ist keine Fahrtauglichkeitsprüfung. Nutze Taxi oder ÖPNV.</Text>
  ```
- ✅ Verkehrs-App, die Kontrollpunkte ausschließlich aus offiziellen Polizei-Feeds übernimmt und die Quelle anzeigt.

**Prüfliste**
- [ ] Alkoholkontrollen stammen nur aus offiziellen Polizeiquellen; keine Nutzermeldungen dieser Kategorie.
- [ ] Keine Ausgabe, die Fahren unter Einfluss als „okay" bewertet.

**Empfohlene Behebung** – Kategorie aus Melde-UI und Datenmodell entfernen; Quellenkennzeichnung; Promille-Rechner mit Warnhinweis und Taxi-/ÖPNV-Verweis statt Freigabe.

### 1.4.5 Mutproben und gefährliche Aktivitäten

**Kern der Regel** – Apps dürfen Nutzer nicht zu Wetten, Challenges oder Aktivitäten drängen, die ihnen oder anderen körperlich schaden können. Das reicht von „Challenge"-Apps mit gefährlichen Aufgaben über Fasten- und Extremdiät-Apps ohne Sicherheitsnetz bis zu Fitness-Apps, die Verletzungsrisiken ignorieren. Gilt auch für die Notarisierung.

**Risikostufe** – Hoch. Häufig bei viralen Trend-Apps und Social-Challenge-Formaten.

**Woran du es im Code erkennst**
- Swift/Objective-C: Aufgabenlisten (`challenges.json`, `dares.plist`) mit Texten wie „48 Stunden nichts essen", „Klettere auf …", „Trinke …"; Belohnungslogik für Aufgaben ohne Sicherheitsprüfung; Fasten-Timer ohne Obergrenze oder Warnungen.
- React Native/Expo: `DareGenerator.tsx`, `ChallengeFeed`, Daten aus UGC (Nutzer stellen Aufgaben, siehe 1.2); `FastingTimer` mit Zielwerten über 24–48 h ohne Hinweis; Workout-Generatoren ohne Warm-up/Belastungs-Hinweise.
- Beide: Wett-Mechaniken auf reale körperliche Leistungen zwischen Nutzern (`bet`, `stake`, `wager`).

**Typische Verstöße**
- ❌ „Wahrheit oder Pflicht"-App mit Aufgaben, die zu Verletzungen führen können.
- ❌ Fasten-App, die 7-Tage-Wasserfasten als Standardziel anbietet, ohne Warnhinweis.
- ✅ Challenge-App mit kuratierter, harmloser Aufgabenliste und Möglichkeit, Aufgaben zu melden.
- ✅ Fasten-App mit Obergrenzen, Warnhinweisen und Ausschluss von Risikogruppen im Onboarding.

**Prüfliste**
- [ ] Keine Aufgaben, Wetten oder Ziele, die körperlichen Schaden riskieren.
- [ ] Bei Fasten/Diät/Training: Warnhinweise, Obergrenzen, Hinweis auf ärztliche Rücksprache.

**Empfohlene Behebung** – Aufgabenlisten kuratieren; Sicherheitsgrenzen in der Logik (z. B. maximale Fastendauer) und Hinweisdialoge; Wett-Mechaniken auf körperliche Leistungen entfernen.

---

## 1.5 Entwicklerinformationen und Support-Kontakt

**Kern der Regel** – Jede App muss Nutzern einen leicht auffindbaren Weg bieten, den Entwickler zu erreichen und Support zu bekommen. Das gilt besonders für Apps, die im Bildungskontext genutzt werden. Wallet-Pässe müssen gültige Kontaktinformationen des Ausstellers tragen und mit einem Zertifikat signiert sein, das zur ausstellenden Organisation gehört. Gilt auch für die Notarisierung.

**Risikostufe** – Mittel. Leicht zu beheben, aber ein fehlender Support-Link fällt beim Review sofort auf.

**Woran du es im Code erkennst**
- Swift/Objective-C: Settings-/Über-Screen mit `mailto:`, Support-URL, `MFMailComposeViewController`; Strings „Support", „Kontakt", „Hilfe". Wallet: `pass.json` mit Feldern für Organisation und Beschreibung, `passTypeIdentifier`, Signaturzertifikat; `PKPass`-Erzeugung im Backend.
- React Native/Expo: `SettingsScreen.tsx` mit `Linking.openURL('mailto:…')`, `expo-mail-composer`, Support-Link; `react-native-wallet`/`react-native-passkit-wallet`-Pässe mit vollständigen Ausstellerdaten.
- Beide: Support-URL in App Store Connect muss auf eine erreichbare Seite mit Kontaktweg zeigen (Metadaten, nicht Code, aber prüfbar über README/Config).

**Typische Verstöße**
- ❌ Keine Kontaktmöglichkeit in der App; Support-URL zeigt auf eine Landingpage ohne Formular oder E-Mail.
- ❌ Wallet-Pass mit leerem `organizationName` oder Signatur eines fremden Team-Zertifikats.
- ✅ Über-Screen mit E-Mail-Link, Support-Website, Versionsnummer und Impressum.

**Prüfliste**
- [ ] Support-Kontakt (E-Mail oder Formular) innerhalb der App erreichbar.
- [ ] Support-URL in App Store Connect funktioniert und enthält einen Kontaktweg.
- [ ] Wallet-Pässe: Ausstellerdaten vollständig, Zertifikat gehört zum Aussteller.

**Empfohlene Behebung** – Expo: `expo-mail-composer` oder `Linking.openURL('mailto:')`; Bare RN: `react-native-mail`; Swift: `MFMailComposeViewController` oder `mailto:`-URL; Über-Screen als Pflichtbestandteil.

---

## 1.6 Datensicherheit

**Kern der Regel** – Apps müssen angemessene Sicherheitsmaßnahmen umsetzen, damit erhobene Daten nicht unbefugt genutzt, offengelegt oder von Dritten abgegriffen werden. Apple formuliert das kurz, prüft aber praktisch: Klartext-Secrets im Bundle, unverschlüsselte Übertragung, Passwörter in `UserDefaults` oder schwache Zugriffsschutzmechanismen fallen darunter. Gilt auch für die Notarisierung.

**Risikostufe** – Hoch. Bei sensiblen Daten (Gesundheit, Finanzen, Kinder) kritisch; Apple nimmt Sicherheitsvorfälle als Grund für Entfernung.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Hartcodierte Secrets: Suche nach `apiKey =`, `secret`, `token`, `password`, `sk_live_`, `AIza`, `AKIA`, `-----BEGIN PRIVATE KEY-----`, Base64-Blöcke in `.swift`, `.m`, `Info.plist`, `.xcconfig`, `GoogleService-Info.plist` (dort sind Client-Keys normal, Server-Keys nicht).
- Falsche Speicherung: `UserDefaults.standard.set(token, forKey:)`, `NSUserDefaults` für Passwörter/Tokens; `FileManager` schreibt Zugangsdaten in `Documents/` ohne `FileProtectionType`.
- Keychain: `SecItemAdd`/`SecItemCopyMatching` oder Wrapper (`KeychainAccess`, `KeychainSwift`, `Valet`); Attribut `kSecAttrAccessible` sollte `WhenUnlockedThisDeviceOnly` oder `AfterFirstUnlockThisDeviceOnly` sein, nicht `Always`.
- Transport: `NSAppTransportSecurity` in Info.plist mit `NSAllowsArbitraryLoads = true`, `NSExceptionAllowsInsecureHTTPLoads`; `http://`-URLs im Code; eigene `URLSessionDelegate`-Implementierung, die `serverTrust` blind akzeptiert.
- Verschlüsselung: `CryptoKit` (gut), selbstgebaute XOR-„Verschlüsselung" oder `MD5`/`SHA1` als Passwort-Hash (schlecht); `CommonCrypto` mit ECB-Modus.
- Biometrie: `LAContext` ohne `evaluatePolicy`-Fehlerbehandlung; Fallback auf gespeicherte Passwörter in `UserDefaults`.
- Logging: `print(token)`, `NSLog(@"%@", password)`, `os_log` mit `%{public}@` für sensible Werte.
- Zwischenablage: `UIPasteboard.general.string = password` ohne Ablaufzeit.

React Native/Expo:
- Hartcodierte Secrets: `.env`-Dateien, die über `react-native-config`, `react-native-dotenv` oder `EXPO_PUBLIC_*`-Variablen ins Bundle gelangen (`EXPO_PUBLIC_` ist per Definition öffentlich!); `extra`-Block in `app.json` mit Server-Secrets; `Constants.expoConfig.extra.apiSecret`.
- Falsche Speicherung: `AsyncStorage.setItem('token', …)`, `AsyncStorage.setItem('password', …)`, `react-native-mmkv` ohne `encryptionKey` für sensible Daten.
- Sichere Speicherung: `expo-secure-store` (`SecureStore.setItemAsync` mit `keychainAccessible: SecureStore.WHEN_UNLOCKED_THIS_DEVICE_ONLY`), `react-native-keychain` (`setGenericPassword` mit `accessible: ACCESSIBLE.WHEN_UNLOCKED_THIS_DEVICE_ONLY`).
- Transport: `app.json` → `ios.infoPlist.NSAppTransportSecurity.NSAllowsArbitraryLoads: true`; `fetch('http://…')`, `axios.create({ baseURL: 'http://…' })`; `react-native-ssl-pinning` (gut) vs. WebView mit `onShouldStartLoadWithRequest`, die alles durchlässt.
- Verschlüsselung: `crypto-js` mit statischem Key im Code; `expo-crypto` nur für Hashing (gut für Integrität, nicht für Passwortspeicherung).
- Logging: `console.log(token)`, `console.log(user)` mit Passwortfeldern; Sentry/Bugsnag-Breadcrumbs mit Request-Bodys.
- Biometrie: `expo-local-authentication` ohne serverseitige Session-Bindung (Biometrie „entsperrt" nur eine im Klartext gespeicherte Anmeldung).

**Typische Verstöße**
- ❌ Server-Secret im Expo-Bundle:
  ```ts
  // ❌ landet im JS-Bundle, lesbar für jeden
  const STRIPE_SECRET = process.env.EXPO_PUBLIC_STRIPE_SECRET_KEY;
  // ✅ nur Publishable Key im Client, Secret bleibt im Backend
  const STRIPE_PUBLISHABLE = process.env.EXPO_PUBLIC_STRIPE_PUBLISHABLE_KEY;
  ```
- ❌ Token in AsyncStorage:
  ```ts
  // ❌
  await AsyncStorage.setItem('authToken', token);
  // ✅
  await SecureStore.setItemAsync('authToken', token,
    { keychainAccessible: SecureStore.WHEN_UNLOCKED_THIS_DEVICE_ONLY });
  ```
- ❌ Passwort in UserDefaults:
  ```swift
  // ❌
  UserDefaults.standard.set(password, forKey: "pw")
  // ✅
  try keychain.set(password, key: "pw", accessibility: .whenUnlockedThisDeviceOnly)
  ```
- ❌ ATS global deaktiviert:
  ```xml
  <!-- ❌ -->
  <key>NSAppTransportSecurity</key>
  <dict><key>NSAllowsArbitraryLoads</key><true/></dict>
  ```
- ❌ Gesundheitsdaten in SQLite ohne Verschlüsselung und ohne `FileProtectionType.complete`.
- ✅ Keychain für Tokens, `CryptoKit`/`SQLCipher` für lokale Datenbanken, ATS-Ausnahmen nur für konkrete Domains mit Begründung.

**Prüfliste**
- [ ] Keine Server-Secrets, Private Keys oder Admin-Tokens im Bundle, in Info.plist, `app.json`/`extra`, `.env` oder `EXPO_PUBLIC_*`.
- [ ] Zugangsdaten und Tokens liegen im Keychain (Swift: `SecItem`/Wrapper; RN: `expo-secure-store` oder `react-native-keychain`), nicht in `UserDefaults`/`AsyncStorage`/MMKV ohne Verschlüsselung.
- [ ] Keychain-Zugriffsklasse ist `…ThisDeviceOnly` und nicht `Always`.
- [ ] ATS aktiv; keine `NSAllowsArbitraryLoads`; Ausnahmen nur pro Domain mit dokumentiertem Grund; keine `http://`-Endpunkte für Nutzerdaten.
- [ ] Keine deaktivierte Zertifikatsprüfung im Produktions-Build.
- [ ] Lokale Datenbanken mit sensiblen Daten verschlüsselt oder mit Dateischutz (`FileProtectionType.complete`).
- [ ] Keine sensiblen Werte in Logs, Crash-Reports oder Analytics-Events.
- [ ] Passwörter werden nie lokal gespeichert; Biometrie schützt einen Keychain-Eintrag, nicht einen Klartextwert.
- [ ] Debug-Flags (`allowInsecure`, `skipSSL`, `DEBUG_MODE`) im Release-Build deaktiviert.

**Empfohlene Behebung** – Expo: `expo-secure-store` für Tokens, `expo-crypto` für Hashes, Secrets ins Backend (EAS Secrets nur für Build-Zeit, nicht für Laufzeit-Geheimnisse); Bare RN: `react-native-keychain`, `react-native-mmkv` mit `encryptionKey` aus dem Keychain, `react-native-ssl-pinning`; Swift: `CryptoKit`, Keychain-Wrapper (`KeychainAccess`), `URLSession` mit Standard-Trust-Evaluation, `FileProtectionType.complete` für Dateien; Backend-Proxy für alle Aufrufe, die Server-Keys brauchen.

---

## 1.7 Meldung krimineller Aktivitäten

**Kern der Regel** – Apps, mit denen Nutzer mutmaßliche Straftaten melden können, müssen die zuständigen örtlichen Strafverfolgungsbehörden einbinden und dürfen nur in Ländern oder Regionen angeboten werden, in denen diese Behörden tatsächlich beteiligt sind. Reine „Bürgerwehr"-Apps ohne behördliche Anbindung sind nicht zulässig. Apple will verhindern, dass Meldungen im Leeren laufen oder zur Denunziation missbraucht werden.

**Risikostufe** – Mittel. Selten, aber bei Betroffenheit eine harte Bedingung (Behördennachweis).

**Woran du es im Code erkennst**
- Swift/Objective-C: Formulare `ReportCrime`, `IncidentReport`, `TipSubmission` mit Foto-/Standort-Upload; Endpunkte, die an eigene Server statt an Behördensysteme gehen; Karten mit „Verdächtige melden"-Layern; Regionsprüfung (`Locale.current.region`, `CLGeocoder`) beim Freischalten der Meldefunktion.
- React Native/Expo: `ReportScreen.tsx` mit `expo-location`, `expo-image-picker`; `Linking.openURL('tel:110')` allein reicht nicht als Behördenanbindung; Konfiguration `supportedRegions`, `agencyEndpoints`.
- Beide: Verfügbarkeit nach Ländern in App Store Connect; Kooperationsnachweis (Vertrag, Schnittstelle) in den Review-Notes.

**Typische Verstöße**
- ❌ Nachbarschafts-App mit „Verdächtige Person melden", die Meldungen nur an andere Nutzer verteilt.
- ✅ Hinweis-App einer Landespolizei, nur in deren Region verfügbar, mit dokumentierter Schnittstelle.

**Prüfliste**
- [ ] Meldungen gehen an eine beteiligte Strafverfolgungsbehörde (Schnittstelle oder vertraglicher Prozess), nicht nur an Nutzer oder den Betreiber.
- [ ] Verfügbarkeit ist auf Regionen mit behördlicher Beteiligung beschränkt (Store-Verfügbarkeit plus Prüfung in der App).
- [ ] Kooperationsnachweis liegt in den Review-Notes.
- [ ] Datenschutz: Standort- und Fotodaten der Meldung werden nur für den Meldezweck verarbeitet (siehe Abschnitt 5.1).

**Empfohlene Behebung** – Behördenkooperation vertraglich sichern und dokumentieren; Regionssperre in der App (`Locale`/`expo-localization` + serverseitige Prüfung) und über Store-Verfügbarkeit; Meldefunktion außerhalb der Regionen ausblenden.

---

## Paketreferenz React Native / Expo

| Zweck | Expo | Bare React Native |
|---|---|---|
| Sichere Speicherung von Tokens/Zugangsdaten (1.6) | `expo-secure-store` | `react-native-keychain` |
| Verschlüsselter Key-Value-Store (1.6) | `react-native-mmkv` mit Key aus SecureStore | `react-native-mmkv` mit Key aus Keychain |
| Hashing/Zufallswerte (1.6) | `expo-crypto` | `react-native-quick-crypto` |
| Certificate Pinning (1.6) | Expo-Config-Plugin für Pinning oder Backend-Proxy | `react-native-ssl-pinning` |
| Biometrie als Keychain-Schutz (1.6) | `expo-local-authentication` + SecureStore `requireAuthentication` | `react-native-keychain` mit `accessControl: BIOMETRY_ANY` |
| Textfilter für UGC (1.2) | `obscenity`, `bad-words` | `obscenity`, `bad-words` |
| Chat-UI mit Melde-/Blockier-Hooks (1.2) | `react-native-gifted-chat` (`onLongPress`), `stream-chat-expo` | `react-native-gifted-chat`, `stream-chat-react-native` |
| Bildauswahl mit Vorprüfung (1.2, 1.1.4) | `expo-image-picker` + serverseitige Moderation | `react-native-image-picker` + serverseitige Moderation |
| Elternschranke (1.3) | Eigene Komponente (Rechenaufgabe/Halte-Geste) | Eigene Komponente |
| Externe Links hinter Schranke (1.3) | `expo-web-browser` nach Elternschranke | `Linking.openURL` nach Elternschranke |
| Tracking-Abfrage (in Kids-Apps entfernen, 1.3) | `expo-tracking-transparency` | `react-native-tracking-transparency` |
| HealthKit-Anbindung (1.4.1) | `@kingstinct/react-native-healthkit` (Config-Plugin) | `react-native-health` |
| Bluetooth für zugelassene Messgeräte (1.4.1) | `react-native-ble-plx` (Config-Plugin) | `react-native-ble-plx` |
| Regionsprüfung (1.4.3, 1.7) | `expo-localization` + serverseitige Prüfung | `react-native-localize` + serverseitige Prüfung |
| Support-Kontakt (1.5) | `expo-mail-composer`, `Linking.openURL('mailto:')` | `react-native-mail` |

## Kurz-Prüfliste für diesen Abschnitt

**1.1 Anstößige Inhalte**
- [ ] Keine herabsetzenden Wortlisten, Vorlagen oder Assets; KI-Ausgaben werden moderiert (1.1.1).
- [ ] Gegner in Spielen fiktiv; keine realen Gewaltaufnahmen; Altersfreigabe passt (1.1.2).
- [ ] Keine Kaufvermittlung oder Bauanleitungen für Waffen (1.1.3).
- [ ] Keine sexuellen Inhalte, keine Freischaltung per Kauf, NSFW-Filter bei Generatoren (1.1.4).
- [ ] Religiöse Zitate mit Quelle; keine Hetze (1.1.5).
- [ ] Keine Fake-Anrufe/-SMS, Fake-Scanner, System-UI-Nachbauten; KI-Medien gekennzeichnet (1.1.6).
- [ ] Keine Monetarisierung realer Katastrophen oder Konflikte (1.1.7).

**1.2 Nutzergenerierte Inhalte**
- [ ] Melden-Aktion auf jeder UGC-Oberfläche.
- [ ] Blockieren-Aktion für Nutzer; Wirkung sofort sichtbar.
- [ ] Meldungen erreichen ein reagierendes System; Reaktionszeit belegbar.
- [ ] Text- und Bildfilter vor Veröffentlichung.
- [ ] EULA/Community-Regeln beim ersten Start.
- [ ] Betreiber-Kontakt sichtbar.
- [ ] Keine anonymen Zufalls-Chats, kein ungefilterter NSFW-Feed.
- [ ] Creator-Inhalte moderiert und über In-App-Kauf bezahlt (1.2.1).
- [ ] Alterskennzeichnung plus wirksame Alterssperre für Creator-Inhalte (1.2.1(a)).

**1.3 Kids-Kategorie**
- [ ] Keine Analytics-/Werbe-/Attribution-SDKs mit Datensammlung; Ausnahmen dokumentiert.
- [ ] Kein ATT, kein IDFA, kein `NSUserTrackingUsageDescription`.
- [ ] Keine verhaltensbasierte Werbung.
- [ ] Elternschranke vor externen Links, Store-Verweisen, Share-Sheets und Käufen.
- [ ] Keine Kinder-PII ohne elterliche Einwilligung; kein Social-Login.
- [ ] Altersband und Inhalte stimmen überein.

**1.4 Körperliche Schäden**
- [ ] Keine Sensor-Messung klinischer Werte ohne Nachweis; Arzt-Hinweis; Zulassung in Review-Notes (1.4.1).
- [ ] Kein Dosierungsrechner ohne institutionellen Hintergrund und Zulassung (1.4.2).
- [ ] Kein Verkauf oder Förderung von Tabak, Vape, Drogen, Alkohol-Übermaß; Cannabis nur lizenziert und regional (1.4.3).
- [ ] DUI-Checkpoints nur aus Polizeiquellen; keine Fahr-Freigabe bei Promille-Rechnern (1.4.4).
- [ ] Keine gefährlichen Challenges, Wetten oder Extremziele ohne Sicherheitsnetz (1.4.5).

**1.5 Entwicklerinformationen**
- [ ] Support-Kontakt in der App und funktionierende Support-URL.
- [ ] Wallet-Pässe mit vollständigen Ausstellerdaten und passendem Zertifikat.

**1.6 Datensicherheit**
- [ ] Keine Server-Secrets im Bundle (`Info.plist`, `app.json`, `.env`, `EXPO_PUBLIC_*`).
- [ ] Tokens/Zugangsdaten im Keychain (`expo-secure-store`/`react-native-keychain`/`SecItem`), nicht in `UserDefaults`/`AsyncStorage`.
- [ ] Keychain-Zugriffsklasse `…ThisDeviceOnly`.
- [ ] ATS aktiv, keine `NSAllowsArbitraryLoads`, keine `http://`-Endpunkte für Nutzerdaten.
- [ ] Keine abgeschaltete Zertifikatsprüfung im Release.
- [ ] Lokale sensible Daten verschlüsselt oder mit Dateischutz.
- [ ] Keine Secrets in Logs, Crash-Reports, Analytics, Zwischenablage.

**1.7 Meldung krimineller Aktivitäten**
- [ ] Behördenanbindung nachweisbar; Meldungen gehen an Strafverfolgung.
- [ ] Verfügbarkeit auf Regionen mit Behördenbeteiligung beschränkt.
- [ ] Kooperationsnachweis in Review-Notes; Datenschutz der Meldedaten gewahrt.
