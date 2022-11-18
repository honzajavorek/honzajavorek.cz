Title: Týdenní poznámky #77: Sníh
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl zase nějaký ten týden (7.12. — 13.12.) a tak [stejně jako minule]({filename}2021-12-06_tydenni-poznamky-76-vanoce-na-discordu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tak zase píšu původně „páteční“ poznámky až v úterý. Fúúúú.


## Dárkový poukaz

Minulý týden jsem se soustředil hlavně na spuštění stránky s dárkovým poukazem. Jak jsem psal, nápad přišel od kamaráda [Petra](https://twitter.com/petr_vacha/), detaily realizace jsme vymysleli s investorkou a vyrobil jsem to v první půlce týdne. Jeden den mi trvalo přidat stránku, hlavně kvůli psaní textů, druhý den jsem kreslil a editoval kresby. Taky jsem strávil nečekaně hodně času s padajícím sněhem.

Nikdy bych netušil, že budu mít na jakémkoliv webu JavaScriptem animovaný padající sníh, ale stalo se. Celkem dlouho mi trvalo najít balíček na npm, který se mi bude ve všech ohledech líbit. Zkoušel jsem různé knihovny, ale každá měla nějaký problém, nebo to byl absolutní kanón založený na komponentách, kdežto můj současný „stack“ by se dal popsat jako „pět řádků vanilla JavaScriptu“.

Nakonec jsem skončil u balíčku [magic-snowflakes](https://www.npmjs.com/package/magic-snowflakes), kde mi vadil jen tvar vloček, ale našel jsem v changelogu [schovaný příklad](https://hcodes.github.io/snowflakes/examples/balls.html) toho, jak to jde změnit. Pak jsem zjistil, že to nefunguje úplně podle představ na mobilu, tak jsem [zareportoval bug](https://github.com/hcodes/snowflakes/issues/51) a ještě jsem využil mentoring v klubu, kdyby náhodou někdo netušil, zda něco nedělám blbě. Do debugování se pustila [Kate](https://twitter.com/KateMihalikova) a hodně mi pomohla, vymyslela hotfix. Nějaký den potom dokonce autor knihovny věc hned opravil a vydal novou verzi, takže paráda. Ne, že by to bylo jakkoliv podstatné teda, je to jen sníh, navíc bílý na žlutém pozadí, takže si ho stejně nikdo nevšimne :D

Taky mi dost času zabralo ono zpracovávání ilustrací. Nakreslil jsem je a vyfotil moc velké, takže měly příliš tlusté linky v porovnání s jinými ilustracemi na webu. Kdyby byly tenké a chtěl jsem je zesílit, šlo by to přes _stroke_ v grafickém programu (ať už Gimp, Photopea, nebo Inkscape), ale naopak už je to horší. S tímto jsem se trápil, protože to není problém konkrétně se stránkou na dárkový poukaz, ale obecně, bojuju s tím pokaždé. Nakonec jsem snad označil bílou plochu v Gimpu v původním JPG, dal _grow selection_ o nějaký ten pixel a vybarvil bíle, čímž jsem ubral tloušťku a toto jsem přeuložil, takže při konverzi do SVG přes [cartoonist](https://github.com/honzajavorek/cartoonist/) už byl výsledek blíž tomu, co chci.

Nicméně celé mě to přivedlo na sledování [tohoto](https://www.youtube.com/watch?v=miybeIlE-e8) a [tohoto](https://www.youtube.com/watch?v=uSnXEqaLrAA) videa, zda by to celé nešlo řešit nějak jinak. Paní v prvním z těch videí má vtipný přízvuk, tipuju že novozélandský, dost mi to připomínalo seriál Flight of the Conchords a na ten já vzpomínám moc rád :) Měl bych si ho pustit znova.

Kreslení [samotného dárkového poukazu](https://junior.guru/static/downloads/darkovy-poukaz-jg.pdf) nebylo tak složité. S investorkou jsme nakonec vymysleli, že bude lepší, když přidám i druhou stranu s informacemi, co má obdarovaný očekávat. O to složitější bylo zařídit, aby se PDF správně deploynulo na web, protože jak přecházím z Flasku na MkDocs a i kvůli spoustě dalších výmluv jsou moje statické soubory celkem _hell_, ve kterém se nedá orientovat. Povedlo se mi to správně nastavit asi až na popáté. Doteď jsem na webu měl jen obrázky, styly a JS, byl to první soubor jiného typu určený ke stažení.

Technicky kupón [zajišťuje Memberful](https://memberful.com/help/integrate/services/wordpress/add-gift-link/). Bylo akorát potřeba vytvořit _plan_, který nemá _free trial_, jelikož takové pak nejdou dávat jako dárky. K měsíčnímu a ročnímu předplatnému jsem tedy přidal i roční dárkové. Jinak vše zatím fungovalo OK.

Nově vzniklá stránka je na [junior.guru/gift](https://junior.guru/gift/). Zatím na ni neexistuje odkaz odjinud, ten jsem si říkal, že dodělám později. I tak na ni k dnešnímu dni [přišlo zhruba 150 lidí](https://simpleanalytics.com/junior.guru?period=month&search=paths%3Agift) a začal ji už indexovat Google. Nasdílel jsem to totiž na sociální sítě.

K dnešnímu dni se prodal jeden dárkový poukaz. Jedna osoba mi přes Instagramu nadšeně napsala, že JG je boží a že si poukaz nadělila sama sobě, takže pokud si dám jedna a jedna dohromady, vychází mi z toho poměrně vtipný průběžný výsledek této vánoční akce :D Ale jak píšu níže v těchto poznámkách, akce nejspíš přispěla k tomu, že do klubu přišlo víc lidí standardní cestou a taky ještě není všem dnům konec. Měl bych zřejmě někam viditelně přidat na tuhle stránku odkaz, přímo na web.


## Sociální sítě

Se sociálními sítěmi teď pracuji jinak než dřív. Jak jsem psal, spojil jsem „firemní“ a osobní kanály, je to teď víc napojeno na mou osobu. Co mi dřív ani nedošlo, na osobních profilech mám víc kamarádů, kteří na tyto věci nadšeně reagují. Myslel jsem, že je informacemi o JG budu obtěžovat, ale místo toho lajkují jak diví nebo občas i komentují, a tím vyhánějí _engagement_ na příspěvcích, takže je sociální sítě považují za oblíbenější, než tomu bylo dřív, a ukazují je více a více lidem (_reach_). To je dost příjemný efekt.

Zároveň jsem nepřestal na sociální sítě dávat věci z osobního života. Naopak, s tím jak jsem se vrátil na Instagram, dávám nově občas i nějakou fotku, třeba z procházek s kočárkem. Samotné posty, pokud se týkají JG, píšu formou delších příběhů rozdělených na odstavce. Nevím, jestli to někdo čte, zkouším to. Každopádně je to forma, která funguje dobře pro všechny sítě kromě Twitteru, kam to musím vždy přespsat do něčeho mnohem, mnohem kratšího, případně rozdělit na víc tweetů. To je trochu otrava.

Některé sítě penalizují odkazy, protože chtějí, aby lidé zůstali uvnitř a nechodili ven, např. na Instagramu do příspěvku žádný odkaz ani dát nejde, takže jsem začal u příspěvků už od začátku předpokládat, že tam odkaz žádný nebude. Na FB odkazy dávám, na Twitter taky. Na LinkedIn ne, odkaz dávám do kometntáře (to je takový _hack_, lidé znalí LinkedInu vědí), na Instagram taky ne.

Začal jsem také používat přímo sociální sítě místo plánování příspěvků na [Bufferu](https://buffer.com/). Zatím jsem si ho nepřestal platit, zatím zkouším, jak to bude fungovat, ale místo fronty teď mám prostě dvakrát týdně vyhrazený časový slot na sociální sítě a na všechny to dávám ručně. Umožňuje mi to využívat je naplno, všechny jejich funkce. Například Buffer nepodporuje tagování lidí na LinkedIn nebo ve FB skupinách, což je dost zásadní, ani mi nedovolí plánovat příspěvky na osobní profil. Neudělám přes něj ani Twitter vlákno, nenaplánuji retweet, atd. Stejně jsem tedy často musel z Bufferu odejít a příspěvky dodatečně upravovat. Buffer může být dobrý pro hobby věci, kde stačí věci naplácat do fronty a neřešit, ale když chci sítě využívat naplno a v zásadě je to můj hlavní, nebo skoro jediný marketingový kanál, dává mi nakonec smysl používat je napřímo.

Díky tomu mohu teď dělat i storíčka. Udělal jsem třeba storíčko, kde kuře vybalovalo z krabice salám junior. Ne každý to pochopil, ale kdo ano, smál se. Nikdy jsem žádná storíčka nedělal, připadám si na to už starý, ale pomalu tomu přicházím na chuť. Na Instagramu i Facebooku si je prohlíží až překvapivé množství lidí a hlavně na Instagramu je lze přesdílet, nebo na ně reagovat, což lidé s mými storíčky dělali. Například [yablko](https://www.instagram.com/yablko/) a další přesdíleli moje storíčko o vánočním dárkovém poukazu a díky tomu mě myslím objevilo dost nových lidí. Je to zajímavý nový kanál. Nemám zatím žádný systém v jeho používání, ale používat ho budu. Oproti storíčkům jiných lidí si tedy připadám dost amatérsky, ale naštěstí to mohu zakomponovat do upřímného obrazu, jaký kolem sebe buduji. Prostě přiznám, že jsem trouba a neumím to, hotovo.


## Heroine

Zatím jsem nestihl veřejně propagovat svůj další článek, který mi na Heroine vyšel. Mám už dva týdny po termínu na čtvrtý článek z pěti. Téma mělo být „jaké všelijaké pozice se v IT nacházejí“.

Toto téma už jsme probírali v úvodu projektu na callu a mě se líbilo, jak [Zuzana Pechová](https://www.heroine.cz/clanky/autor/70000224-zuzana-pechova) (další autorka) navrhovala, že by to mohlo být zpracováno jako příběh jak vzniká aplikace a na tom by byly pozice ilustrované, a ne jako suchý výčet. Přišlo mi to objektivně lepší a nabídl jsem jí tedy spolupráci na článku, abych jí ten nápad nekrad. Jenže včera jsme si k tomu volali a došli jsme k tomu, že oba upřímně chceme, aby to napsala ona, protože k tomu má super nápady a bude to mít nejlepší výsledek.

Tak jsem kontaktoval šéfredaktorku s tím, že bych toto daroval Zuzaně a navrhl jsem jiné téma pro sebe. Zatím čekám na odpověď. Taky jsem s Heroine spojil [Luboše Račanského](https://blog.zvestov.cz/), aby mohlo vzniknout něco, co by stavělo na [jeho zkušenostech s programováním s dětmi](https://blog.zvestov.cz/tag/krou%C5%BEek-programov%C3%A1n%C3%AD/), ale taky teď čekáme na odpověď.

Mezitím se čtení mých článků na Heroine trochu rozjelo a lidi začali dokonce i klikat, takže se Heroine vyšoupla v [mých analytics](https://simpleanalytics.com/junior.guru) konečně i před tento můj blog a dostala se tak do vedoucí pozice mezi normálními weby, tzn. když nepočítám Gůgly, Fejsbůky, apod. To mi činí radost.


## Další poznámky

- Věnoval jsem se mnoha mailům a taky lidem v klubu.
- Pořídil jsem [Stooy](http://www.stooy.cz/) a externí klávesnici atd. Konečně jsem si splatil dlouholetý dluh v podobě zdravějšího pracovního místa u sebe doma. Doteď jsem se různě hrbil v nevhodných pozicích, teď už to konečně připomíná něco, co by mohlo být aspoň trochu zdravé.
- Přišlo mi, že Green Fox Academy už příliš a možná až příliš nepokrytě spamují FB skupinu Učíme Python, tak jsem promazal jejich příspěvky a zapnul schvalování toho, co postují. Skupinu jsem kdysi založil, aby se tam mohli mentoři a učitelé Pythonu propojovat s lidmi, kteří mentory a učitele hledají. Popravdě, ta skupina nikdy nezačala tak úplně sloužit svému účelu a dodnes je to kočkopes, který lidi možná spíš zmate, než aby komukoliv nějak pomohl. Primární skupina české Python komunity jsou [Pyonieri](https://www.facebook.com/groups/pyonieri). Kdyby bylo na mě, tak Učíme Python zruším, ale vlastně je mi do dost jedno na to, abych to nějak řešil. Nepokrytý spam mi už ale vadil, tak jsem to zařízl.
- Discord Support nakonec umožnil Gabi z Engeta dostat se do klubu a aktivovat si zablokovaný účet. Nevím, čím to bylo a co se dělo, ale mám podezření, že se to povedlo i díky mým intervencím, kdy jsem zakládal ticket a připomínal se jako uživatel, který jim nově posílá vlastně celkem dost peněz za Nitro a boosty klubu. Dává mi to aspoň falešný pocit, že mám nějaké dovolání na platformě, na které jsem postavil celý svůj byznys.
- Členka se mi ozvala s nějakým problémem s kupónem, který dostala a který měl být na tři měsíce. Vyřešili jsme to operativně, ale chci ještě napsat na support Memberful a zeptat se, jak to přesně vlastně funguje.
- Spontánní frontendový srazík v klubu se v jeden den dost povedl, postupně tam přišlo asi 20 lidí a trval několik hodin.
- Pája Froňková natočila s prvním hostem první díl budoucího Junior Guru podcastu. Už jsem to slyšel, je to fajn! Teď jen doladit propagaci a vydat to, což mám na starosti já a vůbec nevím, jak se to dělá. Akorát tuším, že tam hraje roli RSS.
- Paralelně se vznikem našeho podcastu jsem přes LinkedIn [zjistil, že už podobný podcast nedávno vznikl](https://www.linkedin.com/posts/%C5%A1%C3%A1rka-kousalov%C3%A1_programhrovani-hr-it-activity-6874233345568473088-ldtM/). Tak jsem zvědav, zda si nebudeme moc šlapat na nohy, ale snad ne. Věřím, že si každý podcast najde něco, čím se odliší, nebo na co se bude soustředit víc.
- Instruoval jsem [Mílu](https://milavotradovec.cz/) přes soukromý chat, jak by šlo zpracovávat body z [issue](https://github.com/honzajavorek/junior.guru/issues/737), které nás má dostat blíž k ML robotovi.
- Vypadá to, že po měsících posunování papírů už konečně budu moci poslat fakturu jedné velké firmě. Ale dokud se to nestane, tak nebudu jásat. Řešíme to od srpna, takže prodloužení o další rok začnu příště řešit raději už v březnu 2022 :D
- Dlouho jsem zjišťoval, proč mi nechce usínat noťas, když ho nechám na Stooy s otevřeným displejem. Po velkém bádání mi došlo, že mám zapnuté [Lungo](https://sindresorhus.com/lungo), které aktivně spaní blokuje :D
- V klubu se odehrála přednáška se Soňou o testování a QA, bylo to moc fajn. Při nahrávání nebo moderování jsem tentokrát snad neudělal moc chyb, záznam byl jako obvykle pro členy dostupný ještě týž večer.
- Do klubu začalo v posledním týdnu chodit docela dost nových lidí. Upřímně si to neumím nějak jednoznačně vysvětlit. Může to být tím, že s určitou setrvačností chytily články v Heroine. Může to být tím, že lidi zahlédli tu vánoční akci s dárkovým poukazem a byť se dárků zatím moc neprodalo, tak se skrze to dověděli o JG a teď chodí do klubu normálně napřímo, bez dárku. Těžko říct, ale nestěžuju si. Akorát si teď trochu připadám možná až příliš jako „vítací typ“ :)
- Během 7 dní od 7.12. do 13.12. jsem při procházkách nachodil 29 km. Celkem jsem se hýbal 8 hodin a zdolal při tom 29 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Dodělat úkoly z vánočního „tudůčka”, kde mám ještě nějakou věc pro firmy a tak.
2. Dořešit články s Lubošem a Zuzanou. Napsat čtvrtý [článek pro Heroine](https://www.heroine.cz/zeny-it/).
3. Napsat nějakou dokumentaci pro Pyvec a zvládnout dobře schůzi Pyvce, kde se budeme připravovat na volby do výboru na jaře 2022.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Jak méně číst, ale mít z toho víc](https://www.lifehacky.cz/jak-mene-cist/)<br>Zajímavý systém. Intuitivně vlastně dost z toho dělám. Vysvětlovalo by to i vznik některých, nebo možná většiny mých propracovanějších článků na blogu.
- [Ceny bytů jsou šílené, hypotéka je sebevražda. Osudy Čechů bojujících s krizí bydlení](https://magazin.aktualne.cz/bydleni-za-vsechny-prachy/r~b9e2f570422c11ecbc3f0cc47ab5f122/)<br>Komplet jsem si prošel a pročetl, zajímavé. Příběhy lidí i rozhovory se sociology.
- [Bulvár #14: Tomáš Hoření Samec - Mainstreamový narativ vytváří dojem, že hypotéky jsou samozřejmé](https://soundcloud.com/advojka2013/bulvar-14-tomas-horeni-samec-mainstreamovy-narativ-vytvari-dojem-ze-hypoteky-jsou-samozrejme)<br>Pustil jsem si ještě rozhovor s jedním z těch sociologů z článku na Aktuálně, zajímavě to tady s Apolenou probrali.

<small>Upozorňuji, že to není vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
