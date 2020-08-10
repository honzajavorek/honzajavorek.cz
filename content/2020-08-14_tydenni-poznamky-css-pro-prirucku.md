Title: Týdenní poznámky: CSS pro příručku
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs


Utekl další týden (3.8. — 9.8.) a tak [stejně jako minule]({filename}/2020-08-07_tydenni-poznamky-dovolenkovani-pripravy-prirucky.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


Pracoval jsem prakticky jen pondělí až středa a co si budeme povídat, moc jsem toho nestihl. Od čtvrtka až do neděle jsem byl v Brně, kde jsem nebyl už strašně dlouho. Navštívil jsem rodinu i kamarády, ale ani tak jsem nestihl navštívit všechny. Povedlo se mi ale aspoň navštívit hned dva klenoty Jižní Moravy, a to [Adamov a Blansko](https://www.idnes.cz/brno/zpravy/pruvodce-to-je-brno-stanislav-biler.A170405_2317327_brno-zpravy_krut/foto/KRU6a610a_Vstiek.JPG).


## Další poznámky

- Po Python "sprintu" předchozí týden jsem se ještě utrhnul k nějakým dodělávkám, a to hlavně k dokončování [archivace hlasování o finančních grantech do naší dokumentace](https://github.com/pyvec/docs.pyvec.org/pull/146).
- Taky hned přišlo několik PR na [Jechovou](https://github.com/pyvec/jechova/). To mě zaujalo, protože Jechová funguje a nic na ní nebylo potřeba měnit, nebylo nic rozbité, ale lidi měli i přesto chuť poslat PR. Vysvětluji si to tím, že její kód je tak jednoduchý, že je bariréra pro přispění hodně malá a lidi motivuje poslat vylepšení i jen tak. Je to možná poučení i pro jiné projekty, které v komunitě spravujeme. Čím jednodušší, tím životaschopnější.
- 2x mentoring session
- Propagoval jsem na internetu [PyCon Africa](https://africa.pycon.org/), který zrovna probíhal online.
- Koukal jsem na [tohle video](https://twitter.com/goodmarketinghq/status/1281592433931948033?s=12) o tom, jak dělat správně pre-launch
- Vytvořil jsem [stránku pro příručku](https://junior.guru/candidate-handbook/), normálně přístupnou a zasazenou do menu. Na ni jsem vytvořil "teaser" na příručku, který můžu dále propagovat. Do úvodního textu jsem se pokusil aplikovat nějaká moudra z videa výše, ale jestli se mi to aspoň trochu povedlo, to netuším.
- Po přidání položky do podmenu jsem si vzpomněl, proč bylo původně vlevo, i když vpravo by možná vypadalo líp. Protože na mobilu se to horizontálně scrolluje a to nefunguje moc dobře, když je to zarovnáno doprava. Takže je podmenu zase vlevo.
- Strávil jsem nějaký čas dolaďováním toho, aby bylo vidět, že se to podmenu dá horizontálně scrollovat. Třeba na mobilu se to otevřelo tak, že nebylo vůbec zřejmé, že jsou za prvními odkazy ještě nějaké další. JavaScriptem tedy detekuji, jak moc co jde vidět, a podle toho to menu na mobilu jakože trochu nedbale odscrolluji, aby bylo jasné, že se scrollovat dá. Nic lepšího mě nenapadlo, designově se takhle podmenu teď dělají, s přístupností se asi nikdo moc nemaže. Já bych se s tím možná taky neměl tak moc mazat, ale jako když mi taková věc pro většinu lidí na mobilu vytlačí odkaz na stránku _Pro firmy_ mimo viewport, tak to nemůžu nechat být.
- Minimálně půl hodiny jsem se snažil doma zabít nebo vyhnat jednu extrémně otravnou mouchu. Vysmívala se mi a sedala si na mě.
- Pomáhal jsem PyLadies s rozhodováním ohledně podzimních kurzů a s nástřelem výpočtu nějakých financí.
- Ladil jsem CSS žlutě zvýrazněných bloků, které na JG upozorňují na různé další věci. Dělal jsem kód obecnější a méně psychedelický, abych tyto bloky mohl použít s různým obsahem a v různých kontextech.
- Tak dlouho jsem přemýšlel jak nacenit "review inzerátu práce", až jsem nabídku od kamaráda asi tak nějak prošvih :( Každopádně - pokud mi někdo pošle pracovní inzerát k okomentování, jak to mám nacenit? Jasně, můžu si dát nějakou pevnou cenu za kus odvozenou třeba od hodiny času, kterou nad tím plus minus strávím. Bojuju ale s tím, že když pošlu zpět 10 připomínek, jde ta práce vidět, ale když ten inzerát bude dobrý, nemůžu přece poslat palec nahoru a k němu fakturu na hodinu práce. Jako strávil jsem ji s tím tak či tak, přečíst jsem to musel, zamyslet jsem se musel, ale klient z toho má jen informaci, že je to dobrý a tak nějak to na mě nepůsobí dobře. Jak to dělají právníci apod.? :D Jak byste takovou věc nacenili?


## Prázdninové tipy

- V Brně zavedli [pípni a jeď](https://pipniajed.cz/). Pro občasné návštěvníky, jako jsem já, je to super. Zajímavé je, že tento způsob placení za jízdné, který jsem zažil poprvé myslím v Londýně, se v ČR šíří z východu na západ. [Nejdříve to měli v Ostravě](https://www.lupa.cz/clanky/daniel-morys-dopravniho-podniku-ostrava-stavime-mhd-rizenou-pomoci-dat/), teď v Brně. Třeba se jednou dočkáme i v Praze!
- Pokud jste kdysi hráli [The Settlers](https://en.wikipedia.org/wiki/The_Settlers), ale dnes máte macOS a tedy vám žádná z těch her nepojede, existuje určitá spása v podobě Open Source hry [Widelands](https://www.widelands.org/) (stačí udělat `brew cask install widelands`). Bohužel je to klon Settlers II. a ne III., takže grafika nic moc, ale herní princip je stejný. Dal jsem tomu zatím tak 2 hodiny, tzn. tutoriál a pár minut kampaně, ale přijde mi, že hrát se to dá.


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Praha chystá cykloobousměrky, Brno je ruší. Policie je považuje za nebezpečné, data ale ukazují opak](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2Fk0ICbaUfsx%3Fssr%3Dtrue&h=0c43ee34861ce5b4c1b0168286654eaaf816e4b1dfcded6f602d87bbdf665af4)<br>Plánuje se plánuje, ale nerealizuje se nic
- [Proti všem. V Bruselu jsme dnes prohráli. Naštěstí. Naše zájmy hájili jiní](https://getpocket.com/redirect?&url=https%3A%2F%2Fnazory.aktualne.cz%2Fproti-vsem-v-bruselu-jsme-dnes-prohrali-nastesti-nase-zajmy%2Fr%7E11aa3ea2cb4711eaa7deac1f6b220ee8%2F&h=9dd2ab14ad0b07b25e8f16179a631a2b73c348dcfc96d791ccb897dacfe8b5a9)<br>Když prohrát znamená zvítězit… Sním o tom, že jednou budou Češi normálním, profesionálním hráčem v EU, který vyjednává, má spojence, zvládá konstruktivní politiku. Jenže my ze sebe stále děláme lojzíky se slámou v botech.
- [Deník N : MeToo v Česku](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2FcMgqw9pObf%3Fssr%3Dtrue&h=7b219f19dd48b6a8b222f9f0a6d1ba8d6f67edd5b6997071f7b17d200f58a458)<br>Skvělý rozhovor
- [The Third Age of JavaScript](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.swyx.io%2Fwriting%2Fjs-third-age%2F&h=d27abfd43e8cbaf3ee493d1cef1a40eece317db4a6e50a3876c2d3bb6590f9da)<br>Vstupujeme do třetí — a poslední — éry JavaScriptu?

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
