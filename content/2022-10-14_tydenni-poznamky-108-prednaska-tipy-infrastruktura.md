Title: Týdenní poznámky #108: Přednáška, tipy, infrastruktura
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl zase nějaký ten týden (8.10. — 14.10.) a tak [stejně jako minule]({filename}2022-10-07_tydenni-poznamky-107-rozjizdeni-prednasek-opravy-vseho-mozneho.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Přednáška v klubu: Pavel Šabatka

Ve středu byla po dlouhé době přednáška v klubu. Pavel Šabatka z [House of Řezáč](https://www.houseofrezac.com/) mluvil o tom, kdo je webový analytik a jak se jím stát. V průběhu odpoledne jsem zjistil, že moje checklisty toho, co a jak dělám, jsou neaktuální a nezahrnují poslední změny, které jsem dělal ohledně streamování na YouTube apod. Kvůli tomu jsem ztratil nějaký čas a byl jsem pak i nervózní, co ještě jsem kde zapomněl.

Když se Pavel připojil, řekl mi, že pozval kolegyni, aby se připojila taky, pod jeho účtem. Řekl jsem, že každý má 2 týdny zdarma, tak ať se klidně registruje za sebe, ale ze zvědavosti jsem šel na mobil a zkusil ze svého účtu jít do Discord callu, zatímco jsem na něm byl z počítače. Tím jsem rozstřelil nějaké nastavení a následujících 10 minut jsme řešili, že mě Pavel neslyší.

Když jsme to vyřešili, zmáčkl jsem omylem ve stresu nahrávání místo streamování. Měl jsem tedy záznam, ale kdyby se připojilo více jak 25 lidí, bohužel by přednášku vidět nemohli. Také jsem tím spláchl asi půl hodiny příprav a přidělal si další půlhodinu nahrávání a upravování záznamu na YouTube po skončení přednášky.

25 lidí nehrozilo, dorazilo jen pár lidí, což mě trochu mrzelo. Uvidím, jak se povede návštěvnost přednášek rozdmýchat v dalších týdnech. Vím, že si to hodně lidí pouští ze záznamu, ale i tak. Pavel si s tím dal práci, přednáška byla dobrá, jeho kolegyně Katka tam říkala hodně dobré věci, celé to bylo fajn, čekali na dotazy. Bohužel tohle prostě neovlivním, lidi na přednášky upozorňuji, řekl bych, až skoro nadměrně.


## Práce na tipech pro nové členy

Mám pocit, že tipy a celý onboarding dělám už celou věčnost. Kvůli tomu mě to už trochu přestává bavit. Nevím, jestli tomu mám rychle najít nějaký konec a dodělat to jen v rámci určitého _scope_, nebo prostě zatnout zuby a pokračovat spolu s tím, že pro rozptýlení se občas podívám na jiné, méně důležité úkoly.

Napsal jsem dva tipy, jeden o tom, aby se lidi nebáli ptát na věci ve veřejných kanálech, druhý o tom, že mají preferovat veřejné kanály oproti soukromým zprávám. Ten druhý vyvolal nějaké reakce a zjistil jsem, že může existovat spousta lidí, kteří Discord a celkově chat používají úplně jinak, než já nebo Dan. Vedli jsme ohledně toho dlouhou (ale zcela konstruktivní) debatu, která mě přesvědčila, že soukromé zprávy se nemám nijak snažit omezovat a že to vlastně ani nejde. Tip jsem stáhl a napíšu ho jinak, víc jako doporučení a nastínění výhod a nevýhod různých přístupů.

Jsem teď přesvědčený, že pokud chci, aby lidi víc psali veřejně, musím zapracovat na [psychological safety](https://en.wikipedia.org/wiki/Psychological_safety) v klubu a na institucionalizovaných příležitostech, kde půjde přispět i jednoduše a malinko.

Následně jsem napsal ještě další dva tipy, jeden žádající lidi o feedback a druhý o placení v klubu. V tom prvním se ptám lidí na tři věci:

- Díky čemu nebo komu víš, že junior.guru existuje? Google? Doporučení? Sociální síť? Podcasty?
- Co se ti tu líbí? Co tě příjemně překvapilo? Co si nejvíc užíváš?
- Co ti tu chybí? Co se ti tu nelíbí? Co by šlo vylepšit? Z čeho máš blbý pocit?

Tím se konečně dostávám k tomu, abych zjišťoval data, která potřebuji pro překopání svého marketingu. Zatím jich moc neodpovědělo. Mám podezření, že vlastně lidi ty tipy přestali trochu číst. Je to ale pouze pocit, možná kdybych měl nějaká čísla, tak to vidím jinak. Časem se musím zamyslet, jestli neposílat víc kratších tipů než méně delších, nebo jestli lidem tipy nepřipomenout, pokud o ně třeba týden nejeví zájem, protože je mohou ignorovat i omylem, nejen záměrně.

Upravil jsem _allowed mentions_ v tipech tak, aby tam byli všichni, koho tipy označují (abych nějak řešil [problém popsaný tady](https://github.com/discord/discord-api-docs/issues/2126)), kromě moderátorů (aby nedostávali zbytečné notifikace). Nevím, jestli to pomohlo a v tipech se budou označení lidi zobrazovat jménem a ne číslem, nicméně víc už pro to udělat nemůžu.

Pozitivní je, že jsem vlastně tento týden dokázal, i přes veškerou prokrastinaci a další úkoly, sepsat čtyři nové tipy.


## Šťourání do infrastruktury

Při pátku už se mi nechtělo psát zase tipy, tak jsem si řekl, že se podívám na chybu SQLite _database disk image is malformed_, která mi shazuje build na CI. Děje se to jen občas, ale dost pravidelně. Děje se to zhruba od doby, co jsem nasadil novou verzi robota na pracovní nabídky, tedy po paměti asi od února nebo března. Celou tu dobu se to děje a já to neřeším.

Koukáním na buildy jsem zjistil, že se to asi děje každé pondělí. Děje se to v nightly buildu na hlavní Git větvi, ale i pro větve, které vzniknou díky dependabotu. Je to zvláštní. Pondělí se nijak neliší od jiných dní, akorát se posílají maily inzerentům. Že by to nějak ovlivňovaly? Bude to nějaký problém s kešováním nebo ukládáním dat mezi jednotlivými fázemi buildu na CircleCI.

[Tady na SO](https://stackoverflow.com/a/5275022/325365) jsem našel tuhle větu, kterou si sem odložím, ale podle mě to není můj případ:

> You should not use traditional backup tools for SQLite (or any other database, for that matter), since they do not take into account the DB state information that is critical to ensure an uncorrupted database. Especially, copying the DB files in the middle of an insert transaction is a recipe for disaster...

Přidal jsem několik debugovacích výpisů a teď asi nezbývá, než čekat na pondělí a celkově to víc pozorovat. Použil jsem [sqlite-utils](https://sqlite-utils.datasette.io/) od svého oblíbence [Simona Willisona](https://simonwillison.net/), abych nad databází pustil nějaké příkazy mimo svůj kód a abych ji optimalizoval před tím, než se bude zálohovat.

Při koukání na buildy jsem si všiml, že mi samo CircleCI radí, [abych si zvýšil _resourceclass_](https://circleci.com/docs/configuration-reference/#resourceclass), což jsem neznal. Zjednodušeně je to způsob, jak CircleCI říct, že má na určitý úkol pustit mašinu těžšího kalibru. Díky silnějšímu CPU a více paměti se pak věc stihne rychleji. Tak jsem to tam do několika míst dal. V souvislosti s tím jsem si všiml, jaké vymakané grafy teďka na CircleCI jsou, fakt dobrý:

![CircleCI Timing]({static}/images/circleci-timing.png)

![CircleCI Resources]({static}/images/circleci-resources.png)

Taky jsem si při tom všiml, že bych měl možná pořídit nějakou tu CDN, protože mi CircleCI lehce naznačuje, že si tam ukládám něco, co bych si měl ukládat spíš jinam, ehm:

![CircleCI Storage]({static}/images/circleci-storage.png)

Když k tomu připočítám podcast a generované obrázky, které mi zabírají čím dál tím víc místa někde v Git repozitářích, možná by se fakt CDNka hodila. Nejspíš jsem teď ale líný to řešit. Taky je asi možnost nějak se domluvit v [CDN77.com](https://www.cdn77.com/), když už JG podporují. Netuším, jaké jsou jejich výhody nebo nevýhody oproti jiným řešením, ale tuším, že pro účely JG to bude fuk. Na obrázky teda už teď používám [Cloudinary](https://cloudinary.com/), v rámci jejich tarifu zdarma, ale to je trochu něco jiného.

Když už jsem se šťoural v tom CI, napadlo mě, že zbytek pátku využiju na to, abych (opět) překopal způsob, jakým se pouští skripty na JG. Relativně nedávno jsem zaváděl [invoke](https://www.pyinvoke.org/) místo už-ani-nevím-čeho, ale spokojený jsem s tím nebyl. Zřejmě jsou mé potřeby už dost specifické. A to, co dělá invoke dobře, už by se dal stejně dobře použít i [click](https://click.palletsprojects.com/), který je podle mě mnohem méně magický.

Aktuálně jsem do clicku přepsal vše kromě té největší části, která má na starost spouštění skriptů na CI a stahování a synchronizaci všech dat. Bylo to dost jednoduché a už teď se těším, až přepíšu i tu složitou část. V novějších verzích clicku jsou navíc věci, které se mi budou hodit:

- [Custom Multi Commands](https://click.palletsprojects.com/en/8.1.x/commands/#custom-multi-commands)
- [Multi Command Chaining](https://click.palletsprojects.com/en/8.1.x/commands/#multi-command-chaining)
- [Group Invocation Without Command](https://click.palletsprojects.com/en/8.1.x/commands/#group-invocation-without-command)
- [Invoking Other Commands](https://click.palletsprojects.com/en/8.1.x/advanced/#invoking-other-commands)

Cílem změn bude, abych mohl:

- Pustit například `jg sync podcast` a ono by mě to upozornilo, že tahle věc závisí na `jg sync club-content` a jestli náhodou nechci spustit nejdřív to, nebo ať si `podcast` teda na vlastní nebezpečí spustím bez toho, pokud si myslím, že data z `club-content` mám dost čerstvá. Toto je něco, co teď JG neumí a při vývoji mi to háže klacky pod nohy doslova každý den.
- Pustit například `jg sync events --flush-images`, aby se přegenerovaly všechny plakátky k akcím v klubu. Tohle teď JG taky neumí a patlám to přes nějaké environment proměnné.
- Automaticky paralelizovat při výoji i na CI stahování věcí, které na sobě nezávisí, ale zároveň aby se dodržovalo pořadí věcí, které na sobě závisí. To znamená, že možná budu mít i separátní databáze pro každý skript a pak je budu nějak spojovat, ale kdo ví.
- Využít nějak [vestavěné paralelizace na CircleCI](https://circleci.com/blog/a-guide-to-test-splitting/)! Sice nepotřebuji paralelizovat testy, potřebuji to udělat se skripty, ale to by mohlo být celkem jedno, princip je stejný.

Už mě nebaví, jak mi buildy jedou 40 minut. Jasně, něco by šlo optimalizovat a zrychlit, ale něco prostě zrychlit nepůjde, protože se tam stahuje hodně věcí, nebo se dělá hodně věcí přes Discord API. Potřebuji ty skripty pouštět vedle sebe a ne za sebou, jak jen to půjde.


## Zapojení dvou juniorek do open source

Povedlo se mi shodou okolností motivovat hned dvě juniorky do práce na open source. Snažil jsem se dělat review a odpovídat na zprávy, ale stejně mám pocit, že to většinou stálo na mně. Lepší už to nebude.

Markéta se [pustila do opravy jednoho skriptu](https://github.com/pyvec/docs.pyvec.org/pull/292), který nám v Pyvci pomáhá dokumentovat udělené granty.

Mia přepsala [mého Pyvo bota](https://github.com/honzajavorek/pyvo_bot) do Pythonu a vytvořila [pyvec/pyvo-bot](https://github.com/pyvec/pyvo-bot/). V průběhu týdne jsme si ověřili, že funguje, zpráva přišla :)


## Sociální sítě a Mimo agendu

Přestávají mě bavit sociální sítě. Poslední hřebíček byl [článek Jakuba Zelenky](https://mimo-agendu.ghost.io/nasel-jsem-recept-na-twitter/), kvůli kterému jsem si dokonce konečně Mimo agendu předplatil. Při čtení dalších jeho článků jsem si uvědomil, jak mě vlastně nebaví ani zpravodajství. Rezonoval se mnou i [rozhovor na Prostoru X](https://www.reflex.cz/clanek/prostor-x/114555/budar-herectvi-mi-prestalo-davat-smysl-ceske-komedie-me-nebavi-ani-jako-divaka-smrt-v-sobe-mame-vsichni.html), kde Budař mluví o tom, jak vůbec nesleduje politiku. Celé to ještě zpracovávám, žádný závěr z toho nemám. Po nocích jsem četl další Jakubovy články, např. o TikToku a mám v hlavě spoustu myšlenek a otázek. Debatoval jsem pak i s Jakubem a dalšími na jeho Discordu.

Láká mě výrazně si sociální sítě omezit a z některých třeba úplně odejít. Zároveň to nemůžu udělat, protože sociální sítě jsou pilíř marketingu mého projektu. Junioři mě ještě možná najdou přes Google, ale firmy žhavím podle mě hlavně přes LinkedIn. Možná budu primárně používat ten a řešit tam jen práci?

[Napsal jsem o svém zpruzení na sociální síť](https://twitter.com/honzajavorek/status/1579932185750298624) a lidé mi odepisovali strategie, ve kterých věnují mnoho energie na to, aby si své sociální sítě nějak čistili a upravovali a odplevelovali. Jednak to taky dělám a zjevně to nepomáhá, jednak je otázka, zda chci něčemu takovému vůbec věnovat čas? Co mi vlastně sociální sítě dávají kromě (v případě neplaceného, stále mizernějšího) dosahu pro moji propagaci JG?

Možná je to jen nějaké pokračování mého vyhoření ze sociálních sítí, když jsem je začal víc používat pro práci. Možná jsou opravdu hodně jiné, než dřív, a možná jsem si toho konečně všiml. Možná jsem zklamaný, že nic, co se na sociálních sítích psalo, se ve výsledku nepromítlo do voleb, a proto mi ve výsledku přijde zbytečné s nimi trávit čas. Reálný svět je totiž nakonec asi opravdu někde jinde, tam venku.

Zjistil jsem, že Instagram jde používat z webu na noťasu a konečně lze takto i nahrát obrázek. Dokonce, když jdu do devtools v prohlížeči a přepnu se jakoby na mobilní prohlížeč, tak mohu nahrát i storíčko. Nelze ale např. nasdílet svůj post jako storíčko apod. Bez ohledu na to jsem zajásal a IG si úplně odinstaloval z mobilu.

Hlavně pro zlepšení produktivity jsem si začal sociální sítě během většiny dne blokovat přes `/etc/hosts`. Jsem zvědav, jak dlouho mi tohle vydrží.

Aby to bylo kompletní, [objevil se](https://twitter.com/honzajavorek/status/1580656545003491328) jeden můj zarytý twitterový fanoušek. Je to myslím jeden ze tří lidí, které si tam blokuju. Pořád mi něco psali, aniž by to dávalo smysl, nebo aniž bych jich prosil o názor.


## Další poznámky

- Kromě [veřejného iCalendar exportu přednášek](http://junior.guru/api/events.ics) jsem vytvořil ještě jeden, který je přímo pro mě. Označí mi v kalendáři výrazněji každý den, kdy je přednáška a v ten den mi automaticky na dopoledne přidá několikahodinový blok, kdy se věnuji rodině jako náhradu za večerní absenci.
- Třídění akcí [na webu](https://junior.guru/events/) fungovalo na bázi dní a ne času. Stalo se, že mi běžel build krátce po přednášce a zjistil jsem, že pak rozdělení na plánované a archivované nefunguje dobře a něco i spadne. Opravil jsem to tak, aby se pracovalo s `datetime` místo `date`.
- Vyladil jsem některá doporučení pro členy v klubu, aby používaly české názvy Discord UI a anglické vždy až v závorce. Díky nedávné anketě v klubu totiž vím, že většina lidí používá Discord s českým UI.
- Opravil jsem nějaké chyby v [informacích pro přednášející](https://junior.guru/speaker/).
- Upravil jsem skripty, které do některých kanálů na Discordu posílají pravidelná upozornění, aby při každém novém vždy smazali předchozí upozornění. Díky tomu se nebudou kanály plevelit těmito automatickými zprávami.
- Udělil jsem jedno stipendium.
- Sdílel jsem [informace o akci](https://bit.ly/3e8lGdm), kterou pořádáme společně s Ataccama, a to do klubu, na všechny svoje sociální sítě a na všechny možné Facebook skupiny.
- Psal jsem si s [Lukášem Augustou](https://www.lukasaugusta.cz/) o jeho nové službě [Landing page odshora až dolů](https://www.designui.cz/landing-page-odshora-az-dolu?referral_code=31kql18) a dělal jsem jí i trochu promo v klubu.
- Během celého týdne jsem ladil detaily ohledně přednášek, ať už těch naplánovaných, nebo nových. Tisíc drobných editací souboru [events.yml](https://github.com/honzajavorek/junior.guru/blob/main/juniorguru/data/events.yml), maily firmám s prosbou o logo, apod.
- Odpovídání v klubu, maily, a tak dále. Komunikoval jsem docela s lidmi na LinkedIn, ať už kvůli přednáškám nebo spolupráci. Ozval jsem se několika firmám, kterým brzy vyprší nebo nedávno vypršela spolupráce v klubu.
- Během 7 dní od 8.10. do 14.10. jsem při procházkách nachodil 9 km. Celkem jsem se hýbal 4 hodiny a zdolal při tom 9 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/). Nabídky práce pro juniory teď inzerují: [Monitora media, s.r.o.](https://junior.guru/jobs/2b1ab731247b03b291bd7c4a0177e052df5ae4a5937144b4f2ce9d11/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/215426887eaaad9105ecf647d0ff24cf94de7c9eb47cc6f2c55e6921/)


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Zvládnout v úterý další přednášku v klubu.
2. Dokončit rozvrtané spouštění skriptů a plně přejít z invoke na click.
3. Napsat zase nějaký ten tip pro nováčky v klubu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Královec jako vtip i klíčové území. Pro NATO představuje problém, upozorňuje politický geograf](https://www.mujrozhlas.cz/rapi/view/episode/7b559a7e-0704-3e68-9c32-b09f888b3bee)
- [Z Hongkongu na Baltu přístavem v kleci. Jak se Kaliningrad ocitl na periferii Ruska a Evropy](https://www.voxpot.cz/z-hongkongu-na-baltu-pristavem-v-kleci-jak-se-kaliningrad-ocitl-na-periferii-ruska-a-evropy/)<br>Taky fajn komentář ke Královci.
- [](https://ecfr.eu/article/the-case-for-a-confederal-europe/?amp=)<br>Tohle by se mi líbilo.
- [„Lithium bude důležitější než zemní plyn.“ Evropa se probouzí do nové energetické geopolitiky](https://www.voxpot.cz/lithium-bude-dulezitejsi-nez-zemni-plyn-evropa-se-probouzi-do-nove-energeticke-geopolitiky/)<br>„Lithium a vzácné zeminy se brzy stanou důležitější než ropa a plyn. Jen naše potřeba vzácných zemin se do roku 2030 zpětinásobí.“
- [How does the Russo-Ukrainian War end?](https://snyder.substack.com/p/how-does-the-russo-ukrainian-war?r=f9j4c)<br>Snyder nastiňuje jeden z pravděpodobných scénářů dalšího vývoje v Rusku.
- [Komentář: Invalidní umění v Karlíně. David Černý ve službách korporátní architektury](https://www.seznamzpravy.cz/clanek/kultura-invalidni-umeni-v-karline-david-cerny-ve-sluzbach-korporatni-architektury-216421)<br>Ha ha! Kromě NIMBY pasáže pěkný text, dobře Černého „rozmazal“.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu jsem použil vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
