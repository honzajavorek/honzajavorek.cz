Title: Týdenní poznámky #71: Simple Analytics, čistka v kódu, psaní článku
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (18.10. — 24.10.) a tak [stejně jako minule]({filename}/2021-10-17_tydenni-poznamky-70-nova-prirucka.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Zrušení starého ceníku a Simple Analytics

Po překlopení příručky na Markdown a nový design mi přišlo nejlepší vyčistit oblast kolem stránky https://junior.guru/hire-juniors/, kde byl ceník pro jednorázové nabídky práce a pod ním ceník sponzorství příručky firemním logem. Tři čtvrtiny ceníku už nebyly tak úplně v platnosti, polovina textů nebyla zcela aktuální. Rozhodl jsem se stránku úplně odebrat. To spustilo jakýsi efekt padajících kostek domina, resp. stránek a kódu, které jsem mohl _konečně_ smazat.

### Simple Analytics

Na stránce byla čísla o návštěvnosti. Rozhodl jsem se konečně zkusit [Simple Analytics](https://referral.simpleanalytics.com/honza-javorek) a [zveřejnit kompletně návštěvnost junior.guru](https://simpleanalytics.com/junior.guru), nepatlat se s nějakými jednotlivými čísly. Jak jsem [psal na Twitteru](https://twitter.com/honzajavorek/status/1451243454558781449), konečně vidím na jeden klik jakou mám návštěvnost, nemusím řešit žádné cookies, mohu mít veřejnou nástěnku s grafy. A má to import z Google Analytics. Dokonce se mi povedlo nasměrovat měřící skript přes vlastní doménu, takže by jej teď už neměly blokovat adblocky (nejde o žádné trackování, jen zcela anonymní počítání návštěvnosti, navíc pokud si v prohlížeči zapnete [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track), SA to respektují a nezapočítají nic). Zatím spokojenost. Pokud chcete vyzkoušet, s [tímto odkazem](https://referral.simpleanalytics.com/honza-javorek) budete mít o měsíc delší trial.

Google Analytics jsem zatím nevypnul, k tomu bych musel udělat ještě několik úkonů. Jejich API používám na různých místech a potřebuji ověřit, co mohu smazat a co mám předělat na Simple Analytics.

Veřejné statistiky se mi také budou hodit pro nadcházející [přednášku na OpenAltu](https://www.openalt.cz/2021/program_detail.php#event_7).

### Ceník v Google Docs

Textové informace z původní stránky jsem zatím hodil na konec [aktuálního ceníku](https://docs.google.com/document/d/1keFyO5aavfaNfJkKlyYha4B-UbdnMja6AhprS_76E7c/), který mám v Google Docs. Přidal jsem i některé informace, jež bych chtěl na budoucím ceníku mít, jako např. jednu _case study_.

Celkově jsem nynější ceník aktualizoval, např. místo natvrdo napsaných čísel tam přidal odkaz na veřejné Simple Analytics. Mám pocit, že některé části ceníku jsou teď ale zbytečně „ukecané“. Zestručním jindy.

Na původní stránce byly _testimonials_ lidí, kteří chválili příručku. Uložil jsem si je pro případ do Trella a některé přidal do aktuálního ceníku. Nechtěl jsem, aby jej příliš znepřehlednily, tak jsem si chvíli hrál s formátováním. Výsledek asi žádný úžas, ale zatím _good enough_.

Uvažoval jsem, zda do ceníku přidat odkaz i na formulář pro zadávání jednorázových inzerátů a celkově zda se tam o tom zmínit pro úplnost, ale nakonec jsem se rozhodl to záměrně neudělat, protože chci firmy od těchto jednorázových inzerátů teď spíš odrazovat, než pracovní nabídky na JG přebuduji (viz dále).


### Změna zadávání jednorázových inzerátů

Udělal jsem veletoč v oblasti zadávání jednorázových nabídek práce, který jsme před časem vymysleli s investorkou. Trápilo mě, že tarif Komunita, který byl zadarmo, využívala spousta standardních firem. Zavedl jsem jej proto, abych nalákal k zadávání i neziskovky a malé projekty a aby firmy, které spolupracují s PyLadies, inzerovaly zdarma. V reálu neziskovky [kromě Česko.Digital](https://cesko-digital.atlassian.net/wiki/spaces/CD/pages/87458200/Koho+te+hled+me) žádné pozice nemají, malé projekty na mě kašlou a radši to napíšou někam do Facebookové skupiny, firem od PyLadies je minimum.

Ze začátku jsem firmy konfrontoval s tím, zda mohou nějak prokázat, že si tarif Komunita zaslouží, ale poté jsem to vzdal, protože to bylo víc práce, než nabídku prostě přijmout a zkontrolovat pouze to, zda je opravdu juniorní a přeformátovat její text do Markdownu. Tato práce mě ale štvala, nebavila a i za cenu 500 Kč, což byl standardní placený inzerát, jsem ji vlastně nechtěl moc dělat.

Nějaké roční paušály pro firmy také nikdo nevyužíval. S velkými firmami jsme našli lepší nástroj spíše v dlouhodobých inzerátech, které paušálně odchytávají zájemce, např. zde [Red Hat](https://junior.guru/jobs/215426887eaaad9105ecf647d0ff24cf94de7c9eb47cc6f2c55e6921/) nebo [Credo](https://junior.guru/jobs/356c084cae33eaaffec2ab9c79fb583f7c1271f730acc612fa2dbfb8/).

Takže jsem to teď celé změnil. Paušály jsem zcela odstranil a zavedl jednu jedinou cenu za inzerát, 1.119 Kč za kus za 30 dní. Je to stejná cena, jakou má roční individuální členství v klubu. Když tedy firma zadá inzerát, bude to psychologicky přesně za částku, kterou by mi jinak člen v klubu vydělával celý jeden rok. A to už by mě mohlo motivovat k tomu, abych na to mrknul. Je to možná trochu moc, ale cílem je jednak necítit se jako _shit_ vždycky, když v emailu uvidím nový inzerát a zároveň chci vlastně firmy trochu odradit.

Jednorázové nabídky práce zadané přes JG mi totiž dělají úplně minimální zlomek příjmů a proto mají nejnižší prioritu v mém podnikání. Mám nějaký plán, jak je celé oživit a předělat, ale k realizaci toho plánu se dostanu třeba až v horizontu půl roku. Do té doby je to něco, co mi spíš přidělává starosti. Navíc je nabídek dost i z jiných zdrojů. Pokud firma zadá nabídku např. na StartupJobs nebo na LinkedIn a bude podle mého robota dost juniorní, u mě na webu se objeví, junioři ji najdou, a já s tím přitom nemám žádnou práci.

Nabídky zdarma jsem vyřešil novým políčkem ve formuláři, kam lze zadat kupón se 100% slevou. Kupón jsem dal k dispozici PyLadies skrze Pyvec Slack. Tento kupón budu kontrolovat pouze ručně pohledem, ale myslím, že to bude stačit. Navíc takto mohu podpořit i jiné komunity.

Mohl jsem dočasně přijímání nových nabídek úplně zavřít, ale říkal jsem si, že když se někde zavře krám, lidi si tam odvyknou chodit. A to bych nechtěl. Moje plány se zadáváním inzerátů přímo na JG počítají, i když v jiné a zjednodušené podobě. Tak zkusím co udělá, když to „nesmyslně“ zdražím.

S výše uvednou změnou jsem také musel upravit kód, aby správně četl tabulku s odpověďmi z formuláře a správně vyhodnocoval na jakém tarifu je jaká nabídka, a to jak historicky, tak pro nové inzeráty.

### Formulář, upsells, emaily

Všude, kde se odkazovalo na stránku https://junior.guru/hire-juniors/ jsem začal odkazovat přímo na formulář pro zadávání inzerátů a důležité informace jsem dal přímo do něj. Navíc jsem do něj dal i otázku, zda si firma přeje stát se členy klubu a odkaz na aktuální ceník firemního členství. Tentýž tip jsem přidal na konec emailů se statistikami přístupů na vyvěšené nabídky práce, které chodí inzerentům. To je mimochodem jedno z míst, kde se používají Google Analytics, ale možná by i to šlo nahradit veřejnými čísly od Simple Analytics, stačilo by tam dávat [permalink s vyfiltrovanou konkrétní stránkou](https://simpleanalytics.com/junior.guru/jobs/215426887eaaad9105ecf647d0ff24cf94de7c9eb47cc6f2c55e6921?period=month). Uvidím, třeba to zjednoduším tak, že se nakonec úplně obejdu bez API, i když jej Simple Analytics poskytuje.

Z emailů jsem také odebral formulář na „feedback“, který mi za celou historii vyplnili asi dva lidi v počátku a pak už nikdo. Ptal jsem se v něm, zda se firmě podařilo díky inzerátu na JG najmout nějaké lidi nebo k čemu jim to vlastně bylo. Zase o kousek historického balastu méně.

### Zrušení „Logo“ modelu a všeho kolem

Firmy, které si zaplatily za logo na příručce, jsem uchovával v Google Sheetu, v tabulce „logos“. Z ní se data stahovala do modelu „Logo“ a ten se používal pro rozesílání pravidelných emailů o tom, jak se logu daří a kolik lidí jej vidělo. Také se z tabulky vypisovala samotná loga na staré příručce.

Časem jsem vytvořil nový list, „companies“, kde jsem evidoval veškerá partnerství firem s klubem, počty zaplacených členů atd. Měl jsem tam i sloupec, zda mají logo na příručce a postupně jsem začal web portovat na to, aby bral data z této tabulky. Jenže posílání emailů a statistiky byly stále napojené na starý model a tak to žilo nějaký čas vedle sebe.

Tento týden jsem všem napsal a zeptal se jich, zda ty emaily čtou. Prý ne. Kdo se zmínil, že by se to snad mohlo hodit do budoucna, toho jsem uklidnil, že to kdyžtak vytáhnu ze statistik a že teď budou kompletně veřejné statistiky, kde si každý zjistí co chce. Tím bylo hotovo, tabulku jsem zrušil a s ní i všechno, co s tímto souviselo v kódu.


## Dolaďování příručky

- Zlepšil jsem (snad!) navigaci na stránkách příručky. Přidal jsem modrý jezdící proužek s odkazem na obsah. Obsah v dolní části stránky byl stručnější, než obsah na desktopu, tak jsem to teď udělal tak, aby byly zcela ekvivalentní. Jednou třeba přidám zobrazování aktuální kapitoly nebo vysouvání menu zleva pomocí JavaScriptu, ale teď to takhle stačí. A třeba to ani nikdy nebude potřeba?
- Na radu Dana Srba jsem přidal `[id]{ scroll-margin-top: 1rem }` do CSS, aby odkazy na kotvy navigovaly na místo, které má trochu „rezervu“. S přidáním modrého `position: sticky` proužku na mobilu to navíc začala být nutnost.
- Udělal jsem pár úprav v textech na webu. Například přidal slovo „zaokrouhleno“ u přehledu příjmů v patičce, aby mi lidi nepsali, že to v součtu nedává přesně 100 %. Vyhodil jsem zmínku o „solo entrepreneur“, protože v Česku stejně nikdo neví co to je. V textu je můj přístup vysvětlen dostatečně opisem.
- Díky nové příručce a neexistenci staré stránky s ceníkem vznikla příležitost odebrat „podmenu“, takové to tečkované, které bylo na příručce a některých dalších stránkách. Neměl jsem jej moc rád a rozhodl jsem se jej odebrat, protože se díky všem těm čistkám používalo už jen na jednom místě, a to nedůležitém. Podmenu zaniklo a není! Radost ze smazaného kódu.
- Další radost přišla s promazáváním JavaScriptu. Stále čekám, kdy budu potřebovat nějaký ten pokročilý framework, ale teď se mi stal spíše opak. Většina mého dosavadního JS kódu řešila různé nedokonalosti a složitosti v designu příručky nebo podmenu. Prošel jsem tedy soubory a dost z nich jsem mohl bez náhrady smazat. Některé budu moci smazat až později, ale pokud se mi to povede, nejspíš mi zbudou tak dva JS soubory o 20 řádcích ¯\\\_(ツ)\_/¯ Zas nebude React, no jo.


## Psaní pro Heroine

Jak jsem se zmiňoval v předchozích poznámkách, dostal jsem se do týmu externích autorů jednoho časopisu. Rozhodl jsem se to v těchto poznámkách už provalit, jde o časopis [Heroine](https://www.heroine.cz/). Domluvili jsme si pět článků, tento týden byl termín na první z nich.

Kromě toho jsem v souvislosti s Heroine opět komunikoval s dalšími lidmi. Například jsem díky Heroine poznal [Pavlu Lokajovou](https://www.linkedin.com/in/pavlaloka/) a ta mě poprosila o tipy na ženy, které by se mohly objevit jako ambasadorky v její připravované publikaci o ženách v ecommerce. Ženy jsem oslovoval a propojoval je s Pavlou, pokud o ambasadorství projevily zájem.

Také mě kontaktovala ještě jedna členka týmu Heroine s prosbou o rady v oblasti obsahového rozhraní připravovaného projektu, s tím jsem také strávil nějaký čas.

No ale k tomu hlavnímu. Psaní článku jsem samozřejmě prokrastinoval a [začal až den před termínem](https://twitter.com/honzajavorek/status/1451840188901208065). Po velkém úsilí v [kavárně](https://atriumzizkov.cz/kavarna) mimo miminkem obývaný byt a následně ještě večer do jedné ranní se mi povedlo článek vytvořit, ale zjistil jsem, že je dvakrát delší, než měl být. Což je můj klasický problém, jak asi pravidelní čtenáři mých poznámek moc dobře vědí.

Takže teď mě ještě čeká to nějak celé seškrtat a vlastně skoro napsat celé znova. Po sobotě jsem byl ale z psaní vyčerpaný a rozhodl jsem se, že bude lepší to dělat s odstupem v pondělí, že budu i na ten text nahlížet už jinak. Tak mi držte palce, ať to dopíšu aspoň den po termínu a ať vše dobře dopadne.

Možná je neprofesionální dodávat dvakrát delší články a teprve po termínu je seškrtávat, ale co si budem, nejsem autor profesionál a tuhletu praxi, stručnost a disciplínu se musím teprve nějak za běhu naučit. Protože blog, JG, ani články zpětně přebrané redakcemi Zdrojáku či EkoListu mě tohle fakt nenaučily.


## Sluchátka

Na základě [doporučení](https://www.facebook.com/honzajavorek/posts/10159276712692707) a desítek odsledovaných YouTube recenzí jsem se rozhodl konečně rozseknout výběr sluchátek, která by měla zvýšit mou domácí produktivitu a těšit mě na procházkách s kočárem po parcích.

Jednak Apple vydal nová, což teoreticky mohlo zlevnit nějaké starší modely, jednak mě kamarád přesvědčoval, že AirPods pecky mu drží v uších lépe než špunty AirPods Pro, což jsem považoval za zcela nemožné. Řekl jsem si tedy, že třeba Apple fakt vytvořil něco nadpřirozeného a prostě to zkusím. Když mi to bude stačit, ušetřím. Když ne, budu zase o něco chytřejší.

Koupil jsem tedy AirPods 2019, bezdrátové pecky. Když jsem si je donesl domů, hned jsem je opatrně vybalil, nasadil si je a pustil hudbu. Držely, zvuk krásný, tak si říkám OK, pojďme se podívat, co se s tím dá dělat. Jak jsem přišel zvenku, měl jsem ještě na sobě svetr a začalo mi být horko, tak jsem jej začal podvědomě sundávat a v ten moment, asi 8 sekund po prvním nasazení sluchátek, mi levé odstřelilo někam daleko pod gauč, mezi nejvíc chucvalců. Naštěstí mám doma 2m dlouhou zářivku, která čeká (a bude nejspíš spolu se sklenicí rtuti z teploměru navždy čekat) na odnos do sběrného dvoru, takže jsem sluchátko dokázal vylovit. Tolik k prvním dojmům.

Nebudu vás napínat, používám je už pár dní a dnes jsem si na Alze zaklikl, že je vracím. Párování s macOS i iOS je fajn. Přecházení mezi zařízeními ze začátku fungovalo dobře, ale potom už méně. Třeba dnes iPhone mi začal sluchátka krást, když jsem poslouchal na noťasu. Dělo se to každou chvíli, tak jsem na telefonu musel úplně vypnout BT a i potom sluchátka čas od času podivně vypadla a odpojila se.

Vůbec mi to ale nesedí v uších. Levé se vysunuje skoro při každém větším pohybu, ale jinak se vysunují obě. Při rychlejší chůzi je musím zandávat zpět co 20 kroků, při rozhlížení se přes cestu mám strach, že skončí v kanálu. Když se směju nebo jím, leze to ven. Také jsem si nezvykl na „double tap“ na sluchátko. I když jsem se fakt snažil udělat to způsobem, jakým to zafungovalo minule, chytlo se to zhruba jednou z pěti pokusů. To mi fakt nepřijde jako dobrý design.

Nuže, teď už víc tuším co chci, co mi vyhovuje, jak vypadá v praxi integrace Apple sluchátek s Apple zařízeními, atd. Jde se na druhý pokus. Tyto vrátím a pořizuji Jabra 75t, které mi v recenzích přišly stejné nebo lepší (záleží co je pro vás důležité) jako AirPods Pro a ještě jsou levnější. Místo přitroublých gest mají tlačítka, takový starý dobrý koncept, který by mi mohl vyhovovat více, také se mi víc líbí jejich design a mají údajně větší výdrž. Funkci, která jsem se bál, že mi bude chybět nejvíc, tedy inteligentní přecházení mezi zařízeními, doufám nahradí tzv. BT _multipoint_, což má Jabra jako jedna z mála na trhu, tedy připojení k dvěma zařízením zároveň. Třeba to bude fungovat i lépe než Applí kradení sluchátek telefonem ¯\\\_(ツ)\_/¯ Pokud nebude fungovat ani to, tak už nevím. Rozhodně nechci klasický BT _hell_, kdy musím stále něco ručně připojovat a odpojovat a nikdy nevím, co je připojeno kde.


## Další poznámky

- Proběhla [AMA s Honzou Králem na téma škálování](https://junior.guru/events/#2021-10-19T18-00-00). Sám jsem se přiučil zajímavé věci. Nahrávku jsem dal hned pro členy klubu na YT.
- Prošel jsem emaily související s Pyvcem, udělal jsem malý úklid v [grantech](https://github.com/pyvec/money), zamergoval jsem nějaké dependabot pull requesty.
- Hrál jsem si chvíli s [tímhle](https://csswizardry.com/ct/), ale pro svou hlavičku jsem z toho nic nevyvodil. Přednášku jsem si poslal do Pocketu.
- Kolegyně z Czechitas, která pracuje s API na pracovní nabídky, mě poprosila o úpravu, která by zajistila stabilní počet sloupců apod. Nakonec jsme došli k tomu, že když to tlačí do Kebooly, tak se možná hodí to posílat spíš jako CSV a ne JSON. [Předělal jsem to](https://github.com/honzajavorek/junior.guru/commit/51c900f178b9124a6b81d2e3da0413fefd7626a9), díky [csv](https://docs.python.org/3/library/csv.html) přímo v Pythonu bylo to nakonec rychleji, než jsem čekal.
- Protože spolupracujeme na datech z nabídek práce, přidal jsem na [stránku klubu](https://junior.guru/club/) logo Czechitas.
- Povedlo se mi omylem napsat zase [tweet, který dostal stovky lajků](https://twitter.com/honzajavorek/status/1451116512824147968) a v době psaní těchto poznámek je stále ještě dostává. Opět nijak nesouvisí s mým podnikáním. Protože jde o tweet v angličtině, zkusil jsem pod něj místo klubu šoupnout aspoň svůj GitHub Sponsors profil, samozřejmě bez jakéhokoliv efektu :)
- Během 7 dní od 18.10. do 24.10. jsem při procházkách nachodil 19 km. Celkem jsem se hýbal 7 hodin a zdolal při tom 19 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Dokončit první článek pro Heroine.
2. V souvislosti s článkem aktualizovat a doplňovat [stránku o motivaci](https://junior.guru/motivation/).
3. Učinit první pokus o cestování vlakem s miminem.

Bonus: Vybrat si bezdrátová sluchátka, která si následně budu chtít i nechat.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [The Free-Libre / Open Source Software (FLOSS) License Slide](https://dwheeler.com/essays/floss-license-slide.html)<br>Užitečný graf!
- [Where does all the effort go? Looking at Python core developer activity](https://lukasz.langa.pl/f15a8851-af26-4e94-a4b1-c146c57c9d20/)<br>Lukasz Langa nově pracuje pro Python Software Foundation jako dedikovaný vývojář. Jako jednu z prvních věcí udělal zajímavou analýzu toho, co se vlastně děje na repozitáři s kódem Pythonu.
- [Ahoj,](https://mailchi.mp/7647753a07e3/ploha-o-stezce-skrze-zoufalstv)
- [Tomáš Vachuda: Chytrá práce je ta, která je udržitelná](https://m.youtube.com/watch?v=VJpJOiVLXro&fbclid=IwAR2syAoUvFyBYqnfll2fJPtXk1ceHCKapi-1KG_Xk6MIahBedCLNSO7485s)
- [136 facts every web dev should know before they burn out and turn to landscape painting or nude modelling](https://www.baldurbjarnason.com/2021/100-things-every-web-developer-should-know/)<br>Bylo zábavné to číst a spousta bodů zarezonovala.

<small>Upozorňuji, že to není vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
