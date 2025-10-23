Title: Týdenní poznámky: Kurz scrapování v JavaScriptu a další věci pro Apify akademii
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/362
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115390217923121340
LinkedIn-Comments: https://www.linkedin.com/pulse/t%25C3%25BDdenn%25C3%25AD-pozn%25C3%25A1mky-kurz-scrapov%25C3%25A1n%25C3%25AD-v-javascriptu-dal%25C5%25A1%25C3%25AD-v%25C4%259Bci-javorek-jzdke
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 7 min čtení 🧐

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-10-10_tydenni-poznamky-obnovovani-newsletteru.md) už utekl nějaký ten týden (10. 10. až 17. 10.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Jeden týden v měsíci pracuji pro Apify, a v říjnu to byl přesně ten týden, který teď uběhl. V pátek jsem se stihl ještě sejít s Tomášem N. z Apify, který bude mít nově na starosti věci kolem dokumentace, a příjemně jsme si popovídali o tom, jak vidíme mé angažmá v Apify a co si myslíme o budoucnosti [akademie](https://docs.apify.com/academy), o kterou bych měl pečovat.

Po napsání minulých poznámek jsem pak vyrazil na oslavu 10 let existence Apify, což byla moc fajn akce a dokonce tam hráli [Mutanti](https://www.youtube.com/watch?v=ch9DISjjDlA), což mi udělalo velkou radost.

V sobotu jsme zůstali doma, dělali jsme nějaké domácí práce a odpočívali. V neděli jsme si udělali výlet za kamarádem do Černošic. Dcerka jela na kole a v pohodě ujela 5 km, i když se ještě trochu bála a chtěla, abychom ji pořád přidržovali (ač to teda reálně nepotřebovala).

Kamarád mi večer dával ochutnat nejnakouřovanější whisky na světe, nebo whisky kouřenou na islandských ovčích bobkách, ale proběhlo to v gentlemanských množstvích, takže z toho nebyly žádné následky.

## Scrapy + Apify

Vláďa D., který v Apify dělá na tom, aby dobře podporovali Python, mě poprosil, abych na [své infrastruktuře se scrapery](https://github.com/juniorguru/plucker), která kombinuje Scrapy a Apify, vyzkoušel nové SDK, protože by v něm měly být vyřešené nějaké chyby z dávných dob, které jsme předtím nedořešili.

Nové SDK jsem vyzkoušel a chyby opravdu zmizely! Ale objevily se nové. Na rozdíl od těch starých však byly konzistentní a snadno zopakovatelné. Byť teda lokálně se neděly, pouze na platformě. Oddebugoval jsem to do té míry, kam až jsem mohl a pak jsem ho s tím nechal.

Na příčinu přišel celkem brzy, ale zdá se mi, že dalším debugováním a opravováním té věci nakonec strávil celý týden. Nejdřív to vypadalo záhadně, ale pak objevil, že se platforma v některých případech špatně potýká s příliš dlouhými URL.

Pokud chcete podobným způsobem spláchnout svůj týden, jsem vám k službám. Stačí, když mi dáte něco vyzkoušet! Cokoliv, co se mi dostane do ruky, většinou skončí jako aspoň pět issues na GitHubu. Vláďa brzy vydá novou verzi SDK s opravou, takže se těším, až to pak vyzkouším…

Jinak když už jsem se vrtal ve svých scraperech, předělal jsem repozitář, aby používal uv a upgradoval jsem i další balíčky.

- [apify/apify-sdk-python#404](https://github.com/apify/apify-sdk-python/issues/404#issuecomment-3370611679)
- [apify/apify-sdk-python#626](https://github.com/apify/apify-sdk-python/pull/626)
- [apify/apify-sdk-python#627](https://github.com/apify/apify-sdk-python/issues/627)
- [apify/apify-sdk-python#630](https://github.com/apify/apify-sdk-python/issues/630)
- [apify/apify-sdk-python#631](https://github.com/apify/apify-sdk-python/pull/631)

## Kurz scrapování v JavaScriptu

Hlavním úkolem pro tento týden bylo dopracovat Pull Request s uveřejněním nového kurzu scrapování v JavaScriptu v akademii. To je o něco složitější, než by muselo být, protože tam je už starý kurz a nechtěli jsme jej úplně odstranit, spíš nějak přesměrovat, archivovat, apod.

Minule jsme vymysleli plán, jak to uděláme, s ohledem na SEO i uživatele. Tak jsem ho našel zpětně někde na Slacku a taky jsem našel [PR, kde už jsem to měl rozpracované](https://github.com/apify/apify-docs/pull/1907).

Tam jsem teď přidal další věci, včetně nové komponenty, která umí zobrazit nějaké upozornění v textu stránky na základě parametru v URL. To pro mně bylo dost nové, ale nakonec to bylo jednoduché, zvlášť s AI za zády.

Z minula jsem našel i [PR, který mu předcházel a připravoval pro něj půdu](https://github.com/apify/apify-docs/pull/1889). Ten jsme mergnuli.

Chtěl jsem ten hlavní PR rebasnout, jednak aby to bylo aktuální vůči hlavní větvi projektu, jednak aby už stavěl nad tou připravenou půdou, ale vůbec to nešlo. Git mi padal s touto chybou:

```
Assertion failed: (newinfo && !newinfo->merged.clean), function process_renames, file merge-ort.c, line 3007.
error: rebase died of signal 6
```

Nakonec jsem po dlouhém pátrání zjistil, že mu vadil jeden konkrétní commit, kde jsem přesouval a přejmenovával hodně věcí. Rozdělil jsem ho na víc postupných commitů a tím jsem se chyby zbavil. Pak už rebase šlo udělat.

Připravil jsem PR k review, ale děje se tam toho hodně, takže než to mergneme, bude to asi ještě trvat. Musel jsem taky opravit nějaké věci kvůli linterům, ale ty věci s těmi změnami nesouvisí, takže jsem to [vytáhl vedle](https://github.com/apify/apify-docs/pull/2023) a kdyby to náhodou někdo orazítkoval dřív, může se o tohle ten hlavní PR ještě zmenšit.

Až se to všechno mergne, bude hotovo a nový kurz scrapování v JavaScriptu bude konečně venku! Akademie pak bude mít dva hlavní kurzy pro začátečníky, jeden v JS a druhý v Pythonu, které jsou zcela nové a téměř totožné, akorát každý v jiném jazyce.

![Velký PR]({static}/images/screenshot-2025-10-17-at-17-15-38.png)

## Různé další drobnosti pro Apify akademii

Po schůzce s Tomášem N. jsem našel _whitepaper_, kam jsem kdysi sepisoval, co si myslím o akademii, co bych v ní chtěl změnit, a jak bych to dělal. Bylo zajímavé si to znova číst. Dost věcí už se povedlo, ale dost ještě ne!

V pondělí pročítal všechny notifikace z GitHubu Apify, které mi přicházely v předchozích týdnech a já je jen odsouval do složky na pozdější přečtení. Na základě jedné věci jsem založil [apify/apify-docs#2004](https://github.com/apify/apify-docs/issues/2004), ale zbytečně, protože už to bylo vyřešené, akorát jsem to nevěděl.

Přidal jsem [jeden řádek o tom, jak se má správně nastavit Vale](https://github.com/apify/apify-docs/pull/2022) a protože mi designérka poslala nové obrázky kurzů jako SVG, mohl jsem [udělat PR](https://github.com/apify/apify-docs/pull/2025), kde je nahazuju do akademie. Když jsem měl chvíli čas, ujal jsem se [review jednoho PR, které přidávalo návod na propojení RapidAPI a Apify](https://github.com/apify/apify-docs/pull/2015).

Dnes, v pátek, mi ještě zbyla trocha času, tak jsem se jal prozkoumat, zda a jak by šlo v dokumentaci kontrolovat správnost Python kódu uvnitř Markdown dokumentů. Objevil jsem nástroj [doccmd](https://github.com/adamtheturtle/doccmd) a hned jsem ho vyzkoušel, tzn. založil hned několik issues:

- [adamtheturtle/doccmd#570](https://github.com/adamtheturtle/doccmd/issues/570)
- [adamtheturtle/doccmd#571](https://github.com/adamtheturtle/doccmd/issues/571)
- [adamtheturtle/doccmd#569](https://github.com/adamtheturtle/doccmd/issues/569)
- [simplistix/sybil#155](https://github.com/simplistix/sybil/issues/155)

Výsledek mého zkoušení je v [apify/apify-docs#2027](https://github.com/apify/apify-docs/pull/2027), ale je to zatím jen PoC. Chtěl jsem prostě jen vědět, jestli to vůbec nějak jde a co to obnáší.

Pak jsem se ještě chvilku vrtal v tom, jestli by šla testovat cvičení na konci lekcí, ale to jsem nedodělal ani do fáze takového rozpracovaného PR. Nicméně někam to směřuje a ještě pár nápadů bych si pak chtěl ověřit.

![Nové obrázky]({static}/images/screenshot-2025-10-16-at-16-43-31-web-scraping-academy-academy-apify-documentation.png){: .img-thumbnail }

## Další

-   Poslal jsem výherce soutěže o lístky organizátorům [DevFestu](https://devfest.cz/).
-   Předělal jsem dceři košíček a zvonek z odrážedla na kolo.
-   Komunikoval jsem se supportem Buttondownu a nakonec jsem snad dosáhl stavu, kdy jsou všichni _subscribers_ ve správném stavu. Taky jsem opravil jednu chybu ve skriptu, který mi lidi průběžně přesypává z Ekomailu na Buttondown. Newsletter jsem pak ale už neposílal, nějak jsem se smířil s tím, že to nechám na později.
-   Koupil jsem nám vlak na hory. Sice super, že díky expresům do Polska dojedu do Jablonného nad Orlicí přímým vlakem z Prahy, a ani to netrvá dlouho, ale pak jsem zjistil, že dál už nic nejede. Autobusy do místních vesnic pamatuju ze svých středoškolských a vysokoškolských let, no teď tam o víkendu nejsou žádné, zmizely. Jo a taky jsem se seknul při kupování zpátečního vlakového lístku, takže jsem to po pár dnech ještě předělával a protože to bylo vyprodané, skončili jsme v první třídě 😬 Hezky nám to teda začíná, ten výlet.
-   Možná jsme pokročili v hledání nového bydlení. Možná ne. Jsou to občas trochu nervy.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 8 dní jsem naběhal 12 km, při procházkách nachodil 7 km. Celkem jsem se hýbal 4 h a zdolal při tom 19 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Nevím jestli poslat, ale určitě nějak dokončit newsletter.
2.  Přijít jako host na živé natáčení podcastu PodVocasem. [Přijďte!](https://www.podvocasem.cz/live)
3.  Začnu se rýpat v designu [seznamu juniorů](https://junior.guru/candidates/).

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Energetické pokrytectví. Evropské země zvyšují dodávky z Ruska - VOXPOT: reportáže, které spojují Česko se světem](https://www.voxpot.cz/energeticke-pokrytectvi-evropske-zeme-zvysuji-dodavky-z-ruska/)<br>„Evropské země sice od počátku invaze na Ukrajinu poslaly úhrnem přes 167 miliard euro, ale za ruské energie utratily přibližně 213 miliard.“
