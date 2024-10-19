Title: Týdenní poznámky: Nové kapitoly do kurzu scrapování a péče o marody
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/330
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/113335141406937247

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-10-04_tydenni-poznamky-jsem-na-tiktoku-ubehl-jsem-pulmaraton-a-mega-vylepsuju-stranku-s-inzeraty.md) už utekl nějaký ten týden (4. 10. až 19. 10.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Nové kapitoly do kurzu scrapování

První týden jsem věnoval Apify, ale naskákala mi do toho spousta dalších věcí. Jmenovitě call s Red Hatem, kde jsme si chvíli povídali o naší spolupráci a o její budoucnosti, potřeboval jsem [propagovat přednášku v klubu o Kubernetes](https://mastodonczech.cz/@honzajavorek/113282418404448705), a byl jsem ve středu dopoledne pozvaný do [diskuzního panelu o komunitách](https://talkbase.io/event/breakfast-for-community-builders/czech-community).

![Panel]({static}/images/img-2868.jpg)

Frontkon (a ani jejich afterpárty v Apify kancelářích) jsem do toho už nenacpal, ale z ohlasů na sociálních sítích byl legendární a potěšilo mě, že hodně trendovala [fotka, kterou sdílela skupinka z junior.guru klubu](https://www.linkedin.com/feed/update/urn:li:activity:7249884643905212418/).

![Členové junior.guru klubu na konferenci Frontkon]({static}/images/1728507188505.jpg)

I když dcera pak zůstávala doma s rýmou a kašlem, práci jsem celkem stíhal, hlavně díky tomu, že nám záměrně na tento můj Apify týden přijela pomáhat babička:

- Apify mělo _all hands_, takže se sem sjížděli kolegové z nejvzdálenějších koutů zeměkoule, třeba z Brna nebo Krakówa. Povedlo se mi konečně potkat s Michałem, jejich technical writerem, a s Vláďou, jejich Pythonistou, který mě do Apify dotáhl a teď pracuje na pythoní verzi scrapovacího frameworku Crawlee. S oběma jsme probrali i dost věcí kolem práce, takže byť před námi bylo kafe nebo pivo, dalo by se to asi považovat za pracovní čas 😀
- Pomohl jsem mergnout jeden [PR s drobnými vylepšeními Akademie](https://github.com/apify/apify-docs/pull/1218) (za kterou zodpovídám).
- Bušil jsem další a další lekce do Python kurzu scrapování. Většina mé práce je v [tomto PR](https://github.com/apify/apify-docs/pull/1244). Ze screencast videa [jsem vyrobil gif](https://github.com/apify/apify-docs/pull/1244#issuecomment-2421796237), což jsem dělal poprvé, nebo skoro poprvé. Opět jsem se díky práci pro Apify něco hezkého naučil!
- Přemýšlel jsem nad tím, jak budu testovat příklady v Python kurzu. Jako na zavolanou, Simon Willison se [šťoural v podobném tématu](https://simonwillison.net/2024/Oct/16/markdown-test-framework/), tak jsem si z diskuze na Mastodonu [vyzobal některé tipy](https://github.com/apify/apify-docs/issues/1243#issuecomment-2418055868).

![Můj GIF]({static}/images/377782597-1bc3b980-c837-4adf-b5da-13cc871eec74.gif)

## Kino a F1news

Kromě „oficiální“ práce pro Apify jsem se zase šťoural i ve svých vlastních scraperech, které sice dělám jen pro radost, ale záměrně jsem je začal vytvářet na Crawlee, abych se s tím naučil.

Po různých peripetiích generujících spoustu feedbacku na Crawlee se mi povedlo dokončit [kino](https://github.com/honzajavorek/kino). Díky tomu mám konečně promítání v blízkých kinech v Google Kalendáři! Nakonec jsem nescrapoval jednotlivá kina, protože by se to špatně udržovalo, ale vzal jsem to z [rozvrhů na ČSFD](https://www.csfd.cz/kino/1-praha/).

![Kino v kalendáři]({static}/images/screenshot-2024-10-12-at-15-54-53.png)

Další projekt? [Zprávy o F1!](https://github.com/honzajavorek/f1news) Dřív jsem sledoval Reddit o F1, ale pak Reddit zařízl API a alternativní klienty. To vyvolalo velké protesty, ke kterým jsem se přidal, a během nichž jsem zjistil, že mi Reddit v každodenním životě nechybí.

Akorát že admini F1 subredditu vytvořili Discord, kam jsem se přidal, a tam padá docela dobrý feed zpráv o F1, který mi vyhovuje. Po čase mi ale došlo, že na tom Discordu nic jiného nesleduju a vlastně mě obtěžuje, že tyhle zprávy mám někde na Discordu (potažmo na Redditu), a ne třeba v RSS čtečce. Bohužel Discord nemá přesně takové RSS, jak je to vyfiltrované do toho Discordu přes nějakého bota, který funguje kdo ví jak. Tak si říkám, hmm, tohle je práce na 15 minut. Stáhnout RSS, udělat HTTP požadavek na každý článek, vyfiltrovat to podle štítku jen na zprávy, a uložit si nové RSS. To si pak přidat do čtečky.

Tenhle projekt na 15 minut mi zabral po kouskách tak 5 hodin. Opět to vygenerovalo spoustu feedbacku na různé věci kolem Crawlee, např. [jak střídat typy crawlerů](https://github.com/apify/crawlee-python/discussions/573), nebo [všechno možné kolem dokumentace a debugování](https://github.com/apify/crawlee-python/discussions/575#discussioncomment-10866411). Poptal jsem [architecture overview](https://github.com/apify/crawlee-python/issues/603) nebo [lepší dokumentaci API](https://github.com/apify/crawlee-python/issues/324#issuecomment-2423846344). Protože to měl být projekt na 15 minut, protože jsem to dělal ve svém vzácném „volném“ čase, a protože to bylo frustrující, prosakovaly do mých komentářů emoce, ale když jsem se zpětně ptal, tak prý vše OK a veškerý feedback je vítán 😅

Každopádně jsem skončil především na tom, že Reddit prostě ty moje HTTP požadavky blokuje. Ale takovým způsobem, že ani rezidentní proxy na Apify mi nepomohlo. Přitom z domácího počítače tentýž kód projde. Dělal jsem vše možné, zkoušel i browser scraping, ale Reddit mi nedal vůbec šanci.

Nenávidím tuhle novou dobu, kde nefungujou základní záležitosti na webu, protože si weby nasadí nějaké Cloudflary a jiné svinstva, takže člověk nemůže udělat ani deset blbých HTTP požadavků, aby si zjednodušil život. Nechť všechny _walled gardens_ a tyhlety _anti-scraping_ ochrany, kvůli kterým mi věčně nefunguje ani kontrola rozbitých odkazů na junior.guru, shoří v pekle.

![Reddit na Discordu]({static}/images/screenshot-2024-10-19-at-17-41-37.png)

## Péče o marody

Po víkendu dcera stále marodila a nechodila do školky. Babička už odjela, takže to bylo plně na nás a začal pracovní týden. Žena uvažovala nad OČR. Ještě nikdy si to nikdo z nás nebral, protože dřív nebylo koho ošetřovat a když bylo, tak byla žena doma a já jsem OSVČ, takže předpokládám, že nic jako OČR nemám 😀

Každopádně se to vyřešilo samo tím, že hned v pondělí žena lehla s nějakým svinstvem a doteď s tím zápasí. Složilo ji to tak, že týden jen spí a horečkuje. Už víme co to je a snad je to na dobré cestě, nicméně z toho doteď není venku. Já jsem tedy v pondělí nastoupil na péči na plný úvazek, nedalo se nic dělat.

Vše šlo stranou, takže do práce jsem skoro nic neudělal, po večerech sotva stíhal aspoň trochu odpočívat, a některé dny jsem se prostě od 7 rána do 9 do večera nezastavil. Dcera byla hodně živá, ale stále nachlazená, tak jsme museli přežít nějak doma, i když venku bylo hezky. Bral jsem ji aspoň do kočárku a projížděli jsme blízké parky a Olšanské hřbitovy. Na nějaké běhání nebyl vůbec čas, tak jsem si na Stravu zapisoval aspoň tohle chození.

Na hřbitovy jsme šli po obědě odpočívat tolikrát, že se tam zalíbilo i dceři a už tam máme i některé oblíbené hroby, třeba zeměkouli nebo pána zarostlého psím vínem. Našli jsme tam i nějakou školku s dětmi. Jako opravdovou, s živými dětmi. Narazil jsem na hrob Agustina Vološina a brácha mi pomohl najít [jeho zajímavý příběh](http://www.cs-magazin.com/index.php?a=a2004071006).

Bylo to dlouhé, intenzivní, a ani nevím, jak jsem to zvládl, ale ode dneška je to za mnou. Opět přijela babička a zachraňuje nás. Uf. Po týdnu si v klidu během dne sedím u počítače a něco si tu ťukám!

![Zarostlý pán]({static}/images/img-2642.jpg)

![Výhled]({static}/images/img-2665.jpg)

## Přednáška

Během péče o marody jsem nějak vyhaluzil i moderování přednášky v klubu. Šlo o úvod do Kubernetes od Lukáše Pavelky, na část přednášky se dívala i moje tříletá dcera a líbilo se jí to.

Myslel jsem, že bych šel na přednášku do kanceláře a že to doma žena zvládne, ale nakonec to moc nepřipadalo v úvahu, takže jsem to bral z domů v hodně improvizované podobě. Přednáška byla fajn, ale blbý bylo, že jsem celý den pečoval a místo abych večer odpočíval, tak jsem ještě řešil přednášku, takže jsem pak byl úplně mrtvý.

![Lukáš o Kubernetes]({static}/images/20241015-f474d9401a4faa290a53555f126dc373da301524da14166d00f610efa4425b6a-dc.png){: .img-thumbnail }

## Srazy jinak

Z kraje týdne jsem měl dojem, že má smysl se třeba po večerech pokoušet o nějakou práci na junior.guru, tak jsem se šťoural ve srazech. Bot do klubu posílá pozvánky na vhodné pravidelné srazy, ale nevyhovuje mi, jak to funguje, tak to chci předělat. Chtěl jsem si u toho odpočinout od předělávání všeho kolem pracovních inzerátů.

Nejdřív jsem řešil to, že když některý ze zdrojů informací o srazech nefungoval, shodilo mi to build celého junior.guru. Proto jsem všechny zdroje srazů přesunul postupně na Apify, odkud si můj build vždy stahuje poslední úspěšný výsledek scrapování, takže je to robustnější. Přidal jsem navíc i CZJUG, se kterým mi [zajímavým způsobem pomohlo ChatGPT](https://mastodonczech.cz/@honzajavorek/113312247621386121).

Pak už ale nebyl čas udělat nic. Když byla chvilka, napadlo mě, že bych mohl aspoň v klubu namotivovat lidi k tomu, aby sami založili nějaké místní skupinky. Do těch by mohl časem bot přesunout pozvánky tak, aby byly cílené. A taky aby se vytvářely místní komunitní buňky, které budou tímhle způsobem mít vlastní chat, i když se zrovna žádná akce neděje. Tím, že si to založí sami lidi, bude to víc „zespoda“ a bude to víc „jejich“, než kdybych to tam nějak předpřipravil, nedejbože udělal botem. S výsledkem jsem spokojen!

Snažil jsem se taky [zjistit](https://www.facebook.com/groups/144621756262987/posts/1567370833988065/), jestli jsou nějaké pravidelné srazy na Slovensku, ale nic moc jsem nenašel. Ani Rubyslava nevypadá, že žije. Tak pokud máte tip, dejte vědět.

![Scrapery na Apify]({static}/images/screenshot-2024-10-19-at-17-43-38.png)

![Motivace a skupinky]({static}/images/screenshot-2024-10-19-at-17-38-29-1.png)

## Nejrůznější opravy

Během těch dvou týdnů se postupně rozpadly různé věci, takže nebyla nouze o opravy:

- Přestal mi fungovat scraper na pracovní inzeráty z LI. Když mě LI zablokoval, zkoušel jsem tentýž požadavek udělat přes browser skrze [scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright/), jenže ten zase neumí brát proxy z Apify a celkově je to tam s proxy složitější. Napsal jsem si na to už dřív vlastní middleware, ale teď se ukazovalo, že se nezvládal vypořádat s nějakým sofistikovanějším blokováním. Zkoušel jsem odchytávat exceptions a nějak opakovat request, ale nic nefungovalo. Nakonec jsem zjistil, že když zvýším počet povolených opakování requestu a browser úplně vyhodím, stačí to. Rotace proxy zajistí, že se to prostě aspoň jednou podaří, i bez browseru. Chybu jsem tedy přestal opravovat, a scrapy-playwright jsem i s middlewarem úplně vyhodil. A zrychlil se i Docker build.
- Opravil jsem chybu ve skriptu, který mi hlásí pokud v klubu je někdo bez předplatného. To se stalo, zjevně Memberful bot neodchytil končící členství a zapomněl člověka „vyhodit“. Jenže jak byla ve skriptu chyba, začalo mi kvůli tomu všechno padat.
- Scraper na pracovní inzeráty z WeWorkRemotely špatně ukládal úvazky.
- Můj nový způsob normalizace lokací pracovních inzerátů měl problém s tím, když tam byl jen stát, např. pouze „Czechia“.
- GitHub začal uplatňovat rate limiting na jeden můj skript tady na blogu, tak [jsem mu přidal token](https://github.com/honzajavorek/honzajavorek.cz/commit/962af8b929177c649c86fea1bc348af1a7d20475).

Taky mi selhala kontrola rozbitých odkazů na junior.guru, protože [probíhal hack a útok na web.archive.org](https://www.youtube.com/watch?v=N3ZGNT5S5IU). Takové to, když vám zmizí z internetu užitečný web, což vám rozbije odkazy, tak ty odkazy nahradíte odkazy do internetového archivu, ale potom vám někdo začne ničit internetový archiv 🤦‍♂️

## Python komunita

- [Opravil jsem kontrolu rozbitých odkazů](https://github.com/pyvec/docs.pyvec.org/pull/400) na docs.pyvec.org (dokumentace české Python komunity).
- Propagoval jsem CfP pro PyCon NA: [LinkedIn](https://www.linkedin.com/posts/honzajavorek_we-are-excited-to-announce-that-the-call-activity-7252200348830842882-t6L1/), [Mastodon](https://mastodonczech.cz/@honzajavorek/113334985407404155). Zkusil jsem taky oslovit Apify, zda by nechtěli PyCon NA sponzorovat a poslat tam někoho, aby ukázal, jak se dá přes [Apify Store](https://apify.com/store) se základní znalostí programování vydělávat. Jsem zvědav, jak to dopadne.
- V souvislosti s prací na srazech v klubu jsem zjistil, že se nějak rozbily i srazy na python.cz a rovnou [jsem to opravil](https://github.com/pyvec/python.cz/pull/582).
- Navrhl jsem _Open Tables_ jako možnou aktivitu pro pražská Pyva.

![Open Tables]({static}/images/screenshot-2024-10-19-at-16-38-33.png)

## Další

-   Ještě než doma všichni omarodili, stihl jsem [sepsat report z půlmaratonu](https://gici.behaj.cz/pmk/) a pak si plný dojmů zaběhat s kamarádem, kterého jsme nakonec i přijali do našeho běžeckého klubu. Stihl jsem obědové rande se svou ženou a dal jsem si tam ořechový čaj. Stihl jsem zajít s jiným kamarádem na [Substance](https://www.csfd.cz/film/1479706-substance/) a mít z toho smíšené pocity.
-   Zkusil jsem na junior.guru zase jiný setup pro Dependabot. Určitě jednou najdu takový, který mě nebude štvát.
-   Koukal jsem na [Hall](https://usehall.com/), který zjevně Apify používá na to, aby diskuze z Discordu šly vidět „ven“ jako fórum, které jde najít přes Google, a kde mohou reagovat i lidé, kteří na Discordu nejsou. Ale jednak to není open source (takže mi to nic neřeší), jednak lze na limity zjevně narazit dost brzo - např. [tady jsem udělal odkaz na jiný příspěvek](https://apify.hall.community/crawlee-for-python-forum-XWWr90RY1tDY/usingproxieswithplaywrightandbestproxyserviceproviders-02nm29tc7shq) a smůla.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Vyměnil jsem admina skupinového předplatného Red Hatu. Udělil jsem jedno stipendium.
-   Za 16 dní jsem naběhal 20 km, při procházkách nachodil 31 km. Celkem jsem se hýbal 16 h a zdolal při tom 51 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

Plánuji si teď odpočinout, když mám babičku za zády, a potom se uvidí. Asi budu dělat ty srazy.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [The Future of ArchiveBox - HedgeDoc](https://docs.sweeting.me/s/archivebox-plugin-ecosystem-announcement)<br>Tohle vypadá zajímavě. Už nějakou dobu si leckterý online obsah raději stahuju offline, kdyby náhodou zmizel (např. přes yt-dlp). ArchiveBox je další level.
- [The Static Site Paradox](https://kristoff.it/blog/static-site-paradox/)<br>„The more we make the web complex, the more we push normal users into the enclosures that we like to call social networks.“
- [Real or Fake? The AI Deepfake Game](https://leonfurze.com/deepfake-game/)<br>Kolik máte? Já 9/10. Generuju AI obrázky jako hobby, takže vím, na co se dívat. Většina byla fakt jednoduchých a odpověď jsem věděl do pár sekund, nebo jsem minimálně tušil a už jen hledal detaily, které mi doměnku potvrdí.
- [Snadná je únava z války, která probíhá jinde – Page Not Found](https://pagenotfound.cz/clanek/snadna-je-unava-z-valky-ktera-probiha-jinde)<br>„To, co vnímáme jako "únavu z války" na Západě, je ve skutečnosti odrazem našich privilegovaných pozic. Máme možnost se od války distancovat, vypnout zprávy, odložit telefon. Ale pro ty, kteří žijí ve válčící zemi, to není možnost. I oni by si rádi šli ve dvě ráno pro pizzu, viděli své otce, bratry nebo sestry častěji než jednou za půl roku. Viděli je naživo a živé, ne jen četli zprávu “+“ na otázku, jestli jsou na frontě v pořádku.“
- [Video scraping: extracting JSON data from a 35 second screen capture for less than 1/10th of a cent](https://simonwillison.net/2024/Oct/17/video-scraping/#atom-entries)<br>Tohle je bomba. Nahraju si video své obrazovky, jak proklikávám věci, to hodím do LLM a z něj vypadne JSON export těch věcí.
- [Using Cloudflare on your website could be blocking RSS users - Open RSS](https://openrss.org/blog/using-cloudflare-on-your-website-could-be-blocking-rss-users)<br>Přesně tohle se mi už několikrát stalo. A jako člověk, který běžně i pro vlastní potřebu chce sem tam něco malého scrapnout, třeba program kina apod., tak upřímně Cloudflare jednoduše nenávidím — a ve jménu pravidla nedělám jiným, co sám nemám rád, nikdy bych si ho na svůj web nedal.
- [The Inevitability of Mixing Open Source and Money](https://lucumr.pocoo.org/2024/10/14/mixing-oss-and-money/)<br>„WordPress by all accounts is a massive success. WordPress is in the top 1% of open source projects in terms of impact, success, and financial return for its creator. Yet despite that — and it finding an actual business model to commercialize it — its creator suffers from the same fate as many small Open Source libraries: a feeling of being wronged.“
- [Age of Invention: The Coal Conquest](https://www.ageofinvention.xyz/p/age-of-invention-the-coal-conquest)<br>Kupodivu uhlí nepřišlo jako řešení deforestace, ale bylo její příčinou. Dřeva bylo dost a byl to obnovitelný zdroj, ale když zlevnilo uhlí, lidi lesy vykáceli.
- [Praha má 1 017 457 parkovacích míst, spočítal architekt. O moc více jich už nevznikne - Zdopravy.cz](https://zdopravy.cz/praha-ma-1-017-457-parkovacich-mist-spocital-architekt-o-moc-vice-jich-uz-nevznikne-223927/)<br>„Na každého obyvatele hlavního města, včetně 220 000 dětí do 14 let, 250 000 seniorů nad 65 let, 35 procent pražských domácností bez jediného auta a 65 procent pražských domácností s 1,2 autem, tak připadá jen ve veřejném prostoru, bez garáží a soukromých stání u rodinných domů, 0,73 parkovacího místa – devět metrů prostoru.“
- [Point Nemo, the Most Remote Place in the World](https://www.theatlantic.com/magazine/archive/2024/11/point-nemo-most-remote-place/679947/)<br>„If you are on a boat at Point Nemo, the closest human beings will likely be the astronauts aboard the International Space Station; it periodically passes directly above, at an altitude of about 250 miles. When their paths crossed at Point Nemo, the ISS astronauts and the sailors aboard the Mālama exchanged messages.“ „The three islands define a circle of ocean larger than the old Soviet Union. Point Nemo, at the center, lies 1,670.4 miles from each vertex.“
- [Pod čarou: Fotky nikdy nebyly realita. AI na tom nic nemění.](https://seznam-zpravy.u.mailkit.eu/mc/VECQVPVC/GLSTEGBNFXFOJUKKCG/VQCUIPVUIWE)<br>„I ‚opravdová‘ fotka vlepená do rodinného alba je vždy nevyhnutelně jen stylizovaný výsek reality, který jsme se rozhodli zachytit (a jiné vynechat).“ „…fotografie přestala existovat jako svébytné médium s technologickou definicí (obraz vznikající dopadem světla na film nebo čip) a stává se z ní spíše jen estetický styl obrazu, tedy něco jako ‚obrazy připomínající výstupy z analogových či digitálních fotoaparátů‘.”
- [Roman Týc](https://www.facebook.com/roman.tyc.3/posts/deset-let-paraleln%C3%AD-polisjako-soci%C3%A1ln%C3%AD-experiment-deset-let-mysl%C3%ADm-sta%C4%8Dilo-te%C4%8F-j/10226850475312760/)<br>Jednostranná výpověď o Paralelní Polis, bohužel jako dlouhý status na zcela nedecentralizované a neotevřené síti Facebook. Proklikat se tam lze ke čtení i bez účtu, kopírovat text na mobilu nelze, takže tentokrát bez citace zajímavých pasáží. Bylo zajímavé číst o tom, že PP nerovná se Bitcoin a kryptoměny, protože jako laik jsem si to samozřejmě myslel. Nejlepší věta je asi ta, že ekosystém kryptoměn není letadlo, ale všichni ho tak dnes používají.
- [Breaking Down OnlyFans’ Stunning Economics — MatthewBall.co](https://www.matthewball.co/all/fansprofitandloss)<br>„It is probably the most successful UK company founded since DeepMind in 2010, and the most significant media platform founded since TikTok (via Musical.ly in 2014), and dedicated creator economy platform… ever“ „In 2024, OnlyFans generated $6.3 billion in gross revenues, up from $300 million five years earlier.“ Tvůrkyně a tvůrci na OnlyFans kolektivně vydělají víc než v součtu všichni hráči NBA nebo Premier League. Firma má 42 zaměstnanců.
- [Chagos Islanders confront their postcolonial future](https://continent.substack.com/p/chagos-islanders-confront-their-postcolonial)<br>Pokud vás zajímá něco o ostrovech Chagos, které doménu .io mají, čtěte @thecontinent: „The fading imperial power leased one of the islands, Diego Garcia, to the United States for a military base. Its inhabitants were brutally evicted and dumped in Mauritius and the Seychelles, with little more than the bags they could carry. They were never allowed to return…“ A na osud ostrovů se původních obyvatel nikdo neptá.
- [The Disappearance of an Internet Domain](https://every.to/p/the-disappearance-of-an-internet-domain)<br>Doména .io s největší pravděpodobností zanikne. Až si příště budete registrovat doménu státu, o kterém nic nevíte, vzpomeňte si na „to neděláš dobře s těma sirkama, Jaromíre“. Pamatujeme bit.ly a válku v Lybii, že?
- [Katastrofa se nekoná. Karviná se chystá na život po uhlí – Page Not Found](https://pagenotfound.cz/clanek/katastrofa-se-nekona-karvina-se-chysta-na-zivot-po-uhli)<br>Jako původně Karviňák oceňuju tuhle reportáž o tom, jak to ve městě vypadá dnes. Super fotky, super průřez vším, co se tam děje. Díky!
- [V policejních datech chybí 90 procent nehod cyklistů, říká výzkumník Šindelář — Dataři](https://www.mujrozhlas.cz/rapi/view/episode/aa369143-284e-39bd-a359-0f1d730ca79a)<br>Super zajímavá epizoda o zkreslení policejních statistik ohledně nehod cyklistů. Wow.
- [Amusing Ourselves to Death by Stuart McMillen - cartoon Recombinant Records](https://web.archive.org/web/20100111052839/http://www.recombinantrecords.net/docs/2009-05-Amusing-Ourselves-to-Death.html)<br>Huxley vs. Orwell
