# Modul 6 – Pflege gegenüber Endkunden (nach der Freigabe)

Stand: Oktober 2026. Bezugspunkte: App Review Guidelines in der Fassung vom 8. Juni 2026 sowie die Pflichten aus DSGVO, BGB und UWG, die Kundenkommunikation berühren.
Zurück zur Übersicht: ../SKILL.md

Dieses Modul unterscheidet sich von den Modulen 1 bis 5. Dort geht es darum, was Apple ablehnt. Hier geht es darum, was nach der Freigabe passiert: Kunden schreiben Bewertungen, fragen nach Erstattungen, melden Fehler, verlangen ihre Daten oder kündigen. Wie das Team darauf antwortet, entscheidet über Bewertungsschnitt, Kündigungsquote und Vertrauen. Apples Regeln berühren diese Themen nur am Rand. Wo sie es tun, steht der Bezug dabei. Alles andere ist Praxis und keine Guideline-Pflicht. Rechtliche Fragen sind offene Fragen an das Team, keine Rechtsberatung.

## Wo Pflege am häufigsten schiefgeht

1. **Die Kündigung ist schwerer als der Kauf.** Ein Abo ist mit zwei Taps abgeschlossen, die Kündigung ist aber versteckt oder nur per E-Mail möglich. Folgen: Erstattungsanträge, schlechte Bewertungen und im Extremfall ein Verstoß gegen 3.1.2.
2. **Bewertungen bleiben unbeantwortet oder bekommen Floskeln.** Gerade bei Fehlerberichten wirkt Schweigen wie Desinteresse. Konkrete, neutrale Antworten schaden nie.
3. **Release-Notes passen nicht zum Build.** Ein angekündigtes Feature fehlt, oder ein Fix, der Kunden betrifft, wird verschwiegen (2.3.12).
4. **Support-Links sind tot.** Website-Relaunch, Login-Pflicht oder ein Kontaktformular ohne Eingangsbestätigung (1.5).
5. **Datenanfragen versanden im allgemeinen Postfach.** Die Frist von einem Monat wird nicht verfolgt.

## Inhalt

