# Abschnitt 3 – Geschäftsmodelle (Business)

Stand: Apple App Review Guidelines, Fassung vom 8. Juni 2026 (geprüft September 2026).
Zurück zur Übersicht: ../SKILL.md

Abschnitt 3 ist der Abschnitt mit den teuersten Ablehnungen: Hier geht es nicht um einen fehlenden Text in der Info.plist, sondern um die Frage, ob das Geschäftsmodell der App überhaupt in den App Store passt. Ein Verstoß gegen 3.1.1 wird selten mit einem „bitte nachbessern" quittiert, sondern blockiert das Release, bis der komplette Kaufpfad umgebaut ist. Prüfe diesen Abschnitt deshalb immer zuerst und mit Blick auf den gesamten Datenfluss: Wo entsteht ein Preis, wo wird er bezahlt, wo wird das Ergebnis konsumiert?

## Wo Apple aktuell besonders genau hinschaut

1. **Externe Kauflinks außerhalb der zugelassenen Storefronts.** Seit den Regeländerungen für USA (Gerichtsurteil 2025), EU (DMA, neue Geschäftsbedingungen ab Oktober 2026), Brasilien (ab iOS 26.5, Juni 2026) und Japan (Smartphone-Gesetz seit Dezember 2025) prüft Review, ob ein Link-out nur dort erscheint, wo er erlaubt ist, und ob das passende Entitlement gesetzt ist. Ein weltweit ausgespielter „Günstiger auf unserer Website"-Button ist der häufigste Grund für eine 3.1.1-Ablehnung.
2. **Paywalls ohne vollständige Abo-Angaben.** Fehlender Preis pro Laufzeit, versteckter Verlängerungshinweis, Testphase ohne Angabe, was danach berechnet wird – 3.1.2(c) wird bei fast jeder App mit Abo geprüft.
3. **Verbrauchsgüter, die verfallen.** Gekaufte Coins, Credits oder Tokens mit Ablaufdatum verstoßen gegen 3.1.1 – Apple erkennt das mittlerweile an den Produktbeschreibungen in App Store Connect.
4. **Erzwungene Bewertungen und Datenfreigaben.** „Bewerte uns, um weiterzumachen" oder ein Feature hinter „Kontakte teilen" fällt unter 3.2.2(x) und 3.1.2(a); Review testet das mit einem frischen Account.
5. **Kredit- und Finanz-Apps ohne Lizenznachweis.** 3.2.1(viii), 3.2.2(viii) und 3.2.2(ix) werden hart durchgesetzt: Ohne Lizenz der Finanzinstitution wird nicht diskutiert.
6. **Loot-Boxen ohne Wahrscheinlichkeiten.** Spiele mit Zufallspaketen ohne sichtbare Drop-Rates vor dem Kauf.

## Inhalt

