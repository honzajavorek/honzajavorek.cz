Title: Týdenní poznámky: Květen
Image: images/img-2549.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 14 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/379
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/116613976656067919

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2026-04-24_tydenni-poznamky-budec-okor-a-nova-paticka-na-webu.md) už utekl nějaký ten týden (24. 4. až 21. 5.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/img-2549.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Odehrálo se toho hodně, a zvlášť v pátky se vždycky něco dělo, takže jsem neměl pořádně čas psát poznámky a píšu až po delší době.

- Řešili jsme dál bydlení, hlavně kuchyň a koupelnu.
- Byla u nás babička a šli jsme s ní na výlet na rozhlednu Doubravku.
- Projel jsem se na kole kolem Vltavy a bylo to fajn.
- Zašel jsem do kina na [Drama](https://www.csfd.cz/film/1556355-drama/prehled/).
- Se ženou jsme doma viděli konečně [Humra](https://www.csfd.cz/film/364012-humr/prehled/).
- Byli jsme na fajn rodinném setkání v Ostružné v Jeseníkách a omylem tam potkali i kamaráda.
- Chytili jsme střevní chřipku a několik dní byli mimo provoz.
- Volal jsem různým rodinným příslušníkům, že nás bude brzy o jednoho víc.
- Kamarád z Indie mě poprosil, abych sehnal certifikát ke Kawasaki motorce, kterou si v roce 2019 koupil v Česku, a tak jsem volal asi deseti různým lidem a vysvětloval jim zamotaný bizarní příběh, abych stejně skončil v nějaké slepé uličce. Ale snaha byla.

## Vylepšování pracovních inzerátů v klubu

Chtěl jsem si trochu odpočinout od práce na homepage, a zároveň se množily reporty bugů v oblasti pracovních inzerátů, tak jsem se pustil do opravování a vylepšování.

Na žádost členů klubu jsem začal do klubu přidávat i text inzerátů. To byl docela oříšek. Text mám, analyzuji jej pro potřebu filtrování, ale zatím jsem jej nikde neuveřejňoval – na webu se jen odkazuje na původní inzeráty.

Bylo potřeba text vzít a správně přeformátovat do Discordího dialektu Markdownu. Většinu práce zvládlo [markdownify](https://pypi.org/project/markdownify/), ale nebylo to rozhodně přímočaré. Nicméně povedlo se.

![Text nabídky inzerátu]({static}/images/screenshot-2026-05-21-at-20-12-54.png)

Discord má však limit na počet znaků ve zprávě, takže se tam dává jen začátek. Bohužel inzeráty nezačínají seznamem požadavků, nebo jinými praktickými informacemi, ale dlouhými odstavci typu „jsme na trhu 30 let a jsme nejlepší, nejdynamičtější a nejmodernější firma v oboru zakulacování šroubků“. Zatím jsem to tak nechal, ale praktičtější by nakonec bylo ten text nechat AI přepsat do pár odrážek 😅

Při této příležitosti jsem pak předělal i zbytek zprávy, takže se teď zobrazují trochu jinak informace o firmě, logo, odkazy, a tak.

![Detaily nabídky inzerátu]({static}/images/screenshot-2026-05-21-at-20-13-10.png)

Upravil jsem na základě bug reportů i prompt, který filtruje nabídky, aby vychytal zatím nevychytané. Snažil jsem se opravit i různé trable s určováním lokace nabídky. Například když byla lokace jen obecné „Czechia“, z nějakého důvodu to můj systém geolokace vyhodnotil na Sobůlky u Brna 😅

Pak jsem ještě přidal do bota, aby jednou za čas hodil do různých kanálů v klubu připomenutí, že v klubu je seznam nabídek práce, které tam zadali sami členové, a ti, kdo hledají práci, by se na ně měli určitě podívat.

Taky jsem opravil chybu, kdy na Discordu nefungovaly správně odkazy, pokud byly v titulku pracovní nabídky emoji.

U toho jsem celkově dost překopal, jak fungují různá připomenutí, a několik jsem jich ještě přidal, například na starší záznamy přednášek.

Nakonec mě ještě potrápil LinkedIn, který mi začal do výsledků házet nabídky práce z celého světa. Byla to chyba LI a druhý den to opravili, ale stejně se mi to pak ještě občas nezdálo, tak jsem začal nabídky filtrovat vyloženě jen na CZ a SK.

## Různé další drobné opravy a vylepšení

- V seznamu kandidátů jsem opravil [zpracovávání připnutých repozitářů na GitHubu](github.com/juniorguru/eggtray/issues/320), kam člověk přispěl, ale které mu nepatří. Poznamenal jsem si u toho i jeden [nápad na potom](https://github.com/juniorguru/hen/issues/137).
- Přidal jsem do kandidátů rozlišení pro elektro VŠ, stejně jako tam už bylo pro matematicky zaměřené VŠ.
- Vrtal jsem se z nějakého důvodu v YAMLech, kde uchovávám různá data, a napadlo mě, že s AI agentem už by šlo docela jednoduše vyházet starý způsob načítání YAMLů přes [strictyaml](https://pypi.org/project/strictyaml/). Myšlenka té knihovny je fajn, ale přece jenom je nestandardní. Zpracování YAMLu se liší od mainstreamu, a nebyl jsem si jistý tím, jak moc je vlastně živá. Člověk si tam tvoří schema, ale není to nic známého odjinud. Takže jsem to postupně nahrazoval kombinací PyYAML + Pydantic, kdy načtu YAML do obyčejné struktury a tu nechám přežvýkat Pydantic modelem pro validaci. Pustil jsem na to AI agenta a opravdu, za odpoledne byl zbytek webu předělaný na tento způsob a `strictyaml` jsem mohl vyhodit ze závislostí.
- Vypršel mi přístup na API [Merku](https://www.merk.cz/), ze kterého se neobejde [katalog kurzů](https://junior.guru/courses/), tak jsem je poprosil o prodloužení a o informaci, kdy to vyprší příště, abych si na to dal upomínku a nespadlo mi to na produkci 😆 Naštěstí odpověděli docela rychle a do druhého dne už to frčelo.
- Zjistil jsem, že se mi na webu jedno tlačítko obarvuje špatně. Ta věta zní jako primitivní záležitost, ale byla to půldenní _rabbit hole_ do hlubin mého systému na produkční deploy, protože se obarvovalo špatně kvůli špatné struktuře HTML elementů a na vývojovém prostředí se to vůbec neprojevovalo! Nakonec jsem zásadně změnil, co se ještě dodatečně s vybuilděným HTML dělá a jakým způsobem.
- Snažil jsem se s pomocí AI agenta zjistit, proč se mi někdy při lokálním vývoji nechtěně zapne zapisování na produkční Discord. Taky z toho byla slušná _rabbit hole_, a snad je to tedy po velkém debugování vyřešeno. Nejtěžší bylo rozlišit, co z toho, co AI agent navrhuje, jsou reálná vylepšení, a co z toho je nesmyslný overengineering. Poměr bych od oka odhadl na 1 ku 10.
- Přestalo mi z ničeho nic fungovat Apify Python SDK a podle chyb jsem jej používal špatně. Posílal jsem do parametrů enumy místo stringů a návratové hodnoty používal jako slovníky a ne jako objekty. Opravil jsem to, ale nechápu, jakto, že to doteď fungovalo? Že bych to někde nějak omylem upgradoval a nová verze byla breaking? No neřeším, hlavně že to teď už zase funguje.
- Když nabídce práce chyběla lokace, tak mi spadlo buildění webu, protože se v jedné chvíli předpokládalo, že to není None, ale string. Sice nevím, jak se stane, že nabídka práce nemá lokaci, ale opravil jsem aspoň to, aby to nespadlo.

## Živé diskuze v klubu

V klubu se odehrálo několik velmi živých diskuzí ohledně AI. Jednoho člena silně demotivovalo, že se učí programovat a totéž, co vydře, teď každý moula vygeneruje přes AI agenta za pár sekund.

Naštval se a odešel z klubu, ale pak zase přišel a nějak jsme to ještě probrali, že stále dává smysl učit se programovat a proč. Pak se to zvrhlo ještě v debatu o formě a obsahu a jestli někdo náhodou nepíše moc arogantně, a kdo jak co v tomto směru vnímá.

Tohle celé se dělo asi dva nebo tři dny v kuse a vygenerovalo to kolem 90+ zpráv denně, takže to bylo celkem náročné. Ale dělám to 7 let, tak už to beru sportovně 😅 A kdyby se takové věci v komunitě čas od času vůbec neděly, asi bych si i myslel, že mi to tam umírá! Mít někde živo holt zahrnuje i intenzitu kategorie „příliš živo“, prostě to k tomu patří.

Pak jsem ještě soukromě pomáhal s krizí jedné člence a sháněl jí kontakty na párové terapie.

## Předělávání homepage

Nakonec jsem se opět dostal i k prioritě, na které mám teď pracovat, a to vylepšování homepage junior.guru.

V plánu jsem měl přidat tam sloupec s kandidáty a vedle toho sloupec s příběhy úspěšných „absolventů“ klubu. Zabralo to několik iterací, ale je to tam:

![Kandidáti a „absolventi“]({static}/images/9db3376b462d763b.png){: .img-thumbnail }

Pak jsem přidal další sekci, která má primárně sloužit jako diferenciace.

![Diferenciace junior.guru]({static}/images/f8fc3d434c988183.png){: .img-thumbnail }

Pak jsem ještě narychlo přidal sekci, která láká na klub:

![Sekce o klubu]({static}/images/screenshot-2026-05-21-at-15-19-08.png){: .img-thumbnail }

Ještě jsem pak vyměnil v číslech na úvodní stránce počet kapitol příručky za počet kandidátů. Ale vlastně ani nevím, co je lepší.

Všechno to tam házím jak vidlema seno a homepage zatím není moc koherentní. Střídají se tam různé designové prvky, různá pozadí, má to všelijaké pořadí, je tam stále historický rozcestník, a tak dál.

Ale po každé dílčí změně to bylo i tak lepší, než bez ní, takže jsem to šoupl hned na produkci, ať to tam nějak pracuje, ať to lidi vidí, ať sbírám feedback. A postupně to budu přeskládávat, uhlazovat, a dolaďovat.

## Nové grafy

Nechtěl jsem dělat už nové grafy, protože je to žrout času a žádným způsobem se to nevyplatí, ale s AI agentem se tahle ekonomika trochu změnila, takže jsem to zkusil.

Začal jsem sledovat nějaké statistiky kolem kandidátů a vytvořil pro to novou stránku v tiráži webu: [junior.guru/about/candidates](https://junior.guru/about/candidates/)

Hlavně mě zajímá vývoj toho posledního grafu, tzn. jestli lidi využívají kontroly GitHubu na homepage a jestli se to číslo zvyšuje a tak. Zvlášť jestli pak budu dělat nějaký marketing, tak jestli to začnou lidi používat ještě víc. Ty ostatní statistiky začnou být zajímavé asi až časem.

Pak jsem přidal i [junior.guru/about/jobs](https://junior.guru/about/jobs/), kam jsem dal průběžné počty inzerátů, nějaké stastiky ohledně efektivity bota (počty zahozených inzerátů), a tak. Graf s počtem uveřejněných inzerátů by mohl pomoci trochu sledovat juniorní trh v čase, i když je to samozřejmě jen nějaký vzorek.

Když už jsem byl u toho, dal jsem jeden z těch grafů ještě zvlášť i na [junior.guru/about/women/](https://junior.guru/about/women/) – počet žen mezi kandidáty, ale ten taky začně být zajímavý až časem.

V grafech jsou vertikální čáry, které označují určité milníky vývoje junior.guru, jen tak pro orientaci, a všiml jsem si, že tam některé chybí, tak jsem je přidal: spuštění seznamu kandidátů a přetvoření homepage. I když ta homepage je dost orientační, protože se jaksi stále ještě přetváří. Ale to hlavní už tam asi teda je.

![Počet inzerátů]({static}/images/7fc902f60fed31e2.png){: .img-thumbnail }

## Rozdělení kandidátů a inzerátů

Doteď byly stránky s kandidáty a inzeráty v jedné sekci webu „Práce“, která měla podmenu s dvěma podstránkami. Teď jsem to předělal, aby to byly dvě zcela nezávislé, samostatné stránky. Takže „Práce“ teď označuje jen inzeráty a pak jsou tam ještě „Kandidáti“.

Bohužel se mi při tom omylem povedlo asi na týden vygumovat z menu odkaz na „Inspirace“. Včera nebo kdy jsem šel publikovat nový rozhovor a všiml jsem si, že mi jaksi v menu úplně chybí odkaz na celou tu sekci 😀

No přišlo mi předtím podezřelé, že se to tam všechno vlezlo. Ale nevšiml jsem si. Takže jsem to opravil a trnul jsem, jestli se to tam ještě pořád všechno vleze i bez hamburger menu. Trochu jsem upravil CSS pro nejmenší displeje a vlezlo se.

![Hlavní menu]({static}/images/screenshot-2026-05-21-at-16-18-02-jak-se-naucit-programovat-a-ziskat-prvni-praci-v-it.png){: .img-thumbnail }

## Týden pro Apify

Během minulého a tohoto týdne jsem se věnoval svému jednomu týdnu měsíčně pro Apify:

- Přepracoval jsem pár věcí v [apify/apify-docs#2275](https://github.com/apify/apify-docs/pull/2275) po review a pak to mergnul – nový úvod kurzu je na webu (ale unlisted)
- Mergnul jsem opravu cvičení s Netflix/movie DB v Academy: [apify/apify-docs#2393](https://github.com/apify/apify-docs/pull/2393)
- Přidal jsem do Academy lint na obrázky a všechny nově přidané musí být ve WebP. Dal jsem si záležet na DX, takže to obsahuje přesný návod, co spustit pro konverzi. Kdokoli, kdo umí spustit `pnpm something`, to snadno splní: [apify/apify-docs#2534](https://github.com/apify/apify-docs/pull/2534)
- Všiml jsem si, že v docs používáme `axios` na jednu jedinou jednoduchou věc, tak jsem ho odstranil: [apify/apify-docs#2535](https://github.com/apify/apify-docs/pull/2535)
- Protřídil jsem pár starých issues, např. zavřel [apify/apify-docs#948](https://github.com/apify/apify-docs/issues/948) nebo [apify/apify-docs#1417](https://github.com/apify/apify-docs/issues/1417)
- Otevřel jsem PR s novou lekcí pro AI kurz o docs-driven přístupu k vibe codingu scraperů: [apify/apify-docs#2537](https://github.com/apify/apify-docs/pull/2537)
- Sestavil jsem příkaz na zálohu Warehouse a na pozadí jsem spustil scrape, ale má to 500 MB a nejsem si jistý, co s tím – viz můj komentář v [apify/apify-docs#1418](https://github.com/apify/apify-docs/issues/1418#issuecomment-4478525555)

## Další

-   Poslal jsem newsletter za duben. Abych jej mohl poslat, musel jsem opravit spoustu rozbitých věcí a trvalo mi to skoro jeden celý pracovní den. Pak mi to ještě generovalo newsletter, kde témata v klubu byly všechny jen o AI, tak jsem měnil prompty a ladil to, aby to bylo pestřejší. Počty inzerátů se nově berou ze stejných statistik, které se ukládají pro účely grafů.
-   [Lucie Tvrdíková končí se svými kurzy testování](https://lucietvrdikova.cz/proc-s-koncem-roku-2026-ukoncuji-kurz-kompletni-priprava-pro-testera/). Umořily ji především dotace na kurzy.
-   Vydal jsem nový upřímný rozhovor od Adély, ale ještě jsem jej nezpropagoval, ani v klubu: [Juniorní tranzit do IT. Musel jsem jít s penězi o dvacet tisíc dolů, říká Petr Kašička](https://junior.guru/stories/petr-kasicka/)
-   Domlouvali a plánovali jsme s Táňou přednášku od Kateřiny Hroníkové – [Web scraping: Nechte internet pracovat za vás](https://junior.guru/events/62/). Ani tu jsem ještě nikde nestačil propagovat.
-   Někdo mi napsal e-mail na `@juniorguru.cz` a nedorazilo to, protože to má být `.guru` a ne `.cz`, i když tu doménu mám a přesměrovává na správný web. Napadlo mně, že to možná není první ani poslední člověk, který se takhle splete, a přidal jsem si `juniorguru.cz` do [ImprovMX](https://improvmx.com/) a přesměroval e-mail tak, aby v pořádku dorazil.
-   Na [pyvec.org](https://github.com/pyvec/pyvec.org) se hromadily problémy s instalací a upgradama balíčků, tak jsem si na to vyhradil zhruba 1 hodinu a přehodil to celé z pipenv (!) na uv.
-   [ITnetwork mi leze do zelí](https://www.itnetwork.cz/blog/jak-prorazit-v-it-absolventum-pomuze-novy-program-alumni). Přeji hodně štěstí. Dělám to 7 let a myslím si, že mít živou, funkční a opravdu užitečnou komunitu není vůbec jednoduché. Svůj Discord má i Engeto nebo Czechitas a myslím, že junior.guru to neohrožuje, protože zásadní je vždycky hlavně výsledné provedení a jestli se tomu někdo každý den věnuje.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. V klubu bylo milion věcí ke čtení a většinu jsem dohnal, ale ještě mi tam chybí podívat se na jedno CVčko. Mailů taky přišlo milion a nestihl jsem je vůbec všechny přečíst, nebo na ně reagovat. Holt musí počkat, dny nejsou nafukovací.
-   Snažil jsem se zjistit, proč se lidi neúčastní měsíční _coding challenge_ a co můžeme udělat proto, aby se účastnili.
-   Vyčistil jsem si po dlouhé době klávesnici.
-   Za 28 dní jsem naběhal 24 km, při procházkách nachodil 4 km, na túrách nachodil 20 km, ujel na kole 31 km. Celkem jsem se hýbal 23 h a zdolal při tom 79 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1. Budu propagovat přednášku a rozhovor.
2. Udělám v klubu soutěž o Java knihu.
3. Budu vylepšovat homepage.

K tomu bude ještě členská schůze Pyvce, schůze SVJ, dítě pojede na školkový výlet, a já pojedu každý víkend na dvě různá místa přes celou republiku, na otočku 😅

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Adieu Visa et Mastercard : 130 millions d'Européens basculent vers un paiement 100 % souverain dès 2026](https://www.lesnumeriques.com/banque-en-ligne/adieu-visa-et-mastercard-130-millions-d-europeens-basculent-vers-un-paiement-100-souverain-des-2026-n250918.html)<br>Super. Ještě by to teda chtělo to Euro…
- [What email will look like in the future](https://buttondown.com/blog/future-of-email)<br>Průlet radikálními změnami, které se odehrávají na poli standardizace e-mailové komunikace. (Zkouším si clickbait komentář 😀)
- [Google Search’s I/O 2026 updates: AI agents and more](https://blog.google/products-and-platforms/products/search/search-io-2026/)<br>Tak co, je SEO mrtvé? A jak to teď teda funguje, když chci, aby mi lidi chodili na web? Nebo už budou lidi chodit jen na tři weby a to bude celý internet?
- [iOS 26.5 updates unlocks Apple Watch and AirPod features for third-party alternatives &mdash; but only if you live in the EU | TechRadar](https://www.techradar.com/phones/ios/ios-26-5-updates-unlocks-apple-watch-and-airpod-features-for-third-party-alternatives-but-only-if-you-live-in-the-eu)<br>Díky, EU! Malé krůčky, ale krásné: „iOS 26.5 also adds proximity pairing support for non-Apple buds. This is the feature that makes it a one tap process to pair AirPods with your iPhone when you start to set them up nearby. Thanks to the update, third-party earbuds can start to support this simplified setup process.“ Ještě by to chtělo možnost mít různá browser jádra na iOS, ale to je běh na dlouhou trať. Naštěstí OWA a DMA nepolevují.
- [In macOS Sonoma, Touch ID for sudo can survive updates &#8211; Six Colors](https://sixcolors.com/post/2023/08/in-macos-sonoma-touch-id-for-sudo-can-survive-updates/)<br>Návod, jak si nastavit macOS, aby se v terminálu pro sudo používalo TouchID místo psaní hesla. Na rozdíl od předchozích návodů by toto řešení mělo přežít nejen restarty systému, ale i upgrady. Podle všeho je to takhle připravené přímo od Apple, udělali tam šablonu na speciální soubor, který nepřemažou upgrady.
- [Maxipes Fík slaví 50. narozeniny |  iROZHLAS - spolehlivé zprávy](https://www.irozhlas.cz/kultura/televize/maxipes-fik-slavi-50-narozeniny-vytvarnik-salamoun-v-nem-zvecnil-bobtaila_2605110702_kvr)<br>Fík je bobtail a Ahníkov opravdu existoval, ale musel ustoupit těžbě.
- [AI rozbila juniorskou cestu k senioritě. Kód vzniká rychleji, zkušenost pomaleji - Zdroják](https://zdrojak.cz/clanky/ai-rozbila-juniorskou-cestu-k-seniorite-kod-vznika-rychleji-zkusenost-pomaleji/)<br>„Dobrý junior v roce 2026 nebude člověk, který odmítá AI. Bude to člověk, který s AI pracuje agresivně, ale skepticky. Nevěří výstupu bez ověření, nepouští do produkce kód, který neumí vysvětlit, a používá model k rozšíření vlastního mentálního modelu.“ „Kent Beck navrhuje, aby junior před mergem AI-asistovaného kódu prokázal, co se při práci naučil. Je to jednoduchá organizační brzda, která nechrání build, ale chrání učení.“
- [The Boring Internet | Terry Godier](https://terrygodier.com/the-boring-internet)<br>Pěkné připomenutí a motivace, že „starý nudný internet“ nikam nezmizel. Nevím, jestli by XMPP souhlasilo s tím, že protokol přežije všechno, ale třeba jo.
- [RedFlags](https://redflags.cz/)<br>Ještě jsem to neviděl, ale vypadá to zajímavě. RedFlags o tom, jak nenaletět na scamy na netu. Hlavně pro děcka, ale asi nejen.
- [The Longest Retreat in History - YouTube](https://www.youtube.com/watch?v=uAH1xnruDOE)<br>Československé legie ve zkratce
- [we need a federation of forges](https://blog.tangled.org/federation/)<br>„OSS needs to break free from monocultures like GitHub, but code collaboration should still be fun and social.“
- [S13E06 - Jiří Kosek - O legendární PHP knize a XML — PodVocasem](https://overcast.fm/+AA0cJ3x9prI)<br>Tohle mě bavilo! Jirka Kosek a XML v podcastu PodVocasem.