- [P1 Kundenbewertungen beantworten](#p1-kundenbewertungen-beantworten)
  - [Antwortvorlagen](#antwortvorlagen)
- [P2 Versionshinweise („Was ist neu")](#p2-versionshinweise-was-ist-neu)
- [P3 Support-Kanal und öffentliche Links](#p3-support-kanal-und-öffentliche-links)
- [P4 Abrechnung, Abos und Erstattungen](#p4-abrechnung-abos-und-erstattungen)
- [P5 Datenanfragen und Kontolöschung nach der Freigabe](#p5-datenanfragen-und-kontolöschung-nach-der-freigabe)
- [P6 Störungen und Notfall-Kommunikation](#p6-störungen-und-notfall-kommunikation)
- [P7 Versionspflege und Kompatibilität](#p7-versionspflege-und-kompatibilität)
- [P8 Ton, Nudging und Dark Patterns](#p8-ton-nudging-und-dark-patterns)
- [Pflegeplan: Rhythmus](#pflegeplan-rhythmus)
- [Fundstellen im Projekt](#fundstellen-im-projekt)
- [Offene Fragen an das Team](#offene-fragen-an-das-team)
- [Kurz-Prüfliste](#kurz-prüfliste)

---

## P1 Kundenbewertungen beantworten

**Kern der Pflege** – Bewertungen im App Store sind öffentlich, Antworten ebenso. Sie wirken auf alle, die den Eintrag lesen, nicht nur auf den Schreibenden. Eine gute Antwort zeigt Interessenten, dass sich jemand kümmert, auch wenn der Schreibende unzufrieden ist.

Apple verlangt in 5.6.1 respektvolle Antworten. Verboten bleiben Bewertungen kaufen oder selbst abgeben, Kunden für Bewertungen belohnen und um „5 Sterne" bitten (5.6.1, 3.2.2(vii)). Bewertungen kann der Entwickler nicht selbst entfernen. Verstöße wie Beleidigungen, Spam oder offensichtliche Fälschung meldet man über den Meldeweg in App Store Connect; Apple entscheidet.

**Regeln für Antworten**
- Auf den konkreten Inhalt eingehen, nicht nur „Danke für Ihr Feedback".
- Keine personenbezogenen Daten in der öffentlichen Antwort: keine E-Mail-Adresse, keine Bestell- oder Kontonummer, keine Fall-Details. Für Details auf den Support-Kanal verweisen (P3).
- Keine Bitte, die Bewertung zu ändern oder zu erhöhen. Das liegt nah an 5.6.1. Neutral bleiben: „Wenn du uns Details schickst, kümmern wir uns."
- Sprache der Bewertung spiegeln. Die Vorlagen unten sind deutsch und für andere Sprachen zu übersetzen.
- Auf Beleidigungen nicht eskalieren. Eine neutrale Zeile genügt, die Meldung ist der eigentliche Schritt.
- Bewertungen nach Themen clustern. Ein Fehler, den zehn Kunden nennen, ist ein Release-Thema (P2), kein Einzelfall.

### Antwortvorlagen

Platzhalter stehen in eckigen Klammern. Vor dem Einsatz prüfen, ob die Aussage stimmt.

| Anlass | Vorlage |
|---|---|
| Lob | „Danke für deine Rückmeldung, schön, dass [Funktion] dir hilft. Viel Spaß weiterhin – [Team]" |
| Fehler, behoben in Version [x.y] | „Danke für den Hinweis. Das Problem mit [Symptom] ist in Version [x.y] behoben. Falls es nach dem Update noch auftritt, melde dich bitte über [Support-Link] mit Gerätemodell und iOS-Version." |
| Fehler, in Arbeit | „Danke, dass du das gemeldet hast. Wir haben [Symptom] nachvollzogen und arbeiten daran. Für die Fehlersuche hilft uns [Information]. Schreib uns dazu über [Support-Link]." |
| Feature-Wunsch | „Danke für die Idee zu [Funktion]. Wir sammeln solche Wünsche, können aber keine Zusage machen. Wenn du uns deinen Anwendungsfall beschreibst, nehmen wir ihn in die Planung auf: [Support-Link]." |
| Preis- oder Abo-Frage | „Es tut uns leid, dass [Preis bzw. Abo] nicht klar war. Verlängerung und Kündigung verwaltest du in den Abo-Einstellungen deines Apple-Kontos. Bei einer Abrechnungsfrage melde dich bitte über [Support-Link]." |
| Datenschutz-Frage | „Die Angaben zur Datenverarbeitung stehen in unserer Datenschutzerklärung: [Link]. Für eine konkrete Anfrage wende dich bitte an [Datenschutz-Kontakt]." |
| Negativ, unspezifisch | „Schade, dass die App dich enttäuscht hat. Wenn du uns sagst, was passiert ist, schauen wir uns das an: [Support-Link]." |
| Beleidigung, Spam, Fälschung | Keine inhaltliche Antwort. Bewertung über den Meldeweg melden. |

**Typische Fehler**

❌ „Vielen Dank für Ihre Bewertung! Ihre Bestellnummer 4711 wurde storniert."
✅ „Danke für den Hinweis. Die Stornierung klären wir direkt. Melde dich bitte über [Support-Link]."

❌ „Bitte ändere deine Bewertung, dann helfen wir dir gerne weiter."
✅ Antwort ohne Bezug zur Bewertung. Die Hilfe hängt nicht an einer Gegenleistung.

**Prüfliste P1**
- [ ] Antwortprozess mit Zuständigkeit und Frist (z. B. wöchentlich) ist definiert.
- [ ] Keine personenbezogenen Daten in öffentlichen Antworten.
- [ ] Keine Bitte um Änderung oder Erhöhung der Bewertung, keine Gegenleistung.
- [ ] Bewertungsthemen werden monatlich geclustert.

**Fundstellen** – Im Code liegt nur die Bewertungsanfrage (`requestReview`, `StoreReview`). Sie gehört zu 5.6.1 (Modul 5). Der Antwortprozess liegt meist außerhalb des Repos, in App Store Connect oder im Support-Tool. Danach fragen, statt ihn zu erraten.

---

## P2 Versionshinweise („Was ist neu")

**Kern der Pflege** – Der Text ist für Bestandskunden die einzige Information über die Änderungen, bevor sie updaten. Apple verlangt in 2.3.12, dass er die tatsächlichen Neuerungen beschreibt. Für Endkunden heißt das: nutzenorientiert, konkret und ehrlich zur Größe der Änderung.

**Aufbau, der sich bewährt hat**
- Eine Zeile mit dem wichtigsten Nutzen.
- Drei bis fünf Punkte, jeweils mit „Neu", „Verbessert" oder „Behoben".
- Keine Ticketnummern, keine internen Begriffe, keine Versprechen auf Funktionen, die erst mit einem späteren Update kommen (2.3.12, 2.5.2).
- Die Standardzeile „Fehlerbehebungen und Verbesserungen" ist nur bei reinen Fixes richtig. Nach einem Redesign oder einer neuen Navigation wirkt sie wie ein Verschweigen.

Beispiel:
```
Neu: Erinnerungen lassen sich jetzt pro Wochentag einstellen.
• Verbessert: Die Synchronisation mit iCloud läuft schneller.
• Behoben: Absturz beim Öffnen von Notizen mit Anhang.
```

**Lokalisierung** – Jede Sprache bekommt eigene Texte. Ein deutscher Text im US-Storefront wirkt nachlässig, ein englischer im deutschen fast genauso. Übersetzungen von einem Muttersprachler prüfen lassen.

**Abgleich vor dem Einreichen** – Changelog oder Git-Log gegen die Release-Notes halten. Nennt der Text ein Feature, das nicht im Build steckt, ist das ein Befund nach 2.3.12, kein Tippfehler.

**Risikostufe** – Niedrig bis mittel. Schwache Texte kosten Bewertungen; falsche Versprechen kosten Vertrauen und bei 2.3.12 die Freigabe.

**Typische Fehler**

❌ „Verschiedene Verbesserungen" nach einem Redesign mit neuer Navigation.
❌ „Premium-Funktionen kommen bald" ohne Build dazu.
✅ Konkrete Punkte, auch wenn sie klein sind.

**Prüfliste P2**
- [ ] Release-Notes sind in allen Lokalisierungen aktualisiert.
- [ ] Jeder Punkt lässt sich im Build nachweisen.
- [ ] Keine Vorankündigungen, keine Ticketnummern.
- [ ] Bei großen Änderungen keine Standardfloskel.

**Fundstellen** – `fastlane/metadata/*/release_notes.txt`, `whatsnew/`, `CHANGELOG.md`, `app.json` (`version`, `buildNumber`) für den Abgleich.

---

## P3 Support-Kanal und öffentliche Links

**Kern der Pflege** – Drei Links gehören zur laufenden Pflege und stehen in App Store Connect: Support-URL (Pflicht), Datenschutzerklärungs-URL (Pflicht) und Marketing-URL (optional). Die Support-Seite muss einen funktionierenden Kontaktweg zeigen und darf nicht hinter einem Login liegen. Auch in der App muss der Kontakt auffindbar sein (1.5, Modul 1).

**Pflegepunkte**
- **Linkcheck pro Release und monatlich.** Website-Relaunches machen Support-URLs still tot.
- **Kontakt in der App.** Über-Screen mit Support-Kanal, App-Version, Build-Nummer, Datenschutzerklärung und Impressum. Diese Angaben beschleunigen die Triage, wenn der Kunde sie mitschickt.
- **Keine Zusagen, die man nicht hält.** „Antwort innerhalb von 24 Stunden" nur, wenn das Postfach das tatsächlich schafft. Besser: „Wir melden uns in der Regel innerhalb weniger Werktage."
- **Triage nach Kategorien**: Technik, Abrechnung, Konto und Löschung, Datenschutz-Anfrage, Missbrauchsmeldung (nutzergenerierte Inhalte, Modul 1, 1.2), Presse und Partner. Jede Kategorie braucht eine Zuständigkeit.
- **Meldungen zu nutzergenerierten Inhalten zeitnah bearbeiten** (1.2). Eine Meldung, die drei Wochen liegt, ist im Prüffall ein Problem.
- **Eingangsbestätigung** für jede Anfrage, damit der Kunde weiß, dass sie angekommen ist.

**Typische Fehler**

❌ Support-URL zeigt nach dem Relaunch auf „Coming soon".
❌ Kontakt nur über ein Formular ohne Eingangsbestätigung.
✅ Support-Seite mit E-Mail-Adresse, FAQ, Statusseite und Hinweis auf die übliche Antwortzeit.

**Prüfliste P3**
- [ ] Support-URL und Datenschutz-URL in App Store Connect antworten ohne Login mit Erfolgsstatus.
- [ ] Support-Kanal ist in der App erreichbar (1.5).
- [ ] Jede Anfrage erhält eine Eingangsbestätigung.
- [ ] Triage-Kategorien mit Zuständigkeit sind definiert.
- [ ] Meldungen zu nutzergenerierten Inhalten haben eine Bearbeitungsfrist.

**Fundstellen** – `SettingsScreen`, `AboutScreen`, `mailto:`, `Linking.openURL('mailto:`, `MFMailComposeViewController`, in `app.json` ggf. `extra.supportUrl`. Die Support-URL selbst steht nicht im Code. Danach fragen.

---

## P4 Abrechnung, Abos und Erstattungen

**Kern der Pflege** – Für Käufe über den App Store entscheidet Apple über Erstattungen. Der Kunde stellt den Antrag bei Apple, über reportaproblem.apple.com oder in den Kaufeinstellungen. Die App soll diesen Weg zeigen und ihn nicht verstecken. Abos verwaltet der Kunde in den Abo-Einstellungen seines Apple-Kontos. Die App darf dorthin verlinken, muss den Kündigungsweg aber nicht selbst bauen.

Anders liegt es bei Abos über externe Kauflinks (3.1.1(a), Modul 3). Dort gelten die Pflichten des Vertrags selbst, einschließlich Kündigung. Siehe „Offene Fragen".

**Umsetzung**
- **StoreKit 2 (Swift):** `AppStore.showManageSubscriptions(in:)` für die Abo-Verwaltung, `Transaction.beginRefundRequest(in:)` für den Erstattungsantrag. Aktuelle Signaturen in der Apple-Dokumentation prüfen.
- **Expo / React Native:** `Linking.openURL('https://apps.apple.com/account/subscriptions')` für die Abo-Verwaltung. Für Erstattungen die Apple-Seite zum Melden eines Problems öffnen, nicht ein eigenes Formular, das so tut, als würde es erstatten.
- **Platzierung:** Abo-Verwaltung und Erstattungsweg gehören in die Einstellungen, nicht auf die Paywall.

**Preisänderungen**
- Preiserhöhungen bei Abos laufen über Apples Zustimmungsverfahren für Bestandskunden. Kommuniziere sie vorher in der App und in den Release-Notes, damit niemand überrascht wird.
- Eine stille Preisänderung ist das Gegenteil dessen, was der Kunde beim Abo erwartet, und erzeugt Erstattungsanträge.

**Guthaben**
- Gekaufte Guthaben laufen nicht ab (3.1.1, Modul 3). Hinweise im Kleingedruckten dürfen diese Zusage nicht aufheben.

**Typische Fehler**

❌ Kündigung nur per Mail an den Support.
❌ Erstattung „auf Anfrage per E-Mail", ohne Hinweis auf Apples Weg.
✅ Einstellungsbereich mit „Abo verwalten" und „Problem melden" nebeneinander.

**Prüfliste P4**
- [ ] Abo-Verwaltung über `showManageSubscriptions` oder die Apple-Abo-Seite erreichbar.
- [ ] Erstattungsweg verlinkt oder über StoreKit angeboten.
- [ ] Keine stillen Preisänderungen.
- [ ] Bei Web-Abos: eigener Kündigungsweg, rechtlich geprüft.

**Fundstellen** – `showManageSubscriptions`, `beginRefundRequest`, `apps.apple.com/account/subscriptions`, `reportaproblem`.

---

## P5 Datenanfragen und Kontolöschung nach der Freigabe

**Kern der Pflege** – Anfragen zu personenbezogenen Daten muss der Verantwortliche beantworten: Auskunft (Art. 15 DSGVO), Löschung (Art. 17), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). Die Frist beträgt einen Monat. Sie kann um zwei weitere Monate verlängert werden, wenn der Kunde über die Verzögerung und die Gründe informiert wird (Art. 12 Abs. 3). Das ist keine Apple-Regel, aber die Frist, an der Datenschutz-Beschwerden hängen.

Zusammenspiel mit Apple: Die Kontolöschung in der App ist Pflicht (5.1.1(v), Modul 5). Eine E-Mail-Anfrage ist ein zusätzlicher Weg, kein Ersatz für die Löschfunktion.

**Praxis**
- **Eingang:** ein eigenes Postfach oder Formular, nicht die allgemeine Support-Adresse.
- **Frist-Tracking:** Eingangsdatum, Fälligkeit, Status. Eine Tabelle genügt.
- **Identität:** Nur so weit prüfen, wie nötig. Eine Ausweiskopie per E-Mail nicht als Standard verlangen, wenn eine Bestätigung über das Konto möglich ist.
- **Auskunft:** umfasst alle Daten, auch bei Drittanbietern (Analytics, Crash-Reporting, Werbe-SDKs). Ausgangspunkt ist die Empfängerliste der Datenschutzerklärung (5.1.2).
- **Löschung:** Backups und Protokolle haben eigene Löschfristen, die in der Datenschutzerklärung stehen müssen. Bei „Mit Apple anmelden" gehört der Token-Widerruf dazu (5.1.1(v)).
- **Datenpanne:** Meldung an die Aufsichtsbehörde binnen 72 Stunden nach Kenntnis (Art. 33 DSGVO), gegebenenfalls Benachrichtigung der Betroffenen (Art. 34). Der Ablaufplan wird vorab geschrieben, nicht im Ernstfall.

**Typische Fehler**

❌ Löschanfragen landen im allgemeinen Postfach und werden nicht gezählt.
❌ Konto gelöscht, aber das Profil beim Analytics-Anbieter bleibt bestehen.
✅ Löschprozess mit Checkliste pro Dienstleister und Eintrag im Verarbeitungsverzeichnis.

**Prüfliste P5**
- [ ] Eigener Eingangsweg für Datenanfragen ist dokumentiert.
- [ ] Die Monatsfrist wird verfolgt.
- [ ] Löschung in der App ist tatsächlich umgesetzt, einschließlich der Dienstleister.
- [ ] Ablaufplan für Datenpannen mit 72-Stunden-Frist liegt vor.

**Fundstellen** – `deleteAccount`, `deleteUser`, `exportData`, `requestDataExport`, `revokeToken`, Datenschutz-Kontakt im Settings-Screen. Ein Export-Endpunkt gilt erst als vorhanden, wenn er im Code nachweisbar ist.

---

## P6 Störungen und Notfall-Kommunikation

**Kern der Pflege** – Bei einem Ausfall zählt, was der Kunde in den ersten Minuten sieht. Bewertungen zu Störungen entstehen oft in den Stunden danach.

**Ablauf**
1. **Erkennen:** Crash-Monitoring (Xcode-Organizer, MetricKit, Sentry, Crashlytics), Serverüberwachung, Support-Eingang als Frühwarnung.
2. **Einordnen:** Welche Funktion ist betroffen, wie viele Nutzer, gibt es Datenverlust?
3. **Kommunizieren:** Statusseite aktualisieren, In-App-Hinweis bei Ausfall eines Dienstes, Antwortbaustein für Bewertungen bereithalten. Keine Schuldzuweisung an Apple, Google oder Drittanbieter.
4. **Beheben:** Hotfix als Store-Update. Ein OTA-Update darf nur Fehler beheben (2.5.2, Modul 2). Bei kritischen Fehlern lässt sich eine beschleunigte Prüfung bei Apple anfragen. Das ist für echte Notfälle gedacht, nicht für den Alltag.
5. **Nachbereiten:** Kurzer Bericht, was passiert ist und was sich ändert. Betroffene Kunden erhalten eine ehrliche Entschuldigung, keine Floskel.

**Verbote in dieser Lage**
- Ein Schalter, der während einer Störung Funktionen ausblendet, ist kein Wartungsmodus, wenn er auch bei Prüfungen greift (5.6.5).
- Wartungsbanner gehören als Daten in die App (Remote Config, Text), nicht als Codepfad, der Funktionen verbirgt.

**Typische Fehler**

❌ Remote-Config-Flag `maintenance_hide_premium`, das Käufe in der Prüfphase verbirgt.
✅ Remote-Config-Text `maintenance_banner`, der bei Störungen einen Hinweis zeigt.

**Prüfliste P6**
- [ ] Statusseite oder ein anderer Kanal für Störungsmeldungen ist vorhanden.
- [ ] Wartungsbanner sind Daten, kein Review-Schalter.
- [ ] Der Weg für Hotfix und Store-Update ist dokumentiert.
- [ ] Eine Vorlage für Bewertungsantworten während Störungen liegt bereit.

---

## P7 Versionspflege und Kompatibilität

**Kern der Pflege** – Kunden auf älteren Geräten oder Betriebssystemen gehören zur Pflege. Wer die Mindestversion anhebt, sollte das ankündigen. Sonst stehen Kunden nach dem Update plötzlich vor einer App, die nicht mehr startet.

**Punkte**
- **Mindest-OS bewusst setzen** (`IPHONEOS_DEPLOYMENT_TARGET`, `expo.ios.deploymentTarget`) und Änderungen in den Release-Notes nennen.
- **Neue iOS-Versionen mit Beta testen** und nach dem Erscheinen zeitnah die Kompatibilität bestätigen. Fehler in neuen Systemversionen sind eine häufige Ursache für negative Bewertungen nach großen Systemupdates.
- **Abgekündigte APIs und Pakete** ersetzen, bevor sie entfernt werden (Modul 2, Abschnitt Software-Anforderungen).
- **SDK-Minimum** für Uploads einhalten. Apple erhöht es regelmäßig.
- **Gekaufte Funktionen erhalten:** Wer auf ein Abo-Modell umstellt, darf bestehenden Kunden nichts wegnehmen, das sie bereits gekauft haben (3.1.2).
- **Lebenszyklus dokumentieren:** Ab wann alte Versionen keinen Support mehr erhalten.

**Typische Fehler**

❌ Mindestversion still von iOS 16 auf iOS 18 angehoben. Kunden auf iOS 16 erfahren es erst beim Update-Versuch.
✅ Release-Notes: „Ab dieser Version benötigt die App iOS 18."

**Prüfliste P7**
- [ ] Mindest-OS ist dokumentiert und Änderungen sind angekündigt.
- [ ] Beta-Test der neuen iOS-Version ist eingeplant.
- [ ] Gekaufte Funktionen bleiben nach einem Modellwechsel erhalten.

---

## P8 Ton, Nudging und Dark Patterns

**Kern der Pflege** – Die App darf Kunden nicht durch Gestaltung zu Entscheidungen drängen, die sie nicht treffen wollen: Kündigung, Newsletter, Tracking, Bewertung. Apple benennt das in 3.1.2 (Lockangebote, Bait-and-Switch) und in 5.1.1 (Datenerhebung ohne Einwilligung). Für Deutschland und die EU kommen dazu:
- UWG: Werbung nur mit Einwilligung, E-Mail-Werbung nach § 7 UWG nur mit ausdrücklicher Einwilligung.
- DSGVO: Einwilligungen müssen freiwillig und informiert erfolgen.
- BGB: Für online geschlossene Verbraucherverträge mit Laufzeit verlangt § 312k BGB eine Kündigungsfunktion (Kündigungsbutton). Siehe P4 und „Offene Fragen".

**Erkennungsmuster**
- Kündigung: „Abo behalten" groß und farbig, „Kündigen" als versteckter Textlink, Gegenangebot mit Schuldgefühl („Willst du uns wirklich verlassen?").
- Countdown-Timer, der bei jedem Aufruf neu startet.
- Vorausgewählte Checkboxen für Newsletter, Tracking oder Werbung.
- Push-Abfrage in einer Schleife nach jeder Ablehnung.
- Ablehnen als graue, kleine Schaltfläche, Zustimmen als Vollfläche.

**Ton in Texten**
- Sachlich und klar. Fehlermeldungen nennen den nächsten Schritt: „Die Verbindung ist unterbrochen. Versuch es in einer Minute erneut." Nicht: „Oops! Da ist etwas schiefgelaufen."
- Du oder Sie: einmal festlegen und durchhalten, auch in Bewertungsantworten und Mails. Das ist eine offene Frage an das Team.
- Keine Angst- oder Schuldtexte und keine Vergleiche mit Wettbewerbern in Antworten.

**Typische Fehler**

❌ Beim Abbrechen der Kündigung: „Bist du sicher? Du verlierst alle deine Daten!"
✅ Kündigungsdialog mit einer sachlichen Angabe, bis wann der Zugang läuft.

**Prüfliste P8**
- [ ] Kündigung ist genauso leicht zu finden wie der Kauf.
- [ ] Einwilligungen für Newsletter, Tracking und Push sind standardmäßig aus.
- [ ] Keine Countdown-Timer ohne echte Frist.
- [ ] Fehlermeldungen nennen einen nächsten Schritt.

**Fundstellen** – `defaultValue: true` oder `isOn: true` bei Marketing-Feldern, `Alert.alert` mit Ablehnungsschleife, `requestPermission`-Aufrufe in Schleifen.

---

## Pflegeplan: Rhythmus

| Rhythmus | Aufgabe | Bezug |
|---|---|---|
| Täglich bzw. werktags | Support-Postfach triagieren, Meldungen zu nutzergenerierten Inhalten bearbeiten, Crash-Alerts prüfen | P3, P6 |
| Wöchentlich | Neue Bewertungen beantworten, Abrechnungsfragen klären, Datenanfragen gegen die Frist prüfen | P1, P4, P5 |
| Pro Release | Release-Notes in allen Sprachen, Links prüfen, Mindest-OS prüfen, Review-Notizen aktualisieren. Bei Änderungen an Abo, Konto oder nutzergenerierten Inhalten den Einreichungs-Check erneut laufen lassen | P2, P3, P7; Module 1 bis 5 |
| Monatlich | Bewertungs- und Support-Themen clustern, Linkcheck, Abo-Kennzahlen und Erstattungsquote | P1, P3, P4 |
| Quartalsweise | Datenschutzerklärung und Verarbeitungsverzeichnis prüfen, SDK-Updates und Privacy-Manifest, Altersfreigabe prüfen, Änderungen der Apple-Guidelines gegen den Stand dieses Skills abgleichen | P5, P8; Module 1, 2, 5 |
| Bei jedem OS-Release | Kompatibilität bestätigen, Mindest-OS überprüfen | P7 |

---

## Fundstellen im Projekt

| Thema | Wo suchen |
|---|---|
| Bewertungsanfrage | `requestReview`, `StoreReview`, `write-review` |
| Support-Kontakt | `mailto:`, `SettingsScreen`, `AboutScreen`, `MFMailComposeViewController`, `extra.supportUrl` |
| Release-Notes | `fastlane/metadata/*/release_notes.txt`, `whatsnew/`, `CHANGELOG.md` |
| Abo-Verwaltung | `showManageSubscriptions`, `apps.apple.com/account/subscriptions` |
| Erstattung | `beginRefundRequest`, `reportaproblem` |
| Datenanfrage | `exportData`, `requestDataExport`, Datenschutz-Kontakt im Settings-Screen |
| Konto löschen | `deleteAccount`, `deleteUser`, `revokeToken` (5.1.1(v)) |
| Störungsbanner | Remote-Config-Schlüssel mit Text, Link zur Statusseite |
| Mindest-OS | `IPHONEOS_DEPLOYMENT_TARGET`, `deploymentTarget`, `MinimumOSVersion` |
| Vorausgewählte Einwilligungen | `defaultValue: true`, `isOn: true` bei Marketing-Feldern |

Antwortprozesse für Bewertungen, Postfächer und Statusseiten liegen meist außerhalb des Repos. Wenn sie im Code nicht auftauchen, ist das keine Lücke im Code, sondern eine offene Frage an das Team.

---

## Offene Fragen an das Team

- Wer beantwortet Bewertungen, in welchem Rhythmus und mit welcher Frist? (P1)
- Du oder Sie in der Kundenkommunikation? (P8)
- Welche Support-Kanäle gibt es, und welche Antwortzeit ist realistisch? (P3)
- Gibt es Abos oder Käufe über Webshops oder externe Kauflinks? Dann gilt zusätzlich das Verbraucherrecht, und eine Rechtsberatung ist nötig. (P4)
- Wie lange werden alte iOS-Versionen unterstützt? (P7)
- Gibt es einen Ablaufplan für Datenpannen mit 72-Stunden-Frist? (P5)

---

## Kurz-Prüfliste

- [ ] **P1 Bewertungen:** Zuständigkeit und Vorlagen stehen, keine personenbezogenen Daten, keine Bitte um Bewertungsänderung.
- [ ] **P2 Release-Notes:** alle Sprachen, Abgleich mit dem Build, keine Vorankündigung.
- [ ] **P3 Support:** Links antworten ohne Login, Kontakt in der App, Triage-Kategorien.
- [ ] **P4 Abrechnung:** Abo-Verwaltung und Erstattungsweg erreichbar, keine stillen Preisänderungen.
- [ ] **P5 Datenschutz:** Monatsfrist wird verfolgt, Löschung inklusive Dienstleister, Ablaufplan für Datenpannen.
- [ ] **P6 Störung:** Statuskanal, Hotfix-Weg, Wartungsbanner ohne Review-Schalter.
- [ ] **P7 Versionen:** Mindest-OS angekündigt, Beta-Test, gekaufte Funktionen erhalten.
- [ ] **P8 Ton:** Kündigung so leicht wie der Kauf, Einwilligungen standardmäßig aus, sachliche Texte.
