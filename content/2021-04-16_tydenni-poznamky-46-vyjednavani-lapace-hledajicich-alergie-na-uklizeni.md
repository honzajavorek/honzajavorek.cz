Title: Týdenní poznámky #46: Vyjednávání, lapače hledajících, alergie na uklízení
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl další týden (12.4. — 16.4.) a tak [stejně jako minule]({filename}2021-04-09_tydenni-poznamky-45-stehovani-adina-mkdocs-macros.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Vyjednávání

S jednou vzdělávací agenturou je dohoda v procesu, s druhou už jsme se dohodli. Vyjednávání to ale bylo trochu nepovedené, protože jsem zapomněl v předchozí komunikaci dost jasně zmínit, že to co si domlouváme, chápu jako něco, co je součástí jejich placeného členství v klubu. Oni brali věc už za hotovou a já přišel s tím, že bych ale rád nějak dořešil tu platbu za členství. Pak bylo něco jako trapné ticho (to si jen představuju, psali jsme si maily) a následné vysvětlování z mé strany. Než jsme si zavolali znovu a vše si ujasnili, tak jsem z toho teda ani nespal. Vše dobře dopadlo, objasnili jsme si vše a domluvili jsme se v přátelské rovině, ale samozřejmě si připadám jako úplný blbec a představuju si, že oni teď budou u každé mé zprávy pochybovat, jestli jsme 100% na stejné vlně. Snad to časem zažehlíme.

To jen abyste, milí čtenáři, věděli, že když člověk neumí sales, tak nejenže nic neprodá, ale dno to nemá na nule, dno je v mínusu. Neschopnost prodávat může být tak „skvělá“, že může dokonce vztahy poškodit. Naštěstí to celé mělo happy end.


## Lapače hledajících

Velkou část týdne jsem dokončoval Proof of Concept stránek generovaných přes MkDocs a vyráběl „lapače na hledající“. Možná se tomu říká _landing pages_ nebo nějak jinak, nejsem SEO expert, vlastně hlavně doufám, že mě za to Google nevymaže z indexu. Při tvoření těchto stránek jsem si připadal jako nějaký podomní prodejce ve fialovém obleku, který vyhrne rukáv a tam má na předloktí 15 druhů rolexek v případě, že si nechcete sjednat pojištění ani vás nezajímá nová smlouva na plyn. Je ale dost možné, že takto si připadám jen já a je to úplně běžná praktika. Osobně to beru hlavně jako experiment.

Identifikoval jsem sadu nějakých zajímavých klíčových slov a skriptem zjistil, kolikrát je někdo zmínil v klubu na Discordu. Nejdřív jsem ukládal celé zprávy s tím, že třeba nějaké půjde přímo na stránkách ukázat, ale nakonec jsem to zavrhl, protože nelze nijak automaticky vybrat nějakou vhodnou, která by dávala smysl, správně navnadila, nebyla vytržená z kontextu, atd. Navíc jsem vlastně nechtěl, aby zprávy zevnitř klubu visely někde na webu. Co se napsalo v klubu, zůstane v klubu. Čísla jsem ale použil. Učil jsem se přitom s oněmi [MkDocs Macros](https://github.com/fralau/mkdocs_macros_plugin) a celkově i s [MkDocs](https://www.mkdocs.org/) a vymýšlel, jak to celé co nejlépe stavět, i do budoucna pro další stránky. Vyzkoušel jsem si makra a proměnné a tak.

Pak jsem tvořil jednotlivé stránky. Vymyslel jsem jich možná až příliš, při patnácté stránce mě to už moc nebavilo, ale dodělal jsem to tedy. Stránky lapají lidi hledající různé kurzy nebo technologie. V Google Analytics časem uvidím, na které lidi chodí a na které vůbec a jestli to vlastně vůbec někoho přesvědčí jít do klubu, nebo aspoň zůstat na JG a pročítat si tam moudra. Teď to nechám uležet a vsáknout se do vyhledávačů a uvidím.

Posloužilo to dobře jako něco, na čem jsem si mohl hned vyzkoušet MkDocs. Teď bych na MkDocs měl ideálně aspoň sem tam překlápět i existující stránky, abych časem mohl kompletně přejít na nový backend. Nevymyslel jsem lepší místo na odkazy na jednotlivé stránky, než patičku webu, takže je v ní teď trochu odkazový binec, ale to se dá časem vylepšit. Blbé je, že ty odkazy jsou v hlavní šabloně webu, a ta nejde sdílet mezi MkDocs a Flaskem, tu jsem musel rozkopírovat a pro každý backend trochu upravit. Výsledkem ale je, že tyhle odkazy tam teď píšu ručně a to ještě dvakrát do každé z těch hlavních šablon. Bylo to trochu ubíjející, nicméně asi zatím rychlejší, než kdybych se to snažil řešit programováním.

Do budoucna jsem chtěl mít na webu stránky pro různé technologie nebo profese, takže teoreticky by se časem mohly vyvinout z těchto lapačů. Zatím jsou lapače jen s minimem textu a jedním tlačítkem, ale když se osvědčí, mohu na nich zapracovat, včlenit je lépe do webu, přidat k nim kvalitnější obsah. Například co je SQL a jak se ho naučit. Reklama na klub by pak mohla být jen doplňkem a ne hlavním sdělením takové stránky. Je to něco, na co se teď trochu upínám ve svých myšlenkách, abych si nepřipadal úplně jako ten podomní prodejce.


## Alergie na uklízení

Předávali jsme starý byt a při jeho uklízení a malování jsem se nadýchal velkého množství prachu. Z toho jsem měl záchvat kašle, který se nelepšil. Navazovalo to na už zhruba týden trvající nalomení zdraví, které jsem pociťoval, ale vždy se nějak ztratilo (takže jsem si šel klidně o víkendu zaběhat a v pohodě). Do toho stres z vyjednávání a z odevzdávání bytu. Následující noc jsem nemohl moc dýchat a kašlal jsem. Po probdělé noci jsem se diagnostikoval přes internet na bronchitidu, kterou ale umí způsobovat i covid-19, takže jsem šel hned na antigenní test a po telefonické konzultaci s doktorkou i na PCR. No, covid-19 nemám a to, co jsem měl, jsem následující dny vyležel. Ještě nejsem 100% ok, ale programovat se s tím dalo a domlouvat spolupráce taky.


## Videa

Budu natáčet krátká videa! Rozbíhám spolupráci na jedné straně se vzdělávací agenturou a na druhé straně s kamarádem. Videa by měla doplnit příručku a celkově rady na JG, protože ne každému se chce číst tuny textu. Uvidíme, jak to půjde, těším se, je to pro mě zase nějaké nové dobrodružství.

Z videí mám trému a tak si je sám přivozuji jen velmi nerad, ideální je, když mě někdo někam pozve. Před přednáškami mívám velkou trému, a to dokonce i před přednáškami v klubu, které má někdo jiný a ne já :D Teď se mi stalo, že se ozvaly hned dvě strany, které by udělaly videa se mnou, no a v týmu to už většinou nějak zvládám, na natáčení kývnu a připravím se. Kdyby ale bylo na mé převážně introvertní duši, tak raději napíšu 4 tuny textu :)


## Další poznámky

- Na úřadě Prahy 3 jsem čekal 2 hodiny ve frontě na změnu trvalého pobytu.
- Dal jsem lepší fotku k [příběhu Pavla z Olomouce](https://junior.guru/motivation/#stories).
- Přidal jsem se na [Discord Elements of AI CZ](https://discord.com/invite/gbEyJEqwSD), o kterém se psalo někde na CzechCrunch, ~~abych měl vlevo ve svém Discordu víc bublinek serverů a byl větší Discordový boss~~ abych se podíval, jak mohou fungovat i jiné české Discordy o programování. Nic moc se tam neděje.
- Samotné Outreachy [retweetovalo můj tweet o rozhovoru s Lenkou Segura](https://twitter.com/outreachy/status/1380226212832800769). Juchů. Mají 13.7K followers, ale nikdo mě díky tomu sledovat nezačal, protože to zajímavé, co dělám, je jen česky. Tak snad aspoň pár lidí díky tomu přišlo na ten CyberMagnolia blog.
- Poslal jsem daňové přiznání a přehledy pojišťovnám.
- O víkendu se mi Adina ozvala, že má zdravotní nesnáz, který ji diskvalifikuje z přednášení, takže jsem úterní přednášku v pondělí přesunul o dva týdny. Internet jsem s tím už nespamoval, jen interně klub, což mělo za následek, že pak přednášku v původním termínu promovala DigiKoalice na FB, ale zachytil jsem to a nechal opravit. Adina tedy bude v klubu 27.4., těste se těšte, její přednáška bude totiž nejspíš i částečně interaktivní.
- Domlouvám do klubu první AMA session s recruiterem. Myslel jsem, že bych to nějak nacpal do příštího týdne, aby se něco dělo než bude Adina, ale jak jsem řešil jiné věci a chorobu, tak jsem to nezvládl a nebude nic. Bude to někdy později. Domlouvám taky přednášku na téma „Život HTTP(s) požadavku“, která bude na témata jako text vs binární protokol, DNS, TLS, TCP, UDP, IP, OSI model, wifi, ethernet, prostě síťové základy, které se mohou hodit každému, kdo se sítí něco někdy dělá, ať už je to frontend, backend, testování…
- Prošel jsem a okomentoval kamarádův byznys plán pro jeho plánovanou mobilní aplikaci.
- Zjistil jsem, že když v jednom procesu spustím a ukončím asyncio event loop (viz článek tady na blogu [How to create a non-interactive Discord bot]({filename}2021-02-06_how-to-create-non-interactive-discord-bot.md)) a potom to chci udělat znova, jsem nahraný, protože loop je už ukončená. Jenže ve svých skriptech, které stahují data z Discordu, potřebuji přesně tohle udělat. Nakonec to vyřešilo použití `asyncio.new_event_loop()`, viz [commit](https://github.com/honzajavorek/junior.guru/commit/d82b2a869f43b28bd1fd5ea48e8494f958e25080).
- Na JG jsem přijal novou nabídku práce, kterou někdo poslal. Tentokrát neplacenou, komunitní. Pokud byste to náhodou nevěděli, na JG [můžete přidávat nabídky práce i zadarmo](https://junior.guru/hire-juniors/), pokud jste třeba jen malá firmička, tým studentů, je to nějaká stážička, brigáda, máte nějakou spolupráci s PyLadies, apod.
- Díky předchozím poznámkám se ozval známý s tím, že by si rád přečetl co připravuju s certifikátama, že by k tomu třeba taky měl nějaké moudro. Tak možná to nakonec nějak s lidma poskládám, i když o tom sám vím teď spíš prd :)
- Naučil jsem se slovní spojení [mat prsy](https://www.facebook.com/groups/967870373283278/permalink/5287774447959494/?comment_id=5288090741261198).
- Připojil jsem se na Frontendisty o vzdělávání, ale nestihl jsem přednášku, která mě zajímala nejvíc :) Třeba si to ještě pustím [ze záznamu](https://www.youtube.com/watch?v=VczYbGFfnI8&t=692s).
- Udělal jsem review na Mílův Pull Request na JG, ve kterém přidává první ML magii (viz před-předchozí poznámky).
- Navštívil jsem online [meetup](https://pynamibia.herokuapp.com/meetup/) v mé milované Namibii. Bylo super vidět po delší době známé z mé loňské návštěvy [PyCon NA](https://na.pycon.org/) (letos bude online a CfP je ještě otevřené!). Třeba Daniele, který [teď hledá nové angažmá](https://twitter.com/evildmp/status/1382021178592800768/retweets/with_comments), [Muheue](https://www.blog.pythonlibrary.org/2021/04/05/pydev-of-the-week-ngazetungue-muheue/), [Jessica](https://twitter.com/JessicaUpani), nebo [Vuy](https://vuyisile.com/blog/). Mimochodem, pokud máte nějaký peníz navíc, můžete s ním udělat kopu radosti [tady na tom Patreonu](https://www.patreon.com/pythonnamibia). Obnos, který v Karlíně vystačí na latéčko, naučí v Namibii dítě programovat. Lidi za touto sbírkou osobně znám a mohu se za ně zaručit.
- Upravil jsem kontrolu toho, zda mi spadly scrapery pracovních nabídek. Předtím to nekontrolovalo chyby, které se nepovedlo zachytit :D Jenže když jsem je začal chytat, zase to bylo moc přísné. Ony totiž ty scrapery zalogují error i když se třeba nepovede scrapnout jednu nabídku, protože server vytimeoutoval. Což mě osobně moc netíží. Ale zase kdyby toho bylo hodně, asi by to byl příznak nějakého problému. Tudíž jsem dodal podmínku, že to spadne jen ve chvíli, kdy těch errorů je víc. Zatím jsem dal pocitovou hranici na 5 %, tedy pokud je počet errorů vůči počtu všech nabídek větší než 5 %. Nevím, jestli to vlastně není moc velkorysé, uvidím. Každopádně asi lepší než nic.
- Během 7 dní od 10.4. do 16.4. jsem naběhal 10 km, na túrách nachodil 8 km. Celkem jsem se hýbal 5 hodin a zdolal při tom 18 kilometrů. Ve skutečnosti teda jen minulý víkend, přes týden jsem nedělal nic a pak jsem odpadl.
- A nejzásadnější milník tohoto týdne: Do klubu se přidal Justin Bieber!

![Justin Bieber]({static}/images/justinbieber.png)


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Ověřit, že nejdůležitější instituce si všimly, že mám nové bydliště, případně jim ho nahlásit.
2. Finalizovat spolupráci s oběma vzdělávacími agenturami, přidat loga na web, apod.
3. Připravit a ideálně i začít překopání [ceníku pro firmy](https://junior.guru/hire-juniors/) a poté stránky s [klubem](https://junior.guru/club/).

Bonus: Přidat někam na JG kapitolku o tom, jestli jde programovat na mobilu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Víc orgasmů, pláče i volného času. Proč se vyplatí randit s feministkou](https://www.idnes.cz/onadnes/vztahy/feminismus-feministky-rovnopravnost-vztahy-randeni.A210324_184857_ona-vztahy_vlc)
- [Small tech](https://scattered-thoughts.net/writing/small-tech/)<br>Příklady produktů/projektů, které jsou úspěšné a uživí se i přesto, že jsou za nimi malé týmy a žádní investoři. Chybí mi tam curl.
- [Bilance](https://www.ceskatelevize.cz/porady/14021364946-bilance/221452801250002-bilance-kolaps-recyklace-plastu/)<br>Jsme v ČR skvělí v třídění plastů. Super! Bohužel jsme naprosto mizerní v recyklaci plastů, takže to třídění tak trochu ztrácí smysl.
- [Surely We Can Do Better Than Elon Musk ❧ Current Affairs](https://www.currentaffairs.org/2021/04/surely-we-can-do-better-than-elon-musk)<br>Kritika Elona Muska. Zajímavé doplnění bezhlavého oslavování jeho osoby a všeho, co dělá.
- [Redneck #47: Jak se v USA (ne)chodí k volbám?](https://a2larm.cz/2021/04/redneck-47-jak-se-v-usa-nechodi-k-volbam/)<br>O tom, jak se volí a volilo v USA. Zajímavá sonda do úplně jiného světa. Americká ústava například právo volit nikomu nezaručuje, neexistuje nic jako občanky, apod.
- [Krize a zánik vlastnictví](https://www.marigold.cz/item/krize-a-zanik-vlastnictvi)<br>„Vznikne pronajatý život, který bude pro chudé drahý a ze kterého bude obtížné uniknout.“
- [PyDev of the Week: Ngazetungue Muheue](https://www.blog.pythonlibrary.org/2021/04/05/pydev-of-the-week-ngazetungue-muheue/)<br>Muheue je úžasnej. Měl jsem tu čest s ním před rokem strávit několik týdnů a je to člověk s velkou energií a vytrvalostí.
- [Everyone Is Beautiful and No One Is Horny](https://bloodknife.com/everyone-beautiful-no-one-horny/)<br>Zajímavý článek o tělech a popkultuře. Hromada generalizací a rychlých závěrů „k zamyšlení”, na kterých něco je.
- [Choose Boring Technology](http://boringtechnology.club/#17)

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
