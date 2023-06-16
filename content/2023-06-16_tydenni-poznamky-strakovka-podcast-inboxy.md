Title: Týdenní poznámky: Strakovka, podcast, inboxy
Image: images/img-4187.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-06-01_tydenni-poznamky-dovolene-spousta-drobnosti-a-build-frontendu.md) už utekl nějaký ten týden (1. 6. až 16. 6.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Strakovka]({static}/images/img-4187.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Dovolená

První delší rodinná dovolená v zahraničí byla fajn.
Neměli jsme raději žádná velká očekávání.

Letěli jsme do Itálie.
Měl to být kompromis válení a poznávání, což se nakonec asi povedlo, akorát naše dítě se moc válet neumí, takže bychom teď svým způsobem potřebovali asi další dovolenou, ideálně s babičkou 😀

![Pláž]({static}/images/img-3896.jpg)

![Hřiště]({static}/images/img-4127.jpg)

Rozhodně to splnilo účel v tom, že jsme to nějak prolomili a nabrali nějaké _know how_ ohledně toho, co obnáší dovolená s dítětem a na co si dát příště pozor, nebo co není vůbec problém.

Mě se zase povedlo si snad poprvé od roku 2019 plně odpočinout na celý týden od práce.
Na junior.guru jsem vůbec nemyslel, prací se nezabýval, Discord jsem ani jednou neotevřel 💆‍♂️
A světe div se, nic se nezhroutilo!
Příjemné.

## Schůzky

Tento týden jsem měl hned čtyři schůzky:

-   V úterý na Úřadu vlády, tzn. ve Strakovce.
    Tam jsem se sešel se dvěma členkami týmu pod Ivanem Bartošem, které připravují Czech Digital Week.
    To má být velká akce pro veřejnost v listopadu tohoto roku.
    Výsledkem schůzky je, že na této akci se budu podílet jak jen budu umět.
    Kontakt na mě jim dali z [Česko.Digital](https://cesko.digital/), čímžto jim převelice děkuji!
-   Ve středu jsem šel ke kadeřníkovi.
-   Spolu s [Lucií Tvrdíkovou](https://www.linkedin.com/in/lucietvrdikova/) mě Jurij Starynec pozval do svého podcastu [IT svět podle Jury](https://www.starynec.cz/category/vsechny-clanky/podcasty/), takže tam jsem šel natáčet hned po kadeřníkovi.
    Souběh s termínem kadeřníka je čistě náhodný, netočilo se video 😀
    Rád jsem Lucii i Juru poznal osobně.
    Lucii jsem hned pozval i do klubu.
    Na podcast jsme si s Lucií připravili spoustu nějakých diskuzních okruhů.
    Natáčení bylo dlouhé.
    Přišlo mi, že přeskakujeme od jedné věci k druhé, že zůstává spousta věcí nedořečeno a že je to chaos, ale naštěstí vím, že s odstupem a po sestříhání tyhle věci dopadnou většinou nakonec dobře.
-   Ve čtvrtek jsem šel na návštěvu do Mews.
    Tam jsem se seznámil s jejich novou „komuniťačkou” a spolu s Janem Meissnerem jsme probrali směřování další spolupráce.
    Vzápětí jsem poslal do Mews fakturu 😏
    A těším se, jak spolu zase od základů překopeme mentoring v klubu, jako každý rok 😀

## Co je Czech Digital Week?

Tady jsou dva slajdy, které asi nejlíp vysvětlují, co bude CDW.

![Slajd 1]({static}/images/screenshot-2023-06-13-at-15-47-45-vyznam-digitalniho-vzdelavani-pro-czech-digital-week.png){: .img-thumbnail }

![Slajd 2]({static}/images/screenshot-2023-06-13-at-15-48-39-vyznam-digitalniho-vzdelavani-pro-czech-digital-week.png){: .img-thumbnail }

## Inboxy

Po dovolené jsem procházel všechny možné „inboxy“, kde mi lidi píšou.
Stále ještě některým dlužím odpovědi.

-   Prošel jsem přes 100 e-mailů a zbylo jich 6, z nichž si tam některé bohužel syslím už od Vánoc.
-   Projít [klubový Discord](https://junior.guru/club/) nakonec nebylo tak hrozné, jak jsem se obával.
    Dělo se tam toho dost, ale stačilo tomu věnovat jedno odpoledne a většinu jsem si stihl projít.
    Ještě mi zbývají uvítání nových členů, pár vláken a něco velmi dlouhého ve „zdraví mysli“, tam mi to píše 50+ nepřečtených zpráv.
-   [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu) byl taky výživný, ale nakonec tam nebylo zas tak moc věcí, na které bych musel reagovat.
-   Messenger, Telegram…
-   Zprávy na LinkedIn.
    Ty jsou nejhorší, protože se nedají označit jako nepřečtené tak, aby stále svítily jako notifikace.
    Takže jakmile člověk nakoukne do inboxu, už musí na vše hned odpovědět, jinak zapomene, že mu někdo vůbec psal.

## Nový build frontendu

Před odjezdem na dovolenou jsem rozpracoval změnu toho, jak funguje build frontendu.
Ač dělám _continuous deployment_, tohle jsem si [schoval do Pull Requestu](https://github.com/honzajavorek/junior.guru/pull/1158).
Teď jsem se k tomu vrátil a ve volných chvilkách tuto velkou změnu šťouchal směrem k produkci.

Asi nemá smysl tady popisovat detaily.
Bylo to sice v podstatě připravené na puštění do produkce, ale postupně bylo potřeba opravit desítky drobných věcí, které se někde rozbily, protože jsem si je neuvědomil, nebo je někde přehlédl.

Po několika kontrolách jsem to na produkci opravdu pustil a zatím to vypadá, že vše fakt funguje.
Až mě to udivuje!

Další den jsem si k tomu ještě doplnil vývojový server s reloadem.
Využil jsem balíček [livereload](https://pypi.org/project/livereload/).
Chvíli mi trvalo to poladit, ale zdá se, že vše funguje tak, jak potřebuji.

Výsledkem je, že build nezabere deset minut, ale pár sekund.
A i ten development server se mi zdá rychlejší.
Do budoucna bych to chtěl celé ještě jednodušší a rychlejší, ale k tomu se potřebuji zbavit nějakých starých záležitostí v kódu a to ještě potrvá.

Negativním efektem změn je prodloužení času, který je potřeba na build dat, ze kterých se webová stránka staví.
Přesunulo se do nich totiž generování „og:image“ náhledů stránek, a to zabírá hromadu času.
S tím mám ale v plánu hned něco udělat.
Takže další kroky budou:

-   Kešování generovaných obrázků mezi buildy.
-   Optimalizace obrázků a dalších věcí v nějakém samostatném buildu.

Pak už toho asi nechám a budu se zas věnovat užitečnějším věcem.

## Další

-   Pokud chcete přednášet na letošním PyCon CZ, [napište to sem](https://cz.pycon.org/2023/cfp/)!
    Zbývá týden času.
-   V červenci bude v Praze [EuroPython](https://ep2023.europython.eu/), největší Evropská konference o Pythonu.
    EuroPython je putovní, takže je to asi jako by kolem Prahy zrovna letěla kometa.
    Bude to fakt velký festival pro všechny pythonisty, sjedou se z celého kontinentu a možná z celé zeměkoule.
    Chtěli by tam udělat workshop programování pro děti.
    Poprosili mě, jestli bych jim nepomohl najít v Česku někoho, kdo by něco takového připravil, nebo se na tom byl schopen nějak podílet.
    Tak pokud o někom víte, napište mi!
-   Chodil jsem do své nové kanceláře, ale jen sporadicky, protože jsem si ráno nedával záměrně budík a odpoledne jsem měl schůzky.
    Přísnější režim si dám až od dalšího pondělí.
-   Zajímavý počin a podle mě něco, co bude mít okamžitě zaplněnou kapacitu: [Angličtina pro ajťáky](https://geekpower.cz/).
    Jestliže umíte učit angličtinu a víte, jaká angličtina je potřeba v IT, lidi vám utrhnou ruce.
    Díra na trhu.
-   Vypnul jsem na CircleCI buildy pro forked Pull Requests, protože jsem stejně neměl věci nastavené tak, aby mohly projít.
    Jednou to vyladím, ale teď nemá smysl, aby se něco spouštělo, když všichni víme, že to tak či tak spadne.
-   Dělal jsem na LinkedIn [promo našemu nejnovějšímu dílu podcastu s Kateřinou Lesch](https://www.linkedin.com/feed/update/urn:li:activity:7074697427642929153/).
-   Dolaďovali jsme s Nelou popis přednášky, která bude v úterý: [Jak se jako ajťák/čka zbavit pochyb a pocitu, že nejsem dost](https://junior.guru/events/#2023-06-20T18-00-00).
    Ukončili jsme dotazník o psychickém zdraví juniorů a odebral jsem z webu proužek, který na dotazník upozorňoval.
    Dělal jsem přednášce [promo na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7075438644286640129/).
-   Prodlužoval jsem platnost domény junior.guru.
    I když mám všechny domény u Wedosu, tuhle mám u subreg.cz, protože u Wedosu nešly .guru domény v roce 2019 koupit.
    Vzhledem k tomu, jak „intuitivní“ bylo zaplatit za prodloužení a vzhledem k tomu, že se zdá, že Wedos už .guru domény umí, dal jsem si do kalendáře upomínku za rok, že to chci převést.
    Ideálně bych to udělal hned, ale nevím, jak funguje přesně to placení.
    Doména .guru stojí skoro tisícovku, takže bych to nerad platil dvakrát jen pro to, abych měl v doménách pořádek.
-   Chvíli padalo API ČNB na kurzy mezi měnami a nemohl jsem kvůli tomu půl dne udělat build webu.
    Přepočítávám tím jedno číslo na [téhle stránce](https://junior.guru/open/).
    Je otázka, zda by šlo věci udělat tak, aby šlo stránku postavit i bez toho, ale popravdě, je to složitější, než se to zdá.
    Takových služeb tam mám hromadu.
    To máte ČNB, Memberful, Discord, Fio API…
    Systém, který by se bez jednotlivých dat obešel a dokázal by na webu zobrazit místo čísla „tady teď chybí data, sorry“, by byl dost sofistikovaný a byť je to smutné a trochu blbé, nemá smysl to nejspíš řešit.
    Prostě musím počkat a hotovo.
    Ono by stejně mělo být junior.guru postaveno tak, aby se nic strašného nestalo, když se tam něco rozbije a já budu týden na dovolené 🤷‍♂️
    Tak co.
-   Spolu s Dariou a Miou z [PyCon CZ](https://cz.pycon.org/) týmu jsme si psali kvůli [CfP PyCon CZ](https://cz.pycon.org/2023/cfp/), začátečnickému tracku, který na konferenci bude, a mému zapojení v celé věci.
-   Některé firmy berou LinkedIn útokem a přes nějakou integraci vytváří každý den novou nabídku práce, pak ji zruší a vytvoří tentýž inzerát, ale pod jiným ID.
    To způsobí, že se jim neustále ukazuje jako čerstvý a nový.
    Také to způsobí, že už po dni na ten původní inzerát nelze reagovat.
    Nebo že to spamuje [můj job board](https://junior.guru/jobs/) a inzeráty v klubu, protože můj robot to neumí vyfiltrovat.
    Takže jsem je [prostě zabanoval](https://github.com/honzajavorek/junior.guru/commit/9fa88cdba5a0b90c5ef2e09264496fda5d8c91ff) 🤷‍♂️
-   Během 16 dní jsem na túrách nachodil 19 km, ujel na kole 32 km. Celkem jsem se hýbal 19 h a zdolal při tom 51 km.
    Ve skutečnosti jsem toho teda v Itálii nachodil mraky, ale neměřil jsem to všechno.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Po dlouhé době zase přednášku v klubu!
2.  Kešování generovaných obrázků mezi buildy.
3.  Optimalizace obrázků a dalších věcí v nějakém samostatném buildu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [#5: Philip Marlowe + Excel = data noir](https://samizdat.cz/datazurnal-005/)<br>„Honza B. v posledních měsících bez nadsázky prokopal cestičku novému žánru – označení se ještě neusadilo, váháme mezi datovou detektivkou a data noir. Pátrání po rozdílech v počtu léků oficiálně dodaných do lékáren a počtu léků v lékárnách oficiálně vydaných lidem ho přivedlo do mnoha potemělých oblastí českého, ba dokonce i evropského zdravotnictví. Pár domnělých nekalostí se nakonec ukázalo být čurbesem ve státních datech a pojmosloví, ale pak je tu inhalátor Symbicort Turbuhaler, kterého zmizelo za stovky milionů a nejpravděpodobnějším vysvětlením zůstává nelegální reexport. Jako správná detektivka to vyšlo jako seriál, a to trojdílný… Trilogie mimo jiné ukazuje, jak pomalá, komplikovaná a komplexní datová žurnalistika je a kolik se toho při ní nachodí. Excel, RStudio nebo Pandas jsou jen začátek.“
- [SŽ reaguje: Zkrácení jízdních dob přinesou až rychlé tratě v nové stopě - Zdopravy.cz](https://zdopravy.cz/sz-reaguje-zkraceni-jizdnich-dob-prinesou-az-rychle-trate-v-nove-stope-165031/)<br>„Platí, že při současné zátěži stávajících tratí mohou zkrácení cestovních dob přinést až vysokorychlostní tratě vybudované v nové stopě.“ Tak toho se nemám šanci dožít 🤯
- [Něco je špička, jiné části jsou zastaralé. Co čekat od VR brýlí Apple Vision Pro](https://www.lupa.cz/clanky/neco-je-spicka-jine-casti-jsou-zastarale-co-cekat-od-vr-bryli-apple-vision-pro/)<br>Někdo, kdo tomu rozumí, sepsal dojmy z Apple brýlí.
- [Nekonečný ukrajinsko-maďarský příběh střídá krize za krizí. Poválečných point může mít několik - VOXPOT](https://www.voxpot.cz/nekonecny-ukrajinsko-madarsky-pribeh-strida-krize-za-krizi-povalecnych-point-muze-mit-nekolik/)<br>Proč Maďarsko nechce pomáhat Ukrajině.
- [Killing Community](https://www.marginalia.nu/log/82_killing_community/)<br>„The only way to make money is to grow, and the only way to grow is to kill the community.“
- [Co víte o strategické prokrastinaci? Zkuste to! — TVŮRCAST](https://podcasters.spotify.com/pod/show/pickey/episodes/Co-vte-o-strategick-prokrastinaci--Zkuste-to-e24q6gc)<br>Óda na nicnedělání!
- [Chartbook #209 The Sudan crisis and the Sahel gold rush](https://adamtooze.substack.com/p/chartbook-209-the-sudan-crisis-and)<br>„As it has swept from East to West, the gold rush has been rearranging populations, economic, social, political and military relations across the Sahel.“ „Gold sales rose from ten percent of Sudan’s exports to 70 percent.“ „…in 2022 $13.4 billion worth of gold production was smuggled out of Sudan.“ A pokračuje to dál - Rusové, boje o nadvládu nad Súdánem, atd.
- [The Afterlife of Go](https://franklantz.substack.com/p/the-afterlife-of-go)<br>Všichni si mysleli, že když AlphaGo porazilo nejlepšího hráče světa, že tím Go prostě končí, roboti vyhráli. AI je, alespoň v této úzké doméně, lepší než člověk. Trvalo 7 let, než se přišlo na to, že si AI vůbec neporadí s naprosto stupidní hrou, kterou zvládne i začátečník. Nemělo se ji kde naučit. Člověk by proti člověku takhle nehrál, protihráčem by to hned prokoukl. AI nic neprokoukne. Není inteligentní. Je pouze naučené na vzorcích minulého chování.
- [Greenland unveils draft constitution in push for complete independence from Danish control](https://www.pbs.org/newshour/show/greenland-unveils-draft-constitution-in-push-for-complete-independence-from-danish-control)<br>Odpojí se Grónsko od Dánska?
- [Moje studio se vejde do dvou brašen a basy s nářadím | Doklidu](https://doklidumag.cz/moje-studio-se-vejde-do-ctyr-brasen-a-basy-s-naradim/)<br>„Mou největší konkurencí je zatím plotr: je rychlejší, dostupnější a levnější než já.“ Daniel Plavecký se snaží obnovit tradici ručně psaných cedulí a o písmomalířského řemesla.
