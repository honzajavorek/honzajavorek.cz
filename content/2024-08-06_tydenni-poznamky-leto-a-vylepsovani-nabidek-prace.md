Title: Týdenní poznámky: Léto a vylepšování nabídek práce
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-07-19_tydenni-poznamky-kokorinsko-a-apify.md) už utekl nějaký ten týden (19. 7. až 6. 8.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
</div>

## Zbytek Apify týdne

Ještě dva dny mi zbývaly do konce týdne, kdy pracuji pro Apify. Udělal jsem několik Pull Requestů na nejrůznější věci a postěžoval jsem si na Mastodonu na [Docusaurus](https://mastodonczech.cz/@honzajavorek/112830258906596969) a na [jQuery](https://mastodonczech.cz/@honzajavorek/112835798448512966).

Protože v srpnu budu mít hodně volna, neměl bych kam vůbec nějaký týden pro Apify natlačit. Domluvil jsem se tedy s nimi, že další bude až v září. To mi dá v srpnu větší volnost, ale samozřejmě pošlu o fakturu méně a bude méně peněz.

## Dovolená a zábava s ekzémem

Od 26.7. do 31.7. jsme jeli na dovolenou. Byli jsme na statku se zvířátky. Teta tam slavila narozeniny a my tam pak zůstali ještě na pár dní a udělali jsme si jeden výlet na kole do papouščí zoo. Bylo to fajn, akorát že na nás lezlo nějaké nachlazení, a nakonec jsem kvůli horku poznal novou zdravotní komplikaci, kterou jsem ještě neznal: dyshidrotický ekzém. Nemohl jsem skoro chodit a v noci to svědilo tak, že jsem nemohl spát.

Když jsme přijeli z dovolené domů, tak se to zrovna rozjelo, takže jsem hned ve čtvrtek zašel na dermatologii (naštěstí měli volno) a dostal léky, _good_. Jenže jedny ty léky měly vedlejší účinky a po sérii tragikomických událostí jsem skončil zase v sanitce a na urgentním příjmu.

Nic mi nakonec nebylo a ještě tu noc jsem byl zpátky doma. Akorát jsem se zase nevyspal, takže pátek jsem pak pro změnu prospal úplně celý. Ekzém se díky (jiným) lékům lepší a jinak mi asi nic není, takže žádné obavy.

Psychoterapeutka mi řekla, že můj život je řítící se vlak událostí, který se na terapiích jen marně snažíme chytit 😀 Jako předsevzetí si dávám, že se budu snažit být víc nudnej.

![Kůň]({static}/images/photo-2024-08-06-17-50-22.jpeg)

## Malé opravy

Když jsem po ukončení Apify týdne naskočil zase do junior.guru, hlavně jsem četl zpětně klub, odpovídal na co jsem uměl a v kódu opravoval, co se kde mezitím rozbilo.

Nedokázal jsem se dostat ke zpětné vazbě na CV v klubu, tak doufám, že tam toho moc nehnije. Mluvili jsme o tom s Danem Srbem a třeba do budoucna vymyslíme nějaký lepší systém, než ten, kdy vše závisí pouze na dobrovolnících z komunity.

Na Apify už se scrapery snadno vyčerpám free tarif a došly mi kredity zdarma nasbírané z různých akcí a konferencí, takže jsem šel a zaplatil jsem si to. Využil jsem nějaký speciální tarif pro _creators_, takže to stálo jen pár dolarů. Ten normální tarif už by byl moc drahý a to bych šel asi už do Apify škemrat o nějakou slevičku, ale zatím to není potřeba.

Opravil jsem pak ještě něco v testech, ve scraperech, opravil jsem jak se zjišťuje počet mých followerů na LinkedInu (ten zase totiž něco změnil), a tak.

## Dependabot

Ladil jsem [nastavení Dependabotu](https://github.com/juniorguru/junior.guru/blob/main/.github/dependabot.yml), aby mi vyhovovala frekvence toho, jak často posílá Pull Requesty. Není to tak snadné, jak se zdá.

Mám hromadu repozitářů, takže každý den dostanu hromadu Dependabot Pull Requestů. Větší změny je lepší mít v samostatných PR, menší změny možná lepší [sdružit do skupinek](https://github.blog/changelog/2023-08-24-grouped-version-updates-for-dependabot-are-generally-available/), což jsem se až teď [díky lidem na Mastodonu](https://mastodonczech.cz/@honzajavorek/112842979843727837) dověděl, že vůbec jde. Závislosti jako Ruff nebo Pytest stále vydávají nějaké malé nové verze, což je otravné. Ale _security updates_ chci spíš hned! A když mám na repozitáři otevřených víc takových PR najednou a jeden mergnu, zpravidla vznikne _merge conflict_ v _lockfile_ a musí se to rebasovat a musím čekat a je to otrava.

Stále s tím ještě nejsem spokojený a ladím to do nějaké podoby, která bude vyhovovat konkrétně mně.

## Lychee

Zkusil jsem na junior.guru vyměnit [broken-link-checker-local](https://www.npmjs.com/package/broken-link-checker-local) za [lychee](https://github.com/lycheeverse/lychee), které znám z Apify.

Největší výzva byla přijít na to, jak na CircleCI nainstalovat věc v Rustu, ale nakonec to bylo vlastně jednoduché. Pak jsem poladil nastavení, opravil nějaké rozbité odkazy, a frčí to. Jediná věc, se kterou mám problém, je [tohle](https://github.com/lycheeverse/lychee/issues/1474), ale to asi nějak vyřeším prostě tím, že ty pomlčky vyhodím.

## Vylepšování pracovních nabídek

Kromě vyřizování mailů, čtení klubu a ladění věcí souvisejících spíš s mým podnikáním, než s juniory samotnými, jsem potřeboval po delší době něco, z čeho bych měl pocit dobře udělané, fakt užitečné práce. Rozhodl jsem se tedy věnovat nějaký čas vylepšování pracovních inzerátů, protože tam to jde vidět a pomůže to hodně lidem.

- Opravil jsem dvě chyby ve scraperu, který stahuje pracovní inzeráty z Jobsů.
- Předělal jsem posílání inzerátů do klubu tak, aby bylo efektivnější a laskavější k Discord API.
- Přešel jsem na model GPT-4o mini. Doporučovali mi „Gemini 1.5 Flash, lepší než 3.5, 1 milion tokenů na request, umí to JSON formát a když tak jsou na to Python libky - v tuhle chvíli nejlepší levné řešení s dobrou češtinou“, ale byl jsem líný přecházet na něco úplně jiného a místo toho jsem zkusil upgrade modelu od OpenAI a poladit prompt.
- Prompt jsem ladil docela dost a dostal jsem se postupně do situace, kdy už to celkem funguje, jak bych chtěl. Předtím to odfiltrovalo příliš mnoho nabídek. Teď se každou chvíli v klubu objevují nové. Jupí!
- K inzerátům v klubu jsem přidal krátké odůvodnění, proč si AI „myslí“, že je nabídka vhodná pro juniory. Je to spíš _debug_ informace pro mně, ale třeba to někoho bude bavit číst 😀
- Vytvořil jsem na Discordu tajný kanál s „košem“ pracovních nabídek. Bot vyřadí třeba 800 nabídek z 900, takže jsem přemýšlel, jak ho nejlépe kontrolovat tak, aby se to dalo zvládat. Ať už jede bot na AI nebo jel předtím na regulárech, vždy jsem řešil, jak to v tom objemu sledovat. A až teď mě napadlo, že kontrola bude namátková! Nevím, proč mě to nikdy nenapadlo dřív. Každopádně vyberu z těch 800 odhozených nabídek ty, které mají v titulku slovo „junior“ a z těch vyberu 20 náhodných. Ty si nechávám poslat do onoho „koše“ a můžu tak sledovat, zda mi bot nevyhazuje něco, co by ve skutečnosti bylo hodnotné.
- U každého inzerátu v klubu je detail firmy a tam je nově odkaz na vyhledávání na Atmoskopu, Googlu, a LinkedInu.
- Začal jsem přidávat analýzu klíčových slov pomocí regulárních výrazů a začal jsem si na to psát [separátní knihovnu](https://github.com/juniorguru/beak), protože se mi tahle věc hodí jak při vítání nových členů v klubu, tak se mi bude hodit u těch pracovních inzerátů. Když to tady ale teď píšu, tak si říkám, že na analýzu klíčových slov možná už mohlo něco hotového existovat? Asi nejsem první na světě, kdo tohle řeší… Tak jsem se hned zeptal kamaráda a ještě na Pyvec Slacku.

![Nabídky práce v klubu]({static}/images/screenshot-2024-08-06-at-17-37-12.png)

## Přednáška o Dockeru

Lukáš Pavelka, který dříve začínal svou kariéru v klubu, se mi opět nabídl s přednáškou, tentokrát o Kubernetes. Ukecal jsem ho na to, že to bude spíš o Dockeru, a s mými velkými prodlevami mezi zprávami jsme nakonec dohodli i termín.

Detaily k přednášce jsme doplňovali trochu na poslední chvíli, a protože mi v ten den zrovna nebylo dobře, Lukášovi jsem neodpovídal. On ale našel správný YAML a dokonce do něj poslal Pull Request se vším, co bylo potřeba, včetně obrázku, takže jsem to pak večer jen mergnul a bylo - boží. Přednášku jsem pak propagoval na [LinkedIn](https://www.linkedin.com/posts/honzajavorek_kubernetes-docker-activity-7226142556907065344-TWxN) i na [Mastodonu](https://mastodonczech.cz/@honzajavorek/112908682528202405).

![Upoutávka]({static}/images/20240806-5d67043bcfae2946c9990d7f6c208701986b13fc74f2e1ca33f3f2451c671504-dc.png){: .img-thumbnail }

Přednáška proběhla dnes. Kameru na noťasu mám stále nefunkční, takže jsem použil mobil přes [Continuity](https://www.apple.com/macos/continuity/). S nahráváním mi pomohl [Patrik](https://www.linkedin.com/in/patrik-brnusak-cz/). Nejvyšší počet lidí online byl myslím 23, což je dost slušná návštěvnost na to, že je venku hezky a jsme uprostřed léta, takže celkem hustý! Asi dobrý téma.

![Přednáška]({static}/images/screenshot-2024-08-06-at-18-28-54.png)

## Pošli LOVE

Po několika neprovedených trvalých příkazech z důvodu nedostatku prostředků jsem přeskládal strukturu trvalých příkazů a omezil, kolik peněz jde do úspor. A zkusil jsem udělat po delší době něco, co by mělo nějaké peníze i vydělat.

- Napsal jsem všem firmám, kterým teď bude končit sponzorství a snažím se s nimi domluvit na prodloužení. Někteří ještě vůbec neodepsali, někde máme domluvené schůzky. Očekávám, že by dvě firmy mohly prodloužit, jedna je tak pade na pade, a jedna nejspíš neprodlouží, protože to byl jednorázový záchvěv dobrodiní před rokem a nezapadá to do žádné jejich dlouhodobé strategie. Nebylo by od věci nalákat i nějaké nové firmy, ale to bych asi musel přitlačit na _sales_, což je věc, kterou neumím a vždy ji nekonečně dlouho prokrastinuji. To dřív naprogramuju profily juniorů.
- Než někomu skončí sponzorství, napsal jsem rychle status na LinkedIn o tom, jak jsou na webu tři loga ze čtyř, a že je jedinečná šance získat čtvrtý a poslední slot 😀 V onom [statusu](https://www.linkedin.com/posts/honzajavorek_lovebrand-dei-csr-activity-7226482201691860993-DPHS) vychvaluji příručku a snažím se jít naplno do toho, abych ve čtenáři vyvolal SHUT UP AND TAKE MY MONEY, ale zatím to jen generuje lajky. Tak snad lajky aspoň způsobí, že se to zobrazí víc lidem a nějakým mávnutím motýlích křídel to někoho někde přesvědčí. Udělá mi velkou radost, pokud na příspěvek zareagujete, nejlépe komentářem, ale i ten lajk nebo share potěší.

V obou případech jsem využil novou stránku [Pošli LOVE](https://junior.guru/love/), na které jsem předtím týdny vyšíval a která by měla umožnit přispět komukoliv, ať už je to jednotlivec nebo korporát, ať už chce do klubu nebo nechce.

![Status na LinkedIn]({static}/images/screenshot-2024-08-06-at-17-37-43-1-post-linkedin.png)

## Další

-   Připojili jsme se jen dva na schůzi výboru Pyvce. Věnoval jsem aspoň ten čas tomu, abych se pověnoval věcem z Pyvce. Poklikal jsem nějaké věci, co byly potřeba poklikat, napsal jsem členům co je za novinky, a motivoval jsem člena Jana Smitku, aby [aktualizoval na našich webech adresu na novou](https://github.com/pyvec/pyvec.org/pull/425). Dodatečně jsem ještě stahoval pro účetního nějaké výkazy z [Benevity](https://benevity.com/), přes které jsme dostali pár darů.
-   Snažil jsem se upozornit MPSV na to, že jim nefunguje doména jsemvkurzu.cz, ale [marně](https://mastodonczech.cz/@honzajavorek/112848436339694237). Odepsal jsem jim ještě a zkusil vysvětlit, co přesně myslím, ale na to už jsem ani nedostal odpověď.
-   Začal mi blbnout [Kanban board v Obsidianu](https://github.com/mgmeyers/obsidian-kanban). Velmi často se nenačte jako board, ale jen jako Markdown. Až když ho otevřu do nového tabu, a někdy až napotřetí. Stává se to jen na počítači, nikdy na mobilu. A je to otravné, protože to je junior.guru úkolníček, který používám každý den, celý den. Trochu pomohlo, když jsem umazal už hotové úkoly, ale nepomohlo to úplně. Možná je ten board už moc velký? Vždyť v něm mám zlomek toho, co jsem míval v Trellu! 😀 Chtěl jsem založit issue někde na GitHubu, ale pak jsem místo toho šel a [autorovi pluginu](https://github.com/sponsors/mgmeyers) jsem jednorázově přispěl přes GitHub Sponsors a dál jsem to zatím neřešil. Pokud chci, aby svět nějak fungoval, musím se na tom fungování taky podílet.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Nestíhám odpovídat na všechny e-maily, hlavně ne na ty povídací, kde lidi posílají dotazy na několik odstavců. Určitě na ně někdy odpovím, ale holt jsou většinou prioritnější věci.
-   Za 19 dní jsem naběhal 12 km, při procházkách nachodil 9 km, ujel na kole 52 km. Celkem jsem se hýbal 37 h a zdolal při tom 73 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

Zítra mi začíná další dovolená, takže neplánuju nic. Pokud se pak mrknu na práci, asi budu hlavně číst klub a e-maily. Až udělám to, můžu si vybrat, jestli opravím [statistiky](https://junior.guru/open/) a naplánuju si čtvrtletí, nebo se budu dál šťourat v pracovních inzerátech.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [FastHTML](https://fastht.ml)<br>FastHTML, nový webový framework v Pythonu. Koukl jsem na intro video a docela hustý.
- [Máme malé nároky, říká terapeutka veřejného prostoru Veronika Rút](https://denikreferendum.cz/clanek/36511-mame-male-naroky-rika-terapeutka-verejneho-prostoru-veronika-rut)<br>„Jako bychom nepochopili, že v civilizované zemi je nutné mít nějaká pravidla a držet se jich. Uvěřili jsme, že nemít pravidla je akt antikomunismu.“
- [My family and other Nazis](https://www.theguardian.com/world/article/2024/jul/23/my-family-and-other-nazis)<br>„Anyone who insists on digging up the shameful past in which so many Austrians participated in the most gruesome crimes will not have a warm reception in my country. There are still large parts of society that think we should let the past rest.“
- [První SMART zastávky na české železnici jsou hotové, začne pilotní provoz - Zdopravy.cz](https://zdopravy.cz/prvni-smart-zastavky-na-ceske-zeleznici-jsou-hotove-zacne-pilotni-provoz-214130/)<br>Tohle je super.
- [Německá Nová Guinea – Wikipedie](https://cs.wikipedia.org/wiki/N%C4%9Bmeck%C3%A1_Nov%C3%A1_Guinea)<br>TIL že Německo mělo kolonie v Pacifiku a část jich dokonce koupilo od Španělska po tom, co Španělsko prohrálo válku s USA
- [Obchod Sneaker Gallery je v insolnvenci. Věřitelé chtějí zpět desítky milionů – Page Not Found](https://pagenotfound.cz/clanek/obchod-sneaker-gallery-je-v-insolnvenci)<br>Forbes, CzechCrunch. O vzletu se dovíte, o pádu nikoliv. „Příliš nadšené zprávy v byznysových médiích a žebříčky úspěšných vytváří zvláštní kulty osobnosti, kde je nejpodstatnější silný příběh a první dojem. Tlak je pak především na to, aby v mladém věku člověk uspěl a dostal se do první ligy miliardářů. Tohle pozlátko někdy může být silnější než realistické byznys plány, které někteří investoři a média moc do hloubky nezkoumají.“
- [Flanérem až do konce svých dnů – Page Not Found](https://pagenotfound.cz/clanek/flanerem-az-do-konce-svych-dnu)<br>„V Česku to patrně nezní dobře, ale místo řídkých a energeticky náročných satelitů s bazény potřebujeme hustou, dostupnou městskou zástavbu, jejíž součástí bude také veřejné koupaliště s parkem.“
- [CityApp](https://fitzlab.shinyapps.io/cityapp/)<br>Jaké bude u nás klima za 60 let? Jako v Bulharsku teď.
- [The New Internet](https://tailscale.com/blog/new-internet)<br>„I read a post recently where someone bragged about using kubernetes to scale all the way up to 500,000 page views per month. But that’s 0.2 requests per second. I could serve that from my phone, on battery power, and it would spend most of its time asleep.“
- [35% Faster Than The Filesystem](https://sqlite.org/fasterthanfs.html)<br>„SQLite reads and writes small blobs (for example, thumbnail images) 35% faster than the same blobs can be read from or written to individual files on disk using fread() or fwrite(). Furthermore, a single SQLite database holding 10-kilobyte blobs uses about 20% less disk space than storing the blobs in individual files.“
- [0,5 % vol. To nejlepší z obou světů – Page Not Found](https://pagenotfound.cz/clanek/05-percent-vol-to-nejlepsi-z-obou-svetu)<br>Jetmar! „Česko je zemí nasáklou chlastem. Patrně i hory tady po ránu vydechují alkovýpary.“ „…jeden z největších pivovarských konglomerátů světa… chce mít už v roce 2040 polovinu svých prodejů z nealko či nízko-alko nápojů.“ „Odvyklí od skutečné práce, té rukama, jsme záhy zjistili, že potřebujeme iontový nápoj. Pivo, byť desetistupňové, nás však zejména v teplejším počasí lenivělo. Navíc jsme museli večer často ještě něco dělat do práce, té placené, na počítači…“
- ["Některými kroky jsem si vytvořil nepřátele na smrt." Jindřich Vobořil o odchodu z funkce protidrogového koordinátora, regulaci návykových látek i trestech za konopí – Page Not Found](https://pagenotfound.cz/clanek/nekterymi-kroky-jsem-si-vytvoril-nepratele-na-smrt-jindrich-voboril-o-odchodu-z-funkce-protidrogoveho-koordinatora-regulaci-navykovych-latek-i-trestech-za-konopi)<br>„Dopady všeho, co je s rizikovým pitím spojené, dělají z alkoholu tu vůbec nejnebezpečnější látku. Když vyskládáme všechny drogy vedle sebe a zhodnotíme míru jejich závadnosti, alkohol z toho vyjde nejhůř a až za ním je heroin. Takhle je to drsné…“
- [Every company should be owned by its employees](https://www.elysian.press/p/employee-ownership)<br>Zajímavý přístup. Co je ekvivalentem v Česku?
- [On Open Source and the Sustainability of the Commons](https://ploum.net/2024-07-01-opensource_sustainability.html)<br>„I’m convinced that paying the contributor/maintainer a dime is not the solution. It worsens the situation. It acknowledges the responsibility of the aforementioned maintainer and legitimises the exploitation.“ „We were tricked into thinking that BSD or MIT licences were "freer" like we were tricked into believing that building a polluting factory next to our local river would be "good for the economy". It is a scam.“
- [Rant: Please stop ruining the search](https://hamatti.org/posts/rant-please-stop-ruining-the-search/)<br>„These algorithms are not for the benefit of the user or the human. They are used for brutally optimizing engagement which means that content that is clickbaity, provocative or simple gets way more exposure than other content.“
