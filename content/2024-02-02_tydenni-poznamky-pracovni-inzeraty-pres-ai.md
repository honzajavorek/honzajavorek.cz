Title: Týdenní poznámky: Pracovní inzeráty přes AI
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/306
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111864126306651665

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-01-26_tydenni-poznamky-scrapery-a-openai-api.md) už utekl nějaký ten týden (26. 1. až 2. 2.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)
</div>

Ve zkratce, celý týden jsem něco programoval a pak jsem vylezl z nory a pochlubil se světu, že pracovní inzeráty na junior.guru se třídí pomocí AI 😀
Koho nezajímá to programování, bude moci velkou část dnešních poznámek asi přeskočit.
Nic jiného jsem nedělal, dokonce i klub jsem zanedbával a doháněl jej až zpětně teď v pátek.

## Kešování OpenAI API

> There are only two hard things in Computer Science: cache invalidation and naming things.
>
> — Phil Karlton

Můj týden byl ve znamení toho prvního.
Z minulého týdne jsem měl funkční prototyp toho, jak by mohlo fungovat posílání pracovních inzerátů do OpenAI API.
Protože to stojí peníze a posílám tam toho moc, důležité bylo správně kešovat výsledky.
Bohužel jsem zrovna tohle ladil většinu týdne.
A stálo to dost peněz 😀

Myšlenka byla taková, že když se budou odpovědi z OpenAI kešovat hodně dlouho, tak se bude při každém buildu na CI zjišťovat názor AI pouze na nové inzeráty, a ne na všechny.
Tím se jednak omezí počet potřebných peněz (každý požadavek na OpenAI API stojí peníze), jednak počet potřebných minut.

I když jsem se teda díval, jak dlouho trvalo ty nabídky práce původně scrapovat přímo v buildu, a průměrný čas vycházel na 20 minut.
Zatímco kombinace stažení dat přímo z Apify a pak dotazy na AI bez keše vycházela na 10 minut.
Minule jsem psal, že je to strašných 10 minut, ale v kontextu reálných dat z minulosti to je vlastně dvojnásobné zrychlení.