- [3.1 Zahlungen](#31-zahlungen)
  - [3.1.1 In-App-Kauf](#311-in-app-kauf)
  - [3.1.1(a) Links zu anderen Kaufmethoden](#311a-links-zu-anderen-kaufmethoden)
  - [3.1.2 Abonnements](#312-abonnements)
  - [3.1.2(a) Zulässige Nutzung](#312a-zulässige-nutzung)
  - [3.1.2(b) Upgrades, Downgrades, Crossgrades](#312b-upgrades-downgrades-crossgrades)
  - [3.1.2(c) Abo-Informationen](#312c-abo-informationen)
  - [3.1.3 Andere Kaufmethoden](#313-andere-kaufmethoden)
  - [3.1.4 Hardwarespezifische Inhalte](#314-hardwarespezifische-inhalte)
  - [3.1.5 Kryptowährungen](#315-kryptowährungen)
- [3.2 Andere Geschäftsmodellfragen](#32-andere-geschäftsmodellfragen)
  - [3.2.1 Zulässig](#321-zulässig)
  - [3.2.2 Unzulässig](#322-unzulässig)
- [Entscheidungsbaum: Ist dieses Gut digital und in der App konsumiert?](#entscheidungsbaum-ist-dieses-gut-digital-und-in-der-app-konsumiert)
- [Paywall-Prüfung: was auf dem Bildschirm stehen muss](#paywall-prüfung-was-auf-dem-bildschirm-stehen-muss)
- [Paketreferenz React Native / Expo](#paketreferenz-react-native--expo)
- [Kurz-Prüfliste für diesen Abschnitt](#kurz-prüfliste-für-diesen-abschnitt)

---

## 3.1 Zahlungen

### 3.1.1 In-App-Kauf

**Kern der Regel** – Alles, was in der App freigeschaltet und in der App genutzt wird (Features, Premium-Inhalte, Level, Vollversion, Abos, digitale Gutscheine), muss über Apples In-App-Kauf (StoreKit) verkauft werden. Fremde Freischaltmechanismen wie Lizenzschlüssel, QR-Codes, Kryptowährungen oder Zahlungs-SDKs sind für digitale Güter tabu. Gekaufte Guthaben und Spielwährungen dürfen nicht verfallen, Käufe müssen wiederherstellbar sein, Loot-Boxen müssen ihre Wahrscheinlichkeiten vor dem Kauf offenlegen, und die App darf IAP nicht schlechter darstellen als andere Kaufwege. Trinkgelder an den Entwickler und Geschenke von IAP-Gütern an andere Nutzer sind erlaubt, Geschenke können nur an den ursprünglichen Käufer erstattet werden. Kostenlose Testphasen bei Nicht-Abo-Apps laufen über ein Non-Consumable der Preisstufe 0 („14-Tage-Test").

**Risikostufe** – Kritisch. Das ist Apples Provisionsmodell; Review sucht aktiv nach Umgehungen und lehnt ohne Verhandlungsspielraum ab. Wiederholte Verstöße führen zum Programmausschluss.

**Woran du es im Code erkennst**

Swift/Objective-C:
- `import StoreKit`, `Product.purchase(` / `Transaction.currentEntitlements` (StoreKit 2), `SKPaymentQueue`, `SKProductsRequest`, `SKPaymentTransactionObserver` (StoreKit 1).
- Fehlt StoreKit, aber es gibt `PKPaymentRequest`, `STPPaymentSheet`, `BTDropInController`, `PayPalCheckout`, `PayPal`, `Adyen`, `Klarna`, `Checkout.com` in Dateien namens `Paywall`, `Premium`, `Unlock`, `Subscription`, `Shop`, `Store`: Verdacht auf Umgehung.
- Hartcodierte Lizenzschlüssel-Prüfungen: `func validateLicense(`, `licenseKey`, `activationCode`, `redeemCode` mit Netzwerkaufruf an eigenen Server, aber ohne StoreKit-Transaktion.
- Produktbeschreibungen mit „expires", „gültig bis", „verfällt nach" bei Consumables; Datenmodelle wie `struct Coins { let expiresAt: Date }`.
- Fehlende Wiederherstellung: kein `AppStore.sync()` und kein `SKPaymentQueue.default().restoreCompletedTransactions()`.
- Loot-Box-Logik: `func openChest(`, `gacha`, `lootBox`, `rollRarity(` ohne UI-Anzeige der Wahrscheinlichkeiten.

React Native/Expo:
- `react-native-purchases` (RevenueCat), `react-native-iap`, `expo-iap` = sauber. `expo-in-app-purchases` ist veraltet und seit SDK 49 nicht mehr enthalten; markiere es als Wartungsrisiko, nicht als Regelverstoß.
- `@stripe/stripe-react-native`, `react-native-paypal`, `braintree`, `react-native-razorpay`, `@adyen/react-native` in Dateien wie `PaywallScreen.tsx`, `PremiumModal.tsx`, `useSubscription.ts`: Verdacht.
- `Linking.openURL(` oder `WebBrowser.openBrowserAsync(` mit URLs, die `checkout`, `billing`, `subscribe`, `pricing`, `upgrade`, `stripe.com`, `paypal.com`, `lemonsqueezy`, `gumroad`, `paddle` enthalten.
- `WebView` mit `source={{ uri: ...checkout... }}` innerhalb der App.
- Fehlende Wiederherstellung: kein `Purchases.restorePurchases()` bzw. `getAvailablePurchases()`.

**Typische Verstöße**

❌ Stripe-Checkout für Premium-Freischaltung:
```tsx
const unlockPremium = async () => {
  await Linking.openURL('https://example.com/checkout?plan=pro');
};
```
✅ StoreKit über RevenueCat:
```tsx
const { customerInfo } = await Purchases.purchasePackage(pkg);
if (customerInfo.entitlements.active['pro']) setPro(true);
```

❌ Lizenzschlüssel als Freischaltweg:
```swift
if LicenseServer.validate(key: enteredKey) { unlockAllFeatures() }
```
✅ Berechtigung aus der StoreKit-Transaktion ableiten:
```swift
for await result in Transaction.currentEntitlements {
    if case .verified(let tx) = result, tx.productID == "pro" { unlockAllFeatures() }
}
```

❌ Verfallende Coins:
```swift
struct CoinPack { let amount: Int; let validUntil: Date }
```
✅ Guthaben ohne Ablaufdatum, Bonus-Coins aus Aktionen (nicht gekauft) dürfen getrennt verfallen.

❌ Truhe ohne Drop-Rates: Kaufbutton öffnet direkt die Zufallslogik.
✅ Vor dem Kaufbutton eine Tabelle „Legendär 1 %, Episch 9 %, Selten 30 %, Gewöhnlich 60 %".

❌ Mac-App verkauft Plug-ins per Lizenzschlüssel: für den Mac App Store ausdrücklich erlaubt, wenn die Plug-ins außerhalb des Stores erworben und in der App nur aktiviert werden. Nicht fälschlich markieren.

**Prüfliste**
- [ ] Jeder Kaufpfad für digitale Güter endet in StoreKit (1 oder 2) oder einem StoreKit-Wrapper.
- [ ] Kein Zahlungs-SDK (Stripe, PayPal, Braintree, Adyen, Klarna) in Kaufpfaden für digitale Güter.
- [ ] Keine Lizenzschlüssel-, Code- oder QR-Freischaltung (Ausnahme: Mac-App-Store-Plug-ins).
- [ ] Wiederherstellung von Käufen ist im UI erreichbar (`AppStore.sync()`, `restoreCompletedTransactions`, `Purchases.restorePurchases`).
- [ ] Gekaufte Consumables haben kein Ablaufdatum.
- [ ] Loot-Boxen zeigen Wahrscheinlichkeiten vor dem Kauf.
- [ ] Digitale Gutscheine/Gift-Cards nur über IAP; physische dürfen anders bezahlt werden.
- [ ] IAP wird im UI nicht abgewertet („nur im Store teurer", „Apple-Gebühr").
- [ ] Trinkgelder an Entwickler und Geschenke laufen über IAP; Geschenkerstattung nur an Käufer.
- [ ] Testphase bei Nicht-Abo-Apps als Non-Consumable, Preisstufe 0, mindestens 7 Tage.

**Empfohlene Behebung** – StoreKit 2 (`Product`, `Transaction`, `AppStore.sync()`) für native Apps; für Expo `expo-iap` oder `react-native-purchases`; für bare RN `react-native-iap` oder `react-native-purchases`. Serverseitige Prüfung über App Store Server API, nicht über eigene Lizenzserver.

### 3.1.1(a) Links zu anderen Kaufmethoden

**Kern der Regel** – Ob und wie eine App auf Kaufmöglichkeiten außerhalb der App hinweisen darf, hängt von der Storefront ab. In den USA sind Links und Buttons zu externen Kaufseiten für digitale Güter ohne Entitlement zulässig; ein Hinweis auf den Preisunterschied ist erlaubt. Überall sonst braucht es das StoreKit External Purchase Link Entitlement (bzw. das External Purchase Entitlement für alternative Zahlungsabwicklung), das nur für bestimmte Regionen vergeben wird – aktuell EU, Japan, Südkorea, Brasilien und einige weitere. Musikstreaming-Dienste haben ein eigenes Entitlement. Irreführende Angebote, Betrug oder Phishing über solche Links führen zur Entfernung der App und des Entwicklerkontos.

**Regionale Sonderregeln (Stand September 2026)**
- **USA:** Link-out ohne Entitlement, keine Apple-Provision auf externe Käufe, kein Pflicht-Modal. Apple darf aber verlangen, dass der Link nicht irreführend ist. Nur auf der US-Storefront ausspielen, sonst greift die Verbotsregel für alle anderen Storefronts.
- **EU:** Ab 1. Oktober 2026 gelten die neuen Geschäftsbedingungen (Anhang 14 des Developer Program License Agreement): Initial Acquisition Fee, Store Services Fee und 5 % Core Technology Commission statt der alten Core Technology Fee. Externe Angebote dürfen beworben und verlinkt werden (Website, alternativer Marktplatz, andere App, In-App-WebView), die Entitlements `com.apple.developer.storekit.external-purchase-link` bzw. `com.apple.developer.storekit.external-purchase` bleiben Pflicht. Apple verlangt eine klare Offenlegung, dass der Kauf nicht über Apple läuft, und ein Hinweis-Sheet vor dem Verlassen der App (`ExternalPurchaseLink.open` oder Apples Modal-Vorlage).
- **Brasilien:** Seit iOS 26.5 (Juni 2026) sind alternative Marktplätze, alternative Zahlungsabwicklung und Angebote außerhalb der App möglich; Bedingungen stehen in Anhang 12 der Lizenzvereinbarung (inklusive Core Technology Commission). Gleiche Entitlements wie in der EU.
- **Japan:** Seit Dezember 2025 (Mobile Software Competition Act) Link-out und alternative Zahlung mit Entitlement; Hinweis-Sheet Pflicht.
- **Südkorea:** Alternative Zahlungsabwicklung mit Entitlement seit 2022, reduzierte Provision; Link-out nach Apples Regelwerk mit Hinweistext.
- **Niederlande (Dating-Apps):** historische Sonderregel, in die EU-Regelung aufgegangen.
- **Alle anderen Storefronts:** Kein Button, kein Link, kein „Mehr auf unserer Website" mit Kaufbezug.

**Risikostufe** – Kritisch. Review sucht aktiv nach Links mit Kaufbezug und prüft, ob sie regional korrekt ausgeblendet sind. Ein falsch konfiguriertes Entitlement ist zusätzlich ein Build-Fehler.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Entitlements-Datei: `com.apple.developer.storekit.external-purchase-link`, `com.apple.developer.storekit.external-purchase`, `com.apple.developer.storekit.external-link.account` (Reader-Apps, siehe 3.1.3(a)).
- Info.plist: `SKExternalPurchaseLink` (Dictionary Storefront → URL bzw. URL-Array), `SKExternalPurchase` (Array von Storefront-Codes), `SKExternalLinkAccount`.
- Code: `ExternalPurchaseLink.canOpen`, `ExternalPurchaseLink.open(`, `ExternalPurchase.presentNoticeSheet(`, `ExternalPurchaseCustomLink` (iOS 17.5+ EU), `Storefront.current`.
- Verdächtig: `UIApplication.shared.open(url)` / `openURL:` mit Kauf-URLs, `SFSafariViewController` auf `pricing`-Seiten, ohne Storefront-Abfrage.

React Native/Expo:
- `app.json` / `app.config.js`: `ios.entitlements` mit obigen Schlüsseln, `ios.infoPlist.SKExternalPurchaseLink`.
- `Linking.openURL(`, `WebBrowser.openBrowserAsync(`, `InAppBrowser.open(` mit Kauf-URLs; prüfe, ob eine Storefront- oder Länderabfrage davor steht (`Purchases.getCustomerInfo()` liefert keine Storefront; `expo-localization` liefert nur die Geräteregion, nicht die App-Store-Storefront – das reicht Apple nicht).
- RevenueCat: `Purchases.canMakePayments()`, `storefront`-Feld aus `Purchases.getStorefront()` (SDK ≥ 8) als saubere Regionserkennung.
- Native Module oder Config-Plugins, die `ExternalPurchaseLink` bridgen.

**Typische Verstöße**

❌ Globaler Link-out ohne Regionsprüfung:
```tsx
<Button title="Günstiger im Web abonnieren"
        onPress={() => Linking.openURL('https://example.com/subscribe')} />
```
✅ Nur für US-Storefront, sonst StoreKit-Paywall:
```tsx
const sf = await Purchases.getStorefront();   // countryCode: 'USA'
if (sf?.countryCode === 'USA') showExternalOffer(); else showStoreKitPaywall();
```

❌ EU-Link-out ohne Entitlement und ohne Hinweis-Sheet:
```swift
UIApplication.shared.open(URL(string: "https://example.com/eu-checkout")!)
```
✅ StoreKit-API mit Pflicht-Sheet:
```swift
if await ExternalPurchaseLink.canOpen {
    let result = await ExternalPurchaseLink.open()   // zeigt Apples Hinweis
}
```

❌ „Apple nimmt 30 %, deshalb zahlst du hier mehr" in der Paywall – Abwertung von IAP (3.1.1).
❌ Externer Link im Onboarding, der mit Deep-Link direkt zum Bezahlformular springt, ohne dass der Nutzer die App bewusst verlässt.

**Prüfliste**
- [ ] Jeder Link mit Kaufbezug ist an die App-Store-Storefront gebunden (nicht an Geräteregion oder Sprache).
- [ ] Für Nicht-US-Storefronts existiert das passende Entitlement und der Info.plist-Schlüssel.
- [ ] Hinweis-Sheet (Apples Modal oder gleichwertiger Text) erscheint vor dem Verlassen der App, wo Apple es fordert (EU, Japan, Korea, Brasilien).
- [ ] Externe URL entspricht der in Info.plist deklarierten URL (Apple prüft die Domain).
- [ ] Kein Tracking-Parameter, der Apple-Kunden zum Abwandern manipuliert (Apple erlaubt Kampagnen-Parameter, aber keine Täuschung).
- [ ] Keine abwertenden Aussagen über IAP.
- [ ] Storefront-Fallback: Wenn die Storefront nicht ermittelbar ist, wird der Link ausgeblendet.

**Empfohlene Behebung** – `ExternalPurchaseLink` / `ExternalPurchaseCustomLink` aus StoreKit; für RN ein natives Modul oder ein Config-Plugin, das Entitlement und Info.plist setzt, plus Storefront-Abfrage über `Purchases.getStorefront()` (RevenueCat) oder `Storefront.current` per Bridge. Für rein US-basierte Angebote reicht ein Storefront-Gate ohne Entitlement.

### 3.1.2 Abonnements

**Kern der Regel** – Auto-verlängernde Abos sind in allen Kategorien erlaubt, wenn sie fortlaufenden Mehrwert liefern, mindestens sieben Tage laufen und auf allen Geräten des Nutzers funktionieren. Die drei Unterpunkte regeln Inhalte, Wechsel und Transparenz.

**Risikostufe** – Hoch. Abo-Ablehnungen sind Alltag, meist wegen 3.1.2(c).

### 3.1.2(a) Zulässige Nutzung

**Kern der Regel** – Ein Abo muss über die Laufzeit etwas liefern: neue Level, Episoden, Multiplayer-Server, regelmäßige Updates, große Medienbibliotheken, SaaS oder Cloud-Funktionen. Abos dürfen mit Einzelkäufen kombiniert werden und Consumables enthalten. Verboten ist, für bezahlten Inhalt zusätzliche Handlungen zu verlangen (Social-Media-Post, Kontakt-Upload, Check-in), und bestehenden Kunden Funktionen wegzunehmen, die sie bereits gekauft haben, wenn die App auf Abo umstellt. Abo-Betrug (Lockangebote, Bait-and-Switch) führt zur Entfernung. Mobilfunkanbieter dürfen mit Apples Zustimmung Musik-/Video-Abos an Tarife koppeln; Streaming-Game-Abos dürfen über mehrere Apps geteilt werden, wenn niemand doppelt zahlt.

**Risikostufe** – Hoch. Besonders Migration von Einmalkauf zu Abo wird geprüft.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Produkt-IDs mit `.weekly`, `.monthly`, `.yearly`; `Product.SubscriptionInfo`, `SKProduct.subscriptionPeriod`.
- Feature-Gates, die nach Migration alte Non-Consumables ignorieren: `if !hasActiveSubscription { lock() }` ohne Prüfung von `Transaction.currentEntitlements` auf Legacy-Produkte.
- Gates auf soziale Aktionen: `if !didShareOnInstagram`, `contactsGranted`, `didCheckIn` vor Premium-Inhalten.

React Native/Expo:
- RevenueCat `Offerings`, `entitlements.active`; `react-native-iap` `getSubscriptions(`, `requestSubscription(`.
- Paywall-Komponenten, die Abo-Status mit Berechtigungsanfragen koppeln (`Contacts.requestPermissionsAsync` unmittelbar vor `purchasePackage`).
- Migration: `AsyncStorage`-Flag `legacyPro` wird nicht mehr ausgewertet.

**Typische Verstöße**

❌ Alte Käufer werden nach Abo-Umstellung ausgesperrt:
```swift
let isPro = subscriptionActive   // ignoriert früheren Einmalkauf "pro.lifetime"
```
✅ Legacy-Käufe weiter honorieren:
```swift
let isPro = subscriptionActive || ownedProducts.contains("pro.lifetime")
```

❌ „Teile die App mit 3 Freunden, um die Premium-Woche freizuschalten" innerhalb eines bezahlten Abos.
❌ Abo für eine statische Taschenlampen-App ohne laufenden Mehrwert.

**Prüfliste**
- [ ] Das Abo liefert erkennbar fortlaufenden Mehrwert (Inhalte, Dienst, Cloud).
- [ ] Mindestlaufzeit 7 Tage; keine Tages-Abos.
- [ ] Legacy-Einmalkäufe werden nach Abo-Umstellung weiter freigeschaltet.
- [ ] Keine zusätzlichen Pflichthandlungen für bezahlte Inhalte.
- [ ] Abo gilt auf allen Geräten (Entitlement-Sync über Apple-ID oder eigenes Konto).

**Empfohlene Behebung** – Entitlement-Ermittlung über `Transaction.currentEntitlements` inklusive aller Legacy-Produkt-IDs; bei RevenueCat Legacy-Produkte demselben Entitlement zuordnen.

### 3.1.2(b) Upgrades, Downgrades, Crossgrades

**Kern der Regel** – Nutzer müssen zwischen Abo-Stufen wechseln können, ohne versehentlich zwei Abos für dasselbe Angebot zu bezahlen. Das erreicht man durch eine gemeinsame Abo-Gruppe in App Store Connect mit korrekter Rangfolge.

**Risikostufe** – Mittel. Review testet gelegentlich den Wechsel; häufiger fällt es durch Nutzerbeschwerden auf.

**Woran du es im Code erkennst**
- Swift: mehrere Abo-Produkte, die per `Product.purchase(` unabhängig gekauft werden, ohne `subscription.subscriptionGroupID` zu vergleichen; keine Nutzung von `Product.SubscriptionInfo.Status` zum Erkennen bereits aktiver Stufen.
- RN: RevenueCat kümmert sich um Gruppen, aber prüfe, ob die Paywall bereits aktive Pakete als „kaufen" anbietet (`customerInfo.activeSubscriptions` wird nicht ausgewertet). Bei `react-native-iap` unter iOS greift die Abo-Gruppe automatisch, sofern alle Produkte in derselben Gruppe liegen.

**Typische Verstöße**
❌ Monats- und Jahresabo in getrennten Abo-Gruppen; Nutzer kann beides gleichzeitig haben.
❌ Paywall zeigt „Jahresabo kaufen", obwohl das Jahresabo aktiv ist.
✅ Eine Abo-Gruppe, Paywall blendet aktive Stufe aus und beschriftet den Wechsel als „Wechseln zu …".

**Prüfliste**
- [ ] Alle Stufen desselben Angebots liegen in einer Abo-Gruppe.
- [ ] Aktive Stufe wird in der Paywall erkannt und nicht erneut verkauft.
- [ ] Wechsel-Buttons sind als Upgrade/Downgrade beschriftet.

**Empfohlene Behebung** – Abo-Gruppe in App Store Connect, `Product.SubscriptionInfo.Status` bzw. `customerInfo.activeSubscriptions` auswerten.

### 3.1.2(c) Abo-Informationen

**Kern der Regel** – Vor dem Kauf muss der Nutzer klar sehen, was er bekommt (Menge pro Zeitraum, Speicher, Zugang), was es kostet, wie lange die Laufzeit ist, dass sich das Abo automatisch verlängert und wie eine Testphase in ein bezahltes Abo übergeht. Das gilt für die Paywall selbst, nicht nur für die App-Store-Beschreibung. Die genauen Formulierungen richten sich nach Schedule 2 der Entwicklervereinbarung.

**Risikostufe** – Hoch. Die häufigste Abo-Ablehnung überhaupt.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Paywall-Views (`PaywallView.swift`, `SubscriptionViewController`): Suche nach `displayPrice`, `subscriptionPeriod`, `introductoryOffer`, `Text("`… mit „pro Monat", „verlängert sich", „kündigen". Fehlen diese Strings, ist die Paywall vermutlich unvollständig.
- Hartcodierte Preise (`"4,99 €"`) statt `product.displayPrice` – falsch für andere Storefronts.
- `SubscriptionStoreView` (StoreKit 2, iOS 17+) rendert die Pflichtangaben weitgehend selbst; prüfe nur, ob `subscriptionStoreControlStyle` und Datenschutz/AGB-Links gesetzt sind.

React Native/Expo:
- `PaywallScreen.tsx`, `Paywall.tsx`, `SubscribeModal.tsx`: Preis aus `package.product.priceString` bzw. `subscription.localizedPrice`, Laufzeit aus `product.subscriptionPeriod`, Intro-Angebot aus `product.introPrice`.
- RevenueCat Paywalls (`react-native-purchases-ui`, `<Paywall />`) liefern die Angaben aus dem Dashboard-Template; prüfe, ob das Template die Verlängerungsinfo enthält.
- Testphasen-Text: „7 Tage kostenlos" ohne „danach 9,99 €/Monat".

**Typische Verstöße**

❌ Nur der Aktionspreis:
```tsx
<Text>7 Tage kostenlos testen</Text>
<Button title="Jetzt starten" onPress={buy} />
```
✅ Vollständige Angabe:
```tsx
<Text>7 Tage kostenlos, danach {pkg.product.priceString}/Monat.
Verlängert sich automatisch, kündbar jederzeit in den Einstellungen.</Text>
```

❌ Jahrespreis als „nur 0,83 €/Monat" ohne den tatsächlich abgebuchten Jahresbetrag.
❌ Verlängerungshinweis nur in der App-Store-Beschreibung, nicht in der Paywall.
❌ Links zu Nutzungsbedingungen und Datenschutzerklärung fehlen auf der Paywall (Schedule 2 verlangt sie).

**Prüfliste**
- [ ] Preis pro Abrechnungszeitraum, lokalisiert aus StoreKit, nicht hartcodiert.
- [ ] Laufzeit (Woche/Monat/Jahr) explizit genannt.
- [ ] Hinweis auf automatische Verlängerung und Kündigungsweg.
- [ ] Testphase: Dauer, Preis danach, Zeitpunkt der ersten Abbuchung.
- [ ] Bei Jahrespreis mit Monatsumrechnung: der abgebuchte Gesamtbetrag ist ebenfalls sichtbar.
- [ ] Links zu Nutzungsbedingungen (EULA) und Datenschutzerklärung auf der Paywall.
- [ ] Inhalt des Abos (was ist drin) ist beschrieben.

**Empfohlene Behebung** – `SubscriptionStoreView` (SwiftUI) oder RevenueCat Paywalls (`react-native-purchases-ui`) verwenden; sonst eigene Paywall nach der Tabelle im Abschnitt „Paywall-Prüfung" aufbauen.

### 3.1.3 Andere Kaufmethoden

**Kern der Regel** – Für bestimmte Kategorien verlangt Apple keinen IAP. Die Buchstaben (a) bis (g) sind abschließend; alles, was nicht darunter fällt, gehört zu 3.1.1.

**Risikostufe** – Hoch. Die Einordnung ist oft strittig; Review entscheidet nach der Frage, wo das Gut konsumiert wird.

#### 3.1.3(a) Reader-Apps

**Kern** – Apps, die zuvor anderswo gekaufte Inhalte anzeigen (Zeitschriften, Zeitungen, Bücher, Audio, Musik, Video), dürfen ohne IAP auskommen, Konten anlegen und verwalten. Mit dem External Link Account Entitlement dürfen sie einen Link zur eigenen Website setzen; auf der US-Storefront ist dafür kein Entitlement nötig. Die Kategorie ist eng: Reine Inhalte-Apps, kein SaaS, keine Kurse mit Interaktion.

**Erkennung** – Entitlement `com.apple.developer.storekit.external-link.account`, Info.plist `SKExternalLinkAccount`, API `ExternalLinkAccount.open()`. In RN: gleiche Schlüssel in `ios.entitlements`, Aufruf per Bridge.

**Prüfliste**
- [ ] Die App verkauft nichts in der App und zeigt keine Kaufaufforderung („Abo abschließen unter …").
- [ ] Bei Link zur Website ist das Entitlement gesetzt (außer US) und der Link ist rein informativ.
- [ ] Inhaltstyp passt zur Reader-Definition (Medien, nicht Software).

#### 3.1.3(b) Multiplattform-Dienste

**Kern** – Was auf anderen Plattformen oder im Web gekauft wurde, darf in der iOS-App genutzt werden, auch Consumables, sofern dieselben Güter auch als IAP angeboten werden. Die App darf aber nicht auf den externen Kauf hinweisen oder ihn bewerben.

**Erkennung** – Login-basierte Entitlement-Abfrage (`/api/me/entitlements`) ohne Kauf-UI; Hinweise wie „Auf der Website kaufen" oder „Im Web günstiger" sind der Verstoß.

**Prüfliste**
- [ ] Extern gekaufte Inhalte werden nach Login freigeschaltet.
- [ ] Kein Text, Link oder Deep-Link, der zum Kauf außerhalb der App führt (Ausnahme: Storefront-Regeln aus 3.1.1(a)).
- [ ] Consumables, die extern gekauft werden, sind auch als IAP verfügbar.

#### 3.1.3(c) Enterprise-Dienste

**Kern** – Wird die App an Organisationen verkauft (Schule, Unternehmen) und nutzen deren Mitglieder sie, darf der Kauf außerhalb laufen. Sobald Einzelpersonen oder Familien direkt kaufen können, ist IAP Pflicht.

**Erkennung** – Anmeldung nur mit Organisations-Konto (SSO, Domain-Zwang), kein Self-Service-Kauf; wenn daneben ein „Einzelplan"-Button mit Stripe existiert, kippt die Einordnung.

**Prüfliste**
- [ ] Zugang setzt eine Organisationszugehörigkeit voraus.
- [ ] Kein Endkundenkauf in der App oder per Link aus der App.

#### 3.1.3(d) Person-zu-Person-Dienste

**Kern** – Echtzeit-Dienstleistungen zwischen genau zwei Personen (Nachhilfe, ärztliche Beratung, Immobilienbesichtigung, Personal Training) dürfen außerhalb von IAP bezahlt werden. Sobald ein Anbieter mehrere Teilnehmer gleichzeitig bedient (Gruppenkurs, Livestream mit Chat, Webinar), gilt IAP.

**Erkennung** – Buchungs- und Videocall-Logik: Prüfe die maximale Teilnehmerzahl im Datenmodell (`maxParticipants`, `roomSize`, `Twilio`/`Agora`-Kanäle mit mehr als zwei Teilnehmern). Aufgezeichnete Sessions, die später verkauft werden, sind digitaler Inhalt → IAP.

**Prüfliste**
- [ ] Zahlung außerhalb von IAP nur bei 1:1 in Echtzeit.
- [ ] Gruppenformate und Aufzeichnungen laufen über IAP.
- [ ] Plattform verkauft keine „Credits" für 1:1-Sitzungen als Vorratsguthaben, das auch für Gruppenformate gilt.

#### 3.1.3(e) Waren und Dienstleistungen außerhalb der App

**Kern** – Physische Waren und Dienstleistungen, die außerhalb der App konsumiert werden (Kleidung, Lieferessen, Taxi, Handwerker), müssen mit anderen Zahlungsmitteln bezahlt werden: Apple Pay, Kreditkarte, PayPal usw. Hier wäre IAP sogar falsch.

**Erkennung** – Positiv: `PKPaymentAuthorizationViewController`, `@stripe/stripe-react-native`, `expo-apple-pay`-Wrapper in Checkout-Flows für Warenkörbe. Negativ: Ein Shop, der zusätzlich digitale Zusatzleistungen (Premium-Mitgliedschaft mit App-Funktionen, digitale Gutscheine) über Stripe verkauft.

**Prüfliste**
- [ ] Physische Güter/Dienste laufen nicht über IAP.
- [ ] Gemischte Warenkörbe trennen digitale Zusätze (IAP) von physischen Posten.
- [ ] Apple Pay wird korrekt konfiguriert (Merchant-ID, `com.apple.developer.in-app-payments`).

#### 3.1.3(f) Kostenlose Stand-alone-Companion-Apps

**Kern** – Eine kostenlose App, die als Begleiter zu einem bezahlten Web-Dienst dient (VoIP, Cloud-Speicher, E-Mail, Hosting), braucht keinen IAP, solange sie selbst nichts verkauft und keine Kaufaufforderung enthält.

**Erkennung** – Kein StoreKit, keine Paywall, aber auch keine Strings wie „Upgrade auf der Website", „Plan erweitern", `Linking.openURL('.../billing')`.

**Prüfliste**
- [ ] Keine Kauf- oder Upgrade-Aufforderung in der App.
- [ ] Alle Funktionen sind mit dem extern erworbenen Konto nutzbar.

#### 3.1.3(g) Werbemanagement-Apps

**Kern** – Apps, mit denen Werbetreibende Kampagnen über verschiedene Medien buchen und verwalten, brauchen keinen IAP für das Werbebudget. Aber: Wird etwas gekauft, das in der App selbst wirkt (Post-Boost, Reichweite für das eigene Profil in derselben App), ist das IAP.

**Erkennung** – Boost-Buttons in Social-Apps mit Stripe-Checkout; `promotePost(`, `boostProfile(` mit externem Payment.

**Prüfliste**
- [ ] Kampagnenbudget für externe Medien: keine IAP-Pflicht.
- [ ] Boosts, Hervorhebungen, Reichweite innerhalb der App: IAP.

**Empfohlene Behebung (gesamt 3.1.3)** – Einordnung dokumentieren und in den Review-Notizen begründen; bei Mischformen die digitalen Anteile auf StoreKit umstellen. Für physische Güter Apple Pay über `PassKit` bzw. `@stripe/stripe-react-native` mit Apple-Pay-Unterstützung.

### 3.1.4 Hardwarespezifische Inhalte

**Kern der Regel** – Funktionen, die nur mit bestimmter Hardware funktionieren (Smart-Home-Gerät, Kamera, Sensor), dürfen ohne IAP freigeschaltet werden. Arbeitet die App mit optionalem, von Apple zugelassenem Zubehör (MFi, HomeKit), darf das Zubehör Funktionen freischalten, sofern dieselben Funktionen auch per IAP erhältlich sind. Die App darf nicht den Kauf unabhängiger Produkte oder die Teilnahme an Werbung zur Bedingung machen.

**Risikostufe** – Mittel. Betrifft nur Hardware-Hersteller; dort aber regelmäßig wegen fehlender IAP-Alternative.

**Woran du es im Code erkennst**
- Swift: `ExternalAccessory` (`EAAccessoryManager`), `CoreBluetooth`-Scan mit Seriennummer-Check, `HomeKit`; Freischaltlogik `if accessory.serialNumber.hasPrefix("XYZ") { unlockPro() }`.
- RN: `react-native-ble-plx`, `react-native-ble-manager`, `expo-bluetooth`-Wrapper; gleiche Freischaltmuster.

**Typische Verstöße**
❌ Premium-Funktionen nur nach Kauf eines Zubehörs, obwohl sie ohne Hardware nutzbar wären und kein IAP existiert.
❌ „Registriere das Gerät und abonniere unseren Newsletter, um alle Funktionen zu nutzen."
✅ Funktion X wird durch Gerät Y freigeschaltet und ist alternativ als Non-Consumable kaufbar.

**Prüfliste**
- [ ] Hardware-Freischaltung betrifft nur Funktionen, die ohne die Hardware keinen Sinn ergeben, oder es gibt eine IAP-Alternative.
- [ ] Keine Kopplung an unabhängige Produkte oder Marketing-Teilnahme.

### 3.1.5 Kryptowährungen

**Kern der Regel** – Krypto ist erlaubt, aber unter Bedingungen: (i) Wallets nur von Entwicklern, die als Organisation eingeschrieben sind; (ii) kein Mining auf dem Gerät, Cloud-Mining ist zulässig; (iii) Handel nur auf zugelassenen Börsen und nur in Ländern mit entsprechender Lizenz; (iv) ICOs, Krypto-Futures und tokenisierte Wertpapiere nur von Banken, Wertpapierfirmen oder anderen zugelassenen Finanzinstituten; (v) keine Krypto-Belohnung für Aufgaben wie App-Downloads, Empfehlungen oder Social-Posts. NFTs dürfen angezeigt und über IAP gemintet, gelistet oder übertragen werden; NFT-Besitz darf keine Features freischalten (außer US-Storefront mit Link-out).

**Risikostufe** – Hoch. Apple prüft Lizenzstatus und Entwicklertyp; Mining-Code ist ein sofortiges Ablehnungskriterium.

**Woran du es im Code erkennst**

Swift/Objective-C:
- Wallet-Bibliotheken: `web3swift`, `WalletCore` (Trust), `BitcoinKit`, `Solana.swift`; Schlüsselgenerierung `HDWallet`, `Mnemonic`.
- Mining: `hashrate`, `stratum+tcp://`, `cryptonight`, `randomx`, `Metal`-Compute-Kernels mit Hash-Schleifen, `ProcessInfo.processInfo.thermalState` in Hash-Loops.
- Börse: Endpunkte `/order`, `/trade`, `binance`, `coinbase` API; `WKWebView` auf Trading-Seiten.
- Belohnungen: `rewardTokens(for: .appInstall)`, `referralBonus` in Token-Einheiten.
- NFT-Gating: `if ownsNFT(contract:) { unlock() }`.

React Native/Expo:
- `ethers`, `web3`, `@solana/web3.js`, `@walletconnect/react-native-compat`, `react-native-get-random-values` + `bip39`.
- Mining-Skripte in `WebView` (`coinhive`-Nachfolger, `injectedJavaScript` mit Hash-Loops).
- `expo-task-manager`-Hintergrundtasks mit Hash-Berechnungen.

**Typische Verstöße**
❌ Wallet-App eingereicht über ein Individual-Entwicklerkonto.
❌ „Verdiene 5 Token pro geworbenem Freund" in einer Krypto-App.
❌ Hintergrund-Task, der „Proof of Work" für ein Netzwerk rechnet.
✅ NFT-Galerie zeigt eigene Token, Minting läuft als Consumable-IAP.

**Prüfliste**
- [ ] Wallet-Funktion nur bei Organisation-Konto (Review-Notizen: Nachweis).
- [ ] Kein Mining auf dem Gerät (nativ, Metal oder WebView).
- [ ] Handel nur über lizenzierte Börsen, geografisch eingeschränkt.
- [ ] ICO/Futures/Token-Wertpapiere nur mit Finanzlizenz (Nachweis in Review-Notizen).
- [ ] Keine Krypto-Prämien für Downloads, Referrals oder Social-Aktionen.
- [ ] NFT-Besitz schaltet keine Features frei (außer US mit Link-out).

**Empfohlene Behebung** – Lizenzunterlagen und Entwicklertyp in den Review-Notizen belegen; Mining-Code entfernen; Belohnungsprogramme auf nicht-monetäre Anreize umstellen.

---

## 3.2 Andere Geschäftsmodellfragen

### 3.2.1 Zulässig

**Kern der Regel** – Apple listet Geschäftsmodelle, die trotz Nähe zu Grenzfällen erlaubt sind. Jedes hat eine Bedingung.

**Risikostufe** – Mittel bis Hoch je nach Punkt; (vi) und (viii) verlangen Nachweise.

**(i) Eigenwerbung** – Die App darf eigene andere Apps anzeigen und bewerben, solange sie nicht bloß ein Katalog ist.
- Erkennung: `SKOverlay`, `SKStoreProductViewController`, `StoreKit`-`AppStore.showProductPage` nur für eigene Bundle-IDs; RN: `react-native-store-view` oder `Linking.openURL('itms-apps://...')`.
- [ ] Beworbene Apps stammen vom selben Entwickler; die App hat eigenständigen Nutzen.

**(ii) App-Sammlungen** – Kuratierte Listen fremder Apps sind nur für zugelassene Zwecke (Gesundheit, Luftfahrt, Barrierefreiheit) und nur mit substanziellem redaktionellem Inhalt erlaubt.
- [ ] Sammlung hat Redaktionsinhalt (Rezensionen, Bewertungslogik), ist kein Store-Ersatz.

**(iii) Ablauf von Leihinhalten** – Filme, Serien, Musik und Bücher dürfen als Leihe nach Ablauf gesperrt werden. Alles andere darf nicht verfallen.
- Erkennung: `rentalExpiresAt`, `expiresAt` an Medienobjekten (ok) vs. an Coins, Features, Sticker-Paketen (Verstoß, siehe 3.1.1).
- [ ] Ablaufdaten existieren nur an Leihmedien.

**(iv) Wallet-Pässe** – Tickets, Coupons, Ausweise, Treuekarten dürfen als Pässe ausgegeben werden, auch mit Zahlungsfunktion.
- Erkennung: `PKPass`, `PKAddPassesViewController`, Entitlement `com.apple.developer.pass-type-identifiers`; RN: `react-native-passkit-wallet`, `expo-passkit`-Community-Pakete.
- [ ] Pass-Type-ID und Zertifikat vorhanden; Pass ist Ticket/Coupon/Ausweis, kein Ersatz für IAP-Freischaltung.

**(v) Versicherungs-Apps** – Müssen kostenlos sein, gesetzeskonform, und dürfen kein IAP verwenden.
- [ ] App ist kostenlos, Vertragsabschluss läuft über regulierte Zahlwege, kein StoreKit-Produkt.

**(vi) Zugelassene gemeinnützige Organisationen** – Von Apple zugelassene Non-Profits dürfen in der eigenen App Spenden sammeln, auch über Drittplattformen, sofern Apple Pay unterstützt wird. Pflicht: Verwendungszweck offenlegen, Recht einhalten, Spendenquittung anbieten. Spendenplattformen müssen die Zulassung jeder Organisation prüfen.
- Erkennung: `PKPaymentRequest` mit `merchantCapabilities` in `DonateView`, Stripe/PayPal-Donate-Flows, `donation`-Endpunkte.
- [ ] Organisation ist bei Apple als Non-Profit zugelassen (Nachweis in Review-Notizen).
- [ ] Apple Pay wird angeboten.
- [ ] Verwendungszweck und Quittung sind in der App sichtbar.

**(vii) Geldgeschenke zwischen Personen** – Erlaubt ohne IAP, wenn das Geschenk völlig freiwillig ist und 100 % beim Empfänger ankommen. Sobald das Geschenk an digitalen Inhalt oder eine Leistung gekoppelt ist (Sticker, Livestream-Gimmicks, Creator-Abos), gilt IAP.
- Erkennung: `tipCreator(`, `sendGift(`, `platformFee`, `commission` in Trinkgeld-Flows; Stripe Connect mit `application_fee_amount`.
- [ ] Keine Plattformgebühr, kein Mindestbetrag, keine Gegenleistung.
- [ ] Virtuelle Geschenke (Sticker, Animationen, Ränge) laufen über IAP.

**(viii) Finanzdienstleistungen** – Trading-, Investment- und Geldverwaltungs-Apps müssen vom lizenzierten Finanzinstitut selbst eingereicht werden.
- Erkennung: Broker-APIs (`alpaca`, `tradier`, `interactive brokers`), Konto-Eröffnung mit KYC (`onfido`, `veriff`, `jumio`), Order-Buchung.
- [ ] Entwicklerkonto gehört der lizenzierten Institution, nicht der Agentur.
- [ ] Lizenznachweis in den Review-Notizen.

**Typische Verstöße**
❌ Trinkgeld-Flow für Creator mit 10 % Plattformgebühr über Stripe.
✅ Trinkgeld über Stripe Connect mit 0 % Fee, oder als IAP-Consumable mit Apple-Provision.
❌ Spenden-Button in einer App einer nicht zugelassenen Organisation.
✅ Verlinkung zur Website (Safari) für Spenden, App bleibt kostenlos.

### 3.2.2 Unzulässig

**Kern der Regel** – Geschäftsmodelle, die Apple grundsätzlich ablehnt. Zwei Nummern sind gestrichen.

**Risikostufe** – Kritisch für (i), (viii), (ix), (x); Hoch für (iii), (iv), (vii); Mittel für (v).

**(i) App-Store-ähnliche Oberflächen** – Keine Storefront für fremde Apps, Erweiterungen oder Plug-ins, keine allgemeinen App-Sammlungen.
- Erkennung: Listen mit `bundleId`, `itms-apps://`, `appStoreUrl` über viele Fremd-Apps; Kategorien-Navigation, Suchfeld, „Installieren"-Buttons.
- [ ] Keine Katalog-UI für fremde Apps.

**(ii) entfällt (von Apple gestrichen).**

**(iii) Werbe-Manipulation** – Keine künstlichen Ad-Impressions oder Klicks; keine Apps, deren Hauptzweck das Anzeigen von Werbung ist.
- Erkennung: Auto-Refresh von Banner-Views in kurzen Intervallen (`Timer.scheduledTimer(withTimeInterval: 2`), unsichtbare `GADBannerView` (alpha 0, off-screen), `injectedJavaScript`-Klicksimulation, Reward-Loops ohne Inhalt.
- RN: `react-native-google-mobile-ads` mit `setInterval` auf `load()`, `pointerEvents="none"` über Ads mit `opacity: 0`.
- [ ] Ads sind sichtbar, nicht automatisch geklickt, App hat eigenen Nutzen.

**(iv) Unautorisierte Spendensammlung** – Spenden in der App nur nach 3.2.1(vi). Andere Fundraising-Apps müssen kostenlos sein und Geld ausschließlich außerhalb der App (Safari, SMS) einsammeln.
- Erkennung: `DonateButton` mit Stripe/PayPal ohne Non-Profit-Zulassung; `PKPaymentRequest` in Spendenflows.
- [ ] Ohne Zulassung: Spenden nur per `UIApplication.open(safariURL)` / `Linking.openURL`, kein In-App-Payment.

**(v) Willkürliche Nutzerbeschränkung** – Keine Sperre nach Standort oder Mobilfunkanbieter ohne sachlichen Grund (Lizenzgebiete sind ein Grund, „nur Telekom-Kunden" ohne Vertragsbezug nicht).
- Erkennung: `CTCarrier`, `CTTelephonyNetworkInfo` (deprecated) in Zugangsprüfungen; `CLLocationManager` als Login-Gate; RN: `react-native-device-info` `getCarrier()` vor `AccessDenied`.
- [ ] Regionale/Carrier-Sperren sind sachlich begründet (Lizenz, Vertrag), nicht willkürlich.

**(vi) entfällt (von Apple gestrichen).**

**(vii) Künstliche Status-Manipulation** – Keine Apps, die Rankings, Bewertungen, Follower oder Sichtbarkeit auf fremden Diensten künstlich pushen, es sei denn, der Dienst hat das erlaubt.
- Erkennung: „Follower kaufen", „Likes boosten", „Bewertungen generieren", Automatisierung von Instagram/TikTok/App-Store-APIs, `rating-bot`, Review-Tausch-Gruppen.
- [ ] Keine Kauf- oder Tauschmechanik für Follower, Likes, Rezensionen, Rankings.

**(viii) Derivatehandel** – Binäre Optionen sind komplett verboten (Web-App empfohlen). CFDs, FOREX und andere Derivate nur mit Lizenz in jeder angebotenen Jurisdiktion.
- Erkennung: Strings `binary option`, `Binäre Option`, `call/put in 60s`, `high/low`; CFD-/Forex-Broker-SDKs; Storefront-Liste ohne Lizenzabgleich.
- [ ] Keine binären Optionen.
- [ ] CFD/Forex: Lizenz je Storefront in Review-Notizen, Storefront-Liste eingeschränkt.

**(ix) Kredit-Apps** – Persönliche Kredite müssen alle Bedingungen offenlegen (maximaler effektiver Jahreszins, Fälligkeit). Der effektive Jahreszins darf inklusive aller Kosten 36 % nicht überschreiten, und die vollständige Rückzahlung darf nicht innerhalb von 60 Tagen oder weniger verlangt werden.
- Erkennung: `apr`, `interestRate`, `loanTerm`, `repaymentDays`, `dueInDays` im Modell; Konstanten wie `MAX_APR = 0.99` oder `term: 14` (Payday-Muster); Strings „Sofortkredit", „Vorschuss", „Payday".
- ❌ `let termDays = 30; let apr = 0.72`
- ✅ `let minTermDays = 61; precondition(apr <= 0.36)` plus vollständige Kostenanzeige vor Abschluss.
- [ ] APR ≤ 36 % inklusive Gebühren, im Code und in der UI.
- [ ] Rückzahlungsfrist > 60 Tage.
- [ ] Alle Konditionen vor Abschluss sichtbar (APR, Gebühren, Fälligkeitsdatum).

**(x) Erzwungene Handlungen** – Die App darf Funktionen oder Inhalte nicht davon abhängig machen, dass der Nutzer die App bewertet, eine Rezension schreibt, eine andere App lädt oder eine ähnliche Store-Aktion ausführt. Belohnungen für Handlungen innerhalb der App (Level schaffen, Werbevideo ansehen) sind erlaubt. In Kombination mit 3.1.2(a) gilt: auch Datenfreigaben (Kontakte, Standort, Tracking) dürfen keine Bedingung für bezahlte oder kostenlose Inhalte sein, wenn sie für die Funktion nicht nötig sind.
- Erkennung Swift: `SKStoreReviewController.requestReview` / `AppStore.requestReview` vor einem Gate; eigene Rating-Dialoge mit „Später" ausgegraut; `if !hasRated { return }`; `if !didInstallPartnerApp`; `CNContactStore.requestAccess` als Bedingung für Feature; `ATTrackingManager.requestTrackingAuthorization` mit Gate bei Ablehnung.
- Erkennung RN: `expo-store-review` / `react-native-rate` in Feature-Gates; `AsyncStorage.getItem('hasRated')` vor Unlock; `Contacts.requestPermissionsAsync` mit `if (status !== 'granted') return <Locked />`; `requestTrackingPermissionsAsync` mit Sperre bei Ablehnung.
- ❌ `if (!hasRated) { navigation.navigate('RateFirst'); return; }`
- ✅ Bewertungsanfrage über `StoreReview.requestReview()` nach einem Erfolgsmoment, ohne Konsequenz bei Ablehnung.
- [ ] Keine Bewertungs-, Download- oder Store-Aktion als Zugangsvoraussetzung.
- [ ] Eigene Rating-Dialoge haben einen echten Ablehnen-Weg.
- [ ] Datenfreigaben (Kontakte, Tracking, Standort) sind keine Bedingung für Inhalte, die sie nicht benötigen.
- [ ] Belohnungen nur für In-App-Handlungen (Level, Rewarded Ad).

**Empfohlene Behebung (gesamt 3.2.2)** – Rating über `StoreReview.requestReview()` (Expo `expo-store-review`, bare `react-native-store-review`) ohne Gate; Spenden über Safari-Link; Kreditkonditionen serverseitig auf 36 %/61 Tage begrenzen und in der UI anzeigen; Binäroptionen entfernen.

---

## Entscheidungsbaum: Ist dieses Gut digital und in der App konsumiert?

Gehe den Baum für jedes Produkt, jeden Button und jeden Link mit Kaufbezug durch. Das Ergebnis bestimmt die Regel.

```
Wird für etwas Geld verlangt (Preis, Abo, Trinkgeld, Spende, Credits)?
│
├─ Nein → kein 3.1-Thema. Prüfe 3.2.2(x) (erzwungene Handlungen).
│
└─ Ja → Ist das Gut physisch oder wird es außerhalb der App erbracht?
    │   (Ware, Lieferung, Taxi, Handwerker, Hotel, Ticket für reales Event)
    │
    ├─ Ja → 3.1.3(e): KEIN IAP. Apple Pay, Karte, PayPal.
    │        Enthält der Warenkorb digitale Zusätze (App-Features, digitaler
    │        Gutschein, Sticker)? → diese Posten separat über IAP.
    │
    └─ Nein, digital → Wird es in dieser App genutzt/erlebt?
        │
        ├─ Nein, nur außerhalb (z. B. Kampagnenbudget für Fremdmedien)
        │     → 3.1.3(g), kein IAP.
        │
        └─ Ja → Ist es eine Echtzeit-Leistung zwischen genau zwei Menschen?
            │
            ├─ Ja (1:1 Tutoring, Arztgespräch, Training) → 3.1.3(d), kein IAP.
            │     1:n oder Aufzeichnung → IAP.
            │
            └─ Nein → Ist es ein freiwilliges Geldgeschenk an eine Person,
                │      100 % ohne Abzug, ohne Gegenleistung?
                │
                ├─ Ja → 3.2.1(vii), kein IAP nötig.
                │     Gegenleistung/Sticker/Rang → IAP.
                │
                └─ Nein → Ist es eine Spende an eine von Apple zugelassene
                    │      gemeinnützige Organisation?
                    │
                    ├─ Ja → 3.2.1(vi), Apple Pay Pflicht, kein IAP.
                    │     Nicht zugelassen → nur Safari-Link (3.2.2(iv)).
                    │
                    └─ Nein → Wurde es bereits außerhalb gekauft und wird
                        │      hier nur genutzt?
                        │
                        ├─ Ja, ohne jede Kaufaufforderung in der App
                        │     → 3.1.3(a) Reader / (b) Multiplattform /
                        │       (c) Enterprise / (f) Companion – kein IAP.
                        │       Jeder Hinweis „kaufe auf der Website" →
                        │       zurück zu 3.1.1(a) Storefront-Regeln.
                        │
                        └─ Nein, der Kauf findet in der App statt
                              → 3.1.1: StoreKit PFLICHT.
                                Einmalig → Non-Consumable / Consumable.
                                Laufend  → Auto-Renewable (3.1.2).
                                Link-out nur nach 3.1.1(a) je Storefront.
```

Hinweise für Grenzfälle:
- **Hybrid-Kurse** (Video-on-Demand plus Live-Gruppencall): digitaler Inhalt in der App → IAP.
- **Coaching-App mit 1:1-Calls und Übungsbibliothek:** Calls extern zahlbar, Bibliothek IAP; ein Kombi-Abo, das beides enthält, ist IAP.
- **Ticket für reales Konzert:** physisch/außerhalb → kein IAP; dasselbe Konzert als Stream → IAP.
- **Credits, die für beides gelten:** gilt als digital → IAP.
- **Software-Lizenz für die macOS-Desktop-Version, in der iOS-App gekauft:** digital, außerhalb dieser App genutzt – Apple stuft das dennoch als IAP-pflichtig ein, wenn die iOS-App den Kauf abwickelt.

---

## Paywall-Prüfung: was auf dem Bildschirm stehen muss

Prüfe jede Paywall (nativ oder RN) gegen diese Tabelle. „Muss" bedeutet: sichtbar ohne Scrollen oder Aufklappen auf dem Kaufbildschirm selbst.

| Element | Pflicht | Quelle | Häufiger Fehler |
|---|---|---|---|
| Name des Abos / Produkts | Muss | `product.displayName` / `product.title` | Nur „Premium" ohne Nennung, was enthalten ist |
| Leistungsbeschreibung (was ist drin) | Muss | eigener Text | Stichworte fehlen, nur Emojis |
| Preis pro Abrechnungszeitraum, lokalisiert | Muss | `product.displayPrice` / `priceString` / `localizedPrice` | Hartcodierte Euro-Preise |
| Laufzeit (Woche/Monat/Jahr) | Muss | `subscriptionPeriod` | „pro Monat" bei Jahresabo mit Umrechnung, ohne Jahresbetrag |
| Gesamtbetrag der Abbuchung | Muss bei Umrechnung | berechnet | „0,83 €/Monat" ohne „9,99 €/Jahr" |
| Hinweis auf automatische Verlängerung | Muss | eigener Text | Nur in App-Store-Beschreibung |
| Kündigungsweg | Muss | eigener Text („in den Einstellungen der Apple-ID") | Fehlt komplett |
| Testphase: Dauer, Preis danach, Startzeitpunkt der Abbuchung | Muss, wenn Trial | `introductoryOffer` / `introPrice` | „7 Tage gratis" allein |
| Einführungsangebot: Dauer der Vergünstigung und Normalpreis danach | Muss, wenn Intro-Offer | `introductoryOffer.period` | Nur der Aktionspreis |
| Link Nutzungsbedingungen (EULA) | Muss | Apple-Standard-EULA oder eigene | Fehlt oder tot |
| Link Datenschutzerklärung | Muss | eigene URL | Fehlt |
| „Käufe wiederherstellen" | Muss (irgendwo erreichbar, idealerweise auf der Paywall) | `AppStore.sync()` / `restorePurchases()` | Nur in tiefen Einstellungen |
| Schließen-Möglichkeit | Muss (Hard-Paywalls sind erlaubt, aber ein Weg zurück zur Free-Version muss existieren, wenn es eine gibt) | UI | X-Button erst nach 5 s, ohne Kontrast |
| Kein Countdown-Druck, keine falsche Verknappung | Muss | UI | „Nur noch 3 Minuten!" für ein Standardangebot |
| Keine Abwertung von IAP | Muss | UI-Text | „Apple-Gebühr", „im Web billiger" außerhalb erlaubter Storefronts |
| Externer Kauf-Link | Nur wo 3.1.1(a) erlaubt | Entitlement + Storefront-Gate | Weltweit sichtbar |

Praktische Prüfschritte:
1. Suche die Paywall-Komponenten (`grep -ril "paywall\|subscri\|premium\|upgrade" --include=*.swift --include=*.m --include=*.tsx --include=*.ts`).
2. Prüfe, ob Preise aus StoreKit-Objekten stammen (`displayPrice`, `priceString`, `localizedPrice`), nicht aus Strings.
3. Prüfe, ob die Wörter „verlängert" / „renew", „kündig" / „cancel", „danach" / „then" in der Paywall-Datei oder in ihren Lokalisierungen vorkommen.
4. Prüfe, ob EULA- und Datenschutz-Links vorhanden sind und auf erreichbare URLs zeigen.
5. Prüfe, ob eine Restore-Funktion existiert und von der Paywall aus erreichbar ist.
6. Prüfe bei RevenueCat-Paywalls (`react-native-purchases-ui`, `PaywallView`), ob das Template die Verlängerungsinfo enthält; das Dashboard-Template entscheidet, nicht der Code.
7. Prüfe bei `SubscriptionStoreView`, ob `.subscriptionStorePolicyDestination(for: .privacyPolicy)` und `.termsOfService` gesetzt sind.

---

## Paketreferenz React Native / Expo

| Zweck | Expo | Bare React Native |
|---|---|---|
| In-App-Kauf (StoreKit) | `expo-iap`; `react-native-purchases` (RevenueCat, mit Config-Plugin) | `react-native-iap`; `react-native-purchases` |
| Veraltet, nicht mehr verwenden | `expo-in-app-purchases` (seit SDK 49 entfernt) | – |
| Paywall-UI mit Pflichtangaben | `react-native-purchases-ui` | `react-native-purchases-ui` |
| Käufe wiederherstellen | `Purchases.restorePurchases()`; `expo-iap` `restorePurchases()` | `react-native-iap` `getAvailablePurchases()`; `Purchases.restorePurchases()` |
| Storefront ermitteln (für 3.1.1(a)) | `Purchases.getStorefront()`; natives Modul für `Storefront.current` | `Purchases.getStorefront()`; `react-native-iap` `getStorefront()` |
| Externer Kauf-Link mit Hinweis-Sheet | Config-Plugin für Entitlement + natives Modul auf `ExternalPurchaseLink` | natives Modul auf `ExternalPurchaseLink` / `ExternalPurchaseCustomLink` |
| Externer Konto-Link (Reader-Apps) | Config-Plugin + natives Modul auf `ExternalLinkAccount` | natives Modul auf `ExternalLinkAccount` |
| Apple Pay für physische Güter | `@stripe/stripe-react-native` (Apple Pay aktiviert) | `@stripe/stripe-react-native`; `react-native-payments` |
| Bewertungsanfrage ohne Gate | `expo-store-review` | `react-native-store-review` |
| Wallet-Pässe | Community-Wrapper um PassKit | `react-native-passkit-wallet` |
| Eigene Apps bewerben | `expo-store-review`-Link; `Linking.openURL('itms-apps://')` | `react-native-store-view` (SKStoreProductViewController) |
| Zahlungs-SDKs, die in Kaufpfaden für digitale Güter NICHT vorkommen dürfen | `@stripe/stripe-react-native`, `react-native-paypal`, `braintree`, `@adyen/react-native`, `react-native-razorpay`, `WebBrowser.openBrowserAsync` auf Checkout-URLs | dieselben plus `Linking.openURL` auf Checkout-URLs |

---

## Kurz-Prüfliste für diesen Abschnitt

**3.1.1 In-App-Kauf**
- [ ] Jeder Kaufpfad für digitale Güter endet in StoreKit oder einem StoreKit-Wrapper.
- [ ] Kein Zahlungs-SDK (Stripe, PayPal, Braintree, Adyen, Klarna) in Kaufpfaden für digitale Güter.
- [ ] Keine Lizenzschlüssel-, Code- oder QR-Freischaltung (Ausnahme: Mac-App-Store-Plug-ins).
- [ ] Wiederherstellung von Käufen ist im UI erreichbar.
- [ ] Gekaufte Consumables haben kein Ablaufdatum.
- [ ] Loot-Boxen zeigen Wahrscheinlichkeiten vor dem Kauf.
- [ ] Digitale Gutscheine nur über IAP.
- [ ] IAP wird im UI nicht abgewertet.
- [ ] Trinkgelder und Geschenke laufen über IAP; Geschenkerstattung nur an Käufer.
- [ ] Testphase bei Nicht-Abo-Apps als Non-Consumable, Preisstufe 0, mindestens 7 Tage.

**3.1.1(a) Externe Kauflinks**
- [ ] Links mit Kaufbezug sind an die App-Store-Storefront gebunden.
- [ ] Für Nicht-US-Storefronts: Entitlement und Info.plist-Schlüssel vorhanden.
- [ ] Hinweis-Sheet vor Verlassen der App, wo gefordert (EU, Japan, Korea, Brasilien).
- [ ] Externe URL entspricht der deklarierten URL.
- [ ] Keine Täuschung, keine Abwertung von IAP.
- [ ] Storefront nicht ermittelbar → Link ausgeblendet.

**3.1.2 Abonnements**
- [ ] Fortlaufender Mehrwert, Mindestlaufzeit 7 Tage, alle Geräte.
- [ ] Legacy-Einmalkäufe nach Abo-Umstellung weiter freigeschaltet.
- [ ] Keine Pflichthandlungen (Social-Post, Kontakte) für bezahlte Inhalte.
- [ ] Alle Stufen in einer Abo-Gruppe; aktive Stufe wird nicht erneut verkauft.
- [ ] Paywall: lokalisierter Preis, Laufzeit, Gesamtbetrag, Verlängerung, Kündigung, Trial-Details, EULA, Datenschutz, Restore.

**3.1.3 Andere Kaufmethoden**
- [ ] Reader-App: keine Kaufaufforderung, Konto-Link nur mit Entitlement (außer US).
- [ ] Multiplattform: extern Gekauftes nutzbar, kein Hinweis auf externen Kauf.
- [ ] Enterprise: Zugang nur über Organisation, kein Endkundenkauf.
- [ ] Person-zu-Person: extern nur bei 1:1 in Echtzeit; Gruppen und Aufzeichnungen über IAP.
- [ ] Physische Güter/Dienste nicht über IAP; digitale Zusätze getrennt über IAP.
- [ ] Companion-App: keine Upgrade-Aufforderung.
- [ ] Werbemanagement: Boosts innerhalb der App über IAP.

**3.1.4 Hardware**
- [ ] Hardware-Freischaltung nur für hardwaregebundene Funktionen oder mit IAP-Alternative.
- [ ] Keine Kopplung an unabhängige Produkte oder Marketing.

**3.1.5 Krypto**
- [ ] Wallet nur mit Organisation-Konto.
- [ ] Kein Mining auf dem Gerät.
- [ ] Handel nur über lizenzierte Börsen, geografisch eingeschränkt.
- [ ] ICO/Futures/Token-Wertpapiere nur mit Finanzlizenz.
- [ ] Keine Krypto-Prämien für Downloads, Referrals, Social-Aktionen.
- [ ] NFT-Besitz schaltet nichts frei (außer US mit Link-out).

**3.2.1 Zulässig**
- [ ] Eigenwerbung nur für eigene Apps, App hat eigenständigen Nutzen.
- [ ] Fremd-App-Sammlungen nur für zugelassene Zwecke mit Redaktionsinhalt.
- [ ] Ablaufdaten nur an Leihmedien.
- [ ] Wallet-Pässe korrekt konfiguriert, kein IAP-Ersatz.
- [ ] Versicherungs-App kostenlos, ohne IAP.
- [ ] Non-Profit zugelassen, Apple Pay, Zweck und Quittung sichtbar.
- [ ] Geldgeschenke freiwillig, 100 % an Empfänger, keine Gegenleistung.
- [ ] Finanz-App vom lizenzierten Institut eingereicht.

**3.2.2 Unzulässig**
- [ ] Keine Katalog-UI für fremde Apps.
- [ ] (ii) entfällt.
- [ ] Ads sichtbar, nicht automatisiert; App hat eigenen Nutzen.
- [ ] Spenden ohne Zulassung nur per Safari-Link.
- [ ] Regionale/Carrier-Sperren sachlich begründet.
- [ ] (vi) entfällt.
- [ ] Keine Follower-, Like-, Rezensions- oder Ranking-Manipulation.
- [ ] Keine binären Optionen; CFD/Forex mit Lizenz je Storefront.
- [ ] Kredit: APR ≤ 36 % inklusive Gebühren, Rückzahlung > 60 Tage, alle Konditionen sichtbar.
- [ ] Keine Bewertung, kein App-Download, keine Datenfreigabe als Zugangsbedingung.
