Title: Týdenní poznámky: Nabídky práce podle regionu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (28.9. — 2.10.) a tak [stejně jako minule]({filename}/2020-09-29_tydenni-poznamky-novy-seznam-nabidek-prace.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


Tento týden jsem pracoval na tom, abych mohl mít samostatné stránky s inzeráty práce pro juniorní programátory pro každý region zvlášť.


## Normalizace místa

Nabídky práce z JG i odjinud mají většinou (pokud nejsou úplně na dálku) informaci o tom, odkud jsou. Už v této větě můžete odtušit hned několik problémů, které jsem musel vyřešit:

- Místo nabídky práce může být v libovolném formátu. Praha. Prague. Brno, Czechia. Káranice, Česká republika. Michálkovická 1137/197, 710 00 Ostrava - Slezská Ostrava, Czechia. Záleží na tom, co se autor nabídky rozhodl vepsat do políčka nebo odkud jsem nabídku převzal.
- Existují nabídky práce, které žádné místo nemají.

K tomu ještě:

- Některé nabídky jsou platné pro více míst. To se projeví tak, že se mi objeví v datech totožná nabídka s jiným místem, nebo že někdo napíše do políčka: Praha nebo Brno. Ostrava nebo na dálku.
- Některé nabídky mají místo, třeba kde je hlavní kancelář, ale jsou zároveň i na dálku.

Základní věc, kterou jsem tedy musel udělat, bylo normalizovat nějak tato data. Popíšu to jako proces tak, jak šly moje pokusy za sebou. Nechť je to dokumentace toho, jak se někdy motám v kruzích a nejsem několik dní schopen něco kloudného vytvořit, protože overengineeruju nebo se sice snažím problém zjednodušit, ale špatným směrem.

1. Už dříve jsem si dělal základní rešerši, jak by se to dalo řešit. Znám služby na geocoding, ale matně jsem si pamatoval, že jsou placené a tomu jsem se chtěl zatím vyhnout. Chtěl jsem najít nějakou "offline" variantu, do které můžu bušit libovolné množství požadavků. Také jsem se rozhodl, že budu nabídky dělit podle krajů, které ale pojmenuji podle jejich hlavních měst, plus sousední země. Region tedy v kontextu JG může být Praha (kraje Praha a SČ), Brno (JMK), nebo třeba Německo.
1. Rešerše mi vyhodila projekt [geograpy](https://pypi.org/project/geograpy/) a s tím jsem tedy i začal. Je postavený nad NLTK a potřebuje si tedy dodatečně stáhnout nějaká data (korpusy). Vše jsem v projektu připravil pro použití geograpy, ale měl jsem problém s instalací. [Založené issue na GitHubu](https://github.com/somnathrakshit/geograpy3/issues/20) jsme nakonec vyřešili do rekordních 10 minut. Jenže když jsem knihovnu vyzkoušel na pár vstupech, zjistil jsem, že vůbec neví, která bije. Na většinu mi nevrátila nic a jednou jsem dokonce dostal něco jako `Praha, Slovakia`. Takže jsem to odinstaloval a všechny věci, co už jsem k tomu připravil, jsem smazal. **Poučení:** Nejdřív vyzkoušej, jestli knihovna vůbec funguje, než jí budeš dělat místečko ve svém projektu.
1. Pořád jsem se držel pocitu, že chci tu normalizaci řešit "offline", už jen proto, že se nabídky práce většinou vyskytují jen v okolí několika větších měst. Toto ovšem nebylo zjednodušení problému, nýbrž jeho komplikace. Zkoušel jsem nějak ručně a jednoduše normalizovat adresy podle seznamu [nejlidnatějších měst u nás](https://cs.wikipedia.org/wiki/Seznam_m%C4%9Bst_v_%C4%8Cesku_podle_po%C4%8Dtu_obyvatel) apod., ale nikam to nevedlo. Navíc stejně, co s adresami, které se do tohoto netrefí?
1. Vytušil jsem, že se zase v něčem moc vrtám, když to jde řešit snadno a rychle, takže jsem sáhl po tom, co znám velmi dobře a už jsem to v minulosti několikrát použil: [geocoder](https://github.com/DenisCarriere/geocoder). Tento projekt umožňuje přeložit adresy na zeměpisné souřadnice pomocí různých veřejných API určených k tomuto účelu. [Nominatim](https://geocoder.readthedocs.io/providers/OpenStreetMap.html) od OpenStreetMaps je zdarma, takže to byla jasná volba. Upravil jsem kód a bylo to.
1. Zjistil jsem ale, že geocoder mi dává malou flexibilitu v tom, jaké parametry mohu OpenStreetMaps poslat. Chtěl jsem totiž ovlivnit, v jakém jazyce přijdou výsledky apod. Narazil jsem na knihovnu [geopy](https://pypi.org/project/geopy/), která vypadala jako ještě známější a používanější projekt. Takže jsem geocoder vyměnil za geopy.
1. Záhy jsem si odzkoušel, že jazyk asi nakonec nastavovat nebudu, protože sice chci Německo místo Deutschland, ale nějak se mi příčilo mít Vratislav místo Wrocław, Lipsko místo Leipzig, a nedej bože, aby se mi tam objevila nabídka práce z Gratzu. Takže jazyk jsem nechal být a udělal si překladovou tabulku na těch pár hodnot, které mě zajímají. Stejně jsem tabulku potřeboval už na to, abych přejmenoval kraje z Vysočina na Jihlava.
1. Nakonec jsem ale zjistil, že ani Nominatim nezvládá dobře některé zcela standardní adresy, např. na něco jako "Brno, South Moravia" to myslím bylo schopné vrátit cosi v Novém Jičíně. Už jsem to měl na produkci a byl to celkem problém (viz další kapitola těchto poznámek), ale naštěstí se zatím jen ukládala data a nikam se to nezobrazovalo, takže to nebylo nic, co by na noc nezachránil jeden `try/except/pass`.
1. Chyby ve stávajícím kódu mě donutily, abych do JG přidal lepší podporu pro evidenci toho, zda jde v nabídce o práci na dálku nebo ne. U externích zdrojů nabídek to nebyl moc velký problém přidat (byť jeden zápas s XPath mě asi bude ještě chvíli budit ze sna). U JG to ale vyžadovalo změnit formulář na zadávání nabídek a tuto položku tam přidat, plus upravit stávající data. Snažil jsem se navíc nějak chytře pojmenovat políčka tak, aby mi lidé možnost o práci na dálku nepsali do místa. Skončil jsem u toho, že políčko pro práci na dálku je ano/ne, je povinné a je před políčkem pro místo. Políčko pro místo je nepovinné a nese název "Office location".
1. Upravil jsem celý backend tak, aby počítal se změnami v datech. Jednak bylo potřeba začít všude evidovat práci na dálku, jednak se místo stalo nepovinnou položkou, což mě donutilo přeházet vidlema spoustu kódu a napsat spoustu testů. Informaci o tom, zda je pozice na dálku, jsem na webu zobrazil aspoň v podobě štítku. Taky se to zobrazuje i u místa. Pokud žádné není, je tam jen "na dálku", nebo se vypíše třeba "Brno, na dálku", pokud se zdá, že nabídka umožňuje oboje.
1. Jal jsem se řešit nespolehlivost OpenStreetMaps pro geocoding českých míst. Nová rešerše. Google [stojí 5 USD za 1000 dotazů](https://developers.google.com/maps/documentation/geocoding/usage-and-billing), což samozřejmě není moc, ale já prostě nějak nemám dobrý pocit z toho, když Googlu do cloudu někam dávám kreditku a zapínám placenou službu. Asi je to jen psychologické, ale já se prostě bojím, že mi někde uteče nějaký token a s ním i spousta peněz. S Googlím supportem se nechci nikdy v životě dohadovat. Google navíc nebere [Revolut](https://revolut.com/referral/janh8pm), takže se to nedá nijak pošéfovat z mojí strany, abych měl klidnější spaní. Musel bych mít asi nějaký prázdný bankovní účet jen na tohle a k němu kartu, kam bych posílal tak akorát peněz. Prostě ne. Pokud můžu, placeným službám z takovýchto generických flexibilních cloudů (ať už je to Google, AWS, Microsoft…) se chci asi zatím vyhnout.
1. Problém taky je, že spousta geocoding služeb na adresu odpoví zeměpisnými souřadnicemi, ale ty já vlastně vůbec nepotřebuji. Mě zajímá jen rozpad na jednotlivé administrativní celky, jako je město, kraj, země. To je u geocodingu vlastně doplňková věc, která je přímo ve výsledcích jen u některých služeb. Obejít se to dá reverse geocodingem (tzn. vložím souřadnice a dostanu, co všechno na nich je), ale to zase znamená dva dotazy na API pro každé místo.
1. Pokukoval jsem dále po Mapboxu, který má dokonce [geocoding do 100000 požadavků zdarma](https://www.mapbox.com/pricing/). Na [hřišti](https://docs.mapbox.com/search-playground/) to vypadalo dobře i pro ČR, ale problém zase je, že jejich podmínky použití vylučují ukládání výsledků. Musí to být interaktivní služba, v podstatě "napovídátko" pro uživatele k Mapboxí mapě, ně nějaký backendový robot. Geocoding pro taková použití mají, ale je to prémiová služba ("contact sales").
1. Následně se vynořila nějaká [vzpomínka na mladá léta, kdy jsem dělal bakalářku a hrál jsem si s mapovými portály v ČR](https://www.zdrojak.cz/clanky/api-k-ceskym-turistickym-mapam/). Nemá náhodou geocoding i Seznam? V jejich [dokumentaci žádné API člověk nenajde](https://api.mapy.cz/), ale [internet, Open Source a základní znalost PHP pomůže](https://github.com/Kdyby/GeocoderSeznamMaps/blob/master/src/SeznamMapsProvider.php):

    - [Brno, South Moravia, Czech Republic](https://api.mapy.cz/geocode?query=Brno,%20South%20Moravia,%20Czech%20Republic)
    - [49.200221,16.607841](https://api.mapy.cz/rgeocode?lat=49.200221&lon=16.607841)
    - [Bratislava](https://api.mapy.cz/geocode?query=Bratislava)
    - [48.13710786189762,11.575382173497758](https://api.mapy.cz/rgeocode?lat=48.13710786189762&lon=11.575382173497758)

1. Podmínky použití zmiňují, že nesmím ručně či strojově dolovat data a ukládat je či stahovat, nicméně se řídím spíš záměrem odstavce, kde tuším ochranu proti krádeži databáze, než že bych to bral doslovně. Pokud by náhodou někomu vadilo co dělám, věřím, že se Seznamem se normálně domluvím. Ono já na JG vlastně nic ani kešovat tak úplně nemůžu, protože žádné persistentní úložiště kromě Google Sheets nemám. Moje SQLite se při každém CI běhu vytváří nanovo z lokálních YAML souborů a stažených dat.
1. Super je, že tenhle geocoding funguje přesně tak, jak potřebuji. V Česku má kvalitní data a pro zbytek světa bere data z OpenStreetMaps. Blbé je, že musím dělat ty dva dotazy, protože v první odpovědi nedostanu info o regionu a zemi. To se ale asi dá přežít. Nakonec já toto dělám jen pro nabídky, které se budou zobrazovat na webu, a těch jsou, ač vzniknou třízením stovek nabídek, zatím pouze desítky.
1. Byť API není JSON, v Pythonu to bylo na pár řádků. A vyhodil jsem geopy. Kdo máte čas a chuť, můžete pro geopy napsat adaptér pro tohle Mapy.cz API, to by bylo určitě fajn.
1. V této fázi jsem se už už chystal nějak normalizovat zemi, a to skrze knihovnu [pycountry](https://pypi.org/project/pycountry/), která vypadá fakt dobře. Hlavně ta funkce `search_fuzzy()`! Jenže ještě než jsem ji vůbec nainstaloval, tak jsem si uvědomil, že vlastně zemi vůbec na nic nepotřebuji, kromě určení regionu. Myslel jsem, že budu zobrazovat třeba "Berlin, DE" a u českých věcí jen "Brno" místo "Brno, CZ". Jenže to potom může vzniknout "Adamov, CZ". A každý neví, kde to je, nebo mohou být různé Adamovy v různých krajích. Ve skutečnosti dává mnohem větší smysl zobrazit "[město], [region]", pokud jsou to různé hodnoty, a jinak prostě "[město]". To řeší úplně všechno, ať už je to Brno, Berlín nebo Adamov. A stačí mi k tomu jen hodnota pro region, žádnou další informaci o zemi zvlášť už nepotřebuji.
1. Ošetřil jsem, aby se vytvořily dvě a více nabídek práce, pokud mi někdo na JG zadá inzerát, kde je jako místo např. "Praha nebo Ostrava". Pokud někdo vymyslí něco ještě úplně jiného, mohu to v Google Sheets vždycky ručně upravit na variantu s "nebo".
1. V tuto chvíli už vše funguje krásně, ale nevzdávám se myšlenky, že by mohlo mít smysl geocoding přece jen lokálně optimalizovat. Napsal jsem si tedy dekorátor pro geocoding funkci, který regulárem odchytá Prahu, Brno a Ostravu, což jsou nejčastější případy, a na tyto rovnou vrátí výsledek, API se vůbec neptá. Když už se ptá, obalí geocoding funkci přes [lru_cache()](https://docs.python.org/3/library/functools.html#functools.lru_cache), což je asi minimální pomoc, zvlášť když pouštím scrapery v několika procesech vedle sebe, ale zas jako proč ne. Pro mě je to jen pár znaků v kódu navíc a když to odchytá i blbých 5 adres, ušetří to 10 dotazů na API.
1. Zbývá vytáhnout data na světlo světa. V rámci continuous deploymentu jsem samozřejmě celou dobu pushoval do masteru a házel vše na produkci, takže už několik dní má výpis nabídek práce štítky o tom, zda je nabídka na dálku, a hned jak jsem byl schopen normalizovat místo, jsem to normalizovaně ihned začal i zobrazovat. Teď ale k tomu hlavnímu, tedy vygenerování samostatných stránek pro jednotlivé regiony. Je pátek a já chtěl končit týden s vítězným pocitem, takže jsem se s tím moc nemazal.
1. Vytvořil jsem si pevný seznam regionů, které chci zobrazovat, aby se web neřídil jen tím, co je v databázi, jinak by se stránky regionů náhodně zjevovaly a mizely podle toho, zda v nich zrovna jsou nějaké nabídky práce nebo ne. HTML kód stránek jsem vzal z hlavního výpisu a upravil zatím jen pár popisků. Ošetřil jsem jen případ, kdy v regionu zrovna žádné nabídky nejsou, ale na CSS už nebyl čas. Odkazy na regiony jsem dal zatím ošklivě jen tak pod seznam nabídek. Kdo si tam toho všimne, třeba ho to úplně neurazí a třeba mu to pomůže, než to udělám hezčí. Jo, je to naprasený, ale je to tam a nějak to funguje. Screenshot sem tentokrát ani nebudu dávat.
1. Stránky pro jednotlivé regiony fungují i jako SEO lákadlo, takže jsem se pokusil pohrát s tím, aby v `<title>` stránek bylo něco, co lidi zkouší na internetu hledat.
1. Vítězný pocit!


## Zmatky a zachraňování produkce

Už to tak nějak vyplývá i z popisu toho klikatého postupu výše, ale ne vždy se daří. Mám však ještě jeden příběh.

Ve středu byl poslední den v měsíci, což znamená, že jsem měl poslat [newsletter](http://eepurl.com/gyG8Bb). V podvečer jsem se dostal do fáze, kdy jsem měl jasně funkční geocoding přes OpenStreetMaps a říkám si, že to už jen pushnu a jdu psát ten newsletter. Jenže pak koukám, že to padá, že OSM si neporadí se spoustou adres na produkci. A že mám chyby v tom, jak se na JG inzerátech řeší a ukládá práce na dálku. Všechny JG inzeráty zcela zmizely z výpisu. Zběsile jsem to začal opravovat, ale s každým commitem jsem akorát zbrkle nadělal další chyby, nechal rozbité testy, apod.

Vždy trvalo, než projde CI, a než zjistím, kde jsem zase přehlédl nějakou chybu. Takže jsem se rozhodl, že v mezičase bych mohl začít připravovat ten newsletter. Sice do něj ani nemůžu ještě dát nabídky práce, když mi zmizely, ale tak nějaký ten text už můžu začít připravovat. Vytvořil jsem v MailChimpu novou kampaň a… rázem mi všechno na CI zase spadlo. Mám totiž na JG skript, který se dívá na MailChimp do kampaní a ukládá informace o tom, jestli byla která nabídka práce už odeslána v nějakém newsletteru a kdy (to se pak posílá v pravidelných informacích inzerentům). Tento skript nepočítal s tím, že existuje kampaň, která nemá datum odeslání :D Takže jsem si akorát přidal další problémy: Kampaň jsem nemohl odeslat, dokud nemám funkční nabídky práce, a ty nebudu mít funkční, dokud bude existovat neodeslaná kampaň. Oprava na jeden řádek, jasně, ale nálada úplně v kýblu.

Do toho mě donekonečna zlobil `pipenv`, protože střídavě z mě neznámého důvodu vytvářel lockfile s knihovnou `importlib-metadata` a bez ní, což mi už měsíce (?) střídavě a náhodně shazovalo CI a zasekávalo continuous deployment. V tuto chvíli už jsem vypěnil a zkusil vše přeinstalovat a updatovat, ale bez výsledku. Nakonec jsem zoufale zkusil upgrade projektu z Pythonu 3.7 na 3.8 a to záhadně (zatím!) zabralo. Uf, ok?!

Nakonec jsem to celé nějak polepil, zachránil, hotfixoval, newsletter dokončil, odeslal a po sedmé večer dokonce s prací i přestal, ale jako… Já nevím no. JG je celé stavěné tak, aby se dalo spravovat v jednom člověku. Když spadne CI, mělo by být jedno, že to opravím až další den. Mělo by být jednoduché udělat revert v Gitu, vrátit se na funkční verzi a nechat opravy na ráno moudřejší večera. Jenže zvyk, že rozbitá produkce je průšvih a musí se řešit hned, je prostě asi silnější. Takhle to ale nejde :) Jsem jeden člověk a nemůžu se nechat stresovat tím, že někde pár hodin přes noc něco na JG chybí. Všem to je úplně jedno a mělo by to nechávat klidného i mě, když vím, že to můžu ráno v klidu opravit. Toto se musím ještě naučit.


## Další poznámky

- Vylepšil jsem (snad) trochu CSS štítků a log firem u nabídek práce.
- Upravil jsem váhy jednotlivých parametrů, které určují pořadí nabídek. Teď už to vypadá, že výsledek plus mínus dává nějaký smysl.
- Odepsal jsem na pár mailů a dořešil pár záležitostí, které jsem dlouho odkládal.
- Díky [Mišo Belicovi](https://github.com/honzajavorek/junior.guru/issues/383) a [Vláďovi Skoumalovi](https://www.skoumal.com/) jsem se [dověděl o WAL módu v SQLite](https://twitter.com/honzajavorek/status/1311578638723297280) a o tom, [jak zapisovat efektivně](https://www.skoumal.com/en/parallel-read-and-write-in-sqlite/). Jak zmínil i [Ondřej Kokeš](https://github.com/kokes) i v komentářích na FB pod minulými poznámkami, ideálně to řešit přes single writera - udělat lokální frontu, všechno mu posílat a zapisovat bude jen on. To je pro JG momentálně overkill (dělá to tak 10 retries), ale je super, že mi lidi takto radí po přečtení poznámek a rozhodně jsem se díky tomu naučil něco nového.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Studio N: Krvavý konflikt o Karabach může eskalovat ve válku](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikn.cz%2F452462%2Fstudio-n-krvavy-konflikt-o-karabach-muze-eskalovat-ve-valku%2F%3Fref%3Dlist&h=ba47c181ad57d7b5a043168f3ddfba737db69211507857f65fc43a84717ebd21)<br>Vysvětlení situace
- [Bláha: Vládní politici celou dobu lžou. Data z nemocnic byla tajná i před zdravotníky](https://getpocket.com/redirect?&url=https%3A%2F%2Fvideo.aktualne.cz%2Fdvtv%2Fblaha-vladni-politici-celou-dobu-lzou-data-z-nemocnic-byla-t%2Fr%7E3f29d4f8042411ebb115ac1f6b220ee8%2F&h=e769466a84e0a897f4e06abf7068658e4687e56d243b89bac1e175036b1f5473)<br>Super rozhovor, díky za update ohledně toho, jak kvalitně se teď na zvládnutí COVID-19 pracuje
- [How One Guy Ruined #Hacktoberfest2020 #Drama](https://getpocket.com/redirect?&url=https%3A%2F%2Fjoel.net%2Fhow-one-guy-ruined-hacktoberfest2020-drama&h=4c175e25be6cee8b1e5a724ed4da186dee0b0f5d84ee939b7965567b9fd9ad04)<br>Proč lidi letos nadávají na Hacktoberfest
- [Karanténa, den čtvrtý: volá hygiena!](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.irozhlas.cz%2Fkomentare%2Fcovid-koronavirus-karantena-hygienicka-stanice-erouska_2010012215_jab&h=c6233a527f0add8d5877222e174701e0a4829ee1f475ae27ba570aab8cf5291f)<br>“Tím, kdo v posledních týdnech s covidem bojuje, jsou – ostatně stejně jako na jaře – Češi. Ne Česko.”

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
