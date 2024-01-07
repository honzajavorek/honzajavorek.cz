Title: Týdenní poznámky: Vánoce
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/301
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111705252534378818

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-12-22_tydenni-poznamky-dalsi-nemoci-anglictina-a-pruzkum-apify.md) už utekl nějaký ten týden (22. 12. až 5. 1.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)
</div>

Pozitivní informace hned na začátek: Přes Vánoce jsem byl zdravý!
Odjeli jsme k babičce a tam jsem měl možnost zrelaxovat.
Odpočinul jsem si od práce i všech dalších povinností.
Myslím, že mi to prospělo a po svátcích jsem se vrátil do života o něco silnější.
Taky jsem měl sílu a čas udělat si pár přemýšlecích procházek po polích a lesech.

## Plány na 2024

Přes svátky jsem hodně přemýšlel.
Jak o životě, tak o práci, o junior.guru a jeho směřování, o rozbitém pracovním trhu, AI, o klesajících grafech, o mém psychickém zdraví, stresu, atd.

Koukám na grafy na junior.guru a jsem z nich smutný.
Pamatuju si, jak počet členů v klubu útočil na 500.
Teď je jich 371.
Nejhorší na těch grafech ale stejně je, že zase vidím chyby v jejich implementaci, přitom jejich přepsání mi vloni zabralo tolik úsilí a času.
Já je snad úplně smažu nebo co.
Aspoň mě nebudou stresovat.

Ale zpět k věci.
Z nějakého toho přemýšlení a rozjímání jsem si už udělal závěry, něco je asi na delší trať.
Každopádně mám krátký odrážkový seznam věcí, které bych chtěl na junior.guru udělat ve Q1.
Od loňska jsem se poučil, že rozhodně nemám plánovat na rok dopředu, a že i půlrok je nějak příliš.
Takže čtvrtletí.

Zatím to sem ale nepíšu, protože nad tím jednak ještě trochu přemýšlím, jednak to bude přece jenom lepší do separátního článku, ať nejsou tyto poznámky zbytečně dlouhé.

## Studie

Přes Vánoce jsme domluvili termín callu, na kterém se dovím já a můj tým z junior.guru (moderátoři) závěry studie mezi career switchery.
Pak jsme si ještě ujasnili okruhy, které nás zajímají nejvíc.

Call jsme měli dnes večer a bylo to výživné.
Určitě nelituju vynaložených prostředků a času.
Nebylo to nic pecka objevného, mnoho z těch věcí ze své praxe v klubu známe, ale bylo to z jiného úhlu pohledu, v jiném rámci, nějak uspořádáno a vyloženo.
Mnoho ze zmíněných věcí do junior.guru půjde nějak zakomponovat.
Mnoho z nich mám někde jako zapadlou kartičku v Trellu, ale nový pohled tomu může dát prioritu.

No, jsem zvědavý, jestli na základě tohoto callu, poznámek, které jsem si udělal, a nově nabytých vědomostí a kontaktů dokážu s tou studií nějak pracovat a aplikovat to, nebo jestli to vyšumí.

## Apify

Dál jsem si hrál s Apify.
Přes Vánoce se mi povedlo stáhnout ukládaná data přes `apify-client` a použít na junior.guru.
Zatím jen na zkoušku pro stahování kurzů měn z ČNB, což je zcela nepodstatná funkce junior.guru, kterou tam mám kvůli jedné malé kravině.
Ale právě proto je to dobrý test.
Zatím vše funguje, takže je jen otázka času, než stejným způsobem přesunu na Apify další věci, především scrapery nabídek práce, kde to samozřejmě dává úplně největší smysl.

