Title: Týdenní poznámky: Schůzky a evidence firemních partnerství
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl zas nějaký ten týden (27. 1. až 3. 2.) a tak [stejně jako minule]({filename}/2023-01-27_tydenni-poznamky-jeseniky-a-fora-na-discordu.md) sepisuji, co jsem dělal a co jsem se naučil.
Tvořím [junior.guru](https://junior.guru/) a nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/) a členy by mohlo zajímat, co dělám.
Psaní poznámek mi taky pomáhá nezbláznit se a nepropadat pocitu, že je konec týdne a já jsem nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


<!-- Honzo, piš jednu větu na řádek! https://sive.rs/1s -->


## Evidence firem

Pokračoval jsem v převádění evidence firem z Excelové tabulky do YAMLu napojeného na zbytek JG:

-   Začal jsem načítat data z YAMLu místo z Excelu.
-   Informace o firemních kupónech nemohou být v YAMLu, protože jsou neveřejné.
    Stahují se tedy přímo z Memberful API.
    Při té příležitosti jsem trochu vylepšil třídu, přes kterou k jejich GraphQL API přistupuji.
-   Přidal jsem varování, když mám v kódu logo firmy, které už skončilo partnerství.
    Chtěl jsem pak loga promazat, ale zjistil jsem, že se používají i jinde (např. na upoutávkách k akcím v klubu).
    Taky jsem zjistil, že i když se nepoužívají, mám kód blbě a spadne to.
    Takže jsem radši zatím nic nemazal.
-   Propojil jsem vzájemně všechny informace pomocí tabulek a cizích klíčů v SQLite.
    Firmy a údaje o jejich partnerství jsou teď asi nejpropletenější tabulky na JG.
    Celkem jsem se u toho zapotil a musel jsem si dost osvěžit SQL.
    Mám to pokryté hromadou testů, protože jsem si vůbec nevěřil a polovina mého programování byla pokus-omyl.
-   Web jsem napojil na nová data.
    Na příručce se tedy vypisují loga už na základě toho, že systém ví, že dané firmy mají určitý tarif a jeho součástí je logo na příručce.
-   Kromě epizod podcastu jsem s daty o firmách propojil i akce v klubu.
    Nově mohu přednášku označit jako partnerskou, pokud si ji firma zaplatila.
    Stejně jako u epizod podcastu, nikde se to zatím neprojeví, je to pouze v datech.
-   Mám připravený kód, který dokáže vypsat všechny benefity určitého tarifu.
    Volitelně buď bez těch, které zdědil od nižších tarifů, nebo s nimi.
    To se bude hodit, až budu chtít na web vypsat ceník pro firmy (aktuálně je v Google dokumentu).
-   Firmy se ve výpisu na webu řadí nově zaprvé podle toho, jaký mají tarif, zadruhé abecedně podle názvu.
-   Při předělávání evidence firem jsem si uvědomil, že `company` a `companies` jsou špatné názvy.
    I v češtině jsem v tom měl zmatek, někde „spolupráce“, někde „sponzorování“.
    Říká se, že pojmenovávání věcí je jedna ze dvou nejtěžších věcí v programování.
    Já jsem velkým zastáncem toho, že pojmenování je hodně důležité a jsem trochu ovlivněný věcmi jako _ubiquitous language_ z _Domain-Driven Designu_ apod.
    Našel jsem vhodnější termín pro firmy a entity kolem nich, a to `partner`, `partnership`.
    V češtině „partner“, „partnerství“.
    Podle mě to nejlépe popisuje vztah, který s firmou máme.
    Do budoucna mi to umožňuje mít v systému i další firmy, které jsou se mnou v jiném vztahu.
    Například inzerenti pracovních nabídek, nebo vzdělávací agentury v katalogu.
    Udělal jsem velkou _search & replace_ akci, při které jsem termíny všude v kódu změnil a sjednotil.
-   Na [/open/](https://junior.guru/open/) jsem vytvořil novou sekci, [Firemní partnerství](https://junior.guru/open/#firemni-partnerstvi).
    V souvislosti s tím jsem nahoru na stránku přidal osnovu stránky, ať se v tom dá aspoň trochu vyznat.
-   V nové sekci jsem nejdřív pouze vypsal firmy do tabulky a poslal to na produkci.
-   Díky [dotazu](https://github.com/mkdocs/mkdocs/discussions/3118) jsem zjistil, jak mohu dynamicky generovat stránky pro svoje MkDocs.
    Je na to plugin [mkdocs-gen-files](https://oprypin.github.io/mkdocs-gen-files/).
    Tím je definitivně vyřešena poslední věc, kterou jsem si nebyl jistý, jak v MkDocs udělám, až ji budu potřebovat.
    Cesta k tomu, abych zrušil starou část JG postavenou na Flasku, je umetená!
-   Vzápětí jsem použil ještě plugin [awesome-pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin), který mi umožnil vygenerované stránky jednoduše zahrnout do navigace MkDocs.
    Sice mi trvalo snad hodinu, než jsem to rozchodil a pochopil, ale už mi to funguje.
-   Vytvořil jsem tedy dynamicky pro každou firmu stránku.
    Na tyto stránky teď odkazuji z tabulky firem v oné nové sekci [Firemní partnerství](https://junior.guru/open/#firemni-partnerstvi).
    Zatím na těch stránkách nic není, ale dalším krokem bude výpis všech benefitů, které má firma objednané, a dalších údajů o partnerství firmy s JG.
-   Těmto novým stránkám jsem nastavil `noindex` pro vyhledávače.
    Nemají být „tajné“, ale nepotřebuji, aby vyskakovaly někde ve výsledcích vyhledávání.
    A určitě nechci, aby na výraz „ENGETO Academy“ někdo našel tohle, místo aby našel jejich budoucí stránku v katalogu vzdělávacích agentur, který letos vyrobím.


## Blog

Upravil jsem bota, který hází do [mé Telegramové skupiny](https://t.me/honzajavorekcz) odkazy na články, které vydám tady na blogu.
Snad budou teď náhledové obrázky fungovat ještě o něco lépe.

Na blogu používám tagování článků, ačkoliv tagy samotné nikde nevypisuji.
Mám je však přístupné z kódu, který sestavuje blog.
Např. se díky přiřazenému tagu dá vypsat „největší pecky“ na [hlavní stránce blogu](https://honzajavorek.cz/blog).
Upravil jsem články tak, aby poznámky měly tag „týdenní poznámky“ a všechny články související s JG aby měly tag „junior.guru“.

Povolil jsem pak v [Pelicanu](https://getpelican.com/) generování RSS pro jednotlivé tagy s tím, že se mi to může v budoucnu hodit při nějaké automatizaci, např. pokud bych chtěl věci související s JG zobrazovat na samotném JG.


## Schůzky

-   Sešel jsem se s kamarádkou a radil jsem jí, jak začít jako tvůrce (např. videí).
    Ona mi na oplátku řekla drby o jedné firmě, která fušuje do vzdělávání.
-   Sešel jsem se s [Mariánem Kameništákem](https://www.linkedin.com/in/mariankamenistak/), který mě už dříve kontaktoval.
    Hledali jsme průsečíky toho, co děláme.
    Konkrétní závěry nemáme, ale byl to příjemný pokec.
    Možná uděláme přednášku v klubu.
-   [Jakub „Rozbité prasátko“ Dvořák](https://rozbiteprasatko.cz/) vydal knihu.
    Píšou o něm [na CC](https://cc.cz/staci-jeden-akciovy-index-a-do-konce-zivota-nemusite-nic-delat-rika-autor-rozbiteho-prasatka/), [byl u Vojty Žižky](https://www.youtube.com/watch?v=rCcGZDi-hCs).
    Kniha se hned vyprodala.
    Jakub mě pozval na křest knihy.
    Nikdy jsem na žádné takové akci nebyl.
    Měl jsem to kousek a moc jsem si to užil.
    Byl tam i ten Vojta Žižka, ale bavil jsem se spíš se spoustou jiných zajímavých lidí, na které jsem tam narazil.
    S redaktorem Jakubova nakladatelství jsem např. diskutoval, jak by šlo vydat příručku na JG jako knihu.
    Překvapilo mě, že JG znal.
    Přesvědčoval mě, že by to vydat šlo a že kdybych to chtěl udělat, ať se mu určitě ozvu.
-   Na online schůzce jsem s ENGETO Academy posunul přípravy společné ankety mezi juniory.


## Zdražení členům v klubu

Přišel únor a s ním zdražení pro stávající členy klubu.
Zkontroloval jsem všechny kupóny a opravil jejich nastavení.
Pak jsem se zhluboka nadechl a použil jsem v Memberful funkci [move](https://memberful.com/help/manage-your-members/move-all-members-of-a-plan/).
Nejdřív na roční, pak na měsíční předplatné.

Vypadá to, že to funguje.
Na starých tarifech už by neměl nikdo být a brzy je úplně smažu ze systému.

Za pár měsíců uvidím, jak moc lidí nakonec odejde a o kolik víc budu vydělávat.


## Další

-   Propagoval jsem v klubu a na Pyvec Slacku možnost dobrovolničení v organizačním týmu PyCon CZ, který se začal sestavovat.
    PyCon CZ bude po covidové odmlce opět v Praze.
    Kdo byste měli zájem pomoct, [přidejte se na Slack podle tohoto návodu](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
    [EuroPython](https://blog.europython.eu/europython-january-2023-newsletter/) bude mimochodem taky v Praze,
    ale má jiný organizační tým a samozřejmě jiný termín.
-   Řešil jsem nějaké detaily partnerství s Green Fox Academy.
    Propojil jsem je s Pájou, aby mohli natočit podcast.
-   PayPal zavedl podporu pro [automatický transfer peněz](https://www.paypal.com/us/cshelp/article/can-i-have-my-balance-automatically-transferred-to-my-bank-account-help398).
    Chodí mi tam pár korun z Patreonu, tak jsem si to nastavil.
-   Nová verze Scrapy [změnila některé věci](https://docs.scrapy.org/en/latest/topics/feed-exports.html#feed-uri-params), tak jsem je opravoval.
-   Zjistil jsem zajímavou věc.
    Kdybych měl dobrá data o pracovních inzerátech pro juniory, minimálně jedna vzdělávací agentura by za ně byla ochotna platit.
    Tohle by mohlo vrátit nabídky práce na JG zase trochu na výsluní mého zájmu.
-   Dolaďovali jsme se Zuzanou Pechovou detaily k přednášce, která bude příští týden.
    Pak jsem to [propagoval na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7026925311933968385?utm_source=share&utm_medium=member_desktop).
-   Propagoval jsem na LinkedIn [novou možnost pohovorů nanečisto s Ataccamou](https://forms.gle/TNT46oPcS3oZEpeb9).
-   [Naučil jsem se](https://github.com/crdoconnor/strictyaml/issues/191) jak ve `strictyaml` načítat pouze datum místo data a času.
    Na celém JG jsem to změnil podle toho.
    Funguje to skvěle.
-   Koupil jsem si lístek na letošní [PyCon NA](https://na.pycon.org/), ačkoliv tam nepojedu.
    [Jsou úžasní]({filename}2021-06-17_jessica-upani-about-python-events-in-namibia-you-have-to-be-pure-in-terms-of-your-why.md) a chci je podpořit.
    Podpořte je taky, lístek stojí zhruba pětistovku.
    Ty lidi znám osobně a mohu se za ně stoprocentně zaručit.
    Každá koruna jim udělá radost.
-   Dostal jsem seriózní nabídku, že by se [cojeapi.cz](https://cojeapi.cz) mohlo sloučit s [naucme.it](https://naucme.it/), spolu s nabídkou odkupu domén.
    Vzal jsem si čas na rozmyšlenou.
    Taky nevím, za kolik bych měl domény cojeapi.cz, jakpsatapi.cz a whatisapi.org prodat.
    Nikdy jsem domény neprodával.
-   Všiml jsem si, že [grafy](https://junior.guru/open/) ukazují nula lidí na stipendijním předplatném.
    To je blbost, takže jsem hledal chybu.
    Chyba se netýkala jen stipendií.
    Kód, který jsem nedávno upravoval, nyní hodně špatně vyhodnocoval, kdo je na jakém kupónu.
    Měl jsem testy na různé hraniční případy, ale neměl jsem test na základní a zcela běžnou situaci.
    Přesně pro ni se to rozbilo 😀
-   Udělil jsem dvě stipendia.
-   Odpovídání v klubu, e-maily, [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), atd.
    Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
-   Během 8 dní od 27. 1. do 3. 2. jsem při procházkách nachodil 9 km. Celkem jsem se hýbal 3 hodiny a zdolal při tom 9 kilometrů.
-   Finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).
    Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/34fa3ec07892dd3ff64458e2ccbf12578e00860483427e9e7c4847bc/)


## Povedlo se

Udělal jsem něco z [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md)?

<!-- Koukni sem https://www.icloud.com/notes/092v6QG3aoSmpVOGHnpg0uIXQ -->

-   Rychle se blížím se k vyřešení „Firma musí vědět vše o svém předplatném, v jakém je stavu, kolik čeho zbývá.“
-   Pomalu se blížím se k vyřešení „Já i firma musíme mít včas informaci, že se blíží konec.“
-   Velmi pomalu se blížím k tomu, abych mohl mít na webu ceník pro firmy.
-   Podílím se na anketě mezi juniory.
-   Věnuji se Pyvci jako člen výboru.


<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví.**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>


## Plánuji

1.  Nastavím, aby Memberful posílalo lidem e-mail, pokud zruší členství.
    Mělo by v něm být něco o tom, aby zkusili stipendium, pokud je pro ně klub moc drahý.
2.  Budu mít pro každou firmu stránku, na které bude výpis údajů o jejich partnerství.
3.  Aktualizuji skript, který vítá firmy v klubu.
    Nově bude odkazovat na ty nové stránky a transparentně informovat o všech závazcích, které k firmě mám.


## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel toto:

- [NetNewsWire - Twitter Integration To Be Removed](https://nnw.ranchero.com/2023/02/02/twitter-integration-to.html)<br>Elon odebere API z Twitteru, moje RSS čtečka odebere podporu pro čtení Twitteru 😢 Na Twitter už dál chodit nechci, ale některé lidi jsem sledoval rád. Bohužel budu asi muset Twitter tím pádem přestat číst úplně.
- [Babiš ho chtěl na Hrad, co s Lojzou teď bude? Navštívili jsme útulek Dášenka, kterému v kampani přinesli granule i nevraživost](https://refresher.cz/130107-Babis-ho-chtel-na-Hrad-co-s-Lojzou-ted-bude-Navstivili-jsme-utulek-Dasenka-kteremu-v-kampani-prinesli-granule-i-nevrazivost)<br>Tohle je parádní článek. Neironicky. Začíná to jako banalita, ale je to úplně skvěle a do hloubky zpracované.
- [The Freedom of Ignorance](https://nemil.com/2019/12/23/the-freedom-of-ignorance/)<br>Vědět o problému příliš mnoho nám někdy zabrání se do něj vůbec pustit. Když jste dítě na prolézačce, prostě skočíte. Když jste dospělí, neskočíte. Víte, že je to 2m vysoko, co všechno se může zlomit, apod. Když moc analyzujete a víte toho až příliš mnoho, najdete příliš mnoho důvodů, proč něco nejde. Mezitím to udělá někdo jiný, komu nikdo neřekl, že to nejde 😀
- [Beware Engineering Media](https://nemil.com/2019/08/30/beware-engineering-media/)<br>Jak nepodlehnout marketingu ve vývojářských komunitách, na konferencích a na webech pro vývojáře. Že existuje sto článků a přednášek o MongoDB nutně neznamená, že tuto technologii všichni používají, ale že v marketingové strategii MongoDB je, aby existovalo sto článků a přednášek. V závěru jsou tři užitečné body, na které se soustředit při čtení věcí jako HackerNews.
- [Komentář: Babiš si přisvojuje monopol na pomáhání. Je to chyba nás všech](https://www.seznamzpravy.cz/clanek/domaci-politika-komentar-babis-si-prisvojuje-monopol-na-pomahani-je-to-chyba-nas-vsech-224119)<br>„Jak se vám asi tak bude žít v oblasti, kde prakticky nefunguje jediná nemocnice? Kde si pacienty překládají na benzinkách, protože vozů je málo a nemohou opustit hranice okresu? Jakou perspektivu máte, když už od střední školy vás vzdělání připravuje pouze a jenom na realitu špatně placené práce v ekonomice montoven? Jaké to asi je, když za prací nebo za vzděláním dojíždíte, ale kvalita dopravy upadá a jízdné se neustále zdražuje?“ … „Vyfouknout Babišovi roli toho, kdo se stará o lidi, můžeme jen tím, že budeme soustavně upozorňovat na to, s jakými strukturálními problémy se Česko potýká, a žádat jejich řešení tak, aby byl Babiš vždy o několik kroků pozadu.“
- [Ferdinand Leffler: Češi čím dál víc milují užitné zahrady. Pěstují zeleninu a chovají slepice — Město](https://www.buzzsprout.com/2007031)<br>Pustil jsem si k úklidu kuchyně povídání se zahradníkem, že to bude chill na neděli. Dostal jsem rozzlobeného muže rapujícího o nedostatcích veřejného prostoru, o politice, developerech, udržitelnosti. Skvělý to bylo!
- [Komentář: Promluvme si o vojně dřív, než o ní začnou mluvit nostalgici](https://www.seznamzpravy.cz/clanek/domaci-zivot-v-cesku-komentar-promluvme-si-o-vojne-driv-nez-o-ni-zacnou-mluvit-nostalgici-194070)<br>Tohle zní jako dobrý nápad.
- [Pod čarou: Neodsuzujme žvanění politiků. Jazyk nemůže za problémy společnosti.](https://seznam-zpravy.u.mailkit.eu/mc/VUQCVLPE/FYSGEKEEEMJWDPOHRD/CUCQCCVECCM)<br>Opět fajn newsletter, tentokrát o mluveném projevu. Třeba tohle pozoruju od začátku války: „Západní novináři i veřejnost většinou oceňují projevy ukrajinského prezidenta Zelenského, který má ostatně ke skvělé rétorice coby herec z povolání dobré předpoklady. Také hraje na emoce, u západních politiků se snaží vyvolat pocity viny, strach, nebo naopak pošimrat jejich ego, opakuje dokola stejné figury a bonmoty, pracuje se zanícenými morálními apely a expresivním projevem.“ Tohle už TikToková generace dávno ví, ale moje si to potřebuje přečíst: „Efektivní a srozumitelný text vyžaduje propracovanou logickou strukturu, precizní argumenty, bohatou slovní zásobu, věcnost a další vlastnosti, které pak mylně vyžadujeme po ústním projevu. Ten má ale jiné, často zcela protichůdné požadavky.“
