Title: Týdenní poznámky: Servis a automatizace
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/308
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111902348217446405

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-02-02_tydenni-poznamky-pracovni-inzeraty-pres-ai.md) už utekl nějaký ten týden (2. 2. až 9. 2.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q1 2024]({filename}2024-01-25_plan-na-q1-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)
</div>

Po úspěchu se zapojením AI do třídění nabídek práce jsem si naplánoval týden, během kterého si odpočinu od intenzivního budování a kdy se budu věnovat servisní práci a automatizaci.
Tak se i stalo.
Příští týden bych se chtěl pustit zase do něčeho většího.

## Servisní zásahy

-   Opravil jsem několik rozbitých odkazů na webu (díky Nelo!),
-   vyčistil jsem z kódu definitivně veškerou podporu pro posílání studentů vzdělávacích agentur do klubu (díky Dane!),
-   [vyzrál jsem nad LinkedIn](https://github.com/juniorguru/junior.guru/commit/92e4126799c7a3920f789291f39f143f5606a7a3) a opravil automatické [sledování počtu followerů](https://junior.guru/open/#socialni-site-a-newsletter) na svém osobním LinkedIn účtu,
-   opravil jsem adresy obrázků na webu (v některých případech se špatně uváděla adresa na [Cloudinary](https://cloudinary.com/), díky Karolino!),
-   zrychlil jsem přes keš skript, který si stahuje ze [Simple Analics](https://simpleanalytics.com/junior.guru) data o návštěvnosti webu,
-   archivoval jsem [projekty na GitHubu](https://github.com/orgs/juniorguru/projects), které tam zůstaly po mých loňských plánech,
-   konečně jsem opravil [čísla v příručce](https://junior.guru/handbook/interview/#prace-na-ico) o limitech na DPH (díky všichni v klubu a díky Dane, že jsi to ještě [vylepšil](https://github.com/juniorguru/junior.guru/pull/1300)),
-   odepsal jsem na e-mail z listopadu, který se týkal spolupráce s JetBrains,
-   přidal jsem do [katalogu](https://junior.guru/courses/) JetBrains Academy,
-   aktualizoval jsem na celém webu screenshoty,
-   automatizoval jsem [noční buildy Apify actorů](https://github.com/juniorguru/plucker/issues/7) na repozitáři se scrapery a zdokumentoval to v README,
-   vyrobil jsem [primitivní monitoring Apify actorů](https://github.com/juniorguru/plucker/issues/17) v repozitáři se scrapery a zdokumentoval to v README,
-   pohrál jsem si poprvé v životě pořádně s [cookiecutterem](https://cookiecutter.readthedocs.io/) a vytvořil jsem [šablonu, ze které mohu rychle vyrobit nový scraper](https://github.com/juniorguru/plucker/issues/8), čímž se dost zkrátilo to README a zmenšil opruz při vytváření (bylo to celé mnohem jednodušší, než jsem čekal, a cookiecutter se mi moc líbí!),
-   odstranil jsem štítek NOVÉ z [inzerátů práce na webu](https://junior.guru/jobs/), protože byl teď s novými daty všude a nemyslím si, že tuto funkcionalitu teď potřebuju,
-   automatizoval jsem upozorňování na Pondělní povídání v klubu (díky Milku, že jsi to doteď dělal ručně!),
-   sepsal jsem klubový tip (dokumentaci) o tom, co je Pondělní povídání (díky Milku, že to organizuješ!),
-   automatizoval jsem zakládání nových vláken v Týdenním plánování v klubu (díky Milku, že jsi to doteď dělal ručně!),
-   přemýšlel jsem, jak vylepšit mentoring v klubu a v souvislosti s tím jsem napsal všem aktuálním mentorům, předestřel jim své nápady a píšu si s nimi, jak to vnímaji oni,
-   přidal jsem nové štítky do klubového fóra, které slouží k tvoření skupinek.

## Výběr témat klubových přednášek

Nejdřív jsem se lidí v klubu zeptal, jaká témata by se jim líbila.
Otevřená otázka.
Objevily se zajímavé tipy.

Pak jsem to smíchal se seznamem svých nápadů a tipů a dal do klubu k hlasování.
To bude asi ještě probíhat, zatím to není vyhodnocené, ale lidi poctivě hlasují a to mi dělá radost.

Tento způsob se zdá lepší, než dělat dramaturgii zcela sám.
Některé mé nápady mají hodně hlasů, některé ale úplně propadly.
A na některá témata bych sám asi vůbec nepřišel.
Možná bude problém na některá sehnat přednášející, ale s tím se nějak snad poperu.

Výsledky hlasování nebudu brát jako zákon, nechám si právo veta a nikdy samozřejmě ani nevím, co a koho se mi povede domluvit.
Už teď je to ale hodně dobré vodítko.

## Dobrodružství s e-mailem

Už delší dobu přemýšlím, jestli chci mít e-mail (a kalendáře a kontakty) na Gmailu, u Googlu.
Jako první krok jsem se rozhodl rozpojit uživatelské rozhraní a server, který se mi stará o e-maily, abych pak mohl snáz vyměnit ten server.

Pokud bych mohl používat Apple Mail, který mám přímo v OS, tak by můj život byl jednodušší, takže jsem to zkusil.
No, je to hrozné.
A na iOS to bylo ještě horší.

Koho by to zajímalo nějak víc, tak jsem si [odfrkával na Mastodon](https://mastodonczech.cz/@honzajavorek/), tady to nechci úplně plevelit svými pocity a potřebami okolo e-mailu.
Taky jsem zjistil, že [ImprovMX](https://improvmx.com/), můj vymakaný způsob, jak mít jednu e-mailovou schránku, ale několik domén, možná není kompatibilní s ničím jiným, než s Gmailem 😀
Ale to ještě uvidím.

Každopádně díky celému tomuto cvičení mě napadlo, že mobilní appku možná vůbec nepotřebuji a odinstaloval jsem ji.
Prostě si e-maily na telefonu vůbec nemám teď jak otevřít.
Je to jen takový experiment.
Během jednotek dní nenastala situace, kdy by mi to chybělo, ale dovedu si představit, že při cestování apod. už to bude nepraktické.

Na co jsem se díval, nebo se na to chci ještě podívat: [Hey](https://www.hey.com/), [Proton](https://proton.me/), [Airmail](https://airmailapp.com/), [Spark](https://sparkmailapp.com/), [Fastmail](https://www.fastmail.com/), [StartMail](https://www.startmail.com/)

## Další

-   Bude [PyCon NA](https://na.pycon.org/), takže jsem jim, jako každoročně, přispěl.
    Letos si nemusím „jakože“ kupovat lístek, ale lze přímo poslat jen peníze přes tzv. _Supporter donation_.
    Každých 500 korun, které jim pošlete, jim umožní vzít na konferenci jednoho člověka, který by si to nemohl dovolit.
-   Zašel jsem s kamarády do [nejlepšího kina](https://kinoaero.cz/) na [Poor Things](https://www.csfd.cz/film/1002404-chudacci/prehled/).
    Nic takového jsem nikdy ještě neviděl.
    A už dlouho jsem neviděl něco tak dobrého.
    Strašně mě to bavilo!
    Po řadě plitkých Netflixových seriálů jsem strašně potřeboval něco artovějšího, takže tohle mi asi fakt sedlo.
    Žena na tom byla v kině o týden dřív a taky se jí to moc líbilo, takže určitě prozkoumáme i další Lanthimosovy filmy.
-   Byl jsem s dcerou v knihovně na [Zimních deskohrátkách](https://www.mlp.cz/cz/akce/e26674-zimni-deskohratky/) a bylo to super, i s dvouleťákem.
-   Naplánoval jsem si nějaká obědová a kafíčková setkání s kamarády.
    Dvě setkání vyšly, dvě odpadly.
-   Rozhodl jsem se, že nebudu spolupracovat s ENGETO na videích k něčemu, co připravují, abych se mohl soustředit na svůj produkt.
    Dal jsem jim ale nějaké tipy na lidi, kteří by jim s tím mohli pomoci.
-   Napsal jsem jménem [Pyvce](https://pyvec.org/) advokátce, aby nám aktualizovala stanovy a poslala je na úřady.
-   Ozvali se mi [IT people](https://www.itpeoplecz.cz/) s článkem sepsaným na základě [rozhovoru na zahajovací akci TDČ]({filename}2023-11-27_tyden-pro-digitalni-cesko-z-pohledu-partnera.md).
    Přečetl jsem jej a udělal nějakou minimální editaci.
    Ptali se mě, jestli pro ně nechci nějak víc přispívat.
    Odepsal jsem, že na to nemám kapacitu, ale nakonec jsme se domluvili, že bych se mohl, pokud by zrovna potřebovali, k něčemu i jen „vyjádřit“ a oni by to pak mohli přepsat a použít.
-   Přemýšlel jsem nad novým ceníkem pro firmy.
-   Potřebuju opravit myčku, která na nás bliká a pípá, ale umývat se jí nic nechce.
-   Napsal jsem na blog o tom, [jak mít sociální sítě a nepoužívat je]({filename}2024-02-04_jak-mit-socialni-site-a-nepouzivat-je.md).
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 8 dní jsem se nevěnoval žádné sportovní aktivitě.

## Plánuji

1.  Napíšu statusy na LinkedIn o podcastu a PyCon NA.
2.  Přidám podporu pro slovenštinu do třídění inzerátů.
3.  Přidám nové zdroje inzerátů (případně rozšířím jeden stávající).
4.  Budu dál vybírat klubové přednášky na rok 2024.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [TikTok Extends the Wasteland](https://hedgehogreview.com/issues/theological-variations/articles/tiktok-extends-the-wasteland)<br>„…we see same dynamic The Real World kicked off in 1992: ordinary people presenting their lives as entertainment, hoping for exposure. If lucky, they can rack up followers, becoming more than just a viral fad… TV isn’t legacy media, but entertainment as ideology—way of understanding the world through televised means… Televised performance has become the most accessible way to participate in public discourse… To be considered worthwhile, ideas must first entertain.“
- [kitze 🚀 (@thekitze) on X](https://twitter.com/thekitze/status/1754189182992253156)<br>Zatím mi přijde, že Apple Vision Pro dopadne jako Segway. Věc, která vypadá fakt hustě, ale lidi nepřijdou na to, pro jaké úkoly je to i praktické. Nicméně ať už to dopadne jakkoliv, tohle demo vypadá fakt hustě! 😀
- [Jak omylem rozdělit společnost](https://fajfka.cz/bubliny/)<br>Jak v několika nevinných a logických krocích vytvořit bubliny a omylem rozdělit společnost. Vysvětleno polopatě.
- [S vůlí úřadů bojujeme, říká ředitel Digitální a informační agentury. Chybí motivace sdílet data](https://www.irozhlas.cz/zpravy-domov/s-vuli-uradu-bojujeme-rika-reditel-digitalni-a-informacni-agentury-chybi_2401211840_hof)<br>„Ve státní správě je jeden z velkých problémů, že se všichni bojí kvůli kontrolním mechanismům. Nad všemi neustále visí Damoklův meč, že je třeba případně zavřou za nějaké pochybení. Ale je tam absence cukru, máme jenom ten bič. Já chápu touhu po odpovědnosti, ale to musí ruku v ruce jít s perspektivou něčeho pozitivního.“
- [Vyděšení čeští rodiče už děti nepouštějí ani 200 metrů od domova](https://www.seznamzpravy.cz/clanek/fakta-cesti-rodice-se-dnes-o-deti-boji-tak-az-jim-vzali-svobodu-231552)<br>„Za tři generace se podíl dětí ve věku 8 až 10 let, které se aspoň jednou dostaly bez doprovodu dospělých dál než kilometr od domu, smrskl z 80 na 27 procent.“ „Za posledních dvacet let se podíl dětí, které se do školy dopravují s rodiči autem, zvýšil čtyřnásobně.“
- [Systém z dob děrných štítků. Důchody v Česku zpracovává program z 50. let](https://www.seznamzpravy.cz/clanek/domaci-zivot-v-cesku-system-z-dob-dernych-stitku-duchody-v-cesku-zpracovava-program-z-50-let-231952)<br>„Od 90. let do roku 2014 jsem školil několik stovek COBOL programátorů nejenom pro českou správu důchodů, ale i pro slovenskou, pro české i slovenské pobočky zahraničních bank, slovenskou energetiku, pro celostátní evidenci hospodářských zvířat, pro mezinárodní koncern Glavunion, který po Evropě dodává skla do aut, a kromě řady dalších také opakovaně pro firmu, která zajišťovala IT provoz Frankfurtské burzy.“
- [Obrázky a paragrafy: moje zkušenost s PicRights](https://www.vzhurudolu.cz/prirucka/picrights)<br>Vymáhání práv za použité obrázky. Hustý. Já mám blog s archivem do roku 2007, tak jsem zvědav, kolik mi toho přijde 🙈
- [The end of 0% interest rates: what the new normal means for software engineers](https://newsletter.pragmaticengineer.com/p/zirp-software-engineers)<br>Po dekádě nulových úrokových sazeb přichází zima. Smete to startupy, juniory, a spoustu dalšího. Kdo bude připraven a vhodně se adaptuje na nové podmínky, přežije.
- [Google Search officially retires cache link](https://searchengineland.com/google-search-officially-retires-cache-link-437122)<br>Zendulka zvítězil. Důvod, proč si mě tehdejší děkan FIT VUT zavolal na kobereček, po 14 letech konečně zmizí. Google Cache končí!
