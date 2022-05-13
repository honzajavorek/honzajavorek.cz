Title: Týdenní poznámky #90: Změny v mentoringu a stream na YouTube
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (7.5. — 13.5.) a tak [stejně jako minule]({filename}/2022-05-06_tydenni-poznamky-89-podcasty-v-klubu-a-mentoring.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Mentoring

Během úterý jsem vymyslel, jak chci pojmout nový mentoring. Přejmenoval jsem kanál #mentoring v klubu na #poradna a vytvořil novou pravidelnou zprávu do kanálu #parťáci, která upomíná na možnost sehnat si přes klub mentora na dlouhodobější 1:1 konzultace. Ve zprávě je i krátký návod, jak k tomu přistupovat a co od toho čekat. Změn bylo víc, ale pro čtenáře poznámek, kteří detailně neznají klub, jsou spíš nerelevantní.

Mentory jsem si nově uložil do YAMLu a později během čtvrtka to předělal ještě tak, aby se mi to ukládalo i do SQLite a mohl jsem snadno data dotazovat (např. vytáhnout jen mentory, kteří nabízí i pohovory nanečisto atd.). Aktuálně je v klubu 14 mentorů, většina z Mews nebo Pure Storage, dva se přihlásili nezávisle sami. Další se mi už hlásí do soukromé zprávy.

Dalo mi dost práce celou zprávu naformátovat tak, aby se v ní dalo vyznat a bylo tam vše podstatné. Chtěl jsem se vyvarovat užívání mentions v tzv. embedu zprávy, protože to na straně Discordu blblo a často se místo jmen lidí zobrazovaly jen jejich ID čísla, což bylo matoucí. Pracuji teď spíše s `display_name` členů. Většina mentorů má nějakou rezervaci časů přes Calendly apod., takže nevadí, že na ně není přímý proklik. U několika je ale kontakt jen přes Discord a je smutné, že proklik nejde snadno udělat. Napsal jsem tam aspoň jejich _tag_, tedy takové to „honza#1234”, přes co by mělo být možné je ručně najít a napsat jim, ale je to neobratné a neintuitivní. Podobné změny bych chtěl udělat i v dalších zprávách od bota, kde se dělá mention na lidi, aby se už nikde neprojevovala ta chyba s čísly.

Do zprávy jsem se taky snažil co nejstručněji zachytit co vlastně tento 1:1 mentoring je, co od toho čekat a jak s tím pracovat. Pomohl jsem si [přednáškou od Anny Ossowski](https://github.com/honzajavorek/become-mentor), kterou bych časem chtěl nějak vložit i přímo na web JG. Do zprávy jsem sepsal jen pár bodů:

- Stanov si dlouhodobější cíl, kterého chceš dosáhnout (např. porozumět API)
- Podle tématu si ze seznamu níže vyber mentorku/mentora. Rezervuj si čas na videohovor
- Domluvte se, jak často si chcete volat (např. každé dva týdny) a jak dlouho (např. 5×)
- Aktivita je na tvé straně. Rezervuješ další schůzky a víš předem, co na nich chceš řešit
- Mentorka/mentor radí, posouvá tě správným směrem, pomáhá ti dosáhnout cíle

A pak ještě že mentoři jsou dobrovolníci, ne učitelé a ať si lidi váží jejich času a dopřejí jim dobrý pocit, pokud pomohli. Určité formulace jsem volil i na základě feedbacku, který jsem dostal z Mews o tom, jak dosavadní mentoringová sezení probíhala. Také jsem měl hodně poznámek z Mezikomunitního sdílení na téma mentoring, což je občasný videohovor s lidmi z jiných českých komunit, kde sdílíme know how.

Z těchto poznámek vyplývala i spousta kroků, které bych mohl ještě dělat, např. ručně propojovat mentory a mentorované podle vyplněných dotazníků, dělat webináře pro mentory i mentorované, dělat rozhovory s mentory a mentorovanými o jejich zkušenostech z programu, vyzývat svou komunitu k tomu, aby v ní lidi mentorovali a to třeba i ti, kdo nejsou zas tolik zkušení. Ale tyto věci jsou podle mě z kategorie „mentoring je můj hlavní produkt“ a mohou si je dovolit třeba React Girls, Czechitas, nebo Femme Palette. Já potřebuji něco víc při zemi, co bude fungovat _dostatečně dobře_ a bude nějak škálovat bez ohledu na moje zapojení. Mentoring zatím není můj hlavní produkt, je to jedna z mnoha věcí, které se v klubu dějí. Budu doufat, že kvalitu mentorů zajišťují firmy, které je k tomu přemluvily, nebo samotné prostředí v klubu, pokud jsou přímo z klubu. Budu se snažit sbírat aspoň nějaký feedback, abych aspoň tušil, jestli je někde nějaký průšvih.


## Intro Pure Storage

Ve středu večer měla být akce v klubu, kde představím změny v mentoringu, vysvětlím co je v ideálním případě mentoring a představíme Pure Storage a mentory od nich, ať jsou to pro lidi v klubu reálné tváře. Udělal jsem si poznámky, co chci říkat a následně i jednoduché slajdy, abych se držel osnovy. Podobnou akci chci v budoucnu zopakovat s Mews.

Jak jsem už psal, chtěl jsem zkusit streamování přímo na YouTube, které má urychlit vytvoření záznamu přednášky a zároveň zajistit, že pokud by se náhodou chtělo připojit více jak 25 lidí, což je limit Discordu na video call, tak mohou stále vidět přednášku, protože jim pošlu odkaz na YT stream.

U této příležitosti jsem si dal konečně tu tříminutovou práci a nastavil [správný poměr stran nahrávaného videa v OBS Studio](https://influencermarketinghub.com/youtube-video-size/), takže se video nebude podivně tísnit na YT stránce a jeho úvodní obrázek nebude ošklivě napozicovaný a rozmazaný.

Streamování už jsem měl na YT zapnuté a povolené, tak jsem zkusil něco nahrát přes webkameru a pak i přes OBS Studio. Bylo to jednoduché. Šel jsem tedy do kódu JG a smazal vše související se „zrcadlem“, z JavaScriptu, CSS, i [textů na stránce pro speakery](https://junior.guru/speaker/). V hlasové místnosti na přednášky jsem uvolnil oprávnění, protože teď už není potřeba nic nikomu zakazovat.

Během středy jsem si ještě uvědomil, že potřebuji jak přednášet a sdílet obrazovku, tak nahrávat (streamovat), a že mám jen jeden displej. Takže jsem si zkoušel různé překliky a jak přesně sdílet okna, co dělat a co nedělat, abych se v tom v průběhu přednášky nezamotal. Myslím, že to mělo velký vliv na kvalitu výsledku, bez této zkoušky bych se v tom rozhodně zamotal a měl velkou paniku.

Samotná akce proběhla moc hezky a bez problémů, myslím, že to bylo přínosné a milé. Záznam se podařil a je celkem sledovatelný, ale obraz se seká. Na mluvící hlavy je to asi jedno, ale kdyby někdo dělal live coding a psal písmenka na obrazovku, už by to bylo horší. Taky YouTube mi napsalo hromadu chyb souvisejících s tím, že se tam snažím sice něco tlačit, ale netlačím dost. Diskutoval jsem o tom pak v klubu s [Tomášem Maňhalem](https://www.linkedin.com/in/tomasmanhal/), členem klubu, který má se streamováním zkušenosti, a ten mi poradil ještě spoustu tipů a dal užitečné odkazy na to, jak to do budoucna vylepšit (díky!):

- [Choose live encoder settings, bitrates, and resolutions](https://support.google.com/youtube/answer/2853702?hl=en#zippy=%2Cp%2Cp-fps)
- [Suggested Upload Speeds for Streaming](https://support.boxcast.com/en/articles/4235072-suggested-upload-speeds-for-streaming)
- [Streaming Bitrate Calculator](https://www.omnicalculator.com/other/streaming-bitrate)

Taky bych si mohl pustit nějaká videa o streamování, která pracují specificky s macOS a M1, což mě předtím, nevím proč nenapadlo. Třeba [tohle](https://www.youtube.com/watch?app=desktop&v=8S3jf-ahLe0). Celkově z toho ale vyplývá hlavně to, že bych si měl sehnat lepší internet, upload 5 Mbit/s na to, abych někam protlačil retina obrazovku, nestačí.

Lepší internet je varianta a ani ne složitá na vyřešení, ale osobně bych radši poslal peníze Discordu za to, že mi dá limit lidí na video callu na 50 a nebudu muset řešit žádný stream. Nechci si z bytu dělat nahrávací studio, protože se nechci vázat na svůj byt. Už jednou jsem dělal v klubu přednášku, když jsme byli na několikadenní návštěvě u kamarádů. Co když někam pojedeme na měsíc? Co když pojedeme ke tchýni, která má nějaký bídný vesnický internet? A podobně jako u mentoringu, přednášky nejsou můj primární produkt, je to jen jedna z mnoha věcí, které se odehrávají v klubu.

Věci v klubu musí škálovat a nesmí mě moc omezovat v životě. Proto nemám runtime a vše jede na CI jednou denně. Proto nemám studio se závěsy, pěti kamerami a mikrofony. Snažím se věci dělat tak akorát _good enough_, aby výsledek sloužil lidem a já se z toho nepo… Takže zkusím ještě poladit do nastavení streamu, nastuduju si další detaily a uvidíme.


## Vylepšování mentoringu

Po intru Pure Storage jsem začal pomalu dál vylepšovat mentoring. Doprogramoval jsem, aby bot dával mentorům roli „Mentoruju“ a vytvořil privátní kanál, kam mají přístup jen mentoři a moderátoři, a kde mohu sbírat zpětnou vazbu, nebo tam můžeme řešit případné problémy.

Dále jsem si připravil půdu pro zprávu, která by se mohla objevovat v kanálu #pohovory a upozorňovat na to, že v klubu jsou mentoři, kteří nabízí pohovory nanečisto a přípravu na pohovor.

Mezitím jsem ve sprše vymyslel, jak předělat zprávu s mentory tak, aby to nebyla nekonečná nudle a aby šlo vyřešit neprokliknutelné mentions. Bude to trochu víc programování, ale očekávám, že mentorů bude spíš přibývat i z řad dalších členů klubu a bude lepší, když to bude už teď robustnější. Chtěl bych vytvořit samostatný kanál, kde bude jen seznam mentorů a návod. Bude jen pro čtení. Každý mentor bude mít svou vlastní zprávu a bot ji bude aktualizovat podle informací v YAMLu. Jsem zvědavý, zda se mi to povede vytvořit a zda to bude fungovat, jak bych chtěl.

Mám v plánu v nejbližší době přidat: vylepšený výběr mentorů, jinou pravidelnou zprávu do kanálu #parťáci, pravidelnou zprávu do kanálu #pohovory, pravidelnou zprávu do kanálu #poradna. Dále novou kapitolu do příručky na téma mentoring a ještě jednu kapitolu, na téma jak se ptát. A všechno to provázat.


## Další poznámky

- Zavolal jsem si s Veronikou Pizano z Aj ty v IT a bavili jsme se o tom, jak bychom mohli spolupracovat. Největší smysl dává, abych přidal podporu do třídícího robota pro slovensky psané nabídky práce a pokryl tak SK trh s nabídkami práce pro juniory. Zkusí mě spojit s někým z Profesia.sk. Další checkpoint bude po 18.5. až 19.5., kdy jsou nějaké Profesia Days. Já bych měl do té doby vymyslet plán, jakým by se dalo postupovat z mé strany.
- Přidal jsem si do svého zálohovacího skriptu složky s nastavením OBS Studio, protože jsem přesvědčený o tom, že kdybych o to nastavení přišel, už to nikdy nebudu schopný dát zase dohromady.
- Prošel jsem _watchtower_, funkci 1Passwordu, která mě upozorňuje na potencálně uniklá hesla. Všude jsem si hesla změnil, bylo to asi 5 služeb. Díky tomu jsem se konečně dostal do jednoho účtu, kam se mi nedařilo už roky dostat. Služba totiž chtěla ověření, že jde opravdu o mě, ale nikdy mi nepřišel ověřovací kód na mail. Teď mě napadlo kouknout se do filtrů v emailové schránce a našel jsem tam nějaký filtr, zřejmě vytvořený kdysi ze zlosti, který všechny maily z této služby mazal…
- Kluky ze [Street of Code](https://streetofcode.sk/) a Alenu z [(re)štarty v IT](https://restarty.dev/) jsem pozval do klubu.
- Sociální sítě: promo podcastu Street of Code a jejich dílu s robime.it, potom promo [svého posledního článku pro Heroine](https://www.heroine.cz/zeny-it/8100-jak-jsem-se-stal-ambasadorem-zacatecniku-v-it-zakladatel-junior-guru-o-vyhodach-komunity-a-sdileni)
- Klub, maily, a tak dále.
- Během 7 dní od 7.5. do 13.5. jsem naběhal 6 km, při procházkách nachodil 8 km. Celkem jsem se hýbal 5 hodin a zdolal při tom 14 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Vylepšovat mentoring.
2. Domyslet spolupráci s Engetem a ozvat se jim.
3. Připravit popis následující přednášky v klubu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Dovolená je změna stavu mysli – nezáleží, kde jste, říká fotografka, která se rekreovala na Sídlišti Ďáblice](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F09%2Fdovolena-je-zmena-stavu-mysli-nezalezi-kde-jste-rika-fotografka-ktera-se-rekreovala-na-sidlisti-dablice%2F&h=d4e378d87e6a8d65b58e5a10fded00aeec4b727165674ad05ed728136e3d2331)<br>Třeba někdy zkusím :))
- [The 2022 Market Crash - Why is Everything Down?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DddWr9dPGqDA&h=f344f5407913c81e36f57fd78713b238157025b74a3d3b45b641ac73797bc6a2)<br>Co se děje s trhy?
- [Bořiči dezinformací. Dáváme lidem argumenty proti nesmyslům, vysvětlují autoři projektu Ověřovna](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BRZMiLLLVk&h=4b7ccc4b28d011bbb4ae8ac1fe86c3bcaf9332933e5fc2b27ef0bf45ebae8ff2)<br>Super.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
