Title: První týdenní poznámky: Třídění nabídek práce
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Rozhodl jsem se začít s pravidelnými týdenními poznámkami o tom, co jsem dělal a co zajímavého jsem se naučil. V listopadu 2019 jsem odešel z [Apiary](https://byznys.ihned.cz/c1-65593630-oracle-kupuje-za-miliardy-korun-cesky-start-up-apiary-zakladatele-ve-firme-zustavaji) na volnou nohu a začal jsem pracovat na svém vlastním projektu, [junior.guru](https://junior.guru/). Více o projektu se můžete dovědět v [rozhovoru](https://kafemlejnek.tv/dil-52-junior-guru/), který se mnou nedávno vyšel. Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

## Kontext

Jak říkám i v odkazovaném rozhovoru, v současné době jsem doma, žiju z úspor a snažím se na plný úvazek [junior.guru](https://junior.guru/) dotlačit k úspěchu a výdělečnosti. Nevěnuji se prakticky ničemu jinému. Ze začátku jsem si chtěl vyzkoušet, jestli by mě něco takového vůbec bavilo. Po půl roce, co se tomu věnuji, jsem si naprosto jistý, že chci dělat právě a přesně toto:

- One-man show projekt, který třeba neudělá díru do světa, ale vydělá dost na to, aby uživil mě a mou rodinu (inspirace: [@levelsio](https://twitter.com/levelsio/), [@pinboard](https://twitter.com/Pinboard), [Make](https://makebook.io/), [Reconsider](https://m.signalvnoise.com/reconsider/), [Gumroad](https://marker.medium.com/reflecting-on-my-failure-to-build-a-billion-dollar-company-b0c31d7db0e7)).
- Technologický projekt, skrze který mohu pomáhat reálným lidem a mít s nimi přímý kontakt, vidět jejich úspěch.
- Projekt, který vyžaduje, abych využíval všechny aspekty své "renesanční" osobnosti: programátor, produkťák, markeťák, designér, UXák, copywriter, "spisovatel", atd. Zároveň se musím učit novým dovednostem - [kolonizovat]({filename}/2016-12-18_kolonizatori-a-spravci-kolonii.md), prodávat, [vědět kdy automatizovat](https://twitter.com/honzajavorek/status/1257192493034156032?s=21).
- Práce, kterou můžu dělat na volné noze, z domova.
- Projekt, který může něco změnit, který se časem může propracovat k tomu, že umožní i lidem ve znevýhodněných podmínkách změnit život a dosáhnout na lepší životní úroveň.
- [Open Source](https://github.com/honzajavorek/junior.guru)!

Tím bych měl tedy vyřešeno čím vyplňovat čas. Teď už jen ten funkční byznys model, abych to mohl dělat opravdu nekonečně dlouho, a je to! :D Původní myšlenka byla vydělávat na [nabídkách práce](https://junior.guru/jobs/), ale těch možností je víc. Sám se nechám překvapit, co bude fungovat. Nebo jestli to budu muset časem prostě zabalit.

## Proč týdenní poznámky?

Týdenní poznámky jsem okoukal na [blogu Simona Willisona](https://simonwillison.net/) ([@simonw](https://twitter.com/simonw/)) a očekávám, že by mi mohly sloužit pro následující:

- Dávat vědět kamarádům a podporovatelům o své činnosti a svých objevech,
- evidovat svoje strasti a úspěchy, abych neměl po každém týdnu pocit, že jsem vlastně nestihl nic udělat,
- dokumentovat věci, které jsem se naučil. Jednak se mi mohou hodit později, jednak se z nich může přiučit někdo jiný, kdo by to tu náhodou četl. V tomto mě inspiruje zase Vladimír Gorej ([@vladimirgorej](https://twitter.com/vladimirgorej/)), který každou novou znalost promění v článek nebo ji aspoň tweetne.

Poznámky budu psát česky. Chtěl jsem sice na blog psát už hlavně anglicky, ale [junior.guru](https://junior.guru/) je zatím zaměřeno jen na český trh a moji podporovatelé i většina kamarádů jsou místní. Taky by čeština mohla přispět k tomu, že nebudu líný poznámky psát.

## Poznámky

### Třídění nabídek práce

Už nějakou dobu pracuji na tom, abych na [junior.guru/jobs/](https://junior.guru/jobs/) mohl zobrazovat i nabídky práce odjinud. Chtěl bych, aby stránka byla agregátorem co nejvíce juniorních nabídek v Česku a stala se tak hlavním místem, kam budou junioři chodit hledat práci. Nabídky, které firmy zadají přímo na JG budou mít zvýraznění nebo lepší umístění a dostanou se i do newsletteru apod.

Abych ale mohl zobrazovat nabídky odjinud, musím být schopen je třídit. Na pracovních portálech sice občas mají nějaký filtr na juniorní nabídky, ale většinou je to k ničemu. Náboráři nabídky označují náhodně, takže se mezi ně dostane i práce pro architekty a seniory. Také má každý jinou představu o tom, kdo je to junior. Já chci zobrazovat jen "entry level" nabídky, ne něco, kde požadují tři roky zkušeností. Zatímco nabídku zadanou na JG mohu přečíst a zkontrolovat, s 300 nabídkami odjinud to dělat nemohu. Potřebuji automatický inteligentní filtr. No a ten teď programuji. Rozdělil jsem jej zatím na tři kroky:

1. Něco jako "lexer", který bude parsovat HTML a vytáhne mi sekce inzerátu.
2. Něco jako "sémantickou analýzu", která se bude snažit porozumět kouskům inzerátu v jejich kontextu.
3. Pravidla, která vyhodnotí výsledky sémantické analýzy a podle různých vlastností a vah rozhodne, jestli je inzerát juniorní dle mého gusta, nebo ne.

Tento týden jsem navrhl jak by to celé mělo fungovat a vytvořil jsem ten "lexer". Umí zpracovat HTML i obyčejný text. Samotného mě překvapilo, na kolika nabídkách funguje. Používám [lxml](https://lxml.de/) a svůj vlastní algoritmus, ze kterého se mi tak motala hlava, že jsem si ho musel nejdřív nakreslit na papír jako [konečný automat](https://cs.wikipedia.org/wiki/Kone%C4%8Dn%C3%BD_automat).

Dal jsem si záležet, aby poznal odrážkový seznam i pokud recruiter místo odrážek použil náhodné emoji. Mám z toho radost, protože to vypadá, že to opravdu asi nějak půjde a neprošlapávám nějakou úplně slepou cestu.

### Další vylepšení a opravy v nabídkách práce

- Už delší dobu mám vytvořený filtr, který detekuje jazyk nabídky práce přes [langdetect](https://github.com/Mimino666/langdetect) a vyhazuje ty, které nejsou česky, slovensky, nebo anglicky. Zjistil jsem ale, že funguje lépe, pokud z textu nejdřív odstraním HTML tagy.
- Pro lokální vývoj kešuji přes [Scrapy](https://scrapy.org/) všechny HTTP požadavky, abych nezatěžoval cílové servery svými pokusy. Jenže tak někdy vznikne nesrovnalost mezi skutečností a keší a stáhne se neúplná pracovní nabídka. Vytvořil jsem tedy filtr, který je zahazuje.
- Z dat ze StartupJobs to vypadá, že podporují více měst u jedné nabídky práce. Promyslel jsem to a rozhodl se, že takové případy budu (zatím) řešit tím, že se prostě nabídka zduplikuje pro každé město zvlášť. Nevypadá to, že je to úplně běžné.
- StartupJobs mají v nabídkách práce "externí spolupráci" jako jeden z typů zaměstnání. Přidal jsem pro to podporu.
- V exportu nabídek od StartupJobs chybělo datum nabídky. Poprosil jsem, aby mi jej přidali, a potom pro něj přidal podporu.
- Zvažuji, že bych na JG zobrazoval i nabídky kousek za hranicemi. Přece jen může pro někoho z Mikulova dávat smysl jezdit do Vídně. Zvláště v Německu je spousta nabídek práce. Německé nabídky (a nejen ty) mají ale ve zvyku být explicitně genderově korektní a všechny mají v titulku m/f/x apod. jako znamení, že počítají s muži, ženami, i kýmkoliv jiným. Mě to přijde zbytečné smetí, protože je přímo v zákoně, že diskriminovat se nesmí, a tudíž by to mělo být tak nějak implicitní. Mám proto čistič, který tyto značky z nabídek práce osekává. Tento týden jsem do něj přidal podporu pro české a francouzské značky.
- Vytvořil jsem prototyp stahovače nabídek práce z LinkedIn, čímž už jsem se dostal na tři různé zdroje a stovky stažených nabídek. Jedno programátorské pravidlo říká, že se může začít zobecňovat až když mám tři různé instance, takže k psaní inteligentního filtru na juniorní nabídky (viz výše) jsem se odvážil až když jsem měl tři zdroje nabídek a spoustu dat na otestování.
- Tři zdroje nabídek znamená tři stahovače a tři stahovače si už daly docela načas. Takže jsem si vzal [multiprocessing.Pool](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool) a přes `Pool().map()` jsem to pustil hezky vedle sebe. Tím jsem si ovšem zadělal na další problém.
- SQLite, kam nabídky ukládám, není zrovna dělaná na velká množství souběžných zápisů. Když pustím několik stahovačů paralelně, občas zápis skončil na tom, že byla databáze zamčená. Řešení to moc nemá. SQLite mi ve všem ostatním vyhovuje a je mi jedno, jestli stahovače skončí dříve nebo později, takže jsem to ošidil prostě tím, že se při chybě zkusí zápis znovu, dokud se to nepovede.
- Vylepšil jsem administraci JG tak, abych lépe viděl co se stahuje a co se proč vyhazuje. Taky jsem přidal `<textarea>` s textem nabídky, aby se mi lépe vytvářely fixtures do testů.
- Můj stahovač nezvládal situaci, kdy se na [StackOverflow Jobs](https://stackoverflow.com/jobs) objeví nabídka zadaná přes agenturu. U jména firmy se potom navíc objevuje "via" a jméno agentury. Otestoval a opravil jsem to.

### Jiná vylepšení a opravy

<blockquote class="twitter-tweet"><p lang="cs" dir="ltr">25.4. přišel e-mail &quot;You&#39;ve been approved for GitHub Sponsors&quot;<br>30.4. mám už čtyři sponzory! 💖<a href="https://github.com/sponsors/honzajavorek/">https://github.com/sponsors/honzajavorek/</a></p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/status/1257554874360827905?ref_src=twsrc%5Etfw">May 5, 2020</a></blockquote>

- K podporovatelům z GitHub Sponsors jsem do [seznamu](https://junior.guru/donate/#sponsors) přidal Petera, historicky prvního patrona z [Patreonu](https://www.patreon.com/honzajavorek)!
- Po diskusi s kamarádem recruiterem jsem přidal kód, který mi do Google Analytics zaznamená "event", pokud někdo klikne na tlačítko na nabídce práce. Tím bych mohl aspoň přibližně změřit kolik lidí opravdu projevilo zájem. Protože některá tlačítka nejsou odkaz ale obsahují e-mailovou adresu na okopírování, jako spouštěč mám zatím prostě `mousedown`.
- Předělal jsem Python importy v celém projektu na absolutní. Nevím, proč jsem původně začal s relativními.
- Když už jsem byl u toho, začal jsem v projektu používat [isort](https://github.com/timothycrosley/isort/). Vlastně nevím proč, asi jsem se prostě neudržel a moje [správcovská duše]({filename}/2016-12-18_kolonizatori-a-spravci-kolonii.md) na chvíli převládla nad rozumem. Testy píšu, ale schválně zatím nepoužívám žádný linter ani nic jiného, aby mě to nezdržovalo, zvlášť když na JG dělám sám. Řazení importů pomocí git hooku je zbytečnost navíc a propálený čas. Ale jako importy řazené podle abecedy, kdo z vás to má?

### Hledání JS frameworku

[Hledám JS framework pro frontend](https://twitter.com/honzajavorek/status/1256512776027230208?s=21). Zatím na [junior.guru](https://junior.guru/) vše píšu ve [Vanilla JS](http://vanilla-js.com/) a [HTML DOM](https://htmldom.dev/), protože jde jen o pár řádků, ale do budoucna budu potřebovat psát i složitější věci a chci mít po ruce něco, co bude splňovat moje požadavky:

- Pracuje s HTML renderovaným na serveru pomocí Pythonu, není to SPA,
- má co nejmenší footprint na výkonu, bundlu, všem.

Projekt typu JG mi přijde nesmyslné tvořit jako SPA, přináší to obrovské množství zbytečné komplexity navíc. Taky chci mít backend prostě v Pythonu a vrstvu navíc v podobě nějakého API tam mít nepotřebuju. Zatím jsem zaznamenal [StimulusJS](https://stimulusjs.org/) a [Unpoly](https://unpoly.com/). Několikrát mi někdo doporučil [Svelte](https://svelte.dev/), ale pořád jsem nezjistil, jestli protože to splňuje moje požadavky, nebo protože je to teď cool. Zatím jsem si jen procházel [tuto prezentaci o Unpoly](http://triskweline.de/unpoly-rugb/#/30).

### Činnosti nesouvisející s JG nebo jen mírně

- Jeden mentorovací videohovor.
- Review článku kamarádky juniorky, která chce začít blogovat.
- Po dlouhé době jsem odpověděl na všechny e-maily. Součástí toho je brainstorming s jedním mentorem jak ideálně prezentovat české mentory na JG.
- Diskuse o tom, jestli by [brněnské Pyvo](https://pyvo.cz/brno-pyvo/) mělo nebo mohlo propagovat [Zázvorodku](http://www.zazvorodka.cz/) a další způsoby, jakými lze přispět na ArtBar, kde se sraz tradičně koná. Aby nám to tam nezaniklo a mohl se tam konat i po koronaviru.
- Radoval jsem se z toho, že se [povedlo natočit film](https://www.hithit.com/cs/project/6835/dokonceni-filmu-nova-sichta/news/9462) o horníkovi Tomáši Hisemovi, který [se stal programátorem](https://www.tedxprague.cz/videa/z-hornika-programatorem), a na který jsem přispěl.
- Radoval jsem se z toho, že se povedlo [Emmě Bostian](https://twitter.com/EmmaBostian) dokončit a vydat knihu pro juniory, [De-Coding The Technical Interview Process](https://technicalinterviews.dev/). Měl jsem ji koupenou v předprodeji, jednak abych Emmu podpořil, jednak abych to mohl přečíst a případně knihu doporučovat. Navíc mám rozepsaného něco podobného, takže mě zajímá, jak moc se to překrývá. Zajímavé bylo sledovat i proces vydávání knihy přes Gumroad s různými teasery, reviews, pre-orders. Už na tom je vidět, jaký je Emma o dost lepší obchodník než bych byl v takové situaci já.
- [Bojoval jsem s Google Cloudem](https://twitter.com/honzajavorek/status/1257646326977888257), aby mi nezastavil všechny služby, ale abych měl jistotu, že za něj nebudu nic platit. Zrovna nedávno si známý na FB stěžoval, jak tam něco neuhlídal a vyžralo mu to peníze z karty.

### Náhrada za ZEIT Now

[Řeším](https://twitter.com/honzajavorek/status/1252952477227536384), kam bych převedl svoji [film2trello](https://github.com/honzajavorek/film2trello) appku a ukázková API z [cojeapi.cz](https://cojeapi.cz). Nedávno jsem všechno nadšeně [převedl na ZEIT Now]({filename}/2020-01-23_how-i-deploy.md), ale ti se teď [přejmenovali na Vercel a jasně deklarovali, že jejich cílovka jsou frontendisti](https://rauchg.com/2020/vercel). Technicky se zatím nic nemění, ale mě je jasné, že podpora pro čisté Python aplikace se bude ztrácet a ostatně už i několika posledními změnami hodili mým projektům dost klacků pod nohy. Z nadšence jsem tedy velmi rychle vystřízlivěl. Zatímco statické stránky asi všechny vrátím na [GitHub Pages](https://pages.github.com/) (a napíšu článek o tom proč a jak), tak s deploymentem jednoduchých aplikací zatím nevím. Vypadá to, že svoje film2trello dám možná někam pomocí [Serverless](https://www.serverless.com/), a že cojeapi.cz, kde jde hlavně o čtenáře a účastníky workshopu, přemigruji na [Glitch](https://glitch.com/) nebo [Repl.it](https://repl.it/). Zatím jsem ale nic v tomto ohledu nepodnikl, kromě toho, že jsem omylem zabil film2trello (viz níže).

### Přesun blogu

Tento blog běží na [Pelikánovi](https://docs.getpelican.com/) a z nějakého důvodu, který si nevybavuji, mi to s ním fungovalo líp, když jsem při generování nastavil absolutní URL. To ale na ZEIT Now moc nešlo. Hackoval jsem to přes API k GitHub Deployments, abych v průběhu buildu zjistil, jaké bude výsledné URL toho konkrétního deploymentu, ale stejně mi to nefungovalo moc dobře a byla to komplexita navíc. Teď jsem zahlédl, že má Vercel nově v dokumentaci proměnnou `VERCEL_URL`, tak jsem to šel použít. Jenže i v Pull Requestu se v této proměnné objevovalo prostě jen `https://honzajavorek.cz/`, takže mi to nic neřeší. To mě naštvalo a i v rámci rozhodnutí zmíněných výše jsem celé [honzajavorek.cz](https://honzajavorek.cz/) i s blogem převedl během čtvrtečního večera zpět na GitHub Pages. Deployment teď díky tomu dělám už jen pomocí [GitHub Actions](https://github.com/features/actions), je zcela přímočarý a pod mou kontrolou. Navíc jsem objevil hezkou akci [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages), která dělá vše kolem GitHub Pages. Dokonce nemusím ani řešit žádné tokeny, vše je už jen v rámci GitHubu. Celé je to o dost jednodušší, což mi stojí za ztracené náhledy pod Pull Requesty. Ty stejně nepotřebuju, když jsem sám. Je to jen blog, prostě to házím do `master` větve a jedu. Je vidět, že jsem předtím prostě propadl nadšení a GitHub Pages úplně stačí. Na takto jednoduché hobby projekty je pro mě Vercel i Netlify zbytečný kanón na vrabce.

Během přesunu DNS z Vercelu zpět na WEDOS jsem samozřejmě zapomněl, že mám na subdoméně [honzajavorek.cz](https://honzajavorek.cz/) i Vercel aplikaci s tím film2trello, takže jsem ji tím zabil a pokud si se ženou budeme chtít posílat ČSFD stránky do Trella, budu to muset v blízké době opravit.

### Skript na poznámky

No a naprogramoval jsem si taky ještě [weeknotes.py](https://github.com/honzajavorek/honzajavorek.cz/blob/master/weeknotes.py), skript, který mi pomůže připravit článek na další týdenní poznámky.

## Shrnutí

Bylo to dlouhé, ale hlavně proto, že jsou to první poznámky, a ve spoustě případů jsem potřeboval čtenáře uvést do rozjeté problematky. Taky tento týden dost pršelo, takže jsem toho udělal poměrně hodně :) Uvidíme příští pátek, jestli mi psaní těchto poznámek vydrží aspoň dva týdny.