Prvních několik dní jsem předělával, jak funguje keš na celém junior.guru.
Používám [DiskCache](https://grantjenks.com/docs/diskcache/), ale doteď jsem to měl naplácané nějak pouze do jedné části kódu a nebylo to moc obratné.
Vytáhl jsem si to do separátního modulu a mohu teď kešovat cokoliv a kdekoliv, pomocí chytrého dekorátoru.
Když už jsem se rýpal do různých částí kódu, přidal jsem někam i [tenacity](https://tenacity.readthedocs.io/), o kterém jsem psal minule.

Když jsem myslel, že mám vyhráno, uvědomil jsem si, že na CI mi vlastně vše jede paralelně.
To znamená, že se v jednom buildu vytvoří několik paralelních keší a pak je potřeba je nějak spojit, pokud s tím chci pracovat dál.
DiskCache pracuje na bázi souborů a SQLite, takže jsem se (už zase) dostal do situace, kdy v podstatě sharduju SQLite databázi.
Koukal jsem na [jednu věc, kterou dřív zmiňoval Simon Willison](https://fedi.simonwillison.net/@simon/111054918019075740), ale zavrhl ji, protože vypadala složitě.

Na CI už nějakou hloupou implementaci slepování paralelně vzniklých SQLite databází mám.
Tím, že už jsem to jednou řešil, myslel jsem si, že to nebude zas takový problém.
SQLite jako SQLite, ne?
Jenže to problém byl.
DiskCache tam má nějaké triggery a prapodivné tabulky bez primárních klíčů (jakési „rowid“ tabulky, vůbec jsem nevěděl, že to jde), prostě samé speciality.
Na tohle moje slepování SQLite databází připraveno nebylo.
Takže jsem se s tím patlal celý jeden pracovní den, než se mi to povedlo nějak rozběhat.
Jak tu keš teď dost používám a je v ní hodně záznamů, trvá pak slučování těch databází docela dlouho, ale to budu řešit zas někdy jindy.
Povedlo se, to je důležité, hurá!

Jenže se mi pořád znova a znova posílaly všechny inzeráty na OpenAI API.
Trvalo mi docela dlouho, než jsem si všiml, že mám překlep v cestě a celá keš se mi kvůli tomu někde uprostřed buildu spláchne a nikam se nepřenese, takže se pak vše vytváří nanovo.

Pak mi Dependabot vytvořil několik Pull Requestů na dependencies a uvědomil jsem si, že i v buildech pro Pull Requesty mi to pošle všechny inzeráty na OpenAI API, jelikož každá Git větev má svou vlastní keš.
No prostě mi každý půlden jen chodil e-mail o tom, jak si OpenAI strhlo z karty dalších $5 😅
Ale na všechno jsem nakonec vykutil nějaké řešení.

## Kešování obsahu klubu

Aby mohl můj bot dělat různé věci na základě dat z klubu, stahuje si obsah celého klubu do databáze.
To bohužel nejde moc optimalizovat, protože klub je realtime Discord chat, a co byla pravda před minutou, nemusí být pravda teď.
Stažení aktuálních dat přitom trvalo i déle jak 4 minuty.

S novou keší mě ale napadlo, že by to přece jenom nějak optimalizovat šlo.
Vymyslel jsem, že když se stahují kanály a zprávy, tak by se to mohlo ukládat do keše a znova by se pak už stahovaly jen věci za posledních pár týdnů (protože lidi mohou zprávy mazat nebo editovat i zpětně, ale řekněme, že to snad nedělají pro příliš staré zprávy).

Sliboval jsem si od toho velké urychlení a pracoval na tom skoro 1,5 pracovního dne v kuse.
Hodně jsem se s tím patlal a hodně jsem debugoval nějaké problémy, které jsem následně zjistil, že byly tím, že mi nějaký cizí kus kódu upravoval datové struktury pod rukama (pomohlo [deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy)).
Udělal jsem u toho i [Pull Request do Pycordu](https://github.com/Pycord-Development/pycord/pull/2340), když jsem si v něm četl kód a našel nesrovnalosti v typech.

No a po velkém programování jsem se s tím skripem dostal na 3 minuty!
To je jako sice velké zrychlení, ale ne takové zrychlení, aby to stálo za tu komplexitu.
Jsem z toho trochu rozpačitý a nevím, jestli to vlastně celé nezahodím, jelikož to může způsobovat i problémy.
Někdy to tak ale asi prostě je, že optimalizace nakonec není zas taková pecka, jak si člověk myslí.
Možná jsem měl ten kód víc zkoumat, než jsem ho šel optimalizovat.
Třeba bych přišel na to, že úzké hrdlo je někde úplně jinde.

Tohle byla jedna z těch věcí, které neměly vůbec prioritu, ale když mě z ničeho nic napadlo, jak to řešit, neubránil jsem se a hned jsem se do toho pustil.
Měl jsem si to jen někam zapsat a nechat na později, jako to běžně dělám.
Třeba by to nějak uzrálo, třeba bych to neudělal nikdy.
Takhle jsem to sice nadšeně udělal hned, ale bylo to vlastně k ničemu.

## Pracovní inzeráty přes AI

Když jsem měl vše kolem kešování vyřešené a opravené, nahodil jsem třídění inzerátů na produkci.
Chtěl jsem to sice nejdřív nějak zkoušet a analyzovat, ale nakonec jsem si řekl, že nebudu na nic čekat a prostě to tam napálím.
Přišlo mi, že už na tom dělám věčnost a nechtěl jsem strávit další týden nějakým opatrným zjišťováním, co by se dalo ještě ladit a opravovat.

Objevilo se hned přes 20 nových inzerátů.
Z 1.200, ehm, ale takhle to holt teď s juniorníma nabídkama je…

Každopádně moje mnohaleté tažení bylo úspěšné, konečně jsem to dotáhl.
Moje předpoklady, že LLM budou vhodné přesně na tento typ problému, se ukazují jako správné.
Scrapery na Apify, třídění na OpenAI, infrastruktura kompletně zjednodušená, tuny kódu smazány jako zbytečné, a celé je to teď ve stavu, že to mohu snadno rozšiřovat a vylepšovat dál a snadno udržovat.
Zároveň mám pocit, že se mi konečně po dlouhé době podařilo udělat něco „velkého“, co reálně pomůže juniorům.

Ještě jsem to pak trochu poladil, aby se největší nesmysly vytřídily ještě předtím, než se pošlou do OpenAI, ať mi zbytečně nelítají peníze vzduchem na jednoznačně seniorní nebo nerelevantní inzeráty.
To jsem udělal po jednoduché analýze nadipsů zhruba 1.200 stažených inzerátů, díky které jsem viděl, co má smysl odfiltrovat ručně, nesofistikovaně.

Zajásal jsem si [v klubu](https://discord.com/channels/769966886598737931/789046675247333397/1201545936338436187), [na Mastodonu](https://mastodonczech.cz/@honzajavorek/111858166483999283), i [na LinkedInu](https://www.linkedin.com/posts/honzajavorek_ai-activity-7158927258647207936-ms70).
Už to je na produkci druhý den a mě to pořád stejně silně těší.
Pořád z toho mám strašně dobrý pocit!

## Oprava scraperů

Mezitím jsem zjistil, že se mi zadrhly scrapery na Apify.
Bohužel jsem to zjistil náhodou a ne díky e-mailům z Apify.
Když jsem pátral, kam e-maily zmizely, tak jsem našel v nastavení notifikací cedulku, že tahle fičura byla zrušena 😀

![Fičura zrušena]({static}/images/screenshot-2024-01-31-at-10-09-22.png)

Tak jsem jim k tomu něco napsal na Discord, protože takhle se to podle mě nedělá.
Teď mám tedy scrapery bez monitoringu, protože ani ručně nastavované alerty na Apify neumožňují nic poslat, pokud scraper selže na chybě.
Buď to nějak vrátí zpět, nebo si holt budu muset napsat skript, který to bude kontrolovat přes API.

Identifikoval jsem chyby, kvůli kterým scrapery padaly, a opravil je.
U něčeho stačilo prodloužit timeout, protože se asi po Vánocích objevil větší objem nabídek, u něčeho jsem opravoval přímo kód.

## Další

-   Měli jsme schůzi výboru Pyvce.
    Zápis [zde](https://docs.pyvec.org/operations/meeting-notes.html).
    Mám za úkol napsat advokátce a vyřídit s ní změny stanov.
-   [Luboš](https://blog.zvestov.cz/) nasdílel v klubu článek z [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/) a moc mě to zajímalo, tak jsem si to na měsíc předplatil, abych si to mohl přečíst.
    Přečtu si tam i jiné články.
    Dlouhodobě to asi odebírat nebudu, přijde mi to spíš pro lidi, co někde pracujou, a ne pro renegáta, jako jsem já 😀
-   Reklama: [Aj ty v IT](https://ajtyvit.sk/) (slovenské Czechitas) hledají někoho, koho by bavilo šťourat se v jejich Discordu a vylepšovat ho po technické stránce.
    Takže různé automatizace přes Discord API, instalace botů, apod.
    Je to na max. 20 hodin měsíčně.
    Nemusíte mluvit slovensky.
    Ideálně na fakturu.
    Není to komuniťácká pozice, obsah si řeší samy, je to spíš technická pozice.
    Pokud vás to zajímá, napište [Veronice Pizano](https://www.linkedin.com/in/veronikapizano/).
    Nebo mně a já jí to přepošlu.
-   Volal jsem si 2 hodiny s dobrým kamarádem.
    Probírali jsme jeho pohovory, moje plány, a celkově život.
-   Pavlína sestříhala jeden už dříve natočený díl podcastu a vydali jsme ho!
    [Ka­ro­li­na Sur­ma a Petr Vik­to­rin o tom, jaké jsou za­čát­ky ve fir­mě z po­hledu ju­ni­o­ra a se­ni­o­ra](https://junior.guru/podcast/20/).
    Podcast žije!
    Ještě jsem si to nestihl pustit, ale moc se na to těším.
    Vydání podcastu bylo obtížnější než obvykle, protože jsou v něm dva lidi.
    Musel jsem ve [Photopea](https://www.photopea.com/) vytvořit koláž z jejich fotek.
-   Volal jsem si s [Vojtou Mádrem](https://www.programhrovani.cz/), který mi dělá moderátora v klubu, a se kterým se vždy rád pobavím o obsahových projektech, programátorských komunitách, podcastech, a všem možném.
    Dohodli jsme se, že by mi mohl systematicky pomáhat s jednou věcí v klubu.
-   Rozjel jsem manželce [vcmi](https://github.com/vcmi/vcmi) a pak už jsem ji neviděl 😂
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Udělil jsem 2 stipendia, odpálkoval jednu firmu, domluvil si s jednou firmou kafe.
-   Za 8 dní jsem při procházkách nachodil 6 km. Celkem jsem se hýbal 5 h a zdolal při tom 6 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Vyberu a naplánuju klubové přednášky na rok 2024.
    Jako fakt už.
    Strašně to prokrastinuju!
2.  Přidám podporu pro slovenštinu do třídění inzerátů.
3.  Dám si pauzu od velkých úkolů a projdu si sloupeček v Trellu s drobnostmi, které dlouho odsunuju.
    Mohl bych taky mrknout na nějaké automatizace v klubu, které dlouho odkládám.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Google Search officially retires cache link](https://searchengineland.com/google-search-officially-retires-cache-link-437122)<br>Zendulka zvítězil. Důvod, proč si mě tehdejší děkan FIT VUT zavolal na kobereček, po 14 letech konečně zmizí. Google Cache končí!
- [Bariérou proti parkování na chodníku. Praha 6 staví zábrany za statisíce - Zdopravy.cz](https://zdopravy.cz/barierou-proti-parkovani-na-chodniku-praha-6-stavi-zabrany-za-statisice-192774/)<br>Ano prosím.
- [Peter Fabor (@faborio) on X](https://twitter.com/faborio/status/1725631676309463137)<br>Tohle je skvělý. Mapa toho, kde jsou největší turistické pasti. Podle hustoty Euronet bankomatů.
- [43. Michal Kašpárek - spisovatel — KAM JDEŠ?](https://www.buzzsprout.com/2050364)<br>Škoda, že to nemá pět hodin.
- [59: Ladislav Miko: Půda je živý organismus — 2050](https://audioboom.com/posts/8427357)<br>Fakt borec, jak to dokáže podat! Parádní povídání o půdě, jak to v ní funguje, co v ní žije, a tak. Půda mě nijak zvlášť nevzrušuje, nemám ani zahrádku, ale tohle jsem si vážně užil.
