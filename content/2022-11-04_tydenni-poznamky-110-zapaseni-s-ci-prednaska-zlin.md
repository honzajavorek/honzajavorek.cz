Title: Týdenní poznámky #110: Zápasení s CI, přednáška, Zlín
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl zase nějaký ten týden (22.10. — 4.11.) a tak [stejně jako minule]({filename}2022-10-21_tydenni-poznamky-109-prednaska-a-prekopavani-kodu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Minulý týden jsem nezvládl napsat poznámky. Bylo toho nějak moc. Taky jsme byli ve Zlíně u babičky a rozhodl jsem se, že si tam i trochu odpočinu, že to potřebuju, takže jsem třeba jeden celý den dělal něco na zahradě a nepracoval jsem.

Nejlepší bylo, že jsem klikl na upgrade macOS Ventura a ten se nějak pokazil. Nikdy se mi to nestalo a proto jsem na to klikl i přesto, že jsem potřeboval pracovat a odjet druhý den vlakem na opačný konec republiky. Nejdřív se to stahovalo snad 10 hodin, potom se to sice nainstalovalo, ale blbě, padalo to do recovery módu a tam byl progress bar na dalších 10 nebo kolik hodin. Během toho jsem jel tím vlakem, ještě o 20 minut zpožděným už na příjezdu, a jen doufal, že se mi to povede ve Zlíně nějak rozjet. Nakonec se to fakt spravilo samo a dokonce i za méně hodin, než bylo na progress baru, ale byl jsem ve stresu a po několika dnech beznadějného programování (viz dále) to dost ovlivnilo můj psychický stav. Naštěstí jsem se mohl vypovídat investorce a odpočinout si pak o víkendu.

Taky jsem se u babičky snad poprvé od narození dcery vyspal jednou do 11 hodin, což bylo osvěžující :)


## Zápasení s CI

Prakticky celý předchozí týden jsem vymýšlel a pokus-omyl prozkoumával, jak by mohly po novém fungovat CI buildy na JG.

Jen připomenu, že CI build je pro JG produkce. Celý projekt funguje tak, že se jednou nebo víckrát denně spustí CI, tam se vše stáhne, vyhodnotí, synchronizuje, udělají se změny na Discordu, pošlou maily, vygeneruje se statická stránka a deployne, a hotovo. JG záměrně nemá žádný jiný runtime. A ano, znamená to, že bot na Discordu reaguje třeba i s denním zpožděním, nebo že nemůžu mít na webu žádný formulář. Výhoda je, že nepotřebuju řešit servery, databáze, uptime, produkční chyby, nic mi v noci nespadne a nezačne mi to pípat na mobilu.

