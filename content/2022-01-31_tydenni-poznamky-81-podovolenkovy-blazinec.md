Title: Týdenní poznámky #81: Podovolenkový blázinec
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl zase nějaký ten týden (20.1. — 31.1.) a tak [stejně jako minule]({filename}2022-01-19_tydenni-poznamky-80-spousteni-podcastu-a-psani-o-cv.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Dohánění nepřítomnosti

Po dovolené jsem šel na sociální sítě, do mailu, na Pyvec Slack a do klubu. Snažil jsem se oddělit důležité od nedůležitého nebo dohnat resty, které jsem měl v mailech třeba i delší dobu. Bylo toho fakt hodně a zavalilo mě to natolik, že jsem i tento týden flákal trochu své vlastní postování na sociální sítě.

V klubu jsem se snažil přečíst, co šlo, ale nějaké zamotané diskuze jsem přeskákal. Záda mi v době nepřítomnosti kryl [Dan Srb](https://coreskill.tech/), který v klubu dělá moderátora.


## Upgrade gql

Mergnul pull requesty od dependabota, co se nasbíraly. U knihovny gql se objevila nová major verze a testy neprošly, tak jsem zkoumal, čím to je.

Nakonec jsem identifikoval dva problémy, [tento](https://github.com/graphql-python/gql/issues/290) a [tento](https://github.com/graphql-python/gql/issues/290#issuecomment-1022425154). Oba jsem nakonec vyřešil a nešlo zřejmě o vadu nové verze knihovny.


## Změny v klubu

Po čase jsem došel k názoru, že už některé návrhy na změny v klubu časem uzrály a měl bych je udělat. Povolil jsem vlákna ve více kanálech. Změnil jsem ikonu pro roli hodně pomáhajících lidí, aby nebyla tak červená, protože to prý vypadá jako notifikace. Přejmenoval jsem některé kanály v klubu tak, aby lépe odpovídaly tomu, co se tam řeší.


## Komunikace s firmami

Komunikoval jsem s firmami a domlouval nové spolupráce. Zkoušíme se na něčem domluvit s Jetveo. S Janem z Mews jsme si naplánovali společnou procházku s kočárkem. Vyřešili jsme pár provozních věcí a pokecali o spoustě zajímavých věcí.

S Appliftingem jsem měl sales call, kde jsem představil JG a ukázal, jak to funguje. Už bych k tomu měl konečně natočit screencast. Jak se ty sales cally opakují, už tuším, co by v něm mělo přesně být a na jaké otázky by měl odpovědět. Nicméně jsem líný to natáčet a zároveň mě baví povídat si reálně s lidmi, poznáme se na tom callu (osobnější), já si je pak přidám na LinkedIn, kde pak čtou moje statusy, apod.

Je tedy otázka, do jaké míry to může škálovat. Zatím mě to asi nezatěžuje tolik, abych to urychleně musel nějak řešit.


## Podcast

Přečetl jsem si smlouvu od Seznamu ohledně podcasty.cz a poslal jim nějaké dotazy. Na první dojem to ale vypadá, že je to OK a jen ošetřují, aby mohli k obsahu přilepovat reklamy, vyplácet nám provizi a zaručit, že práva na obsah zůstávají nám.

Amazon někde vychytal, že existuje náš podcast a poslal mi mail, ať to [přidám do jejich služby](https://podcasters.amazon.com/), kterou sice vůbec neznám, ale přidání na rozdíl od Seznamu vypadalo, že bude trvat 3 minuty, tak jsem to udělal.

Pája už má připraven druhý díl podcastu. Soubor mám k dispozici, ale ještě jsem to neslyšel. Vyjde zřejmě kolem půlky února.


## Firmy v klubu

Začal jsem pracovat na tom, aby byly firmy v klubu víc vidět. První krok byl generovat pro každou firmu botem roli, kterou přiřadím lidem z firmy a díky tomu půjde poznat, kdo je odkud. Doteď tam byla jen obecná role „sponzorujeme klub“.

Protože už byl konec dne, nechal jsem to tak, aby bot role vždy smazal a vytvořil znova. Což jsem věděl, že není ideální, protože pokud udělám na roli mention nebo tak něco, druhý den už původní role nebude existovat a mention bude rozbitá, ačkoliv už bude existovat nová role se stejným názvem. Ale říkal jsem si, že pár dní to tak vydrží, než to opravím.

Mezitím Dan zajásal, že jsou nové role a využil je pro správu kanálů, které využívá k provozu svého mentoringu. Bot mu tyto role druhý den smazal a chudák mi psal, že ztratil veškerá oprávnění ke všemu, apokalypsa. Holt strasti _early adopters_ :D Sice _known issue_, ale bylo bohužel _known_ jen pro mě.

Takže tohle bych teď měl ještě opravit, než budu dělat něco dál.


## Další poznámky

- [Svetlana](https://kompilator.cz/) mě začala [podporovat na GitHub Sponsors](https://github.com/sponsors/honzajavorek/). Díky moc!
- Udělal jsem balíčky samolepek a poslal je PyLadies do Ostravy, Olomouce a Plzně. Brno teď nic neorganizuje a v Praze si pro balíček přijde poslíček. Beztak mi už doma došly obálky.
- Refaktoroval jsem kód, který bot používá na kontrolu toho, zda už byla pravidelná zpráva postnutá nebo ještě ne a v tom případě ji postne. Kód už se totiž opakoval v příliš mnoho skriptech, asi čtyřech. Vše jsem i otestoval. Tedy vše asi ne, protože souhrn nejdůležitějšího dění v klubu na konci týdne se postnul 5x za sebou. Zatím nevím proč.
- Propagoval jsem [svůj článek na Heroine o CV](https://www.heroine.cz/zeny-it/7091-jak-si-napsat-dobre-cv-a-byt-videt-pri-hledani-prvni-prace-v-it). Sice po týdnu od vydání, ale přece! Propagoval jsem i [článek Zuzany Pechové o portfoliu](https://www.heroine.cz/zeny-it/7047-jak-si-vybudovat-portfolio-a-ukazat-co-uz-v-it-umite), protože myslím, že [přináší zajímavou novou perspektivu](https://twitter.com/honzajavorek/status/1486267371262291973).
- Prošel jsem po snad dvou nebo třech týdnech konečně CV jednoho kamaráda a člena klubu, které mi přišlo v soukromé zprávě. Snažím se odpovídat i soukromě na vše, co mi kdo píše, ale popravdě, někdy mi to prostě trvá. CV bylo parádní, takže nezbylo než komentovat drobnosti.
- Náhodou jsem v Discord helpu narazil na [funkci pro placené členství](https://support.discord.com/hc/en-us/articles/4415163187607-Premium-Memberships-for-Servers). Zatím je to nějaká beta, která není smrtelníkům přístupná, ale pro mě je to signál, že placené členství pro jednotlivé servery je něco, co chce Discord do budoucna podporovat. Zda bude vynucovat svůj platební systém místo např. [Memberful](https://memberful.com/), které používám, to je druhá věc, ale pozitivní je, že je můj byznys model zahrnut v jejich plánech a nechtějí to třeba zakázat.
- [Luboš](https://blog.zvestov.cz/) mě poprosil, zda bych v klubu mezi juniory nezpropagoval možnost podílet se na stránkách pro [projekt geomapa](https://geomapa.lounovicepodblanikem.cz/). Zatím se nikdo neozval, ale zkusím to v klubu ještě připomenout.
- Czechinvest inzeroval na JG, takže jsem to zpracoval a [nabídku publikoval](https://junior.guru/jobs/adbca516fcb8da745a785a98e74db6fd89f131506cce8d69434b6cbc/). Přijde mi dost na hranici toho, co já považuju za juniorní, ale přimhouřil jsem oko, protože lidi kolem PHP bývají i jako junioři celkem zběhlí ve více technologiích jako CSS, HTML, atd. (resp. nic jiného jim moc nezbývá, na rozdíl od Pythonistů, kteří si najdou práci prostě i jen s Pythonem a Gitem).
- Přečetl jsem si o [konci nabídek práce na Stack Overflow](https://meta.stackoverflow.com/questions/415293/sunsetting-jobs-developer-story) a přemýšlel nad tím, že mi jednak zmizí jeden zdroj pro JG, jednak zda mohu něco z jejich _experience_ využít v budoucnu u sebe.
- Hledal jsem nějaké geopolitické podcasty. Pár jsem jich zkusil, ale většinu jsem zase zahodil. Kromě jednoho, který teď celkem sjíždím a baví mě: [The Red Line](https://www.theredlinepodcast.com/).
- Během 12 dní od 20.1. do 31.1. jsem při procházkách nachodil 36 km, na túrách nachodil 11 km, sjel na lyžích 39 km. Celkem jsem se hýbal 18 hodin a zdolal při tom 86 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Pokračovat ve zvyšování viditelnosti firem v klubu.
2. Ozvat se firmě, které členství končí. Udělat si upomínátko kdy které firmě končí roční členství v klubu.
3. Připravovat přednášky v klubu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Kouzlo vyprchalo? Harry Potter stárne a jeho fanoušci s ním](https://www.seznamzpravy.cz/clanek/kultura-chlapec-ktery-prezil-slavi-vyroci-zaujme-harry-potter-i-dalsi-generaci-186033)<br>„…co když Harry Potter přestane diváky zajímat? Co když zevšední mladším generacím?“
- [Kde se dá v Praze zaparkovat?](https://www.youtube.com/watch?v=z8vz6GFZD1k)<br>Souhlas
- [Vysílač](https://overcast.fm/+lh3KU6i_U)<br>Masakr. Jak to reálně vypadá, když se dostanete do Česka jako někdo, kdo tady žádá o azyl.
- [Putin’s Wager in Russia’s Standoff with the West](https://warontherocks.com/2022/01/putins-wager-in-russias-standoff-with-the-west/)<br>„Russian force posture can enable a range of choices, but it is difficult to see how Moscow accomplishes any lasting political gains without having to resort to maximalist options.“
- [Jak jsem totálně zvorala pohovor](https://www.hanakonecna.cz/jak-jsem-totalne-zvorala-pohovor/)<br>Článek o tom, jak se juniorka prodírá pohovorem a pokazí ho. Poučné pro juniory i pro ty, kdo pohovory připravují.
- [Jádro nikdo nezakazuje, bude s námi hodně dlouho, říká Čech, který v Bruselu napsal kritizovanou taxonomii](https://archiv.hn.cz/c7-67024090-pp96p-98aa1daef1f2a59)<br>Vysvětlení toho, jak je myšleno nové klasifikování energetických zdrojů v EU.
- [Jak počítačová myš zatřásla s akademií. Historie a budoucnost plagiátorství](https://finmag.penize.cz/veda-a-technika/431771-jak-pocitacova-mys-zatrasla-s-akademii-historie-a-budoucnost-plagiatorstvi)<br>Stručná historie plagiátorství a nastínění toho, jak to může vypadat do budoucna.
- [61 - Turkish Influence in Central Asia](https://theredline.libsyn.com/61-turkish-influence-in-central-asia)<br>Objevil jsem tento podcast o geopolitice a začal mě celkem bavit. V tomto díle se do detailu rozebírají pozice a plány Turecka. Přišlo mi to nesmírně zajímavé.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
