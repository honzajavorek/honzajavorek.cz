Title: Týdenní poznámky: Vánoce a velké plánování
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/339
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/113883431667777182

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-12-20_tydenni-poznamky-nove-prednaskove-plakatky.md) už utekl nějaký ten týden (20. 12. až 24. 1.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Stará „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md), nová teď nejsou.

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Dnes uplynul měsíc od Štědrého dne a ještě delší doba uplynula od posledních poznámek na tomto blogu. Po Vánocích mi přišlo, že není o čem psát, a navíc jsem byl nemocný. Tak jsem to nechal být, pak jsem neměl čas, no a teď už je toho zase strašně moc. Předsevzetí: Poznámky musím psát, i když budu mít pocit, že v nich nic nebude. Jinak se to nakumuluje a těžko se to dohání.

## Vánoce

Vánoce jsme prožili překvapivě v klidu, napůl v Praze a napůl u Zlína. Udělali jsme to letos jinak než obvykle. Neoutsourcovali jsme přípravu svátků u našich předků, ale rozhodli se vzhledem k rostoucímu malému potomkovi uspořádat Štědrý den se vším všudy u nás doma. Pořídili jsme stojan, stromek, baňky, světýlka a připravovali jsme jídlo. Přípravy jsme rozložili docela dobře mezi dva lidi a průběžně přes celý prosinec, tak to ani nebylo nějak stresující a vše se povedlo. A příště už to jen vytáhneme z krabic ve sklepě a bude to ještě jednodušší 💪

![Moje LEGO]({static}/images/img-3659.jpg)

Babička si malou brala docela na starost, takže jsme si se ženou přes svátky zvládli udělat i párkrát rande ve dvou a bylo to fajn. Zašli jsme si třeba povídat do čajovny. Já ani nevím, kdy jsem byl naposledy v čajovně, nějak to plíživě vymizelo z mého života. Navštívili jsme i nějakou další rodinu, jedny kamarády, a viděli velbloudy a lamy v zookoutku Starém Městě.

Přes Vánoce jsem naplno odpočíval a nezabýval se vůbec ničím, co jakkoliv souviselo s prací. Myslel jsem, že se začnu nudit a jednoho dne to vytáhnu a něco udělám, třeba i jen nějakou malou srandu pro radost, na kterou není jindy čas, ale nuda nenastala.

![Velbloud ve Staráku]({static}/images/img-3705.jpg)

Raději jsem čas využil k tomu, abych se zamyslel nad životními plány a uspořádal si osobní poznámky a cíle. Přemýšlel jsem nad tím, co hezkého bych si přál v roce 2025 zažít, a to jak v kontextu celé rodiny, ale i partnersky nás dvou se ženou, nebo i co bych rád zažil já sám. Takže teď koukáme po letenkách, po kalkulačkách na webech bank, a já si občas otevřu mapu, abych se podíval, jak se dá na kole dojet do Švédska, kam se mi odstěhoval kamarád.

