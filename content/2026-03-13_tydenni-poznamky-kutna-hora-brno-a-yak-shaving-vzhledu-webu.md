Title: Týdenní poznámky: Kutná hora, Brno, a ‚yak shaving‘ vzhledu webu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 12 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/374
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/116222705941898467

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2026-02-27_tydenni-poznamky-vymysleni-noveho-kurzu-scrapovani-tentokrat-s-ai.md) už utekl nějaký ten týden (27. 2. až 13. 3.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Během posledních dvou týdnů se nám povedly dva výlety. Ten první víkend jsme byli jeden den v Kutné Hoře, kde jsme koukli na svatou bramboru a herničku v jezuitské koleji. Další den jsem vytáhl dceru na kolo a projeli jsme se centrem Prahy kolem Vltavy. Byl to trochu rodinný _healing_ po náročných týdnech předtím.

Ten další víkend jsme jeli do Brna a okolí, za kamarády, rodinou, a zubařkou. Vrátili jsme se až ve středu. Zatímco týden byl stresující, výlet za fajn lidmi byl pohlazením a taky nám zafungoval jako potřebné nadechnutí.

![brambora]({static}/images/img-0969.jpg)

## Velký ‚yak shaving‘ na webu

Úkol zněl jasně: Přidat pod stránky příručky upoutávku na klub. Ideálně nějakou, která i přímo prezentuje nějakou informaci o tom, jak moc se na dané téma v klubu diskutuje.

Jenže hned jak jsem se do toho pustil, zjistil jsem, že to má hromadu prerekvizit. Že by bylo vhodné nejdřív vyčistit spoustu věcí, které souvisí s patičkou webu, odebrat nehezkou „pagination“, atd.

No a protože jsem zjistil, že stačí napsat, co chci aby se stalo, a Copilot to prostě udělá, nedokázal jsem se vůbec zastavit a vlezl jsem do úplně každé králičí nory, kterou mi můj web přichystal.

- Z patičky webu jsem odebral „Témata, která řešíme v klubu“. Byl to pohrobek něčeho, co jsem z velké části už přesunul do [katalogu kurzů](https://junior.guru/courses/) a co nemělo ani žádnou SEO hodnotu. Zrušil jsem to a přesměroval. Díky tomu jsem mohl vyčistit i jednu z posledních částí _legacy_ kódu z nejstarších dob.
- Z patičky webu jsem odebral SEO farmu se spoustou odkazů. Po konzultaci s AI jsem naznal, že to stejně nemá dnes už na SEO zas takový vliv, a že to tam akorát překáží.
- Udělal jsem pro příručku novou navigaci. Levý modrý panel jsem očísloval a udělal tam mnoho drobných vylepšení. Na mobilu se panel složí pod obsah a funguje trochu jinak. Spolu s tím jsem trochu vylepšil i horní navigaci webu.
- Odebíral jsem „pagination“ z různých stránek a přidával „breadcrumbs“. Do budoucna chci spodek stránek navigačně pojmout spíš formou nějakých „Kam dál?“ nabídek, než že by si lidi procházeli web nějak strukturovaně. A pokud chtějí, budou tam ty „breadcrumbs“.
- Vylepšil jsem design [výpisu epizod podcastů](https://junior.guru/podcast/) a všech podstránek pro jednotlivé epizody. U podstránek jsem přidal sekci „Máš otázky? Chceš probrat podobná témata?“ s upoutávkou na klub.
- Vylepšil jsem design [výpisu příběhů juniorů](https://junior.guru/stories/) a všech podstránek pro jednotlivé epizody. U podstránek jsem taky přidal, resp. předělal a sjednotil sekci „Máš otázky?“ s upoutávkou.
- Pak jsem se neubránil a začal na stejný půdorys předělávat i [výpis klubových akcí](https://junior.guru/events/) a všechny podstránky. Přišlo mi, že podstránky jsou nepřehledné, takže jsem je komplet předělal a nezbyl tam kámen na kameni. Celá stránka je mnohem jednodušší a snad přehlednější. Taky jsem odebral IRL akce z kódu. Přidával jsem to vloni kvůli EuroPythonu a zpětně jsem to vyhodnotil jako blbý nápad, míchat to s online akcema v klubu, ale doteď to zůstávalo v kódu. U odkazů na různé profily speakerů jsem přidal podporu pro rozeznávání odkazů na Bluesky, zobrazí se ikonka s motýlkem.
- Odebral jsem tunu starého kódu, který kdysi řešil výpis různých věcí, než se z toho pak stal newsletter.
- Nejrůznější seznamy odkazů na celém webu se nyní zobrazují se screenshoty v plných barvách (dříve se to obarvilo jen po najetí myši) a i další komponenty doznaly drobných designových úprav.
- Vylepšil jsem mírně design [stránek pro jednotlivé inzeráty](https://junior.guru/jobs/d66feb3de0c8367cc6ca82f3d7448eff19524e25edfd5c3a0b238cc2/), pokud jsou přímo na junior.guru. Aktuálně je taková jen jedna, takže jsem do toho ale neinvestoval zas nějak moc energie.
- Přidal jsem upoutávky na klub pod každou stránku příručky. Dřív jsem se o to snažil ručně, ale zamotal jsem se v CSS a nebyl schopen snadno docílit toho, aby to zapadlo do designu příručky. Teď jsem měl základ za 10 minut hotový.
- Opravil jsem a rozšířil žlutý pruh v patičce, dodal _label_ k formuláři na newsletter pro lepší přístupnost, apod.
- Na [klubové stránce](https://junior.guru/club/) je výpis názvů deníčků. Některé byly příliš dlouhé, tak jsem je nechal automaticky zkracovat.

Zjistil jsem, že Copilot s nejnovějším Codex modelem mi umožňuje na junior.guru webu bez velkého uvažování změnit prakticky cokoliv během pár minut, v ucházející nebo úplně ok kvalitě. Což je super!

Rozhodně to strhává bariéru něco jít a změnit. Dřív bych si skoro na každou odrážku v seznamu výše musel vyhradit aspoň týden času.

Akorát že jsem pak jel jak na matech, tahal jsem pořád za páčku a koukal, co vyleze. Udělal jsem asi 50 různých věcí, každá s (nejspíš?) mizivým dopadem na úspěch projektu 😆

Tak hlavně, že jsme o tom měli teď přednášku v klubu, že vygenerovat tisíc řádků kódu je k ničemu, když je to tisíckrát nesmysl. Ale třeba to jenom zveličuju a budou to užitečné věci…

Ten původní úkol úplně hotový nemám, ale vyčistil jsem hromadu kódu, vylepšil design, přidal upoutávky na klub do mnoha míst na webu, kde doteď nebyly, zpřehlednil mnohé stránky.

Vlastně bych řekl, že i když jsem měl čas za poslední 2 týdny programovat jen asi 3 dny, vypadá teď web podstatně jinak než předtím a udělalo se neskutečné množství práce.

Ručně jsem napsal jen velmi malé množství kódu, v podstatě jsem do toho zasahoval pouze pokud by ruční změna byla rychlejší, než napsat jednu větu do políčka AI agenta. Ale mohl jsem to takhle dělat jen díky tomu, že už umím programovat 🤷‍♂️

## Senior Guru

Nadšení z AI agentů mnoho lidí nesdílí a naopak přemýšlí, co se životem, když už programování přestává být o psaní kódu.

A neuplyne týden, aby mi někdo neřekl, že bych měl dělat spíš „senior guru“ na outplacement vyhořelých ajťáků. Už mi to nezávisle na sobě řeklo tak 20 lidí. A trvá to už roky, není to vyloženě novinka dnešní AI doby.

Ale stále jsem ještě tenhle „vtip“ realizovat nezačal. Možná proto, že nevím co s tím, a že mi „rekvalifikuj se na truhláře“ (kamarád Tomáš z Python komunity) nebo „rozjeďte se ženou automatizovanou květinovou farmu“ (ex-kolega František) nepřijdou jako instantní rady.

Ale byla by to asi bonitnější cílovka! 😀 A teď mi kamarádka konečně vnukla, jak to celé propojit. Je to vlastně _uroboros_. Čím více seniorům pomůžu z oboru ven, tím víc juniorů bude v oboru potřeba 🙃

![rollsafe meme]({static}/images/f8508b387b5b0857.png)

## Feedback na kandidáty

Sbíral jsem feedback na [kandidáty](https://junior.guru/candidates/):

> Posílám update od HR ohledně Junior Guru, vypadá to dost nadějně. Kvalita kandidátů: Profily jsou fajn strukturované, mají tam i odkazy na GitHub a projekty, takže se v tom dá rychle zorientovat. Responsivita: Funguje to skvěle – reagovali 4 lidi z 5. E-maily vs. LinkedIn: Ukázalo se, že psát přímo na mail je jistota (3 ze 3 odpověděli). Na LinkedInu je to slabší, jeden člověk se tam vůbec neozval. Bylo by super, kdyby ten mail měli v profilu fakt všichni.

Nebo:

> Ahojky!!! Zrovna jsem vcera ukazoval nekomu tvoji stranku:)! Myslim na to budeme ted otvirat i intern pozice next week!:)

Nebo:

> Ten předvýběr mega šetří čas - zpracovat 10 lidí vs 100 jako recruiter je super dobrý. A ano, řekla bych, že jsou asi všeobecné vlastnosti, které firmy hledají jaké - jak moc je pokročilý, jak moc se vzdělává, jaký má přístup k práci, jak komunikuje, zda mu sedne menší nebo větší firma atd. Není to pak logicky per firma fit, ale obecný popis kandidáta, kde firma už umí říct, zda to bude nebude fit. Tyhle věci se těžko vyčtou jen ze CV, to je vaše velká přidaná hodnota.

Nebo:

> Já ted nemám juniorní pozice vůbec. A měl bys ihned zahrnout AI do všeho. Když se tam koukám, první, co mě trkne do oka je, že tam není AI vidět na prvním místě. Ted je velká poptávka po AI native SW Eng nebo ještě lepší někdo, kdo vyvíjel AI agenty. Rozděl to na AI Prompting, Vibe coding a Agentic coding.

## Další

-   Odebral jsem z kódu odkazy a loga Týdne pro Digitální Česko, protože to současná vláda zařízla a doména začala vracet chybu.
-   Byl jsem v koupelnovém studiu a obecně jsme řešili hromadu věcí kolem bytu. Včera jsem měl snad osm půlhodinových telefonátů s různými odborníky nebo sousedy. Dnes už jen jeden. Telefonáty jsou stále nepříjemnější. Epizodu „statik“ máme snad už za sebou, epizoda „bourání“ je v plném proudu, epizoda „radiátory” bude ještě taky zajímavá.
-   Seznam Podcasty přecházely z jednotlivých smluv na ToS, tak jsem jim k tomu poslal nějaký dokument co chtěli. Nic neodepsali. Nevim, dál.
-   Do klubu se přidal [Vojta Červený](https://www.linkedin.com/in/vojtech-cerveny/) a ukázal nám svůj projekt CzechiBank, na kterém si mohou junioři vyzkoušet testování a jiné věci. Je to super! Taky jsme měli velké diskuze o AI apod.
-   Odepsal mi jeden poskytovatel kurzů, že nebude pokračovat ve sponzorství junior.guru. Další mi po tři čtvrtě roku zvažování odepsal, že s tím teď nezačne. Oslovil jsem jednoho z dalších sponzorů, jestli by nechtěli o rok prodloužit, ale ani neodepsali. Už dříve skončilo také partnerství s jednou poskytovatelkou kurzů, která pro klub občas udělala i workshop nebo přednášku.
-   Odeslal jsem newsletter. Opět byl OK rovnou tak, jak byl vygenerovaný od AI, takže jsem nic neřešil kolem editoru newsletteru s podporou Buttondownu.
-   Někdo našel mou [fiobank knihovnu](https://github.com/honzajavorek/fiobank) a založil dvě issues, tak jsem to hned odbavil a poprosil o Pull Requesty. Všechno jsem mergnul a releasoval.
-   Zařizoval jsem soutěž o mDevCamp lístek, soutěž o Java knihu, slevu na kurz, slevu na Prague Crawl, promoval jsem Installfest… Napsal jsem [status na LI](https://www.linkedin.com/posts/honzajavorek_sleva-50-5000-k%C4%8D-20-a-30-to-se-activity-7437788232131534848-CtNZ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACB93ABHHj4UI2winetGMZHboHlZIZojJA) o tom, kolik máme teď v klubu různých sleviček a soutěží.
-   Volal jsem si s [Brandleads](https://brandleads.cz/). Oslovili mně, že by mi pomohli se sales a že mají systém, který funguje. Vyslechl jsem si je a doteď mi to trochu vrtá hlavou. Mám trochu odpor k různým prodejním technikám, ale na druhou stranu, bez prodejních technik asi nic neprodám. Ještě nad tím budu přemýšlet. Minimálně bych si možná někde vzal nějakou jednorázovou konzultaci, abych měl trochu kompas. Co se týče B2C, určitě by mi pomohl nějaký systém a lepší marketing. Co se týče B2B, tam bych asi potřeboval nějakého fundraisera, spíš než salesáka. Někoho, kdo umí uhánět firemní dárce, protože to, co firmám odjakživa poskytuju, je _de facto_ jenom CSR.
-   Přišly mi nové platební karty, tak jsem je zadal zase zpátky do všech služeb, kam bylo potřeba je zadat.
-   Sháněl jsem lidi na přednášky do klubu a na rozhovory. Sháněl jsem náhradu za Janu Z., která sehnala fulltime práci, ale kvůli tomu pak přestala mít čas organizovat měsíční projektové výzvy v klubu. Naverboval jsem a snad trochu zaučil [Veroniku Z.](https://www.linkedin.com/in/py-veronika-zpevakova/).
-   Napsal jsem [status na LI](https://www.linkedin.com/feed/update/urn:li:activity:7434961035238797312/?originTrackingId=D%2FA6ilGfORdTacdJjyZOKA%3D%3D) o komunitnosti naší komunity. Olajkovali ho Rychlíková i Zelenka! 😀
-   Chtěl jsem dát kamarádovi dárek v podobě předplatného na nějakou službu, díky které by měl po ruce zvuky nebo hudbu do videí. Ze všeho nejvíc se mi líbilo [Epidemic Sound](https://www.epidemicsound.com/) a hlavně jejich promakané AI funkce na hledání a editaci, ale bylo to příliš drahé, tak jsem nakonec vybral levnější, ale taky pěkné [Uppbeat](https://uppbeat.io/). Pak jsem ještě vibekódil webovku, kde byl v CSS animovaný dárek, na který když se kliklo, tak z něho vypadl „kupón“. Bylo zajímavé pouhými prompty tvořit něco, co bych jinak sám vytvořit vůbec nedokázal, a rozhodně ne za půl hodiny.
-   Objevil jsem díky kamarádovi [Slow Down Radio](https://www.slowdownradio.cz/) a docela jsem ho teď poslouchal.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. Byla toho hromada, hlavně v klubu.
-   Za 15 dní jsem naběhal 9 km, při procházkách nachodil 11 km. Celkem jsem se hýbal 5 h a zdolal při tom 20 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1. Budu promovat [přednášku se Štěpánem](https://junior.guru/events/60/), pořeším soutěž o mDevCamp a Java knihu. Pošlu daňové podklady daňaři.
2. Zkusím znova předělat způsob, jakým se přidávají lidi do zájmových skupinek, protože je tam chyba.
3. Budu pokračovat v předělávání patičky webu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [MALUS - Clean Room as a Service | Liberation from Open Source Attribution](https://malus.sh/)<br>„I used to feel guilty about not attributing open source maintainers. Then I remembered that guilt doesn't show up on quarterly reports.“
- [Weltzeitgeist (@wackJackle@norden.social)](https://norden.social/@wackJackle/116200267162290355)<br>Zajímavé zhodnocení aktuální informační revoluce. Je to jedna velká, nebo je jich několik? Jsme v době počítačové rychlejší s inovacemi, než v době knihtiskové?
- [A Day in the Life of an Ensh*ttificator - YouTube](https://www.youtube.com/watch?v=T4Upf_B9RLQ)<br>Make it shitty!
- [Motůrek (feat. P/ST) - YouTube](https://www.youtube.com/watch?v=AKvsJReSTuA)<br>Protestsongy se vždycky dělily na ty, které vznikly tak nějak před mým životem, a na ty, které vznikly za mého života. Ty první, takové ty Kubišové a ti Krylové, byly posvátné. Ty druhé mi vždycky přišly cringe a nikdy na mě nefungovaly, ať už to byl Klus, nebo Poláková s Kollerem. Teď konečně vzniklo něco, co mi je příjemný. Na nic si to nehraje, je to taková letící dlažební kostka, kondenzovaná frustrace, a zároveň to na mně nepůsobí trapně a lacině.
- [V Krenovce se rodil plán Karlína a tiskly jízdenky](https://www.praha3.cz/aktualne-z-trojky/zpravy/retrospektiva/v-krenovce-se-rodil-plan-karlina-a-tiskly-jizdenky-n1206630.htm)<br>„Přišli už ráno, byl zde např. plukovník Waidenthal z ředitelství fortifikačního a ženijního nebo justiciár Schütz za církevní vrchnost, která měla pod sebou pražské statky, poddané i majetky. Celá skupina pak vyšla na Špitálské pole, obešli ho po obvodu, vše zakreslili, dumali a počítali. Z následných jednání pak vznikl plán nové osady jménem Karlín.“
- [He set out to apply the principles of open-source software to hardware](https://mastodon.social/@impactology/116139011890932933)<br>Borec staví základní technologické kameny moderní civilizace jako open source, který lze snadno vyrobit z běžně dostupných dílů… Traktor, dům… „Jakubowski envisions a future in which the GVCS parallels the Linux infra, with custom tools built to optimize agriculture, construction, and material fabrication in localized contexts.“ „Any intelligent fool can make things bigger, more complex, and more violent. It takes a touch of genius—and a lot of courage—to move in the opposite direction.“ „A GVCS tractor costs $12,000 to build, commercial tractor averages ~$120,000 to buy. If you’ve got a wrench, you’ve got a tractor. More than 110 machines had been built by enthusiasts from around the world.“ „Seed Eco Homes are human-sized modular houses complete with a biodigester, a thermal battery, a geothermal cooling system, and solar electricity. Each house is energy independent and can be built in 5 days, at a cost of ~$40,000. Over 8 of these houses exist.“
- [We need to talk about naked mole rats - The Oatmeal](https://theoatmeal.com/comics/naked_mole_rats)<br>Pohlazení v těžkých časech komplikovaného světa.
