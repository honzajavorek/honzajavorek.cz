Title: Týdenní poznámky #98: Kandidatura a programování onboardingu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (16.7. — 22.7.) a tak [stejně jako minule]({filename}/2022-07-15_tydenni-poznamky-97-debugovani-a-onboarding.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tak je zase pátek a já zase píšu z vlaku. Tentokrát bereme kromě dítěte v nosítku taky moje kolo. V poměru tři dospělí (my dva a babička) na jedno dítě se dá docela dobře zorganizovat si běhání skoro na každý večer, ale v těch vedrech co teď jsou moje motivace na běhání dost klesá. Popravdě, běhání v horku je humus a chci u něj spíš umřít než cokoliv jiného. Ráno nemám morál a stejně je vedro už brzo, večer je vedro i za tmy. Takže zkusím kolo, to by mohlo být v horku příjemnější a bude to změna. Na kole jsem od březnové jízdy napříč republikou prakticky neseděl.


## Onboarding

Většinu týdne jsem pracoval na onboardingu a lepším vítání nových členů v klubu.

Ladil jsem trochu ještě zakládání a správu privátních kanálů na tipy, které bude dostávat každý nový člen. Upravil jsem kód tak, aby se kanál nesmazal aspoň ještě pár měsíců, pokud člen odejde z klubu. Často se stane, že lidem vyprší karta, nebo že z klubu na chvíli zmizí a pak se vrátí. Bylo by otravné, kdyby se jim restartoval celý onboarding a začaly jim chodit opět tytéž tipy.

Rozšířil jsem skript, který už nyní zjišťoval, jestli se nově příchozí člen přidal poprvé, nebo v klubu už někdy byl. Takovým členům skript přidal k uvítací zprávě emoji s mávající rukou a s recyklujícími se špikami, abych to viděl a měl zhruba přehled.

Přidal jsem do toho kód, který pro každého člena identifikuje jeho představovací zprávu v kanálu #ahoj. S tím plánuji pracovat víc do budoucna, teď se to hodilo hlavně proto, aby pod ni bot dokázal dát emoji s mávající rukou a pár dalších takových, vítacích. Také tuto zprávu promění ve vlákno, do kterého se představí jako bot a napíše jednoduché uvítání. Do těchto vláken budu pak psát já a lidi ještě vítat i ručně, osobně, ale bude to bonus a pokud přijde deset nových lidí najednou, nebudu se muset bát, že nebudu stíhat a zůstanou zcela neuvítaní. Vlákna se navíc dají využít všelijak a už teď se tam celkem komentuje. Přesunula se tam určitá část diskuze z obecného pokecu a podle mě to teď bude přehlednější, diskuze bude líp škálovat pro víc lidí a když bude něco zajímavého pro všechny, vždy to můžeme jako moderátoři vytáhnout do těch obecných kanálů. Do zprávy od bota jsem se nesnažil nacpat moc informací, protože ty by pak měly být spíš v tom privátním kanálu na tipy. Nakonec jsem dodělal, aby bot automaticky do vláken přidával všechny moderátory a ne jen mě, protože to tak chtěl Dan, který v klubu moderátora dělá.

Většinu věcí se snažím dělat tak, aby byly _idempotent_ a aby šetřily provoz na Discord API. Idempotent znamená, že i když to spustím několikrát, výsledek bude stejný. Když vlákno pod představením založí uživatel, tak ho bot rovnou použije a třeba přejmenuje na unifikovaný název. Když nějaká zpráva už existuje a není potřeba ji přidávat, bot se ještě podívá, jestli má patřičný textový obsah a pokud ano, neudělá nic, pokud ne, tak zprávu edituje na požadovaný text. Kód je tedy celkem komplikovaný a už teď počítá se spoustou situací.

Vítání členů funguje pro všechny nové členy a v podstatě jsem to ladil rovnou na produkci. S těmi privátními kanály a tipy jsem opatrnější. S Danem jsme se na Pyvu dohodli, že to začnu pomalu pouštět do lidí, kteří zrovna do klubu přicházejí, že to budou moji beta testeři. Až to bude jakž takž fungovat, začnu to pomalu pouštět i do existujících členů.

Nakonec jsem ještě připravoval kód onboardingu tak, aby jednotlivé tipy nebyly pouhý text, ale byly to funkce vracející text, které dostávají nějaký kontext (např. objekt se členem, kterému se má tip poslat). Myslel jsem, že bych se s tím do začátku nepatlal, ale nakonec mi přijde, že to bude fakt potřeba, aby tipy byly víc užitečné než otravné a aby byly schopny se zformulovat aspoň trochu na míru situaci, ve které se člen nachází.

Teď už chybí „jen“ navrhnout první texty tipů a můžu to spustit. Mám trochu pocit, že se mi to psát nechce a tak programuju co můžu a tím to prokrastinuju.

