Title: Týdenní poznámky: Maják a tunel
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (11.5. — 15.5.) a tak stejně jako [minule]({filename}2020-05-08_prvni-tydenni-poznamky-trizeni-nabidek-prace.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

## Frontendový framework

V různých volných chvílích jsem si o víkendu očima prošel celý [tutoriál na Svelte](https://svelte.dev/tutorial/) a přihodil se mi názor, že to je abstrakce, kterou nepotřebuju. Napadlo mě během toho, jak by se dala udělat stránka s inzeráty i bez složitého JavaScriptu, a dokonce by to pomohlo i SEO.

Potom jsem si četl celé [README Turbolinks](https://github.com/turbolinks/turbolinks/blob/master/README.md) a později se do nich shodou okolností pustil Aleš Roubíček na Twitteru, [tak jsem se ho na ně vyptával](https://twitter.com/honzajavorek/status/1260458654857338881).


## Měření výkonnosti a přístupnosti

V pondělí se mi nechtělo hned z ostra naběhnout do programování parseru nabídek práce a začal jsem menším úkolem. Říkal jsem si, že ať už bude na frontendu nakonec cokoliv, budu chtít, aby byl výkonný a přístupný. Už dřív jsem zahlídl nějaké nástroje, které to umí měřit, ale chtěl jsem je dostat přímo do CI. To se mi povedlo a napsal jsem o tom ve zbylém pondělním čase i [rychlý článek]({filename}2020-05-11_monitoring-performance-with-lighthouse-and-circleci.md). Škoda že to nefungovalo na první dobrou a jak kód, tak článek jsem řešil ještě i celé úterní dopoledne.

To mě nakonec trochu mrzelo. Taková blbost a rozlezlo se to hned na dva dny! Nasdílel jsem to tedy na všechny možné sociální sítě, aby z toho byla aspoň sláva. To mi vzalo další čas. Hlavně proto, že jak Facebook, tak Twitter najednou odmítají načítat náhledové obrázky u mých článků, dokud odkaz ručně neproženu přes [Facebookový debug](https://developers.facebook.com/tools/debug/) nebo [Twitter Card validátor](https://cards-dev.twitter.com/validator). Tenhle problém jsem měl už dřív a podle toho, jak to časově lícuje, to vypadá na nějaký problém na straně GitHub Pages. Když blog hostuju tam, je s tímhle problém. Nevím, jak se toho ale zbavit. Každopádně další propálený čas.

A navíc žádná sláva nepřišla, jen pár lajků a k tomu můj hrdina [@levelsio](https://twitter.com/levelsio/) shodou okolností zrovna celou středu tweetoval o tom, jak je tohle měření zbytečné.

Ve čtvrtek ale přišel s tím, že i přes všechno svoje hejtění předchozí den nakonec svůj projekt optimalizoval na skóre 99 ze 100 :D Na to jsem [odpověděl](https://twitter.com/honzajavorek/status/1260815778070265857), že jsem zrovna napsal článek o tom, jak to skóre udržet, a jemu se to líbilo natolik, že to retweetnul svým 82,1 tisícům sledujících. Jsem slavný! Psaní článku se tedy nakonec vyplatilo, radost se dostavila. Dokonce mi někdo poslal [Pull Request s opravou překlepů](https://github.com/honzajavorek/honzajavorek.cz/pull/96). Jupí!

Akorát pak teda někdo vytáhl, že existuje [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci), nějaké udělátko přímo do CI, které jsem možná mohl přímo použít a nevynalézat kolo. Ach jo! Dál jsem se tomu však už nevěnoval a toto udělátko zatím blíže neprobádal.


## Třídění nabídek a Machine Learning

Pod minulými týdenními poznámkami jsem [na FB probíral možnost třídit nabídky práce pomocí machine learningu](https://www.facebook.com/honzajavorek/posts/10158091079317707). Rozhodl jsem se pro následující postup: Zkusím udělat prototyp základního porozumění tomu, co vyhodí lexer, tj. lidské věty klasifikovat na nějaké "flagy", třeba "Požadujeme minimálně 5 let zkušeností s Javou" na `minimal_experience_gt_1_year`, protože pokud jsem schopen udělat to, zbytek už bude brnkačka. Jestliže se to bude jevit jako nekonečná a neuskutečnitelná práce, nechám toho a raději dopíšu nějaké další stahovače nabídek a doladím lexer, abych měl víc dat. Potom bych kamarády poprosil o pomoc zkusit na ta data poslat mašinky.


## Lexer: Prorážení tunelu, tunelové vidění

Jak jsem psal minule, rozdělil jsem si práci na třídění nabídek práce na:

1. Lexer,
2. sémantickou analýzu obsahu.

Tento týden se nesl ve znamení vylepšování lexeru. Byl téměř hotový z minulého týdne, jen ho chtělo trochu doladit a pak se posunout dál na tu sémantickou analýzu. Jestli vám minulá věta zní jako [ninety-ninety-rule](https://en.wikipedia.org/wiki/Ninety-ninety_rule), tak máte pravdu. Škoda, že jsem si toho na začátku týdne nevšiml já.

Každý den už to vypadalo, že lexer je hotový, ale vždy jsem našel nějakou chybu, nějaká data, na kterých to nefungovalo dobře. Bojoval jsem s nějakými šílenými bílymi znaky nebo třeba s tím, že v inzerátech jsou často prostě jen rozházené `<li>` tagy, bez obalujícího `<ul>`. Všechno jsem vyřešil, na všechno mám test, pro všechno jsem nakonec vymyslel geniální algoritmus. Naprosto mě to pohltilo a když to jen trochu přeženu, dalo by se říct, že jsem kromě programování akorát občas jedl, spal a čmáral pokusy o algoritmy na různé papíry. Když jsem se ze svého _mad scientist_ módu vynořil s hotovým lexerem, který rozklíčoval i nejzapeklitější formátování inzerátu, byl čtvrtek odpoledne.

> Hlavně si to všechno okomentuj a zdokumentuj, ať ten kód pochopíš i za týden.

Výrok mojí manželky, když mě viděla při práci na lexeru. A to není z IT! Takže jsem ještě velkou část čtvrtka dával kód lexeru do takové podoby, aby ho jednou šlo i číst.


### Tipy na psaní parseru

Když zpracovávám změť HTML tagů nebo i čistého textu, kterou se na první pohled může zdát nemožné zpracovat, existují dvě zbraně, které jde použít. První je doménový kontext. Já vím, že v té změti je inzerát na práci, takže vím, co mám hledat. Můžu se dívat po konkrétní struktuře i po obsahu. Druhá zbraň je přepnout mozek a nedívat se na vstup jako stroj, nedejbože HTML parser, ale jako když se člověk dívá na to, co z té změti vykreslí prohlížeč. Člověku je jedno, jestli je něco `<h3>` nebo `<strong>`, vidí to tučně. Stejně tak `<p>` nebo `<br>`, je to nový řádek. Překřížené tagy? No a co. Parser se ve svém chápání vstupu musí co nejvíc přiblížit reprezentaci inzerátu v prohlížeči, nebo ještě lépe reprezentaci, kterou si člověk vytvoří v hlavě, když se na ten prohlížeč kouká. Důležité je, kde bude po vykreslení zalomený řádek, kde bude vizuální odrážka, atd. Takto se dá vyřešit spousta zdánlivě složitých problémů.


## Vymýšlení sémantické analýzy

Už během práce na lexeru jsem přemýšlel nad tím, jak bude vypadat sémantická analýza potom. Ve čtvrtek večer jsem se do toho pustil a během pátku prošel přes několik prototypů. No a nebudete věřit na co jsem přišel!

Já nejspíš ten lexer takhle složitý vůbec potřebovat nebudu, ani ta analýza nebude nakonec zřejmě tak složitá, jak jsem myslel. Když mi to došlo, nevěděl jsem, jestli se mám radovat, protože můžu smazat spoustu kódu a jsem mnohem blíž řešení, nebo jestli mám plakat, protože jsem propálil týden času.

Potřeba komplikovaného lexeru byla založena na hypotéze (říkejme jí hypotéza 1), že abych vyhodnotil nějakou větu v inzerátu, potřebuji znát její kontext. Pokud bude požadavek na univerzitní titul v seznamu "Požadavky" nebo v seznamu "Výhodou", tak to přece dost mění význam. Snažil jsem se tedy pochopit strukturu inzerátů a význam jednotlivých sekcí. Jenže po několika experimentech s analýzou jsem došel k tomu, že vliv kontextu jsem nejspíš dost přecenil a je velmi pravděpodobné, že o sekcích nemusím nakonec vědět nic a bude to stačit (hypotéza 2). No, je osm hodin v pátek večer a nechávám to přes víkend uležet v tomto stavu:

- Třídit nabídky automaticky půjde, a nejspíš mnohem jednodušeji než jsem myslel.
- Třetina lexeru se mi bude hodit tak jako tak, to určitě zbytečná práce nebyla.
- Ještě jsem hypotézu 2 neprobádal dostatečně na to, abych hypotézu 1 mohl definitivně zahodit.


### Poučení

Pozor na padání do _rabbit holes_! Dělal jsem si srandu, že dělám něco, co nejde, ale já nevím že to nejde, takže se mi to udělat povede. Odhodlání překonat jakoukoliv nástrahu mě ale oslepilo a zbavilo nadhledu. Sice se mi povedlo provrtat hlavou skálu a udělat do ní tunel, ale když jsem se objevil na druhé straně kopce, zjistil jsem, že nejspíš existuje cestička kolem.


## Proč třídím nabídky

Nakonec jedna připomínka proč se vůbec snažím třídit nabídky. Stahuji je z několika různých míst. Na všech těchto místech mám vyfiltrováno na juniorní nabídky práce, někdy jsou dokonce přímo označené jako _entry level_, což je přesnější popis té kategorie inzerátů, které chci na JG zobrazovat. A stejně mi tam úplně běžně padají věci jako tohle:

> BS in a technical discipline. MS desirable. At least 5 years experience in software quality.

Nebo tohle:

> At least 5 years’ experience as an iOS mobile developer.

Pokud se mi povede to vytřídit, nebude JG _nejlepší_ místo, kde junior sežene pohromadě relevantní inzeráty, ale prakticky _jediné_.


## JG rank

Ve čtvrtek před spaním mě napadlo, že bude lepší nedělat třídění nabídek úplně černobílé, ale mít nějaké "skóre", které by určovalo jak moc je nabídka juniorní. Skóre by se potom mohlo nejen podílet na vyřazování nerelevantních nabídek, ale i na řazení nabídek ve výpisu. Pracovně jsem si to pojmenoval jako "JG rank". Mohl by být klidně transparentní a každý by hned viděl, proč je jaká nabídka považována za více nebo méně vhodnou pro juniory.


## Další poznámky

- Jeden mentorovací videohovor.
- Zmínka o JG se [poprvé objevila v tištěném médiu](https://twitter.com/pavlina_speaks/status/1258734537254809600?s=21) (pokud vím), a to v časopise Marie Claire. Juchů!
- Hana Klimentová na [Pyonýry](https://www.facebook.com/groups/pyonieri/) hodila [dotazník](http://vyuka-programovani-pro-zacatecniky.hanka.one/public/test) pro začátečníky v programování, který zjišťuje učební styly. Koukal jsem na to, četl si o učebních stylech a celkově jsem s tím jeden den strávil docela dost času.
- Potunil jsem Gulp tak, aby každý reload při vývoji byl trochu efektivnější.
- Zahlédl jsem na Twitteru článek [Second-guessing the modern web](https://macwright.org/2020/05/10/spa-fatigue.html) a zapsal jsem si pár nápadů na článek o frontendu, který chci už dlouho napsat.
- Emma Bostian vydala [článek o tom, jak vydělala $40000 na knížce pro juniory](https://compiled.blog/blog/how-i-made-40000-dollars-on-a-book), ale ještě jsem to nečetl. Taky nemám 105,8 tisíc followerů na Twitteru, takže její strategii asi nebudu moci 1:1 obšlehnout.
- Odebral jsem zatím z třídění nabídek práce podporu pro slovenské nabídky. Chci je tam do budoucna mít, ale teď v mých datech není ani jedna a na nulovém vzorku se těžko ladí nějaká sémantická analýza. Slovenštinu přidám zpět v budoucnu jako separátní úkol, i s nějakým zdrojem slovenských nabídek.
- Vylepšil jsem jak se mi v testech načítají fixtures.
- Napsal jsem si dekorátor, který mi pošle na macOS notifikaci a udělá zvuk, když obalená funkce skončí. Když spustím stahování nabídek práce, už to trvá celkem dlouho, a tohle mi pomáhá si všimnout, že data už jsou ready. Možná o tom napíšu samostatný článek.
