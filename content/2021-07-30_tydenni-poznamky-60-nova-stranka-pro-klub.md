Title: Týdenní poznámky #60: Nová stránka pro klub
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl další týden (26.7. — 30.7.) a tak [stejně jako minule]({filename}2021-07-25_tydenni-poznamky-59-plakatky-na-prednasky.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Dokončení nové stránky pro klub

Tento týden jsem konečně přehodil `/club2/` na [/club/](https://junior.guru/club/), byť jsem předtím značně osekal rozsah toho, co jsem chtěl mít dokončeno před finálním vypuštěním do světa. Už teď ale vím, že to bylo to nejlepší, co jsem mohl udělat. Při tvorbě této nové stránky jsem udělal dvě hlavní chyby:

1. Neudělal jsem rychlý prototyp, který tak akorát projde testem „Je to lepší než to, co tam je teď?“, a který co nejrychleji předhodím lidem, abych jej pak podle zpětné vazby postupně vylepšoval.
2. Spojil jsem tvorbu nové stránky s překopáváním technického zázemí webu, ať už šlo o přesun na MkDocs a hledání cest, jak v tomto novém systému budu celý web dělat, nebo o přesun na zcela nový systém psaní CSS.

Druhou chybu jsem udělal záměrně. Vlastně to nebyla chyba, ale nějaký vědomý _tradeoff_, protože jsem si věc od začátku plně uvědomoval, vyhodnotil jsem si ji a vědomě jsem se rozhodl, že půjdu méně efektivní cestou za cenu toho, že budu mít z procesu větší radost a přiblížím se nové architektuře. Můj příjem je stále kolem 20.000 Kč, což není úplně špatné, takže jsem si nějakou tu neefektivitu prostě dovolil, i proto, že mi už trochu začínalo hrabat z toho, jak musí být všechno efektivní a chyběla mi radost ze „zahradničení“.

![Stránka o klubu, první pokus]({static}/images/club-page-1.png)
První pokus o ilustraci

První chybu jsem ale udělal nevědomky a spálila mě. Stránku jsem dělal dlouho, ale ne pouze kvůli dvojce, což by bylo OK. Dělal jsem ji dlouho, protože jsem se mentálně přepnul do režimu „vytvářím něco dokonalého, co všechny ohromí, a až to bude hotové, tak to s velkou pompou spustím.“ Což tedy není ani _lean startup_, ani _continuous delivery_, není to prostě nic, za co bych se pochválil. Jak se tvorba stránky prodlužovala a týdny ubíhaly, začínal jsem mít pocit, že je to nekonečné a že nepřináším žádnou hodnotu, že si tam někde v závětří posouvám pixely jeden den 5 doleva a druhý den 10 doprava, a že nejsem prostě užitečný. To jsem se v tomto týdnu jal ukončit a rozhodl se, že to prostě do pátku vypustím ven.

![Stránka o klubu, druhý pokus]({static}/images/club-page-2.png)
Druhý pokus o ilustraci

Většinu týdne jsem tedy pracoval na stránce a snažil se ji dokončit, ať už šlo o několikadenní zápas s úvodní ilustrací, ladění textů, ladění CSS, celodenní zápas s FAQ, apod. Měl jsem ke stránce spoustu poznámek a kartiček v Trellu, které jsem opakovaně procházel a ujišťoval se, že stránka splňuje vytyčené cíle. FAQ jsem opravdu psal celý jeden den, snažil jsem se inspirovat [Nomad Listem](https://nomadlist.com/faq), ale nedokážu říct, jestli jsem s tím úplně spokojený. Ke konci týdne jsem už měl celou tu stránku vypálenou na sítnici a nebyl jsem schopen dát dohromady kloudnou větu, která by dávala smysl, ze všeho toho psaní a cizelování významů a zkracování vět. Nakonec jsem tedy v pátek v deset večer nahodil na [/club/](https://junior.guru/club/) novou verzi a zeptal se různých lidí, včetně lidí v klubu, co si o tom myslí.

![Stránka o klubu, třetí pokus]({static}/images/club-page-3.png)
Třetí, zatím poslední pokus o ilustraci a celkově texty a uspořádání záhlaví stránky o klubu

A hádejte co? Mám teď hromadu zpětné vazby a už v tento okamžik vím, že tam musím některé věci předělat. Kdybych na stránce nepracoval v závětří, ale ukázal ji lidem mnohem dřív, mohl jsem připomínky možná zapracovávat už v průběhu. Bude nejspíš ještě pěknou chvíli trvat, než tu novou stránku někde začnu propagovat, nejsem s ní zatím spokojený. Ale jo, je rozhodně lepší než to, co tam bylo doteď…


## Plakátky k přednáškám a YouTube

Zkoumal jsem, jak je to s těmi poměry stran pro plakátky, když je chci mít jako _thumbnail_ pro video na YouTube. No a došlo mi, že video je na YT, co se poměru stran týče, zřejmě tak velké, jak velké jsem ho nahrál. V mém případě to znamená, že je velké náhodně a pokaždé jinak. Od toho se pak odvíjí i potřebná velikost pro náhledové obrázky. Pokaždé jinak.

Pokud bych tedy chtěl mít jednu velikost náhledových obrázků, musel bych překódovat všechna videa do nějakého jednotného rozměru. Kdybych dokázal z hlavy napsat příkaz do terminálu, který by to za mě udělal (a doplnil zbytek černou barvou), tak to snad i udělám, ale zatím jsem se na to vykašlal. Patlat se s tím ručně v iMovie, to se mi fakt nechce. Ani vlastně nevím, jestli lze video na YouTube „přenahrát“, nebo se pak musí nahrát celé nové.

Rozměr generovaných náhledů jsem nicméně upravil tak, aby nebyl u většiny videí oříznutý zvrchu a zespodu (protože pak zmizí kusy textu), ale aby spíš způsoboval to, že se po stranách při nesedícím rozměru objeví černé pruhy (protože pak nic důležitého nezmizí a pouze něco nedůležitého přebývá). Opět posílám velký dík [této stránce](https://www.vypocitejto.cz/trojclenka/), kde jsem mohl rychle měnit čísla a pak zkoušet, co bude jak vypadat.


## Počítadla

Delší dobu pokukuji po [Simple Analytics](https://simpleanalytics.com/) místo Google Analytics. Není to priorita, ale občas se k tomu vrátím. Tentokrát mě na to přivedl Jan Tichý [svým statusem na LinkedIn](https://www.linkedin.com/posts/jantichy_google-analytics-4-masterclass-od-honzy-tich%C3%A9ho-activity-6823300847833821184-t5dI). To, co jsme tam řešili, jsem si zkusil [zjistit přes Twitter](https://twitter.com/SimpleAnalytic/status/1419776056479952901) a dostal jsem pěknou odpověď (už vidím, jak mi takhle odpoví někdo z GA, haha). No a potom s podobným tématem přišel zase Simon Willison [na Twitteru](https://twitter.com/simonw/status/1420798613412663307). U něj se objevil odkaz na [Plausible](https://plausible.io/), o kterém jsem předtím nevěděl. Až nadejde čas dát GA pá pá, budu si muset oboje pořádně projít a nějak si vybrat, oboje totiž vypadá dobře. Oboje je navíc vyráběno v EU, což se mi líbí.

GA byly OK na rozjezd, jsou zadarmo, ale nelíbí se mi. Jsou pro mě zbytečně komplikované a přesnost jejich dat [je stejná iluze](https://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/) jako přesnost jakýchkoliv jiných měřidel. Navíc jde o sledovací a reklamní gigant Google. Já své uživatele sledovat nechci, stačí mi orientační čísla. Pokud nemusím, nechci Google krmit svými návštěvníky.


## Další poznámky

- V úterý se odehrála přednáška s Norou Kořánovou o tom, co je to _technical writing_, a povedla se moc pěkně. Trochu jsem stresoval, protože dlouho žádná přednáška nebyla, ale vše bylo OK.
- Dolaďoval jsem další přednášky a informace o nich. Dobré je, že si to už nemusím psát nikam do poznámek, ale mohu si to psát [přímo do events.yml](https://github.com/honzajavorek/junior.guru/blob/4fca99f06da40c11f8a67b5c0201924d7c123fda/juniorguru/data/events.yml). Když od speakera zjistím nějakou informaci, mohu ji hned doplnit. Pokud je informací zatím málo, [akorát blok zakomentuji](https://github.com/honzajavorek/junior.guru/commit/7ebc3de7bfbb1db2ea3679b573e61ebe24a1d55a). A speakeři mohou [posílat PR](https://github.com/honzajavorek/junior.guru/pull/647), nebo [psát komentáře](https://github.com/honzajavorek/junior.guru/commit/816a24b80a28e01897acdbe8d2f9394602ad6aa1).
- Dal jsem do kódu JG dva [easter eggy](https://cs.wikipedia.org/wiki/Velikono%C4%8Dn%C3%AD_vaj%C3%AD%C4%8Dko_(virtu%C3%A1ln%C3%AD)).
- Složil jsem doma nový gauč a starý gauč jsem rozložil a po kouskách odnosil po točitých schodech do sklepa.
- Zapracoval jsem nějaké změny do PR, který má implementovat strojové učení při třídění nabídek práce. Protože jsem ho nechal dlouho ležet a mezitím udělal dost změn v infrastruktuře kódu (třeba přechod na Makefile a Poetry), udělal jsem po domluvě s Mílou [nový PR](https://github.com/honzajavorek/junior.guru/pull/655) se všemi změnami, na kterém může pak pohodlně pokračovat.
- Diskutoval jsem v klubu a vítal nové členy. [Mews](https://www.mews.com/) byli hodně aktivní ve zvaní členů. Mají šest vstupů a všechny poctivě využili, dokonce lidi vybrali dost pestře, aby mezi nimi byli junioři i senioři. Vzorový přístup! Snad to inspiruje i další firmy.
- Dočetl jsem [knihu povídek od Teda Chianga](https://www.goodreads.com/book/show/32200035-arrival). Podle jedné z nich byl natočen film [Arrival](https://www.imdb.com/title/tt2543164/), který se mi osobně dost líbil. Povídka je snad ještě lepší. Nejlepší ale je, že i všechny ty ostatní povídky jsou jedna podruhé každá opravdu šíleným, hlavurozebírajícím úletem. Při čtení mi vždycky vybuchla hlava a musel jsem často nad daným tématem dost přemýšlet a nebo si pročíst půl Wikipedie. Nečetl jsem nikdy moc žádné sci-fi, ani povídky, natož sci-fi povídky. Toto se mi ale dost líbilo. Doporučoval bych tuto četbu každému, jenže to není lehké čtení a kniha nevyšla česky, na čemž by se dost lidí v mém okolí zřejmě zaseklo.
- Zjistil jsem, že [stránku pro členy](https://junior.guru/membership/) patrně nikdo z členů nepoužívá. Což je skvělé, protože ji mohu tím pádem zrušit a zjednodušit i potřebnou navigaci. Základní informace o klubu jsou přímo v klubu. Odkazy na nastavení a propojení s Discordem mohou být ve FAQ, nebo prostě někde bokem.
- Během 7 dní od 26.7. do 1.8. jsem při procházkách nachodil 3 km. Celkem jsem se hýbal 1 hodinu a zdolal při tom 3 kilometry.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Rozšířit tým.
2. Vylepšovat stránku pro klub, zapracovat připomínky.
3. Propagovat [další naplánované přednášky](https://junior.guru/events/#planned) a naházet nové věci do fronty na sociální sítě, kde teď nic nemám.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [The forgotten history of how automakers invented the crime of "jaywalking"](https://www.vox.com/2015/1/15/7551873/jaywalking-history)<br>Jak se automobilovému průmyslu podařilo přesvědčit lidi, že mají vyklidit veřejný prostor v ulicích a cesty přecházet pouze po přechodech. Nevzniklo to samo, šlo o lobby a PR.
- [Please, enough with the dead butterflies!](https://www.emilydamstra.com/please-enough-dead-butterflies/)
- [Tenkrát na Žižkově. Unikátní staré fotografie pražské čtvrti, která slaví 140. výročí](https://zpravy.aktualne.cz/domaci/tenkrat-na-zizkove-unikatni-stare-fotografie-prazske-ctvrti/r~75986ce4b3cd11ebb9860cc47ab5f122/)<br>Super foto série i s popisky
- [Proč má inspekce práce problémy zjišťovat porušování zákoníku práce](https://a2larm.cz/2021/07/proc-ma-inspekce-prace-problemy-zjistovat-porusovani-zakoniku-prace/)<br>Přesný popis toho, jak probíhá kontrola inspekce práce a proč tento systém v současné době příliš nefunguje.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
