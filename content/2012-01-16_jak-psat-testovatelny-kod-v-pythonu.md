Title: Jak psát testovatelný kód v Pythonu?
Date: 2012-01-16 11:00:00
Lang: cs
Tags: práce, projekty, python, webdesign

![obrázek]({static}/images/164.jpg){: .right }Troufl bych si říci, že na WebExpo 2011 byly [testy](http://zdrojak.root.cz/n/testovani/) jedním z předních vývojářských témat. Ať už šlo o JavaScript, PHP nebo cokoliv jiného, hojně se testování skloňovalo.

Já osobně jsem v testování úplný začátečník. Testy jsem nepsal a nepíšu, ale rád bych se to naučil. Bohužel, na vysokých školách jsem neměl to štěstí být donucen jediný test napsat, pokud tedy nešlo o test mých chabých znalostí ;-)

Už dříve jsem pochytil nějaké základy o testovatelnosti kódu a následně i *dependency injection* (hezky [vysvětlil Fabien P.](http://fabien.potencier.org/article/11/what-is-dependency-injection)) v PHP, která s ním úzce souvisí. Na WebExpu jsem si tyto teoretické znalosti rozšířil díky [workshopu](http://webexpo.cz/praha2011/workshop/jak-napsat-otestovat-tisice-radku-kvalitniho-objektoveho-kodu/). Myslím, že teď už základní principy chápu a schází mi především praxe. Bohužel, jediný PHP projekt, který teď udržuji, je [ConcertIn]({filename}2012-01-02_kdy-a-kde-ma-vas-oblibenec-koncert.md) a ten je na starším [Nette](http://nette.org/) a navíc strašně závislý na Facebook platformě, takže abych něco testoval, musel bych upgradovat framework a polovinu věcí si namockovat. Což se mi pro začátek moc nechce, akorát by mě to otrávilo.

Většinu věcí píšu teď v Pythonu. Bohužel mi tamtéž unikla [přednáška Honzy Krále o testování v Pythonu](http://webexpo.cz/praha2011/prednaska/testovani-prakticky/). Projíždím čas od času [uveřejněné videozáznamy přednášek](http://vimeo.com/webexpo/videos), ale pořád ji tam nevidím.

Se zavedením testů do Pythonu mám ale problém. Ono je totiž PHP (Java, C\#…) jiné než Python a já si prostě ta naučená teoretická pravidla neumím nějak v Pythoním kódu představit. Něco už jsem v tom jazyce napsal a myslím, že je běžnou praxí psát v modulech obyčejné funkce, importovat si je do jiných modulů, importovat si tam a zpět nějaké proměnné, třídy, třídy chovající se jako funkce… Vidím takové věci jak v [Djangu](https://www.djangoproject.com/), tak ve [Flasku](http://flask.pocoo.org/). Python je tak dynamický, že mi dělá problém aplikovat na něj tatáž pravidla jako pro PHP, kde stačí říct „nesmíte ve třídě udělat `new`, nové objekty prostě musí přijít zvenčí připravené“.

Ano, mohl bych jej podrobit přísnému režimu a psát kód, který by byl přísně objektový a všemu vyhovoval, ale to by potom vůbec nebylo *pythonic*, nevyužíval bych toho jazyka plně tak jak byl navržen a tak jak to dělají všichni ostatní. No a to je druhá věc – externí knihovny neovlivním a jsou psány stejným způsobem (tzn. i ve svém API očekávají, že budou použity v podobném *pythonic* kódu). Jednoduše, **šel bych proti přirozenosti Pythonu**. Myslím si, že pes bude zakopaný někde jinde.

Ale kde? No, a to právě vůbec nevím. Hledal jsem po internetu chvíli nějaké *best practices* psaní testovatelného kódu v Pythonu, ale moc jsem toho nenašel. A proto bych vás chtěl poprosit: Pomůžete mi vyřešit tento můj problém? Nemáte odkazy na nějaké dobré zdroje, které bych pročetl a bylo by mi tohle všechno hned jasné? Potřebuji příklady, nějaké ukázky z praxe, kde bych to opravdu pochopil, abych mohl takový kód psát, následně tvořit testy a potom to dělat tak dlouho, než do toho proniknu do hloubky a budu moci poučovat zase druhé ;-) Díky za každý komentář!
