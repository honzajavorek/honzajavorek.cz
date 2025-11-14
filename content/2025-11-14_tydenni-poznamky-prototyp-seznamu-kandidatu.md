Title: Týdenní poznámky: Prototyp seznamu kandidátů
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 9 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/366
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115548722780237574

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-11-07_tydenni-poznamky-newsletter-odeslan-a-archivovan-pracovni-inzeraty-prekopany.md) už utekl nějaký ten týden (7. 11. až 14. 11.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

O víkendu jsme se po delší době viděli s kamarádkou z Namibie, Domi K. Užil jsem si VC Brazílie a uvařil dýňovou polívku. Týden byl taky celkem pohodový a klidný, i když byl prošpikovaný různými setkáními. V pondělí jsem si zašel sám do sauny, nabít baterky. V úterý jsem si po dlouhé době zavolal s Terezou P., ve středu sešel na oběd s Matějem D., ve čtvrtek jsem byl na pivu s příštím volebním lídrem místních Zelených, a dnes to vypadá, že půjdu do sauny ještě jednou, s kamarádem Mílou V.

## Prototyp seznamu kandidátů

Většinu týdne jsem se soustředil na to, abych dotáhl [junior.guru/candidates](https://junior.guru/candidates/) do nějakého MVP.

Chvíli jsem uvažoval, jestli JavaScript, který řeší filtrování na stránce [junior.guru/jobs](https://junior.guru/jobs/) s pracovními inzeráty nepřepsat do [Alpine.js](https://alpinejs.dev/), aby to bylo pochopitelnější a udržovatelnější, ale rozhodl jsem se, že na to teď není čas a že přepisovat budu věci až ve chvíli, kdy budou přispívat k tomu, aby junior.guru existovalo a vydělávalo peníze. Takže jsem vzal soubor `jobs.js`, zduplikoval jej jako `candidates.js` a přejmenoval proměnné, hotovo 😎

Přemýšlel jsem, jak vlastně lidem vysvětlit, jak to celé má fungovat. Stručně, ale jasně. Aby to pochopili jak recruiteři, tak samotní junioři. Nakonec jsem se to pokusil vydestilovat do čtyřech bodů, které mají každý ikonku, hlavní text, a ještě doplňující text s odkazy. Formuloval jsem to směrem k recruiterům. Junioři s tím možná budou trochu zápasit, ale budu to zatím brát jako test inteligence a záměrné „tření“, které když junior překoná, tak si zaslouží v seznamu být. Design těch vysvětlujících bodů mi zabral možná až příliš mnoho času, ale s výsledkem jsem teď docela spokojený.

Pak jsem se pustil do samotného [eggtray](https://github.com/juniorguru/eggtray/). [Utáhl jsem šrouby](https://github.com/juniorguru/eggtray/issues/204) tak, aby testy padaly správněji, když se junioři snaží přidat YAML soubor s profilem. Taky jsem předělal to, jak se při jednorázových _reviews_ profilů postují výsledky. Původně bot poslal komentář, že se na profil jde podívat, a ten pak editoval. To ale nebylo ideální, třeba i kvůli e-mailovým notifikacím z GitHubu, a tak jsem to předělal, [aby prostě poslal další komentář](https://github.com/juniorguru/eggtray/issues/106). Opravil jsem i pár dalších chybek a otestoval, že vše funguje, jak má.

Doprogramoval jsem [zásadní věc](https://github.com/juniorguru/eggtray/issues/13), která každý den zkontroluje profily a pokud mají nedostatky, založí na repozitáři issue. Hned to [nějaké issues založilo](https://github.com/juniorguru/eggtray/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22profile%20not%20ready%22) a hned se objevili i aktivní junioři, kteří si to šli opravit. Vyzdvihnu hlavně [Veroniku](https://github.com/juniorguru/eggtray/issues/217), která mi pomohla vylepšit UX celé věci a ještě našla bug v tom, jak můj systém zpracovává odkaz na LinkedIn (psali jsme si pak o tom e-mailem). Zavírání issues, pokud si junior opravil, co měl, jsem doprogramoval až další den 😎 Pak jsem do [eggtray API](https://juniorguru.github.io/eggtray/profiles.json) přidal `report_url`, tzn. odkaz na to issue, které popisuje, jaké nedostatky junior na profilu má.

Následně jsem přidával na všechna možná místa informaci pro juniory, že pokud jejich profil projde bez větších problémů, mohou si na [junior.guru/candidates](https://junior.guru/candidates/) založit profil. Tohle jsem dělal jak pro samotné jednorázové _reviews_ na eggtray, tak pro zpětnou vazbu, kterou bot umí dávat na Discordu v klubu.

Do klubového bota jsem přidal i příkaz, kterým lidé mohou zjistit svoje Discord ID. Když tohle ID dají do YAMLu, systém pak dokáže vyhodnotit, jestli jsou členy klubu a pokud ano, zobrazí je v seznamu žlutě.

Pak jsem šel a konečně předělal klubovou roli „Aktivně hledám práci“ tak, aby byla automaticky navázána na to, jestli má někdo profil na webu, nebo ne. Dřív si ji mohl samoobslužně na Discordu dát kdo chtěl, teď ji spravuje bot a dává ji jen členům, kteří jsou na [junior.guru/candidates](https://junior.guru/candidates/).

No a dnes v pátek jsem se ještě podíval na způsob, jak se v seznamu kandidátů pracuje s lokací, protože je to přece jenom trochu jiná písnička, než u lokace např. pracovních inzerátů. Jeden problém je, že se bere z toho, co si kdo napíše na GitHub, a to je volný text. Může tam být `Brno, Czechia`, ale taky prostě jen `Slovakia`, nebo `Olomouc, Ostrava, Brno - Czechia`, což je docela oříšek zpracovat.

Nakonec jsem si udělal speciální funkci na _fuzzy_ zpracovávání, která to nejdřív nechá analyzovat LLMko a pak to ještě prožene přes moji klasickou funkci, která lokace normalizuje přes API od Mapy.cz. Lokace, kam někdo dá jen `Czechia`, nebo tam dá víc jak dvě místa, se nakonec na webu přeloží jako „všudezdejší“ a ve filtrech mám kromě všech krajů ještě i #kdekoliv. Uvidím, jak to obstojí. Nedělám si iluzi, že to podchycuje komplexitu světa, ale nějaké základní řešení to je a dál se v tom budu šťourat až když to bude potřeba.

Pak jsem ještě na web vložil odkaz na to GitHub issue s nedostatky, pokud junior nějaké nedostatky na profilu má, aby se mohli lidi rovnou podívat, co je tam za problém. Ať už junioři, kteří tolik nesledujou samotný GitHub a budou si to chtít opravit, nebo ti, kdo najímají lidi, kdyby byli zvědaví. Třeba zjistí, že jde o prkotiny a stejně se tomu člověku ozvou.

No a je to, prototyp hotov! Zrovna během toho, jak to tady píšu, tak to nasazuju na produkci. Ještě bych neřekl, že to je úplně MVP, takže to zatím nebudu roztrubovat do světa, ale už to bude na webu a třeba někdo najde chyby, nebo mi posdílí nějaké nápady, co s tím. Aby to bylo MVP a mohl jsem to začít tlačit firmám, tak ještě chybí to nejdůležitější: důvody, proč toho kterého juniora najmout. Zásadní jsou projekty, ty tam musí být v první řadě a skvěle odprezentované. A pak tam ještě chci mít nějaké „odznáčky“, které se budou snažit zdůraznit určité kvality jednotlivých lidí. Vždy půjde o kvality, které jsem schopen nějak aspoň trochu ověřit.

![Vršek stránky s kandidáty]({static}/images/screenshot-2025-11-13-at-15-55-17-kandidati-na-pozici-junior-programator-programatorka.png){: .img-thumbnail }

![Detail kandidátky]({static}/images/screenshot-2025-11-13-at-15-55-38-kandidati-na-pozici-junior-programator-programatorka.png){: .img-thumbnail }

## Další

-   Pro mě dost zásadní novina: [mkdocs-material končí](https://fosstodon.org/@squidfunk/115531980077241805), autor zakládá firmu a produkt „zensical“ a v té firmě bude pracovat i maintainer MkDocs. Na MkDocs mi jede junior.guru a python.cz. Na python.cz se používá i mkdocs-material. A v Python komunitě jsme uvažovali, že bychom to nasadili i na další projekty. Zatím nedokážu posoudit, jestli jsou ty novinky dobrá nebo špatná zpráva, a jak to ovlivní vývoj MkDocs samotných. Založil jsem aspoň [pyvec/python.cz#601](https://github.com/pyvec/python.cz/issues/601).
-   Když jsem se po delší době vrtal v [hen](https://github.com/juniorguru/hen), předělal jsem to z Poetry na uv.
-   Nefunguje mi ignorování jednotlivých stránek v Lychee. [Diskutoval jsem to s autory Lychee](https://github.com/lycheeverse/lychee/discussions/1909), ti mi něco poradili, ukázali mi [dokumentaci](https://lychee.cli.rs/recipes/excluding-paths/), ale nefunguje mi to. Zatím jsem to neoddebugoval.
-   Překopírovávání minulých poznámek na LinkedIn po cestě nějak ztratilo jednu citaci a skoro všechny obrázky. Asi to s tím _vibe codingem_ nebude zas taková sláva! 😀 Zatím jsem to nestíhal opravovat, takže se to nejspíš stane zase.
-   Padaly mi věci kvůli tomu, že `asyncio.Semaphore()` není _thread-safe_ a já z různých důvodů pouštím asyncio loop ve všelijakých vláknech, takže to padalo na tom, že se semafor na úrovni modulu inicializoval s jednou loop, ale pak jsem ho chtěl spustit v kontextu jiné loop. Musel jsem to vyřešit přes nějaký slovník semaforů, odkud se berou podle `id()` aktuální loop 🙈
-   Plánovali a domlouvali jsme s Táňou V. [další klubové akce](https://junior.guru/events/)! V listopadu nakonec budou hned dvě.
-   Pyvec má nově [svou organizaci na PyPI](https://pypi.org/org/pyvec/). Přesunul jsem tedy pod Pyvec projekt [danube-delta](https://github.com/pyvec/danube-delta), na GitHubu i na PyPI. Je to moje dávné rozšíření blog generátoru Pelican a závisí na něm už prakticky jen blog české Python komunity.
-   Napsali mi kluci z [Vosap Podcastu](https://www.youtube.com/channel/UC30YtRWXgJUQwBwRcZRJ_sg), že se jim líbí, co dělám, a že by junior.guru propagovali 😀 Odepsal jsem, že jim můžu poslat samolepky a že držím palce. Zatím ale naše komunikace nepokračovala.
-   Vyhodnotili jsme říjnovou projektovou výzvu v klubu a odstartovali listopadovou. Uhádli byste zvíře, které je na čtyři písmena a není v něm A, E, I, O, ani U? Odpověď najdete [tady](https://mastodonczech.cz/@honzajavorek/115548390479238244).
-   Bridgy Fed [podporuje federaci i přes RSS](https://fed.brid.gy/docs#web-get-started), věděli jste? Ještě nevím, k čemu se mi to hodí, ale třeba k něčemu jednou bude 🤔
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. Tento týden toho nebylo nějak přespříliš.
-   Za 8 dní jsem naběhal 8 km. Celkem jsem se hýbal 2 h a zdolal při tom 8 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

Příští týden budu mít svůj listopadový _stint_ pro Apify.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [FFmpeg to Google: Fund Us or Stop Sending Bugs](https://thenewstack.io/ffmpeg-to-google-fund-us-or-stop-sending-bugs/)<br>„We take security very seriously, but at the same time, is it really fair that trillion-dollar corporations run AI to find security issues in people’s hobby code? Then expect volunteers to fix.“
- [gixy-ng: an overview of a gixy fork with updated, improved, and new checks](https://joshua.hu/gixy-ng-new-version-gixy-updated-checks)<br>Jak to může vypadat, když maintainer open source projektu začne fetovat AI: „I invested a significant amount of time into making this tool much better, and now the code that was created with love and passion was… replaced by an inferior (most importantly) codebase, with a heartless (and apparently dumb) robot.“
- [Douchebaggery](https://blog.codinghorror.com/douchebaggery/)<br>Článek, který Jeff Atwood kdysi napsal jako reakci na DHH, a kde dochází ke (dnes už zcela zjevně správnému) závěru, že DHH je tak trochu douchebag. Ale i když vás DHH nezajímá, je to pěkný text o tom, jak nemáte na lidi tlačit s tím, čemu fandíte, a jak nezáleží na tom, co používáte, ale co s tím vyrobíte. „When has abusing people into agreeing with you ever worked?“ „Don’t waste time arguing about the character select screen. Results speak loudest.“
- [WhatsApp v EU zavádí podporu pro zprávy z jiných aplikací](https://dotekomanie.cz/2025/11/whatsapp-v-eu-zavadi-podporu-pro-zpravy-z-jinych-aplikaci/)<br>Miluju EU! Aspoň za tu snahu! Ať už to dopadne jakkoliv.
