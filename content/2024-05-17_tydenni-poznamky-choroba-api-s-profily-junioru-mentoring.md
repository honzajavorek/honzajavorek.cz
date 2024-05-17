Title: Týdenní poznámky: Choroba, API s profily juniorů, mentoring
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/319
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/112458149869744029

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-05-03_tydenni-poznamky-apify-vitani-a-vsechno-mozne.md) už utekl nějaký ten týden (3. 5. až 17. 5.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
</div>

Předchozí týden jsem odpadl s chorobou, konkrétně nějaká viróza. Ještě se z toho hrabu, pořád trochu kašlu a i když jsem pouze doma, tak pořád ještě dost smrkám, ačkoliv se říká, že po týdnu má být rýma už pryč.
Kvůli nemoci jsem nakonec nemohl ani dorazit do [panelové diskuze s yablkem](https://skillmea.cz/blog/prazaci-pozor-ceka-nas-prvni-meetup), takže paneloval, chudák, sám.

Do toho jsem měl něco na kůži v obličeji, co jsme s doktory týden špatně léčili a teprve potom přišli na to, co to je, takže jsem si zase obešel obvoďačku, dermatologii a očního, ale naštěstí to dobře dopadlo.

## API profilů juniorů

Vytvořil jsem repozitář [eggtray](https://github.com/juniorguru/eggtray), který bude sloužit jako API s profily juniorů. Jak to funguje?

Junior pošle Pull Request s YAML souborem v určitém formátu. Když bude vše OK, mergnu to a kód v repozitáři zbuildí do GitHub Pages obyčejný statický JSON soubor `profiles.json`, kde jsou profily všech juniorů.
Přidávání YAML souboru je záměrná překážka, díky které budu vědět, že junior už aspoň trochu umí s Gitem a YAMLem a mohu jim to připsat k dobru při jejich prezentaci firmám.
Založit YAML soubor si může kdokoliv, klidně junior, který není v [junior.guru klubu](https://junior.guru/club/).

Výsledné API může následně kdokoliv využít, aby juniorům pomohl najít si práci.
Třeba já, který si v rámci repozitáře s webovkou junior.guru stáhnu profily z toho API a zobrazím je na webu.
Ale třeba i někdo jiný, co já vím.

Ďábel je však v detailu. Junioři v YAML souboru poskytují jen absolutní minimum informací. Nemusí tam vyplňovat vše jak na LinkedInu a udržovat aktuální. Spoustu informací si načtu přímo z jejich GitHub profilu. Zároveň jsem díky [hen](https://github.com/juniorguru/hen) schopen dle jejich GitHub profilu zhodnotit, zda už jsou připraveni hledat si práci. Všechny tyto informace se poskládají dohromady a vystaví v tom API.

Při sestavování junior.guru navíc mohu toto vše obohatit ještě i o data, která mám o juniorech díky klubu.
Mohu zvýraznit juniory, kteří jsou členové klubu.
Mohu třeba přidat nějaké malé plus za to, že jsou v klubu aktivní a přispívají tam.
A tak podobně.
Při vypisování ale především velmi upozadím, nebo možná vůbec nezobrazím juniory, kteří nepřekonají mnou nastavenou laťku v připravenosti.
Výpis juniorů tak bude zahrnovat jen ty nejvíc připravené a aktivní, a firmy budou zaručeně vybírat z toho nejlepšího, co se mezi juniory na trhu nachází.
A díky tomu, že kontrolu své připravenosti si může junior kdykoliv spustit v klubu přes Discord, mají jasnou zpětnou vazbu a viditelnou cestu k tomu, aby připravení byli.

Docela dlouho jsem ladil formát YAMLu a reprezentaci dat jako „máš nějakou VŠ?“ nebo „jakým oborům mimo IT ještě rozumíš?“.
Několikrát jsem předělal formát dat, který posílá _hen_, nebo který ukládá _eggtray_.
Věřím, že tohle bude ještě doznávat spousty změn, jak se budou přidávat další lidi.
Mám tam zatím čtyři pokusné králíky a dnes se jako pátá sama přidala [Sandra](https://github.com/juniorguru/eggtray/pull/21).

Mám ještě [spoustu nezrealizovaných nápadů](https://github.com/juniorguru/eggtray/issues) a má to strašně málo dokumentace na to, aby se to dalo pořádně pustit mezi lidi, ale funguje to, a to je hlavní.
Udělal jsem i [pokusnou stránku na webu](http://junior.guru/candidates/), kde se kandidáti vypisují.

![výpis kandidátů]({static}/images/screenshot-2024-05-17-at-21-03-20-kandidati-na-pozici-junior-programator-programatorka.png){: .img-thumbnail }

> Hle­dáš do fir­my ju­ni­o­ra? Za­po­meň na in­ze­rá­ty a sto­hy ži­vo­to­pisů. Vy­ber si prostě ze se­zna­mu. Kaž­dý ju­ni­or tady je ově­ře­ný a má za­ru­če­né zá­klad­ní schop­nosti. Vy­bí­ráš z toho nej­lep­ší­ho na trhu. Oslo­vu­ješ na­přímo, nic ne­pla­tíš.

Možná si říkáte: „Jaký to má, Honzo, byznys model? Zase dáváš všechno zadarmo?“ Ale nebojte! Tohle je monetizované tím, že budou mít junioři velkou motivaci stát se členy klubu. Pokud firma někoho z juniorů najme, je to jen dobře, nechci už tak obtížnou situaci juniorům zatěžovat nějakou provizí. To bych jim moc nepomohl. Když bude firma spokojená, budu u ní akorát apelovat na dobrovolné sponzorství a podporu projektu. Věřím, že kdo na to bude mít chuť a budget, tak si z toho sedne na prdel a ty peníze mi pošle. Kdo juniora najme, ale nebude mít chuť a budget na finanční podporu junior.guru, tak ať, hlavně že má junior práci a já mám aspoň _success story_.

Při tvorbě tohoto celého jsem poprvé použil knihovnu [pydantic](https://docs.pydantic.dev/) (lepší dataclasses) a [moc se mi to s ní líbí](https://mastodonczech.cz/@honzajavorek/112450485166161257), šetří mi hromadu práce. Umí i vygenerovat JSON Schema, tak jsem ho přidal do API jako zoufalou pomoc komukoliv, kdo by nad ním chtěl něco stavět, ačkoliv formát API zatím ještě z hodiny na hodinu radikálně měním.

Taky jsem se naučil nový způsob, jak deploynout GitHub Pages. Nemusí se už commitovat do `gh-pages` větve, dají se použít GitHub Actions.

## Předělaný mentoring

Není to žádná velká sláva, spíš něco, o čem už strašně dlouho mluvím, a konečně jsem to zrealizoval.

Dříve byli mentoři v klubu vystaveni do „vitrínky“, ve které si je mohli junioři vybírat. Často jediné spojení s mentory bylo skrze odkaz na rezervaci v kalendáři. Bylo pro mentory obtížné přidat se do nabídky, odebrat se z nabídky, upravit si popis nebo podmínky, za jakých chtějí mentorovat, a bylo těžké udržet nějakou kvalitu vztahu mezi nimi a _mentees_, protože neexistovalo místo, kde by šlo nějak viditelně komunikovat.

Nyní vitrínka mizí a přichází tržiště realizované Discord kanálem typu „forum“. Kdo bude chtít nabídnout mentoring, založí tam prostě příspěvek. Do něj může napsat něco o sobě, podmínky mentoringu, odkazy do kaledářů nebo e-mail, nebo cokoliv, co mu nebo jí přijde vhod. Protože to napíšou sami, bude to zcela podle nich a když se něco změní, mohou úvodní příspěvek libovolně v budoucnu sami upravit. Pod tímto příspěvkem lze navíc vést diskuzi, např. domlouvat se, zda je ještě místo, nebo je plno, nebo tam mohou „vyvolat“ někoho, kdo se nedostavil na _call_, apod. Také klidně mohou nabídnout placený mentoring, prostě to akorát uvedou v podmínkách.

Kromě toho budou moci příspěvky do tržiště přidávat i junioři, když budou mentoring poptávat. Pokud se tedy mentor nechce nabízet komukoliv, nemusí se vůbec nikde vystavovat. Může prostě sledovat, jestli přibude poptávka, která vás zaujme, a člověku se individuálně ozvat. Takhle se mohou objevit i mentoři, kteří si třeba ani nemysleli, že by mentoring nabídli, ale když uvidí poptávku, zjistí, že dokážou pomoci.

Forum má povinné štítky, které rozlišují nabídku a poptávku, a pak jeden, který umožňuje „zavřít krám“, pokud by člověk dočasně či trvale neměl už volné kapacity. Do budoucna chci ještě přepracovat [stránku o mentoringu v příručce](https://junior.guru/handbook/mentoring/) a vše tam vysvětlit, nový systém v klubu zdokumentovat, a doplnit automatizace, které jej podpoří. Např. aby bot lidem radil, jak má vypadat správně napsaná poptávka nebo nabídka, aby to dobře fungovalo a nechyběly podstatné informace.

Tak jsem teda konečně, po dlouhém kolečku sbírání zpětné vazby a názorů od mentorů i juniorů, udělal to forum, archivoval starou „vitrínku“, a smazal veškerý kód, který s automatizovaným micromanagementem mentoringu souvisel. Ani nevím, proč mi realizace trvala tak dlouho. Asi jsem potřeboval hodně ujištění, že jdu správným směrem, a taky mi trvalo uvědomit si, že se všechny automatizace a vylepšení dají přidat později a do začátku stačí prostě jen vytvořit to forum a koukat, co s tím budou lidi ve skutečnosti dělat.

Chtěl bych tady nepřímo poděkovat dvěma novým mentorům, kteří mě k realizaci aktuálně došťouchali.
Konečně jsem s tím pohnul!

## Kamera v čoudu

Odešla mi na MacBooku kamera.
Ze dne na den.
Nevím proč, s noťasem se nic nedělo, nikam nespadl, nic se na něj nijak zásadně nevylilo.
Potvrzuje to diagnostika přímo na noťasu, že odešla kamera a čislo na stmívání displeje, a potvrzují to [všechny pokusy o to nějak kameru oživit](https://www.reddit.com/r/applehelp/comments/fvacxn/there_is_no_camera_connected_to_my_inbuilt_camera/).

![Kamera v čoudu]({static}/images/img-8822.jpeg){: .img-thumbnail }

Je to dost nepříjemné.
Noťas [mám 4 roky]({filename}2020-12-18_i-bought-apple-silicon.md), takže záruka nic.
Oprava, pokud je to jen výměna celého displeje a není nic s deskou, je minimálně na 10-14.000 Kč.
Což je stále zlomek ceny noťasu, ale je to dost peněz, které mám psychický blok dát za něco, co ještě před týdnem fungovalo a najednou nefunguje, ačkoliv jsem já špatně nic neudělal.

Zároveň nechci externí kameru.
Nepoužívám ani externí monitor, protože mám rád svůj stroj _portable_.
S noťasem se dost pohybuji, tu jsem v kuchyni, v obýváku, v ložnici, v kanceláři, ve vlaku, na konferenci, v kavárně.
Tahat všude externí kameru, nebo ji někde zapomínat, je to úplně poslední, co chci.
Zároveň mám relativně často nějaký _call_ a chci si zachovat možnost skočit na _call_ kdykoliv potřebuji.
Externí kamera by byla prostě mega opruz.

Další možnost je [použít telefon](https://support.apple.com/en-gb/guide/mac-help/mchl77879b8a/mac#:~:text=On%20your%20Mac%2C%20open%20any,rear%20camera%20to%20your%20Mac).
Ten mám všude u sebe, takže asi proč ne.
Jenže iPhone X je prý moc starý a na tohle není už podporovaný 🖕
Uvažuji tedy o koupi nového telefonu.
Ten by stál méně nebo stejně jako oprava (přemýšlím nad iPhone 12 mini nebo 13 mini, velké telefony jsem nikdy nepochopil a nikdy jsem si je neoblíbil) a ještě bych za ty peníze měl upgrade telefonu, což by umenšilo mou bolest z této nepříjemné situace.

## Další

-   Vyšla se mnou [epizoda podcastu PeopleOps](https://www.forendors.cz/p/1c23124f86aa5420ef8261f585ad5942). Propagoval jsem to [na LinkedInu](https://www.linkedin.com/feed/update/urn:li:activity:7196159964824961024/) i [na Mastodonu](https://mastodonczech.cz/@honzajavorek/112441039395872639).
    Irena si s tím dala práci, takže budu rád, když si epizodu koupíte, nebo si podcast předplatíte.
    Pokud jste ale moje máma nebo tak někdo, tak mi akorát napište, můžu poslat mp3.
-   Přesunul jsem doménu junior.guru ze SubRegu na WEDOS.
    Když jsem ji registroval, WEDOS ještě neuměl .guru, tak jsem si založil účet na SubRegu, ale jinak mám všechny domény u WEDOSu.
    Pro jednoduchost správy jsem ji teď, když už WEDOS .guru domény umí, zmigroval k těm svým ostatním.
    Vyžádlo si to snad první historický výpadek webu, o kterém jsem se dověděl díky lidem z klubu.
    Tak jsem si řekl „aha, už to asi převedli“, a šel přepisovat údaje do nových DNS 😀
-   Zkoušel jsem vyrobit písničku s [LMMS](https://lmms.io/), ale zatím jsem nedokázal navázat na svůj um z puberty (byť tenkrát to bylo s nějakým ukradeným [Fruity Loops](https://www.image-line.com/fl-studio/)).
    Jsem zvědav, jestli to ještě zkusím, nebo to bude jen náhodný pokus.
    Ty písničky vyprodukované někdy na gymplu jsou docela motivační - takové to, že vím, že už jsem to jednou uměl, že to šlo.
    Ale teď na to samozřejmě nemám tolik času.
    Při sledování [tohoto videa](https://www.youtube.com/watch?v=XyrCwuU43Qc&t=358s&pp=ygUEbG1tcw%3D%3D) jsem si připadal asi stejně, jako si připadá junior, když vidí yablka na YouTube sekat web v Tailwindu nebo tak něco.
-   Když nakopírujete hromadu souborů na iCloud, ale máte pomalý internet a chcete pak něco dělat, třeba koukat na streaming F1 v Miami, nejde upload iCloudu bohužel nijak pozastavit.
    Našel jsem ale [skript, který mu zabíjí procesy](https://github.com/farnots/StopNsurlsessiond/blob/master/StopNsurl.sh) a tím to pozastaví 💪
-   Czechitas ode mně dlouhodobě odebírají přes API data o pracovních inzerátech, která si následně analyzují, aby věděli, kde je jaká poptávka po čem.
    Chtěli tam nějaké změny, tak jsem je udělal.
-   ENGETO píše nějaký článek a poprosili mě o vyjádření, tak jsem se do něj vyjádřil.
-   Odepsal jsem do JetBrains. Ač obě strany zaneprázněné, po malých krůčcích posouváme malou spolupráci. Všichni členové klubu díky tomu mají např. velmi výraznou slevu na [JetBrains Academy](https://www.jetbrains.com/academy/).
-   Firma, jejíž pověstí si nejsem úplně jistý, vložila na junior.guru inzerát a u toho ještě zaškrtli, že chtějí zlatý tarif. Dnes jsem jim zcela narovinu odepsal, že bohužel, ale kvůli jejich pověsti na českém internetu s nimi nechci být spojován, pracovní inzerát neuveřejním a peníze si od nich nevezmu. Nemusel jsem psát důvod, ale přišlo mi fér, aby věděli, že jejich prezentace a chování má nějaký reálný dopad a omezuje jim možnosti spolupráce.
-   Byl jsem v kině na [Písečné ženě](https://www.csfd.cz/film/124512-pisecna-zena/) a bylo to parádní.
    Strašně mi to v ten den sedlo.
    Celý film jsem seděl jak na trní a pak o něm ještě dlouho přemýšlel.
-   Objevil jsem [just](https://github.com/casey/just), ale neměl jsem zatím čas ho prozkoumat.
-   Lucie Lenértová mě přivedla na [zajímavý nástroj pro postprodukci zvukové stopy](https://www.youtube.com/watch?v=3pAnI7Npi8U&t=437s). Wow!
-   Užil jsem si vítězství McLarenu v Miami!
    Normálně mi při závěrečném ceremoniálu zvlhly oči, jakou jsem měl radost, že Lando Norris konečně vyhrál.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Naštěstí toho nebylo nějak strašlivě moc, ačkoliv jsem marodil a to se pak většinou nasbírá. Asi byli lidi díky svátkům na dovolených.
    Udělil jsem jedno stipendium.
-   Za 15 dní jsem naběhal 8 km, při procházkách nachodil 13 km. Celkem jsem se hýbal 8 h a zdolal při tom 21 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Budu mít opět Apify týden. Uteklo to nějak rychle, ale bohužel hlavně kvůli mému chatrnému zdraví.
2.  Podívám se na připravované změny v textu [stránky o psychickém zdraví](https://junior.guru/handbook/mental-health/).
3.  Musím napsat speakerovi, aby dodal [detaily o nadcházející přednášce](https://junior.guru/events/42/).

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Pláže, hory a gangy. Jak se žije na Haiti plném násilí? — PULS](https://podcasters.spotify.com/pod/show/jolana-humplov/episodes/Ple--hory-a-gangy--Jak-se-ije-na-Haiti-plnm-nsil-e2j5dtu)<br>Toho, jaké výhody vám dává funkční stát, si všimnete, až když kolem vás není. O situaci na Haiti. Doporučený poslech pro všechny anarcho-něco.
- [Tři trendy: Country, máslo a hotdogová limonáda   — PAVLINA_SPEAKS](https://www.pavlinaspeaks.com/blog/tritrendy)<br>„Z ledničky na mě koukaly nejen všechny příchutě světa, ale hlavně mrkaly jaké dobro mi způsobí, pokud je vypiju. Od vitamínů, přes kolagen, vlákninu, prebiotika, CBD až po houbové extrakty, co slibují dlouhověkost. Z večerky se stala pobočka lékárny s posilovnou.“
- [M&M24 258: Do fochu!](https://bigvilik.wordpress.com/2024/05/13/mm24-258-do-fochu/)<br>Přesný.
- [“Link In Bio” is a slow knife - Anil Dash](https://www.anildash.com//2019/12/10/link-in-bio-is-how-they-tried-to-kill-the-web/)<br>Proč platformy neumožňují nebo penalizují odkazy. „If anyone on IG can just link to any old store on the web, how can IG — meaning FB, IG’s increasingly-overbearing owner — tightly control commerce on its platform? If IG users could post links willy-nilly, they might even be able to connect directly to their users, getting their email addresses or finding other ways to communicate with them. Links represent a threat to closed systems.“
- [NOX vs TOX – WHAT are they for & HOW do you CHOOSE? 🐍](https://www.youtube.com/watch?v=ImBvrDvK-1U)<br>Konečně mi to někdo pořádně vysvětlil a ukázal! tox vs Nox
- [Did You Know Czech Railways Are This Good? - YouTube](https://www.youtube.com/watch?v=lBroMoqE2RY)<br>Co jste možná o české železnici ani nevěděli…
- [Why AI art struggles with hands](https://www.youtube.com/watch?v=24yjRbBah3w)<br>Proč AI neumí ruce. Ve skutečnosti neumí nic, ale u rukou si toho všimnem.
- [Heat Death of the Internet - takahē](https://www.takahe.org.nz/heat-death-of-the-internet/)<br>Tohle bolí číst. Popisuje to ty malé otravné bitvy, které musíme každý den vybojovat s dnešním internetem, a které nám nedávají vůbec nic, takže se na ně snažíme okamžitě zapomenout.
- [20 let společných hodnot. Ale jakých?](https://davidklimes.cz/newsletter/191)<br>Klimeš: „…můžeme pociťovat nemalý smutek, že ona konstruktivní a přijatelná unijní politika je ukázková princezna Koloběžka a znamená rozhodné pro i proti euru, pro i proti federalizaci, pro i proti Green Dealu, pro i proti úplně všemu, na co by občan čekal jednoznačný politický názor“
