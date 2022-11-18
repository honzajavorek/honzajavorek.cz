Title: Týdenní poznámky #86: Konečně hotový robot na inzeráty a vítání firem v klubu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (26.3. — 8.4.) a tak [stejně jako minule]({filename}2022-03-25_tydenni-poznamky-85-breznovych-300-km-na-kole-a-spousta-prace.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Hurá! Páteční poznámky konečně v pátek! To, že minulý týden vůbec nevyšly, toho si nebudeme všímat, že ne? :) Ale teď vážně:

## Psaní poznámek

Zamyslel jsem se nad tím, zda chci poznámky stále ještě psát. Hlavní důvod, proč jsem je psát začal, byl, abych si v pátek uvědomil, kolik jsem toho stihl, a neměl blbý pocit, že jsem nic nestihl. Abych si před víkendem vyčistil hlavu. To se ovšem časem, i díky poznámkám, spravilo a tyto pocity teď nemívám. Našel jsem si v práci rytmus, a to nejen v kalendáři a domácnosti, ale i ve své hlavě. Postupně jsem se dopracoval k několika zvykům, které mi pomáhají s pracovním týdnem:

- Administrativu dělám v pondělky a středy.
- Postování na sociální sítě jsem sladil s administrativními dny, tedy chtěl bych to dělat v pondělky a ve středy.
- Úterky, čtvrtky a pátky dělám soustředěnou práci.
- Pracuji z domova, ale ve čtvrtky chodím do [Atria](https://www.kafeatrium.cz/), abych měl nové podněty a doma mi nehráblo.
- O víkendu si nezakazuji chodit na Discord, ale čtu a píšu pouze do kanálu „volná zábava“, nezabývám se zbytkem (tzn. prací).

Také dítě začalo lozit, tak jsme o víkendu přestěhovali mé pracovní místo z obýváku do ložnice, za dveře. Zatím to funguje dobře, navíc dveře se dají nechat otevřené, pokud chci zachovat kontakt se světem a nebráním se návštěvám, nebo zavřené, pokud chci klid a soukromí (stejný trik nám fungoval kdysi na studentském bytě s kamarády).

Rozhodl jsem se, že poznámky nechci přestat psát. Jednak mi to pořád pomáhá uspořádat si myšlenky. Jako rituál se mi to líbí. Je to transparentní. Občas se do nich dívám jako do archivu, do deníčku. A je to dobrý marketing.

Poznámkám ale chybí „zvyk“ a s ním i rytmus a píšu je pak se zpožděním, dlouho a v náhodné dny. Zkusím tedy přidat do seznamu nový bod:

- Ať už hodlám v pátek dělat cokoliv, první věc, kterou z pracovních záležitostí udělám, bude sepsání a publikace poznámek.

## Dokončení robota na pracovní inzeráty

Bylo to už na spadnutí, no konečně jsem to dodělal. Už zbývalo poladit jen pár blbin ohledně spouštění všeho na CI, nějaké cachování a tak, ale pak už se to rozjelo. Obří Pull Request jsem mergnul s tím, že sice nemá moc testů a ještě spousta je toho potřeba dodělat, ale už se nutně potřebuji posunout na další úkoly, odpočinout si od toho po několika měsících a vrátit se ke _continuous delivery_.

To, co mám, jsem vyhodnotil za lepší, než to, co je na produkci, takže proč to nemergnout, že? Udělal jsem si Trello kartičky na věci, které chci pak ještě dodělat. Hlavně musím vrátit zpátky do codebase spoustu testů. Zatím to funguje a jsem s tím spokojený. Nejviditelnější změnou navenek je, že se stahují nabídky práce z více zdrojů.

Po tom, co jsem to konečně mergnul, tak jsem počkal, jestli vše funguje, a potom jsem na JG upgradoval spoustu knihoven, které jsem do té chvíle upgradovat kvůli merge konfliktům nechtěl.

V jeden den se objevila chyba, kterou jsem nepochopil a neměl jsem čas ji odladit a zjistit příčinu. Nechal jsem to na další den, ale to už se neprojevila a ani nikdy potom. Tak nevím, jestli erupce na slunci, ale zatím jsem se na to tedy vykašlal a budu to řešit, až když se objeví znovu.

## Vítání firem v klubu

Nové členy v klubu vítáme, ale firmy jsme dostatečně nevítali. Občas jsem nové partnery v klubu oznámil, ale bylo to nekonzistentní a netransparentní a vůbec.

V rámci plánu zviditelnit firmy v rámci klubu jsem vytvořil skript, který firmy v klubu automaticky vítá. Děje se to v kanálu „ahoj“, kde se představují i lidi.

Bylo by jednoduché udělat skript, který prostě oznámí novou firmu v okamžiku, kdy s nimi uzavřu partnerství a přidám si je do tabulky, ale to by jaksi pominulo těch zhruba 15 firem, které už klub dávno sponzorují. Takže jsem to udělal inteligentnější.

Umí to vítat firmy i zpětně. Neoznamuje firmy častěji než jednou týdně. Bere to od firem, kterým brzo vyprší členství, aby je to stihlo uvítat dřív, než budeme jednat o prodloužení. Pak pojede od nejnovějších firem po nejstarší. Až vyplýtvá zásobník, bude firmy vítat už prostě tehdy, kdy se nějaká objeví, nebo kdy to bude víc jak rok od posledního vítání.

Lidi z každé firmy mají už z dřívějška automaticky roli, skrze kterou je lze označit. Toho ve vítačce využívám, aby lidem z firmy přišla notifikace, že je bot vítá. Když bot (který se jmenuje „kuře“) vítá nějakou firmu, která sponzoruje už déle, přídá se navíc věta, která to vysvětluje:

> 👋 Kamarádi z **Inuits** se rozhodli podpořit klub a jsou tady s námi! Mají roli **@Firma: Inuits**. 🐣 Sice to píšu jako novinku, ale ve skutečnosti klub podporují už od 2.4.2021. Jenže tehdy jsem bylo malé kuřátko, které ještě neumělo vítat firmy.

K tomu je ještě Discord „embed“ s informacemi o partnerství, odkazem na firmu a obrázkem. Obrázek využívám ten, který už si dávno generuju ke každé firmě pro účely oznamování na sociálních sítích.

## Efektivní stahování avatarů

Na [stránce klubu](https://junior.guru/club/) nahoře je vždy pár náhodných avatarů. Pokaždé se stránka vygeneruje s jinými. Avatary se stahují z Discordu a původně se tak dělo pro všechny členy klubu. Kdo měl avatar, tam se avatar stáhl a až potom se náhodně vybralo těch pár, které se zobrazí.

V klubu je teď ale už přes 350 lidí, takže skript s avatary začal trvat nesmyslně dlouho na to, že jde jen o kravinu, která ústí v pár obrázků pro větší důvěryhodnost klubové stránky. Nechce se mi to teď hledat přesně, ale bylo to třeba něco jako 5 minut a to je teda dost.

Takže jsem to přepsal tak, aby se vzali všichni členové, zamíchali do náhodného pořadí a pak se z nich berou „dávky“ po třeba deseti. Tyto dávky se vždy paralelně postahují, čímž se zjistí, kolik avatarů se reálně stáhlo (spousta lidí žádný avatar nemá, nebo se jej kvůli síťovému problému nemusí povést stáhnout a byla by škoda skript nechat spadnout jen kvůli tomu). Po každé dávce se vyhodnotí, jestli už mám dost avatarů, třeba 30, a když jo, tak se skončí.

Teď ten skript trvá 0.4min.

## Vyúčtování studentů

Klub sponzorují dvě vzdělávací agentury, SDA a Engeto. Máme dohodu, že budou své (vybrané) studenty posílat do klubu. Student dostane 3 měsíce klubu zdarma jako bonusovou službu v rámci studia a agentura mi ty 3 měsíce proplatí.

Sliboval jsem si od toho hodně, ale u jedné agentury se to zatím ani moc nerozjelo a u druhé se to rozjíždělo pomalu. Ale pak se to rozjelo dost a nějak mě zaskočilo, kolik toho bylo. Zjistil jsem, že nejsem schopen to snadno vyúčtovat, že na to potřebuji nějaké skripty a způsob, jak si u lidí poznačit, že už jsem je fakturoval.

Na ten jsem už dřív nějak přišel, díky podpoře Memberful jsem zjistil, že ke členům klubu si můžu něco uložit přes API do políčka `metadata`, i když to bohužel nepůjde nijak vidět v administraci. Vymyslel jsem tedy jak bude probíhat procesně fakturace studentů a napsal jsem si skript, který zjistí, koho je potřeba fakturovat a vytvoří mi seznam. Ten mohu poslat agentuře a když si to potvrdíme, skriptem lidi označím jako fakturované.

Fakturu bych mohl vytvořit přes API, ale zatím jsem to nechal ručně, ono to nebude asi zas tak často.

Když jsem pracoval na tomto skriptu, přeuspořádal jsem složky a soubory i kolem dalších skriptů. Přišlo mi, že se mi [invoke](https://www.pyinvoke.org/) líbí méně a méně, protože mám tasků hodně a potřebuji si je různě organizovat do balíčků a potom mi přístup invoke přijde dost nepřehledný a magický. Zabránil jsem si zatím to přepsat celé do [click](https://click.palletsprojects.com/)u, ale jednou to asi udělám.

## Zarovnávání členství firem a lidí z těchto firem

Když jsem některým firmám prodával firemní partnerství, tedy členství v klubu, pozval jsem občas lidi od nich do klubu, aby si to okoukli, a až potom jsme rozjeli firemní roční předplatné. Jenže to teď začalo vytvářet problém. Lidem začalo končit jejich roční členství, ačkoliv firma má třeba ještě několik měsíců členství.

Přemýšlel jsem, jak to budu řešit, protože kupóny jsou na rok a lidi prostě dostanou kupón. A ten má svůj začátek a konec, který není nijak synchronizovaný s členstvím samotné firmy. Už jsem myslel, že to půjde dost složitě, až jsem si v administraci Memberful všiml, že mohu ručně editovat konec členství lidí. Mohu jej ručně natáhnout, jak potřebuji.

A to byl už jen krůček k tomu, abych vytvořil skript, který lidem z firem, kterým by členství končilo dřív, než skončí to firemní, natáhne členství tak, aby se to srovnalo. To elegantně řeší problém a dokonce to elegantně řeší i to, čeho jsem se trochu bál, a to jak budu jednotlivým lidem prodlužovat firemní předplatné, když firma své členství prodlouží. Takhle se automaticky prodlouží samo.

Pouze potřebuji do budoucna vyřešit způsob, jak označit lidi, kterým se prodloužit firemní členství nemá, protože např. z firmy odešli, nebo jej chce firma dát někomu jinému.

## Další poznámky

- Viděl jsem se konečně poprvé v životě naživo s [Markem z Hradce](https://blog.python.cz/ja-python-a-rosti), který měl cestu do Prahy.
- Na sociálních sítích jsem propagoval [nový díl našeho podcastu s Filipem z Appliftingu](https://junior.guru/podcast/) a svou [účast v podcastu ProgramHRování](https://www.programhrovani.cz/1843229/10212890-o-prvni-praci-v-it-s-honzou-javorkem).
- Na [stránku našeho podcastu](https://junior.guru/podcast/) jsem přidal děkovací větu o tom, kdo nám na míru složil znělku.
- Podal jsem přes datovku daňové přiznání.
- Ozvala se mi [Jessica]({filename}2021-06-17_jessica-upani-about-python-events-in-namibia-you-have-to-be-pure-in-terms-of-your-why.md), jestli nevím o vhodných speakerkách pro jejich meetup, tak jsem se pokusil nějaké dohodit.
- Volali jsme si s Nelou a dohodli [zveřejnění přednášky](https://youtu.be/6G4TKGQICw0) a ladili podobu nové stránky na JG, která se bude zabývat psychickým zdravím. Dělali jsme hlavně několik koleček revize budoucího textu. Přednášku jsem následně propagoval na sociálních sítích a upravoval jsem kód stránek, aby se dal zvlášť evidovat veřejný a klubový odkaz na video, protože tato přednáška má dvě verze (v klubovém záznamu je navíc záverečná diskuze s členy).
- Uzavřeli jsme partnerství spolu s STRV a Pure Storage. Ladíme detaily a rozjíždíme dohodnuté věci.
- Proběhly volby do rady [Pyvce](https://pyvec.org/) a zvolili mě :) Zůstávají dva původní členové výboru, tři budou noví. Paráda! Čerstvá krev! Aktuálně probíhá pomalé „předávání moci”. Podílel jsem se hodně na oživení spolku před pěti lety a jsem rád, že jsme to dotáhli až k volbám a tomu, že si spolek přebírá nová generace :)
- Prošel jsem dosavadní žádosti o stipendium a vyhodnotil.
- Volal jsem si s kamarádem z Red Hatu a bavili jsme se o tom, jak by mohli členství v klubu využívat víc naplno.
- Ozvala se šéfredaktorka z Heroine, jestli dodám poslední článek. Tak asi budu muset dodat. V klubu jsem otevřel brainstorming o tom, jak ten článek pojmout, protože jsem nikdy nic takového nepsal.
- Předělal jsem, jak v kódu importuju modely z balíčku. Je to teď víc psaní, ale je to jednodušší na přemýšlení a taky ty importy teď dokáže snadno napovídat editor. Protože po této změně byl v importech trochu nepořádek, doinstaloval jsem `isort`, nakonfiguroval a jednorázově importy nechal uspořádat. Zatím platí, že se neplánuji zdržovat lintery nebo formátovači kódu, isort bude jen na jednorázové použití „na přání“, až se mi zase bude zdát, že je v tom moc binec.
- Komunikoval jsem s autorkou dalšího podcastu, kde bych mohl vystupovat.
- Kontaktoval jsem dvě firmy, kterým bude brzo končit členství v klubu.
- Slíbil jsem organizátorům [pražského Pyva](https://pyvo.cz/praha-pyvo/), že na příštím srazu budu přednášet o JG. To budou zas nervy, ajaj! Možná přijde i Pája a udělá si _lightning talk_ na JG podcast. Dodal jsem organizátorům detaily k přednášce a do svého kalendáře jsem si rozplánoval přípravu.
- Vyřídil jsem až příliš mnoho emailů.
- Vedl jsem diskuzi s člověkem, který z klubu odešel, protože tam nenašel, co chtěl. Bylo to zajímavé a poučné, ale taky zas nemůžu prostě řešit problém všem. Měl specifické požadavky, jasné zaměření (užší než je zaměření klubu) a křehkou trpělivost. Naučil jsem se na tom aspoň správně s takovými lidmi komunikovat, abych zjistil, proč odešli, a abychom se rozešli v dobrém.
- Aktualizoval jsem na webu logo Software Development Academy na novou verzi, kterou teď mají. Konečně SVG!
- Přemýšlel jsem, zda a jaký smysl mají v klubu úzce zaměřené kanály na jednotlivé technologie, které spíš zejí prázdnotou, protože lidi většinou vyřeší co potřebují v obecnějších kanálech. Jasné závěry nemám, mít tam takové kanály má svá pro i proti.
- Zjistil jsem, že se mi na CI nestahují obrázky (loga firem) z exportu od StartupJobs. Doma jo. Šťoural jsem do toho a zjistil, že obrázky leží za nějakým Cloudflare, kde je asi zapnutá ochrana proti robotům nebo DDoS. Chvíli jsem to zkoušel obejít, ale pak jsem se na to vykašlal a napsal jim e-mail. Když je to export, tedy API, asi by mělo fungovat stahování obrázků, považuji to za bug :) Tak uvidíme, jestli to někdy spraví, nebo to budu muset časem vyřešit jinak.
- Našli jsme kluka, kterého chceme spolu s Mews podpořit v rámci speciálního stipendia. Bude to takový pilotní pokus. Volal jsem si s jejich rodiči a je to idální případ na to, co jsme chtěli dělat. Teď se snažíme domluvit další call, kde bychom klukovi věci předali a ještě víc se seznámili, ale byl nemocný, tak se to posunulo.
- Upgradoval jsem knihovny na projektech Pyvce, což tentorkát zahrnovalo i nějaké změny v kódu. Když jsem byl u toho, upgradoval jsem toho víc a [změnil](https://github.com/pyvec/pyvec.org/commit/fe3d0fe60cf1498b34edb193d4e8553500013869), jak se v kódu webu [pyvec.org](https://pyvec.org/) pracuje se závislostma.
- Volal jsem si se starým známým z firmy, která možná bude sponzorovat klub.
- Věnoval jsem se lidem v klubu, vítal nové členy, zapojoval se do diskuzí. Také jsem napsal pár tradičním členům, kteří už třeba mají práci a nezvládají tolik přispívat, soukromé zprávy, abych se zeptal, jak se mají. Nebylo to nic moc plánovaného, prostě jsem měl chuť se s nimi po delší době spojit.
- Během 14 dní od 26.3. do 8.4. jsem při procházkách nachodil 53 km. Celkem jsem se hýbal 18 hodin a zdolal při tom 53 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Napsat článek pro Heroine.
2. Domlouvat přednášky v klubu.
3. Připravit si přednášku na Pyvo.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Rozbité prasátko: Epizoda 40](https://rozbiteprasatko.cz/epizoda40) Jako teď jsem si to pustil a přišlo mi to fakt dobrý! :D
- [Na internetu sledujeme bolest druhých. Jak se vyrovnat s úzkostmi z války?](https://www.voxpot.cz/na-internetu-sledujeme-bolest-druhych-jak-se-vyrovnat-s-uzkostmi-z-valky/)<br>„…tragické zprávy v nás vyvolávají pocity ohrožení a ztráty kontroly. Navíc se přidává i bezmoc – nemůžeme tomu zabránit. Vše může vést k úzkosti nebo panickým atakám, a to i u lidí, kteří předtím žádné psychické problémy neměli.“
- [Nohavica jako oběť? Mluvit o návratu komunismu je nehorázné, říká hudební publicista](https://www.mujrozhlas.cz/rapi/view/episode/9fe68e69-ffd5-3c19-b62b-cbda69c1e7b3)<br>Pěkný díl o kontroverzích kolem Nohavici.
- [Většina světa ruskou invazi neodsoudila: „Chcete po nás solidaritu s Evropou, ale kdy jste vy stáli za námi?“](https://www.voxpot.cz/evropsky-dvoji-metr-aneb-proc-vetsina-sveta-neodsoudila-ruskou-invazi/)<br>„Mimo Západ si také lidé začali všímat konsternace některých médií z toho, že v Evropě probíhá válka. Tento údiv narážel na mylnou a ahistorickou iluzi, že v civilizované Evropě se přeci neválčí. Představy o morální nadřazenosti starého kontinentu, který své spory řeší mírově, však neodpovídají jednak případům nedávných válek, například v bývalé Jugoslávii, ale i faktu, že zdejší mocnosti stále válčí, jen boje se přesunuly mimo náš světadíl.“
- [Millennial History: Children of the Decree](https://anchor.fm/the-europeans/episodes/Millennial-History-Children-of-the-Decree-e1gc4ng)<br>Jak se žilo v Rumunsku za totality.
- [O práci na dálku se Zuzkou Šumlanskou a Honzou Králem — Vzhůru dolů podcast — Overcast](https://anchor.fm/vzhuru-dolu-podcast/episodes/O-prci-na-dlku-se-Zuzkou-umlanskou-a-Honzou-Krlem-e1e0i6l)
- [Stydíš se psát o podřadných genech? Vytáhni zeměpis. Za ruskou tyranii ale zima nemůže](https://www.voxpot.cz/stydis-se-psat-o-podradnych-genech-vytahni-zemepis-za-ruskou-tyranii-ale-zima-nemuze/)
- [Ep. 37 – Junior vs. Mid vs. Senior](https://wp.streetofcode.sk/podcast/ep-37-junior-vs-mid-vs-senior/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=ep-37-junior-vs-mid-vs-senior)<br>Líbí se mi, jak kluci tyhle pojmy probrali.
- [Red is dead: Russian anti-war protesters fly a new flag for peace](https://www.theguardian.com/world/2022/apr/03/red-is-dead-russian-anti-war-protesters-fly-a-new-flag-for-peace)<br>Krásná, ne кра́сная.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
