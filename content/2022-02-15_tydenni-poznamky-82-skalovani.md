Title: Týdenní poznámky #82: Škálování
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (1.2. — 15.2.) a tak [stejně jako minule]({filename}/2022-01-31_tydenni-poznamky-81-podovolenkovy-blazinec.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Jak jste si mohli všimnout, z týdenních poznámek se stávají dvou až třítýdenní. Napadlo mě, jestli by nemělo smysl změnit „oficiálně“ frekvenci vydávání poznámek a nehrnout to před sebou, ale dám tomu ještě šanci.


## Škálování?

Slovem škálování se v IT označuje situace, kdy jste zařízení na nějaký objem (je celkem jedno, jestli zakázek, klientů, e-mailů, zaměstnanců, serverů) a zjišťujete, že se objem zvyšuje a vy se potřebujete rychle zařídit tak, abyste ty vyšší objemy zvládli.

Pokud třeba učíte angličtinu od hodiny, moc to neškáluje, protože jakmile vyplníte počet hodin v týdnu, můžete už jen navyšovat cenu nebo založit firmu a najmout další učitele. Pokud prodáváte PDF knížky, škáluje to skvěle, protože je dost jedno, zda knížku prodáte pěti lidem nebo pěti tisícům lidí. Pokud samozřejmě rukou nevypisujete účetní doklady a neposíláte je zákazníkům s osobním podpisem.

Poslední týdny se u mě nesly ve znamení škálování, které potřebuji, aby proběhlo, ale nestíhám ho dělat. Jsem tedy veselý i smutný zároveň. JG možná na první pohled nevypadá jako něco, co škáluje dobře, přece jen je to dost závislé na mě jakožto jedné osobě, ale od začátku vše kolem něj vymýšlím tak, aby škálovat mohlo, když budu chtít.

Myslel jsem, že věci, které dělám ručně, mohu časem naprogramovat a automatizovat. Chybou by bylo automatizovat je hned od začátku. Chybou ale bylo si myslet, že ta automatizace může proběhnout za odpoledne. Automatizovat vítání členů v klubu je programování na měsíc a když u toho stále ještě ty členy vítáte a je jich stále více, dostáváte se do problému.

Je otázka, zda jsem ale měl prostor s tím něco dělat dřív. Mám tolik priorit, že vlastně dělám hlavně to, co zrovna hoří. To platí celý poslední rok, takže nevím, kdy jsem měl odhadnout, že lidí přibývá, přibývat bude, a že už mám začít automatizovat, zatímco něco jiného v aktuálním momentě hoří víc. Je to těžké.

Každopádně jsem svůj únor začal tím, že se sesypaly hned tři věci:

- Druhý den měla být přednáška v klubu a já jsem stále neměl vyřešené, jak obejít limit na 25 lidí na videocallu v Discordu, pokud je zapnuté video.
- Robot na nabídky práce byl zahlcen nabídkami z LinkedIn a nebyl schopen dokončit svou práci v rozumném čase. Protože toto běží v rámci jednoho velkého skriptu, nedoběhlo ani nic dalšího, neaktualizovala se webová stránka, neprobíhaly všechny automatizované záležitosti v klubu, apod.
- Každý den chodilo do klubu pět až deset lidí za den. Dan i já jsme všechny osobně vítali, co nám síly stačily, ale i tak to bylo vyčerpávající.

Svým způsobem to jsou krásné problémy, protože znamenají, že JG se daří a roste. Na [grafu výnosů](https://junior.guru/open/) jde vidět, že v lednu jsem se flákal s fakturami firmám, ale příjmy z individuálního členství stouply téměř dvojnásobně.

Na druhou stranu, pokud je nebudu schopen efektivně a rychle řešit, mohou se různé věci na JG pod náporem postupně udusit. Kormidluju skalnaté vody.


## Přednášky

_First things first_, jak se říká, takže hned v pondělí jsem se jal řešit problém s limitem 25 lidí na videocallu na Discordu. Napadlo mě, jak to obejít, ale nevěděl jsem, jak to vyrobit a jestli to bude fungovat.

Návod na výrobu jsem našel tady: [Camera and Video Control with HTML5](https://davidwalsh.name/browser-camera) Bylo to jednodušší, než jsem myslel. Prototyp byl hned, nejvíc času mi zabraly tlačítka okolo a CSS.

Vytvořil jsem [stránku pro přednášející](https://junior.guru/speaker/), kde si mohou otevřít „zrcadlo“. Když pak nasdílí do callu svou plochu (což Discord nepočítá jako video), mohou ukazovat slajdy, prohlížeč, nebo třeba svou hlavu, skrze toto „zrcadlo“.

Také jsem změnil hlasové kanály pro přednášení a v „přednáškárně“ jsem nastavil práva tak, aby mohl video a sdílení obrazovky využívat jen speaker. Bohužel nelze tyto dvě funkce rozdělit a zakázat video všem a speakerovi jen sdílení obrazovky, takže speaker když omylem klikne na video, zastropuje call na 25 lidí. Roli, která práva speakerům uděluje, zatím dávám lidem ručně, ale časem by to měl zvládnout i bot.

Dodělával jsem to na poslední chvíli a Svetlana tedy neměla zrovna úžasný komfort pro přednášení, jelikož jsem ji postavil před hotovou věc těsně před přednáškou a celé to bylo nové i pro mě. Navíc jsem se tak soustředil na technické zázemí přednášky, že mě nějak zaskočilo uvádění a úplně jsem se u toho zablekotal a nebyl schopen dát dohromady souvislou větu. Tímto se Svetlaně ještě jednou omlouvám. Že mi během callu zase došla šťáva v noťasu a běhal jsem pro prodlužovačku, to už je skoro folklór, naštěstí to mívá na průběh minimální vliv.

Její přednáška byla jinak super, lidi si ji velmi chválili, prolítli jsme všechny možné cesty jak vyrobit mobilní aplikaci, na co se připravit, co se učit a z čeho, no bylo to plné praktických tipů.

Stránku pro speakery jsem po přednášce doplnil o další informace a poprosil o zpětnou vazbu v klubu. Dostal jsem spoustu dobrých připomínek, aby byla stránka použitelnější, ale ty musím ještě zapracovat.


## Předělávání robota na nabídky práce

Rozhodl jsem se, že po dlouhém odkládání nastal čas přepracovat robota na pracovní nabídky, když už se mi začal hroutit na hlavu.

Aby fungoval zbytek bota a webu, pozastavil jsem stahování nabídek práce z LinkedIn, které proces nejvíc prodlužovalo a zatěžovalo. Jenže jsem zároveň zjistil, že StartupJobs mají chybu v exportu a nejdou teď od nich žádné nabídky. Zároveň [končí nabídky na StackOverflow](https://meta.stackoverflow.com/questions/415293/sunsetting-jobs-developer-story). Na SJ jsem napsal a prý to opraví, ale zatím to stále vrací chybu. Takže ze dne na den vypadly tři zdroje a na webu teď nemám skoro nic, jen vlastní nabídky přímo z JG.

Vytvořil jsem si na svou práci větev na Gitu a [rozpracovaný PR](https://github.com/honzajavorek/junior.guru/pull/780), což moc často nedělám, dělám _continuous delivery_. Ale tady jsem se na to vybodl, protože mi bylo jasné, že pojedu buldozerem a za mnou zbude jen spoušť, kterou pak budu dávat horko těžko vůbec dohromady, natož abych to celé nějak průběžně dával na produkci a bylo to stále nějak funkční.

Hodně mi pomohlo, že jsem se sešel na oběd s [Tomášem](https://tomasvotruba.com/) a povídal jsem mu, co řeším za problém. Přivedl mě na zajímavé myšlenky, které jsme pak ještě [dodatečně řešili i na GitHubu](https://github.com/TomasVotruba/friendsofphp.org/pull/185#discussion_r798387962). Hlavní myšlenka, na kterou mě přivedl, je uložit prostě stažené nabídky práce po jednotlivých dnech do JSONu na disk a tam řešit uskladnění, retenci, případně offload na S3 či jinam. Až potom to zvlášť číst a nějak zpracovávat. To zase navazuje na slova [Jana Suchala](https://twitter.com/jsuchal), se kterým jsem kdysi za dob SynopsiTV seděl někde na obědě v Bratislavě a on říkal, že základ úspěchu se scrapery je uložit data ze scraperu tak jak jsou a čistit až potom. Když je to takto oddělené, snadněji se debuguje, co že to ty scrapery vlastně stáhly za data a případně se dá nad těmi daty pustit postprocessing znova a znova a ladit výsledek bez toho, aby se muselo vše opakovaně stahovat.

Rozdělil jsem tedy scrapery a postprocessing. Scrapery stále řeší Scrapy, pak mám pár pipelines, které mě zbavují úplných nesmyslů, ale dál se to už jen uloží do [JSONL](https://jsonlines.org/) přes [FEEDS](https://docs.scrapy.org/en/latest/topics/feed-exports.html). Lepší než JSON, protože pro velké objemy se dají na rozdíl od JSONu streamovat po řádcích.

Rozdělil jsem build na CircleCI, aby nabídky práce mohly jet paralelně se zbytkem skriptů.

Místo, aby si build stahoval předchozí zálohu a nějak složitě rozzipovával a načítal, rozhodl jsem se ukládat data prostě kumulativně po dnech na disk a jejich perzistenci zajistit přes CircleCI cache. Ta může být až 800 MB, ale samozřejmě by asi bylo lepší soubory časem ukládat jinam, třeba na S3 nebo někam na GitHub, to ještě vymyslím. Každopádně zlepšení, protože i kdyby se muselo něco stahovat ze sítě, JSONL soubor lze stahovat a zpracovávat zároveň, kdežto zazipovaný SQLite .db soubor moc teda ne.

Smazal jsem scrapery na StackOverflow, protože stejně končí, a na DobrýŠéf, protože tam žádné nabídky práce nejsou, aspoň co já vím (kdyby zas někdy byly, vytáhnu snadno z historie Gitu). Odstranil jsem prozatím samotné JG jako zdroj nabídek, protože mám dojem, že se mi tam pletou jabka a hrušky, že JG musím prostě procesovat úplně zvlášť a necpat to do scraperů a tvářit se (čti „mít kód všude samý if/else“), že jsou moje vlastní nabídky totéž jako nabídky z LinkedIn.

Z minulých pokusů o stahování záloh a načítání historie nabídek práce z nich jsem měl, díky _continuous delivery_, všude v kódu dva modely, starý Job a nový Employment, které se různě proplétaly a doufal jsem, že jednou to nějak celé sloučím a zmigruji. To jsem teď udělal, vše jsem smazal a model udělal znovu přesně tak, jak jej chci.

Pak přišel na řadu postprocessing. Tam jsem se snažil, aby vše bylo co nejvíc efektivní. Nejdříve načíst věci z JSONL souborů, zparsovat, zpracovat, pak uložit do SQLite, mergnout duplicity, pak vytáhnout co se uložilo a udělat ještě postprocessing a uložit úpravy, které udělá. Nakonec z toho bylo několik dní s [multiprocessing](https://docs.python.org/3/library/multiprocessing.html). Už jsem byl poučen z dřívějška, že do SQLite by měl zapisovat ideálně jen jeden proces, takže jsem tam měl hned několik situací, které by se daly popsat jako _producer/consumer_. Nakonec jsem to vyřešil přes hned několik `multiprocessing.Queue()`. Zkoušel jsem i `multiprocessing.Pool()`, ale tam mi vždy vytekla nějak paměť nebo to zlobilo jiným způsobem. Mám _pool_ rád na jednoduché věci, ale tady bylo fakt lepší si to pořešit sám těma frontama, už jen proto, že jsem měl kompletní kontrolu nad jednotlivými procesy a mohl si řídit např. připojení k databázi. Celé jsem to pak ještě párkrát optimalizoval a teď to teda nějak funguje, paměť nikde nevytéká a nekončí to na _segmentation fault_, nepíše mi to nic o _leaked semaphore objects_ nebo _corrupted_ databázi, megabyty JSONL souborů to zpracuje a uloží za necelou minutu. Většinu tohoto monstra jsem vytvořil během sezení v kavárně Atrium Žižkov s [Mílou](https://milavotradovec.cz/) a chtěl bych je tímto politovat, že to se mnou museli vydržet.

Funkce, které dělaly postprocessing stažených inzerátů, jsem přesunul ze Scrapy pipelines do tady tohoto mého nového systému.

Pak už jsem stihl jen popřemýšlet nad tím, jestli nejsou vlastně megabajty JSONL souborů zbytečné plýtvání místem a rozhodnout se, že jsou. Místo do texťáku jsem tedy začal ukládat do gizpu a číst z gzipu. Ty největší soubory se díky tomu zmenšily i několikanásobně.

A nakonec jsem to v kódu [zdokumentoval](https://github.com/honzajavorek/junior.guru/pull/780/files#diff-e7b580346e4611dfc645a48ac25efe9a3dc1ea21c19b208d92f6c7a3b35d38b0), abych to byl sám schopen ještě někdy pochopit. Čitatele jsem oslovil jako ve [Viva La Dirt League](https://www.youtube.com/c/VivaLaDirtLeague), _Hello, adventurer!_, abych nastavil ta správná očekávání.

Blbé je, že jsem na tom dělal kdy jsem jen mohl, dva týdny jsou pryč a jsem teprve na začátku. Vlastně jsem projel přes kód tím buldozerem, postavil jsem tam malý nový domeček, ale všude okolo jsou přetrhané trubky a elektrika a já ještě ani nevím, jak to celé pozapojuju zpátky. A až potom to budu moct hodit na produkci.

Ale zase to umožní dělat na spoustě nových krásných věcí, které by se ve staré prohnilé verzi dělaly dost těžko. Třeba s Mílou konečně uděláme to třídění inzerátů s využitím ML, nebo přidám nové zdroje inzerátů.


## Firmy

Jedna firma se rozhodla neprodloužit členství, protože měli pocit, že nedokázali členství naplno využít tak, jak původně chtěli. Rozumím tomu a věřím, že se toto stávat prostě bude. I když neprodlouží, jsem firmám vděčný, že mě podržely v době, kdy to JG nejvíc potřebovalo.

S jinou firmou jsme zase prodloužili spolupráci téměř přes SMSku :D

S další si volám, protože po dlouhých měsících jednání na jejich straně se blížíme k uzavření kontraktu.

Jednal jsem před lednem s více firmami a všechny mi slíbily, že budou něco chtít a že se mi ozvou, ale teď jen čekám. Nevím vlastně ani, jestli už je to dlouho, můj pojem o čase je dost narušený. S miminem mi nějak splývají dny a týdny. Taky mám pořád trochu jiné tempo rozvoje byznysu, například týden může být dlouho pro mě, ale v některých firmách si za takovou dobu ani neuprdnou.

Nemám každopádně čas je uhánět, takže buď se vrátí a objednají, nebo holt přijdou firmy jiné… Nebo si třeba někdy ten čas najdu a těch pět emailů pošlu, ale teď mám prostě jiné priority, potřebuji škálovat byznys na jiných frontách.


## Další poznámky

- Pozvali mě na natáčení podcastu [ProgramHRování](https://www.programhrovani.cz/). Připravoval jsem se na to, celkem poctivě, a nahrávání probíhalo v Holešovicích, kam jsem osobně jel.
- Týdenní souhrn se v klubu objevil pětkrát, to už jsem psal minule. Povedlo se mi to opravit. Bylo to zase chybou v odsazení, která vznikla, když jsem do kódu neopatrně šťoural. Něco bylo v cyklu, i když být nemělo.
- Prošel jsem se s Jakubem z [Rozbitého prasátka](https://rozbiteprasatko.cz/) a hezky jsme si popovídali. Výhoda bydlení v Praze. Jakub už se [na Twitteru rozcvičuje](https://twitter.com/RozbitePrasatko/status/1493266070450417668) před vydáním série dílů svého podcastu, které budou o práci a kde bude jeden díl i se mnou.
- Můj startupový guru Jakub Nešetřil [projevil radost](https://twitter.com/jakubnesetril/status/1493214393601081352) nad tím, jak frčí junior guru :)
- Jeden člen klubu našel svého pravidelného mentora v jednom ze seniorů v klubu. Sice našel svou první práci jinde, ale tam se mu vůbec nevěnovali a tak si tihle dva psali tak dlouho, až mu ten senior řekl, ať jde teda pracovat k nim. Neuvěřitelná story, každopádně se teď setkali v Praze, aby se domluvili, a pak šli na pivo, tak jsem se tam taky stavil a přišel i další člen klubu a byl z toho ve čtyřech takový milý spontánní mini JG srazík.
- V [Česko.Digital](https://cesko.digital/) to vypadá na nějaký konkrétní projekt vhodný i pro juniory, vyměnili jsme si tam k tomu pár zpráv, tak pokud to klapne, zpropaguju tuhle příležitost i v klubu.
- [Lukáš Kubec](https://www.linkedin.com/in/lukas-kubec/), člen klubu, se na náš popud pustil do překládání [How to ask good questions](https://jvns.ca/blog/good-questions/). Měl to asi druhý den hotové, čímž mě trochu přistihl nepřipraveného. Nestihl jsem se na to ještě podívat, natož s tím dál něco udělat. V plánu by bylo včlenit to někam do JG a využít i přímo v klubu.
- Řešil jsem, proč se mi sluchátka na callu zblbnou a dělají samy od sebe _mute_, čímž se stávají nepoužitelnými. Zjistil jsem, že jde asi o bug v macOS Monterey ([Reddit](https://www.reddit.com/r/Jabra/comments/qw5hty/mac_monterey_automuting_issues/), [Reddit](https://www.reddit.com/r/Jabra/comments/rlu30y/jabra_elite_75t_mutedunmutedmutedunmuted/)) a našel nějaké způsoby, jak to zatím řešit ([nějaký blog](https://richardbloomfield.blog/2021/12/my-ear-buds-keep-auto-muting-themselves/), nějaký [doplněk do Chrome](https://chrome.google.com/webstore/detail/disable-automatic-gain-co/clpapnmmlmecieknddelobgikompchkk/related), další [blog](https://codeandframes.com/audio/how-to-stop-google-meet-to-change-microphone-volume.html)). Jako by nestačilo, že musím na Google Meet používat Chrome, protože ve Firefoxu to funguje napůl.
- Připravoval jsem přednášku s Nelou Slezákovou o tom, jak přežít cestu juniora po psychické stránce. Ladili jsme texty, fotku, logo, všechno. Dík [Danovi](https://coreskill.tech/) za pomoc s převedením loga do SVG.
- Propagoval jsem na sociálních sítích přednášku Světlany a včera přednášku Nely, která bude za další týden 22.2.
- Volal jsem si s Jiřím Anděrou z Czechitas a probírali jsme naši spolupráci na datech z pracovních inzerátů a jaké jsou do budoucna možnosti v různých dalších směrech.
- Kousek od nás je ve vnitrodvorku úřadu bio popelnice, tak jsme tam začali nosit bio odpad z domácnosti. Osvědčilo se to, takže jsme se jali koupit nějaký koš na bio. Vybrat mi pomohl [tento článek](https://biom.cz/cz/odborne-clanky/je-mozne-separaci-bioodpadu-zvysit-komfort-a-hygienu-v-domacnostech).
- Pája s yablkem nahrála [nový díl podcastu](https://junior.guru/podcast/). Postaral jsem se o to, aby se správně publikoval, teď mě ještě čeká jeho propagace na sociálních sítích.
- S [Danem](https://coreskill.tech/), moderátorem v klubu, jsme různě řešili, jak by časem mohl vypadat _onboarding_ a vítání nových členů, kdyby nám s tím pomáhal bot. Shodli jsme se, že než bude bot, upravíme a doplníme pravidla klubu, ať je tam co nejvíc praktických tipů, ale já jsem na to pak zapomněl, protože lidi chvíli chodili méně. Včera ale zase pět šest nových.
- V klubu se představilo [Jetveo](https://jetveo.io/cs/blog/articles/jakub-interview), _low-code_ platforma pro C#, na které junioři můžou snadno začít vytvářet celé appky. Lidi měli zájem o demo, tak vybíráme termín a plánujeme to.
- Členovi klubu jsem dal podrobný feedback na jeho CV, v několika vlnách.
- Napsali mi z agentury, která řeší nabídky práce pro AT&T a která si u mě před časem objednala pár inzerátů, že člověk, s nímž jsem komunikoval, už tam nepracuje a jestli jim u mě neco zbylo, třeba nějaké kredity. Odepsal jsem, že jim u mě zbyla nezaplacená faktura, tak jestli na to nechtějí mrknout.
- V klubu se rozjela řetězovka na způsob [tohoto tweetu](https://twitter.com/KateMihalikova/status/1491497856418693123) a musím říct, že v místě, kde se to hemží _career switchery_, je to fakt zábava.
- Zapnul jsem [Headliner](http://headliner.app/), ale díl podcastu s Jiřím Psotkou dodatečně nezpracoval. Dnes zpracoval až druhý díl, s yablkem. Napsal jsem jim na support, ale ta aplikace je celá tak hrozná a nepřehledná, že uvažuju, že si to buď udělám nějak sám, nebo že teda asi smažu intro z YouTube a nastavím to raději celé znova. Čekám zatím co ten support, ale nedělám si vlastně vůbec iluze.
- Propagoval jsem na sociálních sítích projekt juniora [Romana Viktora Dvořáka](https://www.linkedin.com/in/rvdvorak/), [Weather Board](https://jakbude.herokuapp.com/).
- Skript, který vytváří role lidem z jednotlivých firmem, jsem změnil tak, aby role vždy nesmazal a nevytvořil znova. Teď kontroluje, jestli už existují a pokud ano, tak je nechává žít. Toto umožňuje role reálně využít, jelikož se už nemění každý den jejich IDčka a role, kterou člověk viděl včera, je tatáž „instance“, jakou vidí dnes.
- Dal jsem na sociální sítě [článek Hany Konečné o zvoraném pohovoru](https://www.hanakonecna.cz/jak-jsem-totalne-zvorala-pohovor/) a mělo to celkem ohlasy.
- Několikrát jsem samozřejmě prošel celý klub a na vše možné odpověděl, všechny uvítal, atd. Sem tam jsem řešil, když se někdo zaseknul s přístupem do klubu, ale naštěstí nic závažného.
- Issue o tom, že písmo z Bootstrapu je příliš tenké všude jinde než na macOS, bylo [zavřeno](https://github.com/twbs/bootstrap/issues/34813#issuecomment-1035876545). _Closing as stale_ si vykládám tak, že se neobjevilo víc lidí, které by to trápilo a pod tímto issue by se nějak vyjádřili.
- Během 15 dní od 1.2. do 15.2. jsem naběhal 6 km, při procházkách nachodil 32 km. Celkem jsem se hýbal 9 hodin a zdolal při tom 38 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Pracovat dál na botovi, který stahuje a třídí pracovní nabídky.
2. Začít domlouvat, kdo bude přednášet po Nele.
3. Propagovat nový díl podcastu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [51 - Belarus: The Next Crimea?](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BUt4TJt-zM&h=30d16b59242c1fc00df91e50a592e0a7fbec02b6d072f9e7935effc71135f516)<br>Tři odborníci na téma aktuální a budoucí geopolitické role Běloruska.
- [Pod stejnou vlajkou](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.advojka.cz%2Farchiv%2F2022%2F2%2Fpod-stejnou-vlajkou&h=2ffad67f38fb579c83b1293b54699abdd08b808ee9ce117a0340d4cf866c729b)<br>Pěkný rozhovor o pandemii, klimatu, antivax, o tom jak to všechno souvisí. Jak lidé (ne)vnímají politiku nebo jak se vědci nevnímají navzájem. Až si pro nás přijde klima, na pandemii budeme vzpomínat jak během maturity na písemku z páté třídy.
- [Nová generace baterií přichází. Elektromobily změní víc, než si myslíte](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fveda-a-technika%2F431481-nova-generace-baterii-prichazi-elektromobily-zmeni-vic-nez-si-myslite&h=316b934b59db342f715cd12d402bfe5e1e1283eaace9db906d4847c5fe878f86)<br>Budeme mít auta s „nekonečnou“ životností? Co by to změnilo na způsobu, jakým auta kupujeme a používáme?
- [EU chce zakázat prodej spalovacích aut. Proč vám to může být buřt](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fveda-a-technika%2F425328-eu-chce-zakazat-prodej-spalovacich-aut-proc-vam-to-muze-byt-burt&h=09df4f29d376134f1b1297915ce657440a1b0dbeb98024b72effa0e54b6aec49)<br>„EU plánuje zákaz spalovacích aut tak, aby to mohlo vypadat, že něco změnila, i když se to reálně stane i bez jejího vlivu.“
- [Konec mýtů o školném: americké studentské půjčky](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.devian.cz%2F2020%2Fkonec-mytu-o-skolnem-americke-studentske-pujcky%2F&h=4d8d868971655c22602d2b1a1c4ffed44a99e9d7e24a3cbe8ebb899aacccf2b4)<br>Zajímavá kritika studentských půjček zprava.
- [Komentář: Praha, parkoviště Evropy. 170 tisíc míst je beznadějná utopie](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Fdomaci-zivot-v-cesku-komentar-praha-parkoviste-evropy-170-tisic-mist-je-beznadejna-utopie-187217&h=530a4e53bc35062946eeb583b8913c1c1c1741c06bfcb74d3dda39d145089037)<br>„Pražská automobilová doprava zřejmě má být vlajkovou lodí programu ODS. Tento amatérský výkop je ale zcela mimo dopravní, urbanistickou i ekonomickou realitu. Jestli někdo z autorů textu strávil opoziční roky studiem dopravních témat, asi to bylo na vysoké škole života.“
- [11 - The Libyan Civil War](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BUt4TwS_po&h=382c75903aa11e0434185549364281e47875e2e2ffac22296a07c5278318e9d0)<br>Zajímavý díl o tom, v jak beznadějné situaci se nachází Libye.
- [12 - The Vultures of Venezuela](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BUt4SSjV7A&h=6a2a0578769c2b9dfb4f3675459342cdf4b73edf42c6788500638fd08b596572)<br>Až někde zase uvidíte přirovnání založené na tom, že za rozvrat ve Venezuele může jen a pouze komunismus, tak si pusťte tohle.
- [1Password’s Blue Ocean Strategy](https://getpocket.com/redirect?&url=https%3A%2F%2Fsecurityboulevard.com%2F2022%2F02%2F1passwords-blue-ocean-strategy%2F&h=c9ce68c993e66dd4e334e8848c9d7c041ec4eeba59bc3e52ed002e84fdd3d895)<br>1Password dostal další investici a toto je článek, který rozebírá jejich market positioning, byznys model a co můžou chtít vyrobit do budoucna.
- [What Happens After a ‘Million-Mile Battery’ Outlasts the Car?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.wired.com%2Fstory%2Fwhat-happens-after-a-million-mile-battery-outlasts-the-car%2F&h=9ccff33f36a70f2f9c062ceb80f3474cb6011c5fe663b59ca9c755043932c34c)<br>Zajímavé zamyšlení nad tím, co se stane, až baterka natřikrát přežije auto. Na jednu stranu znovupoužitelnost, na druhou se nebudou vracet do oběhu materiály na výrobu baterií z jejich recyklace a bude potřeba mít jejich velké množství vytěženo ze Země.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
