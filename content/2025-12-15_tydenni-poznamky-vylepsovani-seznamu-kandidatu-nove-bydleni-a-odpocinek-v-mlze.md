Title: Týdenní poznámky: Vylepšování seznamu kandidátů, nové bydlení a odpočinek v mlze
Image: images/img-9653.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 13 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/368
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115724215303822568

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-11-28_tydenni-poznamky-konecne-hotovy-kurz-knedlik-v-krku-a-klubove-akce.md) už utekl nějaký ten týden (28. 11. až 15. 12.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![les]({static}/images/img-9653.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Kamarád mě zrovna chválil, že prý si všiml, jak teď ty poznámky píšu fakt pravidelně. Takže teď tedy pro změnu zas po víc než dvou týdnech 🥲 A myslím si, že další budu psát až po Vánocích, tak si to užijte. Dneska to má hodně obrázků!

## Práce na „candidates“

Nedal jsem [junior.guru/candidates](https://junior.guru/candidates) tolik, kolik jsem chtěl, ale prostě teď byly jiné životní priority.

Přidal jsem _badges_, které se u kandidátů vypisují, když můžu z jejich klubové aktivity něco vyvodit. Například „dobře komunikuje na dálku“ (pokud dost komunikuje na Discordu), „nebojí se zpětné vazby” (pokud má vlákno na feedback k CVčku nebo výtvorům) apod. Zapracoval jsem pak feedback od lidí z klubu na celou tu stránku a ladil jsem design těch badges.

Implementoval jsem i vysvětlující _tooltipy_ nad badges. Sice existuje HTML atribut `title`, ale podle mě není moc uživatelsky přívětivý a na mobilu se myslím nezobrazuje vůbec. Bootstrap na tooltipy [přímo něco má](https://getbootstrap.com/docs/5.3/components/tooltips/), ale zdálo se mi, že to je zastaralý a zbytečně složitý přístup plný JavaScriptu. Tak že to udělám nějak jen přes HTML a CSS, protože už existuje [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API). Jenže až když jsem si s tím s pomocí LLM hrál půl dne, tak jsem zjistil, že Popover je na něco trochu jiného a aby to fungovalo jako tooltip, který se zobrazuje u prvku, je potřeba i [anchor positioning](https://developer.chrome.com/blog/introducing-popover-api#anchor_positioning). Zatímco Popover funguje všude, tak anchor positioning rozhodně ne. Takže jsem s tím akorát ztratil čas a nakonec jsem stejně použil ten Bootstrap.

![kandidáti]({static}/images/screenshot-2025-12-15-at-12-54-35.png){: .img-thumbnail }

Taky jsem upravil pořadí kandidátů na stránce tak, aby v rámci jedné kategorie jejich další řazení nebylo podle abecedy, ale náhodné. A upravil jsem texty v `title` tagu stránky a na náhledovém obrázku pro sociální sítě.

Pak jsem chtěl na stránku přidat to nejdůležitější: Odprezentovat v co nejlepším světle u každého kandidáta jejich projekty. Jenže jsem narazil na to, že tuhle věc ještě nemám dobře pokrytou ani v [hen](https://github.com/juniorguru/hen), automatické kontrole profilů, ani v [příručce](https://junior.guru/handbook/). Do toho jsem si všiml i nějakých chyb v tom, co moje nástroje zjišťují o kandidátech – některé projekty se vypisovaly dvakrát, některé se nevypisovaly vůbec.

Tak jsem opravil bugy a přidal nová pravidla, která se týkají projektů. Nově automaticky kontroluju, jestli živá ukázka projektu vrací chybu, nebo se načte, nebo jestli není README příliš krátké. Dovedu si představit podrobnější analýzu README nebo kódu projektu, ale to si nechám na jindy. Doplnil jsem kód, který v README detekuje obrázky (typicky screenshoty) a vrátí mi jejich adresy – toto se mi bude hodit ve výpisu kandidátů. Tímhle vším jsem si trochu připravil backend.

Potom ještě návod. Pokud chci juniorům mlátit o hlavu nějaké nedostatky v projektech, potřebuju je odkázat na text, který jim vysvětlí, jak to má být správně. Tak je to se [stránkou o GitHub profilu](https://junior.guru/handbook/github-profile/), ale tam není nic do detailu o projektech. K tomu má sloužit [tahle stránka](https://junior.guru/handbook/projects/). Takže jsem šel a jeden celý den jsem se probíral poznámkami, které jsem si během let k této stránce ukládal, a uspořádal jsem si je pod budoucí strukturu nadpisů, podobně jako u [komiksové diplomky](https://www.herout.net/blog/2013/03/diplomka-comics-edition/). Dalo to strašnou práci a zatím to není nikde vidět, tak mi musíte akorát věřit 😀 Tento týden bych se na to chtěl vrhnout a začít psát jednotlivé kapitoly. Dejte vědět, pokud si myslíte, že by tam něco nemělo chybět!

![nový náhledový obrázek]({static}/images/c5145ce0d0f4a0d1f9a9b10f98525f1adeb1f10ebf5bc94c77e262babc3345ba.png){: .img-thumbnail }

## Přednáška s Irenou Zatloukalovou

Irčinu přednášku jsem [propagoval na LinkedInu](https://www.linkedin.com/posts/honzajavorek_junio%C5%99i-b%C3%BDvaj%C3%AD-z-program%C3%A1torsk%C3%BDch-sraz%C5%AF-activity-7404070883289567232-deFm/?rcm=ACoAAACB93ABHHj4UI2winetGMZHboHlZIZojJA) a [Mastodonu](https://mastodonczech.cz/@honzajavorek/115688655246741669). Na tom LI to mělo docela velký ohlas a mám pocit, že mě díky tomu začalo sledovat snad 10 nových lidí. Irča má zjevně fakt velký dosah 😀 4.000+ impresí, 80+ lajků, 20+ komentářů.

Na přednášku přišlo 18 lidí, což mi udělalo velkou radost. Menší radost mi udělalo, že se zase dost nepovedl začátek. Nahrávání mi zajišťoval Dan, protože Patrik nemohl. Dana jsem neuháněl s předstihem, takže si začal vše nastavovat až v čase přednášky. Až to nastavil, tak jsme zase zjistili, že se Ireně pokazil Discord a nedaří se jí připojit na call. Technické potíže byly i s Janem Meissnerem, i s Evou Pavlíkovou, a už se z toho stává nemilé pravidlo. Přemýšlím, co s tím můžu dělat.

S Discordem a jeho kvalitou poskytovaných služeb bohužel mnoho nenadělám. Můžu přednášky dělat mimo Discord, ale nelíbí se mi to, z mnoha důvodů. Líbí se mi synergie speakerů pozvaných do klubu a toho, že lidem v klubu stačí kliknout a připojí se. Pokud by to však takto pokračovalo, možná bych to prostě musel přesunout jinam 😞

Další věc je, že Patrik má méně času než dřív a Dan je vlastně jen záloha. Nemůžu se na něj ani moc zlobit, protože to pro mě dělá jen z dobrého srdce. Pokud byste někdo měli zájem nahrávat pro junior.guru klubové akce přes OBS, ozvěte se mi.

Přednáška samotná byla skvělá. Publikum interagovalo, téma to bylo zajímavé a relevantní, lidi přišli, Irča měla dobré tipy, následná diskuze byla super.

Nahráli jsme všechno – včetně všech prostojů, takže to před vydáním ještě sestříhám. To jsem ještě neudělal, takže nahrané to sice je, ale ještě to není upravené a publikované.

![Irča]({static}/images/20251210-b6a735b5fdf45f237e6d4011e0537e870991bbfe42715a3b360318def33bb73d.png){: .img-thumbnail }

## Newsletter

Vydal jsem druhý newsletter junior.guru. Nechal jsem systém vygenerovat asi 5 různých vydání, z nichž jsem si vybral to, kde jsou AI souhrny nejmíň blbé a co nejvíc užitečné. To jsem se pak snažil poslat.

Což mi teda editor Buttondownu znesnadňoval, protože se zjevně nějak neumí poprat s tím, že mu tam do API posílám ten newsletter v Markdownu, nebo nevím. Prostě to tam nějak divně zpracovávají a pak stačí dát kurzor do editoru a celé se to podělá. Což je blbý, protože celá myšlenka za tímhle byla, že si udělám přes API automaticky drafty a ty nejen zkontroluju, ale případně i ručně upravím, a pak pošlu. Takže je dost blbý když do toho šáhnu a nenávratně se to pokazí. Nepsal jsem na support proč se to děje, nebyl čas.

Pak jsem zjistil, že z jejich API může přijít formát newsletteru jak v Markdownu, tak v HTML, a že můj archivační skript s tím nepočítá. Takže se rozbilo formátování v archivu. To jsem nějak opravil, ale tyjo…

Takže archiv čísla [je na webu](https://junior.guru/news/listopad-2025-ve-svete-it-junioru-1883/) a když byl připravený, použil jsem svoje udělátko, které jej překopírovalo na LinkedIn jako článek. U toho jsem si všiml, že to udělátko mi poslalo minulé týdenní poznámky z blogu na LinkedIn jako by to byl junior.guru newsletter 🤦‍♂️ Možná jsem tam vůbec neměl dělat dva „newslettery“ a měl jsem to publikovat jako jednu věc, ale co už.

A myslím, že při tom kopírování tam zase neprošlo všechno a nějak se tam popletly nadpisy. Je to zabugované, ale nemám náladu to ladit a hrabat se v tom. Už to vidím, že jak budu na LinkedIn dávat tenhle článek z blogu, tak to zase zapomene překopírovat půlku obrázků a kdo ví co dalšího. Třeba to někdy opravím, ale teď jsem na to neměl ani čas, ani náladu.

Kdo chce nepokažené verze newsletteru a blogu, nechť jde na web, LinkedIn je peklo. Aspoň na Mastodon se to tentokrát [vypublikovalo dobře](https://mastodonczech.cz/@honzajavorek/115670772379564370).

![newsletter]({static}/images/screenshot-2025-12-15-at-15-48-34-listopad-2025-ve-svete-it-junioru.png){: .img-thumbnail }

## Bydlení

Naše shánění nového bydlení v posledních dvou týdnech gradovalo. Bylo kolem toho hodně stresujícího běhání a zařizování, notáři, CzechPointy, a tak nějak všechno možné, s různými záseky a těsně stihnutými termíny.

Hodně úsilí jsem strávil výběrem pojištění. PDFka jsem natlačil do ChatGPT i Gemini a strávil nad tím několik dní, abych vychytal všechny háčky a dostal se na srovnatelné nabídky od různých poskytovatelů, ale stejně mám nakonec pocit, že platím drahé pojištění 😀 Pojištění se asi nedá vyhrát. Už to neřeším a za rok zkusím sehnat lepší.

Do vybírání pojištění se mi vůbec nechtělo, protože jsem tomu nerozuměl a přišlo mi to jako past vedle pasti. Když jsem to protáhl přes LLMka, tak mě to ale začalo dost bavit. LLMka všechno vysvětlily a pohlídaly. I když mi teda nakonec přišlo, že ze screenshotů těch PDFek četly ty složité tabulky mnohem lépe, než ze samotných PDFek.

Jenže pak jsem zjistil, že podmínky pojišťoven mě stejně nepustí udělat nic jiného, než to, co chtějí pojišťovny, a to už mě pak zase bavit přestalo. Nakonec jsem s tím celým strávil neúměrně zbytečně mnoho času na to, kolik to je ve výsledku peněz.

Ještě nemáme úplně dobojováno, ale to hlavní je snad za námi. Prozradím už jen to, že zůstáváme na Praze 3. Bohužel už ne na dolním Žižkově, kde to máme nejraději, ale chce se mi věřit, že i nové místo si oblíbíme a budeme to tam mít rádi.

![mapa]({static}/images/screenshot-2025-12-15-at-12-59-55.png)

## Advent

Vytvořil jsem pro dceru adventní kalendář. Koupil jsem 25 obálek (zhruba A5) a dal do nich různé drobné dárečky, většinou blbinky z papírnictví. Obálky jsou lepší než loňské svačinové pytlíky. Ty byly příliš průhledné a musel jsem použít vždy dva v sobě. Taky jsou větší. Dcera si kalendář zatím dost užívá.

Dělal jsem doma vánoční výzdobu, připravil slané vafle, na pánvičce udělal improvizované fajitas, zdobil s holkama perníčky.

Šli jsme se podívat na rozsvícení vánočního stromu na náměstí na Praze 3 s mobilní zvonkohrou a omkrnout trochu trhy a potom jsme byli i na rozsvícení stromečku ve školce, tam se i zpívalo.

Dcera si užila Mikuláše a namalovala několik srandovních, roztomilých, nebo i naprosto děsivých čertů. Udělali jsme si prima víkendovou procházku po Vítkově a prozkoumali místní novou kavárnu.

![adventní kalendář v obálkách]({static}/images/img-9376.jpg)

![perníčky]({static}/images/img-9536.jpg)

![zvonkohra]({static}/images/img-9383.jpg)

## Víkend v Abú Zabí

O co náročnější byly všední dny, o to spíš jsem se snažil o víkendech vypnout a maximálně relaxovat. Myslím, že se mi to docela dařilo. Třešničkou na dortu bylo, že první prosincový víkend se jel poslední závod sezóny F1 a můj oblíbený Lando Norris v McLarenu vyhrál mistrovství světa. Sledování jsem si užil, byly to nervy.

Lando Norris mistrem světa je zadostiučinění pro všechny hodný a nesmělý kluky jako já, že tahle cesta funguje taky, a že člověk nemusí za každých okolností být jenom bezohledný, silnější pes, a všechny „rozmrdávat“. Že i mistr světa může mít impostor syndrom, nebo že i mistr světa může plakat.

A když jsem po dekádě začal zase sledovat formuli, tak jsem ze setrvačnosti fandil McLarenu, kterému jsem kdysi fandil jako kluk, když tam jezdili Hakkinen, Coulthart, nebo Raikkonen. Ale tým se spíš propadal v pořadí a výkonnosti. Svou oranžovou mikinu jsem koupil v 50% slevě, když byli poslední. Co se jim povedlo za obrat, to je neskutečný.

![Lando]({static}/images/5130b5c119abfaaa.jpeg)

## Víkend v Hlinsku

S kamarádem Peťou jsme teď v pátek vyrazili do Hlinska, abychom si tam během víkendu odpočinuli od života. Neměl jsem od toho žádné očekávání a byl to celkem spontánní výběr místa. Příjemně nás to překvapilo a byl to super _retreat_. Udělali jsme několik tůr po okolí, zašli do sauny, prozkoumali místní podniky a pamětihodnosti a probrali u toho celý život.

![Betlém]({static}/images/img-9621.jpg)

![krávy]({static}/images/img-9640.jpg)

![výhledy]({static}/images/img-9642.jpg)

![trať]({static}/images/img-9669.jpg)

![místo dalekého rozhledu]({static}/images/img-9687.jpg)

![rozhledna]({static}/images/img-9690.jpg)

Ráno těsně před odjezdem si náš kotel řekl, že má malý tlak a že nebude ohřívat a topit. Tak jsem do něj musel ještě hadicí dopouštět vodu, aniž bych věděl, kde tu hadici ve sklepě přesně máme, nebo abych si pořádně pamatoval, jakým postupem a odkud kam se to posledně dělalo. Luboš R. mi na dálku pomohl a nakonec jsem to nahodil, pak jsem do 4 minut opustil byt a vlak jsem stihl úplně těsně. Doufám, že to nikdy už nebudu potřebovat, ale postup jsem si tentokrát velmi detailně zapsal. Nic než návod!

![kotel]({static}/images/img-9601.jpg)

## Další

-   Mia mě [sponzoruje na GitHubu](https://junior.guru/love/)! Díky! 🙇‍♂️
-   Hodil jsem na LinkedIn [příběhy tří juniorů z klubu, kteří si v poslední době sehnali práci](https://www.linkedin.com/posts/honzajavorek_jestli-jsem-to-minule-nazval-hřbitov-tak-activity-7402364626807447552-GC2G/). Psal jsem to hodně dlouho a při psaní jsem narazil na limit znaků a musel jsem to několikrát upravovat, abych se vlezl 😅 Status pak měl ale docela ohlas, tak se to asi vyplatilo: 3.100+ impresí, 100+ lajků, 16 komentářů, 1 repost. Na Mastodon jsem dával jen [kratší TL;DR](https://mastodonczech.cz/@honzajavorek/115688641594254318).
-   Podporuju místní Zelené v jejich volební kampani. Udělali jsme fotku a vymysleli nějaký text (to bylo nejtěžší) a jsou z toho statusy: [Instagram](https://www.instagram.com/p/DSNHrKhCiNp/), [Facebook](https://www.facebook.com/100069293256415/posts/1161457346174030/), [Mastodon](https://mastodonczech.cz/@honzajavorek/115723093719252363). Přispět můžete na [dary.zeleni.cz/praha3](https://dary.zeleni.cz/praha3). Pokud se hodláte zeptat, že co ta mikina McLarenu, tak mám připravenou odpověď, že formule na blikačkách nepřekáží nikomu s kočárkem na chodníku 😀
-   Napsal jsem jednomu profesorovi, že kdyby náhodou začal zase blogovat, tak že bych to rád četl.
-   Mému Spotify _wrapped_ [dominují dětské písničky](https://mastodonczech.cz/@honzajavorek/115666392489692420) a jsem z toho nesvůj. Dokoukali jsme se ženou [MAID](https://www.csfd.cz/film/925905-sluzka/prehled/) – emočně náročné na sledování, ale perfektní.
-   Dělali jsme v klubu anketu témat, o kterých by mohl mít přednášku příští speaker. Měl jsem srandovní call s Eliškou Č. o tématu její budoucí přednášky.
-   Sháněl jsem dárek pro svou milovanou ženu. Viděl jsem se s Danem S. v Dejvicích, s Tomem V. v Karlíně, zaběhal jsem si na Vítkově s Míšou Š., když byl pracovně v Praze, a byl jsem na kafi s Domi K. Obdržel jsem podarovaný mikrofon od Tomáše Z. z Boskovic.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. Tentokrát fakt hodně e-mailů a zpráv na všech možných kanálech. V klubu to taky dost žilo.
-   Za 18 dní jsem naběhal 13 km, při procházkách nachodil 8 km, na túrách nachodil 34 km. Celkem jsem se hýbal 12 h a zdolal při tom 55 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.
-   Kvůli různým věcem jsem nemálo nocí hodně špatně spal a pak jsem byl často přes den rozbitý a musel jsem si jít v některé dny i na 2h přes den lehnout, abych to přežil. Tak snad se mi to povede teď nějak uklidnit. Nejhorší jsou noci, kdy jdu spát brzo, ale pak se proberu ve tři, rozjede se mi mozek, a do pěti nezaberu.

![spánek]({static}/images/9d6115ab13e9f697.png){: .img-thumbnail }

## Plánuji

1.  Sestříhám a publikuju přednášku s Irčou.
2.  Sepíšu novou [stránku o projektech](https://junior.guru/handbook/projects/) do příručky.
3.  Začnu brát nějak víc na vědomí fakt, že budou Vánoce.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Size of Life](https://neal.fun/size-of-life/)<br>Jé, nový neal.fun, to zas bude propálených produktivních hodin 😀 Jinak onehdá jsem na Wikipedii zjistil, že slon africký je větší než jak byli velcí mamuti a mastodonti, a tady je to taky.
- [Cestování do USA bude složitější. Americké úřady chtějí požadovat třeba historii na sociálních sítích](https://www.irozhlas.cz/zpravy-svet/cestovani-do-usa-bude-slozitejsi-americke-urady-budou-chtit-i-dna-nebo-historii_2512101305_jtr)<br>Čína hadr, tyjo. Na jednu stranu se mi po SF trochu stýská, ale na druhou stranu jsem rád, že nedělám pro firmu, která by chtěla, abych tam pracovně jel, protože to bych byl fakt rozpolcený. Dříve spíš benefit, dnes za trest… Doufal jsem, že se do USA ještě někdy podívám, ale takhle teda nevím nevím.
- [Stagehand: A browser automation SDK built for developers and LLMs.](https://www.stagehand.dev/)<br>„We built an OSS alternative to Playwright that's easier to use and lets AI reliably read and write on the web.“ Zajímavé, tohle budu muset prozkoumat.
- [Europe is under siege](https://www.noahpinion.blog/p/europe-is-under-siege)<br>„Europe finds itself in an extraordinary perilous position right now. Its main protector has suddenly withdrawn. It has a ravenous, brutal empire attacking its borders, supported by the world’s most powerful nation. Its main export markets are shriveling, and its manufacturing industries are under dire threat from waves of subsidized foreign competition. What can it do to fight back?“
- [Až 200 tisíc za místo na rok. Dražba v Karlových Varech ukázala tržní cenu parkovacích stání - Zdopravy.cz](https://zdopravy.cz/az-200-tisic-za-misto-na-rok-drazba-v-karlovych-varech-ukazala-trzni-cenu-parkovacich-stani-267494/)<br>Kolik stojí parkování doopravdy… Tak třeba se jednou této tržní věci dočkáme i v Praze, místo toho komunismu.
