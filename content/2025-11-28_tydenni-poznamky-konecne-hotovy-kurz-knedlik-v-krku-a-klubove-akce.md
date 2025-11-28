Title: Týdenní poznámky: Konečně hotový kurz, knedlík v krku a klubové akce
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 13 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/367
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115628863998359012

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-11-14_tydenni-poznamky-prototyp-seznamu-kandidatu.md) už utekl nějaký ten týden (14. 11. až 28. 11.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Minulý týden jsem měl svůj listopadový týdenní _stint_ pro Apify, ale nedokončil jsem jej a přetahoval do tohoto týdne, tak jsem se ani neobtěžoval s týdenními poznámkami. Takže tyhle jsou po dvou týdnech.

## Týden pro Apify

Stručně v bodech:

- Aktualizoval jsem [obří PR s novým kurzem scrapování v JavaScriptu](https://github.com/apify/apify-docs/pull/1907), Michał dokončil obtížné _review_ a minulý pátek jsme to konečně hodili na produkci. Hurá!
- Všechny kurzy mají nové úvodní obrázky. Designérka [dodala světlá a tmavá SVG](https://github.com/apify/apify-docs/pull/2025), díky AI se mi [povedlo z nich udělat adaptivní SVG](https://mastodonczech.cz/@honzajavorek/115582554143678073), která mění barvu podle potřeby. Když se do SVGček vloží CSS s media query, umí zobrazit různé barvy pro tmavý a pro světlý mód. Pustil jsem na to AI agenta a sice jsem ho musel trochu došťouchat k výsledku, ale povedlo se.
- Pracoval jsem na _proof of concept_ testů pro cvičení, která jsou v jednotlivých lekcí obou kurzů scrapování. Pracují s reálnými weby, takže se mohou snadno rozbít. Týmu se moje řešení pomocí [Bats](https://bats-core.readthedocs.io/en/stable/) celkem pozdávalo, tak [jsem to dotáhl](https://github.com/apify/apify-docs/pull/2097). Testy [objevily spoustu nefunkčních cvičení](https://mastodonczech.cz/@honzajavorek/115609660491860645), takže mají smysl a [mám příště na čem pracovat…](https://github.com/apify/apify-docs/issues/2113)
- Kromě toho jsem měl meeting, kde jsem poznal nového _technical writera_ Marcela z Brna, snažil jsem se vyznat v nedávných změnách od jiných lidí, [zakládal jsem issue](https://github.com/apify/apify-docs/issues/2112), [znovuotvíral jsem dříve vyřešená issue](https://github.com/apify/crawlee-python/issues/526) na Crawlee, dělal jsem _reviews_ jiným lidem, prostě různé menší věci.

Protože toho mám teď nějak moc, rozhodl jsem se, že si dám v prosinci od Apify volno. Další týden mojí externí spolupráce bude tedy až v lednu.

![Nové obrázky kurzů]({static}/images/8632e39379056364.png){: .img-thumbnail }

## Klubové akce: Lucie Lénertová o učení a Jan Meissner o své neprogramátorské cestě do IT

Tak se nám to nějak sešlo, že byly dvě akce v klubu krátce za sebou. Akce jsem propagoval [na Mastodonu](https://mastodonczech.cz/@honzajavorek/115581545606445079) a [na LinkedInu](https://www.linkedin.com/feed/update/urn:li:activity:7397251305133744128/).

Lucie Lénertová měla v sobotu dopoledne [něco jako workshop](https://junior.guru/events/55/). O víkendech běžně nepracuju, ale připojil jsem se a uvedl jsem to. Při pauze jsem se však odpojil a šel se věnovat rodině. Vypadalo to, že Lucie vše stejně zvládá sama 💪 A vypadalo to zajímavě, tak třeba si to někdy dám ze záznamu.

Ve středu jsme měli [Jana Meissnera](https://junior.guru/events/56/) a bylo to fajn. Sice se mu nedařilo čtvrt hodiny připojit, ale nám se nedařilo čtvrt hodiny nastavit správné nahrávání záznamu, takže tak či tak bychom se zdrželi a nic hrozného se nestalo. Jan to měl bez slajdů a vlastně to tak bylo super, člověk se soustředil prostě na to, co vypráví, a bylo to takové pohodové. Bylo pak i celkem dost dotazů. Jeho povídání jsem si užil, a podle všeho si to užili i všichni zúčastnění 👏

V tu středu celý den hustě sněžilo a já musel na přednášku do kanclu a zpět, snažil jsem se ten večer nějak přežít s Coldrexem, tak jsem rád, že to stálo za to a bylo z toho takové fajn povídání.

Záznamy už jsou oba k dispozici a těšíme se na prosinec na Irenu Zatloukalovou. Sice to ještě není oznámené, ale už to intenzivně domlouváme!

V obou případech jsem zkusil přes [cluck](https://github.com/juniorguru/cluck) nahrát zálohu zvuku a sice nebyla potřeba, ale musím se na to ještě nějak podívat, protože se mi zdá, že jednu stopu nahrává cluck blbě a dává mi do ní totéž co do jiné, místo aby nahrál mikrofon z mých sluchátek. No a uvidíme co do budoucna, vypadá to, že [budu mít úplnou náhodou nějaký boskovický mikrofon](https://mastodonczech.cz/@honzajavorek/115621160114402894).

![Proběhlé akce]({static}/images/screenshot-2025-11-28-at-19-36-23-online-akce-pro-zacatecniky-v-programovani.png){: .img-thumbnail }

## Posílání junior.guru newsletterů na Mastodon

Po Apify se mi nechtělo už rozjíždět velké věci, a navíc jsem trochu bojoval s knedlíkem v krku a bolestí hlavy. Nepravidelně a s různou silou mě to omezovalo v průběhu celých těch dvou týdnů. Někdy jsem byl v pohodě, někdy vůbec, a nechce se to pustit. Žena to měla nedávno, stejný průběh 🤷‍♂️

Zkusil jsem se tedy podívat aspoň na nějaké drobnosti, třeba posílání nových junior.guru newsletterů na Mastodon. Chtěl jsem si napsat knihovnu, jen malý wrapper nad `mastodon-py`, který mi umožní posílat idempotentně na můj Mastodon odkazy – třeba na články na můj blog, nebo na newslettery junior.guru, ale hodilo by se to i na [@p3news](https://mastodonczech.cz/@p3news) a jinde. Zatím jsem to totiž všude implementoval trochu jinak, všelijak na koleně.

Už jsem měl vymyšlený název, založené repo, už jsem to programoval, a u toho programování jsem si všiml, že `mastodon.status_post()` má přímo parametr `idempotency_key`. Tak jsem se radoval, že to jde vyřešit na dva řádky a vše, co jsem předtím připravil, jsem smazal. Druhý den jsem ale zjistil, že Mastodon si ten klíč pamatuje jen hodinu, takže to takto použít nejde. Dnes jsem už jen opravil svůj skript a víc jsem se v tom nevrtal. Nové řešení se prostě podívá do historie, jestli už nějaký status daný odkaz obsahuje. Místo dvou řádků deset, žádná knihovna teď nebude.

![Mastodon]({static}/images/screenshot-2025-11-28-at-19-37-06-honza-javorek-kdo-jste-jeste-nevideli-prvni-mastodonczech.png)

## Oprava rozbitých odkazů a hřbitov poskytovatelů kurzů

Už delší dobu [zápasím s Lychee](https://github.com/lycheeverse/lychee/discussions/1909), protože mi odmítalo ignorovat některé adresáře. To se mi povedlo konečně vyřešit, měl jsem lokálně a na CI odlišné verze Lychee. Napsal jsem si pak skript, který mi pomůže do budocna držet verzi Lychee aktuální i na CI.

Taky jsem následně zjistil, které odkazy jsou doopravdy rozbité. Ty jsem opravil. Dva se ale týkaly i poskytovatelů kurzů, tak jsem šel pátrat, jestli už to fakt vzdali, nebo ne. Určité zvěsti byly už dřív.

Naznal jsem, že to fakt vzdali, a to už máme spolu s Greenfox Academy tři subjekty, které bych měl v katalogu pouze v rámci historického okénka, tak jsem už udělal v katalogu rovnou novou kategorii „hřbitov“ a zařadil je tam.

Taky jsem si pohrál se zobrazením těchto subjektů na podstránce, aby z toho bylo jasnější, že už je po nich, a zbytečně tam nebyly sekce, které se zaniklých subjektů netýkají. Tohle vyústilo i v to, že jsem spustil skript na aktualizaci screenshotů a ten zpravidla vyústí zase v to, že ladím seznam webových elementů s cookie lištami, které má screenshotovač ignorovat, takže zábava na celý den. Každopádně po dnešku mám tedy na junior.guru hřbitov. Velmi Žižkovské 😅

![Hřbitov]({static}/images/screenshot-2025-11-28-at-13-22-47.png){: .img-thumbnail }

Když už jsem měl na webu něco nového, hned jsem to spontánně napsal i [na Mastodon](https://mastodonczech.cz/@honzajavorek/115627330896836618) a [na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7400164253812330496/). Vzápětí jsem dostal zprávu, že straším a nepřispívám k tomu, že bude mít IT dobrý obraz navenek a kvůli mně do něj nebudou chtít jít lidi 😅 Tak jsem do toho LI statusu aspoň doplnil nějakou svou analýzu, proč si myslím, že tyhle subjekty skončily:

> Proč skončili? Myslím si, že tyhle subjekty měly positioning nebo produkt ve stavu, že je ochlazení náboru juniorů zasáhlo nejvíc, případně se trefilo do toho, že majitelé neměli vizi co dál a prostě složili karty.
>
> Třeba ENGETO je ze stejné snůšky (z hlediska období, kdy začínali) a věci jako AI, dotace, nebo ochlazení trhu dokázali brát jako něco, na co se lze adaptovat. Byli prostě v kondici, měli trochu jiný byznys model, měli nějakou vizi a zakladatele, kteří nebyli v burnoutu, apod. 🙂
>
> Obecně bych řekl, že „rychlocesta“ do IT se zavřela a každý, kdo na ni měl založený byznys, to už nedává. Taková ta cesta „baví mě to a budu se pomalu ale jistě učit po večerech a na přechod do IT počítám s 1-2 lety konzistentního, ale udržitelného úsilí“ je teď to, co pořád funguje.
>
> Ale ne každý se do toho chce takhle pustit, ne každý jde do IT proto, že ho to baví (ne protože jsou to rychlý prachy a teplo v kanclu/z domova), a pokud dělám kurzy, nedá se na tomhle způsobu rekvalifikace vydělat peníze tak jednoduše jako dřív.

## Článek na Deníku N

Na Deníku N vyšel článek [Hlad po ajťácích skončil. Rychlokurzy nestačí a začátečníky skoro nikdo nechce](https://denikn.cz/1895606/hlad-po-ajtacich-skoncil-rychlokurzy-nestaci-a-zacatecniky-skoro-nikdo-nechce/). Docela se mi líbil, takže jsem jej sdílel dál ([Mastodon](https://mastodonczech.cz/@honzajavorek/115615569453981166), [LinkedIn](https://www.linkedin.com/posts/honzajavorek_ps%C3%A1t-anal%C3%BDzu-na-t%C3%A9ma-jak-jsou-na-tom-te%C4%8F-activity-7399393373939351554-lG0D?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACB93ABHHj4UI2winetGMZHboHlZIZojJA)), s vlastním spontánním komentářem:

> Nejsem zvyklý, že média o juniorech referují poctivě, ne pouze povrchově. Většinou jen honí senzace. Ale tohle je fakt dobrý článek!
>
> Ano, takto to teď vypadá. Je to mnohem lepší a relevantnější text, než ten nedávný, přeložený o stavu trhu v USA od Respektu, který všichni všude sdíleli.
>
> Díky, Terezo Mynářová, muselo to dát hodně práce. Rád bych tu práci aspoň tímto sdílením ocenil. Ta práce, kterou jste do toho dala, se vyplatila, a výsledek se povedl 👍
>
> Kdyby šli do hloubky i vaši předchůdci, nemuselo být na trhu tolik nešťastných juniorů zblbnutých nekritickými hurá-do-IT články, nebo dnes na smrt vystrašených z příchodu AI.
>
> Dřív bylo časté PR pro konkrétní kurzy, nebo se prostě jen nadšeně tvrdilo, jak firmy berou úplně každého… A vycházelo to ještě i v době, kdy se situace na trhu už otáčela. Dnes se zase rádo straší, jak junioři nemají žádnou šanci, že možná celé IT zanikne, a že všechno bude dělat AI.
>
> Myslím, že tento text konečně jednou dokumentuje aktuální situaci nějak vyváženě.
>
> Pozorný čtenář si navíc možná všimne, že firmy spoléhají na seniory, ale juniory nabírat nechtějí. Na tom něco nehraje, že? Je to jako byste chtěli slepice a kohouty, ale ne kuřata. Nevím, jak dlouho to bude trvat, ale firmy tohle rozhodně doběhne.
>
> Kdo nespěchá a rekvalifikuje se po večerech, v udržitelném „pomalu ale jistě“ tempu, protože ho to baví a ne proto, že si vydělá statisíce, tak bude brzy ve správný čas na správném místě.

Tenhle status má na LI k dnešnímu dni 116 lajků, 11 komentářů, 3 reposty a k 10.000 zobrazení. Na to, že jsem tenhle status nijak neplánoval, tak to teda pěkně vylítlo! Tereze jsem pak ještě pod jejím statusem [dával tip na další téma](https://www.linkedin.com/feed/update/urn:li:activity:7399345398730997760?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7399345398730997760%2C7399401321151307776%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287399401321151307776%2Curn%3Ali%3Aactivity%3A7399345398730997760%29):

> Skvělý článek.
>
> Co se týče dalších témat, zajímal by mně efekt EU/MPSV dotací jsemvkurzu.cz na trh. Moje čtení situace je, že dotace nafoukly trh s kurzy přesně ve chvíli, kdy se začala poptávka po juniorech snižovat kvůli ekonomice a řekněme že i kvůli očekáváním od AI.
>
> Poctivé kurzy nemohly dotace ignorovat, bylo nutné je zařídit a poskytnout, jinak by neměli uchazeče. Některé kurzy nafoukly ceny, aby na dotacích vydělaly. Největší borci založili účelové firmy jen pro dotace. Roztočily se kolečka reklamy a Facebook a jiné sítě byly zaplaveny bannery ve stylu „Pojď do IT, vyděláš si 100.000 Kč měsíčně, kurz s dotací“, které nalákaly spoustu nic netušících lidí. Díky dřívější covidové vlně a hurá-do-IT článkům v médiích opravdu netušících, protože co by v jiném oboru vypadalo jako scam, v IT nevypadalo jako hloupost.
>
> To vygenerovalo hromady narychlo a různě pochybně kvalitně vyučených lidí, kteří ale na současném trhu teď marně a zoufale hledají uplatnění. Firmy vypíšou inzerát na testera a dostanou klidně stovky CVček. Z nich je přitom relevantních kandidátů vlastně jen pár. Mnohé firmy ani nejsou zařízené na to, aby dokázaly takovou nálož zprocesovat, a neví si s tím pak rady.
>
> Bylo by zajímavé to zmapovat novinářskou metodou.

To taky nasbíralo 30 lajků a přes 3.000 zobrazení, docela čumím. Ještě se chystám přečíst si [Personalisté ghostují i uchazeče, kteří splňují všechny požadavky, říká autor experimentu](https://denikn.cz/1903692/personaliste-ghostuji-i-uchazece-kteri-splnuji-vsechny-pozadavky-rika-autor-experimentu/), což je prý velmi výživné, ale zatím jsem se k tomu nedostal.

![Deník N]({static}/images/screenshot-2025-11-28-at-19-39-33-hlad-po-ajtacich-skoncil-rychlokurzy-nestaci-a-zacatecniky-skoro-nikdo-nechce-denik-n.png)

## Junioři si nacházejí práci

Za poslední týdny se nám v klubu spustila jakási vlna juniorů, kteří si nacházejí práci. Všichni po dlouhých rocích snažení. Že by nějaký obrat v trendech? Nebo jen náhoda? Nechám se překvapit!

Každopádně mě to velmi těší a tím spíš, že jedna juniorka si práci našla přímo díky klubu – člověk dal do klubu inzerát, že hledají, ozvala se, prošla pohovorem, vzali ji 💪 Kdo tohle čtete a máte přístup do klubu, tak si klikněte a oslavujte s námi: [Bershee](https://discord.com/channels/769966886598737931/1418585399638495272/1426231756574429225), [SMTK](https://discord.com/channels/769966886598737931/789107031939481641/1441203772532461648), [Barbora L.](https://discord.com/channels/769966886598737931/789107031939481641/1443892470650900491) 🎉

![Oslava]({static}/images/celebration-celebrate-4003549944.gif)

## Já před 20 lety

Před 20 lety jsem si poslal e-mail do budoucnosti přes nějakou časovou kapsuli Forbesu, a ten email mi fakt přišel. Je to zajímavé čtení, osobní, ale tohle můžu sdílet:

- Byl jsem před maturitou, chtěl jsem se dostat na VŠ (VUT v Brně). Povedlo se!
- Uspořádával jsem si život a učil se ho žít. Stále v procesu!
- Poslouchal jsem house a nosil křiklavé tkaničky. Teď poslouchám leccos, nosím oranžovou mikinu.
- Hrál jsem eldar.cz/zvav, teď hraju 0 A.D. a SuperTuxKart.
- Četl jsem weblogy.cz, používal Firefox. RSS čtu stále (nebo zase?), Firefox používám stále.
- Kupoval jsem doménu littlemaple.net, dnes mám honzajavorek.cz
- Na DELLu s Celeronem 750MHz a cca 200MB RAM jsem dělal ve Photoshopu weby. Dnes na Applu s M1 a cca 8 GB RAM si v DaVinci stříhám videa a pracuju na vlastním projektu, junior.guru

Mimochodem, tenhle blog jsem začal psát před 18 lety, v roce 2007. Bez tohoto je tu k dnešnímu dni 625 článků, z toho 23 anglicky. Hustý, co?

![já před 20 lety]({static}/images/050618-123601.jpg)
Já v roce 2005 jako časoměřič na cyklistickém závodě

## Další

-   V klubu se objevily nápady, které se točily kolem týmových projektů a povídání v hlasových kanálech, tak jsem si to poctivě pročetl a přidal k tomu svých pár myšlenek, případně něco málo i hned změnil.
-   Připravil jsem trochu půdu v klubu na nadcházející Advent of Code 2025.
-   Přešel jsem z Prettieru na Biome. Trvalo to 10 minut a dělá to totéž, akorát rychleji. Pěkné. Jediná zrada byla, že ve výchozím nastavení to dělá taby místo mezer, trochu se mi při tom zježily chlupy, ale stačí to přepnout.
-   Udělali jsme doma velké a významné kroky k tomu, abychom měli nové bydlení. Měli bychom asi slavit, ale převládající pocit je ten, že jsme se akorát opřeli o stůl občerstvovačky na pátém kilometru horského maratonu.
-   Byl jsem na Festivalu otrlého diváka a viděl [Bulvu](https://vimeo.com/1129356683).
-   Naučil jsem se v DaVinci Resolve udělat z videa němý černobílý film s vadami a klavírním doprovodem, je to sranda.
-   Předělal jsem skript na přípravu newsletteru, aby sumarizoval klub jen když se opravdu dělá newsletter, a ne každý den. Původně jsem myslel, že bych tu sumarizaci využil i jinde v klubu, ale zatím to tak není, tak ať mi nelítají peníze oknem.
-   Mrknul jsem na Pull Requesty na Pyvec repozitářích, hlavně [docs.pyvec.org](https://github.com/pyvec/docs.pyvec.org/).
-   Opravil jsem [f1news](https://github.com/honzajavorek/f1news/), nakonec jsem s tím nemusel přecházet na Apify a stačilo nastavit při načítání RSS feedu HTTP hlavičky, jako kdyby si jej stahoval browser. Což nedává žádný smysl a popírá smysl RSS, ale tohle je prostě internet v roce 2025, bohužel.
-   Opravil jsem [kino](https://github.com/honzajavorek/kino), protože ČSFD trochu změnilo design.
-   Opravil jsem tenhle blog, protože s upgradem Mastodonu začalo API Mastodonu vracet nějaké věci, se kterými můj kód nepočítal.
-   Odnesl jsem v pondělí potrhaný svetr místní švadleně a v pátek jsem si přinesl spravený.
-   Dva dny jsem se [snažil založit si účet v ČSOB](https://mastodonczech.cz/@honzajavorek/115621147801883320).
-   V klubu jsem na chvíli vypnul automatické přidávání nových členů do skupinek podle zájmů, protože to dělalo binec a neměl jsem aktuálně čas na tom vyšívat.
-   Milion e-mailů, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. Udělil jsem jedno stipendium.
-   Za 15 dní jsem naběhal 7 km. Celkem jsem se hýbal 1 h a zdolal při tom 7 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1. Udělám adventní kalendář pro dceru.
2. Budu pokračovat v práci na [junior.guru/candidates](https://junior.guru/candidates/), aby to už nebyl jen prototyp.
3. Pochlubím se na sociálních sítích, že to není všechno hřbitovní, že si tři „moji“ junioři teď našli práci 💪

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Hlad po ajťácích skončil. Rychlokurzy nestačí a začátečníky skoro nikdo nechce – Deník N](https://denikn.cz/1895606/hlad-po-ajtacich-skoncil-rychlokurzy-nestaci-a-zacatecniky-skoro-nikdo-nechce/)<br>Dobrý článek. Ano, takto to teď vypadá. Nejsem zvyklý, že média o této věci referují poctivě, ne jen povrchově a nehoní jen senzace. (Mnohem lepší a relevantnější, než ten nedávný přeložený článek o stavu trhu v USA od Respektu, který všichni všude sdíleli.)
