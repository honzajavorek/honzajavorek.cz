Title: Týdenní poznámky #25: Nové kapitoly o práci na volné noze
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (2.11. — 6.11.) a tak [stejně jako minule]({filename}/2020-10-30_tydenni-poznamky-24-nabidky-prace-na-dalku-a-scraping.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

## Nové kapitoly do příručky

Tento týden jsem se zabýval mnoha věcmi, ale tou nejdůležitější asi bylo napsání nových kapitol pro [Příručku o hledání první práce v IT](https://junior.guru/candidate-handbook/). To provázela i nějaká základní rešerše a jsem v kontaktu i s jednou osobou, která by mi možná poradila, jak se dá v IT přivydělat během péče o dítě. To ale možná bude i na celou další kapitolu. Ty dvě, co už mám připraveny, jsou o práci na volné noze a o práci "přes IČO", tedy kontraktorství a švarc systému. Psal jsem je celý čtvrtek a část pátku (přitom taková blbost, že). Jestliže máte k těmto tématům blízko a chtěli byste mi na to dát zpětnou vazbu, napište mi na [honza@junior.guru](mailto:honza@junior.guru).


## Další poznámky

- Dokončil jsem práci na scraperu nabídek práce z jednoho většího zdroje, který se scrapování brání (viz předešlé poznámky). Hlavní věc, kterou bylo potřeba vyřešit, byla nespolehlivost a nedostupnost proxy z [proxy-list](https://github.com/clarketm/proxy-list). Můj scraper ztratil spoustu času na timeoutech. Takže jsem hledal lepší zdroj těch proxy. [free-proxy.cz](http://free-proxy.cz) vypadalo dobře, protože tam je i sloupec s dostupností a rychlostí proxy, ale záhy jsem zjistil, že ten web nemá žádné API a není snadno scrapovatelný (má relativně sofistikované ochrany, např. při detekci scrapingu odesílá reálně vypadající, ale nesmyslný obsah). Nakonec jsem skončil u stahování seznamu z [free-proxy-list.net](https://free-proxy-list.net/). Následně jednotlivé proxy hned zkouším a HEAD requestem na [honzajavorek.cz](https://honzajavorek.cz) (aby mě někdo nenařknul z toho, že mu [DoS](https://cs.wikipedia.org/wiki/Denial_of_service)uju web) testuju jejich dostupnost a rychlost. Když nasbírám 10 spolehlivých proxy, přestanu s tím. Samotný scraper pak díky tomu jede velmi rychle, vše funguje, a vystačí si s méně než deseti těmi proxy.
- Upravil jsem u výše zmíněného scraperu i vyhledávané fráze. Měl jsem tam "software engineer", ale to nechytalo všechno, tak jsem přidal "developer" apod. Uvidíme, tohle se dá pak už ladit za pochodu, hlavně když to konečně nějak funguje.
- Dokončil jsem melouch pro kamaráda. Vyřešili jsme ještě deployment Python balíčku z privátního GitHub repozitáře na Heroku a bylo to. Řešení jsem [dal na StackOverflow](https://stackoverflow.com/a/64645458/325365). Potěšilo: "Moc jsi nám pomohl, jsem naprosto spokojený. A máme krásné readme! Věřím, že si u tebe někdy objednám readme i na ostatních projektech :D" Dovedu si představit, že občasné psaní readme by mě jako melouch bavilo, takže pokud chcete hezčí readme k nějakému projektu nebo potřebujete napsat jinou podobnou menší dokumentaci, klidně mi napište :)
- Pokud jste někdy potřebovali v GitHub Actions něco commitnout zpět do repozitáře, v [tomto komentáři](https://github.com/EndBug/add-and-commit/issues/56#issuecomment-720452435) jsem se rozepsal o tom, jak to udělat.
- Prošel jsem [sekci o koronaviru](https://junior.guru/learn/#covid19). Upravil jsem formulace zase zpět, aby nepoužívaly minulý čas, ale přítomný :) Taky jsem jasněji rozlišil, co se dělo na jaře a co je teď. Přidal jsem drobnou zmínku o Radůze. Odcitoval jsem Janu Večerkovou z [Coding Bootcamp Praha](https://www.codingbootcamp.cz/), ať mají radost. O bootcampu nic konkrétního nevím a neberte to jako moje doporučení, že je dobrý nebo že se vyplatí, ale přiznávám, že jsme v kontaktu a budu jejich studentům na konci listopadu něco říkat o JG. Nějaké jemné nezávislé spolupráci se nebráním, ale bootcampy aj. kurzy a workshopy zatím doporučovat nechci, protože nemám jak sám ověřit jejich kvalitu nad rámec toho, co o sobě řeknou sami v rámci svého marketingu. Pokud chtějí být na JG, [mohou si zaplatit logo na příručce](https://junior.guru/hire-juniors/#handbook), s tím není žádný problém.
- Udělal jsem si malý "strategický plánek" jak bych mohl v blízké době udělat JG profitabilní. Veškeré sales zatím úspěšně prokrastinuji, ale tak to dál nejde. Musím do toho začít víc bušit. Taky jsem se v poslední době dost vykašlal na sociální sítě, takže na ty bych se měl vrátit alespoň s dvěma pravidelnými statusy týdně, aspoň takový "heartbeat", že JG stále žije. Musím se víc soustředit na LinkedIn, kde mám cílovku v podobě HR a firem. Chci přepracovat [stránku pro firmy](https://junior.guru/hire-juniors/) a udělat z ní různé "landing pages", které by se objevovaly ve výsledcích vyhledávání a které bych mohl i cíleně firmám posílat, když je oslovím. Rozhodl jsem se více vyzdvihnout spojitost mezi diverzitou a juniory a přizpůsobit tomu nabídku firmám.
- Naplánoval jsem tedy na týden dva dopředu nějaké statusy na sociální sítě.
- Zjistil jsem, že můj úžasný [Lighthouse skript]({filename}/2020-05-11_monitoring-performance-with-lighthouse-and-circleci.md) občas spadne. Headless browser se kvůli něčemu nepřipojí apod. Věci, které se stanou náhodou a já je nijak neovlivním. Stalo se to už potřetí, zabudoval jsem tedy do skriptu nějakou _retry_ logiku.
- Protože sdíleli JG na všech svých sociálních sítích, přidal jsem mezi loga na [stránce pro firmy](https://junior.guru/hire-juniors/) i portál [Na volné noze](https://navolnenoze.cz/).
- Psal jsem si s hodně lidmi. Už v úvodu jsem zmínil, že jsem v kontaktu s jednou osobou ohledně péče o dítě a přivýdělku v IT. Napsal jsem ale i českému komunitnímu manažerovi v TopTalu, jestli jejich aktivity nemají i nějaký překryv s juniory, psal jsem si s juniorem, který se málem stal obětí švarc systému, psal jsem si s kamarádem [Vuyem](https://vuyisile.com/), který je junior a dělá freelancera v Zimbabwe, psal jsem si s několika kamarády, kteří jsou aktivní freelanceři nebo kontraktoři, a tak dále. Zkouším navázat nějakou spolupráci s [Kariérko.cz](https://karierko.cz) a jednou aktivitou, která řeší diverzitu a inkluzi při náboru do firem. Jsem také v kontaktu s redaktorem Hospodářských Novin a možná spolu upečeme a vydáme mou reakci na článek, který tam tento týden vyšel.
- Po večerech hraju [Europu Universalis 4](https://store.steampowered.com/app/236850/Europa_Universalis_IV/) a nemůžu se od toho vůbec odtrhnout. Se ou láskou k historii a geografii je pro mě tenhle "map staring simulator" v téhle době "jakože lockdownu" úplná závislost. Pokud příště poznámky nebudou, nebo v nich bude už jen nějaký seznam států, které se staly vazaly mé rozsáhlé Osmanské říše, tak se asi nedá nic dělat. Vnímám to jako nezvratný proces.
- Jo a za chvíli jdu teda pro zpestření hrát [Tmou](https://www.tmou.cz/101/), která je letos online. Očekávám teda, že nevyluštíme ani jednu šifru :D


## Update

Nestihl jsem poznámky před začátkem Tmou po sobě přečíst a vydat, takže vydávám až v sobotu o půl čtvrté. Skončili jsme kolem páté ráno u páté šifry na nádraží v České. Vypadala luštitelně, ale odpadli jsme silami. I když jsme v sobotu vstali až v jednu odpoledne, bolí mě hlava a jsem komplet rozbitý. Neumím si představit, že bychom to opravdu chodili v terénu, ale možná by nás to aspoň probralo. Zase kamarádka by u hraní venku asi nemohla během noci kojit. Všechno má svá pro a proti. Každopádně děkujeme organizátorům za pěknou hru, rozhraní s mapou bylo skvělé. Svou první Tmou v životě jsem si užil i z Prahy :)

![Screenshot Tmou]({filename}/images/tmou.png)


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Covid v evropských městech nakopl cyklistiku. Praha uvízla v době jeskynní](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2FO5hqX7hdWk%3Fssr%3Dtrue&h=5b7db2d712c89a34c8cb20b701bf9eedde41ff1ec640afb897f8f912756dee17)<br>Rozdíl vidím v tom, že o těch západních politicích se dají napsat ty věty jako “co je jeho cílem” nebo “má plán”.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
