Title: Týdenní poznámky #44: Přednáška s Láďou Prskavcem
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (29.3. — 2.4.) a tak [stejně jako minule]({filename}/2021-03-26_tydenni-poznamky-43-pani-z-hr-kuryr-z-dame-jidlo-mkdocs-a-nova-uvodni-stranka.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub podporovatelů](https://junior.guru/club/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tentokrát tedy píšu poznámky už ve čtvrtek, protože v pátek je volno a já volna dodržuji. A kromě toho jej potřebuji využít ke stěhování.


## Přednáška

Hlavní událostí týdne byla [středeční přednáška Ládi Prskavce o Jamstacku](https://junior.guru/events/#2021-03-31T18-00-00) pro členy klubu. V předchozích týdnech jsem vyřešil nahrávání přednášek na mém počítači a přišlo mi, že už od první přednášky nějaký čas uplynul, takže by bylo záhodno naplánovat další. Láďa mohl hned tuto středu, takže jsem to risknul a většinu pondělí věnoval oznámení a přípravě přednášky. Prošel jsem svůj todo list k přednášce a postupně vše odškrtával. V den přednášky jsem vyzkoušel nahrávání a s [Danem Srbem](https://coreskill.tech/) jsme doladili ještě nějaké detaily, aby to lépe znělo, že mám mít spíš drátová sluchátka, a tak. Na přednášku nakonec dorazilo do 20 lidí, což může mít různé příčiny:

- Velmi hezké počasí ten den a nastupující jaro,
- téma jsem pojmenoval Jamstack, což možná začátečníkům tolik neřeklo (možná lepší: „Jak si snadno vyrobit a nasadit staticky generovaný blog“),
- lidé mohli předpokládat, že přednášku zase nahraju, takže o ni nepřijdou, když nepřijdou,
- oznámení proběhlo v pondělí, pouhé dva dny před samotnou událostí.

Každopádně kdo dorazil, tomu se přednáška líbila, zhusta to lidi psali do chatu a děkovali za přínosné informace a odkazy k nastudování. Video jsem nahrál na YouTube hned, mám tam šablonu na popisek, takže to trvalo jen chviličku, než bylo vše připraveno a mohl jsem záznam odkázat z klubu a pak i z webu. [Stránku s akcemi](https://junior.guru/events/) na webu stále spravuji pouze jen přesouváním a editací HTML tagů.


## MkDocs

Prozkoumával jsem dál možnost postupně předělat JG na MkDocs. Vymyslel jsem, jak vyřešit CSS na stránkách, které jsou vyrobené pomocí MkDocs. Prostě jsem doplnil pár pravidel do CSS a doplácl to tam tak, aby vypadaly stejně. Bylo to nejefektivnější a v současnosti nejekonomičtější. Musím změny dělat postupně a nemůžu přepisovat backend a frontend zároveň. Nejdřív backend, pak jednou třeba frontend.

Tím budiž stránka [/privacy/](https://junior.guru/privacy/) první stránkou, kterou na JG generuje MkDocs. Další je [/tos/](https://junior.guru/tos/), kde ale navrchu není design správně. Aby byl správně, musím do MkDocs doplnit podporu pro nějaké komponenty nebo šablonování. A to jsem našel u pluginu [mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/). Myslím si, že ten mi umožní vše, co budu potřebovat. Ve čtvrtek jsem si přečetl celou jeho dokumentaci a hned na GitHubu projektu založil několik issues a poslal několik Pull Requestů. Většina je oprava překlepů v dokumentaci a pak jeden [dotaz](https://github.com/fralau/mkdocs_macros_plugin/issues/75). Jednak projektu opravami pomůžu, jednak díky nim uvidím, jak autor reaguje a jestli na tom mám stavět celý svůj byznys. Dokumentace je taková trochu divoká, autor velmi rád používá různé boxíky na poznámky a upozornění, což ji v důsledku dost znepřehledňuje, ale hlavní je, že dokumentace existuje. Občas jsem pozvedl obočí nad určitými design decisions, ale nebudu dělat chytráka, zatím to vypadá, že toto řeší všechny moje problémy a raději přispěju do něčeho, co už existuje a kde nás na údržbu bude víc, než abych vynalézal vlastní kolo.


## Machine Learning

Kamarád Míla Votradovec se začal šťourat v ML a hledal data a projekt, na kterém by si to mohl vyzkoušet. Ptal se mě, jestli na JG něco nemám. No, mám. Mám robota na nabídky práce a je to dost ruční práce, je třídit. Jakože ne úplně ruční, ale je to hromada regulárů a je to hodně práce vyrobit, odladit, udržovat, opravovat.

Míla si už v předchozích týdnech s pomocí mého vedení stáhl nějaká historická data a začal na nich trénovat modely. Já tomu moc nerozumím, ale vrátil se s tím, že to celkem funguje. Takže jsme si zavolali a vymysleli další postup. Idealistická, naivní vize, kterou jsme vytvořili, je následující:

Na webu by byl výpis nabídek, které robotem prošly. Pak by tam byl bokem i výpis nabídek, které robot vyhodil. Já osobně, ale i návštěvníci webu, bychom mohli oba seznamy pročítat a pokud by něco bylo klasifikováno špatně, mohli bychom kliknout na nějaké tlačítko a dát zpětnou vazbu. To by šlo udělat i na statických stránkách, třeba přes Google Analytics event. Následně se model přetrénuje a bude se takto postupně učit. To by znamenalo, že klasifikace nabídek se bude vylepšovat čistě tím, že si někdy udělám čas a poklikám to, nebo i tím, že na to budou klikat lidi. To by bylo mnohonásobně méně náročné na údržbu než to, co mám teď.

Míla věří, že by možná šlo snadno natrénovat i Slovenštinu, ale to si já nemyslím. Na druhou stranu, přidat teď Slovenštinu znamená programovat prakticky celého robota znova pro další jazyk a dlouze to ladit a probírat se hromadou dat ručně a pak zase ladit, psát testy a ladit. Kdyby robot fungoval přes ML, tak by mi „stačilo“ stáhnout třeba 1000 nabídek z [Profesia.sk](https://www.profesia.sk/), jednou bych je prošel a ručně klasifikoval, ale následně by to už bylo hotové. Pak už by se to učilo „samo“.

Jsem zvědavý, co z toho nakonec bude. Každopádně takovéto věci se vám mohou stát asi jen tehdy, pokud je váš projekt Open Source. K dnešnímu dni jsem už dostal přes Pull Requesty několik oprav textu, a to jsem ani repozitář nijak pro přispěvatele nepřipravil. Toto je další krok k tomu, aby JG byl časem projekt, do kterého přispívají i další z komunity kolem něj.


## Priorita

Řešil jsem, co je teď vlastně moje priorita. Rád bych pokračoval v MkDocs a třeba i předělával CSS na webu, ale tyto věci nemají žádnou hodnotu pro uživatele, pouze v hodně rozmlžené a dlouhodobé podobě. V době, kdy projekt ještě nevydělává dost na to, abych se mu mohl v budoucnu věnovat naplno, si toto nemohu dovolit. Co je tedy ta jedna hlavní věc, kterou bych teď měl dělat? Jakým jedním slovem ji mohu pojmenovat?

Po ranním pondělním zamyšlení jsem si ujasnil, že jsou to „zvyšování hodnoty klubu“ a „marketing“. Potřebuju prostě stále do klubu hlavně dostat víc lidí a firem. To mohu udělat tak, že se o něm doví, a vylepšit tím, že pro členy klubu bude více a více různých výhod a vychytávek. Napsal a nastudoval jsem si na zahraničních webech, co takového mohu dělat. Udělal jsem si z toho kartičky v Trellu a celý nový sloupec, z něhož bych teď měl sekat jednu věc za druhou.

No a chtělo by to ještě i nějaké ty marketingové nápady. Trochu mi dochází dech. Nevím tak úplně, jak bych se zase dostal na úvodní stránku Hospodářek nebo něco podobného :) Ale třeba mě něco napadne.


## Další poznámky

- Mám nového podporovatele! [Petr Vácha](https://github.com/petrvacha) mě teď podporuje [přes GitHub Sponsors](https://github.com/sponsors/honzajavorek/). Hned jsem jej přidal do [seznamu podporovatelů](https://junior.guru/donate/#sponsors) a pozval do klubu. Pokud mě chcete podpořit podobně jako Petr, stačí, když si [koupíte členství v klubu](https://junior.guru/club/). Je ale fakt, že na GitHubu nebo Patreonu mě můžete podpořit vyšší částkou, než je členství v klubu, a konkrétně GitHub ji zatím stále zdvojnásobuje (měl to dělat jen rok a podle mě to už mělo teď nekdy končit, ale stále to zdvojnásobuje a já si nestěžuju). Tyto příspěvky stále tvoří významnou část mého měsíčního příjmu a jsem za ně rád. Každý podporovatel má automaticky přístup i do klubu, i když jsem odměny na GitHubu ani Patreonu s touto informací ještě neaktualizoval.
- Domlouvám už další přednášku. Zatím prozradím jen to, že to bude frontendistka a bude to super.
- Napadlo mě, že bych mohl kromě přednášek dělat i AMA seance. Přemýšlel jsem, s kým by dávaly největší smysl a pak mi došlo, že s recruitery, tedy jak říká yablko, s dávači pohovorov. Jednoho jsem hned naťukl a odpověď byla, cituji, „thousand times yes“. Naťukl jsem to i v klubu a tam to má hromadu palců nahoru v reakcích, takže asi už stačí akorát najít termín a naučit se takové seance dělat, připravovat, moderovat :)
- Poslal jsem [březnový newsletter s nabídkami práce](https://us3.campaign-archive.com/?u=7d3f89ef9b2ed953ddf4ff5f6&id=4d3b35637d). Zvládl jsem to už v úterý, jednak proto, že jsem věděl, že v den přednášky na to nebudu mít vůbec čas, jednak proto, že jsem tam chtěl přednášku promovat. Z MailChimpu zmizela možnost odeslat newsletter do 24 hodin znovu lidem, kteří jej ještě neotevřeli, což v minulosti zlepšovalo doručování. Netuším proč.
- [Daniel Srb](https://coreskill.tech/) si všiml, že když budu mít v CSS `.header__subnav { overflow-x: auto; }` místo `scroll`, tak zmizí některé scrollbary, které se občas na webu zbytečně zobrazovaly. Přemýšlím, jak dlouho tam byly, protože vím, že mi někdo posílal podobný bug report už někdy na začátku, co jsem to menu vyrobil, ale jak na macOS scrollbary vůbec nevidím, tak jsem na to zapmomněl.
- V klubu jsem před názvy kategorií přidal emoji, aby se v levém panelu na Discordu dalo lépe orientovat. Myslím, že to ničemu nevadí a že to s orientací pomáhá. Opět [Danův](https://coreskill.tech/) nápad.
- Všiml jsem si, že StackOverflow změnili trochu HTML u nabídek práce, takže mi je scraper tahá bez data uveřejnění a robot je všechny hází do koše. Vytvořil jsem test na nové HTML a opravil jsem to.
- Šel jsem na poštu a aktivoval jsem si konečně HW klíč z [MojeID](https://overeno.mojeid.cz/), díky kterému jsem se pak mohl online sečíst ve sčítání lidu. Nad otázkou, jaké je moje povolání, [jsem se celkem zapotil](https://twitter.com/honzajavorek/status/1376978562419425280).
- Zrušil jsem webovku na javorek.net, kde byl náhrobek pradávné společné agenturní činnosti mě a [Michala Wiglasze](https://michalwiglasz.cz/), kterou jsme provozovali 2007 až 2012. Zrušil jsem i maily, takže na @javorek.net už nic nedojde. Stejně tam chodil už akorát spam, oba máme už sto let jiné maily. [Repo](https://github.com/honzajavorek/javorek.net/) jsem archivoval taky. Když jsem na něj teď při psaní poznámek šel, abych si okopíroval z adresního řádku odkaz, všiml jsem si [souboru nostalgia.png](https://github.com/honzajavorek/javorek.net/blob/gh-pages/nostalgia.png), klikl na něj a docela jsem se zasmál.
- O víkendu jsem měl trochu času, tak jsem udělal nějaké Pull Requesty na [dokumentaci Pyvce](https://docs.pyvec.org/).
- Na regionálních stránkách s nabídkami práce na JG často nic není, protože prostě juniorní nabídky v Budějcích nebo Hradci aby člověk pohledal. Už dřív jsem tam měl větu „zkus omrknout ostatní nabídky, nejvíce jich bývá v technologických centrech, jako jsou Praha, Brno, nebo Ostrava“, ale teď mě napadlo, že kvůli (nebo díky?) covidu přibývá nabídek práce na dálku, takže jsem dodělal doplňování nabídek těmi na dálku, pokud žádné nejsou v místě. Viz třeba [Jihlava](https://junior.guru/jobs/region/jihlava/).
- [Uzavřeli jsme partnerství](https://twitter.com/honzajavorek/status/1377607653313159171) s [CyberMagnolia](https://cybermagnolia.com/), která sdružuje ženy v IT v Česku, aby je propojila bez ohledu na technologie a úroveň seniority. Zatím je z toho přednáška a logo na webu, ale určitě ještě něco vymyslíme. Chtěl bych mít na webu loga zvlášť pro komunitní partnery, ale zatím jsem dal logo do jedné lajny s firmama.
- Během 6 dní od 27.3. do 1.4. jsem naběhal 9 km, při procházkách nachodil 2 km. Celkem jsem se hýbal 2 hodin a zdolal při tom 11 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Přestěhovat se během Velikonoc o pár ulic vedle.
2. Dokončit PoC landing pages na klub.
3. Poslat DPFO.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Sádlo](https://getpocket.com/redirect?&url=https%3A%2F%2Fwave.rozhlas.cz%2Fsadlo-8398667&h=3ade27fe126f2261e02442dd14455d659787e6463006e1eb15cc20e3aef242cb)<br>Poslechli jsme si hned několik dílů a je to fakt dobrý. Ať už jste tencí, tlustí, nebo ani jedno, pusťte si to, je to FAKT dobrý.
- [Why I decided to quit my job and go full time on my side business](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.alexwest.co%2Fwhy_i_quit_my_job&h=2268fd45969b6ec7c44d2adb0b19bfb56f2a7fa4876138e56bf1661ae502f652)<br>Týpek popisuje důvody, proč odešel z práce, aby dělal na svém projektu. Něco z toho se mnou rozhodně rezonuje.
- [The next frontier after remote work is async](https://getpocket.com/redirect?&url=https%3A%2F%2Flevels.io%2Fasync%2F&h=770834f9b634250717759586fab24d0b87936bd7e180cc4f7ad265291576f06b)<br>Je vaše práce asynchronní, nebo jedete 9-5 a volné víkendy, akorát z domova?
- [SQLite is not a toy database](https://getpocket.com/redirect?&url=https%3A%2F%2Fantonz.org%2Fsqlite-is-not-a-toy-database%2F&h=d8dd60e6a91c733561089a32fe6b73c32bf6658ca7fe8353724d9c518b61ba60)<br>Proč je SQLite super.
- [Jak zakulacení rohů prvků ovlivňuje výsledný design](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.designui.cz%2Flekce%2Fjak-zakulaceni-rohu-prvku-ovlivnuje-vysledny-design&h=691c51d0a381e8fb4b65848d7cff64192250511aa2f3bab9f4d1c9c65347f16b)<br>Zajímavé, dověděl jsem se zase něco nového.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
