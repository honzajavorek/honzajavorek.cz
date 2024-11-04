Title: Týdenní poznámky: Peklíčko s nemocemi
Image: images/img-2903.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/331
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/113426399088583360

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-10-19_tydenni-poznamky-nove-kapitoly-do-kurzu-scrapovani-a-pece-o-marody.md) už utekl nějaký ten týden (19. 10. až 4. 11.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/img-2903.jpg)
Moje poslední týdny byly turbulentní asi stejně jako VC Brazílie

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Stará „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md), nová teď nejsou.

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Špatné

Ani nevím, kde začít. Nebo co vlastně všechno psát. Poslední týdny byly peklíčko, kdy se žena prala s nekonečně dlouhou a ošklivou nemocí, měli jsme u nás nekonečně dlouho babičku, pak zase onemocněla i dcera… všichni kašlali přes den i přes noc, takže se nedalo spát. A protože jsem byl zdravý a plný sil, tak jsem si šel zaběhat a projel se na kole, abych provětral hlavu v náročné rodinné situaci. Takže jsem onemocněl taky 💪

Mezi staráním se o rodinu, snahami o to, aby mi nejeblo, a utrpením během nachlazení jsem nakonec stihl něco udělat i do práce. Nicméně mnohdy když jsem si k práci sednul, neměl jsem na ni ani chuť a zabýval jsem se nepodstatnými věcmi, místo abych dělal ty důležité. Nebo jsem našel deset popadaných skriptů a jen donekonečna něco opravoval. Myslel jsem, že programování mi přinese radost, tak jsem se do něj vrhnul i na dlouhé hodiny, ale většinou vyšly vniveč, protože výsledek stejně moc dobře nefungoval.

![Nevím, dál]({static}/images/img-2832.jpg)
Fotka u vstupu na nějaké čtení poezie v Hlíně na Hybernské

## Dobré

Když ale projíždím fotky za poslední týdny, vidím, že jsem prožil i spoustu krásných chvil. Protáhl jsem babičku a dceru po Praze, užil jsem si krásného počasí, uvařil a upekl jsem spoustu dobrých jídel (máme novou wok pánvičku!), měl jsem čas koukat na F1, cyklovyjížďka s dcerou byla úplně skvělá, zašel jsem si do sauny, a když mi bylo nejhůř, hned dva kamarádi si na mně našli čas. Jeden se mnou zašel na pivo, abych na něj mohl vysypat všechny svoje frustrace, a s druhým jsme uspokojili mou akutní eskapistickou touhu prožít v centru Prahy něco dobrodružného - zašli jsme do Skautského institutu a pak vylezli na Staroměstskou věž, kde jsme ještě nikdy ani jeden z nás nebyli.

![náplavka]({static}/images/img-2746.jpg)
náplavka

![Kaple sv. Kláry]({static}/images/img-2835.jpg)
Sv. Klára nad Trojou

![Hamerský rybník]({static}/images/img-2846.jpg)
Hamerský rybník s nenažranými rybami

![Kunratický les]({static}/images/img-2850.jpg)
Kunratický les

![Staré město]({static}/images/img-2810.jpg)
Staré město z věže

## Kontrola platnosti pracovních inzerátů

Pracovní inzeráty bot stahuje několikrát týdně. Problém ale je, že mohou kdykoliv vypršet a tak se bohužel docela často stalo, že bot nasypal do klubu a na web nové nabídky práce, ale hned několik z nich bylo už prošlých.

Mohl bych zvýšit frekvenci stahování inzerátů, ale to by bylo marginální zlepšení kvůli pár inzerátům, těch pár inzerátů by to plně stejně nevyřešilo, a vytvářel bych velkou zátěž na infrastrukturu svou i těch webů, ze kterých nabídky stahuju.

Jediná rozumná cesta, která mně napadla, byla tedy kontrolovat inzeráty těsně před jejich publikací. Díky tomu by mělo stačit kontrolovat třeba jen výsledných 100 nabídek a ne stahovat znova a znova průběžných 1000 nevytřízených.

