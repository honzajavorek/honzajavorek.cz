Title: Týdenní poznámky: Zuby, florbalky a M5
Image: images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří pracovat na [junior.guru](https://junior.guru/) a dalších věcech?
Od [posledních poznámek]({filename}2026-09-25_tydenni-poznamky-meetingy-statusy-prednaska-unava.md) už utekl nějaký ten týden (25. 9. až 2. 10.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

O prodlouženém víkendu jsme si doma užili návštěvy a jinak jsme měli docela chill. Procházky, očekávání mimina, babička, [0 A.D.](https://play0ad.com/), brácha s rodinou…

Na bytě jsme řešili parapety a radiátory, ale to je spíš koordinace. Rukama jsme udělali akorát úklid a přeuspořádání předsíně, aby tam byl aspoň věšák a botník a zrušili jsme krabice, které tam byly ještě od rekonstrukce.

To, co na mně lezlo, v tom víkendovém klidu zase odlezlo, a nemoc z toho nebyla. Ale začala mě bolet horní čelist. Nejdřív jsem myslel, že to jsou dutiny a že to odejde. Neodešlo a bylo to horší a silnější. Ve čtvrtek obvodní doktorka, ORL. Pokažený RTG, takže do víkendu se to nestihlo. Ale nějaké léky jsem dostal a po nich se změnil charakter bolesti a už to vypadá spíš na zuby. Jenže zubaře mám v Brně. Takže rychlé objednání a v pondělí tam jedu na otočku.

Zatím frčím na ibáčích a uvidíme co bude příští týden. Samozřejmě do toho se kdykoliv může narodit mimino, takže radost.

## Nový počítač

Už to bude pár let, co jsem si [pořizoval svůj M1 MacBook]({filename}2020-12-18_i-bought-apple-silicon.md). Konkrétně šest. A je vlastně fascinující, že ten noťas je pořád v pohodě a drží se.

Když jsem teď ale dostal od Apify nějaký rozpočet na nový hardware, nakonec jsem neodolal a využil to. Mám teď víc meetingů a už jen to, že mi na M1 přestala fungovat kamera, je dost velký opruz. Mám to vyřešené přes iPhone a continuity, ale je otrava to vždycky připravit a pak odstrojit, a vybíjí to baterku mobilu, pokud není v nabíječce.

Navíc paměť. Jo, těch 8 GB superrychlé RAM spolu se superrychlým swapováním na superrychlý disk se držely dost dlouho, ale přece jen mě už představa rychlejšího a silnějšího stroje nenechávala úplně chladným.

Takže hurá na to. Objednal jsem MacBook Air M5 s 32 GB RAM. A je to teda dělo!

Několik dní jsem pak strávil zálohami a setupováním nového počítače. Nechtěl jsem si tam tahat šestiletý nános různých nastavení a nevyužívaných souborů a aplikací (byť jsem to před pár dny s pomocí jednoho AI chatu [podstatně pročistil](https://mastodonczech.cz/@honzajavorek/117353831120749081)). Chtěl jsem si užít čistou mašinu. Dokonce ani profil ve Firefoxu jsem si nepřenesl a založil nový.

Přenášení důležitých věcí jsem tedy udělal ručně a zabralo dost času. Celkem mě to ale bavilo a využil jsem to k několika podstatným změnám v mém workflow:

- Zkouším novou Siri AI a začal jsem ji docela rychle používat jako hlavní AI chat, když chci něco jen zkonzultovat a ne programovat s agentem. Trochu delší recenze [tady na Mastodonu](https://mastodonczech.cz/@honzajavorek/117371457994248018). Už jsem se přistihl, jak jsem tuhle Siri appku hledal na iPhone, ale bohužel v EU (zatím) není a na mém iPhone 13 mini by to myslím stejně ani nejelo.
- Rozhodl jsem se úplně otočit strategii ohledně aplikací. Místo abych si vše syslil v prohlížeči, zkusím mít zvlášť appky na co jde: Slack, Discord, Claude…
- Tohle se snažím dotáhnout i u tak zásadních věcí, jako jsou kalendář a e-mail. Už dlouho se chystám k tomu, abych byl méně závislý na Google ekosystému, ale zatím všechny pokusy vždy skončily fiaskem. Teď jsem tomu dal další šanci. Půjdu cestou nejmenšího odporu a nejjednodušších aplikací, které mám po ruce. A salámovou metodou. Nejdřív si Googlí věci natahám do klientských aplikací a přestanu používat to webové rozhraní. Zvyknu si na změny a pak uvidím, jestli časem nezměním i server, ze kterého se to tahá. Mám v plánu stát se teď Apple ovcí, což neberu jako dokonalý cílový stav, ale jako nejjednodušší první krok. Takže Apple Mail a Apple Calendar. Jsem zvědavý, jak dlouho to vydržím. V Apple Mailu jsem díky dotazování Siri AI objevil možnost, jak využívat e-mailové aliasy, které mám přes [ImprovMX](https://improvmx.com/), a to je _gamechanger_ pro mou schopnost migrace.
- Místo dvou oddělených profilů ve Firefoxu, což jsem zkoušel předtím, teď zkusím víc používat _multi-account containers_ na to, abych od sebe izoloval práci pro Apify a osobní život.
- Začal jsem používat 1Password i pro SSH klíče. Když dám teď git pull, tak mi vyskočí, že si to chce číst SSH klíč z 1Passwordu, já to potvrdím přes otisk prstu a je to. Spolu s tím jsem si nastavil i podepisování commitů mým klíčem, ale to nevím, jestli mi už funguje správně.
- Nahradil jsem definitivně pipx, používám místo toho uv tool.
- Zkouším zatím existovat bez Rosetta2, protože většina věcí už na ARMu běží a Rosettu2 chce Apple stejně za chvíli už zrušit.

Ve výsledku mám prohlížeč, kde mám opravdu jen prohlížení webu a ne permanentně otevřené nějaké aplikace jako připnuté taby. Žádný Slack, Google Kalendář, Gmail, to vše má teď vlastní aplikaci v systému.

Jsem zvědav, k jakým dalším změnám mě nový hardware bude motivovat. A mám radost. Myslím, že už jsem delší dobu nový počítač potřeboval, ale M1 „stačila”, tak jsem nic nového nepořizoval. Sám bych si M5 asi nekoupil, je to na můj vkus hodně drahá hračka. Ale pak přišlo Apify a přišlo v ten pravý čas. Teď si užívám dělo a mám z něho radost.

## Apify

Každý, kdo nastoupí do Apify, musí v prvním měsíci natočit něco jako „produktové demo”, kde nahrává obrazovku, chodí po produktu a vypráví, jak co funguje.

Já jsem to odkládal na nejzazší datum, protože se mi to strašně nechtělo dělat, hlavně protože jsem v Apify jakoby už dva roky a většinu těch věcí znám. Místo abych si to teda rychle odbyl a prostě to udělal, tak jsem se postupně strašně demotivoval. Nakonec jsem se pomocí terapeutických memů probojoval přes nekonečnou prokrastinaci a začal to dělat.

Ale pojal jsem to po svém a rozhodl se většinu věcí přeskočit a poskytnout ve videu důvody, proč to přeskakuju, a ukázat, co už mám nebo na co jsem už napsal kurzy do Akademie. Pak jsem natočil jen věci, které jsem fakt neznal a dělal jsem je poprvé. Hrozně mi to ale celé nešlo, koktal jsem ze sebe všechno, a bylo to strašně dlouhé, i když jsem to sestříhal. A jednou jsem dokonce čtvrt hodiny nahrával nesprávné okno, takže jsem to mohl zahodit a udělat znova.

Výsledkem jsem prakticky vůbec nesplnil zadání, protože jsem měl proklikat a okomentovat věci a mělo to trvat 30 minut a já jsem frajersky spoustu věcí vynechal a místo toho jsem natočil ukoktané demo náhodných věcí, které má 50 minut, a ještě je to prokládáno poznámkami o tom, jak se mi to celé strašně nechtělo dělat, protože mám lepší věci na práci.

Bylo to velmi utrápené a místy neprofesionální, ale co už, odevzdal jsem to, a budu se jen modlit, aby následovalo smilování 😅 Kdyžtak se vymluvím na to, že mě u toho bolely zuby, což mě opravdu bolely…

V pátek jsem pak pro jistotu konečně otevřel PR, kterým bych měl publikovat nový kurz o tom, jak vytvářet scrapery pouze pomocí AI: [apify-docs#3039](https://github.com/apify/apify-docs/pull/3039)

## junior.guru

Na žádný velký vývoj nebyl čas. S pomocí AI agentů jsem dělal především opravy:

-   [Fix indentation in jobs page lead text](https://github.com/juniorguru/junior.guru/pull/1767)
-   [Switch browser engine from Firefox to Chromium](https://github.com/juniorguru/junior.guru/pull/1769)
-   [Fix dead opatruj.se link in mental-health handbook](https://github.com/juniorguru/junior.guru/pull/1772)
-   [Make lychee skip scraped job URLs in inline jobs widget](https://github.com/juniorguru/junior.guru/pull/1775)
-   [Fix OpenAI client reuse across event loops](https://github.com/juniorguru/junior.guru/pull/1776)
-   [Add retry logic to wiki page fetching in feminine names sync](https://github.com/juniorguru/junior.guru/pull/1777)
-   [Replace pync with osascript for desktop notifications](https://github.com/juniorguru/junior.guru/pull/1778)
-   [Include candidates data in automatic record updates](https://github.com/juniorguru/junior.guru/pull/1779)
-   [Browser crashes](https://github.com/juniorguru/junior.guru/issues/1768)

S přelomem měsíce pak přišlo pár klasických prací, jako uvedení další přednášky, publikace nového rozhovoru, atd. Taky jsem se podíval do mailů, na které jsem neměl čas, a přidal jsem jedny nové kurzy do katalogu:

-   [Add a new story and announce next event](https://github.com/juniorguru/junior.guru/pull/1780)
-   [Add Reactivdevs](https://github.com/juniorguru/junior.guru/pull/1781)

Výsledky:

-   [Na pohovoru proti mně sedělo šest lidí. Tomáš Novák o tranzitu z hudby do IT](https://junior.guru/stories/tomas-novak/)
-   [Kurzy od ReactivDevs](https://junior.guru/courses/reactivdevs/)
-   [David Majda: Od zdrojáku ke strojáku: Jak fungují kompilátory a interpretery](https://junior.guru/events/66/)
-   [Září 2026 ve světě IT juniorů](https://junior.guru/news/zari-2026-ve-svete-it-junioru-u1f423-2481/)

Nechal jsem agenta dělat průzkum, jestli by nešlo zjednodušit, jak se na junior.guru dělají screenshoty, ale to nakonec nevyšlo ([junior.guru#1770](https://github.com/juniorguru/junior.guru/pull/1770)). Doplňek v prohlížeči by mi vlastně nic asi neřešil a vše by mělo jen větší komplexitu.

## Osobní projekty a Python komunita

Opravoval jsem si _f1news_, aby teď krásně fungovaly a abych se včera nebo kdy dočetl, že Reddit plánuje úplně zavřít RSS i API, takže dříve či později tenhle projekt už nepůjde nijak realizovat 🤦‍♂️ Každopádně teď to teda snad chvíli fungovat bude: [f1news#38](https://github.com/honzajavorek/f1news/pull/38), [f1news#39](https://github.com/honzajavorek/f1news/pull/39), [f1news#40](https://github.com/honzajavorek/f1news/pull/40), [f1news#41](https://github.com/honzajavorek/f1news/pull/41)

O víkendu jsem zjistil, že _film2trello_ mi pořád ještě nefunguje, tak jsem to zkoušel trochu ještě předělat, a nakonec jsem náhodou objevil úplně jednoduchý a nenáročný způsob, jak obejít ochrany na ČSFD 😀 Tak jsem to využil i u _kina_ a Camoufox šel zase pryč. A taky jsem na kinu opravil jeden bug s rozpoznáním země původu filmu a vlajky: [film2trello#361](https://github.com/honzajavorek/film2trello/pull/361), [film2trello#362](https://github.com/honzajavorek/film2trello/pull/362), [film2trello#363](https://github.com/honzajavorek/film2trello/pull/363), [film2trello#364](https://github.com/honzajavorek/film2trello/pull/364), [film2trello#365](https://github.com/honzajavorek/film2trello/pull/365), [film2trello#366](https://github.com/honzajavorek/film2trello/pull/366), [film2trello#367](https://github.com/honzajavorek/film2trello/pull/367), [film2trello#368](https://github.com/honzajavorek/film2trello/pull/368), [kino#97](https://github.com/honzajavorek/kino/pull/97), [kino#98](https://github.com/honzajavorek/kino/pull/98), [kino#101](https://github.com/honzajavorek/kino/pull/101), [kino#102](https://github.com/honzajavorek/kino/pull/102)

Tady na blogu jsem v [honzajavorek.cz#442](https://github.com/honzajavorek/honzajavorek.cz/pull/442) odebral Notion, protože to začalo blbnout a vlastně mi to už dlouho stejně z neznámého důvodu nefungovalo a nepoužíval jsem to. Tím definitivně zanikl můj [systém na čtení náhodných článků z internetu]({filename}2023-04-01_notion-as-a-replacement-for-pocket.md) a budu vymýšlet nějakou náhradu.

No a nakonec [docs.pyvec.org#581](https://github.com/pyvec/docs.pyvec.org/pull/581), čímž jsem opravil rozbitou kontrolu odkazů na dokumentaci Pyvce.

## Další

-   Jeden z členů klubu zjistil, že má roztroušenou sklerózu 😔 (kdo nemoc neznáte, tak si [pusťte toto](https://www.youtube.com/watch?v=eR6Biiya5Wc)).
-   Ozvala se mi po delší době opět Veronika z [Geek Power](https://geekpower.cz/), ale aktuálně na tom junior.guru není tak dobře, aby mohlo zase členům dotovat lekce angličtiny. Možná ale domluvíme aspoň přednášku v klubu.
-   Koupili jsme si s dcerou florbalky a míček. Už se těším, až si spolu budem občas před barákem pinkat. Nebo i doma, ale to možná není povolený, ještě nevím.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. 13 upgradů závislostí na všech projektech.

## Plánuji

1.  Zjistit, od čeho je ta bolest zubů a ideálně ji i vyřešit.
2.  Uvítat mimino.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Immigration | Dark Thoughts](https://dark.ronacher.eu/2025/12/30/immigration/)<br>„Every country has their rules around immigration but rarely are those set in stone… It’s not uncommon for ppl to immigrate legally one year, only to find out the rules have changed next year and they’re now out. Even if their rights are grandfathered, they might find themselves unable to demonstrate their rights in future. Sometimes even definition of citizenship has changed. The rules are so bizarre, that it’s impossible for anyone to keep track of them…“
- [Budete ve městě rychleji autem nebo vlakem? Poradí nové dálniční cedule - Zdopravy.cz](https://zdopravy.cz/budete-ve-meste-rychleji-autem-nebo-vlakem-poradi-nove-dalnicni-cedule-301273/)<br>Tohle je cool, to by bylo krásné tady mít.
- [Borders | Dark Thoughts](https://dark.ronacher.eu/2025/12/15/borders/)<br>„Being on the better side of the border is a privilege, and it feels good. Wanting to get rid of the border is natural for those on the worse side. Defending the removal of the border by those who benefit from it is unpopular. In fact, it can be seen as irresponsible, even treasonous. Yet without that border, both sides would be better off as commerce and culture would flow more freely.“
- [Can the Male Still Gaze? - YouTube](https://www.youtube.com/watch?v=-4IB4wCZME4)<br>Zajímavé video o tom, jak se vyvíjí Male Gaze v kinematografii.
