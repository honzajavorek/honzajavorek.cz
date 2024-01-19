Title: Týdenní poznámky: Hory a scrapery
Image: images/img-7181.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/303
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111783362132032936

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-01-05_tydenni-poznamky-vanoce.md) už utekl nějaký ten týden (5. 1. až 19. 1.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Zima]({static}/images/img-7181.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)
</div>

Minulý týden jsme s rodinkou odjeli do Jeseníků, takže jsem se neobtěžoval sepisovat poznámky za dva pracovní dny.
Na horách jsem si hezky mentálně odpočinul.
Fyzicky moc ne, protože jsme tam jednak trochu pařili s kamarády, jednak jsem se prošel v celkem rychlém tempu na Šerák, nebo jsem fungoval jako tažný tvor pro boby.
Velmi pozitivní je, že jsem nebyl nemocný.
Z toho se vážně raduju a hned má člověk víc sil něco dělat, a ne jenom přežívat.

## Plucker

Vyšíval jsem dále na novém repozitáři, do kterého stěhuju scrapery z junior.guru, a jenž jsem pojmenoval [Plucker](https://github.com/juniorguru/plucker).

-   Prozkoumal jsem monitoring v Apify a nastavil jej u svých scraperů, ale [možná to udělám nakonec stejně jinak](https://github.com/juniorguru/plucker/issues/13), protože potřebuji hlídat i jiné věci a ty zase lze hlídat jen z kódu.
    Aspoň mi Apify pošle e-mail, když scraper selže.
    Aby scrapery ve Scrapy selhaly s exit kódem 1, to jsem taky musel vyzkoumat, jak to udělat.
-   Povedlo se mi díky [změnám na jejich straně](https://github.com/apify/actor-templates/pull/260/files) použít proxiny z Apify.
    Přes proxy jedou dva moje hlavní scrapery na stahování pracovních inzerátů, takže je to pro mně důležité.
-   Doplnil jsem do Pluckeru CLI, které umožňuje v projektu řešit i něco jiného, než pouze scrapování.
    Musel jsem při tom výrazně ohnout původní šablonu od Apify.
    Mám tam teď CLI přes [click](https://pypi.org/project/click/), kde je jak příkaz pro spuštění scraperu, tak příkaz např. pro vygenerování schéma pro Apify actor z kódu, abych to nemusel psát ručně.
-   Vymazlil jsem na repozitáři testy, přidal [ruff](https://pypi.org/project/ruff/) a sepsal README.
    Díky [pytest-ruff](https://pypi.org/project/pytest-ruff/) mohu vše zkontrolovat jedním příkazem.
    Opsal jsem celé kolečko, od dřívějšího akademického „mazlení“ se s repozitáři, přes pozdější podnikatelské „odbývaní“, po dnešní opětovné „mazlení“ s vidinou toho, že do kódu bude časem třeba schopen přispět i někdo jiný.
-   Přesunul jsem do repozitáře tři další scrapery z hlavního kódu junior.guru a vyladil je tak, aby fungovaly.
    Nakonec jsem odstranil Levelsův [RemoteOK](https://remoteok.com/), protože byl nějaký rozbitý a přišlo mi, že vlastně nemá smysl jej opravovat.
    Dlouhodobě na něm nejsou nabídky relevantní pro české (nebo slovenské) juniory.
    Pokud si mám vybrat, čemu věnovat čas, tak raději stáhnu Profesiu, než udržovat funkční scraper s takto minoritním dopadem.
-   Přesunul jsem do repozitáře hromadu testů a ještě nějaké Scrapy pipelines, které filtrují výsledky, např. zda jim něco nechybí, nebo podle toho, zda jsou v relevantním jazyce.
    Musel jsem vymyslet, jak to udělat tak, aby se určité pipelines pouštěly jen pro určité scrapery a pro jiné zase ne.
-   Posílal jsem zpětnou vazbu CTO Apify (řekl si o ni), zakládal jsem jim na GitHubu různá issue a na Discordu jsem reportoval problémy s GitHub integrací.
    Nevím, jestli z toho mají radost, nebo je tím už otravuju 😀
    Nejspíš to zjistím na [Python Pizza Prague](https://prague.python.pizza/), které bude v jejich kancelářích.
    Příklad toho, co jsem jim psal:

    > Teď dělám něco s actory a už poněkolikáté mě napadlo, že by se mi líbilo, kdybych mohl všechno, co jde udělat přes UI na webu, mít v nějakém JSONu/YAMLu/TOMLu (JSON nemám moc rád, protože tam nejde mít komentáře) as code přímo v repozitáři. Nejsem moc zkušený v ops a nevím, jak přesně fungují Ansible, Terraform, a spol., ale představoval bych si to tak, že když si naklikám u vás na webu Alert u Actora, tak se to propíše do nějakého konfiguráku v repu, a když ten konfigurák změním, tak se propíše do Actora ve vaší platformě. Měl bych pak dojem, že to mám víc pod kontrolou, zazálohované, že Actor je něco, co mohu snadno sundat a nahodit znova vedle, bez velkého klikání. Ale možná je to jen tím, že jich chci mít víc, třeba má váš běžný uživatel dva, tři, a bylo by mu to na nic.

    Největší problém ale je, že mi na Apify vůbec nefungují automatické buildy actorů na základě webhooků z GitHubu.
    [Popsal jsem to k nim na Discord](https://discord.com/channels/801163717915574323/1183092714737254523/1197123079340572705), tak uvidím, jestli to nějak opraví.
    Možná by to šlo nějak obejít [přes API](https://docs.apify.com/api/v2/#/reference/actors/build-collection/build-actor), ale byl bych raději, kdyby jim to fungovalo 😉

Co ještě chybí?

-   Musím opravit jeden scraper, který v současné chvíli nefunguje dobře.
-   Měl bych jít do hlavního kódu junior.guru a přehodit zdroj inzerátů z lokálního Scrapy na API z Apify.
-   Pak to nechám chvíli běžet a budu pozorovat, jak to funguje.
    Mezitím mohu procházet hlavní kód a postupně mazat tuny a tuny nyní zbytečného kódu.

A proč to vlastně dělám?
Po přesunu na Apify se mi umožní následující:

-   Můžu rozšířit záběr stahovaných inzerátů.
    Scrapery bude moci vytvářet nebo opravovat i někdo jiný než já.
-   Můžu zapojit AI a zjednodušit díky tomu filtrování na juniorní inzeráty.
    V souvislosti s tím můžu taky konečně přidat podporu pro slovenčinu.
-   **Ve výsledku budou mít k dispozici členové klubu a návštěvníci webu více relevantních inzerátů, než dnes.**

Začal jsem si pro vývoj Pluckeru [vytvářet issues na GitHubu](https://github.com/juniorguru/plucker/issues).
Uvidím, jak mi to bude vyhovovat, protože jsem zvyklý koukat spíš do svého Trella.
Když ale budou úkoly sepsané externě, existuje možnost, že mi s nimi někdo pomůže.

## Dan, Milek, Tinuki

Viděl jsem se zvlášť s Danem a s Milkem, moderátory z klubu a aktivními účastníky komunity.
Probrali jsme všechno možné, samozřejmě klub, ale i život, a tak.

S oběma jsem probral své nápady ohledně toho, jak by měly vypadat profily juniorů na junior.guru.
Milek teď hodně táhne aktivitu v klubu, čehož si dost vážím.
Organizuje pondělní povídání, na které se připojuje i desítka lidí a kecají tam skoro do půlnoci.
Kromě toho dělá i týdenní plánování a dlouhodobě se také pokouší v klubu rozjet různé projektově orientované _coding challenge_.

Taky to vypadá, že si členové klubu sami zorganizují sraz po [Python Pizza Prague](https://prague.python.pizza/), na který pouze dorazím 😀

Taky jsem si psal s Tinukim, který mi pomáhá nahrávat přednášky.
Což mi připomíná, že jsem stále nenaplánoval přednášky na nový rok, a to už je skoro konec ledna 🙈

## Terapie

Konečně jsem dotáhl hledání psychoterapie.
Zkusil jsem dvě paní a vybral tu druhou.
Uvidím, jaké to bude a jak dlouho tam budu chodit, ale mám z toho dobrý pocit.

Každému bych doporučil zkusit aspoň dva různé lidi, ať má nějaké srovnání, aspoň nějaký základní _benchmark_, co čekat a jak to může vypadat.

Paradoxem celé mojí předchozí snahy zúžit nekonečný seznam terapeutů např. podle místa výkonu je to, že paní, kterou jsem vybral, se den před mým „nástupem“ neplánovaně přestěhovala z Prahy 3 na Prahu 1 a budu k ní dojíždět 😂
Ale tak jednička pořád lepší než někam za řeku, to bych asi vzdal.

## film2trello

Přepsal jsem si ve volném čase [film2trello](https://github.com/honzajavorek/film2trello) do Telegram bota a zdá se, že to nějak funguje.
Hned jsem tam použil pro mě nové věci, např. [ruff](https://pypi.org/project/ruff/) nebo [httpx](https://pypi.org/project/httpx/).
Má to ještě nějaké mouchy, ale po návratu z hor jsem na to neměl čas sáhnout.
Po večerech se dá programovat jen pokud to nedělám ve dne, a já se pak už hodně věnoval těm scraperům.

S přepisováním mi dost pomohl GitHub Copilot.
Potřeboval jsem v zásadě stejnou logiku předělat ze synchronního kódu do asynchronního, nebo z requests do httpx.
Na tohle bylo AI úplně super, jen jsem mačkal tab a doplňovalo to kód za mně.
Nemusel jsem složitě studovat dokumentaci, jak udělat totéž, ale vlastně jinak.

Použil jsem i GitHub Copilot chat.
Nejlepší je to na takové ty věci, které jakoby vím, ale musel bych je dlouho hledat a složitě něco studovat.
Např. „jak nastreamuju obrázek z httpx knihovny přímo do Pillow image?“
Když vidím, co mi to vymyslelo, tak od oka dokážu posoudit, jestli to je blbost, nebo ne.
A jo, dokázal bych to vymyslet i sám, ale zabralo by mi to - se vším všudy - třeba hodinu.

## Další

-   Zjistil jsem, že máme chybu na webu Pyvce.
    Vytvořil jsem issue a nasdílel jej na Pyvec Slacku a na junior.guru Discordu.
    A jeden z „mých“ juniorů [to opravil](https://github.com/pyvec/pyvec.org/pull/385)!
    Super.
-   Začal selhávat můj monitoring počtu followerů.
    Při opravě jsem zjistil, že LinkedIn to číslo zcela odebral ze všech stránek, které nejsou za loginem.
    _Hajzli jedni!_
    Nedá se pro teď nic dělat, zjišťování počtu sledujících na svém osobním LinkedIn profilu jsem pro teď zakomentoval a nestahuje se.
    Třeba v budoucnu zas něco vymyslím.
-   Díky Martinovi a Jožovi za pomoc s Albi tužkou.
    Výsledkem bádání je, že udělat správně USB-C konektor je složitější záležitost, a na Albi tužce je prostě udělaný blbě.
    Takže při spojení USB-C/USB-A funguje správně, ale USB-C/USB-C prostě fungovat nebude.
    Řešení je používat USB-C/USB-A s redukcí z USB-A do USB-C, což je samozřejmě padlé na hlavu, ale bohužel je to tak.
-   V klubu jsem uklidil roli na Advent of Code a vyvtořil novou na další rok.
-   Opravil jsem [czech-political-parties](https://github.com/honzajavorek/czech-political-parties/), stačilo upgradovat závislosti.
-   Pomohl jsem trošku shánět účetní pro Pyvec, ale můj kontakt nevyšel.
    Naštěstí se zdá, že vyjde něco od Anežky.
-   Skončila mi pravidelná léčba, juchů.
    Zda vůbec s něčím pomohla, to se uvidí.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Hodně času jsem věnoval čtení klubu po Vánocích a dohánění všech dalších komunikačních restů.
-   Za 15 dní jsem při procházkách nachodil 6 km, na túrách nachodil 16 km. Celkem jsem se hýbal 14 h a zdolal při tom 22 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Sepíšu na blog plán na Q1.
2.  Vyberu a naplánuju klubové přednášky na rok 2024.
3.  Připravím podklady pro daňové přiznání.
4.  Přepojím junior.guru z lokálních scraperů na Apify API.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Ep. 114 – 2023 – Čo bolo a čo bude — Street of Code](https://wp.streetofcode.sk/podcast/2023-co-bolo-a-co-bude/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=2023-co-bolo-a-co-bude)<br>Zjevně to nemá jednoduché nikdo s malými dětmi. Já píšu poznámky na blog, kluci ze Street of Code nahráli podobně upřímné ohlédnutí za svým posledním rokem.
- [Github Is Changing](https://www.youtube.com/watch?v=mpQUDxoQUyU)<br>„GitHub embracing AI is fine. GitHub embracing AI explicitly at the cost of ignoring the whole reason their platform exists is very very bad.“
- [What riding a high skinny looks like from my POV 👀 #mtb #streettrials #bmx](https://www.youtube.com/watch?v=_3xlzCP4PA8)<br>Masakr.
- [Python 3.13 gets a JIT](https://tonybaloney.github.io/posts/python-gets-a-jit.html)<br>Pěkný článek, který jednoduše vysvětluje docela složitou věc.
- [Google Settles in $5B Incognito Mode Lawsuit](https://www.simpleanalytics.com/blog/google-settles-in-5-b-incognito-mode-lawsuit)<br>„According to the Court, Google knew that consumers misunderstood what Incognito mode does. In other words, the company was aware of the ambiguity and took advantage of it.“
- [8dd7445e203de5336871e6bbb9755a1f.pdf — Are.na](https://www.are.na/block/25566801)<br>Grafický manuál F1 má 205 stran.
- [Státní pokladna a manželství pro všechny](https://www.mimoagendu.cz/untitled-3/)<br>„Rodiče mi říkali, že možná dostanu svou první výplatu v eurech. Po vstupu byli lidé, co se týče evropského společenství, podstatně optimističtější. Dnes bych byl šťastný, kdyby první výplatu v eurech dostalo třeba mé dítě. Jednu generaci jsme v otázce integrace do Evropy přeskočili kvůli hloupým obstrukcím lidi, kteří snad už brzy definitivně odejdou z politické scény.“
- [Místo magistrály městská třída se stromořadím. Na proměně se bude podílet i Pleskot - Zdopravy.cz](https://zdopravy.cz/misto-magistraly-mestska-trida-se-stromoradim-na-promene-se-bude-podilet-i-pleskot-189667/)<br>Už aby to bylo.
