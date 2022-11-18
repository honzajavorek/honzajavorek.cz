Title: Týdenní poznámky #85: Březnových 300 km na kole a spousta práce
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (1.3. — 25.3.) a tak [stejně jako minule]({filename}2022-02-28_tydenni-poznamky-84-akce-v-klubu-a-ukrajina.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tak tentokrát zase po delší době. Říkal jsem si, že napíšu poznámky až těsně před dovolenou. To jsem nestihl. Po dovolené zas bylo pořád co dělat, takže nakonec to píšu až dnes. Vím, že to slibuju v poslední době pokaždé, ale polepším se! Chtěl bych se nějak fakt vrátit k týdennímu rytmu.


## Robot na nabídky práce

Jak jsem psal dříve, jsem teď v procesu překopávání robota na stahování nabídek práce, protože jsem na něm dlouhodobě neřešil různé nedostatky a postupně to celé uhnilo, až se to jednoho dne prostě rozpadlo.

Těžko říct, zda tady detailně popisovat vše, co jsem na tom udělal a jaké myšlenkové pochody se mi při tom honily hlavou. Zkusím to nějak stručně, ale i tak, jde o skoro měsíc práce:

- Navrhoval jsem nové modely. Nakonec mám zvlášť modely pro nabídky stažené odjinud a nabídky zadané na samotném JG. Pak mám ještě třetí model, který se tvoří z těch dvou a slouží pro nabídky, které se mají zobrazit na webu, případně na Discordu.
- Z rozdělení modelů na několik a jednotlivých skriptů na spoustu oddělených fází jsem zatím nadšený. Je teď mnohem jasnější, kdy se má co dít a je to i efektivnější, protože se věci mohou dít jen tehdy a jen pro ta data, kdy to má nějaký význam. Je rozdíl, jestli spouštím geolokaci nebo stahování obrázků pro 300 nabídek, nebo jen pro těch 30, které nakonec chci zobrazit na webu.
- Do robota jsem vrátil vyhodnocování juniornosti nabídky. To se dělá přes spoustu regulárních výrazů a jednou by to měl dělat machine learning, ale zatím jsem se snažil jen překlopit to, co bylo, do nové architektury a nesahat na to moc.
- Změnil a zjednodušil jsem řazení nabídek práce na webu.
- Zrušil jsem admina. Byly to statické stránky na „tajné“ adrese, s vygenerovanými informacemi o tom, co vše robot uložil nebo vyhodil. V patičce bylo napsáno, že pokud nejste administrátor stránek, tak máte odejít pryč :D Zabezpečení, které doteď stačilo. Do budoucna místo toho plánuji využít nějak [Datasette](https://datasette.io/) pro nahlížení do produkční databáze a zároveň si posílat nějaké statistiky přímo na Discord.
- Pracoval jsem na tom, abych dokázal efektivně určovat lokaci k nabídkám práce. To už v původním robotovi bylo, ale teď jsem to musel trochu předělat. Velké zlepšení je, že lokaci stahuji jen k nabídkám, u kterých ji potom fakt využiju.
- Zjistil jsem, že když bylo umístění pracovní nabídky „Czechia“, „Česko“, apod., tak si s tím můj geocoding neporadil a udělal mi z toho Číhošť v Jihlavském kraji. To by vysvětlovalo, proč bylo v Číhošti tolik nabídek. Opravil jsem to.
- Povedlo se mi dotáhnout překopávání robota až k tomu, že jsem konečně dokázal nabídky zobrazit i na webu. To byl skvělý pocit, po měsících koukání do terminálu konečně vidět ta data i v HTML.
- Pracoval jsem na tom, abych dokázal efektivně stahovat loga k nabídkám práce. To už v původním robotovi bylo, ale teď jsem to celé změnil tak, aby se to dělalo jen pro těch pár nabídek, které chci fakt ten den zobrazit, a aby to bylo celé rychlé a efektivní. Myslel jsem, že na to použiju Scrapy a [Media Pipeline](https://docs.scrapy.org/en/latest/topics/media-pipeline.html), ale nakonec jsem si to udělal úplně ve vlastním skriptu a funguje to perfektně. Žádná data už neukládám do EXIFu, což jsem v Media Pipeline dělat musel, abych tím cosi obešel. Smazal jsem spoustu složitostí. Skvěle do toho zapadlo i hledání faviconů, pokud logo firmy nemám k dispozici. Algoritmus, který vybírá nejvhodnější logo z různých kandidátů, na ten jsem vyloženě hrdý. Skoro jako něco z Advent of Code.
- Zajistil jsem, aby i po všech změnách fungovalo správně API, které jsem dříve vyrobil pro Czechitas. Udělal jsem v něm ale nějaké změny v tom, jak funguje, abych měl život jednodušší. Oznámil jsem je druhé straně a vše bylo přijato jako že to je v pohodě, takže paráda.
- Vyhodil jsem z webu sledování počtu klikání na tlačítka na nabídkách práce přímo na JG. Čísla se posílala inzerentům v mailech. Měřilo se to přes Google Analytics eventy a myslel jsem, že to předělám na [Simple Analytics](https://simpleanalytics.com/junior.guru) eventy. Jenže pak jsem na to nějak neměl náladu a řekl jsem si, že to zkusím prostě smazat a když si inzerenti nevšimnou, tak to bude prostě smazané :D Mě to chybět nebude. Běžné statistiky návštěvnosti mít budou a počty „kandidátů“ stejně ví nejlépe oni sami a ne já z toho, co pochybně naměřím JavaScriptem na webu. Díky tomuto kroku jsem mohl už definitivně z kódu smazat vše kolem Google Analytics.
- Posílání emailů inzerentům jsem přesunul do fáze „synchronizace“. Původně byly fáze „fetch“, kde se stahovaly data a „send“, kde se posílaly emaily. Toto už ale dávno neplatí, „fetch“ se změnilo na „sync” a dělají se tam i věci, které něco posílají, třeba do Discordu. Takže je zbytečné, aby emaily byly někde bokem. Potřeboval jsem ale zajistit, aby se nikdy neposlaly dvakrát. Takže si do txt souboru vždy uložím, kdy se poslaly naposled a dávám to do CircleCI cache, aby to přežilo mezi buildy.
- Zatím jsem úplně odstranil monitoring toho, zda se při scrapování nebo zpracovávání inzerátů něco pokazilo. Taky jsem vrátil jen zlomek původních testů a nenapsal skoro žádné nové. Nepočítám s tím, že to dodělám, než všechny změny mergnu. Udělám to později, protože už teď bude i tento nemonitorovaný kód mít lepší výsledek, než co dělá bot na produkci teď, i kdyby v tom byly chyby. _What could go wrong._
- Přešel jsem od Makefile k [invoke](https://www.pyinvoke.org/) a změnil jsem podle toho některé komentáře a dokumentaci. Ne že bych teda nějakou dokumentaci velmi měl.
- Zjistil jsem, že ačkoliv jsem vše udělal paralelní a konkurentní a na fáze a super efektivní, tak stahování nabídek práce z nejmenovaného serveru, říkejme mu třeba LI, stejně zabere strašně moc času. Prostě klidně půl hodiny, hodinu. A to proto, že to stahuju skrze nějaké náhodné proxy, jelikož rozsah IP adres, v němž se nachází moje CircleCI buildy, zřejmě apriori blokují (z domova mi to normálně funguje i bez proxy). No a s tím se nedalo nic moc dělat, než to ladit, ladit a ladit. Našel jsem jiný zdroj těch proxy (místo scrapování [free-proxy-list.net](https://free-proxy-list.net/) jsem našel API na [proxyscrape.com](https://docs.proxyscrape.com/)), zkoušel různé timeouty, různé strategie, různé rotování, atd. Nakonec jsem to nějak vyřešil, chybou bylo mít krátký timeout, abych roztřídil proxy, které fungují, od těch, které nefungují. Zdá se, že větší timeout je lepší, protože může trvat třeba 10-15s první připojení, ale pak už to frčí rychle. Pak stačí nějaký inteligentní algoritmus vybírání těch proxy a vypadá to, že ze 40 minut jsem na 10 minutách. To je naprosto zásadní, protože pokud bych toto nevyřešil, tak nemá smysl nového robota vůbec nasazovat, nebo se později pouštět do přidávání dalších zdrojů nabídek práce.
- Poslední dva dny ladím různé chyby, které se postupně objevují a stojí v cestě tomu, abych to celé poslal už na produkci. Sem tam nějaký edge case, sem tam nějaká exception. Ale už mi to i celé prošlo a build byl zelený, ladím už fakt jen detaily.
- Žongluju ještě s přesným nastavením cache na CircleCI a toho, jak jdou věci za sebou. Třeba jsem zjistil, že když má cache stejný klíč, tak se nepřepíše, ale zahodí, jakože už existuje. To mi udělalo čáru přes rozpočet. Ale pak jsem zjistil, že `restore_cache` umí obnovit podle prefixu klíče, ne jen podle celého klíče, a tím jsem to zase vyřešil.

Jen poznámka. Celý robot je věc, která mi negeneruje žádné peníze. Ano, využívám to jako backfill inzerátů na svůj portál s nabídkami práce, kde firmy inzerují za peníze, tzn. je tam pak třeba 5 placených inzerátů a 30 stažených odjinud, aby to nevypadalo blbě.

Jenže ty placené inzeráty mě živí teď minimálně, reálně je to 2-5 % mých příjmů. Takže kvůli tomu to fakt nedělám. A i kdyby, existuje samozřejmě deset jiných zdrojů nabídek práce než LI, kde je stáhnu prakticky bez práce. Nemusel bych ani řešit žádné velké objemy nabídek, prostě bych jich stáhl pár, třeba deset.

Dělám to celé ze stejného důvodu, jako třeba příručku. Má to být služba juniorům. Chci, aby měli místo, kam můžou jít a budou vědět, že tam jsou pouze juniorní nabídky práce, ze všech běžných zdrojů, kde by je stejně hledali. To je můj primární cíl do budoucna. Služba juniorům, usnadnit jim hledání práce. Zároveň se nabídky propisují nejen na web, ale i do klubu, takže se dá říct, že je ten robot součástí produktu „klub”, nabídky tam lidem chodí díky tomu až pod nos, což dělá z klubu zas o něco užitečnější místo.

Takže byť moje konání vypadá nesmyslně, příliš mnoho práce pro nic, tak bych chtěl upozornit, že totéž se dá říct o příručce (příliš pracného psaní pro nic), ale holt to jsou vlastně ty hlavní věci, které chci tvořit, dát světu zdarma k dispozici, a které mi má pomáhat klub financovat.


## Pyvec

Výbor [Pyvce](https://pyvec.org/) dosluhuje. 4 lidi z 5 (kromě mě) tu práci dělají 10 let. Já 5 let. Tak tak jsme to dokázali doklepat do voleb, v posledních týdnech nám upřímně dělalo problém se i sejít na videohovoru a připravit samotné volby.

Nakonec nás zahchránili samotní členové na Členské schůzi. Vzali si různé úkoly, které nám pomohly volby uspořádat. Bylo to strašně super najednou vidět všechny aktivně něco dělat a spolupracovat. Taky Pyvec Slack zase po dlouhých covidových měsících (rocích?) trochu ožil.

Před volbami jsem oznámil, že budu do příštího výboru kandidovat jen pokud dostanu aspoň tři nominace, což se následně i stalo. Sepsal jsem i své nominace pro lidi, kteří si myslím, že jsou do výboru vhodní. Nakonec budeme volit 5 lidí z 6 kandidátů! Takže to bude i napínavé :)

Po vzoru PSF nakonec hlasujeme přes [Helios](https://vote.heliosvoting.org/). V současné chvíli se hlasuje, volby jsme udělali tak, aby trvaly týden a odhlasovat měl šanci opravdu každý. Jsem zvědavý, jak to dopadne.


## Kupóny pro studenty z kurzů

Některé vzdělávací agentury mi posílají své studenty do klubu s tím, že jim proplatí první 3 měsíce členství. Ze začátku to drhlo a moc jich nechodilo, ale teď se to nějak rozjelo a už dávno jsem to měl fakturovat. A když jsem se o to pokusil, tak jsem si uvědomil, že abych mohl fakturovat, potřebuji si někde poznačit, koho jsem už vyúčtoval a koho ne a že to není v mé současné evidenci tak triviální, jak jsem myslel.

Napsal jsem na support Memberful, jestli je možnost přes API vytáhnout privátní poznámku u členů, ale nejde to. Mají ovšem nějaké jiné políčko, kam jde něco uložit, bohužel k němu není zase UI, takže bych si to tam musel poznačit nějak přes to API, tedy asi přes nějaký skript. Vymýšlením řešení jsem strávil skoro celý jeden den.

No nebude to jednoduché a zatím jsem pouze napsal do agentury e-mail, že na tom dělám a jaký je přibližný stav, a že se ještě ozvu. Aby to nebylo dlouhé mlčení a pak najednou buch, velká faktura. Odložil jsem to a budu to řešit, až dořeším robota na nabídky práce.


## Dovolená

S kamarádem [Mílou](https://milavotradovec.cz/) jsme se relativně spontánně rozhodli, že pojedeme na kole 300 km, z Prahy do [Kozojedského dvora](https://www.facebook.com/kozojedsky.dvur.nitkovice/), kde jsem měl svatbu a rád se tam vracím. Takové cesty jsem dřív už absolvoval v nejrůznějších podobách a délkách, ale vždy v létě. Teď to mělo být v březnu a měla být dost zima. Rozhodli jsme se pro _credit card touring_ místo stanu, ale i tak byl oříšek zabalit se tak, abychom zvládli zimu a vítr. Naši cestu jsme dokumentovali [polotajným deníkem na Twitteru](https://twitter.com/300ukozojed).

Twitter jsme zvolili jako něco, kam lze psát, dávat obrázky a videa, co je veřejné a co můžeme dát kamarádům a rodině, aby věděli kde jsme. Bohužel Twitter už dnes veřejný není, což jsme si neuvědomili. Všichni si stěžovali, že po přečtení pár tweetů to po nich chtělo založit účet. Kde jsou naše staré dobré internety, na které člověk něco napsal a druhý si to mohl přečíst? :(

Dovolená to byla náročná, ale jedním z účelů bylo vyčistit si hlavu. Na klasické dovolené, kde se člověk fláká, mi trvá týden, než přestanu myslet na práci. Na takovýchto náročných cestách se mi líbí, že vyčištění hlavy zabere většinou nanejvýš pár hodin prvního dne.

Cesta se i přes různé nesnáze povedla a v cíli jsme dokonce zahráli na kytaru lidem z Ukrajiny, kteří byli na dvoře nouzově ubytovaní, takže to bylo takové hezké. Hlavu jsem si vyčistil. Zdravotní následky snad žádné permanentní mít nebudu :D

Po dovolené jsem měl 20+ notifikací na FB, 10+ na Twitteru, 20+ notifikací na LinkedIn, 80+ emailů. V klubu toho taky bylo dost, ale nebylo to nakonec tak hrozné, protože ještě trval útlum aktivity po tom, co začala válka na Ukrajině. Všechno jsem nějak dohnal více méně za jeden den, takže se to dalo.

Horší to bylo s fyzickým vyčerpáním, které mi zabránilo po příjezdu do Prahy doplazit se na první [pražské Pyvo](https://pyvo.cz/), které se po dlouhé době konalo živě a ne online.


## Další poznámky

- Účastnil jsem se mezikomunitního sdílení, probírali jsme mentoring. Přínosné!
- Oslovil jsem svého účetního, že bychom měli udělat daňové přiznání. Během několika týdnů jsem mu postupně posílal různé podklady. Dnes mi poslal hotové přiznání do mailu, ale ještě jsem to neodevzdal. Přidal jsem do [grafu výdajů](https://junior.guru/open/) barvičku na účetnictví, ať mám trochu přehled, kolik mě vlastně relativně k ostatním věcem externí zpracovávání daní stojí. Dělat se mi to ale fakt nechce, takže je to spíš orientační, outsourcoval bych to za každou cenu :D
- Zřídil jsem si datovou schránku, abych mohl daňové přiznání poslat digitálně. Doteď jsem datovku neměl a přiznání posílal jako papír v obálce, ale začíná to být těžší, než datovku mít a papíry neposílat. Díky MojeID mám jakou si tu eIdentitu občana, nebo jak se to jmenuje, takže to bylo na dva kliky, což mě překvapilo. Myslel jsem, že budu muset jít na poštu. Dostal jsem radu, že jako OSVČ vše vyřídím i pouze s osobní datovkou, tak jsem si zřídil jen tu a tu podnikatelskou ne. První dojmy z datovky jsou spíš pozitivní. Možná jsem nemusel být takový zpátečník tak dlouho.
- Vydal jsem nový díl podcastu. Pája jej nahrála včas, ale já byl na dovolené, tak to vyšlo později, než to vyjít mělo. Svět se nezbořil.
- Propojil jsem Páju s dalším hostem do podcastu. Funguje nám to skvěle. Pája nadhodí téma nebo charakteristiku někoho, koho by si ráda pozvala. Já pak sáhnu do paměti a do své široké sítě kontaktů a vytáhnu nějaké vhodné kandidáty, ze kterých si vybere. Nebo přijde i s konkrétním jménem a já je můžu aspoň propojit, protože toho člověka znám a hned je vše jednodušší :)
- Domlouval jsem další přednášky v klubu, které přijdou po delší pauze. Jedna by měla být o práci na dálku, druhá o Next.js. Poprvé se stane, že se zopakuje speaker.
- Na MDŽ jsem hejtil [na Twitteru](https://twitter.com/honzajavorek/status/1501136417723928582) i [na Facebooku](https://www.facebook.com/groups/967870373283278/posts/7058376260899295/) fakt, že je v Česku nejmenší procento žen v IT vůbec v Evropě.
- Domlouval jsem si call s firmou, která projevila zájem o firemní členství v klubu.
- Vyšly se mnou hned dva podcasty, kde jsem byl hostem. [Rozbité prasátko](https://rozbiteprasatko.cz/) a [ProgramHRování](https://www.programhrovani.cz/). Zatím jsem ani jedno nestihl pořádně zpropagovat na svých sociálních sítích.
- Přidal jsem na web nahoru lištu, která poukazuje lidi na web [stojimezaukrajinou.cz](https://www.stojimezaukrajinou.cz) od Česko.Digital. Není to nic světoborného, ale třeba to někdo uvidí, třeba na to klikne a třeba díky tomu někomu pomůže. Barvy jsem na ukrajinské změnit nemohl, protože JG už žluté a modré dávno je :)
- Řešil jsem různé náhodné problémy s členstvím, tu něco s kartou, tam nějaký dotaz ohledně placení a tak. Zase se mě někdo ptal, jestli může za klub platit i jinak, než kartou. Nemůže. Musím to dát už do FAQ, ať to nekopíruju a nesepisuju pořád dokola.
- Připojil jsem se na první sraz dobrovolníků nové komunity pro _technical writers_, [TWguild](https://www.twguild.cz/). Dávali jsme si vědět, jak se můžeme vzájemně podpořit.
- Dostal se ke mě kontakt na kluka, který je v ideálním kandidátem na stipendium, jež jsme chtěli už dlouho rozjet s Mews. Dokopal jsem se tedy konečně k tomu, abych připravil formulář na žádost o stipendium a dal ho na třetí tlačítko dole na [stránce klubu](https://junior.guru/club/). Nehledě na formulář jsem si s klukem a jeho tátou zavolal a ještě si to musím nechat potvrdit z Mews, ale myslím, že je podpoříme. Kromě kluka už to vyplnili další dva lidi, které budu muset nějak ještě vyhodnotit.
- Chtěl jsem ten videohovor udělat klukovi jednoduchý, tak jsem svolil k použití MS Teams, které má ve škole. Stejně s tím občas chtějí volat i některé firmy, tak jsem si říkal, že si v tom udělám pořádek. No řeknu vám…! Už dlouho jsem takhle nenadával. To je tak strašná aplikace. A Microsoft mi udělal účet ze Skypu a ještě z čehosi. Prostě udělat si v těch účtech pořádek a zalogovat se do těch Teamsů a nepřijít u toho o nervy, to bylo fakt něco. Hodina života. Pak že musím mít nastavený telefon. Ale z MS Teams aplikace mi to neposlalo kód. Musel jsem jít na web a nechat si to poslat tam. A takové… No ještě teď z toho teču.
- Měla mi po třech letech vypršet [InKarta](https://www.cd.cz/jizdne/in-karta/default.htm), tak jsem si ji koupil na další tři roky přes aplikaci Můj vlak. Překvapilo mě, že to bylo na dva kliky, Apple Pay, cink, hotovo. Dřív se muselo na nádraží pro plastovou kartičku :D
- Volal jsem si s paní ze systému na evidenci dodavatelů jedné korporace, aby ověřili, že já jsem já. Zmátlo je, že neplatím DPH, nebo že neexistuje žádný jiný zaměstnanec mé firmy, který by mohl potvrdit mou existenci. Tak snad už proplatí fakturu a bude to konečně hotovo. Tihleti korporáti, to je někdy fakt za trest. Asi zavedu, že firmy level korporát budou mít ceník o 10k dražší jen z toho titulu, že vyžadují zbytečnou byrokracii a komunikaci.
- Syn partnerky bratrance mé ženy potřeboval doučit HTML do školy, tak jsem ho přidal do klubu. Jsem zvědav, jestli to bude efektivní pomoc, nebo to bude k ničemu.
- Procházel jsem pravidelně klub, vítal nové členy, odpovídal na věci. Prošel jsem v klubu jedno CVčko, ohodnotil nějaké výrobky…
- Možná budu přednášet na příštím [pražském Pyvu](https://pyvo.cz/) a možná tam bude i Pája s lightning talkem o podcastu.
- Nastříhal jsem verzi přednášky s Nelou o duševním zdraví, kterou budeme chtít uveřejnit na web a poslal to Nele na kontrolu. iMovie FTW, vždycky si připadám jak Spielberg u toho.
- S dvěma firmami nejspíš brzo doklepneme partnerství a vyměňuji si s nimi tedy dost mailů.
- Opravil jsem skript, který lidem v klubu přiděluje role. Měl jsem na jednom místě špatné slovo, spouštěl se ve skutečnosti úplně jiný skript (naštěstí zrovna nějaký neškodný).
- Knihovna [py-cord](https://pypi.org/project/py-cord/) začala vydávat už nějaké pre-relase verze, tak jsem přešel z instalace z gitu na instalaci z PyPI. Pak jsem si dokonce všiml, že se snad obnovil i vývoj na původním [discord.py](https://pypi.org/project/discord.py/), ale to jsem nějak nestihl zatím prozkoumat.
- Povedlo se mi značně zrychlit začátek buildu na CI díky tomu, že jsem nastavil git clone na shallow clone. Pomohla mi tato [diskuze](https://discuss.circleci.com/t/checkout-is-taking-way-too-long/39787/2) a využil jsem [tento CircleCI Orb](https://circleci.com/developer/orbs/orb/guitarrapc/git-shallow-clone).
- Mergoval jsem spoustu PR s upgrady knihoven na Pyvec repozitářích od [dependabota](https://github.com/features/security).
- Sekalo se mi VS Code a už jsem toho měl plné zuby, tak jsem hledal, jak to můžu zrychlit. Našel jsem [tenhle článek](https://mikebifulco.com/posts/make-vs-code-load-faster-mac-apple-silicon) a zjistil, že z nějakého důvodu nemám verzi VS Code pro M1, ale Inteláckou. Tak jsem to přeinstaloval, updatoval systém, restartoval. A už dobrý.
- Pár firem inzerovalo nabídky práce přímo na JG, takže jsem díky tomu poslal pár faktur.
- Flákal jsem dost sociální sítě, protože jsem na ně neměl moc náladu (válka, dovolená). Párkrát se mi ale něco postnout povedlo: oznámení o ukrajinské liště na webu, spolupráce s [Jetveo](https://jetveo.io/cs/blog/articles/jakub-interview), nový díl [JG podcastu](https://junior.guru/podcast/) nebo o tom, že o podcastu napsali v tištěném časopise Computer.
- Podepsal jsem smlouvu se Seznamem, aby mohli dát náš podcast na [podcasty.cz](https://podcasty.cz/). Zatím to tam myslím ale není.
- Během 25 dní od 1.3. do 25.3. jsem při procházkách nachodil 40 km, na túrách nachodil 10 km, ujel na kole 370 km. Celkem jsem se hýbal 63 hodin a zdolal při tom 420 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Dokončit bota, který stahuje a třídí pracovní nabídky.
2. Řešit lidi, kteří žádají o stipendium.
3. Podat daňové přiznání.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Skatepark Vltavská – skvělé využití veřejného prostoru, které nestojí majlant](https://www.mall.tv/gebrian-plus-minus/skatepark-vltavska-skvele-vyuziti-verejneho-prostoru-ktere-nestalo-majlant)<br>Tohle je super, že to někdo zrealizoval!
- [Místo s tak krásnou atmosférou by na Národní třídě čekal jen málokdo](https://www.mall.tv/gebrian-plus-minus/tak-krasnou-atmosferu-by-na-narodni-tride-cekal-jen-malokdo)<br>Krása! A ty studny, to je boží :D
- [Ruská společnost v drtivém sevření. Morální apely na tamní opozici jsou naivní](https://a2larm.cz/2022/03/ruska-spolecnost-v-drtivem-sevreni-moralni-apely-na-tamni-opozici-jsou-naivni/)<br>Co se právě teď ďeje v Rusku? Děje se tam něco? A co se tam teprve dít bude? Jsou Rusové schopni svrhnout Putina? Jak vnímají sankce?
- [A no-fly zone in Ukraine will backfire](https://unherd.com/2022/03/a-no-fly-zone-in-ukraine-will-backfire/)<br>Proč by No-Fly Zone nad Ukrajinou jednak vyústila akorát v eskalaci konfliktu, jednak nic nevyřešila.
- [Válka na Ukrajině je sousto, kterým se Putin zadáví, říká politolog Barša](https://a2larm.cz/2022/02/valka-na-ukrajine-je-sousto-kterym-se-putin-zadavi-rika-politolog-barsa/)<br>Baršu si vždycky rád přečtu.
- [Bezletová zóna nad Ukrajinou už nemůže být tabu – řešení existuje](https://www.forum24.cz/bezletova-zona-nad-ukrajinou-uz-nemuze-byt-tabu-reseni-existuje/)<br>Zajímavý nápad.
- [What If Russia Loses?](https://www.foreignaffairs.com/articles/ukraine/2022-03-04/what-if-russia-loses)<br>„Nobody inside or outside Russia should want Putin to win his war in Ukraine. It is better that he lose. Yet a Russian defeat would offer little cause for celebration.“
- [Kým je Putin z pohledu mezinárodního práva? A kdy za zločiny odpovídá voják? Vysvětluje expertka](https://denikn.cz/825574/kym-je-putin-z-pohledu-mezinarodniho-prava-a-kdy-za-zlociny-odpovida-vojak-vysvetluje-expertka/?cst=d2d0a5d9e866ef1a6e3493dfad738501a78d74ab)<br>Ujasnění pojmů. Agrese, genocida, kdo má vlastně zodpovědnost a za co?
- [Jak blízko jsme rozštěpení Internetu?](https://blog.nic.cz/2022/03/08/jak-blizko-jsme-rozstepeni-internetu/)<br>Může mít Rusko svůj internet?
- [Vedle raket i propaganda, aneb moderní konflikt neprobíhá jen na frontě](https://markething.cz/rusko-ukrajinsky-konflikt)líbí. Ukrajinský prezident je hvězda, vojáci na ostrově, atd., to vše drží morálku a vzbuzuje sympatie na Západě. Ukrajina si buduje mýtus, aby se ubránila. Nedělejme si však iluze, že nejde o propagand. Aspoň novináři a média by nemuseli „posílat dál“ úplně cokoliv jako zaručenou věc…
- [Kamil Galeev](https://mobile.twitter.com/kamilkazani/status/1498377757536968711) hotový rychleji, než by mi bylo milé, ale tak zas je to jen Twitter, ne kniha. Je zajímavé si to po večerech pročítat.
- [How did Russia get so big?](https://kamilkazani2.substack.com/p/how-did-russia-get-so-big?s=r)<br>Nesmírně zajímavá historie rozšiřování Moskevského státu.
- [The Next 10 Days Will Decide This War](https://cepa.org/the-next-10-days-will-decide-this-war/)<br>Co si myslí bývalý americký generál o situaci na Ukrajině.
- [Vysílač](https://overcast.fm/+lh3KUU0wU)<br>Přehlcenost sociálními médii. Jak bojovat s instant gratification monkey? A je vlastně doomscrolling problém? Jde mozek přeučit, nebo je to už problém na vždy?
- [How our free plan stays free](https://tailscale.com/blog/free-plan/)<br>Upřímnost, která se jen tak nevidí. Kéž by víc startupů bylo schopno popsat svůj byznys takhle, bez bulšitů.
- [U budoucích ajťáků je nejdůležitější touha nespokojit se s prvním řešením, říká lektor programování pro děti](https://www.heroine.cz/zeny-it/7677-u-budoucich-ajtaku-je-nejdulezitejsi-touha-nespokojit-se-s-prvnim-resenim-rika-lektor-programovani-pro-deti)<br>Luboš píše na Heroine! Jak je to s programováním a dětmi?
- [Geopolitika bitcoinu. Kde se těží hlavní kryptoměna světa?](https://finmag.penize.cz/penize/432670-geopolitika-bitcoinu-kde-se-tezi-hlavni-kryptomena-sveta), což vedlo kolem roku 2016 ke skutečnému kryptoměnovému boomu.“

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
