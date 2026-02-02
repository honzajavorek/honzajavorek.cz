Title: Týdenní poznámky: Lyže, bydlení, pojištění a klub
Image: images/img-0264.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 13 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/371
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115984773506915337

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2026-01-16_tydenni-poznamky-testovani-scrapovacich-cviceni-a-pripravy-noveho-kurzu.md) už utekl nějaký ten týden (16. 1. až 30. 1.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![já a socha kamzíka]({static}/images/img-0264.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Měli jsme prodloužený víkend na horách, konkrétně v Jeseníkách na Ramzové, a bylo to super. Ale v týdnu předtím jsem se nějak nestihl pořádně vyspat, jak jsem se snažil všechno postíhat, a na samotném pobytu jsem zase řádil s kámošema, které jsem dlouho neviděl, takže jsem přijel dost vyčerpaný a v pondělí jsem si dal raději volno, abych doplnil životní sílu. Což se mi naštěstí trochu povedlo. A hory byly fajn, zalyžovali jsme, zajezdili jsme na bobech, sníh byl, počasí bylo v pohodě.

![Šerák]({static}/images/img-0267.jpg)

## Změny na webu a v klubu

- Předělal jsem konečně jak se chovají skupinky v klubu. Nyní se o ně stará _realtime_ bot, který do nich přidává lidi jen pokud se do skupinky něco píše. Udělal jsem to přes _mention_ na roli, ale bohužel to dělalo sice tiché, ale i tak červené a viditelné notifikace, takže jsem to musel ještě pak předělat na to, aby se lidi přidávali jednotlivě. To sice pošle systémovou zprávu do vlákna a děje se to fakt po jednom, ale je to nejvhodnější kompromis mezi všemi mantinely, které mi v tomto směru Discord dává. Zkoušel jsem to udělat pomocí AI agentů, ale [po marném snažení vyždímat z nich něco lepšího než prasokód](https://mastodonczech.cz/@honzajavorek/115929196131711660) jsem si to nakonec napsal v zásadě sám.
- Zdražil jsem klub ze 199 Kč/měs na 299 Kč/měs. Zatím je brzo hodnotit, jaký to má efekt, ale minimálně pocitově se mi nezdá, že by to snížilo počet lidí, kteří do klubu z prodejní stránky nakouknou do _free trialu_. Zdražení bych měl promítnout i do [promo videa](https://www.youtube.com/watch?v=zHt4z5lp2e0), kde je bohužel zobrazena cena, ale to jsem zatím odložil. Stávající členy jsem nechal na původní ceně. Jestli cenu nechám na 299 Kč/h, nebo ji ještě zvýším, bude záležet na výsledcích aktuálního experimentu.
- Kvůli změně tarifů jsem musel změnit nějaké věci i v kódu, např. detekci který tarif je který pro účely statistik nebo vypisování sponzorů podle jejich typu.
- Lepší text pro pravidelná upozornění, že se bude konat nějaký programátorský sraz v nějakém městě. (Díky Dane!)
- Na web jsem přidal upozornění pro přednášky, které jsou více jak dva týdny v budoucnosti, že pokud se někdo přidá do klubu hned, tak přednášku nestihne v rámci _free trialu_. (Díky Táňo!)
- Přidal jsem Apify do partnerů, protože mi dávají free kredity na jejich platformu. Dávají mi je už dlouho a přidal jsem je do partnerů dobrovolně, ani jsem jim to neříkal. Prostě jsem něco upravoval v téhle části kódu, tak jsem si na to vzpomněl a rovnou to udělal.
- Smazal jsem tarif na angličtinu a vysvětlovací stránku na webu o výuce angličtiny v klubu, protože výuka už neprobíhá.
- Řešil jsem u jednoho člena žonglování s účty a předplatnými.
- Aktualizoval jsem [team page](https://junior.guru/about/contact/#tym-pomocniku).
- Upravil jsem prompt, který třídí nabídky práce, aby zůstaly jen ty fakt pro juniory. Trochu jsem rozšířil jeho záběr, protože mi přišel moc přísný, a zároveň opravil nějaké filtry, aby tím nepropadávali CNC programátoři apod.
- Našel jsem kód, který exportuje mnou stahované nabídky práce do API. To mělo být pro Navigaru s tím, že já si zase vezmu nějaké nabídky práce od nich, ale oni mezitím pivotovali jinam a toto API nevyužívali, ani já jejich. Takže jsem to celé smazal.
- Předělal jsem jak se aktualizuje seznam klubových akcí na Discordu. Teď se vždy při změně smázl celý kanál a nasypaly se tam znova zprávy s odkazem na info a na záznam, pro každou akci jedna. Jenže to některým lidem stále ukazovalo ten kanál jako nepřečtený a otravovalo je to. Tak jsem to předělal tak, aby to zprávy přepisovalo přes editace příspěvků.

## Přednáška s Artemem

V úterý jsme v klubu měli [přednášku o testování od Artema](https://junior.guru/events/58/). Týden předtím jsem s ním byl i na obědě. Přednášku jsem pak ještě před odjezdem na hory propagoval na sítích ([LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7419661507560554497/), [Mastodon](https://mastodonczech.cz/@honzajavorek/115932239848214979)).

No a vydařilo se to moc pěkně! Nahrávat přišel Tinuki a bylo to bez jakýchkoliv problémů a zádrhelů. Ani Artem neměl žádné technické potíže, což byla ozvěžující zkušenost a jistá naděje, že lze udělat na Discordu přednášku i bez toho, aby speaker řešil půl hodiny, že ho nevidíme nebo neslyšíme.

Na akci se dostavilo 15 až 17 lidí, což je pěkné publikum – lidi si zvykli na záznamy a hodně si jich to pustí dodatečně. Ale jak napsal jeden člen, který se připojil:

> Je to vždycky super, když je tam na druhý straně doopravdy ten borec a můžeš se ho na něco zeptat v chatu 😃. Milionkrát lepší, než záznamy nebo nějaký videa na yt.

Takže po přednášce jsem měl fakt radost. A i když jsem ještě nedotáhl ten formulář na feedback po přednáškách od Táni, tak se mi povedlo nějaký získat ručně a byl pozitivní. A aji Artem měl z přednášky v klubu dobrý dojem. Je to fakt příjemné, když se jednou zase něco povede 😀

## Prezentace projektů juniorů

Poslední věc, co chci přidat do prototypu [junior.guru/candidates](https://junior.guru/candidates/), je pořádná prezentace projektů juniorů. Je to dost zásadní věc, která určuje jejich úspěch, takže to chci fakt ještě dodělat.

Tento týden jsem pracoval na tom, abych měl v [eggtray API](https://github.com/juniorguru/eggtray) informace o obrázcích, které mají projekty v README, protože to jsou typicky ukázky projektu, třeba obrazovky z mobilní appky.

Pak jsem chtěl ještě přidat screenshoty, pokud má projekt nějaké živé demo, ale to se ukázalo zapeklitější a po několika hodinách programování a vymýšlení jsem velkou část kódu zase smazal. Chtěl jsem použít Simonův [shot-scraper](https://github.com/simonw/shot-scraper) a obrázky vyrobit přímo v rámci eggtray repozitáře, ale pak jsem vyhodnotil, že to možná není nejmoudřejší a že je to komplexnější, než jsem myslel. A taky jsem [narazil na chyby](github.com/simonw/shot-scraper/issues/117). Ještě to budu muset promyslet.

## Zamávání roku 2025 a uvítání 2026

V klubu jeden z členů vykopnul vlákno, kam mohli lidi psát svoje plány na rok 2026. Mělo to mít tuhle strukturu:

- V čom by ste chceli pokračovať
- V čom by ste naopak nechceli pokračovať
- A čo by ste naopak chceli začať

Našel jsem si čas na to se nad tím zamyslet a sepsal jsem to, pro ostatní i pro sebe:

### V čem bych chtěl pokračovat

- Vnímání sebe sama, svých potřeb, zvědomování si různých situací. Myslím, že toto mně posunuje jako člověka za poslední dobu úplně nejvíc.
- Běhání, nebo v podstatě jakýkoliv sport. Teď mi to trochu erodovalo, protože jsem měl nějaké nemoci a teď byla venku zase docela zima, a já nechtěl začínat z nuly v zimě. Ale chci se k tomu vrátit.
- Chci dělat na junior.guru. Vidím, jak to lidem pomáhá a zároveň mě to hodně baví. Budu možná muset udělat nějaké kompromisy a změny, aby se podnikání udrželo za nových podmínek, ale v ideálním případě najdu způsob, jak to provozovat dál. Pokud bych si mohl vybrat, dělal bych to zase na plný úvazek.
- V minulém roce jsem se naučil stříhat videa a stále mě to baví. Chtěl bych se v tom zlepšovat. Je to dobrý relax. Chtěl bych vytvořit něco pěkného, třeba jenom srandovního, s čím bych se mohl pochlubit i ostatním.
- Snažil jsem se učit relaxovat – chodit do sauny, nebo třeba do kina, a to včas, ještě dřív, než začnu být na všechny kolem sebe protivný. Tohle je asi nikdy nekončící proces učení. Některé týdny se mi to daří vychytat, jiné vůbec. Ale aspoň o tom vím a snažím se.
- Přijde mi, že jsem dost omezil alkohol. Nebylo to nějaké zásadní rozhodnutí, spíš to prostě vyplynulo z okolností. Kocoviny víc bolí a spánek i čas je mi dražší. Takže když už nějak víc piju, tak spíš výjimečně, při nějaké příležitosti, a jen tehdy, kdy mi to stojí za to. Současný stav mi vyhovuje. Když se vidím po půl roce s kamarády, klidně si to natáhnu do tří do rána. Ale je to vědomé rozhodnutí, nestane se to „omylem“. A mimo tyhle příležitosti už skoro nepiju. Sem tam skleničku vína se ženou u večerního programu.
- Začal jsem si dávat na noc mobil do obýváku, abych do něj nečuměl před usnutím a po probuzení. Taky mě to ráno donutí vstát na nohy, abych mohl zaklapnout budík. Tohle byla jedna z nejlepších změn za poslední dobu.

### V čem bych nechtěl pokračovat

- Je hodně věcí, co by šlo zlepšit na mojí životosprávě, ale pokud bych měl vybrat jednu zásadní, která má vliv na všechno, tak to bude spánek. Uplynulý rok byl rozhodně lepší než předchozí, ale mnohdy to pořád bylo na autopilota, kdy jsem šel spát úplně zbytečně pozdě. Takže míň tohoto autopilota.
- Mám pocit, že jsme málo odvážní a rozhodní s dovolenýma. Plánujeme to vždycky strašně dlouho a nakonec to třeba ani nenaplánujeme. Když už to naplánujeme, jsme někde jenom týden, nebo ani to ne. Nechci se nechávat ušlapat událostmi a zapomínat na to, že potřebujeme i dovolenou, a že dovolená by mohla trvat i déle než týden. Chci si víc plánovat kvalitní čas na odpočinek a regeneraci. Opět autopilot, který hrne věci a tohle si prostě nikdy nedá jako prioritu. Volna sice máme, ale často jen prodloužené víkendy apod., což k plné regeneraci prostě nestačí. Dřív jsem si myslel, že až budu mít malé děcko, pojedeme třeba na měsíc do Španělska a zkusíme tam chvilku takhle žít, já budu pracovat z domu, žena taky, o dítě se nějak na střídačku postaráme… Teď mám dojem, že to je sci-fi. Že jsme rádi, když za ten rok vůbec dokážeme jet někam dál, nebo na dýl. Navíc teď potřebujeme řešit bydlení, takže nějaká dovolená nebude vůbec priorita a kdo ví, kolik na ni vůbec zbude peněz. A skoro za rok jde děcko už do školy…

### Co bych chtěl začít

- Chtěl bych začít víc využívat AI tak, abych se mohl věnovat junior.guru efektivněji. Zkusit trochu ovládnout všechny ty agenty a kdovíco.
- Zařídit byt, přestěhovat se. To bude asi hodně nového. Těším se na výsledek, ale z toho procesu mám respekt a asi i strach. A taky to bude spousta změn. Určitě přinesou spoustu hezkých věcí, ale já zatím vidím spíš ty komplikace, nebo parametry, ve kterých je to zhoršení, a to mi brání těšit se.
- Na junior.guru bych chtěl rozjet katalog juniorů a snad tím nastartovat další rozvoj projektu. Kdyby se to povedlo, udělalo by mi to fakt velkou radost a můj život by byl hned o něčem trochu jiném. Teď jsem trochu utrápený kapitán lodičky na hodně rozvlněné vodě. Kdybych nemusel chvíli řešit přežití, ale mohl se aspoň chvíli zabývat rozvojem junior.guru jen tak podle toho, co mi zrovna dělá radost, bylo by to super. Nebo ten plný úvazek, to by bylo!

## Další

-   Odstrojili jsme vánoční stromeček a tradičně jej vyhodili z okna. Tedy, ehm, poslali na provázku oknem na chodník, aby nebylo jehličí po celém domě 😀
-   Odehrál se jeden velký milník co se týče našeho nového bydlení 🔑
-   Odvezl jsem si kolo do servisu, zážitkový popis mé cesty je [na Mastodonu](https://mastodonczech.cz/@honzajavorek/115979304850665282).
-   Přišel mi vánoční dárek od kamarádů – objednali mi z UK speciální vydání časopisu Autosport s podtitulem „Secrets of McLaren's newest title winner” ❤️
-   Šel jsem do Mews na brunch pro lidi, kteří se motají kolem komunit. Bylo to hodně dobře zorganizované (díky Gábi!) a bylo to strašně fajn. Pokecal jsem se starými známými, ale potkal jsem i nové, zajímavé lidi.
-   Koupil jsem s předstihem autobus na cestu z dovolené na horách, která nás teprve čeká (sešlo se nám to a tak trochu omylem máme dvě krátké zimní dovolené, každou jinde a každou s někým jiným). Dal jsem si záležet, aby to nebylo [JAMI LINES]({filename}2025-02-14_tydenni-poznamky-schuzky-krkonose-scrapery.md).
-   Oslavili jsme dceřin svátek a já jsem jí konečně mohl dát tu LEGO krabičku, kterou jsem si tak přál.
-   Finišoval jsem výběr životního pojištění. To je věc, kterou člověk starý jako já vybere v ideálním případě poprvé a naposled, protože později už to bude jen dražší a horší. A je to docela složitá věc plná nástrah. Takže mně to dost i stresovalo. [Pomáhal jsem si pomocí ChatGPT](https://mastodonczech.cz/@honzajavorek/115984527866581468) a konzultoval to s kamarády, no nakonec mám něco vybráno. Ale to neznamená, že skončily úkoly z tohoto kyblíku, protože teď zase sháním různé zprávy od doktorů, co chce pojišťovna vidět, než mě vůbec pojistí.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. Klub jsem za ty dva týdny přečetl několikrát celý a dokonce jsem se podíval i na několik CVček a dal na ně poctivou zpětnou vazbu, což většinou spíš odkládám, nebo nechávám na druhých.
-   Za 15 dní jsem moc nesportoval, jen chození a dvě dopoledne lyžování, ale to jsem ani neměřil.

## Plánuji

1. Udělám nějaký zásadní posun co se týče [junior.guru/candidates](https://junior.guru/candidates/), nechť mi je [Doing the thing is doing the thing](https://www.softwaredesign.ing/blog/doing-the-thing-is-doing-the-thing) oporou.
2. Pošlu newsletter a napíšu na podporu Buttondownu kvůli editoru.
3. Podívám se na dotazník spokojenosti, který Táňa udělala pro online akce na junior.guru.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Pětina dětí nečte knihy a většina již využila AI, ukázaly výsledky Minisčítání 2025](https://csu.gov.cz/docs/107508/8e4ea8cf-89c9-44fb-8282-05c0ebc2c3be/csu_tk260128_miniscitani_2025_prezentace.pdf?version=1.1)<br>Zajímavý nový materiál ČSÚ o dětech: „Nástroje umělé inteligence někdy využilo již devět z deseti dětí… Pouze 2 % dětí neměla vlastní mobil. Ještě před nástupem na základní školu ho vlastnila necelá čtvrtina všech dětí. Nějakému druhu fyzické aktivity děti týdně věnují v průměru nejčastěji 2 až 3 hodiny (35 %) a více než 7 hodin dokonce 17 %… Spaní ve volné přírodě pod širákem si vyzkoušelo 28 % chlapců a 24 % dívek… Představy dětí o nadpřirozených schopnostech se liší podle pohlaví i věku. Dívky by si nejčastěji přály umět číst myšlenky, chlapci zastavit čas. Mladší děti by rády uměly létat nebo byly nesmrtelné.”
- [Jak nám ukradli komunitu a prodali zpátky jako měsíční předplatné – Page Not Found](https://pagenotfound.cz/clanek/jak-nam-ukradli-komunitu-a-prodali-zpatky-jako-mesicni-predplatne)<br>„Každá značka má svou komunitu. Každý placený newsletter. Influenceři mluví o své komunitě a myslí tím sledující. Přemýšlím nad tím, kdy jsme to slovo začali používat pro všechno, co komunitou vůbec není.“ Chci si myslet, že i když je můj klub online, tak funguje opravdu jako komunita, nebo minimálně se na tyhle věci snaží navazovat. Rozhodně bych nerad, aby to bylo pro většinu členů jen o „přijdeme, počteme, olajkujeme, pobudeme a odejdeme“.
- [Trump přestal schovávat, kým skutečně je](https://www.voxpot.cz/clanky/trump-prestal-schovavat-kym-skutecne-je)<br>Člověk si o těch věcech čte každý den zvlášť, vsakuje jednu po druhé, a dokud nepřijde takovýhle článek, ani si neuvědomí, kolik toho už je a jak příšerné to je. Přemýšlím, co můžu dělat, než se rozpadne i úplný zbytek důvěry v USA.
- [Na barikádách svobodného internetu – GobGob](https://www.gobgob.org/2025/01/20/goblog-na-barikadach-svobodneho-internetu/)<br>„Nemusíte být programátorka, ani nemusíte hned (ani za pět let) posílat prostředky na jejich vývoj a údržbu. Ani instalovat a používat hned všechno. Stačí jeden software, jedna alternativní služba. Prostě jen zvídavě vstoupit a namísto nedostatků vidět komunitu. Stejně jako si nosíme komba z dodávek, obrazy do schodů a podáváme teplé lahváče v plesnivých sklepech. S potměšilou radostí. Jen tak zlehka. Zlehka si užívat digitální autonomní zóny.“
- [European alternatives for popular services | European Alternatives](https://european-alternatives.eu/alternatives-to)<br>Alternativy nejsou nic moc, ale je fajn vědět, po čem v případě nouze sáhnout. Snad to nebude zapotřebí někdy velmi brzy.
