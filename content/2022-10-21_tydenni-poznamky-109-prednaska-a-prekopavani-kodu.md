Title: Týdenní poznámky #109: Přednáška a překopávání kódu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (15.10. — 21.10.) a tak [stejně jako minule]({filename}/2022-10-14_tydenni-poznamky-108-prednaska-tipy-infrastruktura.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Přednáška s Matějem Kotrbou

[Matěj Kotrba](https://www.linkedin.com/in/mat%C4%9Bjkotrba/) měl v klubu přednášku a na rozdíl od minulého týdne se na akci přihlásilo skoro 50 lidí a přišlo 22. Asi téma „jak se připravit na pohovor“ holt táhlo víc. Slabá návštěva minulé přednášky mě stále mrzí, ale na YouTube už má přes 30 shlédnutí, tak asi nakonec dobrý a jsem rád, že se lidi mezitím trochu rozhýbali a na Matěje dorazili, a to dokonce i přesto, že veřejně jsem jeho přednášku propagoval až den předem.

Hrozilo, že se dostaneme přes limit Discordu na účastníky video hovoru a že se použije online stream, který dělám na YouTube, ale nakonec jsme se vešli do 25 lidí a nepoužilo se to. Matěj měl velký prostor pro dotazy a ty pršely, takže to celé mělo skoro dvě hodiny.

Na začátku přednášky jsem zazmatkoval a přepl špatně okno při výběru toho, co chci natáčet v OBS. Jenže pak to nešlo naklikat zpět, nešlo vybrat to okno, které jsem potřeboval. Klikal jsem tak dlouho, až jsem to vzdal a začal prostě nahrávat celý svůj Discord, ne pouze pop-up s videohovorem, nedalo se nic dělat. Druhý den jsem to nějak spravil, aby to bylo pro příště zase nastaveno správně.

Před přednáškou a i po ní jsem si aktualizoval [seznam úkonů](https://junior.guru/event/), které potřebuji v souvislosti s akcí v klubu udělat. Dal jsem si ho nově ne do GitHub Gistu, ale na samostatnou „tajnou“ stránku přímo na webu. Přijde mi, že je těch úkonů strašně moc a že je čistě statisticky vyloučeno, abych při každé přednášce neudělal nějakou chybu z nepozornosti. Budu muset něco z toho automatizovat.

Při té příležitosti jsem přidal na web podporu pro to, že mohu u libovolné stránky v Markdownu snadno nastavit, aby nebyla indexována vyhledávači. To jsem u této nové stránky rovnou využil.


## Zpětná vazba

Na základně „zpětnovazebního“ tipu, který teď chodí lidem, mi někteří začali psát zpětnou vazbu na klub. Někteří to jen odklikli a nic nenapsali :(

Každopádně jsem si uvědomil, že tahle zpětná vazba bude spíš kvalitativní než kvantitativní, nebo minimálně něco mezi. Vede spíš ke konverzaci nebo k promyšleným odpovědím, které neumím zpracovat nějak hromadně, ale jsou velmi zajímavé. Uvědomil jsem si, že jsem chtěl zpětnou vazbu, ale teď úplně nevím, co s ní. Pozitivní bych si měl někam zapisovat a z negativní bych měl možná dělat Trello kartičky s úkoly. Každopádně něco si zapíšu sem:

> Příjemně mě překvapila aktivita lidí. Tady se furt něco děje, ve středu bude přednáška, v prosinci Advent of Code. Člověk se tu prostě necítí sám. Jo a taky se mi líbí výrobky. Tam ze zvědavosti hodně ráda koukám.

> Připojit se do klubu mě přesvědčily až Honzovi týdenní zápisky 😃

> O junior.guru mám povědomí už od začátku léta. Vím, že jsem na něj narážela, když jsem si mapovala juniorní pozice. A taky už nějakou dobu poslouchám podcast. A právě si nejsem jistá, co z toho bylo dřív.

> Hodně oceňuju možnost si nějaký příspěvek označit špendlíkem. To je fakt dobrá vychytávka!

> Vím, že jsem četl příručku a začal jsem tě sledovat na různých sociálních sítích a tam jsem narazil po nějáké době na výzvu ohledně Discordu.

A na kvantitativní zpětnou vazbu pak musím asi zavést jen nějaké rychlé a jednoduché hlasování přes emoji. Jinak se asi nedovím, co mi do klubu přivádí lidi a co můžu zrušit - jestli je to Google, podcast, osobní doporučení, nebo moje statusy na Instagramu.


## Překopávání kódu z invoke na click

Z minulého týdne jsem se těšil, že převedu na [click](https://pypi.org/project/click/) celou „synchronizaci“ JG, což je soustava skriptů, které se každý den spouští na CI a stahují a posílají data.

Musím říct, že mě click nadchnul. Myslel jsem, že je to overkill, ale je jednoduchý a zároveň dává člověku si cokoliv udělat podle sebe. Mohu tam udělat vše jako v [invoke](https://pypi.org/project/invoke/), ale vlastně o mnoho víc a transparentněji a méně magicky. Základní kód jsem měl celkem rychle, ale je to trochu naprasené, tak to ještě budu refaktorovat. Knihovnu invoke jsem následně definitivně odstranil z kódu.

Koukal jsem pak na [Shell completion](https://click.palletsprojects.com/en/8.1.x/shell-completion/). Říkal jsem si, že by bylo super, kdyby mi to při vývoji napovídalo názvy skriptů a nemusel bych je stále vypisovat. Ale i když se mi to po různých peripetiích povedlo nějak rozchodit, bylo to nějaké strašně pomalé a vzdal jsem to. Taky jsem kvůli tomu musel [nainstalovat novější Bash](https://dev.to/bphogan/use-modern-bash-shell-on-macos-22a6), protože ten výchozí v macOS je údajně nějaký prehistorický (ne že by mě to doteď omezovalo).

Rozhodl jsem se, že dělení synchronizace na „hlavní“ skripty a pak část, kde se stahují pracovní nabídky, a pak nějakou část, která vše spojuje dohromady, opustím. Že to stejně neodpovídá časově, protože pracovní nabídky jsou teď moc rychlé a ta hlavní část je moc pomalá a chtělo by to paralelizovat jinak. Takže by se to, když už do toho rýpu, hodilo udělat obecněji a využít i [paralelizaci, kterou má v sobě přímo CircleCI](https://circleci.com/blog/how-to-boost-build-time-with-test-parallelism/).

Když jsem měl systém příkazů, které reprezentují jednotlivé skripty a u každého jsem měl vydefinované závislosti, tak už zbývalo jen naprogramovat funkci, která mi z toho „vypočítá“, které skripty mohou jet paralelně, protože na sobě nezávisí. Tuto funkci jsem psal „pouze“ půl dne a stal jsem se při tom mistrem práce s množinami v Pythonu.

Na základě výsledku téhle funkce jsem udělal příkaz, který tyto _chains_, jak jsem to pojmenoval, vypíše každý na nový řádek. To předhodím CircleCI a opravdu to funguje, [pouští se to paralelně](https://app.circleci.com/pipelines/github/honzajavorek/junior.guru/6156/workflows/cf6ebfa0-ddc9-47dd-9981-c7bac33b6cd6/jobs/32349/parallel-runs/1?filterBy=ALL)!

Škoda, že to také vytvoří tři nebo čtyři paralelní databáze, složky s obrázky, nebo cache pro Scrapy… takže jsem začal řešit, co s tím, jak to sesbírat, jak to přesunout do další fáze buildu, a jak to v ní sloučit do jednoho výsledku. Naprasil jsem nějaké dva příkazy `jg data node` a `jg data merge`, které hlavně kopírují soubory z místa na místo. Skoro to vypadá, že to funguje, ale můj primitivní přístup ke sloučení paralelně vytvořených databází je asi moc primitivní a další fáze buildu si stěžují, že jim chybí tabulky. Dál jsem se zatím nedostal.

Taky je trochu problém, že prakticky všechno z různých důvodů závisí na jednom skriptu, který zjišťuje informace o obsahu Discordu. Nemá moc smysl to pak paralelizovat. Tento skript bude potřeba vytáhnout před všechny ostatní a pak se to dá paralelizovat krásně, skoro do deseti „uzlů“, jak jim říká CircleCI. Jenže jak si zase předat tu databázi a jak ji pak sloučit?

Je to zapeklité. Nemyslím si, že bych měl opustit SQLite jako místo, kde se ukládají data a kde si je skripty čtou. Na druhou stranu, sdílet SQLite mezi různými mašinami a nějak ji rozdělovat a slepovat, to se zdá nebude zrovna jednoduchý úkol. Pár nápadů mám, ale žádný mi nepřijde úplně úžasný. Mám víc šermovat s [sqlite-utils](https://sqlite-utils.datasette.io/) a ukládat věci jako JSON soubory a slepovat je a rozdělovat je? Mám pro přenos tabulek použít SQL dump?

A protože dělám _continuous delivery_, tak mi teď nefunguje CI a padá to a bude to padat do pondělí, nebo do dne, kdy budu mít čas s tím nějak pohnout.


## Další poznámky

- Do skriptu, který vyhodnocuje palečky a srdíčka pod příspěvky, jsem přidal podporu pro emoji s různou barvou kůže, tedy aby se růžové palce započítaly stejně jako žluté, nebo tmavě hnědé. Musím říct, že když jsem do toho začal vrtat, tak mi [vybuchla hlava z toho, co všechno tenhle problém zahrnuje](https://github.com/carpedm20/emoji/issues/204), ale naštěstí mě zajímá jen zlomek té věci a nějak jsem to nakonec díky knihovně [emoji](https://pypi.org/project/emoji/) vymyslel. Nejdřív emoji převedu na text a pokud v sobě má „skin tone”, tak to ořežu a z textu vytvořím zpět emoji. Tím získám z barevných palečků žluté a počítám žluté.
- Uvažoval jsem, že mi už nevyhovuje nastavení administrativních dní na maily apod. a dní na hlubokou práci, tedy programování a psaní. Jako admin dny mám pondělky a středy, ale přednášky jsou většinou v úterý a zabijou většinou celý den. Ve čtvrtky chodím do kavárny a buď se tam nedokážu soustředit na hlubokou práci, protože na mě mluví kamarádi, nebo to dokážu, ale kamarádi vypadají zklamaní, že si s nimi nepovídám. Takže s tím asi nějak zamíchám.
- Po přednášce s Matějem mi neplánovaně napsal kamarád, že potřebuje emoční podporu a šli jsme na pivo, ačkoliv jsem byl už dost zničený. S pivem jsem to pak přehnal a během středy jsem měl trochu kocovinu a trochu dost deficit spánku. Neměl jsem následně vůbec chuť přijít na [pražské Pyvo](https://pyvo.cz/praha-pyvo/) v ten den večer.
- Volal jsem si s jednou firmou. Aktuálně nebudou prodlužovat spolupráci, protože nemají kam dát juniory, dáme si vědět na začátku 2023. S jinou firmou zase jednáme po mailech o nejvyšším tarifu.
- Jedna juniorka, kterou jsme spolu s Mews podpořili stipendiem, si našla práci.
- Jeden kluk, kterého jsme spolu s Mews podpořili stipendiem, to vzdal a nic z toho nebude. Takový je život.
- Můj oblíbený Aerovod se sloučil s [KVIFF.TV](https://kviff.tv/), což nevím, jestli je dobře nebo špatně, ale věnoval jsem 30 minut tomu, abych podle toho upravil svou aplikaci na evidenci filmů v Trellu, [film2trello](https://github.com/honzajavorek/film2trello).
- Po přidání diagnostických příkazů do buildu na CircleCI se toto pondělí neopakovala chyba s porušenou databází. Ale pak jsem kód buildu stejně zase rozvrtal a databázi budu řešit všelijak jinak, takže je to už asi stejně bezpředmětné.
- Odpovídání v klubu, maily, a tak dále. Tohle mi zabralo snad dva celé dny z tohoto týdne. V klubu se toho dělo nějak hodně.
- Úspěšně jsem si většinu týdne blokoval sociální sítě a čas jsem na nich trávil zcela minimálně.
- Během 7 dní od 15.10. do 21.10. jsem při procházkách nachodil 4 km, na túrách nachodil 17 km. Celkem jsem se hýbal 7 hodin a zdolal při tom 21 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/). Nabídky práce pro juniory teď inzerují: [Monitora media, s.r.o.](https://junior.guru/jobs/2b1ab731247b03b291bd7c4a0177e052df5ae4a5937144b4f2ce9d11/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/215426887eaaad9105ecf647d0ff24cf94de7c9eb47cc6f2c55e6921/)


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Dokončit rozvrtané spouštění skriptů, opravit build, předsunout jeden ze skriptů a rozchodit paralelizaci.
2. Propagovat novou epizodu podcastu.
3. Napsat zase nějaký ten tip pro nováčky v klubu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Lucka Gurellová: Dřív než uměla číst a psát, tak začala programovat](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BoxWiakock&h=3c28c73d42de218b87def01bcde008f1988c9c1da2adffba54ce8996fa7a0ff7)<br>„Bylo mi 11, ale všechno pokročilé programování pro děcka začínalo až od 15…“ :D Hustý.
- [Pod čarou : Radíte chudým, jak šetřit? Nejprve zjistěte, jak žijí.](https://getpocket.com/redirect?&url=https%3A%2F%2Fseznam-zpravy.u.mailkit.eu%2Fmc%2FVVCQVPWV%2FVVPFMXVSZGRZZYZJLB%2FCCIPMIIQMEC&h=12e97483803d2b63ddaf06dedaea946f3865ee29da006fb08c5e450b593ff615)<br>„Nejsou úspory jako úspory, a ekonomické strategie jedné společenské vrstvy se nedají automaticky aplikovat na jinou.“

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
