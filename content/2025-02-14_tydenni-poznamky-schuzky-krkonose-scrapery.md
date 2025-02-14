Title: Týdenní poznámky: Schůzky, Krkonoše, scrapery
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/341
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/114004305563236804

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-01-31_tydenni-poznamky-oprava-lakatose.md) už utekl nějaký ten týden (31. 1. až 14. 2.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Kino

O prvním z proběhlých víkendů jsem si vylepšil [kalendář kin](https://github.com/honzajavorek/kino). Přidal jsem kina, rozdělil to na víc kalendářů (nejbližší a nejoblíbenější kina, vzdálenější nebo méně oblíbená kina, multikina). Přidal jsem rok vydání filmu a vlajku země, odkud film je. Přidání vlajky v podobě emoji byl zajímavý problém, protože na ČSFD kódy státu nejsou, jen české názvy, a navíc jsou tam historické státy, které už neexistují. S výsledkem jsem velmi spokojený, ale v kině jsem od té doby ještě nebyl 😅

![Kino]({static}/images/screenshot-2025-02-14-at-20-48-32.png)

## Petřín

Během téhož víkendu jsme si rozdělili aktivity, částečně i kvůli útočícím rýmičkám. Jeden den jsem vzal dceru na Petřín do zrcadlového bludiště a pak i na rozhlednu. Na ty zrcadla měla tak akorát věk, přišlo mi, a strašně si to užila, byla to velká společná sranda. Další den ji vzala žena na nějaké žonglovací divadlo kousek od nás.

![Hrad]({static}/images/img-3964.jpg)

![trpaslík]({static}/images/img-4005.jpg)

![výhled]({static}/images/img-4018.jpg)

## Scrapery na pracovní inzeráty

Pokračoval jsem v opravách scraperů. Abych toho neměl málo, scraper na katalog kurzů z ÚP začal nějak blbnout a když jsem se na to díval, zjistil jsem, že změnili celé API a mají novou verzi. Takže jsem to celé přepsal.

Dál jsem řešil hlavní scraper na pracovní inzeráty. S Vláďou z Apify jsme společnými silami kutali a kutali, až jsme vždy něco vykutali. Vyřešili jsme spoustu věcí, ale pak jsme narazili na nové, a tak stále dokolečka. Těsně před horami jsem objevil další chybu v Apify SDK, která nejspíš od začátku způsobovala celý problém. Během toho, co jsem byl na horách (viz níže), se povedlo Vláďovi udělat další průlomy a leccos opravit. Vznikly [PR #390](https://github.com/apify/apify-sdk-python/pull/390), [issue #392](https://github.com/apify/apify-sdk-python/issues/392), [issue #401](https://github.com/apify/apify-sdk-python/issues/401), a další.

Po příjezdu z hor vše vypadalo pozitivně a po pár hodinkách přehazování kódu vidlema jsem dospěl k funkčnímu výsledku. Scraper fungoval a za 30-40min svou práci udělal. Hurá! Pustil jsem si [Queeny](https://www.youtube.com/watch?v=04854XqcfCY) a radoval se.

Hned jsem dopracoval i HTTP cache pro Scrapy, která ukládá do Apify key-value storage. Tu jsem poslal jako [PR do SDK](https://github.com/apify/apify-sdk-python/pull/403). Poladil jsem [vstupy pro scrapery](https://github.com/juniorguru/plucker/issues/110) a vytvořil hned i API pro [Navigaru](https://navigara.com/), se kterou si nejspíš budu vyměňovat data. U té cache i u toho API jsem potřeboval gzip a docela mi v tom pomohlo ChatGPT. Díky němu jsem zjistil, že přímo v gzipu je zabudovaný UNIX timestamp a nemusím ho dávat nikam vedle. Nakonec jsem z kódu definitivně vyčistil scraper na [WWR](https://weworkremotely.com/), které pro junior.guru není relevantní.

No ale ten hlavní scraper je prokletý, zase blbne. Zase se objevují chyby, jiné, a zase jsou tajemné a nevím, čím to je. Ale jsou zase někde ve Scrapy-Apify integraci. Ach jo.

## Lea Boháčová a Q&A v klubu

Bylo všeho nějak moc a úplně jsem zapomněl na propagaci akce na sociálních sítích 🤦‍♂️ Nic zásadního se asi nestalo, nemyslím si, že to mělo dopad na návštěvnost, to už spíš fakt, že jsme to naplánovali v rychlém sledu. Akce byla fajn pokec od srdíčka, otázek jsem měl nakonec nejvíc já, ale myslím, že to dopadlo dobře. Patrik měl záznam připravený prakticky okamžitě.

![Lea]({static}/images/20250204-93a4f78746966dc30eae92fe369ce2b918af0b90df9466156b1d1f019bf59efa.png){: .img-thumbnail }

## Schůzky

Během týdne před dovolenou se mi nahromadily schůzky:

-   Oběd a kafe s Lukášem (kamarádské povídání),
-   oběd a kafe s Dariou (kamarádské povídání, dohazování práce),
-   call s Terkou (mentoring / nastavování Memberful / moje LinkedIn statusy),
-   call s [Adamem](https://www.linkedin.com/in/adamkral1/) (přednáška v klubu a psaní rozhovorů),
-   call s [Navigarou](https://navigara.com/) (spolupráce na pracovních inzerátech).

Byť to bylo i s kamarády, nějak jsem zapomněl, že jsem introvert, a navíc se mi do toho začala projevovat nějaká rýmička, tak mě to trochu převálcovalo. Musím si to příště hlídat a neplánovat si toho tolik.

## Krkonoše

Druhý proběhlý víkend a ještě pár dní potom jsme vyrazili do Krokonoš. Byl to pobyt s [Active moms & kids](https://www.facebook.com/activemomsandkids/) a bylo to super. Tento výlet byl promovaný jako ideální pro lidi bez auta, protože do destinace se autem stejně dojet nedalo a z Pece se muselo rolbou 😀 Takže [přesně pro nás]({filename}2021-08-28_bez-auta.md).

Nikoho jsme neznali předem, ale šli jsme do toho, protože se nám to podle popisu líbilo. Tradičně jezdíme na zimní dovolenou s kamarády, ale letos to na nás bylo nějak daleko, tak jsme zkusili tohle. A nelitujem, bylo to mega super. Bylo tam skvělé jídlo, bazén přímo na boudě, fajn připravený program, ideální pro rodiče malých dětí. Buď jsme se mohli účastnit toho, co bylo naplánováno, nebo si dělat, co jsme chtěli. Organizátorky byly taky mamky, tak jsme si nepřipadali jak s cestovkou, spíš jako v nějaké poloorganizované komunitě, a bylo to fajn.

Sbalili jsme se do jedné krosny a do jednoho menšího batohu. Boby jsem vzal do ruk. Jeli jsme tramvají a metrem na Čerňák, a pak autobusem do Pece. Protože nám vyšlo hezké počasí, tak jsme nakonec ani spoustu zabaleného oblečení nevyužili.

Akorát jsme cestou tam narazili na nějakou dementní autobusovou společnost jménem **JAMI LINES s.r.o.**, která nejen že přijela na zastávaku až v minutě odjezdu, takže než borec naložil plný autobus, měli jsme 20 minut zpoždění, ale navíc bylo zakázáno jíst v autobuse. Bylo to úplně bizarní. Autobus byl polepený asi tisícovkou samolepek o tom, že se v něm nesmí jíst, ani pít. Byly všude - na sedadlech, na každém skle, nad řidičem, zepředu na autobusu. Jakmile si kdokoliv vytáhl byť jen nakrájené jabko, řidič na nás začal řvát jako na nějaké malé spratky. Což je samozřejmě super, když má cesta trvat 2,5 hodiny (se zpožděním 3) a jedete s 3,5 roku starým děckem. No nějak jsme to přežili, ale firmě JAMI LINES od srdce přeji, aby shořela v pekle. Jak by řekl Cimrman: Provozovali autobus, ale jezdili jim v něm lidi!

V Peci pak už byly organizované rolby. To byl perfektní zážitek. Sice jsme se tam natřásali trochu jak brambory, ale byla to sranda a co se týče hromadné dopravy, po rolbě mi chybí už asi jen cesta vrtulníkem. Tu jsem ale naštěstí ani při dramatických situacích při jízdě na bobech nepotřeboval 😅

Cesta zpět byla stejná, ale autobus měl jiný dopravce, takže to už bylo bez problémů.

![Pec]({static}/images/img-4079.jpg)

![rolba]({static}/images/img-4104.jpg)

![hra]({static}/images/img-4113.jpg)

![Sněžka]({static}/images/img-4126.jpg)

![Javorka]({static}/images/img-4143.jpg)

![Krakonoš]({static}/images/img-4165.jpg)

![sníh]({static}/images/img-4252.jpg)

## Další

-   Jedna firma mi napsala, že by rádi inzerovali na [junior.guru/jobs](https://junior.guru/jobs). Navrhl jsem, že se mohou přidat do klubu a dát do pro členy zadarmo, nebo že si mohou vybrat [libovolný firemní tarif](https://junior.guru/love/) a že to vložím na web jako dlouhodobý inzerát. Vybrali si první možnost. Zatím to budu dělat takhle a uvidím, co s ručně vkládanými inzeráty bude do budoucna.
-   Přidal jsem nové sponzory junior.guru, [Praha Coding School](https://prahacoding.cz/). Děkuju Danovi, že mi pomohl s SVG variantou loga.
-   Na [junior.guru/jobs](https://junior.guru/jobs) jsem přidal ke každé pracovní nabídce odkaz na [Jaký byl pohovor?](https://www.jakybylpohovor.cz/)
-   V klubu jsem do kanálu s pracovními nabídky přidal automatický připnutý příspěvek, který zviditelňuje ručně přidané inzeráty od lidí přímo z klubu, aby nemizely v záplavě inzerátů stahovaných odjinud.
-   K Valentýnu jsem dal ženě kolopejku v květináči a dostal pytlík kafe se zamilovanou kudlankou.
-   Prodloužili jsme zase o rok nájem.
-   Nakoupil jsem dva další Discord boosts pro server, abychom mohli používat všechny funkce, které potřebujeme. Už to začíná lézt docela do peněz. Kde že je ten Discord zadarmo? 💸
-   Otevřel jsem u Cucumberu [diskuzi o AI](https://github.com/orgs/cucumber/discussions/2230), ale vlastně se moc nerozjela.
-   Abych si připadal užitečný, udělal jsem pro Apify i nějaké reviews, a to [zde](https://github.com/apify/apify-docs/pull/1217) a [zde](https://github.com/apify/apify-docs/pull/1442).
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Hromady, hromady zpráv! Po dovolené bylo jen e-mailů k 60. A zdaleka nemám hotovo.
-   Za 15 dní jsem při procházkách nachodil 8 km, na túrách nachodil 14 km. Celkem jsem se hýbal 11 h a zdolal při tom 22 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Dát nějak dopořádku všechno kolem Apify.
2.  Doplánovat si věci kolem junior.guru.
3.  Udělat administrativu a odpovídání kolem junior.guru.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Jak se ostravský lidovec stal průkopníkem boje proti menstruační chudobě v ČR – Page Not Found](https://pagenotfound.cz/clanek/jak-se-ostravsky-lidovec-stal-prukopnikem-boje-proti-menstruacni-chudobe-v-cr)<br>V Ostravě měli jako první pípání kreditkou za cestu tramvají, teď mají jako první plošně dostupné menstruační potřeby na školách 👏 Kdo ví, jestli se podobné vymoženosti jednou dostanou i do Prahy.
- [Proč Ukrajina míří údery v týlu Ruska na rafinerie?  |  iROZHLAS - spolehlivé zprávy](https://www.irozhlas.cz/zpravy-svet/utoky-ktere-cili-na-zivotni-mizu-valky-proc-ukrajina-miri-na-ropne-rafinerie-v_2502120620_eku)<br>Tohle je pěkné shrnutí aktuálního stavu na Ukrajině.
- [Joe Coleman](https://getcoleman.com/)<br>Tohle je naprosto dokonalý. Většina Česka: úplně vlevo. Většina USA: úplně vpravo 😀
- [The Console Wars Are Over And Nobody Really Won](https://kotaku.com/console-wars-are-over-ps5-xbox-forza-switch-2-sony-1851752956)<br>Herní konzoli jsem nikdy neměl. Zjevně jsem tím zazdil válku, která zrovna končí.
- [Indové překolejili Himálaj a napojili Kašmírské údolí na železniční síť - Zdopravy.cz](https://zdopravy.cz/indove-prekolejili-himalaj-a-napojili-kasmirske-udoli-na-zeleznicni-sit-234847/)<br>„…museli zbudovat 27 tunelů a 37 mostů. Nejdelší tunel měří 13 kilometrů. Most přes řeku Čanáb je nejvyšším železničním mostem na světě, tok překlenuje ve výšce 359 metrů. Za vrchol inženýrského umu označují Indové i lanový most přes řeku Anji. Jde o první železniční lanový most v Indii. Stavbaři se museli vyrovnat s náročným terénem, extrémním počasím, sesuvy půdy i seismickou aktivitou.“
- [What Color is Your Function?](https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/)<br>Klasika, o které jsem věděl, ale nikdy ji vlastně nečetl. Tak jsem to po týdnu zanořeném do boje přesně s těmito věcmi napravil. A autor dobře pojmenoval to, co mi od začátku vždycky u asynchronního kódu vadilo, ať už to byl Node.js, nebo Python.
