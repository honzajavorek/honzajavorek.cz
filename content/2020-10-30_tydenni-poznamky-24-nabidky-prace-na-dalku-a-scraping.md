Title: Týdenní poznámky #24: Nabídky práce na dálku a scraping
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (26.10. — 30.10.) a tak [stejně jako minule]({filename}2020-10-23_tydenni-poznamky-23-pribeh-na-blog-melouch-e-maily.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Poznámky teda tentokrát píšu až v neděli. Ve středu jsem nepracoval, byl státní svátek.


## Práce na dálku

Protože řádí covid-19, rozhodl jsem se soustředit na [stránku s prací na dálku](https://junior.guru/jobs/remote/) s tím, že uvidím, co všechno se z ní dá vymáčknout. Pokud by na ní bylo dost nabídek práce, přidal bych i nějaké rady na práci na dálku a celé bych to pak zkusil propagovat mezi lidmi. V současné chvíli by to mohlo mít nějaký ohlas.

Přidal jsem tedy podporu pro [Remote OK](https://remoteok.io/), [WWR](https://weworkremotely.com/) a nabídky práce na dálku ze StackOverflow. Psal jsem i osobně na Pieteru Levelsovi na Twitteru, jestli mohu použít logo Remote OK, protože to vyžaduje v podmínkách, a dostal jsem svolení.

Na stahování nabídek z RSS se skvěle hodil [feedparser](https://github.com/kurtmckee/feedparser). Taky jsem zjistil, že když si potřebuju dojít pro některé informace až na stránku s inzerátem, je dobré zkontrolovat, jestli stejně jako JG nepodporuje [schema.org meta data](https://schema.org/JobPosting). V takovém případě se totiž nemusím trápit s čtením HTML, stačí vytáhnout ta meta data. No a zjistil jsem, že na to existuje prima knihovna [extruct](https://github.com/scrapinghub/extruct/).

Výsledek ale nic moc, juniorní nabídky práce na dálku prostě nejsou. Sem tam něco, jasně, mám tam nějaké false positives i false negatives, OK, ale i když to všechno vezmu v úvahu, výsledek je spíš velké prd.


## Scrapování

Jeden pro mě důležitý zdroj nabídek práce blokuje HTTP requesty z IP adres CircleCI, kde se mi všechno spouští. Zkoušel jsem to [řešit přes Tor](https://www.khalidalnajjar.com/stealthy-crawling-using-scrapy-tor-and-privoxy/). Rozběhal jsem to lokálně, ale na CircleCI ne a nikdo mi neodpověděl ani na [StackExchange dotaz](https://tor.stackexchange.com/questions/21677/signal-response-contained-unrecognized-status-code-514) (naopak mi napsali, že tohle dělat nemám…), takže jsem tuto cestu po dvou dnech průzkumu a debugování opustil.

Jako další možnost jsem zvažoval Apify, ale nakonec se mi nechtělo scraper psát odznova a zkusil jsem najít nějakou proxy, která by věc řešila. Nejlevnější řešení jsem našel u [ScrapeStack](https://scrapestack.com/), ale po základním otestování jsem zjistil, že mnou scrapovaný web na requesty routované přes ně odpovídá úplně jiným contentem a vynucuje přihlášení. Zajímavé. Nepovedlo se mi to nijak vyřešit, takže tato možnost padla.

Dále jsem zkoušel najít nějaký seznam proxy zdarma, které bych mohl rotovat a dělat requesty přes ně. Zkoušel jsem [free-proxy.cz](http://free-proxy.cz), koukal na věci jako [proxybroker](https://proxybroker.readthedocs.io/en/latest/) (vypadá skvěle, ale je neudržovaný) nebo [scylla](https://github.com/imWildCat/scylla), studoval jsem seznam na [awesome-web-scraping](https://github.com/lorien/awesome-web-scraping/blob/master/python.md). Proxy různě fungují nebo nefungují, jsou různě blokovány nebo nejsou, no byl to velký boj a zase vydal tak na dva dny. V jednu chvíli jsem to vzdal a šel zkoumat to Apify, ale po dvou hodinách zkoušení a čtení dokumentace jsem došel k tomu, že to má stejný problém jako ten ScrapeStack, tedy že web na requesty odpoví přihlašovací stránkou a já nevím proč.

Takže zpátky k proxy. Nakonec jsem našel relativně udržovaný a strojově čitelný seznam na [clarketm/proxy-list](https://github.com/clarketm/proxy-list) a vyladil scrapování tak, aby se proxy uměly rotovat. To ale nijak nepomohlo, web mé requesty stále blokoval. Takže abychom si to shrnuli, na co jsem přišel:

- Hotová řešení z webu vydolují akorát přihlašovací stránku.
- Requesty z různých proxy nebo sdílených IP adres, byť střídané a rotované, mi blokují.
- I když jsem mezi requesty dal nesmyslné rozestupy, stále blokují.
- I když jsem ořezával různé trackování a vypnul cookies, stále blokují.
- I když jsem rotoval user agenty, stále blokují.

Chtěl jsem to vzdát a vykašlat se na to, ale nakonec mě napadlo ještě něco. Web funguje tak, že jejich HTML se dále na věci dotazuje nějakého neveřejného API. Můj scraper se dotazoval na nabídky práce skrze toto API a tento request, typicky první, většinou prošel. Jenže ty další, na jednotlivé nabídky práce, ty už byly blokované. No ale to byly requesty na samotné HTML stránky. Napadlo mě, jestli nejde i ty nabídky samotné tahat přes API a upravit scraper tak, aby šel se vším jen přes API. No a vypadá to, že toto je výsledná cesta, že tím se všechno vyřeší. Na API zřejmě nemají tak drsné ochrany a requestům se tam celkem daří.

Zbývá doladit detaily a zjistit, jestli celá tahle věc nebude tak neefektivní, že bude trvat dve hodiny scrapnout 5 nabídek práce, ale zatím výsledek považuji za úspěch.

Otázkou samozřejmě je, jak správné je toto všechno dělat, ale tož když si mohlo Kiwi oscrapovat půl internetu a založit si na tom byznys… Mým protějškem je obrovská monopolní mega korporace, se kterou se nikdy nedomluvím a jež nemá důvod se mnou spolupracovat. Jsou tam ale nabídky práce pro juniory a já je chci těm juniorům dát na podnose, aby se nemuseli přes jejich nesmyslné filtry prohrabávat tunou smetí.


## Další poznámky

- Seznam [zadal nabídku práce přímo na JG](https://junior.guru/jobs/2c67d25adbae2c784a01bf97c8631963605086c5fbc9f055257f84b8/), takže jsem jeho logo přidal mezi [firmy, které na JG někdy inzerovaly](https://junior.guru/jobs/) (prestiž!).
- Dokončili jsme více méně můj melouch pro kamaráda.
- Po schválení finálních úprav jsem vydal [článek o Baru z Kanady](https://blog.python.cz/pyladies-to-zacalo-kanadou-to-neskoncilo) na blogu české Python komunity. Také jsem ji hned přidal i mezi [příběhy na hlavní stránce JG](https://junior.guru/#stories).
- Radůza mi odepsala na e-mail a poděkovala za fajn rady :)
- Ještě dnes jdu vytvořit a poslat říjnový newsletter. Je prvního listopadu, takže asi nejvyšší čas.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [How Discord Won](https://t.co/DCnxXVAu7w?ssr=true)<br>Konečně mi někdo vysvětlil Discord
- [Neviditelné pouště v regionech, které dusí českou demokracii](https://t.co/gDl3evswYO?ssr=true)<br>Proč mizí lokální média a proč je to špatně
- [Programátorem za 365 dní a zadarmo? Tak určitě!](https://blog.python.cz/programatorem-za-365-dni-a-zadarmo-tak-urcite)<br>Honza Kovanda píše o tom, jak se z něj do roka stal programátor a jak si vytvořil vlastní e-shop
- [Citation Needed](http://exple.tive.org/blarg/2013/10/22/citation-needed/)<br>Proč indexujme pole/seznamy od nuly a ne od jedničky? Výlet do historie, ve kterém figuruje i jachtaření prezidenta IBM.
- [Můžete si za to sami, vzkazuje Babiš kolabující zemi](https://a2larm.cz/2020/10/muzete-si-za-to-sami-vzkazuje-babis-kolabujici-zemi/)<br>“Zbyl jen smutný klaun uprostřed zhrouceného státu.”
- [Covid-19 v evropských městech nakopl cyklistiku. Praha uvízla v době jeskynní](https://t.co/O5hqX7hdWk?ssr=true)<br>Rozdíl vidím v tom, že o těch západních politicích se dají napsat ty věty jako “co je jeho cílem” nebo “má plán”.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>

Podcasty neposlouchám, nenašel jsem si k nim zatím moc cestu. Ale něco jsem teď o víkendu zkusil a toto se mi líbilo:

- [Technicky vzato](https://www.vutbr.cz/podcast), podcast VUT v Brně. Dva díly o robotech nebo esportu. Líbí se mi, že jeden díl má 20 minut a ne sto hodin, jako u jiných podcastů.
- [Fall of Civilizations Podcast](https://fallofcivilizationspodcast.com/) je konečně něco na téma, které mě baví. Nevedou se tam rozhovory s lidmi, je to spíš dokumentární seriál.
