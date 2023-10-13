Title: Týdenní poznámky: Dovolené, spousta drobností a build frontendu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/214

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-05-18_tydenni-poznamky-uklid.md) už utekl nějaký ten týden (18. 5. až 1. 6.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Glance Media](https://junior.guru/jobs/b5bb05d439c71b800ca520b63c5ae9ab261d10d19681ff2bc2acce0c/), [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

Po napsání předchozích poznámek jsem s kamarádem odjel na prodloužený víkend na cykloexpedici po Žatecku.
Bylo to fajn, ale spálil jsem se a měl jsem pak rýmu, možná i nějaký úžeh, takže s tím jsem se pak potýkal ten další týden.
Pořád však lepší než dva předchozí ročníky, kdy jsme vždy akorát zmokli a vloni dokonce chytili covid.

![Kolo]({static}/images/img-3327.jpg)

![Zichovec]({static}/images/img-3350.jpg)

V pátek jsem nějak neměl sílu napsat poznámky, takže je píšu až teď, zpětně za dva týdny.
Kdy napíšu další nevím, protože teď budu pro změnu odjíždět na rodinnou dovolenou.

Bude to od založení junior.guru v roce 2019 první dovolená dlouhá aspoň týden, během které nemám v plánu vůbec koukat na práci.
Udělat si takovou dovolenou bylo [jedním z mých cílů na letošní rok](https://github.com/orgs/juniorguru/projects/1/views/1?pane=issue&itemId=23841635).
A bude to taky první pořádná dovolená s dítětem.
Tak snad si to užijem a nebude to nějaké peklíčko!

## Vítání nových členů v klubu

Snažíme se v klubu nové členy vítat, a to jak automatizovaně, tak ručně.
V ideálním případě by automat poskytl praktické informace, které se stále opakují a jejich psaní stejně působí roboticky.
Lidé by pak poskytli ten vřelý, lidský element typu „jé, vítej, já jsem původně taky z Karviné“.

K tomu má zatím vítání ještě dost daleko, ale teď jsem se k ideálu dost přiblížil.
Trochu jsme probrali s moderátory, ale i s členy klubu, jak by to mohlo fungovat, a vypadlo z toho pár dobrých nápadů na vyzkoušení.

-   Změnil jsem, jak funguje role „Vítací typ“ pro lidi, kteří mají zájem nové lidi vítat.
    Diskutovali jsme, zda má tato role smysl a jaký, zda ji vlastně lidé využívají k tomu, k čemu byla zamýšlena, a proč v klubu vítají jen 2-3 lidi, z nichž někteří tu roli ani nemají.
-   Předělal jsem, jak bot přidává do uvítacích vláken lidi s nějakou rolí.
    Standardní přidávání uživatelů po jednom na Discordu vytvářelo spoustu rušivého „smetí“.
    Teď bot do vlákna přidá zprávu, kde je mention na tu roli.
    Tato zpráva je tzv. silent, aby přidala lidi, ale příliš nerušila.
    Okamžitě po odeslání se zpráva sama smaže (je zajímavé, že toto je přímo funkce API Discordu).
-   Zvýšil jsem logování v [realtime botovi](https://github.com/juniorguru/juniorguru-chick/issues), abych zjistil, proč některé věci nefungují.
-   Migroval jsem realtime bota na [Fly v2](https://community.fly.io/t/fly-migrate-to-v2-automatic-migration-to-apps-v2/11984).
    Nevím, co je Fly v2, ale přišlo mi mailem, že to mám udělat, tak jsem to udělal.
    Klikl jsem, vše jelo, takže dobrý.
    Akorát že vůbec.
    Při prvním pokusu o deploy se to celé rozsypalo a hodinu dvě jsem debugoval, co mám kde opravit a změnit.
    Zase se mi ani [nedařilo připojit na platformu](https://community.fly.io/t/eror-failed-to-start-remote-builder-heartbeat-failed-building-options-failed-probing-personal-context-deadline-exceeded/10708), což už jsem jednou řešil.
    Nakonec pomohlo nějaké náhodné přehození řádků v Dockerfile 🤷‍♂️
-   Realtime bot umí nyní zakládat uvítací vlákna, psát do nich zprávy, přidávat do nich lidi, reagovat na uvítání pomocí emoji.
    Přidal jsem i emoji reakce na základě jednoduché analýzy textu, takže když člověk zmíní Python, bot reaguje pomocí Python loga.
    O tom jsem zatím nikomu neříkal a byl jsem zvědavý, kdo si toho všimne první, ale nikdo se mě na to zatím nezeptal.
    Takže jsem právě prozradil tajemství, resp. překvapení 😀
-   Dali jsme do uvítání i malou hru, na které se může podílet kdokoliv.
    Mohlo by to debatu v uvítacích vláknech strhnout od kariérového poradenství víc k samotnému vítání a poznávání nových členů.
    Jsem zvědav, zda a jak to zafunguje.

## Opuštění python.cz

Opustil jsem roli maintainera [python.cz](https://python.cz/).
Je to součástí mé čistky osobních projektů, kterým se stejně nedokážu věnovat.
Na Pyvec Slack jsem k tomu napsal:

> Jak jsem avizoval po Novém roce, uvolňuji místo jako správce python.cz. Od ledna jsem tam nic neudělal a dnes jsem to napsal i do README a odhlásil se z notifikací. Kdo byste s tímto webem měli nějaké plány, ozvěte se tady ve vlákně nebo v #pyvec. Já s ním měl plánů milion, ale je na čase si přiznat, že nemám paralelní život, a nechci stát v cestě někomu, kdo by tomu webu mohl pravidelně dávat lásku, klidně s tím, že jej od základů předělá.
>
> Kdysi jsem python.cz vytvořil jako jednoduchou stránku, kde byl seznam pár hlavních informací o české Python komunitě. To mi přineslo spoustu nových kamarádů, příležitostí a slávy :) A taky věřím, že to pomohlo českou Python komunitu zcelit napříč městy. Bylo by fajn, kdyby tenhle rozcestník v nějaké, klidně minimalistické podobě zůstal, ale já už za kormidlem být nemůžu.

[Upravil jsem README](https://github.com/pyvec/python.cz/pull/555) a snažil jsem se odebrat z e-mailů, které chodí, když spadne GitHub Action.
Dostávám je rád, ale logicky pouze pro projekty, kterým se věnuji.
Proto nepřipadalo v úvahu vypnout si tyto e-maily plošně, což na mnoha místech radili.
V [dokumentaci](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/notifications-for-workflow-runs) jsem se nakonec dočetl, že notifikace dostává jen ten, kdo vytvořil daný build, nebo kdo jej nějak zapnul 🤯

> Notifications for scheduled workflows are sent to the user who initially created the workflow. If a different user updates the cron syntax in the workflow file, subsequent notifications will be sent to that user instead. If a scheduled workflow is disabled and then re-enabled, notifications will be sent to the user who re-enabled the workflow rather than the user who last modified the cron syntax.

Protože build na python.cz stejně už několik měsíců padá, já to úspěšně ignoruji a nikomu dalšímu to nevadí, řekl jsem si, že je tedy nejlepší cestou to vypnout. Kdo se tomu pak bude věnovat, tak to zapne a začne dostávat notifikace. Jenže jsem nebyl schopen najít ani tlačítko na vypnutí. Udělal jsem to zase až s pomocí [příslušné dokumentace](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow).

## Jak si vybrat kurz? Nová stránka v příručce

Měl jsem v plánu psát do příručky novou stránku o kurzech, abych podpořil vznik [katalogu](https://junior.guru/courses/), ale nakonec jsem v tomto směru mnoho neudělal.
Na psaní potřebuji klid a ten jsem vůbec neměl.
První týden jsem byl doma s rýmou a dítětem, které nemělo zrovna nejklidnější období.
Druhý týden už jsem měl kancelář, ale zase se moje myšlenky zabývaly spíš tím, abych stihl vše podstatné před odjezdem na dovolenou.
Povedlo se mi aspoň následující:

-   Publikoval jsem [připravovanou osnovu](https://junior.guru/handbook/course/) nové stránky a dal jsem ji už do menu.
-   Zběžná analýza klíčových slov, abych věděl, co lidi v souvislosti s kurzy hledají.
    Nejsem na to žádný expert, takže odborník by se mi asi vysmál, že to, co nazývám „analýzou klíčových slov“ je ve skutečnosti jen nějaké šimrání vyhledávačů.
-   Upravil jsem textace v katalogu, aby bylo pochopitelnější, že pokud je tam nějaký kurz, znamená to, že „existuje“, ne že jej junior.guru „doporučuje“.

![Nová stránka]({static}/images/screenshot-2023-06-01-at-14-42-10-jak-vybrat-kurz-programovani.png){: .img-thumbnail }

## Předělávání buildu frontendu

Když jsem viděl, jak se mi nedaří psát novou stránku do příručky, rozhodl jsem se před dovolenou zaměřit na něco jednoduššího, co nevyžaduje tolik soustředění.
Jal jsem se zrychlovat build frontendu.
Je to jedna z mých priorit na tento rok, protože build už dlouho nevyhovuje a s přibývajícími obrázky a stránkami se stává až neskutečně pomalým.

To jsem ale netušil, že začnu tahat za šňůrku a budu tahat a tahat a tahat…
Takže dodělané to nemám.

-   Přešel jsem z Rollupu na [esbuild](https://esbuild.github.io/).
    Pomohl mi článek [Some notes on using esbuild](https://jvns.ca/blog/2021/11/15/esbuild-vue/) od Julie Evans.
-   Díky tomu jsem mohl vymazat spoustu věcí a nakonec i celý původní build založený na Gulpu.
-   Některé věci jsem přesunul do Python skriptů, teď když už mám plnohodnotné CLI s [clickem](https://click.palletsprojects.com/).
-   Všude už používám `import` místo `require`.
-   Jedno největší zdržování způsobují og:image obrázky, které generuji _on demand_ během generování každé HTML stránky.
    Generování og:image zahrnuje spuštění prohlížeče a uložení screenshotu, takže je to fakt pomalé.
    Dalo mi to dost práce, ale nejspíš se mi povedlo celou tuhle věc přesunout do skriptu, který se dá pustit nezávisle na buildu stránek v rámci všeho ostatního, co mi stahuje data potřebná pro vygenerování webovky.
-   Druhé největší zdržování způsobují různé optimalizace obrázků, které se dějou pokaždé a opět _on demand_ při každém buildu.
-   Pokud jde o generované obrázky (např. ty og:image nebo plakáty k přednáškám a podcastu), chtěl bych optimalizace přesunout přímo do míst, kde se generují, aby výsledný obrázek byl už optimalizovaný i za cenu delšího generování, protože to bude stejně vždycky hrozně pomalé.
    Obrázky pak budu nejspíš commitovat do Gitu, aby se negenerovaly znova pokaždé, ale pouze při změnách.
-   Pokud jde o různé manuálně přidávané obrázky, ty už v Gitu jsou, takže stačí udělat něco, co by je jednou za čas optimalizovalo, ať na to nemusím myslet.
    Výsledek by se commitnul zpět do repozitáře.
    Takže ideální věc do CI, podobně jako tam už mám formátování kódu.

No jsem zvědavý, jestli se k tomu po dovolené vrátím a kdy to dodělám.
Každopádně mi to pak nejspíš zrychlí a zpříjemní úplně všechnu další práci kolem samotného webu.

## Ankety

Udělal jsem review nějakých věcí ohledně ankety pro juniory, kterou se snažíme rozjet spolu s ENGETO Academy.
Bohužel osoba, která nám na to měla hodit odborné oko, to má někde na konci priorit, takže náš postup stagnuje a obávám se, že do léta to spustit nestihneme.

Mezitím svou anketu dokončila [Nela Slezáková](https://www.nelaprovazi.cz/), se kterou děláme kapitolu v příručce s názvem [Psychika na cestě do IT](https://junior.guru/handbook/mental-health/).
Chtěla by ji teď doplnit a vylepšit, takže udělala dotazník, kde chce zjistit, s čím se junioři reálně potýkají.
Na dotazník jsem hodil oko a pak jsem s ním otapetoval internet, abychom měli respondenty.
Dal jsem ho i do modrého proužku na každou stránku na junior.guru.
Pokud jste junioři, [vyplňte nám to prosím](https://forms.gle/CvcrqJLwaU9bSLzf7)!

![Upoutávka]({static}/images/nelaform-001.png){: .img-thumbnail }
Tohle jsem maloval snad dvě hodiny.

## Festival o psaní

Nepovedlo se mi najít nikoho, kdo by chtěl lístek na [Festival o psaní](https://festivalopsani.cz/).
Tento týden jsem ho nabízel už i zadarmo, ale každý už má asi na víkend program.
Lístek tedy propadne.
Mrzí mě to, protože nebyl levný, ale termín dovolené prostě vyšel takhle a nedá se nic dělat.
Někdy člověk asi musí věci i odepsat a neřešit.

Škoda, že jsem udání lístku věnoval v posledních týdnech celkem dost energie, takže výsledná bilance jde ještě víc do záporu.
Dokonce už jsem měl kontakt i na jednu studentku, které bych to poskytnul jako stipendium (tzn. za 0 Kč, pro mě stále ztráta, ale aspoň bych měl dobrý pocit).
Ta si to však potom ještě rozmyslela.
Přitom to podle mě bude super akce, na kterou bych jinak moc rád šel.

## Podcast

Pavlína natočila podcast, ale přišlo jí, že se to vlastně moc po obsahové stránce nepovedlo.
Pustil jsem si to a souhlasil jsem.
Blbá situace, ale rozhodli jsme se, že se hostovi omluvíme a epizodu nevydáme.
Tak se i stalo.
Pro Pavlínu funguji jako redakce, takže jsem za to vzal zodpovědnost a sepsal jsem citlivou omluvu.
Host to naštěstí vzal v pohodě, takže dobrý.
Možná spolu nakonec vymyslíme něco jiného.

Mimochodem, zkoušel jsem, zda mi je schopno se sepsáním omluvy pomoci ChatGPT, ale vyhazovalo to věci, které mi přišly necitlivě asertivní a nevhodné pro danou situaci.
Nevím jak vás, ale mě AI zjevně ještě nenahradí.

Pája pak rychle natočila další epizodu a ta vyšla dnes, [tak si ji pusťe](https://junior.guru/podcast/).
Když jsem to dával na YouTube, vyskočilo na mě upozornění, že YouTube už v Česku pomalu spouští svoje speciální funkce pro podcastery.
Označil jsem tedy náš playlist jako podcast a jsem zvědavý, co se bude dít.
[Tahle stránka](https://www.youtube.com/podcasts) u nás zatím nefunguje.
Musím si pak znova pustit [tohle](https://www.youtube.com/watch?v=feMd_GvZSf4&t=1s), ať vím, co čekat.

A jen připomenu, že máte ještě osm dní na hlasování v anketě [Podcast roku](https://www.podcastroku.cz/) 😉

## Další

-   Ataccama [prodloužila partnerství](https://junior.guru/open/ataccama/)!
-   Souhlasil jsem, že budu přednášet na [FrontKonu](https://frontendisti.cz/konference).
-   Anežka z Česko.Digital mě doporučila jako partnera pro [CDW](https://www.beautiful.ai/player/-NUvGiV9GVn6KcmXFcmx/Vyznam-digitalniho-vzdelavani-pro-Czech-Digital-Week).
    Takže jsem si poprvé v životě psal s někým, komu končí e-mail `@vlada.cz` a mám domluvenou schůzku, která bude ve Strakovce.
-   Vylepšil jsem, jak se scrapují a [ukládají](https://github.com/honzajavorek/junior.guru/commit/2586e2143eb129ac09ecf36794d474250a86f587) čísla ohledně mých followers na vybraných platformách.
    Pak jsem to konečně [hodil do grafu](https://junior.guru/open/#marketing).
-   Zpracoval jsem jedno stipendium.
-   Sehnal jsem kancelář!
    Odteď budu každé dopoledne pracovat ze sklepního prostoru u Jiřáku, kam v pohodě dojdu pěšky a v němž NEJSOU ŽÁDNÉ DĚTI.
    Doufám že moje produktivita stoupne aspoň o tolik, o kolik klesne můj příjem kvůli nájmu kanceláře.
-   Můj build na CircleCI umí některé věci uložit zpátky do repozitáře a pushnout zpět.
    Akorát že to dělal i na vedlejších větvích, ne pouze na `main`.
    Tak jsem to chtěl opravit a u toho zjistil, že na to mají [pěknou novou syntaxi](https://circleci.com/docs/using-branch-filters/) a nemusí se to už hackovat v shellu.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), LinkedIn zprávy.
    Hlavně klubu jsem věnoval během těch dvou týdnů opravdu hodně času.
-   Hádal jsem se s podporou [NextBike](https://www.nextbikeczech.com/), že jsem správně umístil kolo a nezasloužím si pokutu, a potom že jsem ho teda sice neumístil správně, ale UI jejich aplikace je v tomto směru naprosto debilní a poskytlo mi dokonalou iluzi toho, že jsem vše udělal správně.
    Pomocí pěti e-mailů jsem pokutu za špatně zaparkované kolo snížil z 300 Kč na 200 Kč a zkouším teď zase používat víc [Rekola](https://www.rekola.cz/).
    Tak či tak, stejně je super, že můžu v rámci Lítačky skočit na kolo a kousek se svézt.
    Na spoustu tras kolem mého bydliště je to mnohem rychlejší a pohodlnější než jít pěšky nebo jet MHD.
-   Zazdil jsem zase společný call Pyvec výboru.
    Už mi to přijde trapné, takže uvažuji nad tím, že si zřídím nějakou věc, která mi před callem vytvoří PagerDuty incident a ten mě postupně upozorní e-mailem, SMSkou a voláním.
    [PagerDuty](https://www.pagerduty.com/) je do pěti lidí zdarma, takže nějak to půjde.
    Jen nevím, jak to propojit s kalendářem.
-   Ozval jsem se opět některým firmám a překvapilo mě, že hned dvě prosily o víc času, protože se tam předává agenda:

    > Chystám se na odchod na mateřskou a připravuji vše pro novou kolegyni, aby její nástup byl co nejhladší :)

    Nebo

    > …já odcházím a pomalu začnu předávat vše mému nástupci, a i toto rozhodnutí má smysl, aby udělal on…

    Škatule hejbejte se!

-   Během 15 dní jsem ujel na kole 266 km. Celkem jsem se hýbal 103 h a zdolal při tom 266 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Užít si dovolenou.
2.  Po dovolené nějak projít klub a maily a zajít na domluvené schůzky.
3.  Dodělat ten frontendový build.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [The coming Russian revolution will unleash horrifying new demons](https://www.telegraph.co.uk/news/2023/05/25/coming-russian-revolution-unleash-horrifying-new-demons/)<br>„Don’t expect another Mikhail Gorbachev. Instead, we could well be looking at a protracted scenario of chaos, violence, rebellion and repression, with fighting between the Russian army, national guard, security services, the plethora of private armies and perhaps Prighozin’s vision of mobs on the streets with pitchforks.“
- [Roman Hraška on LinkedIn: Silicon Valley by nemal byť cieľ w/Peter Širka #65](https://www.linkedin.com/posts/yablko_silicon-valley-by-nemal-by%C5%A5-cie%C4%BE-wpeter-activity-7067114278029275136-9FR9/)<br>Yablko perfektní status. „v tech sektore ľudia akoby zabudli, že je dovolené len vyrábať vec a predávať ju. vyrábať ju, lebo ťa to baví. lebo chceš, aby práve táto vec existovala. tvoriť si svet, kde firma je len potrebná formalita, nie cieľ.“ (Podcast, na který odkazuje, jsem ještě neslyšel)
- [EU AI Act To Target US Open Source Software - Technomancers.ai](https://technomancers.ai/eu-ai-act-to-target-us-open-source-software/)<br>Tohle je šílený. Giganti nemají žádný reálný náskok před open source modely a postupně se dostáváme do situace, že drobné, dostatečně užitečné AI, by si mohl v pohodě každý natrénovat na lepším noťasu. Jenže s novými pravidly se vše zreguluje. Hraju si se Stable Diffusion, je to super. Na obrázek čekám minuty, ale baví mě to. Každý den někdo vymyslí nový způsob, jak to vylepšit, nebo zrychlit. Jdou dělat lepší obrázky. Ale celý ten pokrok stojí na tom, že to je přístupné každému. Je to krásná ukázka toho, co open source dokáže a buduje se kolem toho pěkná komunita. A tohle celé by mohlo být ilegální 🤯 Jediný, kdo bude mít dost peněz projít regulacemi, budou giganti… a na mě naběhne SWAT komando oknem za to, že mám vlastní natrénovaný model na noťasu, díky kterému si můžu vygenerovat svou vlastní fotku s elfíma ušima.
