Title: Týdenní poznámky #107: Rozjíždění přednášek, opravy všeho možného
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (1.10. — 7.10.) a tak [stejně jako minule]({filename}/2022-09-30_tydenni-poznamky-106-onboarding-clenu-volby-a-pulmaraton.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Domlouvání přednášek

Hodně času jsem strávil dolaďováním a plánováním přednášek. Aktuálně jsem ve stavu, že jsem zaplnil kalendář až do Mikuláše. Pak si dám možná už rovnou nějakou vánoční pauzu. Během té bych se měl zamyslet, jak příště na přednášení pozvat víc ženských. Asi prostě budu na leden a dál zvát pro změnu zas jenom ženské, ať se to trochu srovná.

Všechny naplánované přednášky jsou na [stránce s akcemi v klubu](https://junior.guru/events/). První přednáška bude už ve středu příští týden. Jsem trochu ve stresu, protože po dlouhé pauze už upřímně vůbec netuším, jakým způsobem jsem dělal přednášky v klubu a určitě to nějak pokazím a na něco zapomenu. Mám naštěstí aspoň [check list](https://gist.github.com/honzajavorek/b1a77651e566cb6405a131bbf1fb0692), ale ten taky není všespásný.


## Vylepšování skriptu na oznamování přednášek

Po čase jsem se vrátil k myšlence, že by mohlo jít přes bota nahrávat obrázek k Discord eventu. Předchozí pokusy se mi nějak nedařily, nepřišel jsem na to, jak to udělat a akorát jsem založil [dotaz na SO](https://stackoverflow.com/q/72134026/325365), který nikdo neodpověděl.

Když jsem se do toho trochu ponořil a četl jsem si kód pycordu, zjistil jsem, že parametr na nahrávání obrázku nepřijímá `Asset`, ale normálně bajty s obrázkem. Je to akorát špatně zdokumentováno!

Takže jsem poslal [opravu](https://github.com/Pycord-Development/pycord/pull/1667) a tím jsem poprvé přispěl do pycordu :) Na svou SO otázku jsem [napsal vlastní odpověď](https://stackoverflow.com/a/73989454/325365). A naimplementoval jsem nahrávání obrázku. Musel jsem vygenerovat obrázek pro Discordí rozměr, aby se nikde neořezával. Tento rozměr není moc vysoký a nešlo tam nacpat vše, co je na aktuálním plakátu, takže jsem pomocí media query v CSS zajistil, že se určité kousky plakátku schovají, když má být výsledek moc nízký na výšku.

Díky tomu, že mají teď Discord eventy obrázky, začal jsem dávat do různých automatických oznámení v klubu odkazy přímo na ně. Touto změnou jsem způsobil několik chyb, které jsem v dalších dnech postupně opravoval. S výsledkem jsem ale spokojen, lidi se teď mohou rovnou z oznámení na eventy přihlašovat.


## Prosekání „SEO lapačů“

Brutálně jsem prosekal „SEO lapače“, které jsem měl na různá klíčová slova, např. tento na [Advent of Code](https://junior.guru/topics/adventofcode/). Měl jsem tam snad 40 různých klíčových slov, které se hledaly v klubu a prezentovaly na takovýchto podobných stránkách.

Už dlouhou dobu jsem sledoval, že nejvýkonnější jsou lapače, které jsou o vzdělávacích agenturách, tedy o kurzech. Nejdřív mi o tom chodily maily z Google Console, pak jsem to viděl už i [přímo v Simple Analytics](https://simpleanalytics.com/junior.guru?search=paths%3Atopics&period=year&count=1). Do těch jsem se teď podíval a co mělo méně než zhruba 30-40 návštěv za celý rok, to jsem zrušil. Prakticky jsem tedy zrušil veškeré lapače na technologie, asi až na Python a JavaScript, kam lidi opravdu chodí. Git a GitHub jsem přesměroval na [stránku v příručce](https://junior.guru/handbook/git/), i když není úplně dopsaná. Lapač na Learn2Code jsem přesměroval a upravil, protože se přejmenovali na [Skillmea](https://junior.guru/topics/skillmea/).


## Další poznámky

- Užíval jsem si týden, kdy jsem nešel na žádnou akci a ničeho jsem se neúčastnil. Bylo to osvěžující. Několik akcí v budoucnu jsem z různých nesouvisejících důvodů odmítl a nevadí mi to. Jsem zřejmě přesocializovaný a potřebuji dobít baterky.
- Přesměroval jsem všechny historické stránky příručky pod `/handbook/`, se všemi přesměrováními a s opravami odkazů napříč celým webem. Na starých stránkách webu, kam jsem se už dlouho nedíval, jsem našel hromadu neaktuálních odkazů, které jsem taky v rámci možností opravoval.
- Napsal jsem pár lidem, kteří dostali stipendium a zeptal se jich, jak se jim daří. Jedna členka odepsala, že si našla práci!
- Přečetl jsem vše v klubu, podíval jsem se tam na několik výrobků a CVček.
- Opravil jsem skript, který mi na webu kontroluje rozbité odkazy. Neuměl se vypořádat s odkazy na obrázky. Upřímně nerozumím tomu, proč se to projevilo až teď.
- Měli jsme schůzi výboru Pyvce. Pořešili jsme pár věcí. Vyčistil jsem náš Trello workspace od starých Trello boardů. Napsal jsem advokátce, aby nám pomohla upravit stanovy. Vzal jsem [čerstvě vydaný článek na českém Python blogu o letních sprintech](https://blog.python.cz/Letni-sprinty-Python-komunity-v-Msenem) a nasdílel ho aspoň na Facebook a Twitter. Na Facebooku se pod ním tradičně objevily debilní komentáře a já si zase uvědomil, jak na tu sociální síť už fakt nějak nemám nervy.
- Všiml jsem si, že je asi nějaká chyba ve [skriptu](https://github.com/pyvec/docs.pyvec.org/blob/master/_scripts/generate_grants.py), který Pyvci dokumentuje přidělené granty. Informace jsou [tady v komentářích](https://github.com/pyvec/docs.pyvec.org/pull/292). Kdo umíte kódit v Pythonu, pomoc vítána.
- Vylepšil jsem pravidelnou zprávu, kterou bot posílá do kanálu v klubu, kde se řeší CV, GitHub, LinkedIn. Dává lidem tipy na věci, které si mají přečíst, než nás budou žádat o zpětnou vazbu, třeba [návod na CV](https://junior.guru/handbook/cv/).
- Propagoval jsem na sociálních sítích [svou účast v podcastu Street of Code](https://streetofcode.sk/podcast/juniorguru). Epizodu jsem si pouštěl do vlastních uší a bylo to tak dobré, jak jsem si to pamatoval z nahrávání. Tenhle rozhovor se nám fakt povedl a jsou v něm věci, které jsem jinde neříkal :)
- Propagoval jsem na sociálních sítích středeční [přednášku v klubu s Pavlem Šabatkou o tom, jak se stát webovým analytikem](https://junior.guru/events/).
- Vymyslel jsem, jak rozdám [knihy od Martina Michálka](https://www.vzhurudolu.cz/css-layout/), kterých mám pět kusů na rozdávání v klubu. Lidi budou psát, s čím v CSS měli největší problém a jak to případně překonali. Z respondentů pak vylosuju pět, kteří knížku dostanou. Soutěž jsem v klubu rovnou dnes zahájil, bude trvat do prvního listopadu.
- Z [této stránky](https://junior.guru/handbook/learn/) jsem vyčlenil jednu sekci do [separátní kapitoly](https://junior.guru/handbook/help/). Chci ji přepsat, rozšířit, vylepšit. Cílem je, aby mi pak odkaz na tuto stránku pomohl s onboardingem členů do klubu.
- Začalo mi padat CI a bot kvůli tomu několik dní nejel. Když jsem se konečně dostal k debugování, zjistil jsem, že to dělá nový argument `suppress`, který jsem v pycordu začal používat hned po vydání nové verze knihovny. Bohužel zjevně nefunguje moc dobře. Založil jsem [issue](https://github.com/Pycord-Development/pycord/issues/1674) a opravil jsem kód tak, aby problém obešel.
- Na chvíli jsem se vrátil k programování skriptu na nahrávání souborů na iCloud, který využívá [pyicloud](https://pypi.org/project/pyicloud/) a který chci používat k nějakým zálohám, ale moc jsem na tom neudělal.
- Minulý týden jsem se tady chlubil, jak se mi povedlo jednoduchým skriptem udělat podcast z jednoho video pořadu. Tak po pár dnech provozu to spadlo, protože tam vznikaly velké audio soubory a limit na GitHub Pages je 100 MB :D Takže jsem to vypnul. Nemám po ruce žádnou CDN, kam bych to nahrával, a hlavně jsem neměl teď čas si s tím nějak dál hrát.
- Odpovídání v klubu, maily, a tak dále. Komunikoval jsem s jednou firmou ohledně prodloužení partnerství s klubem. S jinou firmou jsem o tom komunikovat měl, ale nějak jsem to nezvládl.
- Velkou část týdne jsem se také snažil být co nejlepším kamarádem dvěma kamarádům, kteří ve svých životech zrovna řeší nějaký shit.
- Během 7 dní od 1.10. do 7.10. jsem při procházkách nachodil 13 km. Celkem jsem se hýbal 7 hodin a zdolal při tom 13 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/). Nabídky práce pro juniory teď inzerují: [Monitora media, s.r.o.](https://junior.guru/jobs/2b1ab731247b03b291bd7c4a0177e052df5ae4a5937144b4f2ce9d11/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/34fa3ec07892dd3ff64458e2ccbf12578e00860483427e9e7c4847bc/)


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Zvládnout po dlouhé době první přednášku v klubu.
2. Psát tipy do onboardingu novych členů v klubu.
3. Ozvat se pár firmám, kterým končí spolupráce s klubem.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Cesty Zdopravy - Petr Borecký](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BpkEsC0dgM&h=d07e8e417c78390bdb6719db97ec537ca202eab61c289997b46f88523e93e9c0)<br>Rozhovor o dopravě ve Středočeském kraji.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
