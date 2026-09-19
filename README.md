# App-Store-Freigabe-Check

Ein Skill für Claude (Claude Code, Cowork, Claude.ai) und kompatible KI-Agenten, der App-Code und Store-Metadaten gegen Apples App Review Guidelines prüft – bevor Apple es tut.

**Autor:** Mark Zimmermann
**Sprache:** Deutsch
**Version:** 1.2.0
**Stand:** App Review Guidelines vom 8. Juni 2026 (geprüft September 2026)
**Plattformen:** iOS, iPadOS, macOS, watchOS, tvOS, visionOS
**Codebasen:** Swift/SwiftUI, Objective-C, React Native, Expo

Projektseite: https://godmodeai2025.github.io/Appstore-Review/

## Was der Skill leistet

Der Skill arbeitet wie ein Gutachter, der eine App vor der Einreichung durchleuchtet. Er erkennt zuerst, was für ein Projekt vorliegt, bestimmt daraus ein Risikoprofil, lädt nur die passenden Regelmodule und liefert am Ende einen Befundbericht, den ein Entwicklerteam direkt abarbeiten kann: Freigabe-Ampel, kritische und hohe Befunde mit Fundstelle und Behebung, mittlere Befunde als Tabelle, offene Fragen an das Team, Einreichungs-Checkliste und ein Vorschlag für die Review-Notizen in App Store Connect.

Jede Aussage trägt eine Nachweisstufe – Codeprüfung, automatischer Test, beobachteter App-Test, Nutzerbestätigung oder Apple-Entscheidung. „Keine Befunde" heißt damit nicht automatisch „einreichbar": Was nicht geprüft werden konnte, bleibt offen und die Ampel steht auf „nicht beurteilbar".

Alle fünf Abschnitte der Guidelines sind vollständig abgedeckt, jeder Punkt mit Kern der Regel, Risikostufe, Erkennungsmustern für Swift und React Native/Expo, typischen Verstößen, Prüfliste und Behebungsempfehlung:

| Modul | Inhalt |
|---|---|
| 1 Sicherheit | Anstößige Inhalte, nutzergenerierte Inhalte, Kids-Kategorie, körperliche Schäden, Entwicklerinformationen, Datensicherheit, Meldung krimineller Aktivitäten |
| 2 Leistung | Vollständigkeit, Archivprüfung des eingereichten Builds, Betatests, Metadaten, Hardware-Kompatibilität, Mac-App-Store-Regeln inklusive Erstinstallations- und Upgrade-Test, Software-Anforderungen (private APIs, nachgeladener Code, Hintergrundmodi, IPv6, Erweiterungen, Werbung) |
| 3 Geschäft | In-App-Kauf, externe Kauf-Links mit regionalen Sonderregeln, Abonnements, Reader-Apps, Kryptowährungen, zulässige und unzulässige Geschäftsmodelle, Paywall-Prüfung, Entscheidungsbaum für digitale Güter |
| 4 Design | Nachahmer, Mindestfunktionalität, Spam, Erweiterungen, Apple-Dienste, Push-Benachrichtigungen, Mini-Apps und Emulatoren, Login-Dienste, Apple Pay, Monetarisierung von Systemfunktionen |
| 5 Recht | Datenschutz (Erklärung inklusive Inhaltsprüfung, Einwilligung, Purpose-Strings, Kontolöschung, Privacy-Manifest, ATT), Drittanbieter-KI in drei Fällen – fest eingebundener Anbieter, vom Nutzer konfigurierte Clients wie MCP, rein lokale Verarbeitung –, Gesundheitsdaten, Kinder, Standort, geistiges Eigentum, Glücksspiel, VPN, MDM, Verhaltenskodex |

Dazu kommt ein Schnellscan-Skript, das ein Projekt in Sekunden nach bekannten Mustern durchsucht: private APIs, hartcodierte Schlüssel, externe Checkout-URLs, fehlende oder vage Purpose-Strings, im nativen Code genutzte, aber nicht deklarierte Required-Reason-APIs, Aufrufe von KI-Diensten Dritter, Tracking-SDKs ohne ATT, Kontoerstellung ohne Kontolöschung, Drittanbieter-Login ohne Alternative, In-App-Käufe ohne Wiederherstellung, Android-Verweise, Hintergrundmodi, OTA-Update-Konfiguration und Debug-Reste.

Gefundene Geheimnisse gibt der Scan nicht aus. Bei Treffern auf Schlüssel, Tokens oder Passwörter nennt er nur Fundstelle und Typ, und bekannte Geheimnis-Schablonen werden auch aus allen übrigen Auszügen entfernt – in der Textausgabe wie im JSON. So landet kein Schlüssel im Prüfbericht, der anschließend durch Chats, Tickets und Dateien wandert.

## Installation

### Claude Code

```bash
git clone https://github.com/GodModeAI2025/Appstore-Review.git ~/.claude/skills/app-store-freigabe-check
```

Alternativ das Repository in ein Projekt unter `.claude/skills/app-store-freigabe-check/` legen, dann gilt der Skill nur dort.

### Cowork / Claude.ai

Die Datei `SKILL.md` zusammen mit den Ordnern `references/` und `scripts/` als Skill hochladen bzw. das Repository als ZIP importieren. Alle Verweise innerhalb des Skills sind relativ, der Ordnername ist frei wählbar.

### Andere Agenten

Jeder Agent, der Skills im SKILL.md-Format liest (Cursor, Windsurf, Codex u. a.), kann das Repository als Skill-Verzeichnis einbinden.

## Nutzung

Den Agenten im Projektverzeichnis starten und eine der folgenden Aufgaben stellen:

```
Prüfe diese App auf App-Store-Tauglichkeit.
Wird Apple das durchwinken? Schau dir besonders die Paywall an.
Apple hat uns wegen Guideline 5.1.1(v) abgelehnt – was fehlt?
Wir bieten einen lokalen MCP-Server an – was muss offengelegt werden?
Ist ATT bei unserem SDK-Setup nötig?
Prüfe die Purpose-Strings und das Privacy-Manifest.
Wir bauen Chat mit Bildupload – was verlangt Apple dafür?
```

Der Schnellscan lässt sich auch direkt aufrufen:

```bash
python3 scripts/schnellscan.py /pfad/zum/projekt
python3 scripts/schnellscan.py /pfad/zum/projekt --json
```

Die Ausgabe ist eine Rohliste und ersetzt nicht die Bewertung im Kontext.

## Aufbau

```
app-store-freigabe-check/
├── SKILL.md                    Ablauf, Risikostufen, Fehlurteile, Umgang mit Ablehnungen
├── README.md
├── scripts/
│   └── schnellscan.py          musterbasierter Rohscan (Python 3, keine Abhängigkeiten)
└── references/
    ├── befund-vorlage.md       verbindliche Berichtsstruktur
    ├── 1-sicherheit.md
    ├── 2-leistung.md
    ├── 3-geschaeft.md
    ├── 4-design.md
    └── 5-recht.md
```

## Grenzen

Der Skill ersetzt keine Rechtsberatung zu DSGVO, COPPA, Finanz- oder Glücksspielrecht und prüft kein Design gegen die Human Interface Guidelines. Metadaten in App Store Connect kann er nicht einsehen; Beschreibung, Screenshots, Altersfreigabe-Fragebogen und Review-Notizen müssen dem Agenten bei Bedarf mitgegeben werden. Er startet die App nicht und öffnet weder Archiv noch Datenschutzseite von sich aus – liegen sie nicht vor, bleiben die zugehörigen Punkte im Bericht ausdrücklich offen.

## Lizenz

MIT
