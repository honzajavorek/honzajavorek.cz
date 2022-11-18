Title: Týdenní poznámky #66: Kousky příručky v Markdownu, data z inzerátů v API
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl zase nějaký ten týden (13.9. — 19.9.) a tak [stejně jako minule]({filename}2021-09-12_tydenni-poznamky-65-prirucka-a-data-z-pracovnich-nabidek.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Komunikace

Velkou část týdne zabrala komunikace: Call ohledně prodloužení partnerství s jednou firmou, call výboru Pyvce (ten byl výživnější, než jsem čekal, všichni to vzali dost poctivě, tak se to protáhlo), call s ředitelkou jedné skvělé neziskovky, call s [kamarádem](https://milavotradovec.cz/) o práci a o AI na třídění nabídek práce.

Dále jsem šel na [pražské Pyvo](https://pyvo.cz/), byť jen tak na dvě hoďky, pozdravit lidi. Dále jsem šel na pokec s člověkem, který má kontakty na dětské domovy a jiné organizace tohoto typu, aby mi řekl, co si myslí o naší připravované aktivitě spolu s [Mews](https://www.mews.com/en/careers). K tomu všemu hromada mailů, domlouvání dalších callů a schůzek, komunikace kolem dat pro Czechitas, prostě takový podzimní shon.

Dal jsem na sociální sítě ještě nějaké promo na WebExpo (už za pár dní) a komunikoval se Šárkou z [WebExpa](https://www.webexpo.net/prague2021), [Danem](https://coreskill.tech/), jenž mě tam zastoupí a lidmi, kteří v klubu vyhráli lístek zdarma. Nakonec jeden ještě narychlo znova losuji.

Ze schůzky o stipendiu pro znevýhodněné jsem si udělal spoustu poznámek, ale zatím jsem neměl čas v tom dál pokračovat. Dalším úkolem je upravit leták, aby odpovídal cílovce a realitě, případně rozjet paralelně s letákem formulář na to, aby se i jednotlivec mohl přihlásit ke stipendiu, už se na to ptaly i další firmy.

Z callu o AI jsem si odnesl poznámky o tom, jaký bude další postup, jak mají vypadat datové modely a jak vlastně to AI v případě JG přesně funguje.


## Přesun částí příručky do Markdownu

Po stránce s motivací se mi tento týden povedlo přesunout do Markdownu stránky se [základy](https://junior.guru/learn/) a s [praxí](https://junior.guru/practice/). Nejtěžší na tom bylo opravdu je pouze 1:1 překlopit a nezačít všechno zuřivě přepisovat a předělávat, což bych si jinak samozřejmě velmi přál udělat. Teď zbývá už překlopit „jen” [stránku o hledání práce](https://junior.guru/candidate-handbook/), která je strašně dlouhá a může to být snad i na týden práce, to se nechám překvapit.


## Vyplňování formulářů

Minule jsem psal o nějaké té byrokracii. Tak jsem zjistil, že zdaleka není hotová. Musel jsem doložit ještě další dokumenty a vyplnit další formuláře. Dále jsem musel vyplnit své finanční výsledky za poslední 3 roky, vlastníky firmy nebo lidi na nejdůležitějších pozicích. Také stále dokola nekonečné vysvětlování, že nejsem plátcem DPH. Ach jo.

![TYS, vlastnictví]({static}/images/tys-ownership.png)
Nebudete tomu věřit, ale jsem 100% vlastníkem junior.guru!

![TYS, pozice]({static}/images/tys-ceo.png)
Zkratku DOS jsem ani neznal, ale jsem si docela jistý, kdo na této pozici v junior.guru pracuje


## Oprava stahování inzerátů z LinkedIn

Minulý týden jsem zjistil, že mám rozbité stahování inzerátů z LinkedIn. Tak jsem ho opravil. Postahovat si jednotlivé stránky a upravit a otestovat scraper nad novým HTML to nebyl zásadní problém.

Nejvíc mi dalo zabrat, že mi LinkedIn vracel stránky v češtině a já nevěděl proč. Chtěl jsem scrapovat uživatelské rozhraní v angličtině, ať je tam napsané „full time“ a ne „plný úvazek“ apod., pracuje se mi s tím lépe. Taky jsem chtěl, abych měl nějakou jistotu, že to bude v určitém jazyce, ne že mi tam skočí francouzský inzerát a místo „full time“ tam najednou bude nějaké „je ne t'aime plus mon amour je ne t'aime plus tous les jours“.

Snažil jsem se nastavit cookies nebo hlavičku `Accept-Language`, ale nefungovalo mi to. Zkoušel jsem upravovat a odesílat HTTP requesty přímo z Firefoxu a zkoumal, jak je udělané přepínátko jazyků. Díky tomu jsem zjistil, že to má fungovat tak, jak to dělám, takže je chyba někde u mě. Naštěstí má Scrapy celkem dobré možnosti debugování toho, co přesně se odesílá. Naneštěstí má Scrapy nějaké nastavení `DEFAULT_REQUEST_HEADERS`, kam jsem kdysi cosi napsal a zapomněl na to. Naneštěstí jsem si nevšiml, že můj scraper posílá requesty na víc místech, než na kterých jsem přidal cookies a hlavičky. No co vám budu povídat, celý den jsem na tom spálil, přitom taková blbost. Ještě že máme v klubu místnost `#past-vedle-pasti`, kam si člověk může postěžovat.


## Data pro Czechitas

Snažím se docílit toho, abych měl API pro Czechitas, kde by byla data o inzerátech, aby nad tím mohly dělat grafy aj. datové kejkle. Domluvili jsme se, jak to má zhruba vypadat a mě se to celkem hodí, protože dost podobné nároky nakonec měl i [Míla](https://milavotradovec.cz/) se svým AI na třídění nabídek práce podle toho, zda jsou juniorní.

Tvořím to trochu za pochodu a stále mi není stoprocentně jasné, jak to celé bude fungovat. Měl jsem nějakou ideu, že se bude zachovávat historie nabídek práce z předešlých záloh databází, ale teď zjišťuji, že je to možná složitější problém. Tu řeším, co s tím, když má nabídka víc URL, tam řeším jak je vlastně chci párovat, atd., každá věc má obrovský dopad na ten systém do budoucna a já bych to chtěl udělat „správně“, ale zároveň „ne zbytečně komplikovaně“, tak zkouším a přemýšlím.

A při tom dělám spoustu i malých chyb, tak programuju, testuju, opravuju, a tak dále. Čím dál tím víc mám pocit, že jsem s těmi inzeráty otevřel nějakou Pandořinu skříňku, že jsem si teď ukousl moc velké sousto, ale zase bez impulzů od Czechitas a od Míly bych to taky nemusel otevřít nikdy a hnilo by to. Musím se víc soustředit na to, abych věci dělal co nejpřímnější, nejjednodušší cestou, a až časem je ladil. Jenže moje hlava inženýra ne a ne se zbavit pocitu, že vše musí navrhnout a vyladit i pro ty méně obvyklé případy.

Nemám to tedy ještě dokončené. Na [adrese API](https://junior.guru/api/jobs.json) stále nic moc není a na disku mám rozpracovaný kód, nad kterým visí víc otazníků než odpovědí.


## Pocity

Mám pocit, že nic nestíhám. Že mám rozjetou hromadu věcí a nemám šanci žádnou z nich v rozumném čase dokončit:

- Data pro Czechitas
- Stipendium pro znevýhodněné
- Přehození příručky na nový design a do Markdownu
- Moderování, odpovídání, vylepšování služeb a drobností v klubu, domlouvání přednášek
- Psaní, ať už článků nebo osvěžování částí příručky

Se zvýšenou komunikační režií teď v září a přechodem na _de facto_ poloviční úvazek, abych si taky užil dítě, si teď připadám úplně ztracený. Navíc mám i pocit, že mi souhrnné měsíční příjmy poslední měsíce spíš stagnují, nebo tedy možná nestagnují, ale zvyšují se velmi pomalu. A teď mám teda pocit, že jsem dostal rýmičku a jestli jsem něco dělal pomalu, tak teď to pár dní nebudu moct dělat vůbec.

Možná budu muset nějaké věci omezit, nebo prostě vykutit přes noc, nevím. Přijde mi, že prioritou byla nová [klubová stránka](https://junior.guru/club/), ale pak se mi to trochu rozstřelilo. Nebylo úplně jasné, co má přednost, tak jsem začal dělat tak trochu vše, navíc do toho spadla spousta nárazových příležitostí, které je dobré kout, dokud jsou žhavé.

Myslím si, že nejvíc bych teď měl dělat marketing. Nová klubová stránka funguje, protože i z [jednoho blbého tweetu](https://twitter.com/honzajavorek/status/1430187105246973957), který jsem nijak nepromoval (jen jsem jej tweetl, abych si jej mohl na Twitteru připnout) přišlo do klubu jednorázově dost lidí. V konverzi tedy už asi není problém, je problém v tom, že na stránku zřejmě míří málo relevantních lidí. Takže už vymýšlím strategie, jakou cestou toho dosáhnout.

Nemyslím si, že můžu jen tak bušit do lidí stále to samé, marketing existujících projektů podle mě funguje tak, že něco význameného přidám a pak to promuju jako novinku, čímž se na světlo dostane i to staré známé. Asi by to šlo vykutit i nějak narychlo, ale já bych to chtěl spíš promyšleně než narychlo. Třeba bych chtěl nejdřív hodit příručku do toho nového designu, než do ní zase něco přidám a začnu to promovat. Taky by mi mohlo pomoct, že domlouvám nějaké psaní textů pro časopis.


## Další poznámky

- Na GitHub Sponsors mě začala podporovat [Veronička](https://github.com/lspdv)! Jupí! Pokud mě chcete taky podporovat, přečtěte si nejdřív [toto](https://junior.guru/faq/#dobrovolne-prispevky).
- Půl dne jsem debugoval, proč se inzeráty někde nezobrazují, než jsem našel zbloudilý `if` v šabloně, kvůli kterému to bylo.
- Byli jsme s dítětem na dvou preventivních kontrolách u doktorů, což si vzalo vždycky tak půlden.
- Možná budu psát články do jednoho časopisu, je to ve fázi domlouvání.
- Některé videa jsem znal už jako gify, ale neznal jsem autora a nevěděl jsem, že má vlastní kanál: [OwlKitty](https://www.youtube.com/c/OwlKitty/videos). [Pulp Fiction](https://www.youtube.com/watch?v=H7G1yjDfwL4) je moje oblíbené.
- Během 7 dní od 13.9. do 19.9. jsem při procházkách nachodil 3 km. Celkem jsem se hýbal 2 hodiny a zdolal při tom 3 kilometry. Kamarádi mě vyhodili z motivační telegramové skupiny na běhání, protože neběhám. Chtěl jsem jet na kole do Roudnice na ZMJ, ale padl jsem s rýmičkou, takže nakonec ani to.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Vyléčit rýmičku ¯\\\_(ツ)\_/¯ U toho bych mohl přesypat Trello a srovnat priority.
2. Udělat jedno větší rozhodnutí ohledně spolupráce a v pondělí nebo úterý dát vědět druhé straně.
3. Vzít prioritu z bodu 1 a pracovat na ní.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [‚Vůbec nevím, proč nám něco slibují.‘ Politické strany cílí na hlasy vietnamské komunity](https://www.irozhlas.cz/zpravy-domov/volebni-billboard-ve-vietnamstine-trikolora-svobodni-soukromnici_2109120500_piv)<br>„Starší generace, která umí vietnamsky, většinou volit nemůže. A ti, co mohou volit díky českému občanství, ten poutač zase sotva přečtou.“
- [Vítejte v nestydaté době. Může být radostná](https://mailchi.mp/fe8726c219f0/ploha-o-nestydatosti)<br>„Pro obě má nestydatá doba opačný význam. Sciortino vidí emancipaci a sebeurčení, Wodak šarlatány rozkládající konvence veřejné slušnosti. Pro první je konečně všechno normální, pro druhou se stává dosud nemyslitelné bohužel normální.“

<small>Upozorňuji, že to není vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