Když už jsem u toho všeho byl, přidal jsem taky kód, který vítá sponzorující firmy i pomocí emoji, ne pouze zprávou.


## Debugování pycordu

Podíval jsem se zase trochu na [tenhle problém s pycordem](https://github.com/Pycord-Development/pycord/issues/1491) a zjistil jsem, že nový pycord mi failuje skoro na všech vláknech, ne pouze na nějakých obskurních. Skoro mám dojem, jako by to moc netestovali a vydali kód, který podle mě nemůže fungovat dobře na každém větším discord serveru, který víc používá vlákna.


## Auto-cancel na CircleCI

Občas se mi stalo, že jsem víckrát pushnul kód do hlavní větve na GitHubu a každý push spustil build na CircleCI. Ty pak jely v podstatě paralelně, ale nevěděly o sobě. Bohužel to pak znamená, že jeden build si přečte Discord, zanalyzuje jeho obsah a začne tam něco posílat, zatímco ten druhý si stihne přečíst Discord ještě předtím a začne tam posílat to samé podruhé.

Než se budou posílat lidem tipy, chtěl jsem tohle vyřešit. Zjistil jsem, že CircleCI [má auto-cancel](https://circleci.com/docs/skip-build#scope) a že ho mám dokonce zapnutý, ale mají tam explicitně napsáno, že pro hlavní větev to nefunguje a fungovat nebude ¯\\\_(ツ)\_/¯ Což je super, když dělám _continuous deployment_ a jiné větve téměř nepoužívám.

Takže jsem hledal, jestli na to není Orb (předpřipravený krok na CircleCI, který už naprogramoval někdo jiný), ale spíš není. [Něco existuje](https://circleci.com/developer/orbs/orb/thinkful/cancel_previous_build_and_wait), ale vypadá to, že to je staré a nepovedlo se mi to použít tak, že by to fungovalo.

Nakonec jsem si to prostě naprogramoval, nějak jsem to narychlo naprasil přes CircleCI API, ale bylo to celkem frustrující, především kvůli tomu jejich API. Lidi, nevytvářejte frustrující API! Přece když chci zjistit, jestli na stejné větvi nejede už nějaký další build, který bych mohl zrušit, tak bych na to neměl potřebovat dva vnořené cykly s requesty na API.

Udělal jsem si z toho task a ten se pouští jako první věc po instalaci projektu. Takže když začne nový build, nainstaluje se vše potřebné a pak se pustí tento skript, který projde běžící buildy na téže větvi a zruší je. Potom tento nejnovější build běží dál.


## Marketing

Sešel jsem se s Jakubem Nešetřilem a bylo to fajn. Povídali jsme si jen tak o životě, ale došlo i na moje dilema s marketingem. Odnesl jsem si z toho zajímavé závěry.

Pokud mým cílem je vydělat zhruba 40 tisíc měsíčně čistého a tuto metu už jsem skoro splnil, aniž bych nějaký skvělý marketing na sociálních sítích měl, možná bych ho nemusel vůbec dělat. Jeho funkci bych mohl nahradit inbound marketingem na webu a jinými věcmi, které škálují. Mohl bych se soustředit na produkt atd., ale prostě možná není vůbec potřeba, abych se tolik věnoval sociálním sítím, když byznys nejspíš funguje tak či tak.

Dává mi to smysl hned v několika rovinách. Jednou z nich je to, že svůj byznys jsem od začátku zakládal jako solo podnikatel s tím, že věci, které nedokážu naškálovat nebo automatizovat, prostě dělat nebudu nebo nemůžu. Není možné, abych dlouhodobě dělal _sales cally_, ale mohu udělat _pricing page_ a screencast, kde všechno ukážu.

Outsourcing je možnost, ale v tom, jak chci podnikat, je to [poslední možnost, když není zbytí](https://twitter.com/ColinKeeley/status/1548286804192686081). Tomuto přístupu bych se neměl zpronevěřovat a měl bych zkusit marketing na sociálních sítích buď aspoň částečně automatizovat, nebo úplně vypustit a nahradit něčím, co udělám jednou a funguje to samo. Například inbound marketing, nebo systém pro to, aby moji členové fungovali jako ambasadoři značky a sami doporučovali klub dál. Protože velká firma se bez sociálních sítí možná neobejde, ale já možná ano, protože mi stačí málo.

Nechám si to ještě rozležet v hlavě a domluvím si asi stejně i tu schůzku s [Janou](https://www.janadolejsova.cz/), ať mám víc názorů a tím i podkladů pro vlastní rozhodování.


## Kandidatura za Zelené

Přišlo mi mailem „pošli prosím jednu větu, která vysvětluje, proč jsi se rozhodl kandidovat“, tak jsem to sepisoval. Jedna věta to nebyla, to neumím, ale něco jsem vyplodil a [je to tady](https://praha3.zeleni.cz/kandidat/jan-javorek). Pak jsem si to dal ještě [na FB](https://www.facebook.com/honzajavorek/posts/10159769154357707:0), [na IG](https://www.instagram.com/p/CgKih9SLhGK/) a [na Twitter](https://twitter.com/honzajavorek/status/1549099609041080327). Když jsem zatím se Zelenými nezvládl vyrazit do ulic v rámci kampaně, zkouším nahnat hlasy aspoň na internetu - to ostatně umím stejně líp, než rozdávat letáky. Celý text:

> Chci ulice, kde se neusmažím horkem, kde v pohodě projedu s kočárkem a kde najdu pítko nebo záchod. Chci přecházet silnici nebo posílat dítě samo do školy a nebát se. Chci nové byty, aby lidé mohli bydlet v Praze a měli většinu věcí za rohem jako já, místo aby dvakrát denně stáli pod mými okny v zácpách. A kandiduji za Zelené na Praze 3, protože chtít nestačí.
>
> Zelení byli na Praze 3 v koalici na radnici poslední 4 roky a moc se mi líbí, co tady prosazují. Toto je můj způsob, jak je můžu podpořit víc, než jen hlasem nebo lajkem na FB. Zatím nejsem ani členem strany, kandiduji jako nezávislý. Patnácté nebo kolikáté místo na kandidátce samozřejmě znamená, že nemám reálnou šanci být někam zvolen, ale budu rád, když třeba i díky mě dostanou místní Zelení nějaké hlasy.

Čekal jsem, že bude tento _coming out_ víc polarizující, ale asi mám dobrou bublinu a schytal jsem jen jeden plačící smajlík a jeden rozpačitý komentář, jinak spíš lajky a srdíčka. Převážně od lidí, kteří na Praze 3 samozřejmě nebydlí :D


## Další poznámky

- Ve středu jsem byl na [pražském Pyvu](https://pyvo.cz/praha-pyvo/), které testovalo nový prostor v Hloubětíně.
- Upgradoval jsem na novější verzi Bootstrapu. Chtělo to pár změn i v SCSS kódu.
- Udělil jsem jedno stipendium na roční členství v klubu. Vzápětí přišla další žádost, ale tu jsem ještě neměl čas pročíst.
- Domlouval jsem přednášku v klubu. Zase až na září, přes léto nikdo nic dělat nechce ¯\\\_(ツ)\_/¯ Mě to nevadí, aspoň mám klid na práci. Členové zatím neprotestují, podle mě jsou taky někde na dovolené.
- Domlouval jsem si cally s firmama na další týdny a uvědomil jsem si, že i v této oblasti [bych chtěl být víc jako Levels](https://twitter.com/ColinKeeley/status/1548286796441694210).
- Vydal jsem Páji nový díl [podcastu](https://junior.guru/podcast/).
- Sociální sítě jsem tento týden dost ignoroval.
- Klub, maily, a tak dále. Ale popravdě jsem administrativu tento týden spíš zanedbával.
- Během 7 dní od 16.7. do 22.7. jsem naběhal 10 km, při procházkách nachodil 8 km, na túrách nachodil 9 km. Celkem jsem se hýbal 10 hodin a zdolal při tom 27 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Připravit první verzi zpráv pro onboarding a pustit je do první testovací skupiny lidí.
2. Zpracovat poznámky z hovoru s mentorem a prodiskutovat je s ostatními mentory.
3. Propagovat nový díl podcastu.

**Bonus:** Doplánovat si pořádnou dovolenou.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Jiří Rostecký: MladýPodnikatel.cz](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2Bi0WtkAqRE&h=1a2c1d093d690735af5b5878f802a1c1993599dd68c3c921a7cbdbd350cad63b)<br>Super rozhovor, kde se řeší hodně věcí, které teď v marketingu zrovna řeším.
- [České zbrojovky jely 24/7, zatímco USA se bály eskalace. Bylo to frustrující, říká náměstek Kopečný](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.voxpot.cz%2Fceske-zbrojovky-jely-24-7-zatimco-usa-se-baly-eskalace-jak-frustrujici-rika-namestek-ministryne-obrany-kopecny%2F&h=c53fc1b0f071eb464302474b140f3085ce48c634d9cd4b468c5d1ddc2f32cc33)<br>Zajímavý vhled do věcí.
- [Pieter Levels: Making $2.7M A Year With No Employees](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BrTsX1IG4s&h=884ea5255776b69e46adb04ff5449a6d3c97cd87778d8dcbce6b99ba60f882fd)<br>Ojedinělý podcast s P. Levelsem o tom, jak startupuje v jednom člověku a žije si život jaký chce.
- [Konvalinka: Letní vlna je největší za celou dobu, nemá smysl čekat na nové vakcíny](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BRZMhp8V1I&h=033c39c38d0e8af5ebf705b89da520bf331f42780607de10bc22e892c8a21c2c)<br>Blíží se další vlna covidu? Užitečné shrnutí.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
