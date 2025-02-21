Title: Týdenní poznámky: Palačinky a dohánění všeho
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/342
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/114042970633093478

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-02-14_tydenni-poznamky-schuzky-krkonose-scrapery.md) už utekl nějaký ten týden (14. 2. až 21. 2.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Své předsevzetí na rok 2025, že se naučím připravovat nějaké nové jídlo, jsem splnil o víkendu - udělal jsem poprvé v životě palačinky. Noc předtím se mi o nich zdálo, takže to bylo jasné znamení.

Dcera si prochází celý týden virózou, takže řešíme rýmičku, kašlíček, teploty. Do školky nechodí, doma rozebírá byt i naši trpělivost na atomy, a my se při tom snažíme aspoň trochu pracovat. A hlavně střídat. Přes den je příliš nemocná na to, aby s ní šlo někam jít, ale dost zdravá na to, aby řádila. A má neklidné noci, takže jsme nevyspaní a už se to na nás podepisuje.

## Apify

Scrapery fungují, „někdy“. Založil jsem [apify-sdk-python#404](https://github.com/apify/apify-sdk-python/issues/404), kde popisuju, co se děje. Debugování je ale složité a popravdě jsem na něj už neměl ani čas, ani chuť. V dejme tomu 20 % případech mi kvůli tomu padají, no tak musím vždy ráno jít a jako trdlo je restartovat tak dlouho, až projdou. Není to dobré, ale je to lepší než nic a musím se už posunout dál, jinak budu celý rok řešit jen scrapery.

V Apify jsem si pak dohodnul, že moje práce na jejich Python SDK se vezme jako kdybych pro ně dělal leden a únor [akademii](https://docs.apify.com/academy), i když jsem dělal na jiných věcech. Časově to zhruba odpovídá, hodnotu jsem dodal, akorát holt ne psaním materiálů pro kurzy. Tím jsem uzavřel nedefinovaný stav, ve kterém se moje práce poslední měsíc nacházela.

V únoru už nic pro Apify dělat nebudu, v březnu budu pokračovat standardně jedním týdnem v měsíci na akademii. Debugování scraperů nebo finišování [apify-sdk-python#403](https://github.com/apify/apify-sdk-python/pull/403) budu dělat jako něco, na co si vyhradím třeba hoďku týdně.

## Kurzy ÚP

Kromě toho opět nefungoval dobře scraper na kurzy ÚP, které stahuju, abych je mohl zobrazit ve svém [katalogu](https://junior.guru/courses/). Nevyřešil jsem to, tak jsem scraper zefektivnil. Původně bral obsah celého katalogu ÚP pro určité počítačové kategorie. Teď si scraper nejdřív zjistí jen seznam firem, pro které má kurzy stahovat. Výsledkem je zhruba 10x méně práce pro scraper.

## Pyvo

Ve středu večer jsem [zavítal na Pyvo](https://mastodonczech.cz/@honzajavorek/114032312867593195), kde byla panelovka o AI asistentech. Po skončení programu jsem se zakecal hlavně s kamarádkou Domi, kamarádem Mílou a [jedním borcem](https://www.linkedin.com/in/carmaine-falcone/), který si hledá uplatnění. Nikoho dalšího jsem nestihl, ale to nevadí. Snažil jsem se krotit a přišel jsem domů jako člověk. Ale dcera nás v noci stejně budila, takže vyspadný jsem tak jako tak nebyl.

## Další

-   Sdílel jsem [dotazník](https://forms.gle/uhaXfHKgDDRisu7Z8) o lidech, kteří to mohou mít na trhu IT práce těžké kvůli zdraví: [LinkedIn](https://www.linkedin.com/posts/honzajavorek_juniorguru-zdravaed-psychickaezzdravaed-activity-7297652024525942784-xAhK/?rcm=ACoAAACB93ABHHj4UI2winetGMZHboHlZIZojJA), [Mastodon](https://mastodonczech.cz/@honzajavorek/114025858110400887) Pokud máte 5 minut, vyplňte!
-   Opravil jsem chybu, kvůli které bot oznamoval Python srazy v klubu o hodinu špatně.
-   Konečně jsem aplikoval změny, které na nabídkách práce chtěl už před časem Red Hat.
-   Koukal jsem do Simple Analytics, zda z toho něco nevykoukám, ale nevykoukal jsem. Jen to, že na webu emimino.cz mají [dobré kariérní rady](https://mastodonczech.cz/@honzajavorek/114035803043399628)!
-   Hodinku jsem strávil tím, že lokálně mi Poetry do lockfilu nainstalovalo nějaký balíček, který se ne a ne nainstalovat na CI. Nakonec jsem to nevyřešil a prostě revertnul poslední aktualizaci dependencies.
-   Komunikoval jsem se supportem Memberful a řešil, jak přesně funguje přikupování míst pro členy u skupinových tarifů. Pak jsem se domluvil s [Lucií](https://www.dokazesprogramovat.cz/), jak to budeme dělat s jejími studenty, a vymyslel, jak budou fungovat tarify pro poskytovatele kurzů. Upravil jsem pak hned několik drobností a formulací na [ceníku](https://junior.guru/love/).
-   Nakreslil jsem na tabletu ilustraci pro [PyCamp CZ](https://pycamp.cz/). Když půjdete na ten odkaz, uvidíte to. Dan Srb pak ještě udělal nějaké čárymáry, aby to SVG zvládalo i dark mode a přepnulo se na kontrastní barvu. Paradoxně není jisté, zda na PyCamp CZ nakonec pojedu, protože mi do téhož termínu vlezlo něco jiného, co dost chci.
-   Stejné čárymáry pak Dan [udělal](https://github.com/pyvec/docs.pyvec.org/pull/407) i pro pár dalších obrázků Pyvce.
-   Zjistil jsem, že letos končí funkční období výboru Pyvce 😱 Musíme uspořádat volby.
-   Sešel jsem se na oběd s [Tomem](https://www.linkedin.com/in/tomas-votruba/) (jen tak pokecat) a na kafe s [Terkou](https://www.linkedin.com/in/tereza-vankova/) (probrat juniory).
-   Nejspíš že byl ten Valentýn, nebo nevím, každopádně Dan mi [vylepšil srdíčko na webu](https://github.com/juniorguru/junior.guru/pull/1505). Děkuju!
-   Sepsal jsem pár tipů pro lidi, kteří za Apify jedou na [PyCon Namibia](https://na.pycon.org/). Myslel jsem, že to bude pár odrážek, ale dopadlo to jako vždycky - nakonec 10.602 znaků.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Přečetl jsem většinu klubu, kde toho bylo fakt hodně, a snažil jsem se tam být tento týden aktivnější, než ty předchozí. A odpověděl jsem všem v DM. Nakoukl jsem do věcí kolem Pyvce a trochu pouklízel v [money](https://github.com/pyvec/money/).
-   Za 8 dní jsem při procházkách nachodil 3 km. Celkem jsem se hýbal 1 h a zdolal při tom 3 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Doplánovat si věci kolem junior.guru, dotřídit si poznámky, rešerše, úkoly.
2.  Připravit seznam benefitů pro prodejní stránku klubu.
3.  Sepsat na blog svůj plán na letošek, nebo aspoň Q1-Q2.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [LibreWolf](https://librewolf.net/)<br>Neznal jsem. Prohlížeč založený na Firefoxu, ale pro lidi.
- [Marshmallow Test and Parenting - @desunit (Sergey Bogdanov)](https://desunit.com/blog/marshmallow-test-and-parenting/)<br>„If you’re a kid and the adults in your life constantly break promises, why would you trust them this time? Why wait for the second marshmallow if history tells you it might not show up?“
- [A year of uv: pros, cons, and should you migrate](https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should)<br>Hezké zhodnocení toho, jestli má smysl přejít se svými Python projekty na uv
- [XScreenSaver: Google Store Privacy Policy](https://www.jwz.org/xscreensaver/google.html)<br>Lol, tak tohle je moc hezké splnění požadavku na “privacy policy” 😀
- [Kvíz české diplomacie](https://dobronebozlo.cz/)<br>Tohle je skvělé. Teda skvělé to není, ale je to skvělý nápad, jak přenést myšlenku, a je to skvěle vytvořené.
- [Vrtěti bydlením - David Klimeš](https://davidklimes.cz/newsletter/223)<br>„Splnila vláda lhaní v oblasti dostupného bydlení na 80, 90 či snad dokonce 100 procent? Bude kolegium ministra financí sestavené z lobbistů ze 100 procent či jen z 90?“
- [Jak se ostravský lidovec stal průkopníkem boje proti menstruační chudobě v ČR – Page Not Found](https://pagenotfound.cz/clanek/jak-se-ostravsky-lidovec-stal-prukopnikem-boje-proti-menstruacni-chudobe-v-cr)<br>V Ostravě měli jako první pípání kreditkou za cestu tramvají, teď mají jako první plošně dostupné menstruační potřeby na školách 👏 Kdo ví, jestli se podobné vymoženosti jednou dostanou i do Prahy.
