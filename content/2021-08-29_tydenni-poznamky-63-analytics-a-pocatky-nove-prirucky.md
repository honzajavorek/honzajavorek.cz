Title: Týdenní poznámky #63: Analytics a počátky nové příručky
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (23.8. — 27.8.) a tak [stejně jako minule]({filename}/2021-08-20_tydenni-poznamky-62-dvounedeli.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Nové náhledové obrázky

Jak jsem psal minule, než budu novou klubovou stránku někde propagovat, chtěl jsem vyrobit lepší náhledové obrázky pro sociální sítě. Tak jsem se na to vrhnul a chvíli zabralo iterování nad různými podobami, až jsem došel k něčemu, co asi není největší pecka, ale jsem s tím poměrně spokojený. Vložte si `https://junior.guru/club/` do [debuggeru](https://developers.facebook.com/tools/debug/) a uvidíte, co jsem vytvořil. Horší byla druhá fáze, kdy se mi nedařilo, aby se obrázek všude správně zobrazoval. Trochu jsem válčil s tím, aby se vygenerovala absolutní URL a vše bylo jak mělo. Nakonec jsem to prohnal i přes Cloudinary, takže obrázky budou _very_ optimalizované, _such_ rychlost, _wow_.

Jakmile byl obrázek, vymyslel jsem [tweet](https://twitter.com/honzajavorek/status/1430187105246973957), který klub v jedné větě odprezentuje a ten jsem si nastavil jako _pinned_ na Twitteru. Zatím jsem víc nic dál nepropagoval. Pokud chcete, můžete mi pomoct tím, že ten tweet pošlete dál.


## Discord

Pouklízel jsem různé věci v Discordu, připnuté příspěvky, kanály, atd. Mentoring v klubu jsem kompletně předělal na thready. Spolu s [Mews](https://github.com/MewsSystems/developers) jsme zavedli možnost, aby si junioři rezervovali v kalendáři několika jejich lidí hoďku na call nebo na to, aby spolu něco probrali, na něco se zeptali. Strašně se mi to líbí. Jenže jsou lidi nesmělí a nerezervujou. Do bota jsem dodělal věc, která jednou za týden tuto možnost všem v mentoring kanálu aspoň připomene. Snad to nebude moc otravné pro ty, kteří tam jsou dlouhodobě a snad to bude dostatečně tuto možnost ukazovat všem novým. Pokud se objeví další firma, která by to chtěla nabídnout, akorát je přidám do výčtu v této pravidelné zprávě.

[Discord.py](https://discordpy.readthedocs.io/) zatím nepodporuje thready, takže se mi po jejich zapnutí rozbil bot a musel jsem ho opravit. Thready zatím přeskakuje. Blbé je, že [maintainer teď vyhořel](https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1), takže kdo ví kdy ta podpora pro thready bude a jestli vůbec. Ajaj!


## Článek na blog

Po dlouhé době jsem napsal nějaký delší článek na blog, na téma, které mi už nějakou dobu vrtá hlavou. Kamarád se mě ptal, jak takový článek vzniká, když má člověk dítě a tak, takže tady je postup.

Bavím se na určité téma se spoustou lidí a čtu na to téma spoustu článků. Vidím nějaký opakující se vzor nebo mám jiné pozorování a chci o tom napsat na svůj blogísek, uspořádat si tam myšlenky, získat zpětnou vazbu, mít radost z psaní. Stejný, jako když jsem na tentýž blogísek psal ve 20. Tím to začne.

Takže chci napsat ten článek, ale nemám na to čas, nebo nevím, jak to téma uchopit. No a nejhorší věc, mám autorský blok, protože mám dojem, že ten blog už čte příliš mnoho lidí a že tam nemůžu psát ty samý blbosti jako ve 20. Že to musí být super ozdrojovaný a vyladěný a argumentačně neprůstřelný a musí to přečíst deset lidí před publikací a dát mi na to zpětnou vazbu a vychytat překlepy. Úplně stejně jsem chtěl napsat a vydat už pět článků, ale tuhle fázi žádný nepřežil. Lidi to rozcupovali, řekli, že to nemá hlavu a patu, našli díry v argumentaci, nebo jsem se k tomu prostě už nedokázal vrátit a dokončit to.

Tentokrát jsem si řekl, že to musím překonat a vrátit se k tomu, jak jsem psal dřív. Napsat to od srdíčka, udělat commit, git push a hotovo, kašlat na lidi. Je to jen můj blbej blogísek, stejně jako kdysi.

Jenže ani tak nemám čas na psaní. Napsat takový článek, to je prostě 5 a více hodin soustředěné práce. A ještě na to musím mít chuť. No a pak jsem se v jednu chvíli sprchoval a nějak mi naskočilo to téma a najednou mi začaly naskakovat i ty věty, tak jak bych je tam chtěl psát, a články, které odkážu, a aspekty problému, které chci zmínit. A tohle já znám. To je _autorská slina_. To je jako padající hvězda. Buď ji stihnu a můžu si něco přát, nebo zmizí a už ji nikdy neuvidím.

Pokud nezareaguju, když přijde _slina_, tak se článek promění pouze v navždy odloženou Trello kartičku. Jejda, takových je! Pokud tomu chci zabránit, musím v ten okamžik sednout a psát a dopsat to. Takže tentokrát jsem sedl a psal jsem, dopil jsem studené kafe z odpoledne a dokončil jsem to ve tři ráno. Pak jsem šel spát a dopoledne jsem to ještě do oběda ladil a nebyla se mnou řeč, než jsem to publikoval. Před publikací to četla jen manželka.

No [a je to]({filename}/2021-08-28_bez-auta.md). A má to nakonec dost reakcí, na to, jaká to je blbost. Celkem mě to překvapilo, [na Twitteru](https://twitter.com/honzajavorek/status/1431969184745918467) se mi dva dny nezastavily notifikace. 190+ lajků, tyjo, co bych za to dal na tom tweetu o klubu :D

Taky mě ale překvapilo, že se mnou lidi celkem souzní a že na to, jaký ten článek měl dosah, tak se ještě neozvali nějací hejtři. I když tomu možná brání to, že jsem vše formuloval dost subjektivně a nesnažil se ze svých pozorování vyvozovat obecnější závěry. To mi dost pomáhá překonat i ten autorský blok. Moje žitá zkušenost je prostě autentická a i když máte jinou, nemůžete ji příliš kritizovat, že.

Takže celý víkend nedělám nic jiného než článek. Nenapsal jsem poznámky. Nestihl jsem nasázet věci na sociální sítě, což jsem chtěl mít do pondělí hotové. Je pondělí večer a já dopisuju tohle, jsem ve všem ve skluzu. Tož zhruba tak se stane, že člověk napíše dlouhý článek na blog na nějaké téma.


## Analytics

Na [stránku klubu](https://junior.guru/club/) jsem přidal JavaScript od Memberful, aby se objevoval interaktivní formulář pro registraci a placení hned po kliknutí na ceníku, tak jak jsem to měl dřív. Obyčejné odkazy fungují taky, ale tohle má prý lepší konverzi. Bál jsem se performance, ale podle Lighthousu mi i po této změně performance likvidují především Google Analytics.

To mě zase přivedlo na myšlenku podívat se na alternativy. [Matomo](https://matomo.org/pricing/) drahé, provozovat sám nechci. [Fathom](https://usefathom.com/) nemá API, takže vypadl hned. [Plausible](https://plausible.io/) i [Simple Analytics](https://simpleanalytics.com/) mají všechno. No a to je problém. Jak si má člověk vybrat? Obojí má API. Obojí je hostované v EU. Obojí si zakládá na _privacy_. Plausible má [hezkou dokumentaci](https://plausible.io/docs/). Simple Analytics má [neméně hezkou dokumentaci](https://docs.simpleanalytics.com/). Plausible má [zveřejněný dashboard](https://plausible.io/plausible.io), na kterém si můžu jejich produkt prohlédnout a vyzkoušet. Simple Analytics má [taky takový dashboard](https://simpleanalytics.com/simpleanalytics.com). Plausible má na GitHubu [nějakou roadmapu](https://github.com/plausible/analytics/projects/1). Simple Analytics mají [nějakou roadmapu](https://github.com/orgs/simpleanalytics/projects/1) taky.

Našel jsem [jediné srovnání](https://dev.to/hmhrex/a-comparison-of-the-top-3-privacy-focused-analytics-platforms-209m), ale je dva roky staré a tudíž vzhledem k překotnému vývoji těchto produktů poměrně dost neaktuální. Tak jsem se pak už naštval a po dlouhém mžourání [jsem jim to hodil na hlavu](https://twitter.com/honzajavorek/status/1430527744023179268) na Twitteru. Rozdíly budiž nějak zmíněny v diskuzi pod tweetem, minimálně SA mi přišlo jako mnohem živější v diskutování a ve snaze mě získat jako zákazníka. Každopádně ještě jsem to nerozsekl, odkládám zatím opět na neurčito.


## ToC a příprava nové příručky

Jako další prioritu jsem si vytyčil oživení příručky a překlopení do nového designu. K tomu jsem ale potřeboval ToC. Myslel jsem si, že si ji natrénuji na [stránce s FAQ](https://junior.guru/faq/), ale nakonec jsem tam hodil jen obyčejné seznamy.

Příručku jsem si začal připravovat [tady vedle](https://junior.guru/handbook/). Jelikož jsem ToC dělal v historii JG už asi popáté, měl jsem už poměrně jasnou představu, co od toho chci a jak technicky (ne)komplikované to má být. Po jednom dni jsem tedy měl ToC hotovou a jsem s ní celkem spokojený. Ještě by šla vylepšovat, třeba ukazovat aktuální nadpis při scrollování, ale to si nechám na jindy. Kdo jste na mobilu, tak tam se ToC jen složí pod článek, pro tu pravou krásu si to musíte otevřít na počítači. Uvidím, jestli to bude stačit takhle, nebo mi budou lidi psát, že by chtěli lepší navigaci.

Do budoucna na tento design překlopím všechny 4 stránky, které už teď souhrnně nazývám příručka: [Motivace](https://junior.guru/motivation/), [Základy](https://junior.guru/learn/), [První praxe](https://junior.guru/practice/) a [Hledání práce](https://junior.guru/candidate-handbook/). Příručka ale dostane ještě i úvodní rozcestník. Ten by měl vypadat podobně „marketingově“ jako [stránka klubu](https://junior.guru/club/), měl by vysvětlit obsah příručky atd., ale to si možná nechám až na jindy. První verze rozcestníku bude asi jen účelová, jednoduchá. I tak budu muset ještě nastylovat dost komponent, než budu moci překlopit stávající obsahové stránky. Dalším krokem potom bude přidání log firem na všechny uvedené stránky a následně rozsekání těchto čtyř někdy poměrně dlouhých nudlí na třeba 10 mnohem kratších stránek. To vše bude zahrnovat jejich překlopení z HTML do Markdownu a tedy příjemnější editovatelnost i jinými lidmi, než jsem já.


## Další poznámky

- Z předešlých poznámek mohlo vyplynout, že si dítě užíváme zcela bezstarostně, tak bych tady pouze chtěl zmínit, že dcera opravdu nejspíš je jedním z těch klidnějších dětí, aspoň podle příběhů jiných lidí, ale to neznamená, že jsme si nejistí ohledně úplně všeho, že se nehroutíme, nejsme ztracený, že stále neřešíme, jestli neděláme něco blbě, že nejsou všude hovna zatímco všichni brečí a já mám přitom v ruce nahé počůrané dítě, nebo že někdy nejdem spát ve 3 a jindy zase nevstáváme ve 4, a tak. Jsme běžní smrtelníci, jo? Ale snažíme se všechno dělat v pohodovým tempu, což pomáhá. A jsme na to pořád dva, což pomáhá fakt dost, všem třem, fyzicky i psychicky.
- Kamarád mi napsal, že se tenké písmo v novém designu nedá číst na Windows. To mě naštvalo, ne protože se mi to líbí tak, jak to je, i když to je taky pravda, ale hlavně proto, že to je zcela výchozí věc v Bootstrapu. Tu by podle mě měli mít odladěnou oni, ne abych si to musel pro různé operační systémy ladit sám. Takže jsem na to [založil issue](https://github.com/twbs/bootstrap/issues/34813). Zatím ticho.
- Jedna nová členka si stěžovala, že jí nechodí maily z Memberful. To je problém, protože to znamená, že se vůbec nepřihlásí. Promptně jsem napsal na podporu Memberful, tam mi řekli, že vše došlo. Tak jsem zkusil ještě podporu Seznamu. Moc jsem od toho nečekal a při nekonečném čekání na připojení člověka do chatu jsem už ztrácel naději, ale potom to bylo vlastně hodně dobré. Vysvětlil jsem problém, na druhé straně nápomocný profík, vše jsme vyřešili. E-maily byly ve spamu, takže jsem člence napsal, ať to ještě jednou překontroluje (a byly tam), ale hlavně se technici Seznamu podivovali, že takové transakční maily padají do spamu a údajně udělali něco, co tomu napříště zabrání. Takže super, snad navždy vyřešeno!
- Volali jsme si s [Danem](https://coreskill.tech/) snad dvě hodiny a probírali CSS na JG a novinky v Python komunitě.
- Občas scrapery nabídek práce narazí na nějaké chyby. To nebyl problém, problém byl, že se to nakešovalo a pak ty chyby řvaly v monitoringu 24 hodin. Až teď mi došlo, že by se to asi kešovat nemělo a tím se to vyřeší. Scrapy na to má naštěstí [nastavení](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html?#httpcache-ignore-http-codes) a když jsem ho přidal, zatím se toto neopakovalo.
- Snažím se vybrat robotický vysavač. Líbí se mi Xiaomi, ale nechápu rozdíl mezi Vacuum Mop Pro a Roborock, na čemž jsem se zasekl. [Věroš](https://twitter.com/verosk) mi poradil, že mám koupit ten levnější a když mě bude štvát, tak ho do 14 dní vrátím a koupím ten dražší. To zní jako dobrá cesta a adekvátní odplata této firmě za neschopnost odprezentovat přehledně rozdíly mezi svými produkty.
- Publikoval jsem zaslanou pracovní nabídku a poslal fakturu na 500 Kč.
- Pomalu zahajuji hovory s korporátem, zda by neprodloužil svou roční náklonnost ke klubu.
- Během 9 dní od 21.8. do 29.8. jsem naběhal 9 km, při procházkách nachodil 26 km. Celkem jsem se hýbal 13 hodin a zdolal při tom 35 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Zvládnout pěkně večerní přednášku v klubu [s Janem Smitkou o databázích](https://junior.guru/events/#planned), kterou jsem vůbec nezvládl zpropagovat na sociálních sítích a která je už v úterý :(
2. Naplánovat statusy na sociální sítě, už mám zase prázdnou frontu.
3. Nic neprogramovat a dohnat všechny malinké úkoly ve frontě, které jsem delší dobu hrnul před sebou.

A, ehm, vymyslet ten systém, při kterém zvládám zároveň pečovat o dítě a pracovat. Tahle věta tu možná bude ještě dlouho :D


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Švédové poprvé dodali „zelenou ocel“. Vznikla bez užití uhlí](https://getpocket.com/redirect?&url=https%3A%2F%2Fct24.ceskatelevize.cz%2Fveda%2F3356954-svedove-poprve-dodali-zelenou-ocel-vznikla-bez-uziti-uhli&h=ec074be738567e3a47a130fe9593bed36e838a204752393cd5c28fba9cd7e221)<br>Meanwhile in Sweden…
- [Čeká nás kruté procitnutí ze žvástu „Ani jednoho uprchlíka!"](https://getpocket.com/redirect?&url=https%3A%2F%2Fnazory.aktualne.cz%2Fkomentare%2Fcesko-bez-imigracni-politiky-krute-procitnuti-ze-zvastu-ani%2Fr%7E419e7786ff6211eb8a900cc47ab5f122%2F&h=7cdc797ff275d8358b28b8f8670ca629469849c082fbe915525907a24c96af7b)<br>„Jsme zemí, která není schopna snižovat nelegální pobyty, nemá dobře nastavená pravidla pro ekonomickou migraci a neumí reagovat na světové krize - pomáhat těm, kteří to nutně potřebují.“
- [Jedna jízdenka pro celou veřejnou dopravu. Rakousko ji spustí 26. října](https://getpocket.com/redirect?&url=https%3A%2F%2Fzdopravy.cz%2Fjedna-jizdenka-pro-celou-verejnou-dopravu-rakousko-ji-spusti-26-rijna-89331%2F&h=4e11d1cb05b30a5179a4a965ebb9351cec255e5f6afed843180177d2c2a20678)<br>Jsem zvědavý na výsledky. Zajímavý nápad.
- [Big tech companies are at war with employees over remote work](https://getpocket.com/redirect?&url=https%3A%2F%2Farstechnica.com%2Fgadgets%2F2021%2F08%2Fvaccines-reopenings-and-worker-revolts-big-techs-contentious-return-to-the-office%2F%3Futm_social-type%3Downed&h=642b339ae35d7d17627a3d65938a5975895d708ce8cce9e5c0ce6a347b1fd868)<br>O tom, jak se firmám v Silicon Valley nechce pokračovat v práci na dálku, ačkoliv jejich zaměstnancům nedává žádný smysl jezdit každý den do kanclu a bydlet v předražené Bay Area.
- [What It Means When Climate Scientists Say They're Certain](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.bloomberg.com%2Fnews%2Farticles%2F2021-08-10%2Fwhat-it-means-that-ipcc-scientists-are-certain%3Fsrnd%3Dgreen&h=47a30844ace25b618512a23b9703fbe57327cc17cf9fecc3ef1a92610fc74506)<br>Článek se zabývá vědeckou metodou, prací vědců s pravděpodobností a jistotou a vysvětluje, jak je možné, že až teď vědci prohlásili, že lidstvo způsobuje oteplování planety „zcela bez pochyb“.
- [How the US made affordable homes illegal](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D0Flsg_mzG-M&h=6041f3a6f4e1bc6daa7fd2f722db29a4b2baf99c23efcd49fcbbd907f2ba359f)<br>V krátkém videu pěkně a názorně vysvětleno, proč je v USA a především v okolí SF realitní krize. U nás to blokuje minimální počet parkovacích míst na jednotku, nutné proslunění bytů a regulace výškové výstavby. Kvůli tomu se všichni rozlézají do polí a ve městech máme novodobé paneláky místo ulic. Nedostatek bytů šponuje ceny a nové byty si běžný člověk už dovolit nemůže.
- [Miroslav Suchý (OpenStreetMap): Bílých míst na mapách je překvapivě pořád strašně moc](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.lupa.cz%2Fclanky%2Fmiroslav-suchy-openstreetmap-bilych-mist-na-mapach-je-prekvapive-porad-strasne-moc%2F&h=9e955caee930b9e46ccb2e874d650df18cb4e9f2fcd977fa84394a922eee93c4)<br>Super rozhovor. Místo Pokemon Go můžete z mobilu jednoduše mapovat své okolí.
- [Glosa: Přechod u Muzea, největší vymoženost po roce 1989](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Fglosa-prechod-u-muzea-nejvetsi-vymozenost-po-roce-1989-172758&h=f1c2f88e6a8ade4fc9e213838657f2b1c18471ed8bf838be1f104bb2f3cd037f)<br>1888: V Praze začalo fungovat první elektrické osvětlení! 2021: Chodci smí chodit přes ulici!
- [Stromy jsou jako klimatizace, v ulicích ale často chybí. Co městu brání v jejich výsadbě?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.campuj.online%2Fblog%2Fjak-funguje-mesto-stromy&h=2b50b0f92891cbd8711f4f4b5da2b11e00beab8019c48d87865317c0162ac119)<br>Moc pěkný článek o stromech ve městě, o jejich hodnotě, o komplikacích s jejich výsadbou, o tom jak mohou lézt do sítí a o nejstarších stromech na území Prahy.
- [Who Owns My Name?](https://getpocket.com/redirect?&url=https%3A%2F%2Famandamarieknox.medium.com%2Fwho-owns-my-name-93561f83e502&h=3cb7b0d138bec0d8e7698cea63ac7c202b7698526d2362d24b0fec84c6422cbf)<br>Jaké to je, když příběh vašeho života nepatří vám a všem je to jedno.
- [Jak jsem se stal vývojářem](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.apitree.cz%2Fblog%2Fjak-jsem-se-stal-vyvojarem&h=8ede957d015a38d2490619d45cd351c17eeb806dcc60de532c72880178b7a2c2)<br>Moc hezká success story!
- [The Semiconductor Heist Of The Century | Arm China Has Gone Completely Rogue, Operating As An Independent Company With Inhouse IP/R&D](https://getpocket.com/redirect?&url=https%3A%2F%2Fsemianalysis.substack.com%2Fp%2Fthe-semiconductor-heist-of-the-century&h=b641f823d65594360e38e1df796645ad726ed88b4de2a9e8434c3caf2dea4838)<br>Arm si v Číně založil pobočku. Pobočka si vzala IP, tzn. veškeré know how a intellectual property, vyhlásila nezávislost a pokračuje s vývojem úplně vlastních čipů. Tududum tum.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
