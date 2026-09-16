# Befundvorlage – App-Store-Freigabe-Check

Verwende diese Struktur für jeden Bericht. Abschnitte ohne Inhalt bleiben stehen und erhalten den Vermerk „keine Befunde", damit das Team sieht, dass geprüft wurde.

---

# App-Store-Freigabe-Check: {App-Name}

**Geprüft am:** {Datum} · **Codebasis:** {Swift / Objective-C / React Native / Expo} · **Zielplattformen:** {iOS, iPadOS, …}
**Guideline-Stand:** App Review Guidelines vom 8. Juni 2026
**Prüfumfang:** {welche Module geladen wurden, welche Verzeichnisse gelesen wurden, was nicht eingesehen werden konnte}

## 1. Freigabe-Ampel

{Ein Satz. Genau eine der drei Aussagen:}
- 🟢 **Einreichbar.** Keine kritischen oder hohen Befunde.
- 🟡 **Einreichbar nach Behebung.** {n} kritische und {m} hohe Befunde, alle mit klarer Behebung.
- 🔴 **Nicht einreichbar.** {Grund in einem Halbsatz, z. B. Geschäftsmodell umgeht In-App-Kauf; braucht Konzeptentscheidung.}

## 2. Kritische und hohe Befunde

{Pro Befund ein Block. Reihenfolge: erst 🔴, dann 🟠, innerhalb der Stufe nach Aufwand aufsteigend – schnelle Gewinne zuerst.}

### {Nr}. {Kurztitel} — 🔴 Kritisch · Guideline {x.y.z}

**Was der Gutachter sieht:** {Beschreibung des Verhaltens oder der Metadaten aus Sicht der Person, die die App testet. Kein Code-Jargon.}

**Fundstelle:** `{pfad/zur/datei.swift}:{Zeile}` – {ein Satz, was dort steht} · {weitere Fundstellen, falls gleicher Befund}

**Behebung:** {konkrete API, konkretes Paket, konkreter Text. Bei React Native/Expo zuerst das Expo-Paket, dann die bare Alternative.}

```{sprache}
{max. 10 Zeilen Zielzustand, wenn es die Behebung klarer macht}
```

**Aufwand:** {Stunden / Tage, grob} · **Abhängigkeiten:** {z. B. Backend-Endpunkt für Kontolöschung nötig}

---

## 3. Mittlere Befunde und Hinweise

| Nr | Stufe | Guideline | Befund | Fundstelle | Behebung |
|----|-------|-----------|--------|------------|----------|
| {n} | 🟡 | {x.y.z} | {ein Satz} | `{datei:zeile}` | {ein Satz} |
| {n} | 🔵 | {x.y.z} | {ein Satz} | `{datei:zeile}` | {ein Satz} |

## 4. Was bereits gut gelöst ist

{Drei bis fünf Punkte mit Guideline-Bezug. Zweck: Das Team soll beim Beheben nichts davon versehentlich entfernen.}

- {z. B. Käufe werden über StoreKit 2 mit `Transaction.currentEntitlements` verifiziert und `AppStore.sync()` ist im Einstellungsbildschirm erreichbar (3.1.1).}

## 5. Offene Fragen an das Team

{Alles, was aus Code und Konfiguration nicht entscheidbar ist. Jede Frage mit dem Guideline-Punkt, den die Antwort betrifft.}

- {z. B. In welchen Regionen wird die App angeboten? Davon hängt ab, ob der externe Kauf-Link in `PaywallView.swift` zulässig ist (3.1.1(a)).}
- {z. B. Liegt für die Musik im Onboarding eine Lizenz vor? (5.2.1)}

## 6. Einreichungs-Checkliste

{Kurz-Prüflisten aus den geladenen Modulen, abgehakt. ✅ erfüllt · ❌ Befund oben · ➖ nicht zutreffend · ❓ nicht prüfbar}

### Datenschutz (5.1)
- ✅ …
- ❌ … → Befund {Nr}

### Zahlungen (3.1)
- …

{weitere Abschnitte je nach geladenen Modulen}

## 7. Vorgeschlagene Review-Notizen

{Optional, aber wertvoll: Text für das Feld „Notes for Review" in App Store Connect – Demo-Zugang, wo versteckte Funktionen zu finden sind, warum bestimmte Berechtigungen nötig sind, Nachweise für Lizenzen. Auf Englisch, weil Apples Gutachter Englisch lesen. Laut App-Store-Connect-Hilfe nimmt das Feld höchstens 4.000 Bytes auf – nicht Zeichen: Umlaute, Sonderzeichen und Emoji belegen mehrere Bytes, deshalb vor dem Einfügen in UTF-8-Bytes zählen.}

---

## Regeln für die Formulierung

- Jeder Befund beginnt mit dem, was der Gutachter sieht – nicht mit der Codezeile. Beispiel: „Beim Kauf des Premium-Pakets öffnet sich Safari mit einer Stripe-Seite" statt „`Linking.openURL` in `Paywall.tsx`".
- Guideline-Nummern stehen immer dabei. Das Team sucht damit in Apples Ablehnungstext und in den Modulen.
- Keine Weichmacher wie „eventuell", „könnte problematisch sein". Wenn du unsicher bist, gehört der Punkt in „Offene Fragen".
- Ein Befund, der an mehreren Stellen auftritt, wird einmal beschrieben und listet alle Fundstellen. Keine Wiederholungen.
- Behebungen nennen die konkrete API oder das konkrete Paket. „Datenschutz verbessern" ist keine Behebung; „`NSUserTrackingUsageDescription` ergänzen und `ATTrackingManager.requestTrackingAuthorization` vor dem ersten `Adjust.appDidLaunch` aufrufen" ist eine.
- Aufwandsschätzungen sind grob und ehrlich. Eine fehlende Kontolöschung mit Backend-Anbindung ist kein Nachmittag.
