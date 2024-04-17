Title: Týdenní poznámky: Automatická zpětná vazba na GitHub profil a opravy scraperů
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/317
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/112286492533616477

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-04-06_tydenni-poznamky-vedlejsak-v-apify-a-velikonoce.md) už utekl nějaký ten týden (6. 4. až 17. 4.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
</div>

Velkou část období, za které píšu tyto poznámky, jsem byl doma sám, anžto zbytek rodiny jel k babičce.
Díky tomu jsem stihl spoustu běhání, chození do kina, apod.
Bylo příjemné si odpočinout, ale teď už frčím vlakem za nimi.

## Automatická zpětná vazba na GitHub profil

Tak jsem to vyrobil.
Vypadá to nějak takhle: [Mastodon](https://mastodonczech.cz/@honzajavorek/112254288049055908), [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7184275571894317057/).
V klubu je kanál #cv-github-linkedin, kde už dřív lidi koukali na CV a poskytovali tam zpětnou vazbu.
Když tam teď někdo založí vlákno s odkazem na GitHub profil, ujme se toho bot, automaticky projede nějaká pravidla, a do vlákna vypíše výsledek.

Měl jsem vymyšlené, že to bude žít v repozitáři [hen](https://github.com/juniorguru/hen) jako samostatný nástroj, a že to bude celé v [asyncio](https://docs.python.org/3/library/asyncio.html) a bude to používat [pubsub](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) v podobě [blinker](https://github.com/pallets-eco/blinker/)u.
Přišlo mi, že taková architektura bude dost rychlá, asynchronicita se bude dobře snoubit s Discordem, a do budoucna to bude díky tomu pubsub dostatečně flexibilní.
Časem bych chtěl, aby mohl kdokoliv přispívat novými pravidly, takže je pro mě důležité oddělit kód samotných pravidel od jádra, které získává data.
Aby VS Code hezky napovídalo, používám všude typování, naučil jsem se používat dataclasses, TypedDict, apod.

Nejdřív jsem si udělal rešerši knihoven na GitHub.
Požadavek na asyncio hned několik z nich vyřadilo.
Zvažoval jsem nakonec [gidgethub](https://github.com/gidgethub/gidgethub) a [githubkit](https://github.com/yanyongyu/githubkit), vybral jsem githubkit.
Jako HTTP knihovnu začínám všude používat [httpx](https://github.com/encode/httpx) a jako nejnovější objev mám [hishel](https://github.com/karpetrosyan/hishel), HTTP keš.

Každé pravidlo má dokumentaci v podobě odkazu na odstavec v návodu v příručce, takže když si chce někdo zjistit kontext celé věci, klikne, a dostane se do příručky na kompletní návod, kde je i nějaká ta omáčka.
Kvůli tomu [nemám ještě hotová nějaká pravidla](https://github.com/juniorguru/hen/issues), ač by bylo snadné je naprogramovat, protože holt nemají ještě svůj popis v příručce.

Nejzajímavější je asi pravidlo na kontrolu GitHub obrázku, které analyzuje jeho barvy.
Díky tomuto pravidlu jsem zjistil, jak správně s `httpx` a `pillow` stahovat obrázky, takže jsem si mohl opravit [chybu ve film2trello](https://github.com/honzajavorek/film2trello/issues/136#issuecomment-2045476698).

Počistil jsem při této příležitosti [balíček s realtime botem](https://github.com/juniorguru/chick), kde se zatím zpětná vazba spouští.
Udělal jsem nějaký refactoring, opravy, přidal [ruff](https://github.com/astral-sh/ruff), apod.
Chtěl jsem mít co nejrychleji prototyp, který mohou lidi zkoušet, takže jsem ani neměl ještě všechny pravidla, a už jsem tlačil na integraci s Discordem.

Potom už jsem jen dolaďoval věci podle zpětné vazby od lidí a užíval si nadšení, které jsem prožíval já a zjevně i všichni, kdo to vyzkoušeli.
Například jsem přidal možnost spouštět _review_ opakovaně v rámci jednoho vlákna, naučil bota detekovat i odkaz na LinkedIn nebo vložené PDF s CV a dolaďoval jsem zprávy, které bot posílá.
Taky jsem vylepšoval dokumentaci repozitáře.
Ještě musím dopsat testy, ale to jsem nevěděl jak dobře udělat, tak jsem se nejdřív [zeptal autora githubkitu](https://github.com/yanyongyu/githubkit/issues/98).

Už dlouho něco v klubu neudělalo takové vlny a já mám ohromnou radost, protože jsem zjevně vyrobil něco fakt užitečného.
A to je přitom teprve začátek!

## Opravy

-   Zmigroval jsem jeden ze skriptů na nové [Fakturoidí API v3](https://www.fakturoid.cz/api/v3) (o jednu Apiary dokumentaci na světě méně, zamáčkněme slzu).
    Protože se s nimi znám, poslal jsem jim zpětnou vazbu na to, jak se mi s API pracovalo.
-   Opravil jsem stahování CSV z Memberful.
    [Něco tam vylepšovali](https://memberful.com/help/metrics-and-analytics/export-data/), takže mi to rozbili.
    Zabralo pár hodin, než jsem to zase rozběhl.
    Díky tomu mám opět data s odpověďmi od lidí, např. kde objevili junior.guru, nebo proč odcházejí z klubu.
-   Opravil jsem jeden detail v jednom ze scraperů, které stahují pracovní inzeráty.
-   Vrtal jsem se zase i ve scraperu, který inzeráty stahuje z LI.
    Opět nefunguje.
    Tak jsem zkusil vytáhnout těžký kalibr: [scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright).
    V Apify si jistě všimli, že na něčem dělám, protože jsem se neubránil a [založil jedno issue](https://github.com/apify/actor-templates/issues/274), přidal [4 komentáře sem](https://github.com/apify/actor-templates/issues/252#issuecomment-2056265976), a založil jedno support vlákno na jejich Discordu.
    Objevil jsem taky zajímavou knihovnu `fake-useragent`, ale [to si nechám na příště](https://github.com/juniorguru/plucker/issues/37).

## Chickenbook

Měli jsme v neděli večer tříhodinový hovor s tvůrci projektu [Chickenbook](https://github.com/jg-chickenbook/) (ještě před pár dny fungovalo i [chickenbook.pythonanywhere.com](https://chickenbook.pythonanywhere.com/), ale asi to předělávají).

V rámci _challenge_ v klubu začala po vlastní ose skupinka juniorů vytvářet aplikaci na profily juniorů.
Pustili se do toho s vervou, nadšením a očekáváním, že by tento projekt mohl pomoci junior.guru a později se do něj zaintegrovat.

Přijde mi úplně úžasné, co vytvořili a moc si toho vážím.
Měl bych to určitě zpropagovat na sítích a vynést je do nebes, ať jim to pomůže i na trhu a udělá trochu jméno.

Co se ale týče Chickenbooku a junior.guru, tak tam bojuju s tím, že bych sice chtěl, aby lidi mohli mít na junior.guru profily, ale mám to vymyšlené z jiné strany a používám jiné technologie.
Také není jasné, kdo to bude provozovat, nebo tam opravovat v příštích letech chyby.

Na hovoru jsme si vysvětlovali, jak to kdo má, co od toho čeká, jaké jsou možnosti.
Shodli jsme se, že Chickenbook by měl junior.guru spíš doplňovat, stát se součástí jeho širšího vesmíru, nebo se nějak vymezit, a najít si své vlastní místo.

## Video?

Přemýšlel jsem hned s několika lidmi, zda bych nezkusil natáčet krátká videa.
Přijde mi, že by mi to mohlo zabrat méně času, než se přemáhat psát statusy na LinkedIn apod.
Navíc taková videa lze pak nahrát na YouTube, na LinkedIn, na TikTok…
Video na výšku je dnes asi jediný formát, který jde natočit jednou a nacpat všude.

Nechám si to ještě projít hlavou, ale neexistuje důvod, proč to nezkusit, i kdybych s tím měl po týdnu nebo měsíci přestat.
Minimálně mi přijde dobré se vytrénovat a naučit se takové věci točit přirozeněji.
Jako stárnoucí mileniál jsem totiž rád, že sotva plynule ovládám selfíčka.

Byl by to výstup z komfortní zóny, ale bylo by to i něco nového a nejspíš by mi nevadilo, že to stojí za prd.
Na rozdíl od textu.
I když jde jen o status na LinkedIn, kladu na sebe příliš velké nároky a píšu to klidně půl hodiny nebo déle, ačkoliv se to nevyplatí.

## Výstava o F1

Byl jsem na [výstavě o F1](https://f1exhibition.com/vienna/).
Bylo to pěkné, bylo toho možná i moc, dala by se tam strávit spousta hodin.
Plno videí a interaktivních prvků.
Líbila se mi i technická část, kde byly skvěle zpracované milníky v rozvoji směrem k dnešní formuli (monokok, aerodynamika…).

Výstava nevyšla draho, v přepočtu snad 700 Kč nebo tak nějak, nebyla to nějaká řacha, a ještě člověk mohl vychytat i nějakou Velikonoční slevu (my teda ne).
Akorát je to ve Vídni no.
Zlanařili mě kamarádi z Ostravy, dali jsme to na otočku.
Vstal jsem někdy v 5, vyrazil RegioJetem, před polednem tam, pak 8 EUR celodenní lístek MHD ve Vídni, na výstavě jsme strávili několik hodin a pak v podstatě jedno kafe a domů zase RegioJetem.
Nejdražší na tom byl čas (ale tak já jsem ve vlaku pracoval, nebo si něco četl) a zpáteční lístek.
Nevím, do kdy to tam ještě je, ale na webu mají všude _NOW OPEN BUY NOW_, tak asi stále ještě můžete.

![Honza a F1]({static}/images/img-8435.jpg)

## Další

-   Viděl jsem v kině [Stovky bobrů](https://www.csfd.cz/film/1240536-stovky-bobru/) a bylo to super, smál jsem se od začátku do konce.
-   Dočetl jsem konečně The Future of Freedom: Illiberal Democracy at Home and Abroad (Fareed Zakaria), [recenze zde](https://www.goodreads.com/review/show/3544707917).
    Podle Kindlu jsem knihu rozečetl v říjnu 2020.
    Je duben 2024 😅
-   Apify, kde mám teď 20% úvazek, [dostalo investici](https://cc.cz/tezi-data-z-webu-a-je-v-zisku-datove-apify-ma-pres-200-tisic-uzivatelu-ted-nabira-70-milionu/).
-   Jedno celé dopoledne jsem nahrával podcastový rozhovor pro [PeopleOps](https://www.forendors.cz/izatlouk).
    Ten bude hlavně pro lidi z firem, kteří by nad juniory uvažovali.
    Jiné celé dopoledne a ještě i kus odpoledne jsem nahrával youtubový rozhovor pro [Lucii Lenértovou](https://www.youtube.com/@LucieLenertova/).
    Ten bude hlavně pro začátečníky, kteří by uvažovali o kariérní cestě Python programátorky nebo programátora.
    Z obou rozhovorů mám dobrý pocit a věřím, že se povedly.
    Na oba jsem se připravoval podle zaslaných okruhů a to významně zvýšilo mou pohodu při natáčení.
    Byť teda u Lucie jsem se mohl odtrhnout od programování dřív a připravit se dřív než noc předtím ve 2 ráno, možná bych pak byl čerstvější.
-   Byl jsem s kamarádem na kole.
    Píchnul a pak jsme to 2h řešili.
    Tuto historku jsem následně použil v rozhovoru s Lucií jako důkaz, že programátoři se nevzdávají, dokud nevyšťourají řešení problému, takže mě teď ty 2h serou o dost méně, mělo to smysl…!
-   Vedl jsem debaty pod příspěvkem o tom [jak Seznam kompletně zavřel svoje služby všem s adblockem](https://mastodonczech.cz/@jakubzelenka@mastodon.social/112246524750181098).
-   Přejmenoval jsem balíčky v junior.guru repozitářích podle [PEP 0423](https://peps.python.org/pep-0423/), takže mám teď `jg.plucker`, `jg.chick`, `jg.hen`, apod.
    Nevěděl jsem, jak pojmenovat balíček s monolitem, ale pouze `jg` by byla cesta do pekel a možná by to ani nešlo kvůli importům z těch ostatních balíčků.
    Tak jsem zkusil `jg.core`, ale to se mi nakonec nelíbilo a změnil jsem to na `jg.coop` (protože _coop_ by měl být kurník).
    Zabralo mi to mnohem víc času, než bych chtěl.
    Nejdřív jsem zápasil s tím, abych správně strukturoval složky a poladil konfiguraci Poetry.
    Změnami se pak rozbily všechny importy a všechny cesty mezi soubory, takže to jsem pak musel několikrát opravovat.
-   Volali mi ze Skillmea, že yablko bude mít nějaký meetup po svém JavaScript kurzu, tak jestli se nepřidám, neuděláme diskuzní panel, neodprezentuju junior.guru a nepozvu lidi z klubu.
    Tak jsem řekl že jo, že to zní dobře.
    Nemělo by v tom být nic, co mě stresuje, nebo vyžaduje mega přípravu.
    Termín ještě doladíme, ale bude to v květnu v Praze (Karlíně).
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Napsal jsem [článek o plánech na toto čtvrtletí]({filename}/2024-04-06_plan-na-q2-2024.md).
    Sdílel jsem na sociálních sítích [návod na to, jak si vyladit GitHub profil](https://junior.guru/handbook/github-profile/).
    Řešil jsem jeden nefunkční přístup do klubu.
-   Za 12 dní jsem naběhal 10 km, při procházkách nachodil 15 km, ujel na kole 46 km. Celkem jsem se hýbal 19 h a zdolal při tom 71 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Pár dní dovolené.
2.  Týden 22.-26.4. se budu věnovat kontraktu pro Apify.
3.  Sepíšu seznam fičur, které nabízí klub.
    Bude to podklad pro tvorbu nové prodejní stránky.

Během toho budu sledovat, jak lidi používají _reviews_ GitHub profilů a budu vymýšlet, jak bude přesně vypadat další krok směrem k profilům juniorů.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Důchodový sitcom](https://davidklimes.cz/newsletter/189)<br>Klimeš naložil: „Nevíme, co s dětmi, které ještě ve čtyřech se nemohou dostat do žádné školky, v druhém stupni jim zmizí půlka třídy na výběrové školy, na střední se složí z přijímaček, protože měli na vysvědčení dvě dvojky, což stačí na diskvalifikaci (či půl roku nechodili na drahé kurzy), aby nakonec po tom všem kolem roku 2028 zjistili, že stát je extrémně zaskočen silným zájmem končících středoškoláků o vysokoškolské vzdělání…“
- [Alonso will be "first to raise my hand" if he loses F1 edge at 45](https://www.autosport.com/f1/news/alonso-will-be-first-to-raise-my-hand-if-he-loses-f1-edge-at-45/10597928/)<br>Alonso bude závodit i ve 45 letech.
- [Moderní láska: Čím dál víc lidí se nehlásí k heterosexuální identitě — Balanc](https://www.mujrozhlas.cz/rapi/view/episode/7f97582d-180d-3868-9210-7f3ff3d29eb9)<br>Ve vztahu muže s mužem nelze spadnout do vyjetého stereotypu, který říká, kdo myje nádobí, kdo pere, kdo uklízí. Ti dva si to musí prostě domluvit. Tohle a spousta dalších super postřehů a myšlenek v epizodě Moderní lásky (Balanc).
- ['Pay or Okay' explained: Why more and more websites make you pay for your privacy](https://noyb.eu/en/pay-or-okay-explained-why-more-and-more-websites-make-you-pay-your-privacy)<br>Seznam začal s drsným "Pay or Okay". Max Schrems vysvětluje, jak to funguje a co nás v tomto směru čeká.
- [Why PHP continues to be a popular but divisive programming language](https://thenextweb.com/news/why-php-continues-to-be-a-popular-but-divisive-programming-language)<br>„PHP is used by 76.5% of all the websites whose server-side programming language we know.“ „While the rival languages see a higher frequency of use in high-traffic websites, PHP is still the dominant language across more than 60% of the world’s top 1,000 websites.“
- [Open Source Maintainers Owe You Nothing](https://mikemcquaid.com/open-source-maintainers-owe-you-nothing/)<br>„Most open source software is developed by volunteers in their free time but both maintainers and users of open source software have adopted an unsustainable business/customer-like relationship“
