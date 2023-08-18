Title: Týdenní poznámky: Sekce s novinkami a Jinja
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-08-12_tydenni-poznamky-hemzeni-neuronu-a-e-mailu.md) už utekl nějaký ten týden (12. 8. až 18. 8.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [teď plánuji]({filename}2023-08-07_letni-pit-stop.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/3/).
</div>

## Sekce s novinkami

Minule jsem vytvořil novou sekci na webu, do které jsem přesunul podcast a klubové akce.
Postupně ji osekávám do tvaru, jaký chci, stejně jako sochař osekává nějaký nevzhledný šutr.

-   Do novinek jsem přesunul příběhy juniorů.
    Jejich kompletní výpis je na úvodní stránce webu, ale tam jednou nebude.
    Další kompletní výpis byl úplně dole na [stránce o motivaci](https://junior.guru/handbook/motivation/).
    Odtamtud jsem příběhy přesunul.
-   Odladil jsem menu na mobilu, aby nepřesahovalo mimo viewport.
-   Vymyslel jsem CSS komponentu, kartu, která je schopna člověku odprezentovat obsah typu přednáška, epizoda podcastu, nebo odkaz na _success story_.
    Docela jsem si s tím hrál a její design ještě v průběhu týdne měnil.
    Tuto kartu jsem pak použil na výpis přednášek, podcastů, i příběhů.
-   Vytvářel jsem podstránky pro klubové akce a pro epizody podcastu.
    Abych to mohl udělat, musel jsem každé akci přiřadit nějaké ID.
    Přišlo mi to jako nejlepší řešení, protože vše ostatní se může měnit (název, datum a čas), nebo to není unikátní (např. přednášející).
    Dřív se používal čas konání, ale šlo jen o kotvu na jedné dlouhé stránce.
    Když se to změnilo, člověk se dostal na seznam přednášek, ne na 404ku.
    U podcastu byl zase jakýsi zmatek v tom, co je vlastně ID, co je číslo, a co je nějaké technické unikátní označení.
    Tento chaos jsem musel vyčistit.
-   Přidal jsem na podstránky _breadcrumbs_.
    Sjednotil jsem, jak vypadá navigace dole.
    Použil jsem to pak i v katalogu kurzů.
-   Příběhy přebrané z jiných webů jsem předělal tak, aby se otvíraly do nového okna a přidal jsem jim UTM parametry.

![Příběhy]({static}/images/screenshot-2023-08-18-at-19-06-51-inspirativni-pribehy.png){: .img-thumbnail }
Takhle nově vypadají odkazy na příběhy

![Klubové akce]({static}/images/screenshot-2023-08-18-at-19-06-59-online-akce-pro-zacatecniky-v-programovani.png){: .img-thumbnail }
Takhle nově vypadají odkazy na klubové akce

![Podcast]({static}/images/screenshot-2023-08-18-at-19-07-41-podcast-pro-juniory-v-it.png){: .img-thumbnail }
Takhle nově vypadají odkazy na epizody podcastu

![Podstránka klubových akcí]({static}/images/screenshot-2023-08-18-at-19-08-08-marta-kirchgessner-dev-fiction-juniori-a-realita-vyvojarskeho-tymu-online-akce.png){: .img-thumbnail }
Podstránka klubových akcí je zatím ošklivá, ale je tam…

![Podstránka podcastu]({static}/images/screenshot-2023-08-18-at-19-07-56-anastazie-sedlakova-dnanexus-nejen-o-materstvi-a-kariere-v-it-epizoda-podcastu.png){: .img-thumbnail }
Podstránka podcastových epizod je taky zatím ošklivá…

Teď bych chtěl udělat novinkám úvodní stránku, která bude takovou „palubní deskou“.
Nejnovější podcast, plánovaná přednáška, poslední přednáška…
No a tahle palubní deska by měla mít potenciál stát se jednou obsahem pravidelného newsletteru.
Až bude tahle úvodní stránka, odstraním nejspíš úplně ten modrý postranní navigační panel.
Nějak mi to na ty novinky nesedí.
Nechám lidi proklikat se jen z „palubní desky“ a rozšířím _breadcrumbs_ o jednu úroveň.

## Cache busting

Zjistil jsem, že když jsem začal používat [esbuild](https://esbuild.github.io/), vyhodil jsem tzv. [cache busting](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching#cache_busting).
To byl kousek kódu, který do HTML přidával za adresu k .css nebo .js souboru jeho verzi, aby prohlížeče načetly novou, pokud se soubor změnil.
Doteď jsem nic v tomto směru velmi neměnil, tak to nevadilo, ale teď jsem začal do CSS dost sahat, tak to zlobilo.

Šlo by to nějak řešit přímo v esbuildu, ale já mám z historických důvodů složitý stack (přecházím z Flasku na MkDocs a stále ještě mám něco ve Flasku a něco v MkDocs), tak jsem si to [musel udělat po svém](https://github.com/honzajavorek/junior.guru/blob/aab0ea34b9b9a0bde787a2c3745b48b6edf4121d/juniorguru/cli/web.py#L159).
Krátký skript, který pouštím těsně před deployem, a který projde vygenerované statické HTML a tohle do nich přidá.

Staromilsky chci mít HTML kód čitelný, neminifikovaný.
Když jsem byl puberťák, čtením HTML kódu cizích webů jsem se naučil většinu věcí.
Tohle bych chtěl umožnit i juniorům, kteří by se zajímali o to, jak junior.guru funguje.
Napadlo mě, že když už mám ten postprocess skript, mohl by nad tím HTML rovnou pustit [Prettier](https://prettier.io/), aby to bylo vyloženě krásné.
Ale na to teď nemám čas, tak třeba někdy, jednou 🙂

## Jinja

Při tvorbě nové sekce na webu jsem narazil na spoustu nepříjemností kolem toho, jak mám webovku udělanou.
Jednou z věcí je chaotičnost Jinja šablon a maker.

Další z věcí je pomalost generování MkDocs.
Ta je způsobena tím, že jsem do Markdownu narval ještě jednu Jinju.
Taky to vytváří ještě větší chaos v tom, co je vlastně Markdown, co je HTML, co je šablona.

Hodně jsem nad tím přemýšlel a díval jsem se, co všechno existuje.

-   Prošel jsem si celý [MkDocs katalog](https://github.com/mkdocs/catalog).
-   Objevil jsem [JinjaX](https://jinjax.scaletti.dev/), komponenty v Jinje. Wow!
-   Zamyslel jsem se nad tím, kolik stránek je Markdown a kolik je v podstatě čistá Jinja.
    Napadlo mě, že některé věci by šly řešit ne Jinjou, ale rozšířením přímo v Markdownu.
-   Objevil jsem [Customblocks](https://github.com/vokimon/markdown-customblocks).
-   Koukal jsem na expermentální [PyMdown blocks](https://facelessuser.github.io/pymdown-extensions/extensions/blocks/).
-   Objevil jsem formátovač Jinja šablon, [djLint](https://djlint.com/). Wow!

![JinjaX]({static}/images/screenshot-2023-08-18-at-19-06-26-jinjax-documentation.png)
_From chaos to clarity!_

Nějaké velké závěry z toho nemám.
JinjaX se mi líbí hodně, rád bych to použil, ale [nevím, jestli to za současného stavu vlastně jde](https://github.com/jpsca/jinjax/issues/17).

Syntaxe a zpracování Customblocks se mi líbí víc než PyMdown blocks.
Možná bych tím mohl vyřešit spoustu věcí, které teď do Markdownu plácám jako Jinja makra.

Napadlo mě, že jednu věc můžu udělat hned.
Rozdělit explicitně co je Markdown s Jinjou a co je čistá Jinja.
Půlka stránek na junior.guru je _content-heavy_, zatímco druhá půlka je zase _custom_ a plná HTML značek a Jinja maker.
U té druhé půlky by se dal Markdown úplně přeskočit.

Snažil jsem se najít, jak MkDocs rozšířit, abych mohl pro některé stránky Markdown vypnout, ale zrovna tohle bohužel nejde.
Když jsem se dověděl, že to nejde oficiálně, tak jsem si přečetl kód a udělal to neoficiálně.
Udělal jsem si [knihovničku mkdocs_jinja.py](https://github.com/honzajavorek/junior.guru/blob/aab0ea34b9b9a0bde787a2c3745b48b6edf4121d/juniorguru/lib/mkdocs_jinja.py), do které jsem jednak přesunul nějaké smetí, které už jsem měl různě jinde po souborech, jednak jsem si tam dal tzv. _monkey patching_, který říká MkDocs, že soubory s koncovkou .jinja jsou taky dokumenty, a že pro tyto soubory má úplně přeskočit generování HTML z Markdownu.
Překvapilo mě, jak to nebylo vůbec složité a skoro na první dobrou to zafungovalo!

Ne že bych do toho hned překlápěl všechny stránky, ale nějaké nové, např. podstránku podcastu, jsem udělal už jako .jinja.
Zatím nepozoruji nějaké výrazné zrychlení generování MkDocs, ale to jsem popravdě ani moc nečekal.

Super je, že jsem ještě našel [Better Jinja](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml) doplněk do VS Code, a ten mi teď krásně obarvuje .jinja soubory.
A obarvoval by i .md.jinja (jako mix Markdownu a Jinjy), kdybych je tak měl pojmenované.
Nechápu, proč jsem tento doplněk nenašel a nezačal používat už dřív!

Dalším krokem by mohlo být použití Customblocks aj. rozšíření Markdownu.
Tím by se možná docílilo toho, že bych ve spoustě dokumentech vůbec Jinju nepotřeboval.
Nedělal jsem nějakou velkou analýzu, ale je možné, že by pak všechny _content-heavy_ dokumenty mohly být čistý Markdown a vedle toho by byly vyladěné (djLint? JinjaX?) .jinja soubory na ty _custom_ stránky.
To už by pak nejspíš mohlo vést i ke zrychlení, protože pro jedny by se zcela přeskočilo generování Jinjou, a pro druhé by se zcela přeskočilo generování Markdownem.

Taky mě napadlo, že můj Jinja filtr `{{ 'balloon'|icon }}`, kterým generuju `<i class="bi bi-balloon"></i>`, aby se tam po načtení speciálního fontu zobrazila ikonka z [Bootstrap Icons](https://icons.getbootstrap.com/), by mohl stejně tak dobře generovat rovnou SVG těch ikon. Mohl bych pak úplně vyhodit ten font, který mi furt někde dělal starosti 😀 Tak to až se budu někdy nudit.

## Další

-   Hned v pondělí jsem své nové spolupracovnici připravil podklady pro rozhovory s juniory.
    Všechno okamžitě rozjela a začala kontaktovat lidi.
    Dva hned slíbili, že si na ni udělají čas.
    Nejdřív se nedostala na Discord, ale už tam je a může si k jednotlivým lidem dočíst kontext.
-   Měl jsem call s další vzdělávací agenturou, která zvažuje partnerství, aby šla víc vidět v [katalogu](https://junior.guru/courses/).
    Partnerství si nejspíš nezaplatí, ale mám zajímavé poznatky.
    Jednak se jim líbí co dělám a hodně mi fandí a posílají mi na web lidi.
    Jednak by chtěli mnohem víc nějakého filtrování v katalogu.
    Jednak obhájit zaplacení něčeho takového zahraničním šéfům je složité, takže kdybych jim k té obhajobě předpřipravil nějaká data, čísla a informace, tak by se jim to mnohem víc chtělo obhajovat.
    A rozhodně by neposílali studenty a absolventy do klubu, protože kariérové poradenství se snaží mít pod svými křídly.
-   Zapracoval jsem feedback od pokusných králíků.
    Anketa mezi juniory je snad připravená ke spuštění.
-   Několik hodin jsem byl na kafi s Lukášem z [Fakturoidu](https://www.fakturoid.cz/) a kecali jsme o podnikání a o životě.
-   Když už jsem se v MkDocs šťoural v generovaných stránkách, předělal jsem všechny permanentní redirecty tak, aby to nebyly soubory v repozitáři, ale aby se vygenerovaly.
    Je super, že teď můžu ve VS Code hledat v souborech `learn` a nenabídne se mi už `learn.md` (redirect), ale jen `handbook/learn.md`.
    Na redirecty je nějaké [rozšíření](https://github.com/mkdocs/mkdocs-redirects), ale já to udělal přes [generování](https://github.com/oprypin/mkdocs-gen-files), které už tam stejně mám.
    Nebylo to nic složitého a můžu to mít jak já chci (např. česky).
-   Dělal jsem [code review kamarádce](https://github.com/juniorguru/juniorguru-chick/pull/27).
    Bylo osvěžující zase s někým spolupracovat a dělat code review!
    Tatáž kamarádka, protože má zkušenosti z byznysu, mi ještě prošla grafy a sepsala mi, co si o nich myslí.
    Měla zajímavé nápady.
-   V týdenním souhrnu v klubu se objevilo vlákno, které bylo privátní.
    Opravil jsem souhrn, resp. stahovač obsahu klubu, aby taková vlákna přeskakoval.
-   Patička junior.guru by už chtěla trochu změnit, ale aspoň jsem v ní změnil tlačítko „Podpoř mě členstvím“ na „Grafy a čísla“.
    Tohle tlačítko je vedle informace, že vydělávám 65.853 Kč měsíčně, tak mi přišlo blbé žádat o nějakou podporu.
    Když jsem tam to tlačítko prvně dával, vydělával jsem tuším kolem 10.000 Kč 🙂
-   V jednu chvíli jsem se zasnil a přemýšlel jsem nad tím, jak bych programoval junior.guru, kdybych s ním začínal dnes.
    Rozhodně bych vzal SQLAlchemy místo Peewee.
    A rozhodně bych to celé udělal v asyncio, s tím, že do synchronního kódu bych [odskakoval](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor), kdyby bylo potřeba.
    Teď to mám naopak a je to _pain_.
-   Šel jsem dceři ukázat Vltavu a lodě.
-   Chodil jsem po doktorech.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Během 7 dní jsem ujel na kole 17 km. Celkem jsem se hýbal 8 h a zdolal při tom 17 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Rozjet „přáníčka“ od juniorů pro juniory, což musím stihnout do PyConu.
    Udělat jim vlastní sekci v novinkách.
2.  Mít úvodní stránku pro Novinky, která bude mít potenciál stát se pravidelným obsahem newsletteru.
3.  Naplánovat přednášky na podzim.

**Bonus:** Jet na [komunitní Python sprint](https://blog.python.cz/Letni-sprinty-Python-komunity-v-Msenem).

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [FullJourney - The EVERYTHING AI / Video, Images, Music, Text to Speech, Sound FX](https://www.youtube.com/watch?v=GQUl2ySyj9U)<br>Nestíháte sledovat novinky v AI? Tady je video o tom, jak si to můžete všechno rovnou vyzkoušet na jednom místě. Vygenerujte si bolywoodskou písničku, zvuk prdu, hlas, video…
- [Média se pseudokritičností obírají o vlastní vliv](https://www.mediar.cz/media-se-pseudokriticnosti-obiraji-o-vlastni-vliv/)<br>„Média svou pseudokritičností a přejímáním lobbistických příběhů připravila sebe samá o to nejcennější: schopnost nastavovat agendu. Spíš čím dál víc slouží jako jeden ze zdrojů contentu, který přináší jen o trochu jiný emoční vzruch než true crime podcast.“ Nebo: „Nejsou peníze, za které by se zaplatil dostatek kvalifikovaných lidí. Nešťastnou vyhladovělost státní aparát a média sdílí. Obě strany se drží ve vyčerpaném klinči, zatímco se stávají snadnou kořistí pro zájmové skupiny.“
