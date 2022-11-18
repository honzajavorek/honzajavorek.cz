Title: Týdenní poznámky #65: Příručka a data z pracovních nabídek
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (6.9. — 12.9.) a tak [stejně jako minule]({filename}2021-09-05_tydenni-poznamky-64-dohaneni-malych-ukolu-prednasky-a-stipendium.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Příručka

Minule jsem psal, že chci pokračovat v CSS pro novou příručku, portovat stránku [Motivace](https://junior.guru/motivation/) na [tajnou novou stránku](https://junior.guru/handbook/motivation/) a tunit ji tak dlouho, dokud se mi nebude líbit. To se mi, myslím, povedlo.

- Nastyloval jsem trochu seznamy v textu, i vnořené.
- Zkoušel jsem, zda neudělám scrollovací ([sticky](https://developer.mozilla.org/en-US/docs/Web/CSS/position)) nadpisy a rozhodl jsem se, že neudělám, jelikož pak relativní odkazy ve stránce přestaly fungovat jako navigace (zůstávaly ve _viewportu_, tudíž nebylo kam skákat). Navíc to působilo jako přesně taková ta komplikace, kvůli které bych si zadělal na spoustu dalších problémů a běžný uživatel se bez ní obejde.
- Dodělal jsem proužek s logy firem. Vybalancovat, aby nerušily a zároveň byly vidět, to mi dalo celkem zabrat a než jsem s nimi byl spokojený, dostal proužek mnoho různých podob.

![Příručka, loga v1]({static}/images/prirucka-loga-v1.png)
První verze toho, jak mohl vypadat proužek s logy firem, ale tady mi přišlo, že loga příliš přebíjí hlavní nadpis

![Příručka, loga v2]({static}/images/prirucka-loga-v2.png)
Druhá verze

- Dodělal jsem zbytek Markdownu pro stránku Motivace.
- Styloval jsem [karty](https://getbootstrap.com/docs/5.0/components/card/) pro boxíky s odkazy.
- Styloval jsem seznamy se _success stories_, kterých bylo na stránce Motivace celkem dost.
- Zjistil jsem, že mi nefunguje správně něco v MkDocs makrech a filtrech. Musel jsem je kvůli tomu zase trochu překopat a přidat na spoustu míst `with context` (viz [dokumentace](https://jinja.palletsprojects.com/en/3.0.x/templates/#import-context-behavior)), abych mohl dělat odkazy s filtrem `|url`.
- Přidal jsem dospod stránky odkazy na předcházející a další stránku v příručce. Musel jsem si to udělat sám, i když to MkDocs nabízí v základu, protože používám navigaci MkDocs trochu jinak, než zamýšleli autoři.
- Šťoural jsem do různých detailů na stránce Motivace tak, aby se mi líbila.
- Poladil jsem fonty, aby JG preferovalo Helveticu nebo Arial, což bylo v původním CSS, ale v novém jsem měl cosi výchozího z Bootstrapu.
- Koukal jsem, zda použít [SVG sprite místo ikonového fontu](https://www.lambdatest.com/blog/its-2019-lets-end-the-debate-on-icon-fonts-vs-svg-icons/), ale pak jsem si řekl, že šťourám už fakt do nesmyslů a tohle bych neměl řešit. Navíc ten font je na bajty menší než ten SVG sprite.

### Strategie pro novou příručku

Ujasnil jsem si aktuální strategii pro novou příručku. Když jsem se pustil do přesunu příručky na nové CSS a MkDocs, neměl jsem úplně jasno v tom, kde tato aktivita začíná a končí. Mám spoustu nápadů, jak příručku vylepšovat, ale musím je dělat postupně. Například jsem chtěl postupně přidat novou stránku jako rozcestník pro příručku, rozsekat stávající stránky na jiné, změnit strukturu URL, atd. Jenže to je spousta změn najednou a spousta času.

Rozhodl jsem se, že projekt zatím nevydělává tolik, abych do toho mohl investovat takové množství času, že si mohu dovolit zatím jen pár změn. Plán je tedy takový:

- Rozcestník pro příručku zatím nebudu dělat, ani v omezené podobě. Když jsem ho začal psát, došlo mi, že i kdyby byl pouze textovou podobou (a ne formou vymazlené _landing page_), psal bych ten text několik dní, aby sdělil to, co má sdělit. Novou stránku tedy nechám zatím na jindy.
- Hlavní změnou teď bude přesun na nové CSS, aby si lidi zvykli, novou navigaci (která bude pro jednotlivé stránky vedomě horší, jelikož počítá s jejich rozsekáním na menší stránky do budoucna).
- Hlavní _business value_ bude vizuální sjednocení všech textových stránek pod jednu „příručku“ a s tím i sjednocení pruhu pro loga a navýšení ceny za „příručkové“ logo, protože se bude zobrazovat na více místech. Zlepší se orientace, zvýší se viditelnost log a zjednoduší se mi vysvětlování firmám, jaká je hodnota takového loga.
- URL zachovám původní, zatím nebudu řešit žádné redirecty.
- Stránky zachovám původní jak byly, zatím je nebudu rozsekávat na menší.
- Teď už tedy jen portuji zbylé stránky do nového CSS a uveřejním to. Pak budu sbírat feedback a prodávat loga, než přistoupím k dalším změnám.

[Dan](https://coreskill.tech/) se nemůže zbavit dojmu, že původní web měl „duši“ a byl strohý, ale zapamatovatelný, a že ten nový je generický a nudný, prostě stejný jako jiné weby. Mě zase přijde čistší, netahá tolik za oči a umožňuje mi řešit spoustu problémů s tím původním designem, o kterých mnoho lidí ani neví. Například umístění _call-to-action_ tlačítek. Čitelnost textu. Nemožnost stránku poslat do Pocketu nebo Kindlu. Přecházení očí z tečkovaných ploch, když se scrolluje. Nedostatek použitelných barev a tudíž nemožnost něco odlišit nebo zvýraznit. Nejasný způsob jak vkládat videa aj. prvky tohoto typu. A tak dále a tak dále. Ono to vypadá, že jsem vzal Bootstrap a udělal z toho _just another Bootstrap web_, ale v podstatě za každou změnou bych našel odůvodnění, proč je to krok dobrým směrem. On ten Bootstrap spoustu věcí řeší, spousta chyb, které jsem v minulém designu udělal a pak s nimi trpěl, se díky němu ztratí. Ano, výsledek je možná generický, ale možná je to částečně nevyhnutelné, pokud chci dodržet různá UX doporučení a zároveň stavět na již připraveném rozčlenění velikostí textu apod.?

Každopádně jedna věc na nové příručce chybí, a to jsou ilustrace. Ty jsem zatím zcela odstranil, protože chci nakreslit nové. Ty stávající mají nevhodný formát (např. na výšku), já bych je chtěl nově koncipovat spíše jako horizontální pruhy, které zaberou v příručce celou šířku a půjde je díky tomu jednodušeji včlenit do stránky na mobilu atd., žádné obtékání jako teď. Tak snad až tam budou ilustrace, bude to zase o trochu víc amatérské a bude to mít zpátky kousek té „duše“.


## Tanečky s korporátem

Nejmenovaný korporát mi slíbil prodloužení spolupráce, takže jsem se jal konečně dodělat papírování kolem toho, že jsem jejich _trusted supplier_. Toto papírování a vyplnění 14 dotazníků jsem odkládal zhruba rok. Na začátku spolupráce jsem všechny informace dodal, ale pak změnili svůj interní systém pro dodavatele a chtěli je po mě všechny znova. Když jsem to rozklikl, bylo tam milion dotazníků. Tak jsem se zapřel, že to vyplním, až budu mít fakturu na další rok.

Kumar z Indie mi čas od času napsal, ať to vyplním. Pak mi začal psát Vinodini, ten přikládal i vykřičníky. Ale já dřív v korporátu pracoval, takže jsem věděl, že mám času dost a investoval jsem do dotazníků energii až ve chvíli, kdy to pro mě mělo nějaký význam - tedy opravdu až teď, když korporát naznačil, že objednávka na další rok bude.

Také díky svému angažmá v korporátu znám i další triky, například jak vyplnit do políčka typu „nahrajte soubor“ odkaz na webovou stránku:

![Jak se dělá PDF]({static}/images/docs-privacy-policy.png)
Moje _Zásady ochrany osobních údajů_, když je mám někam nahrát jako PDF


## Spolupráce s Czechitas

Měli jsme call s Czechitas o tom, že bych jim mohl předávat data z nabídek práce a ony by nad nimi dělaly analýzy. Také bych díky tomu získal větší páku na scrapování Jobsů a celkově je pro mě dobré, pokud se s Czechitas mohu nějak kamarádit, přece jenom by byla škoda fungovat paralelně vedle sebe bez jakékoliv synergie, když jsme na stejném písečku a nekonkurujeme si.

Dohodli jsme si přes call potřebné kroky, sdělili jsme si co kdo má a potřebuje a s Martinou, s níž budu na úkolu spolupracovat, si teď píšeme a domlouváme nějaké API. Martinu jsem za účelem domlouvání pozval do klubu. Sice mě API trochu děsí, protože to znamená, že bude nějaká část JG, kolem které budu muset být trochu opatrný a nebudu ji moct měnit z commitu na commit jak se mi zachce, ale poté, co jsem viděl [API od Levelse](https://remoteok.io/remote-dev-jobs.json?api=1), zůstávám asi klidný, jen musím zapomenout na vše, co o API vím.

Než dám Czechitas data, chci trochu překopat datový model. Jednak to usnadní dost věcí pro tento účel, jednak jsme o tom stejně mluvili už s [Mílou](https://milavotradovec.cz/), který pro JG programuje třídění nabídek práce pomocí AI.

Překopal jsem trochu balíčky v kódu, abych mohl přidat [Scrapy](https://scrapy.org/) scrapery, které nesouvisí se současnými nabídkami práce. Vše jsem dal do balíčku `sync` a některé věci zobecnil. Pak jsem potřeboval vytvořit paralelní balíček, který už by fungoval novým stylem a s novými modely, ale nemohl jsem přijít na název, protože `jobs` už má stará architektura. Nakonec jsem skončil u sice blbého, ale funkčního `employments`.

Napsal jsem scraper, který stahuje zálohy databáze z CI a z nich čte historii, kterou bude ukládat do tabulky a deduplikovat. Tím získám SQLite databázi s historií pracovních inzerátů (na rozdíl od současné splachovací SQLite, která se vždy vytvoří znova a pak zahodí) bez toho, abych musel mít na JG nějaký _runtime_ a musel se o něj ve dne v noci starat. Na tyto záznamy chci pak navázat 1:1 další tabulku, kde budou informace pouze k aktuálně inzerovaným věcem, atd. Uvidím, jak se mi to podaří celé zorganizovat, spousta přemýšlení probíhá za pochodu. Dále jsem rozpracoval prototyp toho, jak mohu v MkDocs vygenerovat soubor, který není stránka. Vygeneroval jsem zatím [tohle](https://junior.guru/api/jobs.json), jde to.

Také jsem u toho všeho zjistil, že mám rozbitý scraper na LI a monitoring mi to nechytl. Ajajaj! Rozbitý scraper nevadí, mlčící monitoring vadí. Budu to muset všechno opravit. Holt pracovní nabídky na JG dlouho nedostaly lásku a teď do toho šťourám, tak nacházím pavučiny :/

Plán je především opravit LI a dodělat export pro Czechitas, zbytek překopu zase jindy. S Mílou se pak domluvím, co by prioritně pomohlo jemu. Jinak si budou muset pracovní nabídky ještě počkat, mám spoustu jiných věcí, kterým se potřebuji teď věnovat a vydělávají víc peněz.


## Další poznámky

- Na lásku pro bota nebo další aktivity v klubu zatím nezbyl čas, upřednostnil jsem teď spolupráci s Czechitas na datech z pracovních nabídek a vrátím se k tomu, až bude export hotový.
- Viděl jsem [tohle](https://twitter.com/dagorenouf/status/1430916255758831617) a připomenul jsem si, že JG ještě stále nevydělává miliony a měl bych si méně hrát a víc přitlačit na věci, které ty miliony přinesou.
- Zapsal jsem si feedback na leták pro neziskovky a dětské domovy (viz minulé poznámky) od různých lidí, ale zatím jsem dál v tomto směru nic nedělal. V pondělí se mám ještě s někým sejít, s kým to celé proberu. Taky jsme s Mews probírali, zda případně mohou podarovat i nějaké staré počítače, kdyby bylo potřeba je někomu znevýhodněnému dát.
- Prošel jsem nasbírané maily a odpověděl, komu jsem mohl. Prošel jsem klub, vítal lidi, psal odpovědi.
- Mám v klubu někoho, kdo dělal CNC programátora, tak jsem mu nechal přečíst [odstavec o této profesi](https://junior.guru/motivation/#cnc) a nasbíral od něj feedback, jestli tam neplácám hlouposti.
- Zmenšil jsem ToC na [FAQ](https://junior.guru/faq/), aby to nebyla taková nepřehledná hrůza.
- Užili jsme si [Žižkovské mezidvorky](https://facebook.com/events/504884303959208/) i s kočárem.
- Během 7 dní od 6.9. do 12.9. jsem při procházkách nachodil 14 km. Celkem jsem se hýbal 8 hodin a zdolal při tom 14 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Portovat zbylé 3 stránky příručky na nový design a uveřejnit „novou“ příručku.
2. Dopracovat export pracovních nabídek pro Czechitas, opravit LI, přidat logo Czechitas na web.
3. Sejít se na téma podpory znevýhodněných, připojit se na call výboru [Pyvce](https://pyvec.org/).


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Ideje počkají, až porazíme Babiše! Na kampani s Milionem chvilek](https://a2larm.cz/2021/09/ideje-pockaji-az-porazime-babise-na-kampani-s-milionem-chvilek/)<br>„Podobně jako aktivisté Milionu chvilek se pozitivně naladění občané často snaží své kritické spoluobčany poučovat v domnění, že druhá strana jenom nemá ty správné informace. Lidé v průzkumu definovaní jako ‚kritičtí‘ ale naopak často mají pocit, že jejich každodenně prožívaným socioekonomickým problémům nikdo nevěnuje pozornost.“
- [Delays Aren't Good Enough—Apple Must Abandon Its Surveillance Plans](https://www.eff.org/deeplinks/2021/09/delays-arent-good-enough-apple-must-abandon-its-surveillance-plans)<br>„EFF is pleased Apple is now listening to the concerns of customers, researchers, civil liberties organizations, human rights activists, LGBTQ people, youth representatives, and other groups, about the dangers posed by its phone scanning tools. But the company must go further than just listening, and drop its plans to put a backdoor into its encryption entirely.“
- [Místo herců umělá inteligence. Editor Hlasem umí převést texty do audia během vteřiny](https://www.startupjobs.cz/newsroom/misto-hercu-umela-inteligence-editor-hlasem-umi-prevest-texty-do-audia-behem-vteriny)<br>Hezký nápad a provedení

<small>Upozorňuji, že to není vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
