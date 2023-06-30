Title: Týdenní poznámky: Smršť v klubu a programování lepšího týdenního shrnutí
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/234

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-06-23_tydenni-poznamky-optimalizace-obrazku-a-jamiroquai.md) už utekl nějaký ten týden (23. 6. až 30. 6.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Smršť v klubu

Chtěl jsem konečně najet na režim, kdy ráno vstanu na budík, dám si rychlou snídani, odejdu do kanceláře a pracuju.
Tak jsem vstal na budík, ale najednou vidím, že mi píše moderátor, že se v klubu něco děje.
Tak to nějak řeším a stojím doma s mobilem jak trubka, snídám v deset, do kanceláře jdu kdo ví kdy.
No nic.

V klubu se zvrhla nějaká původně nevinná diskuze, protože se někomu nelíbilo, že mu opravili překlep, a někomu dalšímu se pak nelíbilo, že ten první člověk po sobě smazal všechny příspěvky.
Vyjádřil to trochu zpruzeně a to se zase nelíbilo některým moderátorům (třeba mně), tak jsme ho začali mírnit.
To vyústilo ve velkou diskuzi, zda by měli moderátoři lidem chodit za zadkem, zda to neodrazuje přispívání do klubu, zda a jak dosáhnout _[psychological safety](https://en.wikipedia.org/wiki/Psychological_safety)_, apod.
Jak by řekli Cimrmani, „udělal si klub a chodili mu tam lidi“.

Řešili jsme to celý den a ještě i kousek dalšího dne.
Já v tom nějaké velké emoce nemám, byť mě to místy už moc nebavilo a trochu mě mrzelo, že jsem měl konečně čas něco pro klub udělat, ale místo toho jsem se tam motal v těchto diskuzích.

Ten člověk, kterému opravili překlep, se rozhodl z klubu odejít.
Nabídl jsem mu vrácení peněz, ale odmítl to.
Moderování v klubu jsme nějak probrali a mám z toho _takeaways_ ohledně toho, jak chceme k podobným situacím do budoucna přistupovat.

![This is fine]({static}/images/this-is-fine-meme-218964059.jpg)

## Změny v klubu

Řekl jsem si, že klub by si po delší době zasloužil nějakou lásku a šel jsem vymetat pavučiny a přesunovat regály.

-   Poladil jsem [Discordí onborading](https://support.discord.com/hc/en-us/articles/10394859532823) do klubu a tzv. _Server Guide_.
    Zajímavá funkce.
    Měl jsem tam jeden zásek, kdy jsem dokonce napsal na support, ale nakonec se mi to povedlo opravit samotnému.
-   Zrušil jsem zprávu, která v uvítacích vláknech vybízela k networkingu formou hry: „Napiš o sobě tři krátké věty. Dvě pravdy a jednu lež. Ostatní můžou hádat, co z toho není pravda 😎“
    Nefungovalo to, nikdo na to nereagoval.
    Když to napíše bot, asi to působí neosobně.
-   Místo toho jsem přidal zmínku o tom, že lidi mohou své představení dodatečně upravit nebo rozšířit přes editaci příspěvku.
-   Bot v klubu zdraví sám sebe.
    Opravil jsem to, akorát že vůbec.
    Zjevně mi někde něco uniká.
-   Vytvořil jsem speciální kanál na týdenní plánování.
    Ještě chci automatizovat zakládání nových vláken každé pondělí.
    Udělal jsem i dobrovolnou roli pro lidi, kteří se chtějí tohoto rituálu účastnit.
    Rituál zavedl jeden z aktivních moderátorů a nejdřív to celé dělal ručně v rámci existujících kanálů.
    Celkem se to osvědčilo, tak pracuji na tom, abych to institucionalizoval.
    Super, že něco takového vzniklo odspoda!
-   Kanál na CVčka a na výrobky jsem konečně převedl na typ „fórum“.
    Do budoucna si dovedu představit je ještě vylepšit pomocí drobné automatizace.

## Lepší týdenní shrnutí

Bot každý týden do klubu posílá shrnutí, kde jsou nejlepší příspěvky za poslední týden.
Jednak jsem v něm chtěl udělat pár drobných úprav, jednak jsem tam chtěl přidat i kanály, kde se nejvíc diskutovalo.
Přijde mi totiž, že některé zajímavé diskuze ve vláknech prostě pro spoustu lidí zapadnou.

![Týdenní přehled]({static}/images/screenshot-2023-06-30-at-20-02-19.png)

Data mám v databázi, takže šlo jen o to je správně dostat ven přes Peewee, otestovat to, nějak to zobrazit na Discordu.
Nebere se v úvahu kolik se napsalo příspěvků, ale kolik se celkem napsalo písmenek.

Když jsem se snažil přehled zobrazit, přišlo mi, že je to takové prázdné a přemýšlel jsem, jakou informaci tam ještě dát.
Počet znaků mi nepřišel užitečný, ale pak mě napadlo odhadnout tam dobu čtení.
Jenže všechny vzorce na dobu čtení se počítají ze slov a já mám v databázi jen počet znaků.
Všiml jsem si ale, že [normostrana](https://cs.wikipedia.org/wiki/Normostrana) má údaj kolik je to přibližně slov.
Díky tomu jsem dokázal vypočítat přibližnou dobu čtení i z počtu znaků.

V přehledu nej zpráv se zobrazuje i kousek z textu každé zprávy.
Jedno z malých neviditelných vylepšení, které jsem udělal, bylo očištění tohoto textu.
To se doteď nedělo, takže pokud tam bylo nějaké formátování nebo nové řádky, do shrnutí se to projevilo.

Pojal jsem to tak, že jsem text příspěvku protáhl přes Markdown parser, tím jsem dostal HTML, a toto HTML jsem zbavil tagů.
Očištění o tagy není úplně triviální záležitost, když člověk chce podchytit všechny chytáky, ale měl jsem na to už hotovou funkci z dob, kdy jsem dělal bota na pracovní nabídky.
Zjistil jsem však, že tato funkce nefunguje a plodí nesmysly.
Pak jsem zjistil, že ta funkce nemá testy.
A když jsem ji opravil, tak jsem zjistil, že najednou bot do Discordu nasypal asi 10 nových pracovních nabídek 😱
Raději nechci vědět, jak dlouho to bylo rozbité a jestli kvůli tomu bot náhodou nezahazoval hromady použitelných nabídek práce…

Pozitivní je, že jak čas čtení, tak opravu funkce na očištění HTML tagů jsem měl docela rychle díky tomu, že jsem se podobnými věcmi zabýval už tady na blogu.
Potěší, že jsem znovupoužil něco, co jsem myslel, že dělám jen pro radost a nikdy žádný větší užitek mít nebude.

Jo a taky jsem zjistil, že bot při vyhodnocování „karmy“ jednotlivých příspěvků nepočítal emoji 💪 jako pozitivní reakci, přičemž tato je jedna z nejpoužívanějších v klubu.
Nevím, jak mi to mohlo uniknout.
Docela to pak zamíchalo s pořadím týdenního přehledu a kdo ví, možná i s karmou různých lidí v klubu…

![This is fine]({static}/images/this-is-fine-meme-218964059.jpg)

## Pokusy o naládování IRL srazů do klubu

Mám v plánu, že by bot sledoval srazy vybraných komunit a zakládal pro ně v klubu Discord eventy, aby si jich členové všimli.
Taky pak půjde vidět, kolik lidí z klubu se tam chystá.
Za junior.guru neplánuju dělat žádné IRL akce, chci aby se junioři mísili s ostatními na již existujících srazech.
A aby se tam potkávali ti lidi z klubu, kteří mohou a chtějí.

Zdánlivě jednoduchý plán.
Prostě nasosám iCalendar exporty z meetup.com a pyvo.cz, nějak to v Pythonu přechroustám a vytvořím příslušné akce.

Jenže z meetup.com se, zatímco jsem pár let nedával pozor, stala _walled garden_!
Jako ze všeho na dnešním internetu.
Už mě to fakt štve.

[Tady to pěkně popsal](https://wordpress.org/support/topic/trouble-with-meetup-calendars-please-read/) autor nějakého WordPress pluginu.
Odkazy na iCalendar existují, ale nefungují.
Tedy fungují, ale jen pro přihlášeného uživatele, což je ale úplně k ničemu, protože s tím si žádný software na kalendáře neporadí.
Odkazy na RSS nebo Atom pro jistotu nefungují vůbec.

Našel jsem, že [meetup.com má API](https://www.meetup.com/api/).
Pohled do dokumentace na nějaké šílené [JWT Flow](https://www.meetup.com/api/authentication/#p04-jwt-flow-section) mě sice vyděsil, ale říkal jsem si, že by mi s tím snad nějak ChatGPT pomohlo a že bych měl být především rád, že to jde vůbec použít bez interakce s uživatelem.
To bývá velký problém u všech API založených na OAuth a znemožňuje to jejich použití v samostatně běžících skriptech.
Jelikož tvořím jen samostatně běžící skripty, taková API nenávidím.

Nuže jal jsem se založit si tam appku, přes kterou dostanu přístupy atd. a kroutil jsem hlavou, že prostě nemůžu použít normálně ten iCalendar a musím se trápit s nějakým API.
Ale po založení appky se u ní objevilo _pending_ a musel jsem čekat.
A druhý den mi přišlo mailem, že to zamítli, protože si nejdřív mám platit meetup.com přes nějaké jejich Meetup Pro!
No tak to se už úplně po…

Tolik práce a přitom taková blbost!
Nechť všechny _walled gardens_ dnešního internetu shoří v pekle!

Vytáhl jsem tedy [Playwright](https://playwright.dev/python/) a napsal jsem pár řádků, které se přihlásí do meetup.com a stáhnou ten iCalendar.
Dalo mi zabrat udělat to stahování, ale povedlo se.
Udělal jsem si na to separátní účet, aby mi případně nezablokovali můj.
To taky nebylo hned, nebyli mi schopni ani doručit ověřovací e-mail.
Povedlo se mi založit nový účet až napotřetí, s e-mailem na doméně @centrum.cz.

Nakonec se mi povedlo opravdu vytvořit skript, který se přihlásí na meetup.com a stáhne dva iCalendar soubory s exportem událostí pro Frontendisty a React Girls srazy.
Když mi to fungovalo, ještě párkrát jsem to pustil a stránka s iCalendar exportem začala vracet HTTP 500, chyba serveru.
V tu chvíli jsem to vzdal a uvidím, jak a kdy budu v tomto úkolu pokračovat.

![This is fine]({static}/images/this-is-fine-meme-218964059.jpg)

## Optimalizace buildu

-   Opravil jsem fungování cache na CircleCI.
    Ještě to má nějaké mouchy, ale najednou mi začaly fungovat věci, které byly dlouho rozbité a nevěděl jsem proč.
    Řešení bylo prohodit tři řádky v YAMLu.
-   Protože začala fungovat cache, zjistil jsem, že potřebuji mergovat různé verze různých souborů.
    Soubory ze `.scrapy` cache jsem se rozhodl nějak neřešit.
    Soubory s daty scraperů nabídek práce bych ale i celkem řešil.
    Naprogramoval jsem slučování `.jsonl.gz` souborů, ale je to pomalé a ještě to ladím.
    A možná bych to taky mohl přeskočit, ještě to musím promyslet, zda nedělám zas nějaké zbytečné věci.
-   Opravil jsem cesty k `og:image` obrázkům a ověřil, že to jede.
-   Dal jsem formátování kódu do separátního plánovaného buildu, který se spustí jednou denně v noci.
    Předtím to bylo po každém `git push` a to bylo otravné.
    Navíc vznikaly konflikty, pokud tentýž build chtěl formátovat kód a zároveň zapsat nějaká data v souborech zpět do gitu.
-   Mentální poznámka: Až budu zas někdy řešit optimalizaci PNG, měl bych použít jak pngquant, tak oxipng.
    Podle [komentáře autora pngquant](https://github.com/kornelski/pngquant/issues/386#issuecomment-952899561) dělá totiž každý něco jiného.

## Další

-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
    Konečně jsem prošel většinu nahromaděných restů a shodil ze sebe stres z toho, jak věci celý červen akorát hrnu před sebou.
-   Zašel jsem si do kina na [Asteroid City](https://www.seznamzpravy.cz/clanek/kultura-reziser-z-instagramu-filmy-wese-andersona-jsou-chytrejsi-nez-se-zda-232961).
    Do [nejlepšího kina](https://www.kinoaero.cz/).
-   Na správu účtů používám Memberful.
    Tam je super funkce referalů, tzn. slev pro lidi, kteří doporučí další lidi.
    Jenže doteď to nešlo použít dohromady s kupóny, které používám fakt hodně.
    A odteď už to prý jde!

    > Member referrals is one of the most effective ways to grow your membership business. With this latest update, your members can enjoy the perks of both referral-earned discounts and promotional coupons at the same time!

    Takže jsem si udělal poznámku, že bych mohl nějaký referal program zavést.

-   Četl jsem si, [jak LinkedIn změnil algoritmus](https://www.entrepreneur.com/science-technology/linkedin-changed-its-algorithms-heres-how-your-posts/454728).
-   Zkusil jsem přes [Whisky](https://github.com/IsaacMarovitz/Whisky) nainstalovat [Original War](https://en.wikipedia.org/wiki/Original_War), ale nešlo mi to.
    Zkusím to ještě znovu, až budu mít někdy zase čas.
-   Dělal jsem review jednomu textu, který má vyjít na základě rozhovoru se mnou.
-   Prošel jsem si sloupec v Trellu s různými úkoly a pročistil jej.
    Smazal jsem věci, které už nejsou relevantní, nebo jsou dávno hotové.
-   Zablokoval jsem v botovi další firmu, která spamuje LinkedIn pozicemi každý den opakovaně otevíranými a rušenými.
-   Zaplatil jsem poprvé nájem za kancelář a upravil jsem svoje skripty, aby tyto platby uměly rozpoznat a v grafech obarvit odlišeně.
-   Četl jsem si, jak Discord maká na [server subscriptions](https://discord.com/blog/server-subscriptions-updates-media-channels-tier-templates-and-more) a je to hustý.
    Jestli tohle dotáhnou, udělají velkou čáru přes rozpočet všem patreonům, herohero, pickey, apod.
    Je to teda zatím jen pro USA, pokud vím.
-   Tinuki dotáhl stříhání záznamu přednášky s Nelou a máme z toho [toto veřejné video](https://youtu.be/FIijszEVQHY).
-   Domluvil jsem na pondělí call s ENGETO Academy, kterým bude končit partnerství.
    Navíc nám vypadla kamarádka, která nám měla pomoci s dotažením ankety mezi juniory, tak to budeme muset nějak vyřešit.
-   Během 8 dní jsem ujel na kole 17 km. Celkem jsem se hýbal 4 h a zdolal při tom 17 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Naprogramovat ještě nějaká vylepšení pro klubového bota.
2.  Opravit [/open/](https://junior.guru/open/), pokud to nějak půjde.
3.  Nějak uzavřít překopávání toho, jak se buildí frontend junior.guru.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Jak zmáknout novou dovednost — TVŮRCAST](https://podcasters.spotify.com/pod/show/pickey/episodes/Jak-zmknout-novou-dovednost-e25sdvf)<br>Sice pro tvůrce, ale jsou tam dobré tipy vlastně pro kohokoliv, kdo se učí něco nového: „Bez toho, abyste si na zahrádce ušpinili ruce nikdy nic nevypěstujete!“
- [Konečně vydali pravdu o dezinformacích](https://www.mediar.cz/konecne-vydali-pravdu-o-dezinformacich/)<br>„Západ a Východ, demokracie a autoritářství, budoucnost a minulost, rozum a emoce, my a oni – ospravedlní jakékoliv prostředky, současně celý problém dezinformací i jednoduše vysvětlí. Příběh Česka, kterému hrozí únos ze Západu, všichni známe. Někteří politici i novináři skrze něj vysvětlují téměř každé volby. V delikátních otázkách pravdy a faktů převládl přístup, ve kterém bojuje dobro a zlo. Práce Alexandry Alvarové, Evropských hodnot či Českých elfů má ovšem velké slabiny.“
- [AskHistorians Podcast Episode 208 - Pirates and Public History with Rebecca Simon — The AskHistorians Podcast](https://askhistorians.libsyn.com/askhistorians-podcast-episode-208-pirates-and-public-history-with-rebecca-simon)<br>Máte rádi piráty? Pásky přes oči, zakopané poklady, papoušci na rameni, černé vlajky? A víte, jak to bylo doopravdy? A proč máme vlastně piráty dneska rádi?
