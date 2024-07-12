Title: Týdenní poznámky: EuroPython a překopávání sponzorů
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/323
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/112774927866396175

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-06-28_tydenni-poznamky-sponzori-a-scrapovani-uradu-prace.md) už utekl nějaký ten týden (28. 6. až 12. 7.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
</div>

Se státními svátky a probíhajícím EuroPythonem píšu poznámky zase po dvou týdnech, protože to byla taková zvláštní kombinace nejrůznějšího volna a pracovního nasazení.

## Sponzoři

Pokračoval jsem v čištění všeho kolem sponzorů, abych měl připravený nový ceník a vše potřebné na moment, kdy budou prodlužovat 2-3 firmy. Jelikož ten moment se blíží velmi rychle a chci si přes léto brát i nějaké volno, muselo kvůli tomu vše stranou a pracoval jsem prostě na tomhle.

- Přidal jsem na GitHub „sponzorovací“ tlačítka ke všem repozitářům, kde to dává nějaký smysl.
- Jasně jsem rozdělil sponzory a partnery. Sponzoři platí peníze. Partneři se mnou mají nějakou dohodu, jsou to většinou nějaké spřátelené komunity a projekty a buď neplatí nic, nebo málo. Všechny spřátelené projekty jsem zmigroval do partnerů. Toto mě zdrželo několik dní, protože jsem si do určité chvíle myslel, že by sponzoři a partneři mohli být jedna věc. Jenže při psaní už osmého „ifu“, který mezi nimi rozlišoval, jsem se rozhodl, že jsou to dvě různé věci a budou se v systému chovat úplně jinak. Takže jsem pak všechen kód, už skoro hotový, převrátil zase naruby.
- Na úvodní stránce junior.guru jsem přestal zobrazovat partnery.
- Výpisy sponzorů nyní rozlišují tarif velikostí zobrazeného loga a tarify jsou jasně vizuálně oddělené.
- Výpis v katalogu provozovatelů kurzů je nyní rozdělený na několik sekcí, kde nejdřív jsou sponzoři, pak partneři, pak ostatní. U každého je vysvětleno, co to znamená.
- Na podstránkách sponzorů a partnerů v katalogu poskytovatelů kurzů je vždy napsáno, co přesně s nimi mám.
- Předělal jsem, jak se propojují sponzoři, partneři a provozovatelé kurzů. Řešil jsem různé hraniční případy, např. že jeden sponzor může stát za více provozovateli kurzů apod.
- Navázal jsem tarify ještě víc na nastavení přímo v Memberful. Co má být v YAMLu, je v YAMLu. Co má být v Memberful, je teď v Memberful.
- Přesunul jsem všechny sponzory a partnery na [group plans](https://memberful.com/help/plans/create-a-group-plan/) a zrušil jsem některé kupóny. Moc se mi líbí, jak se s tím teď pracuje a jak to funguje. Je to o mnoho jednodušší, než způsob, jakým jsem dřív ohýbal kupóny. Vymyslel jsem, jak ohackovat group plans i pro partnery, kteří typicky nic neplatí (protože s touhle variantou Memberful nepočítá).
- Udělal jsem skript, který mi dá přes spadnutí v nočním CI běhu každé pondělí vědět, pokud během následujících dvou měsíců vyprší nějaký sponzor.
- V rámci všeho výše jsem přepsal nebo smazal hromadu kódu, předělal spoustu HTML šablon a opravil nebo přidal kopy testů.
- Změnil jsem přiřazování rolí v klubu, aby se nedělalo podle kupónu, ale podle group plans. Při tom se mi povedlo pokazit oprávnění některým členům v klubu a najednou viděli něco, co vidět neměli. Byl z toho telefonát v osm ráno, rychlá oprava a snad to nebude mít velké následky.

## Statistiky

Začal jsem pak předělávat, jak se vytvářejí produktové statistiky - kolik mám členů, kolik z toho na individuálním členství, kolik z toho na měsíčním, na ročním, atd. Nyní se vše složitě čte a analyzuje z API Memberful, ale to má velké limity a hlavně se nikde nepočítá s tím, že se změní historie. A ona se mění. Třeba když v administraci jdu a smažu _subscription_, tak prostě už nikde v datech není.

Takže všechny grafy mám už delší dobu zase blbě. Nově to budu dělat tak, že se prostě spustí skript, který přečte jen aktuální čísla a ta uloží jako snapshot. A ten snapshot mi už nikdy nikdo nevezme. Z takových historických snapshotů posléze vykreslím grafy.

Doteď jsem se tomuto přístupu bránil, protože přejít na něj znamená zahodit všechna dosavadní data a začít historii grafů nanovo. Ale došel jsem do bodu, kdy je mi to už jedno a chci to hlavně opravit. Klidně spláchnu vše, co tam doteď mám, a začnu sbírat novou historii, jen když ta čísla budou dávat nějaký smysl.

Samozřejmě když ve výpočtu udělám chybu, tak ji zpětně neopravím. Ale to se nedá nic dělat. Žádný dokonalý přístup neexistuje. Nebudu kvůli pár statistikám vytvářet nějaký _data warehouse_.

## EuroPython

Tento týden je v Praze [EuroPython](https://ep2024.europython.eu/), největší konference o Pythonu v Evropě.
Dostal jsem se tam jako kouč na pondělním Django Girls workshopu.
Účastnil jsem se v průběhu týdne jen tak polehoučku, dal jsem si jeden _social event_ a na konferenci jsem byl hlavně ve středu.

Django Girls byly OK, ale připomněly mi, proč jsme je v ČR přestali dělat a místo nich Petr Viktorin vymyslel [Hadí workshop](https://naucse.python.cz/2024/hradec-snake-jaro/).
To je ale téma na větší rozepsání, o tom jindy.
Během workshopu jsem nedokázal ukončit Vim a [napsal jsem o tom hluboký lidský příběh na LinkedIn](https://www.linkedin.com/posts/honzajavorek_europython-djangogirls-activity-7216179306069159938-mmE4).

Uvažoval jsem, zda a jak na EuroPythonu propagovat junior.guru, ale vlastně mi nepřišlo, že je to nějak důležité.
Konference je hlavně v angličtině, junior.guru je v češtině.
Budou tam hlavně profíci, junior.guru je pro začátečníky.
Nakonec jsem to nehrotil.
Po domluvě s organizátory jsem donesl svůj panel a zbytek samolepek a udělal jen [improvizovaný stánek](https://mastodonczech.cz/@honzajavorek/112761131183103036).
Myslím, že to bylo adekvátní situaci.

Jeden den jsem opět [vzal na konferenci i dceru](https://mastodonczech.cz/@honzajavorek/112762951623593925).
Moc se jí líbilo obcházet stánky a vybírat všude samolepky, ale v _childcare_ sama být opět nechtěla.

Na stánku Apify jsem si [pokecal se Sauravem](https://mastodonczech.cz/@honzajavorek/112768192042238022) o novém Crawlee, ale brněnského Vláďu Duška, se kterým si nejvíc píšeme a který mě do Apify dotáhl, jsem se opět těsně minul.

Z konference mám doteď velké FOMO, mám dojem že se tam toho dělo tolik a já využil tak 5 % potenciálu celé té věci, ale vzhledem k tomu, že jsem chtěl tento týden i pracovat, starat se o dceru, plánovat víkend, potřeboval jsem i nějaký _me time_ atd., tak to prostě jinak nešlo.

![EuroPython a samolepky]({static}/images/4ca6da9132db7170.jpeg)
Samolepky

![Apify stánek]({static}/images/img-0638.jpg)
Apify stánek

![Muheue]({static}/images/img-0682.jpg)
Muheue z PyCon Namibia

## Další

-   Martin Wenisch udělal [pracovní inzerát](https://mastodon.cesko.digital/@mwenisch/112738901030623489), kde je v požadavcích na kandidáta „aktivní členství v klubu junior.guru“. Wow!
-   Po [Danu Srbovi](https://www.linkedin.com/feed/update/urn:li:activity:7216736419749236738?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7216736419749236738%2C7217175310654459904%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7216736419749236738%2C7217186407155453956%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287217175310654459904%2Curn%3Ali%3Aactivity%3A7216736419749236738%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287217186407155453956%2Curn%3Ali%3Aactivity%3A7216736419749236738%29) má rakovinu další člověk, se kterým v klubu aktivně spolupracuji: [Lucie Lenértová](https://www.lucielenertova.cz/p/projekt-humr). Oběma držím palce. Oba se rozhodli svou situaci netajit a dokumentovat ji (viz odkazy), proto si dovoluji to tady dát.
-   Pro změnu jsem tmelil sprchový kout a řešili jsme, kudy jinudy to ještě teče. Následovala návštěva řemeslníka a výměna různých věcí, tak snad už to neteče.
-   Byl jsem na krásném výletu na kole přes Brdy až do Plzně.
    Byl jsem na Moravě, válel se na terase nebo u vody a běhal po polích.
-   Domluvili jsme [klubovou přednášku o Dockeru](https://junior.guru/events/43/).
-   Přidal jsem na své weby [tenhle tag](https://blog.joinmastodon.org/2024/07/highlighting-journalism-on-mastodon/).
-   Zpracovával jsem si materiály z kurzu masáží a digitalizoval jsem si poznámky.
-   Koupil jsem knihy do soutěže k [dotazníkům](https://forms.gle/TJbV5ANrUWZbE6L78), kde stále ještě sbírám odpovědi, ale ještě jsem si je nevyzvedl ze Zásilkovny. Vždycky mi hlava odešla někam na EuroPython a zapomněl jsem na to.
-   Přehodil jsem hodinu, kdy se spouští scrapery pracovních nabídek, na nějakou normální denní, místo noční. Zdá se mi, že to pomohlo a moje scrapování spíš splyne s běžným trafficem.
-   Všiml jsem si, že se rozbilo menu v příručce, opravil to až downgrade MkDocs. [Slíbil jsem jim](https://github.com/mkdocs/mkdocs/issues/3532#issuecomment-2200135348), že to založím jako issue, ale zatím jsem se k tomu nedostal.
-   Udělali jsme ještě s Nelou malé úpravy na [stránce o psychickém zdraví](https://junior.guru/handbook/mental-health/).
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Procházel jsem Trello a čistil a přesypával trochu úkoly, jen to mi určitě zabralo několik hodin.
-   Za 15 dní jsem naběhal 32 km, ujel na kole 73 km. Celkem jsem se hýbal 13 h a zdolal při tom 105 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Vyzvednout knihy ze Zásilkovny.
2.  Oslovit končící sponzory.
3.  **Pracovat pro Apify.**
4.  Projít průběžně klub a odpovědět, na co bych měl odpovědět.
5.  Sepsat si plán na Q3.
6.  Domluvit nahrávání přednášky o Dockeru.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Sam Altman Is Full Of Shit](https://www.wheresyoured.at/sam-altman-is-full-of-shit/)<br>Tenhle borec dobře nakládá. „…it's time to stop listening to anything that Sam Altman has to say. Sam Altman is full of shit, and his reign at OpenAI has been defined far more by its empty promises than any realized dreams… Sam Altman has repeatedly said things that, if any founder with less power, presence, access and funding had said, they'd be laughed at, ignored, and treated like fantasists.“
- [Marcus' Blog
](https://mbuffett.com/posts/programming-advice-younger-self/)<br>„There’s a spectrum of “trying to figure out everything for yourself” to “bugging your coworkers with every little question”, and I think most people starting their careers are too far on the former side.“
- [A Personal Site Versus Social Media - Jason Journals](https://jasonjournals.com/posts/a-personal-site-versus-social-media)<br>„The process itself of writing/thinking is desirable. The final product, a published blog post, is a goal, but so is the process of writing in the first place. Both the journey and the destination are valuable.“
- [On the origins of DS_store](https://www.arno.org/on-the-origins-of-ds-store)<br>Původ souboru .DS_store
- [Why Is Chile So Long?](https://unchartedterritories.tomaspueyo.com/p/why-is-chile-so-long)<br>Proč je Chile tak dlouhé? Zajímavá věta z komentářů: „The differences between Chilean Spanish and other Spanish accents are more significant than those between Czech and Slovak, which are generally considered two different languages.“
- [pacient.erecept.sukl.cz](https://pacient.erecept.sukl.cz/)<br>Z newsletteru Datažurnál od Samizdat: „Vypíchnout si zaslouží tip na eRecept PACIENT, webovou a mobilní aplikaci, která umí vyhledat léky z vašeho receptu ve skladových zásobách lékáren v okolí. Není to bez much (data nejsou úplně real-time a krabičky si taky mohl někdo zamluvit po telefonu), ale pořád mnohem lepší než obcházet apatyky naslepo.“
- [Voliči na periferiích opět selhali. Zapomněli volit strany, které jejich problémy ignorují](https://denikalarm.cz/2024/06/volici-na-periferiich-opet-selhali-zapomneli-volit-strany-ktere-jejich-problemy-ignoruji/)<br>„Že by se ty po dekády se zpřesňující analýzy o úpadku úrovně škol konečně vzaly vážně? Že lze možná ten záhadný úkaz, kdy „muži z periferií a se základní školou volí Filipa Turka“, vyřešit třeba tím, že bychom posunuli nejen tyto muže vzdělávací soustavou nahoru, aby si třeba nemysleli, že úspěch je haljující borec v drahém autě, který doporučuje pít savo a ve volném čase sbírá svastiky.“
- [I'm giving up — on open source - Blog](https://nutjs.dev)<br>„Publishing source code for the greater good is a noble cause, but to be honest, I think that over the years, using "open source" has become an excuse to avoid paying for software. And who's to blame if something goes wrong? The maintainers, of course.“
- [Open source is neither a community nor a democracy](https://world.hey.com/dhh/open-source-is-neither-a-community-nor-a-democracy-606abdab)<br>„There's an ever-latent instinct in a substantial subset of OSS users who will continuously rear itself to question why it's the people who do the most work or deliver the most value or start the most projects that get to have the largest say. And when people talk about OSS burnout, it's often related to this entitlement syndrome. Although it's frequently misdiagnosed as a problem of compensation. As if begging for a few $ would somehow make it bearable.“
- [Orientalism: Desert Level Music vs Actual Middle-Eastern Music](https://www.youtube.com/watch?v=LR511iAedYU)<br>Žádná hudba reprezentující Blízký východ, kterou jste kdy slyšeli, jej ve skutečnosti nijak nereprezentuje. Ať už jde o soundtracky ke hrám, k filmům, všechno je to jen povrchní orientalistická představa nás ze Západu, co se asi tak zhruba hraje tam někde mezi vším tím pískem a velbloudama. Jo, Zimmer taky! Je to dlouhé video, ale perfektně udělané, vše vysvětlené, místy i dost vtipné. Pusťte si aspoň prvních 10 min - to dáte, fakt!
- [Entering a New Phase of the Web, with Citation Needed’s Molly White](https://flipboard.video/w/ovAsDRovkgbihkZa3wMcUA)<br>Fajn rozhovor s Molly White o webu, internetu, Mastodonu, blogování, sociálních sítích, walled gardens, interoperabilitě a suverenitě, byznys modelech pro tvůrce, Wikipedii…