Povedlo se mi několikrát za sebou omylem poslat tytéž maily, protože kontrolní mechanismus jsem změnami rozbil. Řešil jsem, jak paralelizovat celý build na CircleCI [pomocí funkcí, které nabízí](https://circleci.com/blog/how-to-boost-build-time-with-test-parallelism/). Šlo hlavně o to, jak mohu sloučit soubory a SQLite databázi po tom, co se běh rozdělí do několika paralelních. Rozbil jsem při tom i kumulativní keš dat kolem nabídek práce a budu je muset obnovit ze zálohy. Příruční [Datasette](https://sqlite-utils.datasette.io/) mi pomohlo zjistit, proč je moje databáze je najednou menší o 100 MB.

Slučování dat jsem nakonec vyřešil tak, že mám skript, který projede vše, co je ve složce s JG a zapamatuje si časy poslední změny k jednotlivým souborům. Udělá tedy něco jako _snapshot_. Potom se spustí synchronizace a pak se zase spustí skript, který udělá nový _snapshot_, porovná je, a změněné soubory si odloží bokem tak, aby je šlo později přenést do další fáze buildu a sloučit. Slučovací skript se umí poprat s databází.

Nejdřív jsem naivně exportoval SQL dump, upravil jej, aby byl idempotentní (CREATE TABLE IF NOT EXISTS, INSERT OR REPLACE INTO, CREATE INDEX IF NOT EXISTS), a pak načetl všechny dumpy přes sebe, ale to byla blbost. Zjistil jsem totiž (opět díky zkoumání výsledku pomocí příruční Datasette), že některé synchronizační skripty zapisují do stejné tabulky. Takže jsem to udělal normálně tak, že se databáze otevře, čte se z jedné a záznamy se kopírují do druhé formou nějakých UPSERTů, kdy neexistující záznamy se převedou jak jsou a existujícím se updatují pouze NULL sloupce, pokud je pro ně v přenášeném záznamu nějaká hodnota. Dalo mi dost práce to udělat správně, protože [UPSERTy jsou v SQLite trochu zamotané](https://github.com/simonw/sqlite-utils/issues/66). Tohle mi funguje a hezky to merguje paralelně vytvořené databáze přesně tak, jak potřebuju.

Celkem mi při tom pomáhá i [sqlite-utils](https://sqlite-utils.datasette.io/), ale asi by to všechno šlo snadno udělat i [přímo z Pythonu](https://docs.python.org/3/library/sqlite3.html) a v některých verzích kódu jsem to tak měl.

Taky pomáhá, že před manipulací s databází vypínám WAL mód, aby fungovala víc jako jeden soubor, což jsem dřív nedělal a možná proto jsem občas dostával chyby související s poškozením databáze.

Nakonec jsem si hrál s rozdělením různých fází buildu. Jeden skript, na kterém záviselo spousta jiných, jsem vyčlenil před hlavní build a díky tomu jsem mohl mnohem lépe paralelizovat zbytek. Pak mi došlo, že bych mohl vedle něj pustit i všechny další skripty, které na ničem nezávisí a tak mám vlastně dvoufázový build, kdy se v první řadě paralelizuje tohle a pak se paralelizuje zbytek. Rozdělení do fází jsem si naprogramoval a počet paralelních kontejnerů, nebo co to je, se kontroluje a záměrně to spadne, pokud ideální počet nesedí s tím, co je nastaveno v YAML konfiguraci buildů. Při ladění mi pomohlo implementovat si `--dry-run` option, která jen vytiskne do terminálu názvy skriptů, místo aby se spustily.

To ovšem způsobilo, že druhá fáze buildu začala spouštět znova věci z té první, protože nevěděla, že už vlastně běžely. Potřeboval jsem, aby si synchronizace uměla evidovat co běželo, a to napříč procesy a dokonce napříč několika fázemi buildu. Dal jsem to tedy do databáze. S každým spuštěním synchronizace se uloží pod nějakým ID a k tomu se eviduje, co už běželo. Nic se nepouští dvakrát. Jako ID se při vývoji automaticky vezme nějaký timestamp spuštění, aby se to vždy spláchlo, ale na CI se vezme ID workflow (měl jsem tam ID jobu a to byla blbost, nefungovalo to správně, DoS-ovalo to Discord API a opravoval jsem to potom), takže se to v průběhu nespláchne.

Nejvíc jsem se ale natrápil se strukturou kódu, který mi organizuje jednotlivé commandy v [clicku](https://click.palletsprojects.com/). Vždy jsem něco předpokládal a pak jsem zjistil, že jsem to předpokládal špatně. Chtěl jsem to mít udělané nějak pohodlně a zároveň vyvážit co je explicitní a co je magické a co se děje během importu a co až když se něco spustí, totálně jsem se do toho zamotal a v podstatě několik dní v kuse jsem přepisoval dokola stále tytéž soubory a narážel na tytéž opakující se chyby. Co mít jako command group? Jak rozšířit třídy? Jak bude vypadat command? Odkud co se bude importovat, aby se neimportovalo cyklicky? Jak udělat správně dekorátory a dělat vlastně vůbec nějaké? Spousta commitů, refactoringu, přemýšlení, revertů. Dohnalo mě to k velké frustraci a povedlo se mi to vyřešit až v pondělí den před přednáškou, kdy jsem u toho, byť odpočatý po víkendu, seděl až do pozdního večera.

Postupně jsem čas buildu dostal z 40min na 36min a potom dokonce až na 24min. Chtěl jsem spočítat, kolik to je ušetřeného času, ale pak jsem si všiml, že to píše přímo CircleCI ve svém UI, takže rovnou vidím, že je to celé zhruba o 35 % rychlejší.

Teď můžu případně optimalizovat některé skripty, aby byly rychlejší, ale vlastně to ani nemá moc smysl dělat u všech. Jen u těch, které jsou nejdelší a zdržují celý paralelně běžící balík.

Některé věci se mi ještě nepovedlo dořešit. Nefunguje správně posílání mailů a musel jsem ho na chvíli vypnout, aby se v pondělí neposlalo nějak moc mailů. Taky jsem ztratil historii nabídek práce a musím je nějak obnovit a možná celé vymyslet jinak.


## Přednáška v klubu

Protože je u babičky špatný internet, jel jsem na přednášku v klubu ke švagrovi s tím, že tam pak i přespím, večer pokecáme a uděláme na zahradě druhý den nějakou práci. Bohužel jsem na místě zjistil, že má úplně stejně špatný internet, 10/1. S tímhle se fakt nedá streamovat na YouTube a vlastně je skoro i problém mít vůbec stabilní videohovor.

Měl jsem fakt za to, že tam je internet rychlejší, ale jak se říká, myslet je hovno vědět. Nebo jak říkal jeden lektor v Londýně, slovo assumptions začíná slovem ass.

Přednášku jsem tentokrát připravil skvěle a všechny úkony udělal správně, okna měl správně, tlačítka zmáčknul správně, ale co mi to pomohlo, když mi vypadával internet a speakera jsem ani neslyšel. Úplný fail. Odpojil jsem z wifi i svůj mobil, vypnul všechny ostatní programy, ale stejně, nepomohlo to. Stream rozhodně ne, ale ani záznam neměl moc smysl a po čase jsem to vypnul, protože by na záznamu bylo jen chrčení.

Michala, přednášejícího, jsem na to před přednáškou upozornil a omluvil jsem se. Nabídl se, že může udělat záložní nahrávku u sebe, ale po přednášce jsme zjistili, že se mu nepovedlo nahrát zvuk :D Mám teď jeho soubor s nahrávkou a nějaké svoje, ale neměl jsem zatím čas to nějak poslepovat nebo analyzovat, zda má smysl z toho něco vůbec dělat. Jen jsem se omluvil lidem v klubu, že záznam nejspíš ani nebude.

Měl jsem pak dost blbou náladu, ale nějak se spravila soutěží o knihu (viz dál) a večerním pokecem u vína. U švagra byl na přednášku aspoň v oddělené místnosti klid, protože u babičky není moc kam se takhle schovat. Ale pro příště vím, že buď si v našem Zlínském „letovisku“ zařídím lepší internet, nebo že odtamtud prostě přednášky dělat nemůžu.

Ale investorku napadla ještě jedna věc, která možná není vůbec blbost: Měl bych najít někoho, kdo ty přednášky bude řídit za mě a bude to jeho jediná práce! Tím by se mi dost podstatně uvolnil i kalendář. Stejně jen klikám na tlačítka, uvádím speakera, atd. Je to perfektně delegovatelné.


## Soutěž o knihu

[Martin Michálek](https://www.vzhurudolu.cz/) dal klubu pět svých knih [CSS: moderní layout](https://www.vzhurudolu.cz/css-layout/), abych je rozdal členům. Jeden kus mám doma s věnováním a mohu říct, že je to moc pěkná a užitečná kniha. Muselo to dát strašné práce! 440 stran, 904 gramů.

Dlouho jsem přemýšlel, jak knihy rozdat. Nechtěl jsem dělat jen nějaké hlasování a losování. Trvalo mi měsíce něco vymyslet, ale s výsledkem jsem velmi spokojený. Lidi měli napsat, která oblast CSS jim dala nebo dává nejvíc zabrat - museli se ji složitě učit, nešla moc dobře pochopit, atd. Připojili větu o tom, proč to nešlo, co si myslí, že na tom bylo nejsložitější, nebo hodili odkaz na nějaký návod, díky kterému se to konečně naučili. Příklad ze života (mého):

> **CSS flexbox** - měl jsem zmatek ve všech těch vlastnostech a nepamatoval jsem si je. Procvičoval jsem je přes https://flexboxfroggy.com/, ale stejně mi to nepomáhalo. Nakonec mě vyučila až praxe, prostě jsem se to snažil použít. Nejvíc jsem čerpal z https://css-tricks.com/snippets/css/a-guide-to-flexbox/ a dodnes to mám v záložkách a pravidelně to při psaní CSS otevírám, nedám bez toho ani ránu.

Z lidí, kteří takto odpoví, jsem losoval pět výherců, náhodně. Následně jsem je kontaktoval, dali mi korespondenční adresu a Martin jim knížku pošle. Nezáleželo na tom, jakou práci si s příspěvkem dali, ale věřil jsem, že se posnaží a pokusí se fakt rozepsat a přidat odkazy, abychom se všichni něco díky této soutěži naučili. A fakt se všichni snažili!

Vzniklo nádherné vlákno, užitečné všem. Jak samotným soutěžícím, tak i Martinovi, který si z toho udělal poznámky na svoje další výukové činnosti a materiály. Soutěž jsem nechal běžet skoro měsíc a vyhodnocoval jsem ji 1.11. večer po přednášce.

Udělal jsem to trochu napínavé a že byli zrovna lidi online, tak se v den losování spustila lavina memů a gifů a mělo to perfektní atmosféru. [Natočil jsem video z losování](https://youtu.be/If8fVpUrzCM), schválně jako screencast toho, jak to losování programuju, aby to bylo poučné, a nahrával jsem ho pak na YouTube, ale jak jsem byl na strašně pomalém internetu, tak to trvalo věčnost a lidi byli o to víc napjatí. Chtěl jsem tam dát mp3 s „to sou nervy“ z [opravy traktoru](http://milujipraci.cz/), ale zjistil jsem, že je za tím ještě „ty pi*o“ :D tak jsem to ještě ořízl v Audacity a dal to do klubu bez toho, což sklidilo velký ohlas :D

Některé to tak nabudilo, že i když knihu nevyhráli, šli si ji koupit :D Takže se to fakt celé moc hezky povedlo a měl jsem z toho pak dost dobrou náladu.


## ADHD

Kdysi jsem četl [článek](https://www.theguardian.com/society/commentisfree/2020/jan/15/a-new-life-being-diagnosed-with-adhd-in-my-40s-has-given-me-something-quite-magical), který mě trochu nalomil, ale pak jsem nad tím mávl rukou, že diagnostikovat se z internetu na takové věci je asi jako číst si horoskopy.

No ale teď přišlo ještě [tohle](https://www.mujrozhlas.cz/vinohradska-12/dospeli-adhd-nemate-ho-taky-snaz-se-pozna-lide-jsou-ochotnejsi-problemy-resit) a [tohle](https://denikn.cz/1000209/studio-n-jak-se-zije-s-adhd/) a dostala se ke mě [tahle příručka](http://nepozornidospeli.cz/images/ADHD_prowebFIN.pdf). Jak jsme byli u babičky, měl jsem konečně čas se tím trochu probrat a začínám mít fakt velmi vážné podezření, že je to přesně o mně! Jako by to vysvětlovalo celý můj život :D

Nad tímhle rukou mávnout už nemůžu. Bylo by to nějak moc náhod najednou. Jsem vlastně už docela přesvědčený, že to mám, ale určitě zkusím vyhledat někoho, kdo by mi mohl udělat diagnózu. Nevím, kdy na to zase budu mít čas, ale zkusím svoje pátrání po kouskách posouvat dál.


## Další poznámky

- Napsal jsem na Twitter [kritiku článku, který vyšel na Seznam Zprávách](https://twitter.com/honzajavorek/status/1588147581544239104).
- Řešil jsem, proč se moje loggery na JG jmenují každý jinak. Některé mají celou cestu k modulu, s tečkama, jiné mají jen název modulu. Pak jsem zjistil, že `__name__` [funguje jinak pro balíčky a jinak pro moduly](https://docs.python.org/3/library/__main__.html#name-main) :-o Nikdy jsem si toho nevšiml. Takže jsem všude změnil, jak se loggery pojmenovávají a dělám to parsováním `__file__`, ať to mám všude stejně a tak, jak mi to vyhovuje.
- Odpovídání v klubu, maily, a tak dále. V klubu se roztrhl pytel s CVčky a i když jsem jich postupně prošel snad 10, tak tam na mě dalších 10 čeká.
- Koukal jsem na [diskcache](https://grantjenks.com/docs/diskcache/tutorial.html), jestli by mi nemohla pomoci s urychlením některých skriptů, ale přišlo mi to nějaké moc složité pro můj případ.
- Koupil jsem si [Four Thousand Weeks](https://www.oliverburkeman.com/books), ale nedočetl jsem zatím ani úvod, vždycky jsem usnul.
- S Matějem Kotrbou v návaznosti na přednášku v klubu připravujeme něco o věcech, které by firmy fakt neměly říkat lidem na pohovoru.
- Do svého osobního kalendáře přednášek jsem přidal automatický event týden před přednáškou, který mi připomene, že mám přednášku propagovat.
- Měl jsem mít schůzku s někým, kdo chce založit vzdělávací byznys, ale nakonec to nevyšlo. Třeba příští týden.
- Zjistil jsem, že existuje [SwitchUp](https://www.switchup.org/), neznal jsem.
- Viděl jsem [video](https://www.youtube.com/watch?v=TTisy5gmP7I), ze kterého je vystřižený dramatic look chipmunk.
- Komunikoval jsem s klientem a při tom jsem mu chtěl poslat nějaká čísla k našemu podcastu. Tak jsem se přihlásil do všech služeb a zjistil je. YouTube 147 subscribers, 969 views. Google Podcasts 97 subscribers, 463 meaningful plays. Spotify 484 followers, 979 listeners (= unikátní lidi, kteří si pustili epizody), 4357 streams (= přehrání delší než minutu). Apple Podcasts 172 followers, 195 engaged listeners, 3000 plays. Plus 3100 unikátních návštěv, 4800 zobrazení [webové stránky podcastu](https://junior.guru/podcast/), kde se dá epizody pustit nebo stahovat přes RSS, ale kde neměříme stáhnutí samotných souborů s mp3. Čísla jsou za poslední rok, tedy za celou dobu existence podcastu.
- Poslouchal jsem prima epizodu [ProgramHRování s Lumírem](https://www.programhrovani.cz/1843229/11599562-o-organizovani-meetupu-s-lumirem-balharem), který rozjel Python komunitu v Ostravě.
- Prošel jsem si konečně [fotky z CBW 2022](https://photos.google.com/share/AF1QipNwruVI0RmvsKp3S34P8_OM_mAQJNaPoovZ5OraGDD-ncSDpEU6jIf_4ENItxoyXg?key=QllETmJUcm9sdExBWERfeWcxbWozZ01sRU5yUjB3) a zjistil jsem, že tam mám spoustu pěkných fotek!
- Měli jsme schůzi výboru Pyvce. Řešily se hlavně účty na Google a jejich organizace. Pokusil jsem se zase o kousek posunout [práci na opravě chyby](https://github.com/pyvec/docs.pyvec.org/pull/292) v jednom Pyvec repozitáři a mám se ještě ozvat advokátce a něco jí připomenout.
- S [Lukášem Augustou](https://www.designui.cz/landing-page-odshora-az-dolu?referral_code=31kql18) jsme si psali, že by bylo fajn, kdyby [Memberful](https://memberful.com/) zavedl češtinu. Ze sportu jsem napsal do Memberful na support, jestli to stále ještě neplánují (už kdysi jsem to po nich chtěl a Lukáš prý taky, ale bez velkého efektu). Nejdřív odepsali zase něco neurčitého, ale pak napsali, že češtinu zavedou! Wow! To jsme fakt nečekali :D Takže z JG už konečně nebudou chodit maily, které jsou napůl anglicky a napůl česky. A registrace a administrace budou taky česky.
- YouTube zavádí podporu pro handly, tak jsem si pro [kanál JG](https://www.youtube.com/channel/UCp-dlEJLFPaNExzYX079gCA) zaregistroval handle `@juniordotguru`, podobně jako na dalších sociálních sítích, kde nebylo volné přímo juniorguru.
- Prošel jsem si sloupec v Trellu, který mám na administrativní úkoly a který už přetékal všelijakým bincem. Spoustu úkolů jsem smazal, seřadil jsem to podle priorit, roztřídil co patřilo jinam.
- Koordinoval jsem návštěvu kamarádů z Namibie a Zimbabwe v Praze příští týden. Přijedou na The Ubuntu Summit a nejspíš se poprvé po více jak 2 letech od mé návštěvy [PyCon NA](https://na.pycon.org/) uvidíme!
- Zpracoval jsem dvě žádosti o stipendium. Změnil jsem texty a otázky ve [formuláři na stipendium](https://docs.google.com/forms/d/e/1FAIpQLSeJ_Bmq__X8AA-XbKqU-Vr1N6fdGHSBQ-IuneO5zhBcGCOgjQ/viewform?usp=sf_link). Hlásili se mi lidi, kteří za klub akorát nechtěli platit, ne že na to neměli. Hlásili se mi lidi, kteří klub ani nevyzkoušeli, i když je tam napsané, že to vyzkoušet mají. Některé otázky byly pro odpovídající špatně rozlišitelné a psali do nich skoro totožné texty. Tak jsem to udělal trochu jinak a součástí formuláře je nyní bohužel i dotaz „Proč je pro tebe 109 Kč měsíčně za podpůrnou skupinu příliš drahé?“
- Nainstaloval jsem si [Rome: Total War](https://en.wikipedia.org/wiki/Rome%3A_Total_War) a prošel tutoriál. Na víc jsem se nezmohl a když jsem měl chvilku, zahrál jsem si zase [0 AD](https://play0ad.com/).
- Viděl jsem [GP Mexika](https://www.formula1.com/en/racing/2022/Mexico.html) a byla to mega nuda.
- Na uvítací zprávu od bota, kde lidi prosí, aby napsali v [jaké juniorní fázi podle příručky](https://junior.guru/handbook/) jsou, nikdo moc neodpovídá. Tak jsem to zkusil předělat tak, že bot rovnou pod svou zprávou udělá reakce s čísly, na které stačí kliknout. Při tom se mi povedlo udělat chybu a bot očísloval spoustu jiných zpráv, nebo čísla dával v náhodném pořadí, ale asi jsem to už opravil.
- Propagoval jsem [novou epizodu podcastu](https://junior.guru/podcast/) s Markétou Lourenco o cestě od lingvistiky k datové analýze. Propagoval jsem přednášku v klubu s Michalem z Codeac.
- Během 14 dní od 22.10. do 4.11. jsem naběhal 19 km. Celkem jsem se hýbal 2 hodin a zdolal při tom 19 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/). Nabídky práce pro juniory teď inzerují: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/215426887eaaad9105ecf647d0ff24cf94de7c9eb47cc6f2c55e6921/)


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Věnovat se kamarádům z Namibie a Zimbabwe, kteří přijedou do Prahy na konferenci.
2. Změřit, jak moc a jestli vůbec lidi čtou tipy v onboardingu.
3. Vyřešit poslední nefunkčnosti týkající se CI buildu.

**Bonus:** Zadat práci kamarádovi, který se tváří, že by mohl dělat rozhovory s juniorama, které bychom pak publikovali na JG.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Hodina na počítači denně je přežitá, technologie už slouží dětem jinak, říkají autoři výzkumu o digital teens](https://www.universitas.cz/osobnosti/9216-hodina-na-pocitaci-denne-je-prezita-technologie-uz-slouzi-detem-jinak-rikaji-autori-vyzkumu-o-digital-teens)<br>Zajímavý vhled do toho, jak se pracuje s technologiemi ve školách… a jak by se pracovat mohlo…
- [Putinovi se daří zdejší společnost dělit. Naštěstí ale ne dost, říká sociolog Buchtík](https://zpravy.aktualne.cz/domaci/rozhovor-putinovi-se-dari-zdejsi-spolecnost-delit-nastesti-a/r~6eaae5c44ec211ed8c6f0cc47ab5f122/?utm_source=pocket_mylist)<br>Jak moc je společnost názorově rozdělená? Méně, než si z Twitteru myslíte.
- [Osobní rozvoj převrátil naruby: Co je klíč ke štěstí? Přijít na to, jak klást nohu před nohu](https://denikn.cz/860121/pres-deset-let-psal-o-tom-jak-zit-stastnejsi-zivot-lide-chteji-po-priruckach-spasu-zadna-neni-a-je-to-v-poradku/?cst=43f957f78e1ed537d7e62567c37b1ade7054d735)<br>„Myslím si, že jedna z děr, které po sobě v křesťanské kultuře zanechalo náboženství, souvisí s touhou po zdůvodnění své existence. Spása spočívá v myšlence, že má naše místo na planetě jakýsi smysl. Náboženství vám tento důvod dává. Pokud ale věřící nejste, můžete nabýt pocitu, že své existenci dáte význam, když toho budete dělat dostatečně mnoho.“
- [Začala emancipace mediálních hvězd. Podcast Kecy a politika je silný jako malé vydavatelství](https://mimo-agendu.ghost.io/zacala-emancipace-medialnich-hvezd-podcast-kecy-a-politika-je-silny-jako-male-vydavatelstvi/)<br>„Pickey, Gazetisto, HeroHero nyní bojují o to, aby vysvětlili, že za kvalitní obsah se platí. V budoucnu se ale budou muset přeměnit na talentové agentury, které kromě platební brány poskytnou klientům i vedení, aby jejich obsah vzkvétal a naplnil svůj potenciál. Koneckonců něco podobného už dělá u velkých autorů v zahraničí Substack. Poskytuje právní služby, editace textů i prostor k psaní s pokrytím nákladů na zkoušku.“
- [Co je psáno, není dáno. Online média mění názvy článků i několikrát za den](https://a2larm.cz/2022/10/co-je-psano-neni-dano-online-media-meni-nazvy-clanku-i-nekolikrat-za-den/)
- [Jak se žije s ADHD](https://denikn.podbean.com/e/jak-se-zije-s-adhd/)<br>Naprosto přesně já :-|
- [Sebrali lidem kvůli parkování kus chodníku, nepomohli nikomu. Víc míst = víc aut](https://denikn.cz/994039/sebrali-lidem-kvuli-parkovani-kus-chodniku-nepomohli-nikomu-vic-mist-vic-aut/?cst=7331f61dd1abdd4a7b3c1bfa750e4eaad81cd26c)

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu jsem použil vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
