Title: Týdenní poznámky #56: Bootstrap a námluvy s firmami
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl další týden (21.6. — 25.6.) a tak [stejně jako minule]({filename}2021-06-18_tydenni-poznamky-55-python-a-setkavani.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

V pondělí bylo strašné vedro, takže jsem téměř nedokázal pracovat. Měli jsme už objednaný nějaký [lepší větrák](https://www.alza.cz/eldonex-arctic-ice-ochlazovac-vzduchu-bily-d5801648.htm) a [třívrstvé zatemňovací závěsy](https://www.orbytex.cz/zatemnujici-zavesy--black-out-metraz/), jenže to všechno dorazilo až v průběhu týdne.


## Bootstrap

Dál jsem pracoval na [nové stránce pro klub](https://junior.guru/club2/), kde ale nakonec dělám i nový design celého JG. Jak jsem psal minule, rozhodl jsem se využít Bootstrap, a to jak pro základ stylů a „atomy“, z nichž můžu složit vlastní komponenty pomocí `@extend` v SCSS, ale nakonec i pro jejich komponenty.


### Rozplétání CSS proměnných

Jedna z věcí, které jsem musel vyřešit jako první, byla sdílení [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties), které jsem v projektu vytvořil nedávno. Šlo o to, že jsem chtěl barvy a font uložit do CSS custom properties a ty pak využít jak v místě úplně mimo web (např. generátor plakátků k přednáškám nebo generátor `og:image` pro jednotlivé stránky), tak přímo na webu v CSS. Jenže teď jsem chtěl mít barvy zase v SCSS, abych je mohl nastavit do Bootstrapu. A taky jsem viděl, že je to čím dál větší nepořádek, že je to prostě moc zamotané do sebe. Ani to tady nejde pořádně popsat, abych vám to vysvětlil, to je vždycky dobrý ukazatel toho, jestli je něco zbytečně složité.

Takže jsem to všechno od sebe oddělil, vše je _decoupled_. Barvy jsou zvlášť v CSS pro generátor plakátků a náhledů, zvlášť ve starém SCSS pro web a zvlášť v novém SCSS pro web. Aby to drželo po hromadě, napsal jsem si [testy](https://github.com/honzajavorek/junior.guru/blob/master/tests/test_css_variables.py), které kontrolují, že je to vše konzistentní. Když už jsem byl u toho, doplnil jsem i testy, které kontrolují, že SVG obrázky mají správnou barvu. Ty dokonce odhalily několik SVG s černou místo s tmavě šedou barvou, tak jsem je opravil. Až zase přidám SVG pro nějakou svou malůvku a nechám ho černé, místo abych barvu přepsal na `#343434`, spadnou testy a upozorní mě.


### Past vedle pasti

Protože jsem se učil nové věci, šlo to ddoosstt [ppoommaalluu](https://cs.wikipedia.org/wiki/Ppoommaalluu) a nadával jsem u toho. Nefungovaly mi nějaké třídy, pořád jsem něco hledal, nevěděl jsem co si mám tvořit sám a co můžu najít už hotové v Bootstrapu. Dokonce jsem využil vlastní klub na to, abych si nechal poradit, když jsem se zasekl. Na tom je krásně vidět, že „juniorství“ a „začátečnictví” není lineární záležitost, ale i já můžu být začátečníkem, když se pouštím do něčeho nového a i člověk, který je papírově junior, ale bude se tomu věnovat o několik měsíců déle než já, mi může dobře poradit.

Nicméně výsledkem je, že místo tun vlastního CSS mám jen pár řádků nad rámec Bootstrapu a hotové je celé základní stylování textu a vrchní žlutý proužek, který je responzivní. Bál jsem se, že bez BEMu v tom bude chaos, ale jak vidím, ono nakonec možná nebudu toho vlastního CSS potřebovat dost na to, aby v tom nějaký chaos mohl vzniknout. Nechám se překvapit do budoucna, ale zatím to vypadá slibně!


### Patička

Dál jsem pracoval na rozmyšlení a otextování patičky webu. Bude tam hned několik sekcí. Očumoval jsem patičky jiných webů, třeba nového webu Czechitas, potom CzechCrunch, Engeta, DámeJídlo, Rohlíku… No, všude jsem se trochu inspiroval. Text bych měl, teď zbývá jej „oživit“ a nastylovat. Oživení znamená, že některé informace by se měly dynamicky vypisovat z reálných hodnot. V patičce webu by například mělo transparentně být číslo, kolik zrovna vydělávám měsíčně. Stejně se mě na to pořád někdo ptá :)

Nová patička mi pomůže zbavit se [stránky pro média](https://junior.guru/press/) a zruším časem i [stránku prosící o dobrovolné příspěvky](https://junior.guru/donate/).


## Firmy

Když jsem zrovna neměl hlavu zabořenou v CSS, komunikoval jsem s firmami. Nevím, čím to je, jestli se to sešlo náhodou, nebo zda oznámení [partnerství s Mews](https://twitter.com/honzajavorek/status/1407583463159574528) v některých lidech vyvolalo [FOMO](https://cs.wikipedia.org/wiki/FOMO)? Nebo je to tím, že mám teď [velmi úspěšný status na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:6810811424017842176/) (130+ reakcí v době psaní tohoto článku)?

<iframe width="640" height="360" src="//www.youtube.com/embed/GA8z7f7a2Pk" frameborder="0" allowfullscreen></iframe>

No, bylo by to krásné, ale podle mě je to teda spíš náhodou. Každopádně, domlouvám teď partnerství hned na několika frontách:

- S Mews, SDAcademy a Engetem jsem hledal možnosti spolupráce na onom projektu pomáhání různým znevýhodněným lidem do IT.
- Uzavřel jsem partnerství s [Pipetail](https://pipetail.io/), dnes jsem přidal jejich logo na web.
- Byl jsem na kafi s člověkem z JetBrains, kteří u mě inzerovali nabídky stáží a já je zkusil e-mailem oslovit, zda by nechtěli společně vymyslet i něco víc.
- Volal jsem si s [Šárkou](https://www.linkedin.com/in/sarkastrossova/) z WebExpa a domluvili jsme spolupráci s klubem. Tuto jsem uvedl v realitu dnes: Členové klubu mají 20 % slevu na vstupné a k tomu losování o 2 volňásky. Navíc chci na konferenci jít, nebo za sebe poslat záskok, aby tam nebyli junioři samotní a ztracení, ale měli někoho jako záchytnou osobu a především někoho, kdo jim pomůže dál networkovat. To mi přijde docela důležité.
- Přes švagrovou jsem řešil kontakt na jednu společnost, která nejspíš najímá juniory.
- Ozval se mi starý známý z [jakési ovocnářské společnosti](https://youtu.be/LZK5VRuUfEY?t=18), tak uvidíme, jestli spolu něco vymyslíme.
- Připomenul jsem se ve firmě, která ve skutečnosti zaštiťuje hodně jiných malinkých firem :)

Jedna vzdělávací agentura díky klubu našla lektorku na kurz testování a taky lektora-recruitera. Jsem vždycky strašně rád, když vidím, jak ta komunita takhle funguje a mají z klubu, někdy možná až nečekaný užitek jak individuální členové, tak spolupracující firmy.

Pokud to tady čtete, připomínám svou [aktuální nabídku pro firmy](https://docs.google.com/document/d/1keFyO5aavfaNfJkKlyYha4B-UbdnMja6AhprS_76E7c/edit#), která tedy zatím žije v Google dokumentu, ale očividně to stačí :)

![Já, již brzy]({static}/images/scrooge-mcduck.jpg)
Já, již brzy. Obrázek jsem ukradl [tady Fukovi](https://www.fffilm.name/p/ffffriends.html).

K dnešnímu dni mi od začátku roku JG vydělalo 19 509 Kč čistého měsíčně. Zaokrouhleno: 52 % je od firem za členství v klubu, 28 % je od lidí za členství v klubu, 19 % je z příspěvků přes GitHub Sponsors nebo Patreon, 2 % je z plateb za inzerci pracovních nabídek. Cílem je mít aspoň 35 000 Kč čistého měsíčně, nechat uvadat dobrovolné příspěvky a naopak zvýšit podíl peněz, které plynou z individuálního členství.


## Sourcing speakerů

Po krátké pauze jsem chtěl opět nastartovat večerní akce v klubu. Někteří lidé se mi sami přihlásili s přednáškou, ale chci to prokládat i lidmi, které si vyberu sám. Mám tak možnost oslovit někoho, koho by třeba ani nenapadlo, že má co říct, někoho méně ostříleného, někoho z méně obvyklého prostředí. Dříve jsem takto občas dělal dramaturgii přednášek na [brněnském Pyvu](https://pyvo.cz/brno-pyvo/) a celkem se mi to dařilo, potom jsem tentýž skill využil při shánění speakerů do CfP [PyCon CZ](https://cz.pycon.org/), takže teď to jen opráším a jedu.

Udělal jsem si pořádek v existujících tipech na přednášející a s některými si ujasnil, kdy by mohli přednášku připravit. Dalších asi 5 lidí jsem našel a oslovil nově. Možná bude AMA o frontendu, možná bude něco o GISu, o relačních databázích, o technical writing… Bude to ještě hodně dopisování, ale chtěl bych si trochu naplnit frontu na ty přednášky, ať to pak zase chvíli nemusím řešit.


## Další poznámky

- Naplánoval jsem statusy na sociální sítě na další týden. Když v [Bufferu](https://buffer.com/) chci označit nějakou stránku ve FB statusu, napovídá mi to stránky podle toho, co píšu, jenže vidím jen název a ID. A ony se ty stránky občas jmenují stejně. Už jednou se mi stalo, že jsem označil špatnou firmu a to je potom trochu _faux pas_. Takže jsem hledal něco, kde bych mohl bez práce vložit odkaz na FB stránku a vyhodilo mi to ID, abych ověřil, že označuji správnou stránku. Nástroj jsem našel a tady si jej poznačím: [Lookup-ID.com](https://lookup-id.com/)
- Opravil jsem jednu chybu ve skriptu pro přišpendlení příspěvků, pokud si hodně členů v klubu přeje příspěvek přišpendlit. Poprvé se stalo, že bylo už špendlíků dost a samozřejmě to spadlo, chyběl mi někde `await`.
- Všiml jsem si, že `Markup` se už nemá importovat z `jinja2`, ale z balíčku `markupsafe`. Tak jsem to upravil, abych neměl terminál plný _deprecation warnings_.
- Jedna moje podporovatelka byla na kurzu testování a propagovala tam z vlastní iniciativy JG. Jejími slovy: „Vtipné bylo, že lektor tě vůbec neznal, ale účastníci kurzu tě znali a věděli že na ně vyskakuješ všude a všichni při jakémkoliv dotazu odkazují na tebe“. Což je opravdu vtipné, protože nemám vůbec žádnou reklamu. Neplatím si nic ani na FB, ani na Googlu, nikde. Píšu statusy na sociální sítě a tvořím web, to je vše. Měl jsem pár „článků v novinách“, ale to bylo už před půl rokem, v té době ještě neexistoval ani klub.
- Po diskuzi v klubu jsem prozkoumal, jak to na LinkedIn přesně funguje a následně tam založil skupinu pro členy klubu. Členové klubu se do ní mohou dobrovolně přidat, pokud chtějí. Potom uvidí v _members_ další členy a mohou si je přidat a tím se na LinkedIn vzájemně propojit. Také se bude JG členům zobrazovat v _interests_ na profilu. Nevím, jestli JG na profilu přidá nějaký kredit u recruiterů, ale minimálně jako poznávací znamení mezi námi by to časem zafungovat mohlo - něco jako „jé, koukám že ty jsi taky chodil do skauta? chodíš ještě? jakou máš přezdívku?“ Členové mohou být jinak v klubu anonymně. Sice tlačím na to, aby měli obrázek (a šli díky tomu mezi sebou rozlišit) nebo se nějak představili, ale povinné to není a své občanské jméno tam nikde mít nemusí. Dobrovolné přidání se do LinkedIn skupiny je tedy způsob, jak umožnit _opt-in_ propojení těm, kteří si to přejí.
- Šli jsme do [Aera](https://www.kinoaero.cz/) na [Pich](https://www.csfd.cz/film/988751-smolny-pich-aneb-pitomy-porno/prehled/) a byla to bomba, strašně se mi to líbilo. Jsem rád, že jsem si před filmem nepustil [Filu](https://magazin.aktualne.cz/fila-smolny-pich-aneb-pitomy-porno/r~ced8b0fab4ba11eb99faac1f6b220ee8/), protože spojluje průběh filmu. Už dříve jsem viděl [Barbary](https://www.csfd.cz/film/627611-je-mi-jedno-ze-se-zapiseme-do-dejin-jako-barbari/prehled/) od stejného autora a byl jsem dvakrát v Rumunsku, což bylo rozhodně dobré pro kontext. Minimálně záběry z Bukurešti jsem si užil o dost víc, než kdybych tam nikdy nebyl. Režisérovi se povedlo perfektně kamerou a zvukem vystihnout pocity, jaké tam má člověk jako chodec. Každopádně pokud máte rádi artové filmy a zvlášť ty Rumunské, Pich si užijete. Další tipy na starší Rumunské filmy: [4 měsíce, 3 týdny a 2 dny](https://www.csfd.cz/film/231418-4-mesice-3-tydny-a-2-dny/prehled/), [Sieranevada](https://www.csfd.cz/film/434115-sieranevada/prehled/)
- Když už jsem u těch filmů, nedávno jsme šli do Aera na [Chlast](https://www.csfd.cz/film/734768-chlast/prehled/), taky hodně dobrý.
- A když už dávám takové tipy, objevil jsem nedávno díky [bráchovi](https://twitter.com/mjavorek/) super podcast, [Přepište dějiny](https://prepistedejiny.cz/). V jednotlivých dílech vždy vezmou nějakou, občas i velmi aktuální hlášku nebo přirovnání, kterým se zaštiťují politici, nebo kdy si prostě někdo „bere historii do huby“ a překrucuje ji pro své rétorické potřeby. Tématu se čtvrt hodinku věnují, komentují jak to bylo ve skutečnosti, smějí se nepovedeným paralelám. No a mají i díl o historii podle Daniela Landy, tož neberte to! Sjíždím to teď jako divý.
- Sestavil jsem komodu. Malý ruční AKU na vruty a šroubky se velmi zaradoval, protože od doby, co máme elektrický mlýnek na kávu, jen ležel v krabici. Teď se pěkně zapotil.
- Nosím ze sklepa a do sklepa po točitých schodech štafle, věšeli jsme 3m závěsy.
- Během 7 dní od 19.6. do 25.6. jsem naběhal 6 km. Celkem jsem se hýbal 1 hodinu a zdolal při tom 6 kilometrů. Ajaj!


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Pokračovat v budování nové stránky klubu.
2. Naplánovat po pauze nějaké další přednášky v klubu.
3. Komunikovat dál se všemi firmami.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Je hlas pro Šlachtu hlasem pro Babiše? Opaku nasvědčuje pramálo](http://go.sparkpostmail.com/f/a/veNgVG0s-nFt6rg5Lpbo-w~~/AAA-fAA~/RgRirupPP0TOaHR0cHM6Ly9kZW5pa3JlZmVyZW5kdW0uY3ovY2xhbmVrLzMyODE1LWplLWhsYXMtcHJvLXNsYWNodHUtaGxhc2VtLXByby1iYWJpc2Utb3Bha3UtbmFzdmVkY3VqZS1wcmFtYWxvP3V0bV9zb3VyY2U9ZWNvbWFpbCZ1dG1fY2FtcGFpZ249MjAyMV8wNl8xOF96cHJhdm9kYWpfMTg2MjAyMSZ1dG1fbWVkaXVtPWVtYWlsJnV0bV90ZXJtPTQzODg4JmVjbWlkPTQ2MTBXA3NwY0IKYMqKZcxgL7cCh1IUbWFpbEBob256YWphdm9yZWsuY3pYBAAAaVE~) VV, pak Babiš, ach jo.
- [uBlock Origin works best on Firefox](https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox)<br>O důvod víc, proč používat Firefox
- [„Skleněný strop jsem neviděla, dokud jsem do něj nenarazila“. O ženách v české politice](https://a2larm.cz/2021/06/skleneny-strop-jsem-nevidela-dokud-jsem-do-nej-nenarazila-o-zenach-v-ceske-politice/)<br>„Abych našla odpověď na otázku, proč je tak málo žen ve volených funkcích, oslovila jsem političky, aby mi popsaly, s čím se setkávají. Mluvila jsem a psala jsem si s více než čtyřiceti ženami ze sedmi politických stran.“
- [Jsou horší přemnožené nutrie, nebo exekutoři? (Všichni tady umřeme #13)](https://www.youtube.com/watch?v=-pK0aVDc-5o)<br>Čtrnáctiminutový průlet českou situací co se týče exekucí a srovnání s českou situací co se týče nutrií. Potkáte-li exekutory, nekrmte je!
- [Z horníka programátorem: Už jsem to vzdával, narážel jsem na nezájem, říká Hisem](https://video.aktualne.cz/dvtv/z-hornika-programatorem-uz-jsem-to-vzdaval-narazel-jsem-na-n/r~fbb04576cfa811ebbc3f0cc47ab5f122/)<br>Pěkný rozhovor v DVTV o pozadí vzniku filmu Nová šichta s režisérem a hlavním protagonistou.
- [Kill the 5-Day Workweek](https://www.theatlantic.com/family/archive/2021/06/four-day-workweek/619222/)<br>Jak je to s čtyřdenním pracovním týdnem? Má nějaké nevýhody? Jak to bylo historicky? Kdo si jej přeje a kdo ne? Co lidé ve volném čase dělají? Může čtyřdenní pracovní doba ohrozit někoho, kdo je na tom už dnes dost mizerně? Dlouhý, ale zajímavý článek, který prochází mnoho aspektů případného zkráceni pracovní doby v USA.
- [Věci z druhé ruky jsou trendy. V Česku vzniká projekt, který vám doma udělá pořádek a zároveň pomůže.](https://markething.cz/veci-z-druhe-ruky-jsou-trendy)<br>Second-handy se vrací na scénu a budou vytlačovat „rychlou módu“ šitou dětmi v Bangladéši.
- [Behind The Charge | Our Magical Journey from the Czech Republic to Slovakia](https://www.youtube.com/watch?v=ijVPkmEqmWc)<br>Možná jste viděli From Castle to Castle, reklamu na Česko a Slovensko od Red Bullu. Tady je video o tom, jak to točili.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
