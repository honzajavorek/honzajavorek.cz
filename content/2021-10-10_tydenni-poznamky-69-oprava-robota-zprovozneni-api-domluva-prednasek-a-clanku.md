Title: Týdenní poznámky #69: Oprava robota, zprovoznění API, domluva přednášek a článků
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (4.10. — 10.10.) a tak [stejně jako minule]({filename}/2021-10-03_tydenni-poznamky-68-odstraneni-vercelu-cally-pracovni-inzeraty.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Výkonnost synchronizace

Když spustím `make sync`, stáhnou se všechna potřebná data z internetu do SQLite. Až potom mohu spustit `make build` nebo něco podobného a vygenerovat tím statický web JG. Onen `sync`, tedy synchronizace, se stará o vše, komunikaci s Discordem, stahování finančních výsledků, scrapování pracovních nabídek, apod.

Jak jsem psal minule, tento týden jsem startoval s tím, že je tato část JG rozbitá. Jednak generovala příliš mnoho textu na výstupu jako logy, takže se na mě CircleCI už vyprdlo s tím, že by to ukládalo. Jednak už to po posledních změnách trvalo příliš dlouho, déle než půl hodiny.

Velký objem textu padal ze Scrapy, jež ve výchozím stavu vypisuje každý scrapnutý kousek dat, který mu projde pod rukou. To jsem nakonec vyřešil jiným `__repr__()` pro `Item` objekty, aby se vypisoval třeba jen titulek a dvě tři další políčka, ale zbytek ne. Jak to funguje se můžete podívat [v testech](https://github.com/honzajavorek/junior.guru/blob/main/tests/test_lib_repr.py).

Následně jsem ještě poladil logování a jeho nastavování, takže jsem v tomto směru důkladně pročetl jak [dokumentaci Scrapy](https://docs.scrapy.org/en/latest/topics/logging.html), tak [Python docku](https://docs.python.org/3/library/logging.html) a [HOWTO](https://docs.python.org/3/howto/logging.html), které je její součástí. Dlouho jsem se v logování nerýpal, takže jsem už úplně zapomněl věci jako existenci _root_ loggeru, což mě celkem potrápilo, když jsem hodiny debugoval, proč se mi vypisuje spousta věcí, které jsem vypisovat zakázal. Rovněž souhra Scrapy a mého vlastního loggingu byla občas oříšek, nicméně nakonec jsem vše nastavil tak, jak jsem chtěl. Vlastně „stačilo“ vyhodit `logging.basicConfig()`, přečíst vše o tom _root_ loggeru a jak se dědí handlery, apod.

Dalším problémem bylo trvání celé synchronizace. Doteď jsem scrapery pouštěl paralelně v každém procesu, ale bylo to jen takové rychlé a špinavé řešení. Můj `sync` proces přes `multiprocessing.Pool().map()` pustil paralelně `subprocess.run()` se `scrapy crawl <název scraperu>`, a takhle pro každý scraper. To jistě nějaký čas ušetřilo, ale na čtyřjádrově tvářícím se stroji to pustilo jen 4 scrapery zároveň. Vždy se čekalo, až nějaký dojede, a pak teprve začal další. Když nějaký scraper ze začátku hodně stahoval, bylo to de facto blokující IO, jelikož v tomtéž procesu nejelo nic jiného, co by se mohlo během toho dít.

Řešením bylo pustit všechny scrapery v jednom procesu a nechat je prolínat se. Myslel jsem, že to snad se Scrapy ani nejde, o to víc mě překvapilo, že příklad, jak to udělat, byl [přímo v dokumentaci](https://docs.scrapy.org/en/latest/topics/practices.html). Buď je to nové, nebo jsem to dřív přehlídl. Každopádně potřeboval jsem to až teď a teď to tam bylo, tak že dobrý. Překvapilo mě, jak byl přechod na „Scrapy v jednom procesu“ okamžitý. Přepsal jsem 10 řádků kódu a vše fungovalo prakticky jako předtím, ale rychleji. O to víc mě pak zaskočil jiný problém, a to nemožnost restartovat Twisted reaktor v rámci jednoho procesu.

Scrapy jede nad frameworkem Twisted, jenž je starý pomalu jak Python sám, ale stále se vyvíjí a na síťové věci je to prý stále pecka. Mě to vlastně nemusí moc zajímat, protože mám synchronní kód a Scrapy mě od Twisted všude odstiňuje. Jenže když jsem začal Scrapy pouštět v rámci svého vlastního programu spolu se spoustou dalších věcí, už to začal být trochu i můj problém, že Twisted má v sobě nějaký reaktor a je asynchronní apod. Podobnou věc jsem [řešil už u Discord bota]({filename}/2021-02-06_how-to-create-non-interactive-discord-bot.md), ale tam šlo o `asyncio`, u něhož se mi povedlo najít způsob, jak _loop_ restartovat, resp. zahodit starou a použít novou. Díky tomu jsem mohl v jednom procesu (`make sync`) sekvenčně za sebou spouštět různé věci, z nichž některé byly v podobě asynchronního bota, jenž nastartuje, něco udělá, a poté skončí. Přičemž tyto věci o sobě neví navzájem a nesdílí žádnou _loop_, neví se kolik jich tam je, nic podobného. Toto, jak jsem pochopil, s Twisted reaktorem udělat nejde. V jednom procesu může existovat jen jednou. Dokud se nezastaví, tak ten proces blokuje. Jakmile se zastaví, už se nedá nikdy znova spustit.

Nic dalšího jsem k tomu nenašel, takže jsem se s tím smířil a zkusil nejjednodušší možné řešení: Vyrobit vždy jeden jediný `multiprocessing.Process()`, v němž se spustí Scrapy se svým reaktorem, pak profrčí všechny scrapery, pak se reaktor zastaví a proces skončí. Rodičovský proces `make sync` na tento počká a jede si dál, přičemž celá věc se může následně zopakovat podruhé, nebo kolikrát chce. Je to sice malá režie navíc, ale popravdě, výroba nějakého jednoho procesu fakt není něco, co by ten `make sync` zdržovalo. Celé to teď trvá 15-20 minut, což není úžas, určitě by to šlo zlepšovat, ale není to ani 30+ minut jako předtím.


## API pro Czechitas

Spolu s opravou `make sync` jsem byl už jen krůček od finalizace API pro Czechitas, stačilo opravit nějaké kritérium v databázovém dotazu. Pak jsem ještě zjednodušil určité věci, např. překopal jak se eviduje časový údaj o tom, kdy byl inzerát vidět na internetu, pak ještě odverzovat tabulku s inzeráty tak, aby vše respektovalo její aktuální schéma, a bylo to.

Výsledný soubor je [tady](https://junior.guru/api/jobs.json) a jsem zvědav, co se nám s tím povede vyrobit. Naštěstí jsem nebyl v našem akčním týmu sám, komu se povedlo za dva týdny akorát motat v kruzích, takže jsme čtvrteční call s domluvou „co a jak dál“ nakonec posunuli. Vygenerováním tohoto souboru bych si přál mít definitivně za sebou aktuální pasáž života s podtitulkem „Honza se nekonečně dlouho brodí přebudováváním datového modelu kolem pracovních inzerátů“, ale tak jednoduché to nebude.

Tím, že jsem do inzerátů začal šťourat, přišel jsem totiž na nějaké objektivní a těžko ignorovatelné chyby. Už dřív jsem si všiml, že když mi přestane fungovat scraper, můj monitoring není schopen to chytit. Původně jsem si myslel, že by mi bot mohl do klubu do nějaké tajné místnosti reportovat každý den statistiky, ale nakonec jsem to vyřešil jednodušeji. Skript `make check-scrapers`, který vyhodnocuje statistiky ze scraperů a případně selže s tím, že neodpovídají očekáváním, jsem pouze obohatil o heuristiku, zda náhodou nějaký scraper neselhal. Funguje to tak, že pokud scraper vyhodí příliš velké procento nabídek z podezřelých důvodů, selže to. Velikost procenta budu asi muset ladit, teď tam mám 5 %, ale už teď je to záchranná síť, pokud by to selhalo celé, jako dřív scraper na LI.

No a právě scraper na LI mi teď dělá velké starosti. Sice zase funguje, to jo, to je velké plus. Jenže funguje až moc. Pokud LI nenajde na slovo „programátor“ nebo „tester“ už nic zajímavého, začne mi vracet věci jako „operátor/ka vstřikolisu“ nebo „dělník na úseku pálených lupků“. Robot je přitom naučený rozpoznávat, jestli je inzerát juniorní nebo ne, ale pozice vůbec neřeší. Dřív se stalo, že do výběru spadl „projekťák“ a vrtěli jsme hlavami, jestli to tam patří nebo ne, ale teď to nabralo jiné obrátky. Je to bohužel věc, která lidi na denní bázi obtěžuje a bude potřeba ji vyřešit. Zároveň je to věc, kterou nevím, jak vyřešit jednoduše.

Také jsem díky šťourání do inzerátů zjistil, že mi nejspíš celou věčnost správně nefungovaly typy práce u inzerátů přímo z JG. Když u mě někdo inzeroval, nejspíš se na web ani do klubu nezpropagovala informace, zda jde o vedlejší úvazek apod. To se mi tento týden taky povedlo opravit.


## Časopis

Komunikoval jsem s časopisem, do kterého mám psát. Sestavili jsme minulý týden tým externích autorek a autorů. Každý měl do čtvrtka zpracovat nějaký svůj vklad, čemuž jsem se věnoval skoro celý jeden den. Zároveň jsem dal v různých komunitách vědět, že budu pro časopis psát, aby se mi případně zajímaví lidé se zajímavými nápady přihlásili sami. Nabídl jsem i propojení s obchodním oddělením časopisu lidem, kteří zastupují zajímavé firmy na trhu. Z toho já osobně nic nemám, ale karma a kontakty se taky počítají. Dověděl jsem se díky tomu např. o success story, kterou jsem hned přidal na web: [Irena, z asistentky na vedoucí bezpečnosti](https://medium.com/ataccama-life/unlimitedplayground-irenas-story-7fef75e8625). Na základě našich vstupů nakonec šéfredaktorka zavelela a rozdělila úkoly, takže teď je plán jasný a zbývá hlavně psát. Celkově byla tahle činnost hodně velká kopa komunikace a rešerší.


## Další poznámky

- Odstranil jsem [automatickou kontrolu performance aj. věcí pomocí Lighthouse přímo na CI]({filename}/2020-05-11_monitoring-performance-with-lighthouse-and-circleci.md). Začalo to padat a během 20 minut jsem nepřišel na to, co je příčinou. Dokonce to vypadalo na nějaký bug v Lighthouse, nebo podivnost v tom, jak jej spouštím. Jednak se na ty výsledky nedívám a limity mám podle mě dost nízko. Jednak jsem později zjistil, že existuje [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci), který bych měl použít místo vlastního řešení. Nemám teď na nic takového čas, takže jsem to prostě smázl a Lighthouse CI přidal někam daleko do backlogu.
- Volal jsem si s komunitní manažerkou jedné firmy a domlouvali jsme se, co spolu můžeme v budoucnu podniknout.
- Četl jsem _purchase order terms_ ke kontraktu s korporací. Je milé, že moje _liability_ je zastropovaná na $1.000.000, hned jsem klidnější. Vyjasnili jsme si pár věcí, ale v zásadě asi OK. Uvidíme co dál, kolečka se pomalu otáčejí.
- Domlouval jsem nové přednášky. Dvě už mám rozjednané, s některými lidmi jsem se pokusil obnovit starou konverzaci, někdo se dokonce přihlásil sám! Tak se těším, co všechno z toho bude.
- Díky [mému aktivismu](https://github.com/twbs/icons/issues/916) přestane ikona pro lampu v Bootstrap Icons vypadat jako záchod! Taková blbost, zlepší to trochu svět, udělat to může každý.
- Volil jsem [Zelené]({filename}/2021-09-22_volim-marketing.md). Můj povolební komentář je ve [vlákně na Twitteru](https://twitter.com/honzajavorek/status/1446914374078246925). A teď zpátky do práce, přemýšlením nad politikou jsem strávil příliš mnoho času, které jsem mohl věnovat lecčemu jinému. Sice mě to bavilo, ale ke konci už unavovalo a zároveň to bylo ve výsledku celé k ničemu :D Teda k ničemu ne. Zelení mě nakonec pozvali na společné sledování výsledků v jejich štábu, kam jsme se jako rodinka dostavili (s tříhodinovým zpožděním) a dokonce nesměle u piva promluvili s pár lidmi. Celkově mi to dost připomínalo Pyvo, konalo se to na pohodu venku na Štvanici a i na tu zelenou tam došlo.
- Volal jsem si s borcem z LI, který byl nadšený do pomáhání juniorům ze strany byznysu a HR. Takových lidí nemám v klubu zatím moc, alespoň těch aktivních, takže jsme se dohodli, že jej přidám a pak si napíšeme, co by se dalo společně vymyslet dál.
- Během 7 dní od 4.10. do 10.10. jsem při procházkách nachodil 7 km. Celkem jsem se hýbal 4 hodin a zdolal při tom 7 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Začít portovat příručku hledání práce do Markdownu.
2. Domluvit další přednášky.
3. Naučit robota filtrovat pozice? :(


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Česko je skanzen, chováme se jako blázni, úředníci jsou odtržení od reality, říká šéf IPR Boháč](https://www.youtube.com/watch?v=yjjUQ_NB3wE)<br>Perfektní rozhovor o bytech, dopravě, urbanismu, městě.
- [Islám v ČR nechceme. A budoucnost taky ne. Chmury mileniálky nad volební urnou](https://nazory.aktualne.cz/komentare/islam-v-cr-nechceme-a-budoucnost-taky-ne-chmury-milenialky-n/r~2474b92a256611ecb91a0cc47ab5f122/)<br>Klára Votavová popisuje úplně přesně moje aktuální dojmy z české politiky.
- [Volby 2021](http://zbiejczuk.com/blog/2021/10/volby-2021/)<br>Moc pěkně sepsáno.
- [Blog a cookies](https://blog.wuwej.net/2021/10/03/blog-a-cookies.html)<br>Nevěděl jsem, že Google Analytics jde nastavit do módu bez cookies. Zajímavé!
- [Příští volby už budou o klimatu, mladí přemýšlejí jinak, říká exministr](https://www.seznamzpravy.cz/clanek/pristi-volby-uz-budou-o-klimatu-mladi-premysleji-jinak-rika-exministr-176466)<br>„Teze, že u nás není možné postavit energetický systém na obnovitelných zdrojích, není pravdivá.“

<small>Upozorňuji, že to není vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