Nakonec jsem ale programování přece jenom otevřel a vytvořil bota [@p3news](https://mastodonczech.cz/@p3news), který na Mastodon posílá oficální zprávy o Praze 3.

![Zprávy o Praze 3]({static}/images/screenshot-2025-01-24-at-10-35-05-zpravy-z-prahy-3-p3news-mastodonczech-cz-mastodonczech.png){: .img-thumbnail }

## Tablet

Napadlo mně, že bych si mohl pořídit kreslící tablet a tím obnovit svou chuť kreslit ilustrace pro účely junior.guru, nebo českých Python aktivit. Teď se totiž vymlouvám na to, že postprocessing věcí nakreslených na papír je otravný a zdlouhavý, že to žere čas, a že mě to pak nebaví. Jestli nová hračka moje kreslení odblokuje, to netuším, ale když neodstraním překážky, tak se to nedovím.

Nakoukal jsem tedy [nejrůznější videa](https://www.youtube.com/watch?v=mcaL1Vramgk) o tabletech a pak se brácha ozval s tím, že má jeden na půjčení, takže jsme se domluvili a od tohoto týdne ho mám doma. Dalo práci ho rozběhat, protože je to starý kousek a já mám nový operační systém, ale zachránil mě borec z Nového Zélandu, který ten ovladač na koleně opravil a [má ho na GitHubu](https://github.com/thenickdude/wacom-driver-fix). Jen díky tomu jsem to včera večer rozchodil, takže jsem mu hned poslal něco přes Ko-fi jako poděkování. Více jsem s tabletem zatím nestihl. Toto na něm ve Photopea stihla ještě před večeří nakreslit dcera:

![Kreslení na tabletu]({static}/images/new-project.png)

## Balíček fiobank

O Vánocích jsem měl čas podívat se na zbylé Pull Requesty od Michala Čihaře, které poslal na mou knihovnu [fiobank](https://github.com/honzajavorek/fiobank). Přisypal jsem tomu projektu ještě nějakou lásku a dotáhl jsem to až k [vydání verze 4](https://github.com/honzajavorek/fiobank/releases/tag/v4.0.0). Ta vypadá, že funguje, na junior.guru už ji používám.

Balíček fiobank je teď můj první projekt, který sice využívá `pyproject.toml`, ale nemá tam Poetry. Dalo mi to trochu zabrat vykoumat, ale zdá se, že to frčí. Na instalaci používám `uv`. Ještě v tom nejsem úplně zběhlý, ale je fajn, že jsem se aspoň zase naučil něco nového.

![Release v4]({static}/images/screenshot-2025-01-24-at-12-57-02-release-v4-0-0-honzajavorek-fiobank.png)

## Poetry

Když už jsme u Poetry, tak vyšla verze 2. Nevím, co tam je nového, ale rozbilo mi to úplně všechny projekty, protože tam byl nějaký [bug s `poetry run`](https://github.com/python-poetry/poetry/issues/9961). Takže jsem šel a na asi pěti nebo možná i více projektech jsem musel všude v GitHub Actions konfigurácích nebo v `Dockerfile` jít a připnout verzi na 1.x.

Nestěžuju si, autoři Poetry vydali velkou verzi, a i bez toho bugu tam mohly být breaking věci, takže je to spíš můj problém, že jsem to neměl zapinované. Ale nepotěšilo a strávil jsem s tím docela dost času.

Lidi píšou kritické články na adresu Poetry a oslavné články na adresu `uv`, tak uvidíme, jestli někdy vůbec na v2 upgradovat budu. Když už se v nějakém projektu budu šťourat, možná ho rovnou převedu na `uv` a bude to.

## Čtení Veseckého

Udělal jsem trololo [status na LinkedIn](https://www.linkedin.com/posts/honzajavorek_tak%C5%BEe-m%C5%AFj-pl%C3%A1n-na-2025-je-asi-jasn%C3%BD-dnes-activity-7280613158442958848-AtGc), kam jsem plácl svůj sen o tetřevovi. Hned se tam zjevil Adam Vesecký, který na LinkedInu sbírá bizáry. Dostat se do jeho lednového výběru by pro mě byla čest.

Každopádně ač jsem ho znal a možná i sledoval, pojal jsem toto jako příležitost zjistit, co je vlastně zač. Připomenul jsem si, že je autorem článku o tom, jak [absolvoval 100 pohovorů](https://vesecky-adam.medium.com/100-interviews-in-1-year-what-have-i-found-part-i-the-data-090aebe68ff5) během svého sabatiklu. Má to několik částí a já si na to tehdy nenašel čas, tak jsem to zrovna celé přelouskal, když byl ten vánoční klid. Bylo tam i pár mouder, které se mohou hodit do příručky na junior.guru.

Taky jsem se podíval, kde Adam pracuje. A zjistil jsem, že [Navigara](https://navigara.com/en/about) scrapuje nabídky práce! A že sídlí kousek ode mně na Žižkově. Tak jsem jim napsal, jestli si nepopovídáme, protože by se mi možná líbilo data z těch nabídek nějak propojit s [junior.guru/jobs/](https://junior.guru/jobs). Následně z komunikace vyplynulo, že přes kamaráda dokonce znám jejich CEO. Na schůzku zatím nedošlo, protože nám trvá domluva (aktuálně je míček na mé straně), ale jsem zvědavý, jestli z toho něco bude.

Pokud jo, tak by status s tetřevem byl po byznysové stránce nadmíru úspěšný!

## VELKÉ PLÁNOVÁNÍ

Na přelomu roku jsem měl trochu krizičku. Propadl jsem nejistotě, co bude s junior.guru dál, a jestli je vůbec v mých silách dostat tam víc lidí a udělat všechny ty věci, co jsem tam chtěl vždycky udělat. Přišlo mi, že se pachtím a pachtím, ale výsledky jsou malé a pomalé. A taky na mě dolehlo, že už to dělám déle jak 5 let, což je [déle než prakticky cokoliv jiného, co jsem kdy dělal](https://mastodonczech.cz/@honzajavorek/113797515207949376).

Svěřil jsem se kamarádům a diskuze s nimi mě z toho trochu vytáhly. Taky pomohlo, že jsem měl pocit, že už mi odchází viróza uhnaná přes Vánoce a že je mi lépe. Taky jsem si záměrně pustil nějaké veselé písničky a překvapilo mě, že to mělo až nečekaný efekt. Chtěl jsem si najít nějaký nakopávací podcast, ale vlastně žádné byznysové neposlouchám, tak jediné, co jsem ve své podcastové appce našel, bylo tohle [shrnutí od kluků z Fakturoidu](https://overcast.fm/+ABFzW3OVK4I), ale účel to splnilo a namotivovalo mě to.

Rozhodl jsem se, že udělám VELKÉ PLÁNOVÁNÍ. Že si musím ujasnit, co je teď na junior.guru fakt úplně nejvíc nejdůležitější a bude mít největší dopad na jeho úspěch. A že mých 700 kartiček napůl v Trellu a napůl v Obsidianovém kanbanu není udržitelný způsob, jak si něco plánovat. Rozhodl jsem se přesypat kartičky do Markdown dokumentů v Obsidianu, které budou jen „rešeršemi“ na různá témata, bez priorit. Prostě nápady. A že konkrétní úkoly budou jiný druh záznamu, jinak organizovaný, než pouhé nápady 😀 A že vymažu všechno, co už není relevantní, protože takových věcí tam bylo mraky. Taky jsem našel na disku ještě nějaké staré složky a dokumenty a byla sranda to číst.

Během toho, jak jsem to postupně přesypával, tak jsem získával mnohem lepší představu o tom, co je vlastně jen „nápad“ a co je spíš „úkol“, který má nějakou důležitost a bylo by dobré jej v blízké době udělat. Taky bylo příjemné zjistit, že po promazání toho vlastně není vůbec tolik, kolik jsem myslel, a že hodně věcí je na junior.guru už hotových.

Objevil jsem rok starou nahrávku callu s Veronikou Jozifovou, kde se mnou sdílela závěry svojí studie o juniorech. Znova jsem si to celé pustil a přišlo mi, že to dnes už vidím v jiném světle a že mi to mnohem víc zapadá do ostatního jako dílek puzzle. Po roce stráveném s Terkou Palaščákovou nad novou prodejní stránkou, ale [ve skutečnosti nad mým celým byznysem](https://en.wikipedia.org/wiki/Business_model_canvas), už jsem prostě mnohem dál, než když jsem to slyšel poprvé.

Z krizičky jsem přešel do mánie. Nabitý energií a namotivovaný jsem se týden prohrabával úplně vším, co k junior.guru kde mám. Odebral jsem definitivně vše související s junior.guru z Notionu. Trello jsem [vyčistil a zavřel](https://mastodonczech.cz/@honzajavorek/113826307001004563), ale všechno čištění a plánování dokončené ještě nemám.

Prošel jsem si závěry dotazníků z minulého roku a nabilo mě to ještě víc. Objevil jsem tam zajímavé věci, kterých jsem si sám nevšiml, ale taky hromadu povzbuzení od lidí z klubu, kteří mi tam psali, jak je junior.guru super, jak to dělám dobře, a jak jim to pomohlo a změnilo život. To bylo opravdu hodně nakopávací, až mě to dojímalo.

Chtěl bych v dalším týdnu dodělat čištění a pak si vytvořit nějaký plán. Ten bych chtěl dělat s vědomím, že existují věci jako [Impact/Effort matice](https://www.youtube.com/watch?v=vMj_SQJgECw) nebo [Eisenhowerova matice](https://duckduckgo.com/?t=ffab&q=Eisenhowerova%20matice&ia=web).

![Sněhulák]({static}/images/img-3735.jpg)
Tenhle sněhulák s ničím nesouvisí, ale bylo mi líto ho do poznámek nedat, když mi dal tolik práce

## Návštěvnost

Koukal jsem po delší době na grafy. Něco se mi nezdálo. Nejsem v žádné vyloženě byznysové komunitě, spíš v ajťáckých, tvůrcovských, a tak, takže jsem se s tím šel poradit do Terčiny komunity, [Content Party](https://contentparty.substack.com/p/coming-soon).

Nadhodil jsem dotaz ohledně výpočtu konverzního poměru. Přišlo mi, že by tam mohl být kromě copywriterů i někdo víc byznysově založený. Povídáním si sám se sebou a následně i s členy komunity, hlavně [Erikem Lerchem](https://www.linkedin.com/in/erik-lerch), jsem došel k tomu, že konverzní poměr prodejní stránky je nadprůměrný a že změřený je správně. I data z dotazníků podporovala teorii, že prodejní stránka vlastně docela funguje, byť by na ní šlo vylepšit hromadu věcí. Jenže kde je tedy zakopaný pes?

Konverzní poměr trialu vypadal taky dobře. Takže jsem hledal, čím to je, že stejně do komunity nepřibývá nějak moc nových lidí. Že by mi tolik odcházeli staří členové a noví je nestíhali nahrazovat? No nakonec jsme se dobrali k tomu, že se stačí podívat na graf návštěvnosti a je to jasné.

![Návštěvnost]({static}/images/screenshot-2025-01-24-at-12-13-09.png){: .img-thumbnail }

Můžu mít konverzní poměr nejlepší na světě, ale když na tu prodejní stránku přijde málo lidí, tak do klubu prostě doputuje málo lidí. A já s hrůzou zjistil, že návštěvnost junior.guru oproti loňsku touto dobou klesla na polovinu.

Tohle zjištění mi udělalo neskutečnou radost a ještě víc mě namotivovalo. Samozřejmě nejsem rád, že mi lidi nechodí na web, ale najednou vidím jasný problém, který má nějaká více či méně jasná řešení. Už netápu ve tmě, ale znám problém a mohu začít dělat kroky, které mohou ten problém řešit!

Na grafu jde vidět, že v létě a září šla návštěvnost nahoru. Z té doby si pamatuju, že i čísla klubu stoupaly a měl jsem pocit, že se junior.guru odrazilo ode dna. Na tom jde vidět, že návštěvnost je zásadní a je opravdu asi tím největším problémem. Takže tím, co bych měl dělat v první řadě, je marketing, marketing, marketing.

## Apify

Tento týden jsem měl pracovat pro Apify. Ale moc mi to nešlo, protože mi do toho spadla spousta věcí, od rodinných záležitostí, přes návštěvu doktorky, terapeutky, setkávání se s bráchou, s rodiči, dva cally, až po psaní těchto nekonečných poznámek. Budu tedy přetahovat a příští týden jim věnuju ještě jeden nebo dva dny. Zatím jsem stihl:

- Projít veškerou komunikaci na PRs a issues z minula.
- Doladit a mergnout kapitoly z minula.
- Vytvořit [#1417](https://github.com/apify/apify-docs/issues/1417) a [#1418](https://github.com/apify/apify-docs/issues/1418)
- Kouknout na nový spelling, který máme na repozitáři skrze [Vale](https://vale.sh/).
- Dotáhnout třetí lekci o DevTools a dát [PR k review](https://github.com/apify/apify-docs/pull/1321).
- [Rozpracovat PR](https://github.com/apify/apify-docs/pull/1424) na poslední lekci kurzu o tom, jak scraper nasadit na Apify. V té je hodně částí, kde se má něco instalovat nebo registrovat, tak si to všechno zkouším, studuju to, a hrozně mi to trvá.

![Python Packaging]({static}/images/screenshot-2025-01-24-at-12-56-29-overview-of-python-packaging-python-packaging-user-guide.png)
Na tomto webu jsem strávil až příliš mnoho času

## Další věci na junior.guru

-   Publikovali jsme záznam z prosincové přednášky o AI asistentech. Upravil jsem rozměry a nahrál jsem [na YouTube kanálu](https://www.youtube.com/@juniordotguru) nové obrázky ke všem videím (záznamy přednášek nejsou většinou veřejné, tak nejdou vidět, ale je jich hodně). Dal jsem pár hodin průzkumu, zda by můj bot náhodou tohle nemohl dělat sám i pro přednášky, které teprve budou, když už ty obrázky generuje, ale bohužel. Na rozdíl od jiných Google služeb je u YouTube jen neprůstřelné OAuth, které musí mít interakci s uživatelem a Googlem ověřenou a schválenou appku a kdo ví co. Jak už to tak u API bývá, mohlo to být užitečné API, kdyby tam nedali auth, který z něj dělá zcela zbytečné a nepoužitelné API.
-   Aktualizoval jsem některé screenshoty na webu. Dělal jsem to jako [yak shaving](https://en.wiktionary.org/wiki/yak_shaving) při jiném úkolu. Až při tom mi došlo, že dělat screenshoty během Vánoc je úplná blbost, protože všechny weby jsou zasviněné nějakými křiklavými promo bannery.
-   Udělil jsem jedno stipendium.
-   Uvažoval jsem, na co bych já osobně využil EU dotace, které se rozdávají přes [jsemvkurzu.cz](http://jsemvkurzu.cz/). Má to v létě nebo kdy končit, tak bych si měl pospíšit. Nakonec jsem usoudil, že se nebudu prohrabávat nekonečnou nabídkou kurzů, ale vsadím na něco, kde znám lidi, kteří to organizují, a věřím kvalitě. Plánuju se registrovat k Havranovi na [Pravidla se změnila](https://www.pravidlasezmenila.cz/). Třeba mi to pomůže dělat efektivnější a kreativnější marketing. Třeba konečně na něco praktického využuju to svoje hraní s generováním AI obrázků.
-   Opravoval jsem scrapery, které se různě rozbíjely. Ať už kvůli [špatně napsanému URL](https://github.com/juniorguru/plucker/commit/82a2699a0c989a1b12bf34141464934954b10340), nebo kvůli tomu, že úřad práce změnil API, na kterém běží jeho katalog kurzů.
-   Objevil jsem [Buttondown](https://buttondown.com/) a asi jsem se zamiloval. Ještě jsem ten produkt neviděl, ale díky jejich copywritingu a skvělému webu i blogu mám pocit, že to strašně chci platit a používat 🤣 Už se třesu, až budu mít chvilku času, abych to zkusil propojit tady s blogem nebo s tím vytvořil junior.guru Newsletter. Vypadá to fakt dobře a za rozumnou cenu.
-   Měl jsem call s Terkou a probírali jsme marketing.
-   Měl jsem call s Miou a Arturem z organizace EuroPythonu, který letos [bude opět v Praze](https://ep2025.europython.eu/). Bavili jsme se o tom, co může konference udělat pro začátečníky. Uzavřeli jsme to tím, že je hodně věcí, které se dají udělat, a že hodně z nich udělám já 🤣 Tak se můžete těšit. Pokud se to schválí, možná bude na EP něco jako den pro juniory, a dokonce možná mimo standardní ceny lístků.
-   Přestal mi fungovat `stylelint --fix`, ale nějak jsem to vyřešil. Teď na mě chrlí už jen hromadu varování, takže asi dobrý.
-   Zajistil jsem si přístup do komunity Czechitas a na jejich nový Discord. Neměl jsem ale zatím čas to tam moc prozkoumat. Pokud tam jste, zamávejte mi.
-   Glance Media [hledají do týmu produktového specialistu](https://junior.guru/jobs/4054a4e651936559fc00f099e678defa5c30c7e0dc023ea93abb11b5/), tak jsme se dohodli na sponzorství. Umístil jsem inzerát, logo, zařídil předplatné, a poslal fakturu. Není to vyloženě programovací pozice, ale dřív byli spokojení s lidmi, kteří z junior.guru na jejich pracovní inzeráty chodili, tak jsme se domluvili, že to takhle uděláme znova.
-   Bývalá PyLady se mi ozvala s příležitostmi pro juniory v [NTK](https://www.techlib.cz/cs/), ale to jsem ještě nedotáhl a čeká to na mou odpověď.
-   Zkusil jsem ve [statusu na LinkedIn](https://www.linkedin.com/posts/honzajavorek_juniorguru-trello-obsidian-activity-7284888731398897666-ftn1) poprvé použít trik s „podpisem“.
-   Oprava nejrůznějších odkazů, které přestaly fungovat. Státní instituce se postupně stěhují na jednotnou doménu gov.cz a někdy nemají dobře udělané redirecty, tak se vždycky dovím, kdo migruje 😀 Posledně přestal fungovat odkaz na MVČR (junior.guru tam odkazuje na seznam kontaktů pro psychickou pomoc). Taky už definitivně zmizel web Green Fox Academy, tak jsem odkázal do web archivu.
-   Narazil jsem na [nodriver](https://github.com/ultrafunkamsterdam/nodriver), nějaký záhadný efektivní způsob jak scrapovat, ale zatím jsem neměl vůbec čas to víc prozkoumat.
-   Řešil jsem různé trable s přihlašováním lidí do klubu, nebo s účty.
-   Koupil jsem žluté post-ity a černou a modrou fixu. Mám s tím marketingové plány 😀
-   Při VELKÉM PLÁNOVÁNÍ jsem udělal zálohy některých dat.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Řešil jsem něco s [jakybylpohovor.cz](https://www.jakybylpohovor.cz/) a s Red Hatem, ale ani jedno jsem zatím nestačil dotáhnout.
-   Kamarádi z [CoreSkillu](https://coreskill.tech/) si už dál nebudou platit Nitro na Discordu, a tím pádem přijdu o jejich boosty pro klub. Pokud tyto boosty chci, budu je muset doplatit v rámci svého Nitra. Provoz klubu tedy stoupne o 70€ ročně. To je sice na prd, ale jsou i horší věci.

## Další věci v životě

-   Zažádal jsem si o nový řidičák. Přihlásil jsem se online přes nějakou tu identitu, odklikl jedno tlačítko, a bylo to hotové.
-   Objevil jsem v kavárnách matcha latté a zjistil, že mi chutná. Objednal jsem si domů čaje a [trpěl při tom](https://mastodonczech.cz/@honzajavorek/113855337609184938).
-   Nic netušící jsem si pustil [The Bear S02E06](https://www.csfd.cz/film/1184280-medved/1236872-ryby/recenze/). Asi nejlepší seriálovou epizodu, jakou jsem kdy viděl. Naprostá bomba jak v rámci kontextu seriálu, tak i samostatně. Vydýchávám. Čumím úžasem i nadšením, jak skvělé to bylo.
-   Dan Srb si pustil mou [Q&A na YouTube](https://www.youtube.com/watch?v=GkT0hRhykgk) a tak moc jsem se mu líbil, že u toho vytvořil [sticker set pro Telegram](https://t.me/addstickers/honzajavorek) s mýma hlavama.
-   Byl jsem v kině a v sauně.
-   Doplňoval jsem údaje pro sociálku. Mají [důchodovou aplikaci](https://eportal.cssz.cz/web/portal/informativni-duchodova-aplikace#/), kde se můžete podívat, co pro vaši osobu evidují. Jak [popsalo před časem Aktualne.cz](https://zpravy.aktualne.cz/finance/v-duchodove-kalkulacce-mi-chybi-cast-zamestnani-studium-i-vo/r~a18b7b2cedf511eb8a900cc47ab5f122/), často tam hodně věcí chybí a nezbývá, než to sociálce doložit, aby to správně započítali. Napsal jsem tedy do třech škol, kde jsem studoval, aby mi vystavili potvrzení o studiu, a tyto posílám na sociálku, aby to zaevidovali. Všechno řeším pouze dopisováním přes datovku a zatím jsem nenarazil na žádný problém, všichni byli nápomocní a milí.
-   Šel jsem si přes svátky zaběhat v mrazu a mlze, což bylo hrdinské, dokud to hrdinské nebylo. Oddělal jsem si ledovým vzduchem průdušky, uhnal na to virózu, a až tento týden se cítím docela zdravý. Kromě bolestí zad a kolem žeber po ránu, to ještě s doktorkou zkoumáme, ale snad to nějak zrehabilituju.
-   Za 36 dní jsem dohromady naběhal 10 km, při procházkách nachodil 3 km. Celkem jsem se hýbal 3 h a zdolal při tom 13 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Dokončit práci pro Apify.
2.  Dokončit VELKÉ PLÁNOVÁNÍ.
3.  Projít všechny maily, zprávy na Discordu a ostatní věci, které na mě čekají.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [I Met Paul Graham Once - Phill MV](http://okayfail.com/2025/i-met-pg-once.html)<br>Doporučuju přečíst do konce, je tam zajímavý plot twist.
- [Are better models better? - Benedict Evans](https://www.ben-evans.com/benedictevans/2025/1/the-problem-with-better-models)<br>„If I need something that does have answers that can be definitely wrong in important ways, and where I’m not an expert in the subject, or don’t have all the underlying data memorised and would have to repeat all the work myself to check it, then today, I can’t use an LLM for that at all.“ „…we adopted a device that breaks if you drop it with a battery that lasts a day instead of a week, in exchange for something new that came with that.“
- [Video: Become a Wikipedian in 30 minutes](https://blog.mollywhite.net/become-a-wikipedian-transcript/)<br>Jak začít editovat Wikipedii. Pěkný návod do startu od Molly White. Nebojme se toho!
- [Šest týdnů inkognito v hlubinách českého Discordu – Page Not Found](https://pagenotfound.cz/clanek/sest-tydnu-inkognito-v-hlubinach-ceskeho-discordu)<br>Šílený. Nemám co dodat.
- [A good publishing workflow is an escape hatch](https://buttondown.com/blog/good-publishing-workflows)<br>Tenhle přístup k publikaci a propagaci se mnou hodně rezonuje.
- [Demokracie má velký problém, na který volby nestačí, říká Yuval Noah Harari - Deník N](https://denikn.cz/1615227/nemeli-bychom-se-bat-terminatoru-ale-ai-byrokratu-rika-historik-harari/)<br>„Většina informací není pravda. Většina je odpad.“ „Najít pravdu je nákladné. Chcete-li napsat fiktivní příběh o Římské říši, je to snadné. Napíšete to první, co vás napadne. Fakta ověřovat nemusíte. Nemusíte znát latinu, řečtinu, hledat střepy keramiky a snažit se vyložit, co znamenají.“ „Abyste lidi kolektivně motivovali, potřebujete příběh, mytologii, ideologii. A když dojde na budování mytologie, která lidi nadchne, nejsou už fakta tak zásadní.“
- [12 Famous Fairytale Princesses, And The Real Stories, Folktales, And Actual History That Inspired Them](https://www.bustle.com/p/12-famous-fairytale-princesses-the-real-stories-folktales-actual-history-that-inspired-them-8554483)<br>Z jakých původních pohádek nebo dokonce historických osobností vychází Disneyovské princezny. Musim teda říct, že Pocahontas, nebo Ariel jsou docela maso. Šípková Růženka mě tolik nešokovala, to už jsem někde četl dřív.
- [Zúčtování s rokem 2024 a nahlížení do politiky verze 50 | Marigold.cz - Sítě a Technologie](https://www.marigold.cz/item/osobni-politicke-ohlednuti-2025/)<br>„Vzájemná politická konkurence a obchodní zájmy jsou důležitější, než posun republiky kupředu. Upřednostnit republiku znamená zmařit své politické šance na znovuzvolení.“
- [Death Of A Forum: How The UK’s Online Safety Act Is Killing Communities | Techdirt](https://www.techdirt.com/2024/12/20/death-of-a-forum-how-the-uks-online-safety-act-is-killing-communities/)<br>„When you regulate the internet as if it’s all just Facebook, all that will be left is Facebook.“ „The promise of the internet was supposed to be that it allowed anyone to set up whatever they wanted online, whether it’s a blog or a small forum. The UK has decided that the only forums that should remain online are those run by the largest companies in the world.“
- [Stop Trying To Schedule A Call With Me](https://matduggan.com/stop-trying-to-schedule-a-call-with-me/)<br>U tohoto jsem se hodně dobře bavil, ale pokud jste někdy byli na jedné nebo druhé straně sales procesu, asi bych sem měl připsat trigger warning nebo něco 😅 Pro vás to bude jako sledování videí od KRAZAM, chcete se smát, ale místo toho vám vyhrknou opravdové slzy a jdete si domluvit další sezení na terapii.
- [Python is the new BASIC](https://log.schemescape.com/posts/programming-languages/python-as-a-modern-basic.html)<br>Mise splněna, můžeme rozpustit naši neziskovku 😀
- [Borecký: Proč jezdíme v příměstských vlacích PID jako sardinky a proč situace potrvá do roku 2029 - Zdopravy.cz](https://zdopravy.cz/borecky-proc-jezdime-v-primestskych-vlacich-pid-jako-sardinky-a-proc-situace-potrva-do-roku-2029-232899/)<br>„…zatímco před 20 lety jste se z Kolína do Prahy dostali pod hodinu, dnes po mnohamiliardových investicích se dojezdová doba prodloužila skoro o 20 minut.“ „Pokud tedy někdo chcete ode mně nějakou časovou osu, kdy 'bude líp', tak to vypadá zhruba takto: březen 2025 – prosinec 2025 – prosinec 2029 (tohle datum se ale může posunout).“
- [Generace Z: Volby srdcem, ministerstvo péče a jiná pošetilá přání – Page Not Found](https://pagenotfound.cz/clanek/generace-z-volby-srdcem-ministerstvo-pece-a-jina-posetila-prani)<br>„Potřebuju asi něco jako ministerstvo péče. Někoho, kdo nám připomene, že na všech záleží. Na všech.“ V článku odkázaný výukový materiál konkrétních základních škol o rasách je fakt síla, to si dejte.
- [Reckoning: Frontend&#39;s Lost Decade | Alex Russell | performance.now() 2024 - YouTube](https://www.youtube.com/watch?app=desktop&v=0XwWVjQOmyg)<br>Proč web prohrává na mobilu a co se s tím dá dělat. Krásně vysvětleno a podáno. A pokud děláte frontend, nejspíš se vám nebude líbit závěr, nebo vám minimálně rozbije hračky.
- [(bez titulku)](https://pod.geraspora.de/posts/17342163)<br>„Summing up the top UA groups, it looks like my server is doing 70% of all its work for these fucking LLM training bots that don’t to anything except for crawling the fucking internet over and over again.“
- [Build libraries, not vaults: minimizing private channels in Slack &amp; Teams &#8211; More Than Coding](https://morethancoding.com/2024/12/10/build-libraries-not-vaults-minimizing-private-channels-in-slack-teams/)<br>Princip, který se odjakživa snažím prosazovat ve všech komunitách, kde jsem členem: „Hidden information sources like private channels and direct messages (DMs) are commonly used in collaboration tools like Slack and Teams. They are necessary for safely discussing some subjects, like personnel situations or sensitive topics. However, using them pervasively is an anti-pattern. Organizations work more effectively if information is open and accessible.“
- [Does current AI represent a dead end? | BCS](https://www.bcs.org/articles-opinion-and-research/does-current-ai-represent-a-dead-end/)<br>„A correct output on a test of a stochastic system only evidences that the system has the capability to respond correctly to this input, but not that it will do this always or frequently enough.“ „So, whole system testing is the only verification tool available, but it can never represent more than a drop in the ocean.“
- [ELIZA - Wikipedia](https://en.wikipedia.org/wiki/ELIZA)<br>„While ELIZA was capable of engaging in discourse, it could not converse with true understanding.However, many early users were convinced of ELIZA's intelligence and understanding, despite Weizenbaum's insistence to the contrary.“
- [Ed Zitron - Why Are All Tech Products Now Shit? - YouTube](https://www.youtube.com/watch?v=7Slib2bbMs4)<br>Dobrá smršť 😀
- [Master Flaky Systems With Retries in Python 🐍 (avoid self-DDoS) - YouTube](https://www.youtube.com/watch?v=BxikFuvaT1Y)<br>Všechno o důležitosti a rizicích retries
- [Major Pitfalls of Self Development](https://vesecky-adam.medium.com/major-pitfalls-of-self-development-50c470ee0bf2)<br>„Time spent can never be reclaimed or refilled. The work will always be there and it will never end, but your life will. And at the end of the day, the most mature thing any of us can ever do is to live a life to remember.“
- [Seznam nejvyšších věží v Česku – Wikipedie](https://cs.wikipedia.org/wiki/Seznam_nejvy%C5%A1%C5%A1%C3%ADch_v%C4%9B%C5%BE%C3%AD_v_%C4%8Cesku)<br>Věž brněnského Jakuba je o 8m vyšší než katedrála na Petrově. Dóm v Olomouci je vyšší než vysílač na Ještědu i než katedrála na Pražském hradě.
- [Mapy.cz mají předplatné, ale Seznam už mě naučil používat něco jiného &#8211; Sesivany&#039;s blog](https://blog.eischmann.cz/2025/01/01/mapy-cz-maji-predplatne-ale-seznam-uz-me-naucil-pouzivat-neco-jineho/)<br>Zaplatit za Mapy od Seznamu, nebo přejít jinam? Nevím. Ale tohle je kdyžtak dobrá inspirace.
- [Milion plus](https://smichovreviewofcities.substack.com/p/milion-plus)<br>Kolik máme parkovacích míst. Ručně spočítáno.
- [Things we learned about LLMs in 2024](https://simonwillison.net/2024/Dec/31/llms-in-2024/)<br>„The default LLM chat UI is like taking brand new computer users, dropping them into a Linux terminal and expecting them to figure it all out.“ „The key skill in getting the most out of LLMs is learning to work with tech that is both inherently unreliable and incredibly powerful at the same time. This is a decidedly non-obvious skill to acquire!“
- [What Is Your Dream for Mozilla?](https://mozillafoundation.tfaforms.net/100)<br>Tady má Mozilla (taková ta organizace, která vyrábí třeba Firefox) anketu, kde můžete vyplnit, co byste si přáli, aby dělala a na co aby se zaměřovala. Já vyplnil!
