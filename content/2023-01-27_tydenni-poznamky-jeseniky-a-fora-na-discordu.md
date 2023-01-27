Title: Týdenní poznámky: Jeseníky a fóra na Discordu
Image: images/img-1577.jpg
Lang: cs
Tags: týdenní poznámky
Telegram-Comments: https://t.me/honzajavorekcz/92


Utekl zas nějaký ten týden (27. 1. až 27. 1.) a tak [stejně jako minule]({filename}/2023-01-27_tydenni-poznamky-jeseniky-a-fora-na-discordu.md) sepisuji, co jsem dělal a co jsem se naučil.
Tvořím [junior.guru](https://junior.guru/) a nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/) a členy by mohlo zajímat, co dělám.
Psaní poznámek mi taky pomáhá nezbláznit se a nepropadat pocitu, že je konec týdne a já jsem nestihl nic udělat.

![Hory]({static}/images/img-1577.jpg)


<!-- Honzo, piš jednu větu na řádek! https://sive.rs/1s -->


## Dovolená v Jeseníkách

Minulý týden jsem pracoval jen dva dny a v pátek jsem byl na horách, tak jsem poznámky nepsal.
Do Jeseníků jsme [jeli vlakem]({filename}2021-08-28_bez-auta.md).
Dítě v nosítku, nějaké ty baťohy a já táhl ještě boby, ale přišlo mi, že se vše odehrálo v dobré náladě a bez stresu.
Jeden přestup v Zábřehu, vlak s bistro vozem, bistro vůz s řízkem a kafíčkem, pohoda.
Dítě už konečně začíná vnímat, co vidí za oknem, tak máme zase novou zábavu.

![Nádraží Ramzová]({static}/images/img-1592.jpg)

Trochu blbé je, že jsme si z hor odvezli zase nějakou chorobu.
Naštěstí nic vážného.
Kašlíček a rýmička.
I tak už mě to ale unavuje, v podstatě měsíc v kuse nejsem fit.
Smrkání a zalévání coldrexů mi taky bere energii pouštět se do nových věcí.


## Fóra na Discordu

Konečně jsem na to sedl a udělal to.
Přidal jsem do bota podporu pro to, aby uměl číst kanály typu fórum, [které Discord před časem přidal](https://discord.com/blog/forum-channels-space-for-organized-conversation).

Když už jsem měnil kód, zkusil jsem bota naučit i nový, pohodlnější způsob načítání klasických vláken.
Tento nový způsob dřív neexistoval, ale [pycord](https://pypi.org/project/py-cord/) už nějakou chvíli tyhle věci má.

Při tom jsem zjistil, že nový a starý způsob vrací různý počet vláken.
Nemohl jsem přijít na to proč.
Skončilo to až u toho, že jsem si všechna vlákna nechal vyjet jako CSV a pak použil [tohle](https://www.textcompare.org/csv/compare) (šikovná věc!), abych je porovnal.

Zjistil jsem, že někdy lidé založili vlákno, ale pak si to rozmysleli a smazali jeho počáteční zprávu.
Zbytek vlákna však zůstal viset v paměti Discordu jako sirotek.
Starý způsob je nenašel, ale nový tyto sirotky přečte.
Záhada odhalena, vše je v pořádku.

Každopádně jsem tedy do klubu přidal první kanál typu fórum.
Nahradil jsem jím starou poradnu, protože tam to dává největší smysl.

![Původní poradna]({static}/images/screenshot-2023-01-27-at-14-22-24.png)
Původní poradna

![Nová poradna]({static}/images/screenshot-2023-01-27-at-14-20-21.png)
Nová poradna

Žádné další velké změny jsem nedělal, abych lidi nezahltil, a aby si měli čas prohlédnout, jak fórum funguje a co umí.
Ponoukl jsem členy, aby mi psali nápady, kde všude by se to dalo dále využít.
Strhla se zajímavá debata o tom, jak by šlo přeuspořádat klub.

Fórum umí i tagovat témata.
Přidával jsem v poradně tagy: Python, JavaScript, Java… ale brzy jsem narazil na strop.
Limit je 20 tagů na fórum, takže s nimi musím šetřit.
Aby tagy co nejvíc kopírovaly dosavadní realitu, vyjel jsem si všechna témata ze staré poradny a očima analyzoval, do jakého tématu zhruba spadají.

![Tagy]({static}/images/screenshot-2023-01-27-at-14-23-28.png)

Změny jsem pak všude v klubu s velkým jásotem oznámil a starou poradnu archivoval.


## Nástěnka a přednášky

Přednášek je už tolik, že se nevešly na nástěnku.
Discord má limit znaků na tzv. _embed_ u příspěvku a ten už přednášky přesáhly.

Myslel jsem, že bych vytvořil celý nový kanál jen na přednášky.
Nejspíš kanál typu fórum, kde by každé vlákno bylo pro jednu přednášku.
Spravoval by to bot a byl by to takový pěkný archiv záznamů přednášek.

Pak mi ale došlo, že je to hodně programování, které v [plánech na rok 2023]({filename}2022-12-26_strategie-na-2023.md) nemám.
A že to jde zatím řešit i jednodušeji.
Zaznamenal jsem si to jako nápad a nástěnku jsem upravil tak, aby ukazovala jen posledních deset přednášek.
Nenechal jsem se unést!
Držím směr!
Musím se pochválit.

![Seznam záznamů přednášek]({static}/images/screenshot-2023-01-27-at-14-17-29.png)
Na screenshotu je chyba, poslední věta je nalepená na poslední přednášku. Všiml jsem si toho díky psaní těchto poznámek a hned jsem to v kódu opravil.


## Discord Server Template

Naučil jsem bota vytvářet a každý den aktualizovat tzv. _server template_.
Je to způsob, jak si na Discordu zazálohovat aspoň nastavení serveru, když už nic.

Bylo to hodně jednoduché na vytvoření.
Ale jak to teď tak píšu, došlo mi, že to má vadu.
Když mi někdo zlikviduje klub, mohlo by se stát, že se pak nad ránem spustí bot a změny automaticky uloží.
Přepíše zálohu.
To budu muset asi ještě promyslet!


## Podcast

Pavlína vydala novou epizodu [podcastu](https://junior.guru/podcast/).
Poslechl jsem si ji a moc se mi líbila.
Na LinkedIn jsem ji ale [promoval až včera](https://www.linkedin.com/posts/honzajavorek_feedback-impostorsyndrome-activity-7024349175571980289-PcvL?utm_source=share&utm_medium=member_desktop).

Začínám se s Pavlínou dělit o zisk, který mám díky spolupráci s firmami.
Domluvili jsme se, že mi bude posílat fakturu za každou epizodu.

Začneme také označovat epizody, které jsou finančně podpořené spoluprací s firmami.
Zatím takové nebyly, ale budou.
Pozvání do podcastu mám teď normálně v ceníku.

Epizodu s Lukášem z Fakturoidu jsme nedělali na základě aktuálního tarifu z ceníku.
Fakturoid si však od začátku existence junior.guru platí nejvyšší tarify a příprava epizody odpovídala spíš spolupráci.
Bude to tedy taková epizoda na pomezí, kterou asi nakonec jako spolupráci označím.

Zkusil jsem si do [podcastového YAMLu přidat údaj o firmě](https://github.com/honzajavorek/junior.guru/blob/35075510b8555a01f233b43b6f9df20697f1ac21/juniorguru/data/podcast.yml#L26), ale zatím se to neprojevuje ani na webu, ani v popiscích epizod.


## Blog

Povedlo se mi zjistit, proč mi v GitHub Actions nefungoval `PAT` (_personal access token_) na to, aby commit zpět do repozitáře udělaný z Actions vyvolal další build.
[Podle dokumentace](https://github.com/EndBug/add-and-commit#the-commit-from-the-action-is-not-triggering-ci) se musí token nastavit pro `actions/checkout@v3`.
To jsem dělal a nefungovalo to.
Teď jsem si všiml, že mám v buildu ten checkout dvakrát!
Jednou na začátku, kam jsem ten PAT dával, ale uprostřed buildu jsem potřeboval resetovat Git, tak jsem tam měl checkout znova a ten jsem úplně přehlédl.
Ten tedy použil zase vestavěný `GITHUB_TOKEN`, který nestačí, a proto to celou dobu nefungovalo.
Opraveno, funguje.

Když teď napíšu článek a udělám `git push` na GitHub, spustí se GitHub Action, která jej publikuje na GitHub Pages, následně vezme odkaz na článek a ten mi pošle soukromou zprávou na Telegram.
To způsobí, že Telegram načte náhledový obrázek.
GitHub Action chvíli počká a pak tentýž odkaz dá do [mé telegramové skupiny](https://t.me/honzajavorekcz).
Vezme URL telegramového příspěvku a vepíše jej zpět do zdrojového kódu článku.
Tuto změnu commitne, pushne zpět na GitHub, a tam se opět publikují GitHub Pages.
V této nové verzi už je článek zpětně propojený s telegramovým příspěvkem, takže pod ním jdou načíst komentáře.
Krásné!

Co není krásné?
Že mi asi nefunguje ten [newsletter](http://eepurl.com/ifI06H).
Zdá se, že ačkoliv jsem minule vydal poznámky, nikomu to nic neposlalo.
Zřejmě není tak snadné udělat si vlastní Substack, jak jsem myslel.

Ale klidně se tam hlašte.
Ať už to nakonec vyřeším jakkoliv, ten seznam e-mailů použiju a rozesílat to začnu.

Když jsem psal tyto poznámky a chtěl jsem sem nahrát fotky z hor, zjistil jsem, že můj skript na automatické vcucnutí fotek do Markdownu neumí `.HEIC`.
Jakožto Apple ovce mám v `.HEIC` všechno, tak jsem přidal do skriptu podporu pro tento formát (použil jsem [pillow-heif](https://pypi.org/project/pillow-heif/)) a naučil jej konvertovat takové fotky do `.jpg`.


## Firmy

S Engetem jsem si měl volat kvůli připravované anketě mezi juniory, ale kvůli různým věcem jsme to několikrát posunuli.

Poslal jsem mail do dvou vzdělávacích agentur, se kterými jsem dřív komunikoval.
Nastínil jsem jim nový produkt, katalog agentur.
Jedna napsala, že to vypadá dobře, ale že zrovna řeší rozpočet a budoucnost na tento rok a potrvá to, tak se ozve později.
Druhá napsala, že to vypadá dobře a rádi budou spolupracovat.

Následně jsem tento týden dotáhl _deal_ s [Green Fox Academy](https://www.greenfoxacademy.cz/), který souvisí s mým novým záměrem dělat v určitých mezích byznys i se vzdělávacími agenturami.
Logo je na webu, faktura poslána!

![Green Fox Academy na příručce]({static}/images/screenshot-2023-01-25-at-20-01-24.png){: .img-thumbnail }
Green Fox Academy mají nejvyšší tarif, takže je jejich logo i na příručce.

V klubu je bot ještě neuvítal, protože jsem to na chvíli vypnul.
Chci tuto funkčnost zrovna revidovat a vylepšit.
K tomu ale potřebuji dokončenou novou evidenci firem.


## Evidence firem

Začal jsem připravovat nový způsob evidence závazků, které mám k firmám.
Jednak moje Excelová tabulka přestává trochu stačit, jednak chci být transparentní i v tomto, především kvůli tomu, aby lidi znali moje závazky se vzdělávacími agenturami a mohli zvážit, jak moc nezávislý jsem.

Začal jsem si do YAMLu přepisovat [ceník](https://github.com/honzajavorek/junior.guru/blob/35075510b8555a01f233b43b6f9df20697f1ac21/juniorguru/data/company-plans.yml) a [seznam firem](https://github.com/honzajavorek/junior.guru/blob/35075510b8555a01f233b43b6f9df20697f1ac21/juniorguru/data/companies.yml).
Zatím to není na nic napojené, akorát jsem skriptem ověřil, že údaje o firmách jsou totožné s údaji v Excelu a že jsem se někde při přepisování nespletl.

Chtěl bych mít stránku pro každou firmu, kde budou informace o tom, co si objednali, co jsme už udělali, co ještě zbývá udělat, kdy končí jejich spolupráce, apod.
Nejspíš to bude někde v rámci [/open/](https://junior.guru/open/).

Bylo by super, kdybych tam mohl mít i malinkou klientskou sekci, kde by viděli i poslední faktury, nebo by tam měli odkaz, přes který mohou posílat lidi do klubu.
To však nejsou veřejné věci a můj web jsou statické stránky.
Existuje nejspíš hodně složitých způsobů, jak to řešit.
Z těch jednoduchých se mi líbí zatím tři:

1.  Zaheslovat to nějak přes [PageCrypt](https://dev.to/render/password-protect-static-sites-with-pagecrypt-4dia).
    Má to různé nevýhody, ale nejdůležitější je podle mě z hlediska UX.
    Vůbec nevím, co by mělo být heslo, aby si ho někdo, kdo se mnou v té firmě vyjednává partnerství, pamatoval i za půl roku.
    Údaje jako faktury nebo odkaz do klubu tam chci mít, aby je ti lidi měli po ruce a neptali se mě na to.
    Tohle by jen změnilo jejich dotaz na dotaz ohledně zapomenutého hesla.
2.  Poslat jim tyto rozšířené informace mailem.
    E-mail by mohl chodit čtvrtletně, to mi přijde jako rozumná frekvence vzhledem k tomu, že spolupráce s firmami mám roční a naše aktivity mívají spíš pomalejší tempo.
3.  Udělat to variantou 2., ale ne teď.
    Nechat to na jindy jako možné vylepšení, protože je to jen blbina navíc.

Pokud zjistím, že těm lidem stejně potřebuji něco posílat e-mailem (např. že bude končit spolupráce a měli bychom se bavit o tom, jestli chtějí prodloužit), tak udělám variantu 2.
Jinak 3.


## Audit vzdělávacích agentur

Volal jsem si se zakladatelem Green Fox Academy a bavili jsme se o katalogu vzdělávacích agentur a o nezávislém auditu bootcampů.
V Maďarsku to [existuje](https://ivsz.hu/bootcamp-auditjelentes/) a kultivuje to tamní trh vzdělávacích agentur.

Přišlo mi, že by to mohl být zajímavý krok, jak vylepšit můj budoucí katalog a jak mu dodat velkou váhu.
Chtělo by to ale spojit se v tomto s nějakou seriózní institucí, které budou ostatní věřit víc, než brýlatému týpkovi s webovkou, která má v názvu „guru“.

Zkusil jsem hned hodit e-mail do [DigiKoalice](https://digikoalice.cz/), když už jsem členem, jestli to není náhodou něco, co by je zajímalo.
Když to bude vlažné, tak zkusím, co by mi poradili v [Česko.Digital](https://cesko.digital/).


## Infrastruktura

-   Zjistil jsem, že mi na CircleCI nefungují některé věci.
    Bylo to tím, že po jejich [nedávném security incidentu](https://circleci.com/blog/jan-4-2023-incident-report/) (až by se dalo říct _fuckupu_) nejspíš pro jistotu invalidovali všechny svoje tokeny.
    Takže jsem si udělal nové a pak už vše jelo.
-   Zjistil jsem, že můj geniální systém na paralelizaci buildu nepočítá s tím, že na CircleCI použiju funkci „restartuj build, ale jen od toho místa, kde to failnulo“.
    Prostudoval jsem ještě jednou _environment variables_, které mám k dispozici.
    Místo `CIRCLE_WORKFLOW_ID` teď používám `CIRCLE_WORKFLOW_WORKSPACE_ID` a zdá se, že to funguje přesně tak, jak potřebuji.
-   Vytvořil jsem si příkaz `jg install`, který mi umožní jednoduše při vývoji udělat `git pull --rebase origin main`, potom `poetry install`, `playwright install` a `npm ci`.
-   Všiml jsem si, že `playwright install` stahuje tři prohlížeče, ale já používám jen jeden.
    Tak jsem to změnil na `playwright install firefox`.
    Díky tomu jsem zjistil, že mi vše spadlo, protože ten jeden prohlížeč, který jsem v kódu používal, bylo ve skutečnosti Chromium.
    Tuto herezi jsem napravil a nyní kód všude používá jediný správný prohlížeč, [Firefox](https://www.mozilla.org/cs/firefox/new/).
-   Trochu neplánovaně jsem se pustil do zkoumání, zda a jak obtížné je udělat commit ze CircleCI zpátky na GitHub.
    Pomohlo by mi to s perzistencí některých dat.
    Navíc by to umožňovalo [sledovat i historické změny](https://simonwillison.net/2021/Dec/7/git-history/), pokud bych to potřeboval.
    Četl jsem si [tohle](https://support.circleci.com/hc/en-us/articles/360018860473-How-to-push-a-commit-back-to-the-same-repository-as-part-of-the-CircleCI-job) a [tohle](https://blog.jdblischak.com/posts/circleci-ssh/).
    U toho jsem si uvědomil, že commity ze CircleCI na GitHub už dávno dělám, protože odtamtud dělám deploy na GitHub Pages.
    To není nic jiného, než commit a push do `gh-pages` větve.
    Na zkoušku jsem naimplementoval automatické formátování kódu pomocí [isort](https://pypi.org/project/isort/).
    Trochu jsem se do toho celého zavrtal a zjednodušil jsem dost věcí v konfiguraci CircleCI.
    Také jsem vyhodil [CircleCI Orb na GitHub Pages](https://github.com/sugarshin/gh-pages-orb) a vyměnil jej za léty ověřený [ghp-import](https://github.com/c-w/ghp-import).
    Udělal jsem to především proto, že jsem konfiguraci pushování na GitHub [sdílel na více místech](https://github.com/honzajavorek/junior.guru/blob/03a362774ac174fda226bc138c30f669f35ab1ac/.circleci/config.yml#L16) a potom už nedávalo moc smysl ten Orb používat.


## Další

-   [Zeptal jsem se](https://github.com/crdoconnor/strictyaml/issues/191), jestli můj oblíbený strictyaml umí i něco jako Date, protože častěji potřebuji jen datum, než [datum a čas](https://hitchdev.com/strictyaml/using/alpha/scalar/datetime/).
-   Měli jsme v klubu [přednášku s Týnou Doležalovou o Analýze geoprostorových dat, GIS a geospatial data science](https://www.linkedin.com/posts/honzajavorek_datascience-geospatial-geospatialdata-activity-7023236557289488384-8IQr?utm_source=share&utm_medium=member_desktop).
    Mě se moc líbila a vypadá to, že lidem taky a pouští si ji dost i ze záznamu.
    O vytvoření záznamu se opět postaral můj pomocník a stále si strašně užívám, jak jednoduché pro mě teď ty přednášky jsou.
-   Ozval se mi [Štefan Prokop](https://www.linkedin.com/in/stefanprokopdev/) a plánujeme přednášku na téma security.
-   Napadlo mě, že by click mohl umět automaticky generovat tasky pro VS Code.
    Ale možná je to blbost.
    [Zeptal jsem se](https://github.com/pallets/click/discussions/2442), jestli je to blbost, nebo jestli to už neexistuje.
-   Stát mi vytvořil třetí datovou schránku.
    Proč musím mít zvlášť schránky jako smrtelník a jako živnostník, to mi fakt uniká.
    Nepřišel jsem na to, jak se mohu mezi svými schránkami přepínat bez toho, abych se musel odhlásit.
    Nainstaloval jsem aplikaci [Datovka](https://www.datovka.cz/).
    Jsem rád, že existuje, ale vypadá jak nějaký linuxový e-mailový klient z devadesátek.
    Po otevření na mě vyskočil formulář s dvaceti políčky.
    Pro vyplnění bych potřeboval návod, takže jsem aplikaci zase zavřel.
    Nastavím ji a využiju až pokud mi bude chodit pět zpráv do datovky týdně.
-   Bavil jsem se s Memberful supportem.
    Jako obvykle skvělá zkušenost.
    Zajímalo mě, jak přesně funguje funkce na [přesunutí lidí mezi tarify](https://memberful.com/help/manage-your-members/move-all-members-of-a-plan/).
    Pak jsem chtěl vědět, zda mohu přes API vytahovat informace o _custom fields_ (kde lidi narazili na junior.guru) a _cancellation surveys_ (proč ruší předplatné), abych to mohl analyzovat, nebo si to někam posílal.
    Zatím to nejde.
    Custom fields [jen přes nějaké webhooky](https://memberful.com/help/customize/create-custom-fields/#can-custom-field-data-be-accessed-outside-the-memberful-dashboard).
    Cancellations však mohou odesílat automatický e-mail, kde mohu lidem něco napsat.
    Chtěl bych to využít k tomu, že když někdo zruší předplatné kvůli penězům, v tomto e-mailu bych nabídl, ať zkusí stipendium.
-   Prdla nám žárovka v digestoři, tak jsem koupil novou.
    Při té příležitosti jsem koupil i nové filtry.
    Dnes jsem to vyměňoval a zevnitř jsem to i trochu očistil.
    Překvapilo mě, že vnitřek digestoře není ve skutečnosti žlutý, ale bílý.
    Jedna z nevýhod bydlení v nájmu je, že pokud děláte nějakou údržbu spotřebičů, nejspíš jste první člověk v historii bytu, který se do toho pustil.
-   Nainstaloval jsem si konečně na počítač osmou verzi 1Password.
    Zaujala mě pak novinka, [použití 1Password pro CLI nástroje](https://www.youtube.com/watch?v=7aT4K1AMfGI).
-   Šel jsem volit.
    Nepotřeboval jsem se tentokrát o ničem rozhodovat, takže jsem v rámci zachování duševního zdraví vynechal všechny články a debaty na téma prezidentských voleb.
    Podle zoufání kamarádů, kteří se neubránili, to považuji za výborné rozhodnutí.
-   Odpovídání v klubu, e-maily, [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), atd.
    Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
    První týden jsem doháněl e-maily ještě z Vánoc, potom se to už trochu uklidnilo.
    V klubu jsme řešili spoustu věcí, takže tam jsem strávil fakt hodně času.
-   Během 15 dní od 13. 1. do 27. 1. jsem při procházkách nachodil 5 km, na túrách nachodil 13 km. Celkem jsem se hýbal 8 hodin a zdolal při tom 18 kilometrů.
-   Finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).
    Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/215426887eaaad9105ecf647d0ff24cf94de7c9eb47cc6f2c55e6921/)


## Povedlo se

Udělal jsem něco z [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md)?

-   Přidal jsem úplně základní podporu pro forum kanály a pozoruji, jak to lidi používají.
-   Komunikoval jsem se vzdělávacími agenturami a zjišťoval zájem o MVP katalogu.
-   Udělal jsem kroky, které mi umožní mít ceník přímo na webu.
-   Udělal jsem kroky, které mi umožní mít na webu přehled spolupráce s firmami: „Firma musí vědět vše o svém předplatném, v jakém je stavu, kolik čeho zbývá. Já i firma musíme mít včas informaci, že se blíží konec.“
-   Udělal jsem kroky, které mi umožní označovat epizody, které jsou finančně podpořené spoluprací s firmami.
-   Začnu se s Pavlínou dělit o zisk, který mám díky spolupráci s firmami.
-   Měl jsem dovolenou. Byla ale krátká a chodil jsem během ní občas do klubu.
    Ve strategii jsem si nařídil delší dovolené.


<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví.**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>


## Plánuji

1.  Pokročím ve zpracování evidence spolupráce s firmami a nechám bota uvítat Green Fox Academy v klubu.
2.  Projdu všechny kupóny na Memberful a upravím je, aby šly použít na nové tarify.
3.  Pořádek v Trellu.


## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel toto:

- [Genders.WTF](https://genders.wtf/)<br>Lidi, kteří tvoří formuláře, zjevně opravdu zápasí s dotazem na gender
- [Programming, Fast and Slow | Almad&#39;s Changelog](https://almad.blog/essays/programming-fast-and-slow/)<br>Po čase jsem si to znova přečetl a nemohu než souhlasit. Na základě zkušeností z práce, hobby projektů a komunitních projektů: Vidím to úplně stejně.
- [Cruel optimism (and lazy pessimism)](https://tegowerk.eu/posts/cruel-optimism/)<br>„Cruel optimism boils down to the folly of suggesting personal solutions to systemic problems. It’s about advice given from a position of privilege to people who will never be able to apply it to their own lives–because the cards are stacked so unfairly against them–but who will nonetheless interpret their failure as a personal one“
- [Milá ČT, oslovili jsme za Tebe expertky do volebního vysílaní. Přišlo by jich 37](https://refresher.cz/129254-Mila-CT-oslovili-jsme-za-Tebe-expertky-do-volebniho-vysilani-Prislo-by-jich-37)<br>Dobrý stěr 😀
- [My si nezačali, tvrdí lidé z Babišovy marketingové mašiny. Kampaň je brutálnější, než čekali](https://www.e15.cz/volby/prezidentske-volby/prezidentske-volby-2023/my-si-nezacali-tvrdi-lide-z-babisovy-marketingove-masiny-kampan-je-brutalnejsi-nez-cekali-1396105?ref=mimo-agendu)<br>Ze zákulisí Babišova marketingového týmu.
- [Nadchází doba nenápadného plýtvání: nespotřebovaných předplatných](https://www.mediar.cz/nadchazi-doba-nenapadneho-plytvani-nespotrebovanych-predplatnych/)<br>Kolik služeb si platíte vy?
- [Agent Babiš, rozvědčík Pavel. Co mají společného? — Vinohradská 12](https://www.mujrozhlas.cz/rapi/view/episode/3049411b-0514-3a31-99be-a3ec0ff0cffe)<br>Zajímavý pohled na oba kandidáty z hlediska jejich angažmá za minulého režimu. Přesně pro tyhle díly, které překročí tuny hnojometů a najdou si odstup a užitečný pohled na věc, Vinohradskou 12 rád poslouchám.
- [Why 97% of Namibia is Empty](https://www.youtube.com/watch?v=arzhTBqTd7I)<br>Zajímavé video o Namibii (kde jsem byl na PyCon NA a kam byste měli jet taky)

