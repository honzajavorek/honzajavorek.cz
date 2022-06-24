Title: Týdenní poznámky #94: Přemýšlení, psaní a čištění
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (21.6. — 24.6.) a tak [stejně jako minule]({filename}/2022-06-20_tydenni-poznamky-93-konference-a-dalsi-akce.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Poslední poznámky jsem psal v pondělí, ale chtěl bych najet na klasický páteční rytmus, takže dnes píšu další. Snad to bude díky tomu aspoň krátké.

## Text v hlasových kanálech a upgrade PyCordu

Discord zavedl [textový chat v hlasových kanálech](https://support.discord.com/hc/en-us/articles/4412085582359). V klubu jsem tedy zrušil kanál, který to suploval a změnil bota, aby používal novinku, například při ohlašování nadcházející přednášky.

Zjistil jsem, že abych to mohl udělat, musím upgradovat knihovnu py-cord, jejíž upgrade jsem dlouhodobě prokrastinoval, protože novější verze všechno rozbila. Pustil jsem se tedy do toho a za pár minut odhalil podle changelogů příčinu. Stačilo nastavit nějaké nové oprávnění (_intent_) pro čtení obsahu zpráv na Discordu a vše začalo zase fungovat.

## Přemýšlení

Investorka (manželka) se mě zeptala, co plánuji dělat tento týden. Rozjel jsem nekonečný monolog, u kterého jsem si uspořádal myšlenky a rozhodl o některých věcech. Investorka byla potěšena, že mi pomohla, ač to bylo metodou [gumové kachničky](https://en.wikipedia.org/wiki/Rubber_duck_debugging). Cílem je především zjednodušení byznysu, abych nedělal deset věcí tak trochu, ale dvě nebo tři, ale pořádně.

- Nebudu už vzdělávacím agenturám nabízet program pro jejich studenty, kdy je na 3 měsíce posílají do klubu a proplácejí jim vstup. Dokud o to bude mít zájem SDA, budu jim to poskytovat a nebudu na to sahat, ale nedává mi smysl nabízet to dalším, protože si na základě průzkumu myslím, že hodnotu, kterou dodává klub, pokrývají ostatní agentury jinak. Měl to být produkt pro víc firem, nakonec jej využívá jediná (i když jiná, než která jej vymyslela). Přináší to lidi do klubu a peníze, ale je to _distraction_ od toho hlavního, co bych měl dělat. Už teď to je hodně specialit v procesech i v kódu.
- Nejsem zatím přesvědčen o tom, že má smysl dělat nějaké velkolepé plány kolem stipendia. Nechám prostě vystavený formulář a když tam spadne někdo zajímavý, ozvu se Janovi z Mews a uvidíme, zda nám bude dávat smysl člověka podpořit i nějak víc. Zatím nebudu hledat víc firem, které by do tohoto se mnou šly.
- Omezím režii kolem dobrovolných příspěvků. Už delší dobu je nepropaguji, protože chci, aby mi peníze chodily primárně skrze moje podnikání, ne skrze Patreon a GitHub Sponsors. Bez dobrovolných přispěvatelů by dnes JG nejspíš neexistovalo, ale teď je čas se postavit na vlastní nohy. Rušit profily nebudu, bránit lidem podporovat mě nebudu, ale osekám vše kolem.
- Zkusím delegovat nějakou práci na marketingu na sociálních sítích.

Toto přemýšlení nepovažuji za dokončené, naopak mám dojem, že jsem skoro ještě nezačal :) Primárním cílem je opravdu zjednodušit byznys tak, aby se šlo snadno soustředit na jednu dvě věci a vedle toho se zabývat samotným tvořením, tedy psaním příručky a programováním robota a dalších věcí.

## Psaní

- Napsal jsem [inzerát na marketingovou výpomoc]({filename}/2022-06-24_vypomoc-na-socialni-site.md), kterou začínám hledat. Budu rád, když mi někoho doporučíte, nebo se sami ozvete, pokud vás to zaujme.
- Společně s datovým analytikem z [Processand](https://www.processand.com/) jsem připravoval jejich inzerát pro juniory na [junior.guru/jobs](https://junior.guru/jobs/). Ještě jsme jej nepublikovali, možná v pondělí.
- Na sociálních sítích jsem propagoval [nový díl podcastu s Markétou Willis](https://junior.guru/podcast/). Protože Markéta lektoruje v Czechitas, nacpal jsem to i do všech FB skupin Czechitas. Bál jsem se, že mi to pomažou, ale místo toho se mi ozvala adminka ostravské skupiny, o které jsem ani nevěděl, jestli bych to tam nedal taky.
- Klub, maily, a tak dále. Komunikoval jsem hlavně ohledně stipendií a firemních členství.
- Domlouval jsem se s [Codeac](https://www.codeac.io/) na tom, jak si můžeme vzájemně pomoci. Jeden z nápadů je, že by mohl jejich nástroj pomoci s automatickým připomínkováním projektů juniorů, např. že se necommitují tokeny do Gitu, že se nedělá to a tamto.

## Čištění

- Začal jsem čistit historické členy v klubu, kteří tam jsou od samého začátku, ale následně už nijak nekomunikovali a nepovedlo se mi je převést na účty v Memberful. To mi dlouhodobě komplikuje kód, statistiky, atd. Vyházel jsem všechny až na [Martina](https://www.vzhurudolu.cz/), kterému pak musím ještě napsat a ukecat ho, aby se mi doklikal do Memberful.
- Zrušil jsem studentské kupóny, které původně měly být pro jednu vzdělávací agenturu, ale která je nakonec nikdy nevyužila a nevyužije.
- Udělal jsem pořádek ve studentech [CoreSkillu](https://coreskill.tech/), kteří byli z historických důvodů na všelijakých kupónech a byl v tom dost zmatek.
- Pár měsíců zpět jsem myslel, že jak firmy budou prodlužovat členství, budu další roky řešit pomocí dalších kupónů. Podle toho jsem začal vydávat obskurně komplikovaně skládané kupóny, ve kterých bylo dokonce i číslo faktury. Pak jsem ale přišel na to, že mohu botem prodlužovat lidem délku členství a mohou přitom zůstat na předplatném, které už mají. To vše extrémně zjednodušuje. Nyní jsem celou mechaniku se složitými kupóny smazal z kódu a všechny složité kupóny zjednodušil.
- Smazal jsem ze systému všechny neaktivní slevové kupóny.
- Smazal jsem vánoční stránku s dárkovým členstvím v klubu. Smazal jsem animaci padajícího sněhu. Tolik práce to bylo a přineslo to nakonec 3 členství v klubu. Trvalo mi půl roku, než jsem se dokázal vypořádat s tím, že to nejlepší, co mohu v této věci udělat, je smazat to z kódu a už takové blbiny nikdy nedělat.
- Promazal jsem staré archivované kanály v klubu. Většina z nich tam byla rok pouze pro čtení a jejich hodnota byla už nulová.
- Smazal jsem stránku `/donate/` a zatím přesměroval na `/open/`. Mám nějaký nápad, jak by se to dalo jednou udělat lépe, ale teď jsem chtěl hlavně odstranit dávno neaktuální prosbu o dobrovolné příspěvky.
- Překopal jsem svoje profily na GitHub Sponsors a Patreonu. Původní texty jsem si [uložil sem](https://gist.github.com/honzajavorek/ed2036751a65c6e6820e4c813b9d950d). Oba profily jsem předělal do angličtiny a napsal jsem tam jednotný text, kde vysvětluji co zhruba teď dělám a že nikomu nebudu bránit mě podporovat, ale že si mohou taky normálně koupit členství v [klubu](https://junior.guru/club/). Výsledek bude zhruba stejný, ale z peněz se strhne méně poplatků. U jednotlivých částek jsem dal jasně najevo, že za to podporující nic na oplátku nedostává. Nikdo totiž nikdy nic reálně nechtěl realizovat ani z těch „výhod“, které jsem tam doteď měl.
- Členům, kteří už mě nepodporují ani na GitHub Sponsors ani na Patreonu jsem odebral kupón, který jim zajišťuje členství v klubu zdarma. Většina z nich jej stejně nevyužívala a členství měla jen nominálně. Nepotřebuji nafukovat čísla mrtvými dušemi.

## Další poznámky

- Nahrál jsem [slajdy ze své páteční přednášky na SpeakerDeck](https://speakerdeck.com/honzajavorek/we-are-the-robots).
- Domluvil jsem se s [Martinem](https://www.vzhurudolu.cz/), jak budeme distribuovat výtisky jeho nové knihy členům klubu. Mohu rozdat pět knih. Teď už jen vymyslet, jak to udělám. Přijde mi asi škoda to zase nějak náhodně losovat, chtělo by to nějakou reálnou soutěž nebo to použít jako cenu za něco, no ještě uvidím.
- Na základě předchozích poznámek mi bylo doporučeno [toto video](https://www.youtube.com/watch?app=desktop&v=0DyWG1JiDYk) na protahování rukou. Zkusil jsem.
- Ozval se mi starý kamarád z dalekých krajů, že je zrovna v Praze. Vzal jsem si den volno a strávil s ním pěkné odpoledne.
- Narazil jsem článek o [jednoduchém triku, jak psát úderně a stručně](https://sive.rs/1s). Třeba ho někdy dočtu a začnu to praktikovat.
- Během 4 dní od 21.6. do 24.6. jsem naběhal 10 km. Celkem jsem se hýbal 2 hodin a zdolal při tom 10 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště jsou stejné jako minule, protože jsem žádnou z nich nedokázal dokončit a jsou stále nejdůležitější:

1. Zjistit, co můžu zrušit, delegovat, nebo automatizovat, abych měl víc času na samotné tvoření.
2. Spočítat po čtvrt roce zase domácí finance a vymyslet nový ceník.
3. Podívat se na inzerát pro Processand.

**Bonus:** Vymyslet MVP robotického onboardingu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Twenty years of my blog](https://getpocket.com/redirect?&url=http%3A%2F%2Fsimonwillison.net%2F2022%2FJun%2F12%2Ftwenty-years%2F%23atom-entries&h=ca4f550019d1bc801e67699b9b0107f7ea902e99346e3638f7efc55258404be3)<br>Boží průlet Simonovou historií.
- [Lanyrd: from idea to exit - the story of our startup](https://getpocket.com/redirect?&url=https%3A%2F%2Fblog.natbat.net%2Fpost%2F61658401806%2Flanyrd-from-idea-to-exit&h=b6f474917857bbfac380b7ee4b225feb41cfdf60c2459c16066c425734c9d4d5)<br>Proč nezakládám firmu, v jedné větě: „We moved from building the product to building the machine that builds the product. This meant hiring a team and designing a company.“
- [The Left-NIMBY canon](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2Faz0WjVgkYN%3Fssr%3Dtrue&h=7fd47fbeefc5f9fcb8d4fe92452fb5a8f7638024c18734e842e755f277a8277f)<br>Různé pohledy na řešení krize bydlení. Levicové NIMBY vs YIMBY.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
