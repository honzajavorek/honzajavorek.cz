Title: Týdenní poznámky: Rozkládání dat o předplatném na atomy
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-07-07_tydenni-poznamky-sam-doma.md) už utekl nějaký ten týden (7. 7. až 14. 7.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Bug v datech o předplatném

O víkendu nebo tak nějak jsem dostal report, že se někomu nepřiřazují na Discordu správně role.
Hlavně jedna role, která umožňuje přístup do některých skrytých kanálů, a která se přiřazuje na základě kupónu, s nímž vzniklo předplatné daného člověka.

A tak začalo pátrání.
Brzy jsem zjistil, že role se přiřazují správně, ale ty kupóny chybí v datech.
Občas.

Začal jsem zkoumat, co mi chodí z API od [Memberful](https://memberful.com/), ze kterého to beru.
No a zjistil jsem, že to celé nějak nesedí.
Napsal jsem na (naprosto skvělou) podporu Memberful, co jsem zjistil, a pak jsme společně zkoušeli různé věci, například jestli nemám chybu v tom, jak stránkuju odpovědi.
Strávil jsem debugováním dva dny, ale výsledek byl nakonec jasný.
Je to chyba na jejich straně.

API vracelo v seznamu předplatných duplicity a některé předplatné naopak ve výpisu chyběly.
Můj kód samozřejmě předpokládal, že každý objekt v odpovědi je unikátní a že jsou tam všechny.

Bug se však projevoval jen na výpisu předplatných.
Protože jde o GraphQL API, snadno jsem se na všechna předplatné dostal oklikou přes výpis členů, kde bylo vše správně, a svůj systém opravil.
Z Memberful mi poděkovali za report a debugování, a pak mi dali vědět, když se to povedlo opravit i jim.

Starý skript se staral jak o (kritická) data pro přiřazování rolí, tak o (nedůležité) statistiky pro [/open/](https://junior.guru/open/).
To vše jen komplikovalo.
Nově jsem to tedy rozdělil na dvě zcela nesouvisející věci, i co se týče tabulek v databázi.
Také jsem přidal kontrolu, zda nemám na Discordu někoho úplně bez účtu na Memberful.

To vyústilo ve vyhození jedné osobnosti českého internetu, která samozřejmě nebyla černým pasažérem, ale byla v klubu úplně od začátku ještě na nějakou pradávnou čistě Discordí pozvánku.
Omluvil jsem se, ale pořádek musí být, tak snad se vrátí zpět přes standardní účet u Memberful 😀

## Zrušení vyúčtování studentů

Od loňského podzimu jsem vyjednával s jednou vzdělávací agenturou, zda si zaplatí partnerství na další rok a jaké.
V rámci předchozí dohody měli i to, že mohli do klubu posílat studenty na 3 měsíce.
To jsem vždy jednou za čas sečetl a poslal jim na to fakturu, aby mi tyto 3 měsíce pro své studenty propláceli.
Ačkoliv už jim neběželo partnerství, posílání studentů jsem nechal funkční, na dobré slovo.
Přece jenom to byl příslib peněz.

Tato věc měla několik nevýhod:

-   Agentura neměla moc motivace dotahovat roční partnerství k dohodě, protože vlastně měli, co potřebovali.
-   Vyúčtování studentů nebyl vůbec triviální skript a komplikovalo mi to kód na více místech projektu.
-   Tuto věc využila pouze tato firma a žádná jiná.
-   Šéfka, s níž jsem měl dohodu, z firmy odešla.
    Člověk, který to měl převzít, mi nikdy na zprávu neodpověděl.
-   Do budoucna už jsem tímto způsobem pokračovat nechtěl.
    V novém ceníku jsem nabídl měsíc zdarma pro studenty, pokud si firma zakoupí stříbrný tarif, a tři měsíce zdarma, pokud zlatý.
    Paušálně, bez další administrativy, bez dalšího proplácení.

Jak jsem hledal bug ve skriptech stahujících informace o předplatném, ruply mi už nervy z toho, jak jsou komplikované, a napsal jsem jim mail.
Že to celé trvá moc dlouho, že jim zastavuji studentský kupón a posílám fakturu.
A že se moc rád domluvím na pokračování, ale s čistým stolem a podle aktuálního ceníku.

Při tom jsem zjistil, že jak jsem si před časem omylem smazal některá historická data ohledně předplatných, tak jsem si nejspíš promazal i údaje o tom, kdo šel přes tenhle kupón.
Bohužel jsem se tedy nejspíš obral o dost peněz tím, že už nejsem schopen spočítat a doložit, kolik přesně studentů poslali.
Udělal jsem co nejpoctivější analýzu aspoň těch dat, které mám, a studenty, které doložit umím, jsem vyúčtoval.

Pro jistotu jsem přidal do kopie i kontaktní mail celé firmy a fakturu vystavil jako proformu.
Nepřekvapivě se mi zpráva člověku, který to měl převzít, vrátila jako nedoručitelná, protože už tam asi nepracuje.
Jinou odpověď zatím nemám.
Nevím, co se tam děje a nevím, jestli své peníze někdy uvidím.

Tak či tak jsem ale šel a okamžitě smazal všechen kód, který se této funkce jakkoliv týkal.
Aspoň to mi udělalo velkou radost.

## Opravování grafů s předplatným

Když už jsem se v tom všem zrovna vrtal, jal jsem se opravit grafy s předplatným na [/open/](https://junior.guru/open/).

Chvíli jsem měl dojem, že jsem si možná žádná historická data nesmazal, že to byla jen ta chyba na straně Memberful.
Ale není to tak, bohužel opravdu nějaká data nemám.
Pokud někdo přišel do klubu, byl tam chvíli, a pak ukončil členství ještě před změnou tarifů, tak byl i po migraci tarifů stále navázaný na ten starý tarif, který jsem následně ~~uklidil~~ smazal.

Na fungování klubu to nemá vliv.
Jediné, co mě napadá, je že pokud by se ten člověk vrátil, tak mu akorát bot nezapočítá, že už je s námi hodně dlouho a nedostane odznáček za odkroucené roky.

Na fungování statistik to má zásadní vliv.
Prakticky mám do letošního března nekompletní data, z nichž tudíž nemůžu nic zásadního vyvozovat.

Co s tím?
Pokusím se postahovat vše, co k dispozici mám, a poskládat z toho aspoň něco.
Některá data jsem schopen získat z jakéhosi „activity logu“.
Když to dám dohromady, možná budu stejně muset některé grafy ořezat, ale jiné budou možná moci zůstat na celou délku historie klubu.

Začal jsem na tom hned pracovat.
Onen „activity log“ mě taky přivedl na myšlenku, že by to možná mohl být lepší způsob, jak údaje o předplatných reprezentovat v databázi.
Původně jsem si ukládal nějaké úseky od-do, ale bylo strašně obtížné s tím správně pracovat při skládání dotazů do databáze.
Teď to zkusím jako body v čase, které označují nějaké události.
Třeba to bude lepší.

Když jsem potřeboval udělat něco zapeklitého v SQL, respektive v Peewee, tak mi docela dobře pomohlo ChatGPT.
Některé věci bych sám vůbec nevymyslel, nebo bych je vymýšlel týden.
Někdy mi poradil blbě, ale přivedl mě na dobrou myšlenku.

![ChatGPT radí]({static}/images/screenshot-2023-07-14-at-14-36-54.png){: .img-thumbnail }

![ChatGPT radí]({static}/images/screenshot-2023-07-14-at-14-37-05.png){: .img-thumbnail }

## Prevence ztráty dat?

Do budoucna mě napadlo, že by se historické statistiky neměly živě počítat znovu a znovu.
Měl bych si ke každému grafu někam ukládat podkladová data, třeba anonymizovaná.
Podkladová proto, že pokud si uložím agregovaná, tak nemůžu už přidat nový graf, nebo změnit metodiku výpočtů.

Ta podkladová se ale už nezmění a nemá smysl je stahovat stále znova.
Taky se může stát, že se smažou, a to nejen omylem, ale i záměrně.
Některá data mohou mít retenci, nebo někdo půjde a svoje data prostě ručně smaže.

## České řazení v databázi

Zjistil jsem, že neexistuje moc jednoduchých a snadno přenositelných způsobů, jak řadit česky v SQLite.
To znamená tak, aby ch bylo po h, nebo š po s.

Napadlo mě, zda by nějak nešlo použít balíček [czech_sort](https://github.com/encukou/czech-sort) od Petra Viktorina, ale nešlo.
Tak jsem založil [issue](https://github.com/encukou/czech-sort/issues/8), co by mi poradil.
Odpověděl komentářem s implementací a prosbou, zda bych nechtěl poslat Pull Request.

Sednul jsem na to a [PR poslal](https://github.com/encukou/czech-sort/pull/9), ale nedokončený, protože czech_sort stále podporovala Python 2 a ten já už neumím.
A hlavně neumím a už ani nechci umět psát kód, který podporuje jak Python 2, tak Python 3.

Petr byl za PR rád a nakonec udělal [stream](https://www.youtube.com/watch?v=qEMCs3lQDIw), kde změny živě zpracoval a knihovnu trochu aktualizoval.
Ještě jsem to neviděl.

Měl jsem pak ještě jeden [dotaz](https://github.com/encukou/czech-sort/issues/13) a poslal [jedno malé zvýraznení](https://github.com/encukou/czech-sort/pull/12) a [jedno malé zestručnení](https://github.com/encukou/czech-sort/pull/11) dokumentace.

Výsledkem je, že teď jde czech_sort použít i jako _custom function_ v SQLite.
Např. v Peewee [takto](https://docs.peewee-orm.com/en/latest/peewee/database.html#sqlite-user-functions).

Až později jsem si všiml, že SQLite má i něco jako _custom collation_, což by se možná vlastně hodilo víc, ale to raději Petrovi říkat nebudu 😱
Mě to určitě stačí jako funkce, řazení mi teď funguje hezky.
Nedal jsem ho ještě všude, ale pro začátek aspoň do katalogu kurzů.

Vzápětí mi sletěly testy, protože moje testovací databáze tuto novou funkci neměla.
Hrál jsem si pak docela dlouho s [pytest fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html), aby to celé začalo nějak fungovat.
Nic lepšího než [překopírování funkcí z nějakého privátního atributu](https://github.com/honzajavorek/junior.guru/blob/3882b3060ca30194502e0295f55d6817d288bb2c/tests/testing_utils.py#L20) jsem nevymyslel.

![Řadím česky!]({static}/images/252895730-887af0ae-e08d-4823-bac7-57a73ac5c38e.png){: .img-thumbnail }

## Data z úřadu práce

Ve volné chvilce jsem se podíval, jestli nějak půjde scrapnout [katalog kurzů úřadu práce](http://www.jsemvkurzu.cz/).
Nejdřív jsem napsal mail na MPSV, zda ten katalog náhodou nemá API, nebo někde není jako open data ke stažení, ale to mi přišla jen automatická odpověď, že to dorazilo na podatelnu, a kdo ví kdy a jestli dostanu odpověď i od člověka.

Rychlejší bylo šťourání do té webovky.
Hned jsem si všiml, že celá běží nad JSON API, které je sice česky, má dost podivnou strukturu a místy je trochu tajemné, ale celkem bez problémů se dá _reverse engineerovat_.
No a už jsem si nedokázal zabránit, nadšeně jsem to zkusil rovnou krátkým skriptíkem postahovat.

Do svých YAMLů k jednotlivým poskytovatelům kurzů jsem ke každému přidal IČO a podle něj spároval data.
U některých bylo docela zapeklité IČO zjistit.
Že jsou kurzy až takový divoký západ, to jsem nečekal.
Někteří poskytovatelé mají těch IČO více, protože jsou firma i neziskovka.
Zajímavé.

Data jsem spároval a vypsal na webu jako seznam.
Někde je dlouhý a ošklivý, někde krátký, někde není vůbec.
Hezčí zobrazení vyřeším později.
Zatím jsem z toho akorát ořezal emoji a seřadil to podle abecedy.
Emoji ořezávám tady i v pracovních inzerátech proto, že je do titulků firmy sypou jako levnou formu zvýraznění nebo jako trik, jak být první v nějakém výpisu.
Katalog úřadu práce na to imunní není, ale můj katalog na to imunní bude :)

![Kurzy z úřadu práce]({static}/images/screenshot-2023-07-14-at-23-19-28-zkusenosti-s-engeto-academy.png){: .img-thumbnail }

## Simple Analytics API

Ve volné chvíli mě napadlo, že bych mohl přidat na [/open/](https://junior.guru/open/) grafy s návštěvností webovek junior.guru.
Ta je veřejně na [Simple Analytics](https://simpleanalytics.com/junior.guru), ale já jsem chtěl udělat nějaká souhrnná čísla, např. kolik lidí chodí na všechny URL, které klasifikuju jako příručka, atd.
Prostě si to rozdělit podle „produktů“, které provozuji.

Taky jsem si chtěl pohrát s [API od Simple Analytics](https://docs.simpleanalytics.com/api/stats), protože pokud bych se v něm vyznal, mohu si stahovat i detailní čísla ke katalogu apod. a třeba je použít na řazení kurzů, nebo to reportovat firmám, které platí za zvýraznění.
A to ani nepoužívám [eventy](https://docs.simpleanalytics.com/events), které by tomu dodaly ještě další rozměr.

No a to API mě strašně příjemně překvapilo!
Je tak jednoduché, že jednodušší už to ani nejde.
Pokud má můj projekt veřejné statistiky, což má, tak jsem ani nepotřeboval žádný token, nic.
Jeden požadavek na jedno URL, jedna odpověď, [a je to](https://simpleanalytics.com/junior.guru.json?version=5&fields=pageviews,visitors,pages&info=false&page=/courses/*).
První pokusy jsem měl hotové snad za pět minut programování.
Byl jsem, a stále jsem, naprosto nadšený.
Neumím si představit, že bych se stejná data snažil vytahovat z API od Google Analytics.
To bych dělal snad doteď.

Výsledky [jsou už na webu](https://junior.guru/open/#navstevnost) v podobě dvou grafů.
(Může se z nich zdát, že po zdražení mi přestali lidi chodit na web, ale to je jen optický klam.
Ve skutečnosti jde o to, že návštěvnost je silně sezónní a nejvíc lidí hledá jak začít s něčím novým v září a v lednu.)

![Grafy návštěvnosti]({static}/images/screenshot-2023-07-14-at-23-38-56-jak-se-dari-provozovat-junior-guru.png){: .img-thumbnail }

## Python komunita

Celkem dost jsem se tento týden věnoval Python komunitě:

-   Intenzivní čtení a odpovídání na [Pyvec Slacku](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
-   Zavolali jsme si konečně jako výbor a probrali jsme důležité věci.
    Nevíte někdo o někom, kdo dělá účetnictví spolků?
-   Přidal jsem do patičky [pyvec.org](https://pyvec.org/) kód naší datovky.
-   Jako emeritní člen komunity jsem dostal lístek na EuroPython 2023, který se koná příští týden v Praze.
    Neplánoval jsem tam jít, protože mě to o pár let minulo a co se týče Python komunity, cítím se za zenitem.
    Mám rodinu, podnikání, aktivní v komunitě už tolik nejsem, nic neorganizuji, konference neobrážím, Python už nežeru moc do hloubky.
    Ale asi teda přijdu.
-   Hledal jsem doma krabici se starými věcmi na stánek Python komunity.
    Na EuroPythonu totiž takový stánek bude.
-   Napsal jsem na [1Password](https://1password.com/), jestli mají nějaké slevy na týmové tarify pro neziskovky.
    Odepsali velmi svižně, slevy mají.
    Možná v Pyvci využijeme.
-   A nakonec mi možná dokonce hrozí _last minute_ účast v [tomhle panelu](https://ep2023.europython.eu/session/python-organizers-panel-exploring-community-driven-python-conferences) 😱

## Další

-   Volal jsem si s [ENGETO Academy](https://junior.guru/courses/engeto/).
    Domluvili jsme se na prodloužení partnerství.
    Hned jsem využil nové grafy návštěvnosti na /open/ 😀
    Kromě jiného budeme dál pracovat na anketě pro juniory.
    Vše jsem pak [zaevidoval](https://junior.guru/open/engeto/) a poslal fakturu.
-   Ozval jsem se po čase do [Praha CODING School](https://junior.guru/courses/prahacodingschool/), se kterými komunikuji už dlouho, ale nějak jim trvá rozhodování.
-   Přišla mi z ničeho nic poptávka od [Coders Lab](https://junior.guru/courses/coderslab/) na zařazení do katalogu a zvýraznění.
    Tak si budu držet palce, třeba to klapne.
-   Povídal jsem si se supportem Meetup.com a potvrdili mi, že Atom jim nefunguje, protože už ho podporovat nechtějí (ale odkazy zůstaly a jsou rozbité?) a iCalendar odkaz je záměrně za loginem.
    Zeptal jsem se jich, proč je záměrně za loginem, ale nemám na to zatím odpověď.
    Jelikož jako Pyvec několika skupinám proplácíme organizátorské předplatné na Meetup.com, jsem z jejich přístupu zklamaný a bude pro mě těžší takové proplácení podpořit jako člen výboru.
    Možná by šlo používat [TalkBase](https://talkbase.io/), které doporučuje [Láďa Vašek](https://www.linkedin.com/in/ladislav-vasek/)?
    Přijde mi, že to je spíš na firemní akce, než na komunitní.
    Meetup.com zná každý a je tam vyhledávání, což samo od sebe funguje na akvizici nových lidí.
    I když - funguje?
    Nevíme, asi neměříme.
-   Opravil jsem chybu, kdy bot v kanálu #ahoj na Discordu zdravil sám sebe 🤦‍♂️
-   Pro komunikaci se supportem Memberful i Meetup.com jsem použil nahrávání krátkých screencastů přes [Loom](https://www.loom.com/) a bylo to hodně jednoduché a pohodlné.
-   Na LinkedIn se toho tento týden dělo nějak hodně.
    Můj komentář [tady](https://www.linkedin.com/feed/update/urn:li:activity:7079342067864219649/?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7079342067864219649%2C7079595234296299520%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287079595234296299520%2Curn%3Ali%3Aactivity%3A7079342067864219649%29) dostal 41 lajků, Martin Kavka dál [propagoval moje moudra](https://www.linkedin.com/posts/newsletterista_newslettery-komunita-radyprotvahdrce-activity-7085203887996956674-aliF?utm_source=share&utm_medium=member_desktop), já jsem [propagoval svoje moudra](https://www.linkedin.com/feed/update/urn:li:activity:7084509168178450432/), Vít Heřt [pochválil junior.guru](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7082344697024655361/) a já mu to [trochu vrátil](https://www.linkedin.com/feed/update/urn:li:activity:7085216795363553280/), Jakub Pacanda se na mě odkázal ve [svém příspěvku](https://www.linkedin.com/posts/jakubpacanda_%C4%8Derven-2023-honza-javorek-o-placen%C3%A9-komunit%C4%9B-activity-7082230059276607489-l5kg/).
-   E-maily, [klubový Discord](https://junior.guru/club/).
-   Nešlo mi upgradovat stylelint na nejnovější verzi, tak jsem založil [issue](https://github.com/stylelint/stylelint/issues/7057) s chybou a komentářem, že netuším, čím to je.
    Nakonec to byl opravdu nějaký problém, který se vyřešil [novou verzí jiné knihovny](https://github.com/stylelint/stylelint/issues/7057#issuecomment-1627688725).
    Díky tomu pak [mohli upgradovat stylelint i v Bootstrapu](https://github.com/twbs/stylelint-config-twbs-bootstrap/pull/208#issuecomment-1627689125) 💪
-   Kdysi dávno jsem byl v kontaktu s Romea a nabízel jim, že rád klubem podpořím někoho, kdo by chtěl programovat.
    Bavili jsme se o konkrétním člověku, ale nakonec to nějak nedopadlo, maturoval a neměl vůbec čas.
    A teď přišel!
    Po takové době.
    Už je na vysoké, pamatoval si klub.
    Mám radost.
-   Na Hospodářkách vyšel [článek, který zmiňuje junior.guru](https://benative.hn.cz/c1-67208400-neznam-vlidnejsi-obor-nez-it-rika-byvala-ucitelka-ktere-profesni-certifikat-zmenil-karieru).
    Vím, že zmiňuje, protože mi to přišlo mailem v Google Alertu 😀
    Abych si ho přečetl, koupil jsem si kvůli tomu za pár korun na jeden měsíc předplatné.
    Ale ještě jsem to neměl čas přečíst 😀
-   Opravil jsem si vkládání obrázků do článků tady na blogu.
-   Než jsem dopsal tyto poznámky, přišla mi do mailu poptávka na [zlatý tarif](https://junior.guru/pricing/) 😮
    Nemůžu tomu uvěřit a počkám do pondělí.
    Jestli to tam v pondělí pořád ještě bude a nezdá se mi to, tak zajásám a pošlu fakturu.
-   Během 8 dní jsem naběhal 9 km. Celkem jsem se hýbal 1 h a zdolal při tom 9 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Opravit metriky na [/open/](https://junior.guru/open/) a přidat nové, abych se mohl rozhodovat, co dál.
    Zdá se mi, že mi na několika frontách klesají čísla.
    Chtěl bych se zamyslet nad svými prioritami a zaměřit se na to, co nejvíc pomůže zvrátit trend.
    Ale k tomu potřebuju nejdřív vědět, co se přesně děje a mít na to čísla a grafy.
2.  Dělat promo věcem, kterým mám dělat promo.
3.  Dopracuji anketu, kterou plánujeme s ENGETO Academy.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Jak na budování komunit s Láďou Vaškem (CzechCrunch) — ProgramHRování - váš HR průvodce světem IT](https://overcast.fm/+1O3lrq4cc)<br>Hodně dobrý! Aspoň teda pro mě, „community buildera“ :) Kdo uvažujete o komunitě, nebo nějakou už máte, tak si to pusťte.
- [(něco na Twitteru)](https://twitter.com/george__mack/status/1679569846965764096?t=jBrR3garNEhlv7V3Xp-Ybg&s=19)<br>Zajímavé vlákno. Abych nesdílel jen tak „k zamyšlení“, tak mě osobně zaujalo: 👉 The gaming industry is bigger than all music, TV, and film combined. It has out-earned music and entertainment for the last 8 years. 👉 TikTok is associated with Gen-Z by the media. But YouTube is another level: One-in-five teenagers report being "almost constantly on YouTube". 👉 There's no such thing as "mainstream media" anymore. Instead, there is "legacy media" & "new media". 👉 BRICS are now 31.5% of global GDP vs the G7's 30%.
- [Velké proměny Paříže. Chodci budou mít v dopravě prioritu, zmizí polovina parkovacích míst - Zdopravy.cz](https://zdopravy.cz/velke-promeny-parize-chodci-budou-mit-v-doprave-prioritu-zmizi-polovina-parkovacich-mist-168085/)<br>Meanwhile in Paříž
- [The LLM CLI tool now supports self-hosted language models via plugins](https://simonwillison.net/2023/Jul/12/llm/)<br>Nástroj do příkazové řádky, který vám umožní stáhnout a dotazovat jakékoliv dostupné LLM. Wow!
- [Kam se v létě 2023 vydat vlakem?](https://cestavlakem.cz/kam-se-v-lete-2023-vydat-vlakem/)<br>Tipy na cesty vlakem po Evropě. Když se připočítá čekání na letišti a cesta na a z letiště, zatímco vlaky jezdí často přímo do center měst, začíná to být skoro konkurenceschopné. Navíc se v nočním vlaku člověk prý i vyspí (vodorovně) a někdy i osprchuje. Zaujalo i toto: „Z La Spezia se dá navíc pohodlně dostat do Pisy i zbytku Toskánska a jezdí odsud i noční vlak až na Sicílii (specialitou je překonání moře přívozem, který naloží celý vlak!).“
- [🌈 The Town Hall Analogy](https://rosie.land/posts/the-town-hall-analogy/?ref=rosieland-newsletter&attribution_id=649dc3f2f3b26b000154f0d6&attribution_type=post)<br>Poučné, i pro JG: „Most people don't actually want to participate in Town Halls. They want to be served or make progress in their life. Find a job. Sign up to an event. Meet and connect with people. To see progress. To find ways to rally, support and contribute along the way. And to see problems solved. They are there because they are invested in the ecosystem and care about the space the community exists in.“
- [How bad is it to live in Czechia?](https://www.quora.com/How-bad-is-it-to-live-in-Czechia/answer/J-S-7793?ch=15&oid=320904751&share=d4e1f94b&srid=76F0&target_type=answer)<br>Zajímavá odpověď na otázku „How bad is it to live in Czechia?“
- [The Tyranny of Malcolms](https://stianstian.medium.com/the-tyranny-of-malcolms-259f3e01f17a)<br>„Let’s say the author has written a chapter arguing that that rivals make the best teams. Often nowadays they will begin the chapter with a long story about John Lennon getting in an argument with Paul McCartney, before recording a classic Beatles album, or about two rival basketball teammates, or whatever.“
