Title: Testování v JavaScriptu a v Pythonu
Date: 2016-05-31 10:43:00
Lang: cs
Translation-ID: testing-in-javascript-and-in-python


Štve mě testování serverového JavaScriptu a v tomto článku vám napíšu proč. Pokud nemáte náladu na [rant](http://www.urbandictionary.com/define.php?term=rant), doporučuji si [vybrat jiný článek](https://honzajavorek.cz/blog/).

Jelikož jsem člověk původně ze světa Pythonu, srovnám _developer experience_
u obou jazyků, aby bylo jasnější, co přesně myslím. Ačkoliv jsem velkým
propagátorem jazyka Python, mým účelem není napsat hejt na JavaScript a zdůraznit,
že Python je nejlepší na světě. Chci pouze upozornit na nedostatek v jednom
z těchto dvou ekosystémů. Příště klidně napíšu článek o tom, jak mě štve
balíčkování v Pythonu a proč se mi mnohem víc líbí npm.

## Testování v Pythonu

Hodně lidí při psaní testů v Pythonu používá [unittest](https://docs.python.org/3/library/unittest.html),
modul ze základní knihovny, který lidem umožňuje rychle vytáhnout nějaký ten [XUnit](https://en.wikipedia.org/wiki/XUnit)
způsob psaní testů, plný `class TestNěco`, `self.assertTamto()` a `setUp/tearDown`
tohleto.

Když je testů více, běžně si k tomu člověk vezme nějaký test runner,
třeba [nose](http://nose.readthedocs.io/en/latest/). Test runner je něco, co umí
inteligentně spouštět testy - např. jen ty, které posledně selhaly.

Protože nose testy spouští, umožňuje vyběhnout z XUnit stylu a nabízí spoustu
triků, jak můžete testy vylepšit a zjednodušit. Ty ale nikdo nepoužívá, protože
o nich neví. Nicméně v zásadě platí, že pokud chci pustit jen nějakou podmnožinu
testů, nebo chci upravit výstup testování, existuje na to chytrý přepínač. To je fajn především díky dvěma věcem:

- Konvence (kolega nemusí zjišťovat který konkrétní přepínač používám v tomto konkrétním projektu),
- pohodlí a uživatelská příjemnost (přepínač je po ruce i když ho potřebuju třikrát za život).

No a pak je tady [pytest](http://pytest.org/), což je framework, který zvládne nejspíš vše co nose,
ale navíc k trikům dává programátorům i úplně ulítlé možnosti, jak psát testy
jednoduše. Ačkoliv se v Pythonu [razí spíš _be explicit_ a _no magic_](https://www.python.org/dev/peps/pep-0020/), na oblibě pytestu
se ověřilo, že v případě testů je magie přijatelná a užitečná. Zvyšuje totiž
deklarativnost a čitelnost testů.

Protože za pytestem stojí i člověk, který napsal [PyPy](http://pypy.org/)
(překladač Pythonu napsaný v Pythonu), je ta magie na poměrně hluboké úrovni.
Např. Python má klíčové slovo `assert`, které je ale v základu dost primitivní a umí akorát porovnat dvě
hodnoty a vyhodit obecnou chybu, pokud hodnoty nesedí. Totéž co [funkce assert
v Node.js](https://nodejs.org/api/assert.html). Co ale dělá pytest?
[Pomocí introspekce se hrabe v mezikódu Python interpreteru](http://pybites.blogspot.co.at/2011/07/behind-scenes-of-pytests-new-assertion.html) a [obohatí asserty](https://pytest.org/latest/assert.html) tak,
aby kontextově poznaly, co porovnávají, a podle toho vyhodily pěkné srovnání. Nepotřebuji tedy tahák na `assert.domysliSiSvojiPorovnávacíFunkci`, stačí mi používat
normální opetátory a typy, které se nacházejí v jazyce.

Také se mi líbí, že frameworky mají běžně v dokumentaci sekci o testování a nabízí mi
pomocnou ruku (tipy jak na to, nástroje, třídy k podědění) v tom, abych mohl svůj kód otestovat
snadněji, rychleji, a bez psaní zbytečně detailního [boilerplate kódu](https://en.wikipedia.org/wiki/Boilerplate_code) okolo.
Viz [Flask](http://flask.pocoo.org/docs/0.12/testing/), [Django](https://docs.djangoproject.com/en/1.10/topics/testing/), [Scrapy](https://doc.scrapy.org/en/latest/topics/contracts.html) (odkazy na dedikované kapitoly v dokumentaci).

Ve výsledku se při psaní testů cítím jako v bavlnce. Napíšu web v mikroframeworku,
ale i ten mi kód testů zjednoduší. Běžně je test jen na pár řádků, což šetří čas můj,
mého kolegy, který dělá code review, i všech ostatních, kdo budou ty testy v budoucnu číst. Testy si spustím z jaké složky chci a snadno
si spustím třeba jen ty, které mi posledně neprošly.

## Mocha

Ve světě serverového JavaScriptu, s jakým jsem měl tu čest se v [Apiary](https://apiary.io/) seznámit, je zlatým standardem [Mocha](http://mochajs.org/). Tvrzení _feature-rich_ v podtitulku znamená, že si máte doinstalovat i ten [assert](http://chaijs.com/). Ne, teď vážně. V Mocha vypadají _killer features_ takto:

- Spouští všechny testy a když někam napíšu `.only`, spustím jen ten daný test,
- umožňuje použít _glob patterns_ pro výběr toho, jaké testy chci spouštět,
- umožňuje grepovat přes popisky testů (když grep chytí víc popisků, spustí se víc testů),
- jakože-[BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) přístup, který se skládá z `describe` a `it`,
- tuny boilerplate kódu v `before` nebo `beforeEach` (protože [_Mocha currently has no concept of a shared behaviour..._](https://github.com/mochajs/mocha/wiki/Shared-Behaviours)),
- když spadne test, někdy se ani nedovím, ve kterém souboru nastal problém,
- dokumentace k uzoufání jen o něco méně než ta od [Mongoose](http://mongoosejs.com/),
- vypisuje věci barvičkami a s unicode znakem ✔️, což je velmi cool,
- umožňuje používat jen jeden reporter zaráz (hodně štěstí s generováním test coverage nebo `xunit.xml`).

Pro srovnání, pytest:

- Žádné XUnit třídy, žádné hry na BDD, prostě [jednoduché funkce](http://docs.pytest.org/en/latest/getting-started.html#our-first-test-run) s obyčejnými [asserty](http://pytest.org/latest/assert.html),
- pomáhá odhalovat [co se sakra děje](http://pytest.org/latest/example/reportingdemo.html),
- automatická [správa `stdout` během testů](http://pytest.org/latest/capture.html),
- koncept [fixtures](http://pytest.org/latest/fixture.html) pro psaní závislostí jednotlivých testů,
- [parametrizace testů](http://pytest.org/latest/parametrize.html),
- [distribuované testování](http://pytest.org/latest/xdist.html),
- umí spouštět jakékoliv testy Python světa včetně [nepythoních](http://pytest.org/latest/example/nonpython.html) nebo [testů dokumentace](https://docs.python.org/3/library/doctest.html).

Že se Mocha nebo [Chai](http://chaijs.com/) pomocí introspekce nehrabou v nějakém mezikódu jim nemůžu vyčítat, protože JavaScript
nemá ani introspekci, ani mezikód. Ten zbytek může Mocha nejspíš klidně naimplementovat, ale nedělá to. Je libo feature request na parametrizovatelnost testů (což považuji za základní
funkci obecného test frameworku) i s rantem o tom, jak Mocha maintaineři
nové features odmítají jako nepotřebné, nechávají je vyhnít, nedělají review apod.?
[Prosím](https://github.com/mochajs/mocha/issues/1454).

Jenže to není jen o maintainerech. Dobře, není nabídka, ale ona není ani poptávka. Z vyhledávání a issues na GitHubu mi přijde, že v Node.js ekosystému úplně chybí ambice takové funkce používat a požadovat. Většina pisatelů Mocha testů nejspíš ani neví, že tyto věci mohou existovat. Výsledkem je, že

- tyhle věci nenapíšou a nepošlou jako Pull Request nebo z toho neudělají balíček na npm,
- ve větších test suites jejich testy živelně přerostou do 1000řádkových souborů plných boilerplate kódu, které se nedají ani číst, ani spouštět.

Kdyby někde zahlédli že existuje něco jako parametrizace nebo správa fixtures,
třeba by je to trklo a zkusili by to použít, psát ty testy čistěji. Ale tím, že
to po ruce nemají, tak buď testy copy-pastují, nebo si pomůžou přes `forEach`
a všude naplácejí nějaké funkce na sdílení assertů. Nevím, který z těch dvou
přístupů je horší. První je čitelný, ale špatně spravovatelný, druhý je nečitelný,
byť alespoň iluzorně o něco lépe spravovatelný.

## npm zachraňuje situaci - nebo taky ne

Člověk, který už nějakou chvíli s Node.js pracuje, by si řekl, že tohle všechno jde nejspíš doplnit přes balíčky na npm. Jak jsem už naznačil, kvůli chybějící poptávce to není úplně růžové. Když už balíčky vůbec existují, [mají do deseti commitů a posledním z nich proběhl před dvěma roky](https://github.com/jpstevens/mocha-shared). Autoři už nejspíš dávno píšou
v [Elmu](http://elm-lang.org/), takže nové verze neřeší... Navíc se zdá, že balíčky pro Mochu v zásadě řeší spíš její nemoci a nedostatky. Nepřidávají vychytávky, které by vylepšovaly _developer experience_.

V době psaní článku je [mocha-clean](https://github.com/rstacruz/mocha-clean) nejvíce ohvězdičkovaný doplněk pro Mochu na GitHubu. Tedy z těch, které opravdu něco přidávají - přeskočil jsem integrace typu Mocha + React, Mocha + Mongo, Mocha + prohlížeč, apod. Opravuje _stacktraces_.

Co jiného bych si představoval? Tak třeba [pytest-testmon](https://github.com/tarpas/pytest-testmon/) je doplněk, který využívá code coverage k tomu, aby určil, jaké testy má spustit znova a jaké může nechat ležet ladem. Tzn. něco, co extrémně zvyšuje produktivitu. Žádné manuální `.only` nebo otrocké grepování.

A co se týče ovládání spouštění testů nebo formátu výstupu, i kdybych nakonec na npm našel něco, co mi vysněné přepínače doplní, nebude to jedna standardní implementace, standardní konvence, kterou by znal i nově příchozí kolega.

## Trendy

Článek jsem napsal jako vyústění dlouhodobé frustrace z toho, že se v JavaScriptu
musí na poli testování nejen vynalézat znova kolo, ale že ho ani nikdo nevynalézá.
Ani módní výstřelky typu [AVA](https://github.com/avajs/ava) proti [špagetám](https://en.wikipedia.org/wiki/Spaghetti_code) nebrojí. Už podle
`README` nevidím, že by se řešilo cokoliv z mnou nastíněných problémů. AVA vypadá jako
Mocha s jinou syntaxí, ještě méně features (tzn. bude vyžadovat nový ekosystém
`ava-*` balíčků na npm) a jednou jedinou _killer feature_, což jsou asynchronní testy
(Promises, async/await). To samozřejmě pytest nemá...

[Oh await!](https://pypi.python.org/pypi/pytest-asyncio)

No dobře, nebudu tak zlý. AVA vede k izolaci testů a extrémně zrychluje dobu běhu test suite. Uznávám,
vypadá to hodně dobře. Není tam jinak ale nic, co reálně ovlivňuje jednoduchost psaní složitějších testů. Autoři sice spálili hromadu času na tom, aby to jelo se všema Babelama a Reactama
a TypeScriptem, ale to nejsou věci, které mi ušetří čas při psaní testů, to
jsou šaškárny JavaScript ekosystému, za které nemůžu, a jako prostého uživatele mě moc nezajímají.

## TL;DR

Abych to shrnul, na testování v JavaScriptu mě štvou dvě věci:

- Asserty jako jsou v pytestu (nebo deklarativnost pomocí dekorátorů,
ale ty možná JavaScript už má nebo mít bude) nikdo neudělá kvůli omezením jazyka.
- Jestli je AVA následovníkem Mochy, tak JavaScriptové frameworky nesměřují
k jednoduššímu a pohodlnějšímu psaní testů, ale k jejich rychlejšímu spouštění díky paralelizaci (palec nahoru) a
_frikulínství as a feature_ (palec dolů). Nikde na obzoru nevidím ani tak základní
věc, jako je _namakanější spouštěč testů_, což bylo něco, čím Python žil před lety
a dnes je to komodita. To, čím Python žije dnes - jak psát strukturovanější,
spravovatelnější a čitelnější kód testů, vypadá ve srovnání s JavaScriptem jako velmi vzdálené
_first world problems_. Jsem smutný, že to v JavaScriptu nikomu nechybí, ale chápu, že je to asi jako
propagovat třídění odpadu v Súdánu.

**Reklama:** Většinu vědomostí o testování v Pythonu jsem načerpal na [Pyvech](http://pyvo.cz/), srazech Python programátorů, a to především na nedávném [pražském](http://pyvo.cz/praha), které bylo přímo na téma testování. Pokud chcete být tak chytří jako já, choďte na Pyvo.

_Tento článek jsem napsal z čiré frustrace, původně jen jako [cár Markdownu, úplně mimo blog](https://gist.github.com/honzajavorek/fc3279273dbffa7416ce384fa614cd1f).
Sem byl přepsán v lednu 2017 a posléze přeložen do angličtiny jako [Testing in JavaScript
and Python]({filename}2017-01-18_testing-in-javascript-and-in-python.md)._
