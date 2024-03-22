Title: Týdenní poznámky: Nový příběh, oprava scraperů a nový návod
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-03-15_tydenni-poznamky-mycka-pribehy-a-schuzky.md) už utekl nějaký ten týden (15. 3. až 22. 3.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q1 2024]({filename}2024-01-25_plan-na-q1-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)
</div>

## Nový příběh

Minulý týden se mi povedlo publikovat dva nové příběhy na web.
V pondělí jsem jeden nasdílel na sociální sítě:

-   [Mastodon](https://mastodonczech.cz/@honzajavorek/112116162050186114),
-   [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7175432637157646336/),
-   a velké množství skupin na Facebooku.

Když už jsem byl po sto letech zase na Facebooku, procházel jsem si dotazy v [Programátoři začátečníci](https://www.facebook.com/groups/144621756262987/) nebo [IT jobs / Práce v IT](https://www.facebook.com/groups/1806114342948040/) a pokusil se tam na pár odpovědět.
Vzápětí mi do klubu přišlo pár lidí z Facebooku, tak bych měl tohle možná dělat častěji.

## Obsahová spolupráce

S [Vojtou Mádrem](https://www.programhrovani.cz/) jsme formou spousty písmenek v soukromých zprávách brainstormovali nad různými obsahovými projekty a možnostmi spolupráce.
Nic konkrétního z toho není, uspořádávali jsme si myšlenky a nápady.

Volal jsem si s [Lucií Lenértovou](https://www.youtube.com/@LucieLenertova/) a dohodli jsme se, že by zhruba od září mohla dělat nějaký obsah pro klub.
Ještě musíme doladit detaily spolupráce, ale už teď se na to těším.
Myslím, že to bude _win-win_.

## Oprava scraperů

V Apify opravili integraci se Scrapy.
Zjistil jsem, že mi scrapery stále nefungují, ale ne kvůli Apify, což byla příjemná změna.

Jeden scraper jsem opravil relativně rychle, ale druhý mi dal dost zabrat.
Stahuje nabídky práce na LI, a LI se urputně brání, abych to dělal (jsou to [veřejná data na jejich webu, nic za loginem](https://nubela.co/blog/is-linkedin-scraping-legal/)).

To mě přivedlo k myšlence, že můj život je možná příliš krátký na to, abych s LI hrál hru na kočku a myš, a začal jsem hledat hotové řešení.
První cesta vedla do _Apify store_, ale:

-   [$16/měsíc + provoz](https://console.apify.com/actors/8swo47WpOkyzxtvAR/information/),
-   [$25/měsíc + provoz](https://console.apify.com/actors/gdbRh93zn42kBYDyS/information),
-   nebo dokonce [$30/měsíc + provoz](https://console.apify.com/actors/BHzefUZlZRKWxkTck/information/),

mi zatím přišlo jako velké náklady na to, že jsou nabídky práce na junior.guru spíš doplňkovou službou, která přímo nic nevydělává.
I když ten za $16, ten by možná ještě šel…

Z výběru jsem vyřadil scrapery, které vyžadují zadání mých cookies.
Svoje cookies nikomu nedám a i když si na LI vytvořím _fake_ profil, bojím se, že sice hodím peníze na problém scrapování, ale vyměním ho akorát za problém vytváření nových a nových účtů po tom, co mi je LI zabanuje.
Chci, aby scraper využíval veřejná data, která jsou vidět anonymně, nebo aby na sebe vzal problematiku účtů.

Hledáním jsem narazil na [py-linkedin-jobs-scraper](https://github.com/spinlud/py-linkedin-jobs-scraper), ale to bych stejně musel provozovat.
Pak jsem našel nějaký [Scrapingdog](https://www.scrapingdog.com/linkedin-jobs-api), dokonce i s [návodem](https://www.scrapingdog.com/blog/scrape-linkedin-jobs/), který v podstatě popisuje přesně to, co sám dělám.
Ale jsou na mě moc drazí.
Další podobný návod jsem našel na [scraperapi](https://www.scraperapi.com/blog/how-to-build-a-linkedin-scraper/).

Pak jsem našel [proxycurl](https://nubela.co/proxycurl/), které vypadá dost zajímavě.
Mají pouze data, která jsou veřejná, [kešují to](https://nubela.co/blog/how-fresh-are-profiles-returned-by-proxycurl-api/), umí i [vyhledávat](https://nubela.co/proxycurl/docs#search-api-job-search-endpoint), mají API, a mají [_pay-as-you-go_ od $10](https://nubela.co/proxycurl/pricing).
Taky mají v rámci API i nějaké _free endpointy_, např. na [obrázek člověka](https://nubela.co/proxycurl/docs#people-api-person-profile-picture-endpoint) nebo [logo firmy](https://nubela.co/proxycurl/docs#company-api-company-profile-picture-endpoint).
Vyzkoušel jsem to a hned mi napsali, jestli se mi to líbí, tak jsem jim napsal feedback.
Rozhodně na mě udělali dobrý dojem, ale:

-   Kešované profily lidí mi bohužel neřeší jednu věc do budoucna, co plánuji,
-   vyhledávání inzerátů by mohlo být náhradou za scraper, ale vracelo mi to trochu jiné výsledky. Musím to ještě vyzkoušet a nějak se rozhodnout.

Nakonec jsem to ale nějak opravil, ten scraper, který už mám.
Takže vzápětí motivace dotáhnout to a zjistit, jestli by ho proxycurl mohlo nahradit, klesla na nulu.
Až se to zase rozbije, tak tu myšlenku oživím.

## Nový návod

Velkou část týdne jsem psal příručku.
Konečně!

Zpracoval jsem všechny poznámky, které jsem měl k [úvodní stránce příručky](https://junior.guru/handbook/), a trochu jsem ji ještě upravil.
Nově jsem tam naznačil možné záseky, které mohou juniory na cestě potkat.
Snad to teď ale nebude moc _doom & gloom_ a všechny to neodradí 😅

Ještě jsem sepsal důvody, proč příručku píšu, a hodnoty, na kterých je postavená, ale nakonec mi přišlo, že se to na tu úvodní stránku nehodí.
Bylo mi líto to smazat, tak jsem to zatím [nacpal do FAQ](https://junior.guru/faq/), a časem vymyslím, kam to zapadne.

No a pak jsem konečně přidal novou stránku do příručky, na nové téma, s novým návodem!
Mám z toho ohromnou radost.
Tady to je: [Jak si vyladit profil na GitHubu](https://junior.guru/handbook/github-profile/)
Snažil jsem se vyhrát si s tím a hlavně mnohem víc než dřív využívat obrázky.
Budu rád za zpětnou vazbu!

Samozřejmě mě svrbí prsty, chtělo by to hned přespat i kapitoly o Gitu, o projektech, a tak dál, ale holt nejde udělat vše najednou.

![Nová kapitola v příručce]({static}/images/screenshot-2024-03-22-at-20-43-37-jak-si-vyladit-profil-na-githubu.png){: .img-thumbnail }

## Další

-   Byl jsem po dlouhé době na [Pyvu](https://pyvo.cz/praha-pyvo/).
    Přijel [Tatanka](https://junior.guru/podcast/5/) a vzal jsem s sebou kamarádku [Domi](https://domicanhelp.cz/).
    Překvapilo mě, že přišlo dost lidí, které znám ze starých predcovidových časů.
    Dokonce se hrálo na ukulele!
    Akci jsem si moc užil, i díky nové strategii, kdy si dám nějaké to pivo, ale potom pokračuji nealkoholickými.
    Nezabránilo mi to přijít domu o půl třetí ráno po tom, co jsme „pomáhali“ Tatankovi čekat na ranní vlak domů, ale ničeho nelituju.
-   Zašli jsme na [Den Vltavy](https://denvltavy.vsevltavskyspolek.cz/) a bylo to fajn.
    Vyšlo nám krásné počasí.
-   Byl jsem na obědě s kamarádem, v sauně, udělal jsem si procházku po Praze, byl jsem u holiče.
    Byl jsem na schůzce v Apify.
-   Nepovedlo se mi po upgradu pycordu vyřešit `ERROR: Unclosed client session`, tak jsem to nechal být a pouze na to [založil issue](https://github.com/Pycord-Development/pycord/issues/2399).
-   Zjistil jsem, že na Memberful od začátku špatně pracuji s kupóny.
    Když někomu dám roční kupón se 100% slevou, za určitých podmínek jsem mu tím dal omylem dva roky zdarma.
    Nejspíš se mi to stalo u velkého množství lidí 🤦‍♂️
-   Známý mě odchytl na Pyvu a prý že shánějí juniora.
    Tak kdo umíte trochu Excel a chcete automatizovat, ideálně ještě pokud se třeba rekvalifikujete z účetnictví, [mrkněte na to](https://www.jobs.cz/fp/asb-czech-republic-s-r-o-233975/2000176507/?searchId=5b2e93b9-305a-443a-87dd-e647bfdf8e7c&rps=329).
-   Už se plánuje další [Týden pro Digitální Česko]({filename}2023-11-27_tyden-pro-digitalni-cesko-z-pohledu-partnera.md).
    Prošvihl jsem call s Bartošem, ale pozvánku na Slack, který zřídili, jsem si vyzvedl.
-   Začal mi padat skript, který si stahuje nějaké statistiky.
    Používá se to jen na vykreslení pár grafů.
    Zatím nevím, jestli to bude permanentní problém, a budu to muset nějak řešit, nebo jen dočasný výpadek na druhé straně, ale znamená to, že mi neprojde build.
    A to v pátek znamenalo, že nemůžu publikovat novou kapitolu o GitHub profilu a pochlubit se s ní světu!
    Takže jsem narychlo splácal způsob, jak build může obejít chybu, nareportovat mi ji na Discord, a místo grafů na webu napsat, že chybí data a dočasně je to rozbité.
    Takový mechanismus by se mi do budoucna určitě hodil na spoustu dalších věcí, ale asi ho budu implementovat až když zase někde něco spadne.
-   Redis [změnil licenci](https://redict.io/posts/2024-03-22-redict-is-an-independent-fork/) a Bo Bayles, který ode mně kdysi převzal [redis-collections](https://github.com/redis-collections/redis-collections/), mi napsal, jestli to nezavřem.
    Zavřem.
    Ani jeden už to stejně nepoužíváme.
    Tím skončí jedna z nejmilejších věcí, která se mi v rámci open source stala.
    Ty redis-collections jsou jeden z prvních vážně míněných projektů, který jsem kdysi dal na GitHub.
    Když jsem to přestal rozvíjet, ozval se mi Bo, náhodný člověk z druhého konce planety, že by to převzal.
    Důvěřoval jsem mu a mnoho let se o knihovnu staral a rozvíjel ji.
    Vždy mi to přišlo jako milý příběh úspěšné spolupráce lidí různě po světě, pro dobro světa.
    Takové to, co v tom open source asi všichni tak nějak hledáme, a proč to děláme.
-   Někdo mě pozval jako hosta do kanálu v jejich Slacku.
    Musím říct, že nic tak strašného, jako proces, kterým jsem se tam snažil dostat, jsem už dlouho nezažil.
    Protože jsem si kanál nechtěl přidat do Czechitas, Pyvce, ani jiného svého existujícího Slacku, vytvořilo mi to nový workspace, který se jmenoval „Honzajavorek“ a já jsem se v něm jmenoval „mail“.
    Pak mi to ale napsalo, že pozvánku mám stejně na jiný e-mail a nemohu ji vyzvednout.
    A nakonec mi to napsalo, že tuhle pozvánku mohu vyzvednout jen v rámci placeného workspace.
    Druhá strana mě musela pozvat znovu a nakonec jsem si to stejně musel vlepit do Pyvec Slacku, i když jsem to tam nechtěl (je Pro a chodím tam nejčastěji) 🤯 No, zase se mi ověřilo, že Slack už pro mně není.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Po tomto týdnu mám v e-mailu asi jen 10 nedořešených zpráv, juch.
-   Za 8 dní jsem při procházkách nachodil 20 km. Celkem jsem se hýbal 7 h a zdolal při tom 20 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Rozhodnu co s barterem (viz minulé poznámky).
2.  Pustím se do něčeho, o čem tady napíšu za týden.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [A month of the Vision Pro — Benedict Evans](https://www.ben-evans.com/benedictevans/2024/3/17/a-month-of-the-vision-pro)<br>„What will we do with VR? The metaverse! What is the metaverse? What we do with VR!“
- [Pokud si koupíte do města hummera, jste idiot. Radním na okraji Melbourne došla trpělivost s velkými vozy - Zdopravy.cz](https://zdopravy.cz/pokud-si-koupite-do-mesta-hummera-jste-idiot-radnim-na-okraji-melbourne-dosla-trpelivost-s-velkymi-vozy-198540/)<br>lol 😀 jako tohle by se v Praze hodilo taky, že…
- [Jak dostat lidi z D1 do vlaků. Průzkum zjišťoval, proč někdo preferuje auto a zda to změní VRT - Zdopravy.cz](https://zdopravy.cz/jak-dostat-lidi-z-d1-do-vlaku-pruzkum-zjistoval-proc-nekdo-preferuje-auto-a-zda-to-zmeni-vrt-198327/)<br>„Třetina lidí na D1 sedí v autě sama, což je pro srovnání lepší číslo než ve městech, kde bývá průměrná obsazenost vozu jen 1,2 člověka.“
- [Marie Heřmanov&aacute; - TikTok je hlavně interaktivn&iacute; televize, efekt soci&aacute;ln&iacute;ch bublin na s&iacute;t&iacute;ch se přeceňuje &mdash; Kolaps &mdash; Overcast](https://share.transistor.fm/s/e1244489)<br>Marie Heřmanová opět skvělá. Skoro bych si nainstaloval TikTok.
