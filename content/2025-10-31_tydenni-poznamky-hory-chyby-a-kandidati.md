Title: Týdenní poznámky: Hory, chyby a kandidáti
Image: images/photo-2025-10-31-15-41-42.jpeg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-10-24_tydenni-poznamky-zive-nataceni-podcastu-podvocasem-posledni-pripravy-newsletteru-a-inzeraty-z-li.md) už utekl nějaký ten týden (24. 10. až 31. 10.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![já a sova]({static}/images/photo-2025-10-31-15-41-42.jpeg)
Fotil Martin Bakeš

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

V sobotu jsme odjeli do Orlických hor a byli tam až do úterý. Pak jsme přejeli k babičce ke Zlínu, odkud pracujeme na dálku a odpočíváme od velkoměsta. Hory byly hromadná akce s našimi kamarády a jejich dětmi, a byly strašně super, i když nám ten víkend celý propršel. Teď ty další dny se dokonce objevilo sluníčko, tak jsme si nakonec užili pěkný barevný podzim.

![muchomůrka]({static}/images/photo-2025-10-31-15-42-30.jpeg)

![Čenkovice]({static}/images/photo-2025-10-31-15-41-25.jpeg)

## Discord bot a zájmové skupinky

V klubu se strhla debata o tom, jak by šlo vylepšit aktuální fungování zájmových skupinek. Bot přidává nové lidi do skupinek, ale kvůli omezením Discordu to nelze udělat tak, aby při tom ostatním neoznačil vlákno jako nepřečtené. Takže tam je zbytečný spam o tom, že se přidali noví lidé a zbytečně to oživuje vlákna, kde se nic neděje. V debatě jsme dospěli k následujícímu:

- Přidávání by se přesunulo do „rychlého kuřete“ a dělo by se v reálném čase, a to pouze tehdy, pokud by někdo něco napsal do vlákna a tedy by jej tím oživil a dal by tam obsah, na který se ostatní stejně budou chtít podívat.
- Bot by mohl přidávat lidi přes silent mention na roli a pak svou zprávu smazat. To také označí kanál jako nepřečtený, ale v kombinaci s předchozím by to nemělo vadit. Když někdo určité vlákno odsleduje, Discord jej znova nepřidá, takže tato funkčnost by měla být zachována.
- Soukromé zprávy o tom, že bot někoho někam přidává, by zůstaly.

Výše uvedené jsem nenaprogramoval, ale do budoucna se k tomu snad brzy dostanu a mám skvělý pocit z toho, že řešení existuje a že jsme to v klubu takhle hezky společně vymysleli.

Dostal jsem v klubu před odjezdem na hory feedback na [dokumentaci bota](https://junior.guru/about/bot/), tak jsem to pak po příjezdu ještě popřeházel a vylepšil. Když jsem byl u toho, napadlo mě přidat do bota _slash command_, který by vrátil odkaz na tu stránku.

Nikdy jsem _slash command_ nedělal. Působilo to jednoduše, ale pak jsem se jako obvykle zamotal v nějakých OAuth srajdách a jiných _permissions_, takže jsem v tom pár hodin utopil, ale nakonec se to povedlo. Když teď v klubu někdo napíše `/help`, tak bot vrátí odkaz na dokumentaci!

Kdo ví, co dalšího zajímavého by bot tímto způsobem mohl dělat, že…?

![Help!]({static}/images/screenshot-2025-10-31-at-16-26-27.png)

## Chyby

Před odjezdem na hory se mi povedlo ještě opravit ten LinkedIn. Ale když jsem se vrátil z hor, sypaly se na mě jen samé chyby. Každá souvisela s něčím úplně jiným. Nová data, která tečou z LinkedInu, proklepla všechny možné hraniční případy v kódu, takže jsem asi na pěti místech musel přidávat nová ošetření, nebo podmínky.

Třeba že [weby mají favicon jako BMP](https://mastodonczech.cz/@honzajavorek/115456794522147200) nebo GIF… Nebo že někdy z LinkedInu přijdou odkazy ve tvaru bez počátečního `https://`. Nebo mi API z Mapy.cz vrátilo nějakou slovenskou adresu v okrese Pezinok v neočekávané struktuře. Nebo se mi zamotával scraper, který stahuje loga firem u pracovních inzerátů. Pak jsem pro změnu narazil na [bug v Apify](https://github.com/apify/apify-sdk-python/issues/655). Po celém dni opravování jsem objevoval další a další a bylo to poměrně frustrující. Naštěstí máme v klubu kanál #past-vedle-pasti, kam jsem si mohl postěžovat.

![CI padá, něco si přej]({static}/images/screenshot-2025-10-30-at-16-13-06.jpg)

## uv

Když jsem sáhl na nějaký projekt, neodolal jsem tomu, abych jej převedl z `poetry` na `uv`. Už jsem to dělal několikrát, takže to mám celkem v oku a daří se mi to dělat rychle. Proto se do toho taky směle pouštím, i když mám zrovna dělat něco jiného. Ale zatímco [eggtray](https://github.com/juniorguru/eggtray) bylo hned, tak [chick](https://github.com/juniorguru/chick) se roztáhlo na několik hodin.

Přestal mi na Fly fungovat Dockerfile, tak jsem hledal, jak použít `python:3.13-slim-bookworm`, mít tam `uv`, a zároveň i `git`, protože tam mám git závislosti. A potom mi na GitHub Actions neprocházely testy, zatímco lokálně ano. Vůbec jsem to nechápal. Podle všeho se na CI vytvořilo zcela totožné prostředí, byla tam stejná souborová struktura, atd., ale přesto se nedařilo importovat některé věci. Kontroloval jsem nastavení pytestu a všeho možného, konzultoval chybu s AI asistenty, ale nic.

Až jsem si všiml, že ve VS Code jsou některé soubory šedé a ne bílé. Přesunem kódu do složky `src` se totiž změnil způsob, jakým se aplikoval `.gitignore`. Byla v něm jedna zrada a při té změně cesty mi začal ignorovat celou složku `lib`. Toho jsem si nevšiml a takto to commitnul. Takže ty soubory byly na mém disku, ale vůbec nebyly v Gitu, a samozřejmě ani na GitHubu!

## Kandidáti

Při pátečku se mi většinou už nechce rozjíždět velké věci, ale tentokrát jsem si řekl, že takhle bych ty kolečka kapitalismu nikdy neroztočil, a že je potřeba taky někdy přitlačit, zvlášť když jsem čerstvý po dovolené a motivovaný přinášet hodnotu po dni stráveném opravováním chyb.

Cílem pro tento podzim je oživit a rozjet [seznam kandidátů](https://junior.guru/candidates/), o kterém mluvím už fakt dlouho a který má potenciál podpořit růst junior.guru. Je to teď nejzásadnější věc a jestli ani ta s klesajícími trendy nehne, tak už nevím, co budu dělat.

Začal jsem tím, že jsem si stránku otevřel a přemýšlel nad tím, jak by měl ten frontend vypadat. A i když jsem měl v hlavě odjakživa představu, že to budou nějaké profilové boxíky s ksichtíky, tak najednou mi přišlo, že by nemusela být úplná blbost to udělat úplně stejně, jako jsou udělané pracovní inzeráty. Akorát místo inzerátů by tam byli lidi.

Tak jsem na tom začal makat a za půlku pátku jsem se díky znovupoužití spousty věcí [dostal dost daleko](https://github.com/juniorguru/junior.guru/pull/1590). Když už jsem se vrtal v tomhle, tak jsem taky konečně opravil zobrazování lokace, které bylo od posledního překopání inzerátů dvojitě a i všelijak jinak špatně.

![Kandidáti]({static}/images/screenshot-2025-10-31-at-15-10-53.png){: .img-thumbnail }
Rozpracovaná verze seznamu kandidátů

## Další

-   Ve volném čase občas hraju [0 A.D.](https://play0ad.com/), ale teď mě to nějak omrzelo a chtěl jsem nějakou arkádovější srandu. Našel jsem [SuperTuxKart](https://supertuxkart.net/) a je to super! 😎
-   [Zkoušel jsem CodeRabbit](https://mastodonczech.cz/@honzajavorek/115468449933384922), ale zatím nic moc.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. Po příjezdu z hor byla nálož různé komunikace, kterou by bylo radno projít, docela velká, ale prokousal jsem se tím.
-   Stále pracujeme na novém bydlení. Vypadá to zatím, že to je na dobré cestě.
-   Za 8 dní jsem naběhal 5 km, při procházkách nachodil 2 km, na túrách nachodil 26 km. Celkem jsem se hýbal 10 h a zdolal při tom 33 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Odešlu newsletter!
2.  Budu pokračovat ve tvoření seznamu kandidátů.
3.  Zajdu na očkování, terapii, ke kadeřníkovi, na lampionový průvod, a zavolám si s Terezou.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Free software scares normal people—Daniel De Laney](http://danieldelaney.net/normal/)<br>Amen.
- [uv is the best thing to happen to the Python ecosystem in a decade - Blog - Dr. Emily L. Hunt](https://emily.space/posts/251023-uv)<br>Pokud ještě nepoužíváte uv…
- [Engeto míří do USA s platformou Nuomy. Systém, který mění způsob vzdělávání pomocí umělé inteligence | Hospodářské noviny (HN.cz)](https://benative.hn.cz/c1-67805620-engeto-miri-do-usa-s-platformou-nuomy-system-ktery-meni-zpusob-vzdelavani-pomoci-umele-inteligence)<br>Jsem zvědav, jestli tohle je budoucnost učení. Od knih a lektorů před tabulí se většina lidí už dávno přesunula na YouTube. Je možné, že dalším krokem bude na míru vygenerovaný AI učitel?
- [Blog N: Mýty ministra Migaľa: „Dostaneme zdrojové kódy, nebudú nás vydierať“ &mdash; Denník N](https://dennikn.sk/blog/4934481/myty-ministra-migala-dostaneme-zdrojove-kody-nebudu-nas-vydierat/)<br>Husté. Na Slovensku už dávno mají být projekty pro stát pod otevřenou licencí. Jenže to ve výsledku vůbec nic neznamená.
