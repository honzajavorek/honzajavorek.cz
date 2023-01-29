Title: Týdenní poznámky #111: Kamarádi z Afriky
Image: images/praha-vecer.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/15


Utekl zase nějaký ten týden (5.11. — 11.11.) a tak [stejně jako minule]({filename}2022-11-04_tydenni-poznamky-110-zapaseni-s-ci-prednaska-zlin.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Praha večer]({static}/images/praha-vecer.jpg)


Drtivou většinu týdne jsem trávil tím, že jsem se věnoval [kamarádům z Afriky]({filename}2021-06-17_jessica-upani-about-python-events-in-namibia-you-have-to-be-pure-in-terms-of-your-why.md), kteří do Prahy přijeli na [Ubuntu Summit](https://events.canonical.com/event/2/). Jeden večer jsme zařídili večeři, další večer jsme jim udělali zážitkovou prohlídku noční Prahy. Spousta organizačních věcí, někdo si zapomněl doma nabíječku a kupoval jsem rychle nějakou v Alze, někdo potřeboval invalidní vozík, spousta přesunů, apod., takže velká divočina. Měl jsem mít přes týden i nějaké schůzky, ale (aby organizace všeho výše nebyla moc jednoduchá), různě se přesouvaly nebo rušily.

![Kámoši z Afriky]({static}/images/afrika-kamosi.jpg)

[Muheue](https://twitter.com/muheuenga) zůstal ještě o den déle, tak jsme mu udělali i denní prohlídku Prahy a protože vyšlo krásně počasí, bylo to fakt super. Můj kamarád, který prohlídky dělal, to měl dost vymakané a já sám jsem někdy čuměl, co pěkného v tom Starém Městě nebo na Malé Straně vlastně je a co vůbec neznám. Můj osobní _highlight_ byli Maltézští rytíři a jejich areál. Máme spoustu nádherných zážitků a fotek a dojemných, dobrodružných i vtipných situací. Já osobně z toho mám i velký spánkový deficit. Ale myslím, že se to celé moc pěkně vydařilo.

![Na Vítkově]({static}/images/afrika-vitkov.jpg)


## Spojování databází

Chtěl jsem vytvořit nějaký mechanismus, který mě upozorní, kdybych náhodou přepisoval data ve stejném sloupci ve stejné tabulce. Dovedu si představit, že jak vytvářím paralelní SQLite databáze a pak je po paralelizaci spojuji, tak by mohla vzniknout nepříjemná chyba z nepozornosti, kterou bych pak hledal hodně dlouho.

Nakonec jsem se rozhodl vůbec nepoužít `.insert_all()` nebo `.upsert_all()` z [sqlite-utils](https://sqlite-utils.datasette.io/), ani nepsat nějaké šílené SQL, se kterým bych zápasil celý den. Prostě jsem to napsal v Pythonu. Řádek po řádku kontroluje, co se přesně děje a řádky sloučí, nebo vyhodí chybu, pokud nastane situace, kdy bych měl přijít o nějaká data. Výkonnostně to, zdá se, nepředstavuje žádný problém a navíc mohu všechny situace transparentně logovat i testovat a nemusím se spoléhat na to, že jsem správně pochopil nějaký složitý SQL konstrukt, a to ještě v SQLite dialektu.

Hned mi to našlo chybu. Zapisoval jsem do tabulky s lidmi, kdy se registrovali na Discord. Potom jsem tam ale zapisoval znova, pokud jejich registrace na Memberful byla dřív. Spíš než že by mě to omezovalo, přišlo mi, že to nemám vlastně dělat. Že motám dvě věci dohromady a je to spíš _code smell_. Přepracoval jsem tedy tuto část kódu a v tabulce jsou nyní dva různé sloupce s různou sémantikou a používají se v různých případech.

Slučování databází teď podle mě funguje dobře a bezpečně. Jediné, co neumím, je smazat věc. Kdyby jeden skript nastavil nějakou hodnotu v záznamu v tabulce, tak další skript ji nemůže přepsat `NULL` hodnotou. Slučování totiž nedokáže rozeznat, zda je tento `NULL` záměrný, nebo je to důsledek toho, že se prostě slučuje databáze, ve které nejel skript, který by danou hodnotu naplnil. Snad to nebude ničemu vadit, aktuálně to nikde nepotřebuji.


## Posílání mailů

Zjistil jsem, že maily se neposílají správně, protože se informace o jejich poslání ukládá do souboru a slučování souborů po paralelizaci funguje tak, že soubory stejného jména se nepřepisují, nikdy se soubor neaktualizuje a neuloží se nová informace co CircleCI keše, což by mělo zajistit perzistenci.

Přepracoval jsem, jak se slučují soubory. Porovnávají se a když jsou stejné, tak se tiše nic nestane, ale když jsou jiné, tak to selže s chybou. Zjistil jsem, že porovnávání souborů je přímo v Pythonu: [filecmp](https://docs.python.org/3/library/filecmp.html). Počkám, až bude pondělí, jestli to selže, a dodělám potom nějaký seznam souborů, u kterých očekávám, že se budou přepisovat. To by mělo být dost funkční i defenzivní (mělo by mě to chránit před tichým přepisováním souborů, které přepisuji nechtěně).


## Přeskakování dlouhých skriptů

Někdy programuji skript, který ale závisí na datech z nějakého velice dlouho trvajícího skriptu. Potřebuji to spouštět a ladit několikrát za sebou, ale nechci, aby se mi při tom lokálně stahovala stále tatáž data z toho dlouho trvajícího skriptu, která budou třeba jen o pět minut aktuálnější.

Vytvořil jsem tedy potvrzení. Pokud je nastavena určitá environment variable, dlouhý skript se mě interaktivně zeptá, jestli má spláchnout svou tabulku a stahovat, nebo to přeskočit a nechat data jak už je mám. Díky `envvar` a `confirm` v [clicku](https://click.palletsprojects.com/) to bylo hotové raz dva. Přesně takhle jsem si to představoval, když jsem chtěl mít ty věci založené na clicku. Každý skript teď může mít snadno nějaké svoje parametry, je to flexibilní a je v tom pořádek. Environment variable si lokálně nastavuji přes [direnv](https://direnv.net/).


## Drobná vylepšení klubu, bota a webu

- Smazal jsem v klubu roli, která umožňovala organizovat Discord akce. Dal jsem toto oprávnění všem, aby si každý mohl konat co chce a kdy chce a mohl na to efektivně upozornit ostatní. Nevím, proč jsem to neudělal už dávno, asi mě to prostě nenapadlo. Teď mě to napadlo, protože Dan si chtěl naplánovat několik událostí, na kterých dělá něco jako „open office hours“ pro zájemce o [CoreSkill](https://coreskill.tech/).
- Upravoval jsem textace některých automatických zpráv v klubu, aby je lidi lépe pochopili a bylo jasnější, co se děje a proč. Je zajímavé, jak lidi mohou dost zápasit s Discordem i s mými vlastními tipy a mým botem. Ale nedovím se to. Třeba prostě akorát na nic nekliknou. A když se Dan asertivně zeptal, proč někdo neklikl, odpověď byla „zaškrtala jsem několikrát, ale nevím, co to má dělat“. Asi bych se měl lidí víc ptát. Jenže mě to moc nejde, no.
- Opravil jsem několik drobných chyb v kódu, které asi nestojí za větší rozbor.
- Do grafu s typy členství jsem přidal [speciální barvičku pro lidi se stipendiem](https://junior.guru/open/#typy-clenstvi). Když už jsem si s tím hrál, poladil jsem barvičky i v jiných grafech. Chtěl jsem začít programovat měření toho, jak lidi čtou onboarding tipy, abych měl data a mohl se nějak rozhodovat, co s tím dál. Ale zasekl jsem se na tom, že nevím, co chci vlastně měřit. Kolik lidí má rozečtených kolik tipů? Jak dlouhý je interval mezi tipy? Na kolikátém tipu je kolik lidí? Jak má vypadat ten graf, co chci vlastně vytvořit? Nevymyslel jsem to zatím.


## Další poznámky

- Akce s Ataccamou má ještě volná místa, takže kdo chcete zkusit na pohovor nanečisto, [zaregistrujte se](https://bit.ly/3e8lGdm)! Online nebo osobně v Praze v jejich kancelářích. Nemusíte být ani junioři.
- Přečetl jsem důkladně a následně [pochválil na Twitteru](https://twitter.com/honzajavorek/status/1589624519311835136) článek Deníku N o lidech, kteří se rekvalifikují do IT. Je to celé vlákno s recenzí.
- Dokončili jsme [příspěvek jedné juniorky do open source Pyvce](https://github.com/pyvec/docs.pyvec.org/pull/301)! Super!
- Odpovídání v klubu, maily, a tak dále. Povedlo se mi na chvíli dokonce dosáhnout inbox zero :) Většinu CVček jsem nedokázal projít, ale naštěstí se tam rozpovídali jiní lidi. Jedno CV zapadlo a nedostalo žádné komentáře a já stále odsunuji, že se na něj kouknu, tak jsem zkusil jen napsat do kanálu, zda by na něj někdo nemrknul. Uvidím, jaký to bude mít efekt :)
- Domlouval jsem další přednášky do klubu.
- Připomenul jsem se advokátce s jednou věcí, co potřebujeme řešit pro Pyvec.
- Na GitHub Sponsors mě začal sponzorovat [Indeed Engineering](https://github.com/indeedeng)! Velké překvapení. Předpokládám, že to je nějaká akce v rámci [tohoto fondu](https://opensource.indeedeng.io/Investing-in-Open-Source/). Fakt by mě zajímalo, jak se to stalo a co vlastně z mojich věcí, co mám na GitHubu, považují za přínosné :) Indeed je docela známý agregátor pracovních nabídek, takže je i trochu v mojem segmentu.
- Přemýšlel jsem, jestli už úplně nezrušit Patreon a nepřesměrovat 3 lidi, kteří mi tam přispívají, na jiný způsob (třeba přímé posílání na účet, na které dost lidí přešlo), ale nakonec jsem se rozhodl, že je s tím nebudu otravovat a nechám to být.
- Díky projektu Jakuba Zelenky [Mimo agendu](https://mimo-agendu.ghost.io/) jsem objevil [BeyondWords](https://beyondwords.io/), věc, která má nějak pěkně zabalené strojové čtení od Microsoftu. Je to asi nejlepší čtení, které pro češtinu existuje a není to tady ani nijak pekelně drahé. Uvažoval jsem, že by se tím daly nechat načíst kapitoly v příručce. Dalo by se to i publikovat jako podcast, nebo tak něco.
- Se ženou jsme spolu 12 let. Nebyl zatím čas to oslavit. Nejlepší by bylo, kdybychom mohli třeba den v kuse spát :D
- Hrál jsem si s Duplo traktorem a Duplo ovcemi. Dítě už dokáže samo sjet menší skluzavku.
- Dostal jsem účet zdarma u [CDN77.com](https://www.cdn77.com/) (děkuji!) a mám tedy docela cool CDNku! Teď jen vymyslet, co s ní udělám :D Už ale v mailu vidím super rozbor od [Libora](https://www.linkedin.com/in/liborvanekcz/) s radami, který je přímo na míru na moje _use cases_, tak se těším, až se na to podívám.
- Během 7 dní od 5.11. do 11.11. jsem nenaměřil žádnou sportovní aktivitu. Mohl bych napsat, že jsem se celkem hýbal 0 hodin a zdolal při tom 0 kilometrů, ale to je blbost, protože jsem toho nachodil a na sdílených kolech najezdil fakt dost. Ta sdílená kola začínám používat čím dál víc, jsou fakt super. Když na Žižkově teda jsou, protože v některé časy tady na kopci není ani jedno.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/). Nabídky práce pro juniory teď inzerují: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/34fa3ec07892dd3ff64458e2ccbf12578e00860483427e9e7c4847bc/)


## Co plánuji

Dvě věci, které bych chtěl zvládnout udělat příště:

1. Zvládnout uvítání mentorů v Mews (večerní akce v klubu, kde budu mluvit a prezentovat i já).
2. Vyřešit poslední nefunkčnosti týkající se CI buildu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Back to the Future of Twitter](https://stratechery.com/2022/back-to-the-future-of-twitter/)<br>„…most people don’t get their news off of Twitter; the places they get their news, though, are driven by Twitter.“
- [The Knights Templar](https://www.bbc.co.uk/programmes/m001cpwt)<br>Kdo byli Templáři?
- [What to blog about](https://simonwillison.net/2022/Nov/6/what-to-blog-about/)<br>Ano!
- [Spouštíme MastodonCzech.cz. Chcete vyzkoušet decentralizovanou obdobu Twitteru?](https://www.lupa.cz/clanky/spoustime-mastodonczech-cz-chcete-vyzkouset-decentralizovanou-obdobu-twitteru/)<br>„Vedle masových sociálních gigantů přitom existuje zajímavý svět decentralizovaných aplikací, které pro určitou, zatím malou, skupinu lidí představují kýžený únik ze světa algoritmicky řízených feedů a timeline, všudypřítomné reklamy a sledování jejich pohybu po internetu.“

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu jsem použil vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