Už mám nějaké zkušenosti, takže jsem nebyl tak naivní, abych si myslel, že udělám `for job in jobs` a pro každý z nich `requests.get()`, abych zjistil, jestli jsou aktuální. [Bylo by to krásné](https://mastodonczech.cz/@honzajavorek/113363190309608611), ale takto jednoduchý dnešní svět [bohužel není](https://mastodonczech.cz/@honzajavorek/113363681392686510).

Hned zkraje jsem to začal stavět jako nový scraper na Apify. Musel jsem výrazně upravit i [Plucker](https://github.com/juniorguru/plucker), protože moje monorepo zatím neobsahovalo žádné scrapery, které se pouští na vyžádání a ještě s nějakým vstupem.

Následoval v podstatě týden zápasení s tím, abych to rozchodil. [Tohle](https://mastodonczech.cz/@honzajavorek/113363190309608611) jsem psal, když jsem si myslel, že mám hotovo, ale potom ještě následovalo mnoho úprav. Nejjednodušší práce byla s Jobsy. SJ měly brutální ochranu, ale naštěstí mám od nich export, takže jsem akorát přestal chodit na samotné inzeráty a prostě zkontroloval, zda je nabídka stále ještě v exportu. Největší problém je samozřejmě jako vždy s LI, kvůli kterému teď trvá kontrola 150 nabídek něco přes 10min a i tak občas selže.

Tuhle věc jsem programoval, protože je to potřeba, ale zároveň mě to vůbec nebavilo. Ovládaly mě pocity naštvání ze stavu dnešního internetu, bezmoci, a celkově bych do toho nejraději kopnul a vykašlal se na to. Ale LI je docela důležitý zdroj nabídek pro juniory a [nemůžu to nechat jen tak být](https://mastodonczech.cz/@honzajavorek/113364407078436832).

Co mi pomohlo: [scrapy-fake-useragent](https://pypi.org/project/scrapy-fake-useragent/) ani moc ne, [scrapy-impersonate](https://pypi.org/project/scrapy-impersonate/) víc, ale stejně to na LI nestačí, ani s Apify proxy.

Ještě jsem pak upravil skript, který posílá inzeráty do klubu, aby archivoval vlákna s prošlými nabídkami. Ještě ale nevím, jestli to nepředělám na nějaký viditelnější štítek, protože ta archivace není moc zřetelná. A taky mi to archivuje ručně přidané nabídky, což je bug.

![Krása]({static}/images/screenshot-2024-10-29-at-20-51-24.jpg){: .img-thumbnail }

## Nové srazy

Dotáhl jsem věci z minula a předělal v klubu srazy tak, aby se oznámení na události už nevytvářely jako Discordí události a nespamoval se s nimi kanál #pozvánky-a-promo, protože to zabilo _engagement_ a nebylo to asi ani moc užitečné, ani přehledné.

Teď se jednak vše přesunulo na Apify scrapery, takže je to robustnější, jednak jsem přidal Java srazy, jednak se to posílá do nově vytvořených lokálních skupinek. Lidi se „hlásí“ pomocí emoji a časem třeba přidám funkci, že jim bot připomene, že akce je dnes. Ale už teď ostatní díky emoji reakcím vidí, kdo chce jít.

Zároveň se ve skupinkách buduje kontinuální lokální komunita, a to vidím jako jednoznačný přínos nového řešení. V Brněnské to žije tak, že už se i sešli, v Pražské se plánuje nějaký cowork. Oboje bez ohledu na oficiálně konané srazy, jen z toho titulu, že vznikl prostor, jak se družit podle místa, kde kdo žije. Největší radost mám ale z toho, že se možná sejdou a poznají dva lidi od Rychnova nad Kněžnou 💪

Kromě nasazení nového kódu jsem vypnul starý, pročistil jsem Discord od starých pozvánek, sepsal oznámení, atd. Měl bych ale ještě sepsat klubový tip o tom, jak to funguje, a víc to ještě protlačit mezi lidi - třeba i přes _mention_ na všechny členy, protože i lidi, kteří klub docela sledují, byli překvapení, že to je teď takhle.

![Skupinky]({static}/images/screenshot-2024-11-04-at-13-03-54.png)

## Nová „nástěnka“

Když byly srazy hotové, ale vše kolem scraperů a pracovních inzerátů mě dost unavovalo, rozhodl jsem se, že poladím pár věcí v klubu, což jsem už dlouho nedělal.

Trnem v oku mi byl kanál „nástěnka“, který dřív sloužil jako místo, kde jsou permanentní informace. Jenže pak Discord přidal [Průvodce serverem](https://support.discord.com/hc/en-us/articles/13497665141655-Server-Guide-FAQ), tak jsem začal různé věci přesouvat tam. Nástěnka zůstala osekaná a trochu zbytečná.

Jenže Discord vyžaduje kanál, kde budou „pravidla“, takže jsem ho nemohl úplně zrušit. Vymyslel jsem, že tam dám pár základních věcí, pod to vypíšu tipy na to, jak v klubu co funguje, a zkusím to celé vcucnout do Průvodce serverem jako první stránku. A tak se i stalo.

Při práci na nástěnce a na tipech jsem změnil způsob, jak se aktualizují kanály, které jsou součástí Průvodce serverem. Dřív jsem to udělal „jednoduše“ tak, že se prostě přepsaly jednou za měsíc. Hlavně u záznamů přednášek to ale vypadalo divně, když tam dlouho nový záznam chyběl. Takže jsem to teď zlepšil a aktualizuje se to na základě toho, zda se změnila podkladová data.

![Nová nástěnka]({static}/images/screenshot-2024-11-04-at-18-37-06.png)

## Lepší nahrávání emoji

Taky jsem se podíval na to, jak používám emoji, když je chci mít v _embedu_ Discord zprávy jako náhledový obrázek. Tohle jsem už potřeboval pro seznam rolí, ale těch je jen pár, tak jsem si prostě stáhl ručně z [Emojipedie](https://emojipedia.org) průhledná PNGčka pro těch pár emoji, pak dostal z Unicode znaků pro dané emoji jejich název, a podle něj se na disku hledal odpovídající soubor. Ten se nahrál jako náhled _embedu_.

Tohle bylo moc hezké a dostačující, dokud jsem nechtěl na nové nástěnce vypsat i klubové tipy, kterých je hodně a musel bych pro každý jednak stáhnout ručně zase to PNG, což není úplně zábavné (je to celkem zahrabané v rámci té stránky a každé stáhnutí je asi 10 netriviálních kliků), ale hlavně bych musel při psaní nových tipů vždy ještě stahovat to PNG a nezapomenout na to, a to už bych asi nenapsal tipy nikdy žádné nové. Taky jde tušit, že se tenhle způsob prezentace informací osvědčuje a že tuhle funkcionalitu využiju i v budoucnu.

Zabředl jsem tedy do toho, jak bych mohl ta PNG z daného emoji získat nějak automaticky. Přímočaré by bylo vždy scrapnout Emojipedii, ale taky by to bylo ukrutně blbé, protože bych s takovou věcí jednak závisel zase na externí službě, zase bych měl další scraper, nějak by se to muselo _ad-hoc_ samo scrapovat a pak kešovat nebo ukládat, no prostě bordel. Po týdnu s nefunkčními scrapery jsem tohle už nechtěl.

Zkoumal jsem Twemoji a zjistil jsem, že mají [fork](https://github.com/jdecked/twemoji/), kde ex-Twitter a Discord vývojářky a vývojáři dokonce vydávají nové verze. Tam jsou v branchi `gh-pages` vygenerované všechny PNG i SVG, ale názvy souborů jsou nějaká změť znaků. Tak jsem trochu zjišťoval, snažil se číst kód (nepochopil jsem), a nakonec vytušil, že to jsou _codepoints_. Což jsem nevěděl co je, ale tak to už se dalo nějak hledat a zjistit, jak se k tomu dostat přes Python. Prostě je to kód každého znaku v Unicode. Ale bez nějakých těch spojovacích znaků, ty jsem musel ořezat. Pak stačilo seskládat správnou URL tak, abych mohl mít funkci, [která pro zadané emoji vrátí URL na obrázek](https://github.com/juniorguru/junior.guru/blob/68f581c99fd44755c2fc56081255560559881780/tests/test_lib_text.py#L31).

Kdybych potřeboval soubor, oproti scrapování Emojipedie by mi to zas tak moc nepomohlo - i když jedno „vypočítané“ URL pořád lepší než zjišťovat pro každé emoji URL scrapováním. Jenže já nepotřeboval soubor, při nahrávání na Discord ve skutečnosti potřebuju URL, a to může vést buď na přiložený soubor přes `attachment://`, nebo kamkoliv na internet. Takže místo obrázků na disku a nahrávání na Discord teď vkládám jen vypočítané URL!

Jediná nevýhoda je, že to PNG není tak hezké jako to z Emojipedie. Jsou to čtverce 72px, zatímco na Emojipedii měli 500px, takže i na mé retině to vypadalo hezky. Teď je to trochu rozmazané, ale tuto daň jsem ochoten v tomto případě přijmout. SVG bohužel na Discord takto nahrát nejde.

Javorek právě napsal skoro 3.000 písmenek o nahrávání emoji obrázku na Discord. To jste si určitě potřebovali dneska přečíst, co?

## Nové tipy

Napsal jsem i dva nové tipy popisující jak v klubu něco funguje:

-   [☕ Jak se zapojit do rituálů?](https://github.com/juniorguru/junior.guru/blob/main/jg/coop/data/tips/11_rituals.md)
-   [🔬 Jak dostat zpětnou vazbu na CV nebo kód?](https://github.com/juniorguru/junior.guru/blob/main/jg/coop/data/tips/12_feedback.md)

Jsou docela dlouhé, dřív jsem se to snažil co nejvíc zkracovat. Teď jsem se do nich snažil ale nacpat co nejvíc věcí, aby nemuselo být příliš mnoho tipů. Nevím, co je lepší strategie, ale každopádně napsané a existující tipy jsou lepší než nenapsané a neexistující.

![Nový tip]({static}/images/screenshot-2024-11-04-at-18-34-16.png)

## Opravy

Skoro každé ráno se probudím, otevřu mail a najdu tam asi pět spadlých věcí, které pak postupně opravuju. Už mě to moc nebaví. Většinu z toho sem ani nebudu psát. Tady jsou věci, které možná stojí za zmínku:

-   Zjistil jsem, že itnoob.cz přestal existovat, tak jsem se optal, a fakt. Takže další odkaz, který teď míří do internetového archivu.
-   Mise je tak cool, že [začalo](https://github.com/jdx/mise/pull/2705) vytvářet `venv` pomocí `uv`, pokud je přítomno. Což je jistě rychlejší, ale vytvoří to virtuální prostředí, kde není `pip`, takže půlka věcí přestane fungovat. Milá věc, která měla být opt-in, ne opt-out, a ukrojila mi hodinu života.
-   Zkusil jsem konečně upgradovat MkDocs. Blokoval to [bug](https://github.com/mkdocs/mkdocs/issues/3532#issuecomment-2200135348), který se v nové verzi projevoval v tom, jak MkDocs pracují s `title`. K mému velkému překvapení jsem tento bug ale [nedokázal teď už reprodukovat](https://github.com/mkdocs/mkdocs/issues/3532#issuecomment-2426056828). Takže upgrade byl nakonec hladký!
-   Chtěl jsem přidat emoji do skriptu, který oznamuje přednášky. Při tom jsem si všiml, že skript nebude fungovat dobře během Týdne pro digitální Česko, kdy plánujeme dvě akce v klubu rychle za sebou. Hned jsem to opravil.
-   Předělal jsem jednu obtížně vysvětlitelnou část toho, jak se na junior.guru spouští skripty. Zkrátím to tak, že sdílení globálního stavu mezi jednotlivými skripty skrze environment variables nefungovalo dobře a že jsem nevěděl proč, ale pro jistotu jsem to přepsal tak, aby to používalo [diskcache](https://grantjenks.com/docs/diskcache/) stejně jako vše ostatní, co na projektu nově dělám.
-   [Opravil jsem problém v pycordu](https://github.com/Pycord-Development/pycord/issues/2399#issuecomment-2432813267) kolem nějakých neuzavřených connections v asyncio, který mě trápil už dlouho. Nevím, co to dělalo, ale zjistil jsem, že v upstreamu discord.py se jim to povedlo opravit. [Můj PR](https://github.com/Pycord-Development/pycord/pull/2618) bez velkých okolků přijali, ačkoliv jsem ani moc nevěděl, co vlastně dělám 😅
-   Opravil jsem regulární výraz, který špatně chytil „Hradec Králové – Kukleny + 5 dalších lokalit“ ve scraperu na Jobsy, což způsobovalo, že o mnoho dál mi pak selhal pokus o zjištění přesné lokace inzerátu.

![pisoáry]({static}/images/img-2826.jpg)
zdobená stěna nad pisoáry pod Staroměstskou radnicí

## Další

-   Michal Čihař objevil moji fiobank knihovnu a hned poslal několik PR: [status badge](https://github.com/honzajavorek/fiobank/pull/41), [pylama](https://github.com/honzajavorek/fiobank/pull/39), [testování 3.13](https://github.com/honzajavorek/fiobank/pull/40), [transakce v rámci jednoho requestu](https://github.com/honzajavorek/fiobank/pull/38) a [automatizování release procesu](https://github.com/honzajavorek/fiobank/pull/42). Tři jsem mergnul, dva čekají, až budu mít chvíli volno na to, abych dal knihovně nějakou lásku. Když na repozitáři nebyl žádný provoz, tak jsem neměl motivaci se jí moc věnovat, ale teď, když vidím, že to asi někdo používá a má chuť se podílet i na vývoji, tak si na to čas vyhradím.
-   Přidal jsem příkaz, který mi umožňuje spustit ve správném pořadí všechny skripty související s pracovními nabídkami a nic jiného. Použil jsem při tom [graphlib](https://mastodonczech.cz/@honzajavorek/113356894220208146) ze standardní knihovny.
-   Zrychlil jsem start všech junior.guru skriptů. Při každém startu se totiž iniciovala keš na dynamické generování obrázků (HTML + CSS + screenshot přes Playwright = obrázek). Při tom se spouštěl vždy i `esbuild` a další věci, což bylo dost pomalé (ale stále lepší, než to, co jsem kdysi měl). Přemýšlel jsem, zda mohu z esbuildu nějak dostat, na které soubory sahá. Díky tomu bych mohl vypočítat hash, kešovat to, a pouštět to celé jen pokud se nějaký ten soubor změnil. V dokumentaci jsem hledal dlouho, ale našel jsem prd. ChatGPT mi pak poradilo, že mohu po esbuildu chtít _metafile_, kde tohle je, a pak se mi to povedlo udělat.
-   Koukal jsem, jestli můžu ve Scrapy použít nejnovější Pydantic, ale [nemůžu](https://github.com/juniorguru/plucker/issues/60#issuecomment-2437603344).
-   Asi třikrát jsem opravoval nějaké nesrovnalosti v kontrole odkazů na [docs.pyvec.org](https://docs.pyvec.org/).
-   [Simple Analytics](https://simpleanalytics.com/junior.guru) jsou stále fajn, ale zjevně z roku na rok tiše podražily, protože mi přišla nějaká větší cena za prodloužení. Měnit to nebudu, ale trochu mě to naštvalo. Snažím se horko těžko přihazovat peníze na hromádku, aby konečně bylo dost, a mezitím všechny věci akorát zdražují a zdražují, takže to nikam nevede. Takhle jsem si ten [lifestyle business](https://en.wikipedia.org/wiki/Lifestyle_business) nepředstavoval 😅
-   Ozval jsem se Frontendistům, že mají komunitní přístup do junior.guru klubu a poradil, jak jej mohou využít, pokud chtějí.
-   Do [příběhů odjinud](https://junior.guru/stories/#pribehy-odjinud) jsem přidal [Život DEVky](https://zivotdevky.cz/2024/09/27/prvni-prace-v-it-aneb-proboha-co-jsem-si-myslela/).
-   Poslal jsem Patrikovi výsledky hlasování o přednáškách, abychom rozjeli spolupráci kolem přípravy přednášek. Taky jsme vymysleli, co bude prosincová přednáška, ale pak už jsem to nedokázal táhnout dál.
-   Přepsal jsem skript, kterým lokálně upgraduju závislosti na hlavním repozitáři junior.guru. Teď se vypořádá s konflikty mezi závislostmi mých vlastních projektů.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 17 dní jsem naběhal 32 km, při procházkách nachodil 17 km, ujel na kole 32 km. Celkem jsem se hýbal 16 h a zdolal při tom 81 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.
-   Pokud vám někdy Strava pokazí vaši trasu jako mně, když jsem běžel svůh epický běh, nemusí vám tím pokazit i náladu. Lze to celkem snadno opravit přes nástroj [gpx.studio](https://gpx.studio/) a nahrát znova ručně.

## Plánuji

Ne že bych měl nějakou představu, kdo bude kdy zdravý a kolik zbude na co času, ale zkusím být odvážný a něco si naplánovat:

1.  Věnovat se svým rodičům, kteří za námi přijedou pondělí-úterý.
2.  Dodělám resty:
    - Přečtu celý klub,
    - ozvu se Terce a všem dalším, co mi psali soukromou zprávu,
    - uzavřu už konečně dotazníky, vylosuju a pošlu knihy,
    - domluvím přednášku na prosinec,
    - pročtu maily,
    - sepíšu plán na zbytek roku.
3.  Budu zdravý na čtvrteční očkování proti covidu a chřipce.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [We don’t do that here: Setting social norms - Eric Holscher](https://www.ericholscher.com/blog/2023/feb/10/we-dont-do-that-here/)<br>Tohle tady neděláme. Jak se vypořádat s chováním v komunitě, které nechceme, ale zároveň ho nechceme vyloženě trestat a jak to efektivně přenést na nově příchozí.
- [Missing stair - Wikipedia](https://en.wikipedia.org/wiki/Missing_stair)<br>TIL že existuje metafora „missing stair“ pro situaci, kdy komunita chrání toxického člověka tím, že se ho nezbaví, ale naučí se kolem něj fungovat. Když přijde někdo nový, může si za případné neštěstí sám, protože špatně aplikoval nepsaná „pravidla“, jak se kolem tohoto člověka pohybovat, která se sdílí diskrétně.
- [How Google Reader died — and why the web misses it more than ever - The Verge](https://www.theverge.com/23778253/google-reader-death-2013-rss-social)<br>„There were people that met on Google Reader that got married.“ Příběh Google Readeru na základě rozhovorů s jeho tvůrci.
- [Cameron's World](https://www.cameronsworld.net/)<br>Dokonalý.
- [We can have a different web](https://www.citationneeded.news/we-can-have-a-different-web/)<br>„We may feel as though we are trapped in a tiny, crowded, noisy space, but it is only because we don't see over the walls.“ „People can experiment with combining the things they loved about the old gardens with the tools and models of the ones that have grown since then, or return to the spirit of experimentation and try new things altogether.“
- [Australia/Lord_Howe is the weirdest timezone](https://ssoready.com/blog/engineering/truths-programmers-timezones/)<br>Krásný článek o prapodivnostech v časových pásmech, které znesnadňují programátorům život.
- [Writes and Write-Nots](https://paulgraham.com/writes.html)<br>Budou kvůli AI lidi umět míň psát? A budou tím pádem i míň přemýšlet?
- [Why I Lost Faith in Kagi](https://d-shoot.net/kagi.html)<br>Aktualizovaný příspěvek o vyhledávači Kagi. Wow a lol.
- [(bez titulku)](https://dlmultimedia.esa.int/download/public/videos/2024/10/023/orig-2410_023_AR_EN.mp4)<br>Znáte takové ty krimi seriály, kde nějakého lupiče zachytí kamera na rohu a policejní tým je schopný rozkostičkovaný obraz 50x zazoomovat tak, aby viděli písmenka na knoflíku dotyčného? Vždycky jsem se u toho smál. No, tak ESA teď totéž udělala s vesmírem, akorát že jako fakt. A zazoomovala 500x.
- [Home - Database of Databases](https://dbdb.io/)<br>Databáze databází. Až na vás někdo vytáhne něco jako „my to hážem do DuckDB“, nemusíte jen nepřítomně mrkat a přemýšlet, jestli si dělá srandu, nebo fakt existuje nějaká kačeno-databáze 🦆 Můžete si to najít v databázi databází!
- [Things I’ve learned serving on the board of the Python Software Foundation](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/)<br>Super ochutnávka toho, jak vypadá zevnitř  a jak to tam funguje. Pro mně zajímavé čtení a srovnání s českým Pyvcem:
- [Big changes are coming to ArchiveBox!](https://docs.sweeting.me/s/archivebox-plugin-ecosystem-announcement)<br>Tohle vypadá zajímavě. Už nějakou dobu si leckterý online obsah raději stahuju offline, kdyby náhodou zmizel (např. přes yt-dlp). ArchiveBox je další level.
