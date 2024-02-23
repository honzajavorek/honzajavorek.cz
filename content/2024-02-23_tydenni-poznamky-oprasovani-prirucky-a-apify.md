Title: Týdenní poznámky: Oprašování příručky a Apify
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/310
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111982959441050356

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-02-16_tydenni-poznamky-vic-inzeratu-a-mene-duvery-v-platformy.md) už utekl nějaký ten týden (16. 2. až 23. 2.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q1 2024]({filename}2024-01-25_plan-na-q1-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)
</div>

Mám zase nějakou rýmu, ale nebudu propadat beznaději!

## Oprašování příručky

Prošel jsem si všechny poznámky, které jsem u příručky měl v souvislosti s učením angličtiny.
Pak jsem vzal dvě sekce, které jsem už v příručce měl, a přesunul je na [samostatnou stránku o angličtině](https://junior.guru/handbook/english/).
Poznámky a tuto stránku jsem pak předal [Veronice](https://geekpower.cz/), aby tam mohla připravit vlastní obsah po vzoru [Nely](https://junior.guru/handbook/mental-health/).

![Angličtina]({static}/images/screenshot-2024-02-23-at-21-50-16-anglictina-pro-programatory.png){: .img-thumbnail }

Pak když jsem měl jít konečně psát novou verzi [stránky o Gitu a GitHubu](https://junior.guru/handbook/git/), tak jsem se zakoukal do kódu, nějak neodolal, a šel jsem předělat úvodní stránku příručky.
Měl jsem dost jasnou představu, jak by to mělo vypadat, a přišlo mi, že to bude za chvilku hotové.
No, takže to není hotové doteď, klasika 😀

Na [úvodní stránce](https://junior.guru/handbook/) byla cesta juniora, ale bylo to tam naplácané v obyčejném seznamu, nepřehledně, a odkazy dovnitř příručky tam byly vepsané prostě ručně.
Chtěl jsem, aby to bylo hezčí a aby se to automaticky generovalo.
Přidal jsem tedy YAML, kam jsem si sepsal jednotlivé fáze, dal jim ikonky, a tak.
Do každé stránky příručky jsem pak přidal informaci, do jaké fáze spadá.
To jsem následně načetl do databáze a propojil, což mi zabralo víc času, než jsem chtěl, protože jsem pořád zakopával o nějaké nástrahy.

Aktuálně je tedy na té úvodní stránce prozatimní verze, kdy se seznam už vypisuje z databáze a vše je propojené, ale zdaleka to nevypadá tak, jak bych chtěl, aby to vypadalo.

![úvodní stránka]({static}/images/screenshot-2024-02-23-at-21-48-50-prirucka-pro-juniory.png){: .img-thumbnail }

## Apify

Tento týden je ve znamení Apify:

-   V pondělí jsem byl v kancelářích Apify na schůzce, o jejímž obsahu zatím pomlčím.
    Něco domlouváme, ale není to zatím kompletně domluveno.
-   V úterý jsem si hodinu volal s produkťáky z Apify.
    Na Apify Discordu se totiž objevila výzva, že dělají nějaký UX průzkum a kdo se přihlásí, může dostat nějaké kredity zadáčo.
    To mi přišlo jako _win-win_.
    Někdo bude hodinu poslouchat, jak ten produkt používám, čímž jeho vývoj mohu přiklonit k tomu, co potřebuju, a ještě tím ušetřím.
    A tak se i stalo.
    Pokec to byl příjemný a dle jejich názoru prý i užitečný.
-   S [Vláďou](https://github.com/vdusek) jsme řešili bug v integraci se Scrapy.
    Povedlo se mu to opravit, ale pak jsme objevili ještě něco dalšího.
-   Zítra je [Python Pizza](https://prague.python.pizza/).
    Koná se v kancelářích Apify 😀

Když jsem měl chvilku a prokrastinoval jsem důležitější věci, připsal jsem si skript, který umí založit nový scraper na Apify přes jejich API.
Tím se opět zkrátilo [README](https://github.com/juniorguru/plucker?tab=readme-ov-file#how-to-add-new-scraper), které popisuje kroky nutné k tomu, aby v repozitáři vznikl nový scraper.
Skript ještě [není úplně takový, jak bych chtěl](https://github.com/juniorguru/plucker/issues/20), ale vypadá to, že funguje, což je fajn.

## Úpravy na nabídkách práce

-   Vyčistil jsem určitou historickou nesrovnalost ohledně toho, jak se v datech zapisuje datum, kdy byla nabídka práce publikována.
-   Smazal jsem složku `jobs_legacy`, což je malý krok pro lidstvo, ale obrovský milník pro junior.guru 😤
-   Do filtrů nabídek práce jsem přidal jeden, který vyhodí příliš staré nabídky.
    Je možné, že se tam nějaké zatoulaly a pak by byly jednak matoucí, jednak by mi zbytečně žraly OpenAI tokeny.
-   Timeoutuje mi jeden ze scraperů, ale nějak jsem to nestihl opravit.

## Výběr přednášek

Uzavřel jsem si pro sebe hlasování v klubu.
Výsledky jsem si vynesl do Google Sheets tabulky a seřadil si to podle počtu hlasů.
Plánuji zhruba na rok dopředu, takže chci zhruba 12 přednášek.
Vybral jsem 6 nejpopulárnějších témat a na ty budu hledat přednášející a termíny.
Dalších 6 jsem vybral sám z toho zbytku, částečně podle hlasů, ale i podle toho, co si myslím, že je zajímavé i přesto, že to není populární.
Např. lidé, kteří ještě ani nemají svou první práci, netuší, že budou v té první práci potřebovat tušit o existenci Jiry nebo SCRUMu, a tedy pro to logicky nebudou hlasovat.

Tím jsem si odkroutil něco, co jsem dlouho prokrastinoval.
Teď už „jen“ sehnat přednášející a domluvit všechny termíny.

## Budoucnost přednášek

Je tu ale jeden _elephant in the room_, a tím je otázka: Proč to, Honzo, vlastně vůbec děláš?
Máš to vůbec dělat?
Jaká je hodnota přednášek?
Jaké je ROI vynaložené energie?

### Mínusy

-   Často tuto práci prokrastinuju.
    A když ji týdny nebo měsíce prokrastinuju, nikdo si nestěžuje, že přednášky v klubu nejsou.
-   Nepřijde mi, že bych potkal jediného člověka, který by řekl, že do klubu zamířil a zůstal v něm kvůli přednáškám.
-   Je to obsah a já si myslím, že junior.guru má být komunita, platforma, rozcestník a agregátor, ale nemá vytvářet vlastní obsah nad rámec příručky.
    Neškáluje to.
    Pája dělá podcast, ale kdyby ho nedělala ona, tak já ho dělat nemám a prostě by neexistoval.
    Je možné vzít obsahový projekt pod značku junior.guru, ale já sám bych to vytvářet neměl.
-   Obsahu je plno.
    Je spousta šikovných youtuberů ([Lucie](https://www.youtube.com/@LucieLenertova), [yablko](https://www.youtube.com/channel/UC01guyOZpf40pUopBvdPwsg)…), kteří video udělají zajímavěji a lépe.
    Je spousta konferencí, kde jsou přesně takové přednášky jako v klubu, a mají pak videa na YouTube.
    Někdo dělá šikovně Instagram ([Markéta](https://www.marketawillis.com/)).
    Někdo dělá šikovně podcasty (namátkou [Šárka a Vojta](https://www.programhrovani.cz/), [Jakub a Gabo](https://streetofcode.sk/)).
    Jaká je přidaná hodnota přednášek a záznamů přednášek v klubu?
    Jestli je junior.guru spíš komunita, platforma, rozcestník a agregátor, tak by spíš mělo pomoci dostat se k existujícímu kvalitnímu obsahu, utřídit ho a vypíchnout to nejlepší - protože tam leží přidaná hodnota junior.guru - ne do té hromady ještě přidávat svoje.
-   Dost podobné webináře nebo _live streamy_ teď pravidelně pořádají [Programátoři začátečníci](https://www.programatorizacatecnici.cz/) nebo [Nauč mě IT](https://naucme.it/).
    Stává se to komoditou, která mě ale stojí dost přemáhání, času a práce.

### Plusy

-   Přednášky přivádí do klubu zajímavé lidi, což občas (pokud tam zavítají i mimo přednášku) obohacuje klub.
-   Přednášky jsou česky a jsou tematicky laděné pro úplné začátečníky, a to nebývá zas tak běžné ani v té záplavě po covidu oživlých konferencí a YouTube videí.
-   Přednášející jsou v klubu a členové s nimi mohou interagovat, ptát se dotazy, atd.

### Co s tím?

Nevím.
Aktuálně zachovám _status quo_.
Do budoucna ale cítím, že to bude chtít nějaké změny.
Buď přednášky komplet deleguju, zruším, nebo změním formát.

## Jak to jde s plány?

Pojďme si připomenout, [co jsem plánoval na první čtvrtletí]({filename}2024-01-25_plan-na-q1-2024.md), protože už je konec února.
To to letí!

-   ~~Programovat a psát, nerozptylovat se akcemi a spolupracemi.~~ Toto se mi, myslím, daří. Nějaké věci jsem odmítl.
-   ~~Soustředit se na problémy lidí, kterým chci pomáhat, ne na svoje problémy.~~ Dělám co umím 😅
-   ~~Přestat aktivně hledat produkt pro firmy.~~ Načrtl jsem si nový ceník, ve kterém bude velké prd, a pak to nechal zapadnout někde v Trellu, takže dobrý.
-   ~~Vytvořím nebo aspoň vymyslím MVP profilů kandidátů~~ Mám jasnou představu, co je potřeba udělat a vymýšlením té představy jsem strávil docela dost času, povídal jsem si o tom s Milkem, a udělal jsem i jeden malý PoC.
-   Dopíšu kapitoly v příručce: LinkedIn, Git, GitHub 👀
-   ~~Přesunu scrapery pracovních inzerátů na Apify a začnu je třídit přes LLM~~ Hotovo 😤
-   Vydám další _success stories_ na web 👀
-   ~~Automatizace v klubu (povídání, týdenní plány…)~~ Hotovo 😤
-   ~~Vyberu a~~ domluvím ~~klubové přednášky na rok 2024~~ 👀 😅

No, nepřijde mi to špatný!
Ještě mám celý březen.
To bych mohl docela hezky postíhat.
Mám z toho radost.
Přitom stačilo dát si realistické cíle, být aspoň chvíli aspoň trochu zdravý, a nenechat se rozptylovat od toho, co je podstatné 💪

## Další

-   Díky [Tvůrcast](http://tvurcast.cz) komunitě jsem zjistil, že s podcastem nemáme vůbec špatná čísla, minimálně na Spotify.
    Já je vůbec nesleduju a hlavně nemám srovnání.
    Teď vím, že máme 25.000 starts, 18.500 streams, 3.000 listeners, 1.200 followers, 15.500 impressions.
    A to jsme ještě i na YouTube, Apple Podcasts, a spousta lidí si nás (nejspíš?) pouští i [přímo na webu](https://junior.guru/podcast/), kde nemám žádné sledování, to jsou jen `<audio>` tagy s audio souborem.
    Na to, že je to Pájino hobby a už ani nedodržujeme jednu epizodu měsíčně, je to podle mě docela dobrý 😀
-   Prošel jsem [moudra](https://junior.guru/wisdom/) a trochu je uhladil, případně něco smazal, a tak.
-   Domluvil jsem termín, kdy poskytnu jednorázovou placenou konzultaci na vedení komunity.
    Těším se na to.
-   Spadl mi build na junior.guru, protože GraphQL API od Memberful ze dne na den zase něco změnilo.
    Nakonec mi poradili, že můžu přidat nějaký parametr a bude to zase fungovat.
    Pozitivní je, že jsem to mohl hned opravit a funguje to.
    Smutné je, že to je zjevně bug na jejich straně, ale nepřišlo mi, že by je to nějak moc trápilo.
-   Zatím jsem moc nepokročil s přesunem pryč z Gmailu.
    Naopak, vzdal jsem používání Apple Mail a jsem zpátky i v tom webovém rozhraní.
    Až se budu zase nudit, tak zas něco vyzkouším, ale teď mám asi lepší věci na práci.
-   Propagoval jsem PyCon NA [na LinkedIn](https://www.linkedin.com/posts/honzajavorek_community-thankyou-python-activity-7165238625528463360-pf_O) a [na Mastodonu](https://mastodonczech.cz/@honzajavorek/111957344665919060).
-   Ze Smitio mě poprosili, ať nasdílím [průzkum ohledně mezd v IT](https://www.survio.com/survey/d/L0Y9W0D9D8B5N2J7J), zatím jsem to udělal v klubu.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 8 dní jsem při procházkách nachodil 5 km. Celkem jsem se hýbal 4 h a zdolal při tom 5 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Dodělám novou úvodní stránku příručky.
2.  Přepíšu [stránku o Gitu a GitHubu](https://junior.guru/handbook/git/).
3.  Užiju si [Python Pizza](https://prague.python.pizza/) jako pouhý návštěvník! A potom i večerní junior.guru srazík.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [25 top freelancerů: o AI (3. díl rozhovoru) | Otto Bohuš](https://ottobohus.cz/25-top-3-dil-ai)<br>„Ve vztahu ke své vlastní práci jsem aha efekt nezažil. Při psaní pracuji především s humorem, češtinou a fakty – a zrovna tohle jsou tři věci, v nichž AI dosud nevyniká.“ Tohle máme se Ziburou stejně. I to Dřímalkovo rezonuje: „FOMO z toho, že kolem nás vzniká ještě víc příležitostí, než kdy jindy a že je nebudu schopen využít. Možná ale trochu i obava z toho, jestli se svět nezmění až moc. Třeba tak, že se mi to nebude líbit.“ A Bohdana Goliášová taky super!
- [Konec lyžování v Česku. Jde o první skutečnou klimatickou ránu pro náš národ?](https://a2larm.cz/2024/02/konec-lyzovani-v-cesku-jde-o-prvni-skutecnou-klimatickou-ranu-pro-nas-narod/)<br>Zmizí lyžování?
- [Multi-layered calendars](https://julian.digital/2023/07/06/multi-layered-calendars/)<br>Zajímavý pohled na kalendář.
- [Markwhen | Markwhen](https://markwhen.com/)<br>Markdown a čas. Může se hodit.
- [The killer app of Gemini Pro 1.5 is video](https://simonwillison.net/2024/Feb/21/gemini-pro-video/)<br>„The ability to analyze video like this feels SO powerful. Being able to take a 20 second video of a bookshelf and get back a JSON array of those books is just the first thing I thought to try.“
- [Air Canada must honor refund policy invented by airline’s chatbot](https://arstechnica.com/tech-policy/2024/02/air-canada-must-honor-refund-policy-invented-by-airlines-chatbot/)<br>„It should be obvious to Air Canada that it is responsible for all the information on its website. It makes no difference whether the information comes from a static page or a chatbot.“ „Air Canada’s initial investment in customer service AI technology was much higher than the cost of continuing to pay workers to handle simple queries.“
- [Alternative search engines](https://www.simpleanalytics.com/blog/alternative-search-engines)<br>„Google Search is a very good search engine. In fact, it is arguably the only good product Google developed in-house. And yet, googling information is more frustrating than ever, because Google Search has some big problems.“
- [Průmyslová revoluce naopak](https://www.mimoagendu.cz/prumyslova-revoluce-naopak/)<br>„Nejnebezpečnější pro média bude tahle doba otřesů, kdy vlastně nikdo netuší, jakým směrem se dějiny rozběhnou. Jestli jde něco novinářům hodně špatně, tak je to reagování na změny. Doteď nevyřešili internet a synergii mezi servery a papírem. Krátká videa na Instagramu a TikToku jsou pro nás stále ještě okrajovou záležitostí, i když influenceři a marketingové firmy je dávno adoptovali jako vlajkovou loď svého obsahu.“