Předtím se ale ještě musím naučit použít na Apify jejich proxiny.
Zatím to nešlo, ale za mého velkého fandění Vláďa Dušek přes svátky [podporu pro proxy do Apify klienta a do Scrapy šablony přidal](https://github.com/apify/actor-templates/pull/260).
Taky se mi ozval Marek Trunkát, CTO Apify, že je rád, že i někdo z Česka staví něco nad Apify a jestli jim dám zpětnou vazbu na _developer experience_.

Protože jsem sledoval _code review_, když přidávali podporu pro proxy, a všiml jsem si tam malého úkolu, který chtěli udělat, napadlo mě jednou večer, že v rámci relaxu bych to mohl udělat jako open source příspěvek, když už se mnou tak pěkně komunikují.
Nakonec se mi to nepovedlo dokončit, ale i tak jsem to [vykopl do PR](https://github.com/apify/apify-sdk-python/pull/161) a třeba to někomu pomůže.
Sám jsem se při tom hned něco naučil, např. že [ruff](https://pypi.org/project/ruff/), o kterém vím, že existuje, ale nepoužívám ho, umí i formátovat kód a má zakomponované i věci jako [isort](https://pypi.org/project/isort/).

Musím říct, že největší problém v komunikaci s Apify je přeučit se, že po písmenech Api- následuje -fy a ne -ary.
Zvyk je železná košile a tahle slova jsou si až příliš podobná 😅

## PoC profilů juniorů

Rozhodl jsem se začít tvořit profily juniorů na junior.guru, aby si mohli snadněji shánět práci.
Měl jsem to už dlouho vymyšlené.
Základem byly role na Discordu.

Ve čtvrtek jsem si vytyčil úkol zhruba na hodinu, že si informace z rolí uložím do databáze.
Základní kámen celé věci.

Po 3-4 hodinách hledání, psaní na různá fóra, čtení kódu a _reverse-engineeringu_ Discord API jsem naznal, že to, co jde vidět v Discord aplikaci, tam prostě není a nemám se to jak dovědět.
Takže jsem nenaprogramoval nic a zpět ke kreslícímu prknu.

## Terapie

Chtěl jsem si konečně sehnat nějakou psychoterapii, takže jsem mkrnul na [czap.cz/adresar](https://czap.cz/adresar), který mi někdo doporučil.
Bohužel vyhledávání a filtrování mi tam vůbec nevyhovovalo.
V Praze je hromada terapeutů a abych tam mohl chodit pravidelně, chtěl jsem se omezit pouze na ty, kteří jsou poblíž bydliště nebo kanceláře.
Bohužel tak detailní filtrování tam není.
Nezbylo než si vyhrnout rukávy…

Dal jsem tomu zhruba hoďku a jo, nějak to šlo, takže další hoďku jsem to ladil a za jeden večer jsem si takhle přes Python scrapnul celý ten katalog.
Nejvíc mi dalo zabrat, že API ze serveru vrací data v JSONu, ve kterém byl jako hodnota uložený nějaký JavaScriptový objekt.
GitHub Copilot mi poradil knihovnu `demjson`, která nefungovala, ale objevil jsem [demjson3](https://pypi.org/project/demjson3/), a s tím už to nějak šlo.

Stažený katalog už pak šlo docela snadno na pár řádcích vyfiltrovat tak, jak potřebuji já.
Dokonce jsem si k jednotlivým terapeutům dogeneroval odkazy na Mapy.cz s jejich adresou apod.
Vyřadil jsem terapeuty, o kterých nešlo nic zjistit, nebo kteří mi z jakéhokoliv náhodného důvodu nebyli sympatičtí z webu.
Ale ve výsledku jsem měl pořád příliš mnoho možností, asi deset.

Než abych si četl weby terapeutů, kteří možná nenabírají, rozhodl jsem se všem napsat e-mail s jedním řádkem, zda je informace v katalogu aktuální a opravdu nabírají nové klienty.
Překvapilo mě, že asi tři lidi odpověděli hned v noci, a přemýšlel, zda je mám vyřadit na základě jejich špatného _work-life balance_.
Počkal jsem do druhého dne.
Vyřadil jsem terapeuty, kteří neodpověděli, nebo nepřijímali klienty.
Někdo také změnil adresu, která by už byla moc z ruky, takže taky z kola ven.

Ze zbytku si už budu muset nějak vybrat, pořád je to asi pět lidí.
Nejspíš nezbývá než je potkat a vyzkoušet.

## Další

-   Začal jsem přepisovat [film2trello](https://github.com/honzajavorek/film2trello) z webové appky a bookmarkletu do Telegram bota.
-   Byli jsme se ženou poprvé od narození potomka oba spolu v kině.
    Akorát když se ta příležitost naskytla, tak tam nic moc nedávali, takže jsme šli na [Wonku](https://www.csfd.cz/film/972101-wonka/prehled/).
    Protože jsme viděli [recenzi od Fily](https://www.kinobox.cz/clanky/recenze/32901-videorecenze-wonka), věděl jsem, co čekat.
    A v kině jsem dostal, co jsem čekal, a ještě něco navíc - aspoň teda já jsem si v tom filmu všiml kritiky současné formy kapitalismu.
    Co mě trochu mrzí je, že na to, že to byl muzikál, tak mi z filmu hraje v hlavě všeho všudy [jediná písnička](https://www.kinobox.cz/clanky/recenze/32901-videorecenze-wonka), která tam byla spíš ze srandy.
    Když srovnám s Vlasy nebo Nocí na Karlštejně, tak bída.
-   Volal jsem si s ENGETO a bavili jsme se s Marianem o trhu, budoucnosti, AI, krachu Green Fox Academy, a všem možném.
    Tyto hovory mě baví.
    ENGETO je něco mezi zákazníkem a konkurencí, ale vlastně si s Marianem volám spíš jako s podnikatelem z oboru, jen tak si povídáme a zamýšlíme se nad vším možným.
    Chtěli jsme původně řešit anketu mezi juniory, ale shodli jsme se, že to teď oba máme na chvostu priorit, a necháme to zatím u ledu.
-   Napsal jsem e-maily všem dokotrům, ke kterým mám zajít.
    Od všech mi přišlo, že mám zavolat.
    Když jsem volal, nikdo to nezvedl.
-   Nepovedlo se mi na Alze koupit USB-C/USB-C kabel, který by správně fungoval s Albi tužkou.
    K ní je dodávaný jen USB-A/USB-C kabel.
    Když jsem se jich ptal, jaký si mám koupit, aby to fungovalo, tak mi napsali, že mi kabel klidně pošlou zdarma, akorát mám napsat, zda chci micro USB, nebo mini USB.
    V ten moment jsem si uvědomil, že se právě nacházím v kabelovém pekle a nechal jsem to zatím být.
-   Něco se rozbilo na [czech-political-parties](https://github.com/honzajavorek/czech-political-parties/), tak jsem to opravil.
    Akorát že teď po pár dnech se rozbilo zas něco jiného, takže to budu muset zase opravit.
    Po delší době jsem se přihlásil na Twitter a zjistil jsem, že data z tohoto projektu [někdo dokonce reálně používá](https://twitter.com/ProgramyDoVoleb/status/1737120205099188467).
-   Zjistil jsem, že pokud využívám GitHub Pages a mám na doméně hvězdičkové DNS, tak toho mohou zneužít hackeři a vytvořit si stránku na sub-sub-doméně.
    Ošetřil jsem jak junior.guru, tak weby Pyvce, aby se to dít nemohlo.
    Hackerům se povedlo založit `sltgacorterbaru.id.junior.guru` nebo `wasiat4d.go.pyladies.cz`.
    Viz [oranžový Warning tady](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages).
-   Opravil jsem pár chyb v Discord botovi, něco v nabídkách práce, něco v seznamu rolí…
    Debugoval jsem, proč se některé kurzy na jsemvkurzu.cz neobjevují v katalogu na junior.guru.
    Důvod už znám, ale oprava bude na větší programování.
-   Měli jsme schůzi výboru Pyvce.
    Nevím, jestli jsme zvládli zápis, bylo to nějaké zmatené, ale vyřešili jsme nějaké věci a posunuli jsme vpřed hledání účetní.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Udělil jsem dvě stipendia na členství v klubu.
-   Za 15 dní jsem při procházkách nachodil 17 km, na túrách nachodil 24 km. Celkem jsem se hýbal 10 h a zdolal při tom 41 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1. Sepíšu na blog plán na Q1.
2. Zapojím Apify proxy.
3. Odjedu bobovat do Jeseníků.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Praha hlavní nádraží (1/4): Jak jsme se dostali do současného stavu?](https://www.youtube.com/watch?v=Ac2KEGISVKQ&list=PLhvTPVIo2nUHr_zzW4tt9DWK7IMr6hCNY)<br>Pěkný Gebrianův seriál o novém Hlaváku.
- [Jsme připraveni stavět města pro život? — Studio N](https://denikn.podbean.com/e/jsme-pripraveni-stavet-mesta-pro-zivot/)<br>Anděl? Tak to mě zklamal. Jedině dolní Žižkov 😤😀 Jinak samozřejmě jako vždy, co věta, to zlato.
- [hashtagstredovek (@hshtgstredovek) on X](https://twitter.com/hshtgstredovek/status/1741001742068986178)<br>Pěkné vlákno o tom, jak lidé ve středověku využívali a měnili les
- [A General History of the Pyrates - Wikipedia](https://en.wikipedia.org/wiki/A_General_History_of_the_Pyrates)<br>Skoro všechno, co víme o pirátech, pochází z jediné knížky od anonymního autora. A mnoho z toho, co o nich víme, moc neodpovídá zažitým popkulturním představám. Např. se v naprosté většině plavili na lodích s jedním stěžněm.
- [Pod čarou: Jak předpovědět budoucnost? Počítejte s tím, že půjde o peníze.](https://seznam-zpravy.u.mailkit.eu/mc/VUCVVPPV/RYHYKCADEIVXQOMKYA/CPMCLPPVWVE)<br>„…řada lidí dokáže skvěle vykreslit vize světů, kam by nás nové technologie mohly teoreticky zavést, ale zcela zapomíná na to, kam nás za současných ekonomických a společenských podmínek zavedou zcela určitě.“
- [The hardest part of building software is not coding, it's requirements - Stack Overflow](https://stackoverflow.blog/2023/06/26/the-hardest-part-of-building-software-is-not-coding-its-requirements/)<br>Tak budeme psát kód, nebo nebudeme? Tenhle článek se snaží říct, že programátoři budou potřeba i s AI, ale já to teda čtu tak, že budou potřeba spíš technicky zdatní produkťáci, přesně jak Matt Welsh naznačuje v té své přednášce na Hardvardu.
- [Large Language Models and The End of Programming - CS50 Tech Talk with Dr. Matt Welsh](https://www.youtube.com/watch?v=JhCl-GeT4jw&t=749s)<br>Tohle mě, musím říct, přinutilo přemýšlet.
- [58: Peter Bednár: Urbanistův pohled na dopravu ve městě — 2050](https://audioboom.com/posts/8418824)<br>Největší problém aut je, že zabírají příliš mnoho prostoru.
- [Vlašský salát – Wikipedie](https://cs.wikipedia.org/wiki/Vla%C5%A1sk%C3%BD_sal%C3%A1t)<br>„Úpadek receptury nastal v posledních válečných a poválečných letech z důvodu nedostatku některých ingrediencí a dále pak po únoru 1948, kdy se jednalo o obdobu bramborového salátu, přičemž šunku, sledě a ančovičky vystřídal šunkový salám.“ Tohle je snad nejpropracovanější heslo na Wikipedii, jaké jsem za dlouhou dobu viděl.
- [Matika mě úplně pohltila, říká mezinárodně oceněná studentka. Stále slýchá komentáře na založení rodiny](https://www.irozhlas.cz/veda-technologie/veda/dominika-buresova-matematika-cvut-vyzkum-kvantove-logiky_2312240500_epo)<br>Matika drsnej obor: „Začala jsem pozdě v disciplíně, které se lidé často věnují už od šesti let, a chytla jsem se…“ Ale zjevně i tam může člověk jako career switcher uspět: „Když mě to na právech nebavilo, tak jsem utíkala do jiného světa. Chodila jsem na šifrovačky, různé logické soutěže, turnaje ve strategických deskovkách. Šlo mi to, a tak mi okolí začalo říkat, že bych byla dobrá na matiku. Tak jsem se rozhodla, že to zkusím.“
- [I Accidentally Saved Half A Million Dollars — Ludicity](https://ludic.mataroa.blog/blog/i-accidentally-saved-half-a-million-dollars/)<br>„It's cosplaying as a real business and the board thinks the costume is convincing.“ „I would have been better off not doing anything.“
