Title: Týdenní poznámky: Oprava Lakatoše
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/340
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/113924915659185306

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-01-24_tydenni-poznamky-vanoce-a-velke-planovani.md) už utekl nějaký ten týden (24. 1. až 31. 1.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

Kdo neznáte opravu Lakatoše, nebo nevíte, že se to tak jmenuje, je to [tohle](https://www.youtube.com/watch?v=AAkwMlapkJs&pp=ygUQdHJha3RvciBsYWthdG_FoQ%3D%3D) a nakouskované do instantních hlášek to máte pro případ potřeby na adrese [milujipraci.cz](http://milujipraci.cz/).

## Oprava ~~Lakatoše~~ scraperu na pracovní inzeráty

Přestal mi fungovat scraper na pracovní inzeráty. Ne proto, že by nefungoval, ale protože je pomalý a Apify ho po čase restartuje. To není bug, ale [feature](https://docs.apify.com/academy/expert-scraping-with-apify/migrations-maintaining-state) té platformy. Jenže s tímhle se Scrapy nevyrovná. Restartovaný scraper začne odznova. Pokud je restartován těsně před koncem po hodině scrapování, začne znovu a trvá další hodinu. A takhle dokola. [Reportoval jsem to už dřív](https://github.com/apify/actor-templates/issues/303), ale teď mi to začalo dělat konzistentně.

Pingnul jsem Vláďu Duška z Apify, jestli je nějaká šance, že se na to podívají, jinak asi budu muset migrovat jinam, nebo nevím. Nakonec jsme se dohodli, že na tom zkusíme nějak po kouskách společně pracovat a rozlousknout to. Původně se mi do toho strašně nechtělo, ale takhle ve dvou přišla chuť. Měl jsem dodělávat svou práci na návodech pro Apify, což je můj vedlejšák, ale místo toho jsem pracoval na jejich open source, protože je zároveň používám jako zákazník 😅

Všechno šlo stranou a ponořili jsme se. Tušil jsem, že z práce na návodech, ani z jakékoliv jiné práce pro junior.guru tento týden asi sejde, ale že to bude tak špatné, to jsem nepředpokládal. Leželi jsme v tom oba vydatně, vždy tak nějak na střídačku, psali jsme si, sdíleli své objevy a já tedy dost sdílel i své chmury, protože na mě doléhala bezvýchodnost situace. Ujišťoval mě, že jsme udělali velký pokrok a máme za sebou hodně práce. Zkusím si to tu nějak sesumírovat:

- Rozumím teď Scrapy, Twisted, a asyncio asi o milion víc, než před pár dny. Dokonce jsem si psal i se Scrapy vývojáři.
- Dokázali jsme rozběhat v jednom Twisted reaktoru jak Scrapy spider, tak věci z Apify asyncio knihovny. Poskládali jsme to z tisíce a jednoho kousku informací, mezi nimiž byl např. i [tento článek](https://meejah.ca/blog/python3-twisted-and-asyncio).
- Našel jsem [bug v Apify SDK](https://github.com/apify/apify-sdk-python/pull/385).
- Udělal jsem [milion pokusů](https://github.com/juniorguru/plucker/pull/108), jak spouštět asyncio věci z útrob synchronního kódu a došel na to, že asi jedině ve vláknech.
- Zjistil jsem, že problémy vznikají při HTTP požadavcích přímo na platformě a postupně jsem izoloval, čím to přesně je. Nakonec jsem dokázal pomocí `APIFY_IS_AT_HOME=1` přesvědčit lokálně běžící Apify knihovnu, že si myslí, že je na platformě, a tím jsem problém zreprodukoval i lokálně. Díky tomu se pokusy dost zrychlily.
- Pokud se snažíme pouštět asynchronní kód ze synchronního pomocí vláken, narazíme na to, že knihovna HTTPX, nacházející se hluboko v útrobách Apify knihovny, vyhodí chyby. Nelíbí se jí, že asyncio loop z předešlého vlákna je už pryč. Je to proto, že dělá _connection pooling_ a [snaží se navázat na stream, který vznikl v jiném vlákně, v jiné asyncio loop](https://github.com/encode/httpx/discussions/2959).
- Klientská Apify knihovna je napsaná tak komplikovaně a tak nerozšiřitelně, že se mi ani po hodinách pokusů nepovedlo zařídit, aby vždy a ve všech vláknech a se všemi requesty HTTPX posílalo hlavičku „Connection: close“, což zamezí _connection poolingu_.

Během dneška mi ale bylo už jasné, že to ani po celém týdnu nerozlousknem. Strašně mě to štvalo a musel jsem se z toho vypsat do kanálu #past-vedle-pasti v junior.guru klubu a pak se projít venku, abych to nějak vyvětral z hlavy.

> Celý týden se snažím opravit scraper na nabídky práce. Apify platforma mi ho v půlce běhu restartuje, takže začne znova a pak timeoutuje, třeba protože běží už 2h. Ty restarty jsou údajně feature, ne bug. Takže mě napadlo, že udělám cache, aby se scraper mohl restartovat a pak pokračovat, kde byl. To celé vedlo k tomu, že řeším zamotané asyncio dohromady s Twisted, vlákna, function coloring, atd. Nakonec potřebuju jen to, aby knihovna httpx uvnitř Apify SDK posílala věci s „connection: close“, ale nejsem schopen toho kvůli extrémně komplikovanému OOP kódu nijak docílit. Past vedle pasti jak se patří. Celý týden jen něco debuguju, mám pocit bezmoci, bezvýchodnosti, a snažím se nasadit kolečko na čtvereček, bez výsledku. Jsem z toho akorát frustrovaný a smutný, o to víc, že potřebuji na junior.guru dělat úplně jiné věci, než opravovat scraper. Jdu se projít ven, ale myslím, že můj blbý pocit z celého týdne a smutek ze ztraceného času to nezachrání. Jo, i takové jsou někdy dny programátorů…

No ale nějak jsem se z toho po té procházce dostal. Postaral jsem se o malou a byla s ní sranda, tak to mě z toho nějak vytrhlo. Teď bude víkend, tak se pokusím soustředit na jiné věci. Pracovní inzeráty jsou stále tak trochu mimo provoz, všechna ostatní práce stojí, ale co nadělám.

![Lakatoš]({static}/images/lakatos.jpg)

## Kreslení

Pokračoval jsem o víkendu s testováním tabletu a s kreslením jsem celkem pokročil. Zkoušel jsem program Krita, ale pak jsem zjistil, [jak kreslit přímo v Inkscape](https://www.youtube.com/watch?v=ZoOg2CmbYBg), aby z toho vylezlo přímo SVG. Tím, jak jsem víc a víc kreslil, začínají kresby už trochu i stylem připomínat ty moje původní kresby na papír.

![Inkscape s tabletem]({static}/images/screenshot-2025-01-26-at-13-59-18.png)

## Automatické DPH, když jsem identifikovaná osoba

Aktuálně platím daňařovi, aby za mě řešil DPH z nákupů různých zahraničních služeb. Nejsem plátce daně, ale když nakoupím třeba Copilot nebo Simple Analytics, stávám se identifikovanou osobou a musím to pro tyto platby řešit. Je to pár korun měsíčně a asi to není těžké zprocesovat, ale sám to rozhodně dělat nechci, takže za to platím tomu daňařovi. Ten si bere několik set měsíčně za to, že se tím nemusím zabývat.

Jenže se těch pár set měsíčně nasbírá, a ty daně jsou tak malé, že mě napadlo, jestli by to nešlo dělat nějak levněji, automaticky. Napsal jsem Fakturoidu a odepsali toto:

> V Krabici můžete využít vytěžení dokladu - tzn. že se z dokumentu díky Digitoo AI vytvoří automaticky Náklad. Vždy je ale potřeba data zkontrolovat, např. zahraniční doklady bývají často nestandardní a AI s tím může mít potíž. Na tarifu Komplet (5.060 Kč ročně) nabízíme exporty pro státní správu. V praxi to pro vás znamená, že pokud služby ze zahraničí jen přijímáte, jednou za měsíc půjdete do Přehled > Exporty, kde si daňové přiznání k DPH stáhnete, nahrajete jej na portál mojedaně, kde se po odeslání dokumentu objeví částka k zaplacení i platební údaje.

To by bylo v součtu levnější řešení. Ale nebylo by to stoprocentní a stejně bych s tím musel něco dělat. Daňař mi teď pošle do mailu QR kód a já ho přejedu mobilem a to je celé. Takže asi spíš budu zkoušet vydělat víc peněz, než šetřit na dodavatelích a nahrazovat daňaře pomocí AI.

## Platba za „studenty“ v klubu

Při procesování sponzoringu od Prague Coding School jsem zjistil, že jsem špatně pochopil vlastní systém a že nemůžu docílit toho, co nabízím v ceníku 😀

V rámci tarifu je 15 lidí v klubu, další se měly dát přikupovat. Jsou to ale místa, ne konkrétní lidi, takže když někdo přijde o místo, je volné pro někoho jiného. Potud dobrý. Problém je, že jsem při psaní ceníku udělal mentální zkratku a nabídl, že lze přikupovat „lidi za měsíc“ a nacenil to 100 Kč/měs. Ale ono to je jinak, v mém systému lze přikupovat jen ona „místa“ a tato přikoupená trvají do konce předplatného, viz [dokumentace Memberful](https://memberful.com/help/member-interface/manage-group-subscriptions/#purchase-additional-member-seats).

Naštěstí PCS hned nepotřebuje místa přikupovat, takže si to můžu promyslet a ještě změnit a nic strašného se nestalo.

## Andew Sharp

V klubu někdo sdílel odkaz na sharpprogrammer.cz, což je nějaký borec, který srší rady a slibuje bombastické věci lidem, kteří se chtějí rekvalifikovat do IT. Rozjeli jsme nějaké srandičky, až jsem to musel trochu brzdit, abychom nesklouzli k lacinému vysmívání. Každopádně jsme s Lucií Tvrdíkovou, Vojtou Mádrem, Petrem Glaserem, a dalšíma otevřeli i diskuzi o tom, jak na tyhle věci efektivně upozorňovat a lidi varovat, čímž jsme se opět vrátili k věčnému tématu jak ověřovat kvalitu kurzů.

Založili jsme nakonec v klubu vlákno na marketingové bizáry a nesmysly provozovatelů kurzů. Když tomu neumíme zabránit, tak to můžeme aspoň sbírat a hořce se tomu smát. Ostrého Ondru jsme našli na LinkedIn a dal jsem mu follow, tak se těším, co tam na mě od něj vyskočí. Asi teď ale nemám morál na to, abych projížděl a komentoval jeho staré věci.

![Andrew Sharp]({static}/images/screenshot-2025-01-31-at-20-31-20-sharp-programmer-nejlepsi-resource-pro-uspech-v-it.png)

## Další

-   Koupili jsme letenky na dovolenou v dubnu. Juchů!
-   Kromě opravování traktoru jsem pro Apify na začátku týdne stihl ještě [vylepšit konfiguraci linteru](https://github.com/apify/apify-docs/pull/1430), udělat pár reviews a mrknout na [úpravy v tutoriálu Crawlee](https://github.com/apify/crawlee-python/pull/936#pullrequestreview-2574935045), který přímo souvisí s lekcí, kterou bych měl psát.
-   Doktorka: „Dělá to na mě dojem blokády hrudní páteře, která mohla vzniknout právě po tom prochladnutí při běhu v kombinaci s nastupujcí respirační infekcí.“ No každopádně než jsem si stihl shánět rehabilitaci, tak to začalo trochu ustupovat, takže uvidím, jak se to bude vyvíjet, a možná to zahojí hlavně čas.
-   Domluvil jsem na příští týden [Q&A v klubu s Leou Bradáčovou z Národní technické knihovny](https://junior.guru/events/49/). Pracoval jsem na domlouvání dalších dvou přednášek. Veronika Rychlá mi poslala draft textu pro stránku o angličtině do příručky, ale na to jsem se vůbec nestihl podívat.
-   Sešel jsem se s [Adamem Veseckým](https://www.linkedin.com/in/adam-vesecky/) a příjemně jsme pokecali. Možná se objeví v klubu.
-   Žena a dcera byly zase trochu nemocné. První rok ve školce, nekonečno nemocí.
-   Opravil jsem některé rozbité odkazy na webu, opět musela úřadovat [Wayback Machine](https://web.archive.org/).
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Vyřídil jsem tentokrát opravdu velké množství mailů, různých administrativních úkonů, a prošel skoro celý klub a na vše odpovídal. Byl jsem v kontaktu s Prague Coding School a Mews.
-   Za 8 dní jsem při procházkách nachodil 13 km. Celkem jsem se hýbal 4 h a zdolal při tom 13 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Zvládnout v úterý Q&A s Leou.
2.  Dořešit projekt Lakatoš.
3.  Dorazit lednové Apify návody. Možná můžu rovnou udělat i únorové…
4.  Udělat aspoň nejnutnější administrativu a odpovídání na junior.guru.

A pak odjet na dovolenou na hory. To jsem teda zvědavý, jestli bude vůle pevná a _time management_ zmenežovaný tak, abych v pátek napsal poznámky!

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Vodičkova – Wikipedie](https://cs.wikipedia.org/wiki/Vodi%C4%8Dkova)<br>TIL že pražská ulice Vodičkova se jmenuje, i přes dlouhý seznam slavných Vodičků, podle řezníka, který tam měl před stovkami let největší dům. Tolik asi k tomu, co dělat, pokud chcete své jméno zvěčnit navždy.
- [Once You're Laid Off, You'll Never Be the Same Again | Mert Bulan](https://mertbulan.com/2025/01/26/once-you-are-laid-off-you-will-never-be-the-same-again/)<br>„I’m not sharing all of this to brag but to highlight that, in the end, none of it mattered. On the day I announced I had been laid off, I received numerous messages from colleagues, even those I hadn’t worked with directly, telling me that I had inspired and motivated them. While those messages were heartwarming, they didn’t change the reality: to the company, I was just a row in an Excel sheet.“
- [Krajní pravice fašismus nepotřebuje |  | A2 – neklid na kulturní frontě](https://www.advojka.cz/archiv/2024/21/krajni-pravice-fasismus-nepotrebuje)<br>„Krajní pravice našla cestu, jak se bez revoluce obejít, tím, že kontaminovala liberální demokracii. Fašismus už není potřeba – je možné vytvářet xenofobní stát, zavírat hranice před migranty, a přitom čerpat peníze z Evropské unie, jak ukazuje Orbánovo Maďarsko.“
- [I Met Paul Graham Once - Phill MV](http://okayfail.com/2025/i-met-pg-once.html)<br>Doporučuju přečíst do konce, je tam zajímavý plot twist.
- [Are better models better? &mdash; Benedict Evans](https://www.ben-evans.com/benedictevans/2025/1/the-problem-with-better-models)<br>„If I need something that does have answers that can be definitely wrong in important ways, and where I’m not an expert in the subject, or don’t have all the underlying data memorised and would have to repeat all the work myself to check it, then today, I can’t use an LLM for that at all.“ „…we adopted a device that breaks if you drop it with a battery that lasts a day instead of a week, in exchange for something new that came with that.“
