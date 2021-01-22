Title: Týdenní poznámky #34: Εὕρηκα! Členství vyřešeno
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (18.1. — 22.1.) a tak [stejně jako minule]({filename}/2021-01-15_tydenni-poznamky-33-poptavky-a-placeni.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

_Εὕρηκα_ je takové to Archimedovo zvolání. Nechtěl jsem to tu mít latinkou, aby si lidi nemysleli, že mám něco společného s vyhledávačem zboží. Už tak jsem dostal za uši, když jsem měl v nadpisu HN a nebyly to HackerNews, ale Hospodářky. Musel jsem se kvůli tomu pak stát slavným nejen na Hospodářkách, ale i HackerNews.

Tento týden se nesl v duchu rozklíčování **technického a procesního řešení nákupu členství**. Paralelně se mnou mi daňař odpovídal na dotazy ohledně daní a právnička pracovala na mých obchodních podmínkách.

## Členství

V minulých poznámkách jsem skončil tím, že jsem v pasti a neumím vyřešit propojení Stripe a Discord. Nový týden jsem nastartoval s tím, že si musím dát nějaké konkrétní kroky, přes které se doberu výsledku:

- Poptat se na všech možných místech, zda to už někdo neřešil nebo neví, jak to řešit.
- Ještě jednou projít hotová řešení a spočítat _pricing_. Co kdyby to nakonec vycházelo nějak přijatelně?

Výsledkem prvního bodu byly dotazy na [supportu Discordu](https://support.discord.com/hc/en-us/community/posts/1500000208241-How-can-I-say-which-Discord-member-came-through-which-invite-), [na Stack Overflow](https://stackoverflow.com/questions/65810723/how-can-i-say-which-discord-member-came-through-which-invite), [na Twitteru](https://twitter.com/honzajavorek/status/1351888926517186560). Také jsem intenzivně hledal a přece jenom jsem nakonec něco našel. Pokud bych se nakonec rozhodl pro vlastní řešení, zřejmě by mě k němu dovedl [tento článek na Mediu](https://medium.com/@tonite/finding-the-invite-code-a-user-used-to-join-your-discord-server-using-discord-py-5e3734b8f21f) a tato [odpověď na SO](https://stackoverflow.com/questions/65074741/how-can-i-see-which-invite-link-the-newcomer-came-from/65074934#65074934). Jak ale vyplývá z formulace předchozí věty, rozhodl jsem se nakonec vybrat hotové řešení. Zvažoval jsem následující:

- [Memberful](https://memberful.com/) - Koupil je Patreon, skvělý support, spousta funkcí.
- [LaunchPass](https://launchpass.com/) - Malá firma, dobrý support, málo funkcí.
- [Upgrade.Chat](https://upgrade.chat/) - Platící bot, možná trochu něco jiného, než chci. Jakýsi strašně zmatený support přes Discord. Nejmenší marže, ale vyloučil jsem je vlastně celkem brzo.

Dále jsem se díval na:

- [Circle](https://circle.so/) jako na možnou alternativu Discordu a _all-in-one_ řešení. Líbil se mi design, nelíbil se mi ceník a funkce.
- [Auth0](https://auth0.com/) jako na možný stavební blok pro přihlašování,
- [MemberStack](https://www.memberstack.com/) jako alternativu Memberful,
- [MemberSpace](https://www.memberspace.com/) jako další alternativu Memberful.

### Outsourcovat nebo ne?

Stále jsem všechno zvažoval a rozvažoval. Hlavně jsem si nebyl jistý, zda mám opravdu něco takhle outsourcovat. Nakonec mě přesvědčily následující věci:

- Udělal jsem si detailní tabulku pro výpočet předplatných, všech marží atd. Náhled níže. To mě přesvědčilo, že marže hotového řešení se tam vleze a že to pořád dává smysl.
- Všechna hotová řešení jedou přes Stripe, který je _industry standard_ a sám má skvělé API, takže to není úplný _vendor lock-in_.
- Když jsem si četl o nejrůznějších funkcích jednotlivých řešení, pochopil jsem, že tohle si fakt sám programovat nechci. Možná bych dokázal vyrobit jednoduchý skript pro ten základ a něco bych ze začátku ušetřil, ale když jsem viděl, co všechno hlídají, jaké maily posílají, co vše jde nastavit, apod., najednou to nebylo jen "propojení Stripe a Discord", byla to hromada práce, kterou nebudu muset řešit. [Daně](https://memberful.com/help/how-to/collect-taxes/). [Kupóny]().
- Přemýšlel jsem nad tím, jestli chci programovat řešení pro online členství nebo chci budovat komunitu, psát příručku a vylepšovat JG. Jasně mi z toho vyšlo, že tohle prostě není můj _core business_ a můj život bude mnohem šťastnější, když použiju hotovou věc a zaplatím za ni.

Z možných řešení jsem nakonec vybral Memberful. Líbilo se mi, že za nimi stojí společnost, která asi jen tak nezanikne, že dělají přesně to co chci a přesně způsobem, jakým chci. Mají dokumentaci a z jejich webu je vše zřejmé - hlavní výhoda oproti LaunchPass. Mají API, mají funkční a úžasný support (prohodil jsem s nimi asi 10 mailů, než jsem si vše ujasnil). Dokonce mají i drahou variantu s možností [prodávat skupinové členství](https://memberful.com/help/how-to/manage-team-plans/). Zprvu jsem myslel, že ji budu potřebovat, ale nakonec jsem to vymyslel jinak. Vědomí, že mi bude stačit levnější varianta, mě už definitivně přesvědčila.

### Velké počítání

![Velké počítání]({static}/images/pricing-jg.png)
Rozpočítávání cen, marží, nákladů. Mohu měnit čísla v modrých řádcích a vše se přepočítává. Mohu měnit i základní cenu nebo čísla kolem navržených nabídek pro firmy. Ty jsou ve velmi ranném stádiu uvažování.

Když jsem si dělal tabulku, ve které se vše propočítávalo, zkoušel jsem si už rozvrhnout i nabídku pro firmy. Nejdřív jsem myslel, že by byla jedna za zhruba 10 000 Kč, kde by firma mohla pozvat třeba 10 nebo aspoň 8 členů, ale nevycházelo mi to jako moc výhodné. Částky 10 000 Kč ročně se chci ale držet, protože si myslím, že je to psychologická hranice, u které spousta firem mávne rukou a zaplatí ji klidně i jen proto, aby mě podpořili v tom, co dělám. Nakonec jsem zkusil načrtnout spíš dvě nabídky, jednu pro firmy s menším počtem lidí a druhou pro větší. Samozřejmě bude i třetí, pro všechny ostatní, ale ti mi napíšou e-mail a domluvíme se individuálně. Intuitivně jsem to rozdělil tak, že levnější varianta zaplatí za 6 vstupů a dražší za 18, ale pro jistotu jsem nadhodil ankety na [FB](https://www.facebook.com/groups/193575630828729/permalink/1674691469383797/) a [Twitter](https://twitter.com/honzajavorek/status/1351992847105478656), ať to není úplně vycucané z prstu. Prakticky potvrdily mou úvahu.

No ale stejně to je celé zatím jen pro mou tabulku s čísly, takže o nic nejde. V nejbližší době nepočítám s tím, že se budu dělat s ceníkem na webu, prostě mi firmy napíšou na mail a dohodneme se. Taky to může skončit u toho, že bude nějaká fixní sazba za logo mezi členy klubu a pak dynamické "šoupátko", které výslednou cenu prostě vypočítá násobením počtu členů, které chtějí zaplatit. Třeba žádné "přednastavené" balíčky ani nebudou.

### Memberful

Memberful má [pohodlné propojení s Discord](https://memberful.com/help/third-party-integrations/discord/), umí CZK a celkově mi přišel nejlépe připravený pro to, co já potřebuji. Dá se vyzkoušet naživo bez toho, aby za to člověk platil - dokud se nerozhodnu, že to chci překlopit do ostré verze, jede to v testovacím režimu a můžu zkoušet i funkce, které jsou pro placené účty. To jsem dělal snad jeden celý den a vytvořil jsem si kvůli tomu i další testovací Discord server. Administraci a možnosti Memberful jsem dlouho poctivě proklikával. Díky tomu jsem pak i rozklíčoval dilema jak technicky řešit hromadné předplatné pro firmy, které chci dělat na fakturu. Zkoušel jsem různé nápady, např. že by každá firma měla svůj vlastní _plan_, který jinak nepůjde koupit, a jenž bude určovat podmínky předplatného… ale pak jsem na to přišel.

Udělám to přes [kupóny](https://memberful.com/help/how-to/create-a-coupon/)! Objev kupónů a myšlenka, že se s nimi dá řešit skupinové předplatné byl hlavní _εὕρηκα_ moment tohoto týdne a udělal mi velkou radost. Do té doby jsem si připadal na dobré cestě, ale stále zaseknutý. S kupóny najednou vše začalo zase dávat smysl. Firma prostě nakoupí třeba 5 kupónů se 100 % slevou na rok a je to. Ať už je dá svým lidem nebo je někomu podaruje, vše bude fungovat. Akorát si napíšu Python skript, který mi udělá nějaký přehled v Google Sheets tabulce. Mohl by mi třeba i poslat mail, když se bude blížit vypršení doby předplacené fakturou, klidně sám kontaktuji firmu a dořešíme distribuci nové sady kupónů. Pokud firma za někoho platit už dál nebude chtít, tak ten nemusí odejít, může za sebe dál platit individuálně. Právě onen individuální aspekt kupónů a existence individuálních účtů, které firma jen předplatí, se mi na tom hodně líbí. Navíc mohu vytvářet kupóny i s menší než 100% slevou, že, a rozdávat je třeba do nějakých spřízněných komunit :) Ou jé.

Abych nedopadl jak s propojením Stripe/Discord, rozhodl jsem se ještě opravdu vyzkoušet, že API od Memberful je použitelné a mohu přes něj udělat, co potřebuji. V testovacím režimu to naštěstí šlo. Mají GraphQL API, což jsou pro mě pořád ještě trochu vody, ve kterých tápu, ale s pomocí [gql](https://github.com/graphql-python/gql/) jsem docela rychle splácal něco, co mi vyhodilo přesně ta data, která bych při integraci s mými Google Sheets potřeboval. A to už byl pátek, takže dál jsem už nic nedělal a mohu jít dnes spát s tím, že velké dilema je vyřešeno.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Having a surprisingly decent experience with <a href="https://t.co/AGnJTBXgmJ">https://t.co/AGnJTBXgmJ</a> Nice!<br><br>I remember trying to consume <a href="https://twitter.com/hashtag/GraphQL?src=hash&amp;ref_src=twsrc%5Etfw">#GraphQL</a> from a server-side <a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a> script back in 2018. Huge drag! The tooling wasn&#39;t ready and many things were DIY. Now I can get a response on 4 lines of code.</p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/status/1352562694797275137?ref_src=twsrc%5Etfw">January 22, 2021</a></blockquote>

Tedy jsem se rozhodl vykopnout se z Patreonu dveřmi (časem chci zrušit [svůj Patreon](https://www.patreon.com/honzajavorek) a nahradit jej právě členstvím v klubu) a přijít k němu oknem :D No, hlavně jsem rád, že jsem si to všechno mohl osahat a vyzkoušel jsem si i to API, takže za to mohu s klidným svědomím zaplatit, prohlásit přijímání členů a placení za vyřešené a posunout se na lepší věci. Na Stripe/Discord jsem se naučil, že je asi vždy lepší nejdřív si ověřit, zda předpoklady sedí i v realitě. Nestačí jen fakt, že existuje API, tak vše určitě nějak půjde :)) A taky jsem pochopil, že to není práce pro jeden skript. Že nejde jen o propojení Stripe/Discord, ale že kdybych se do toho pustil sám, programoval bych to a opravoval na tom chyby tak zhruba do konce života.

Jinak další super věc na Memberful je ta, že se tam moji členové mohou přihlásit a je tam celý _billing portal_, kde mohou změnit předplatné, zrušit, změnit kartu, atd. To by uměl i Stripe sám o sobě, ale jak jsem psal minule, tam bych musel já implementovat to přihlašování. A navíc, pokud bych v budoucnu chtěl vyrobit něco jako knížku nebo video pouze pro členy, mohu to nahrát do Memberful a po přihlášení do svého účtu na to budou mít všichni členové odkaz ke stažení apod. Teď to neplánuji, ale do budoucna se to hodit může a já k tomu budu mít už infrastrukturu bez práce.

### MailChimp

Všiml jsem si, že Memberful má i pěknou integraci s MailChimpem, ale po pár dotazech na jejich support jsem se rozhodl, že ji zatím využívat nebudu. Můj newsletter vznikl už dříve a pro jiný účel. Spojovat bych to teď nechtěl, navíc si nejsem jistý, jak moc legálně to mají uděláno vzhledem k českým pravidlům - např. by se mi líbilo, kdyby tam bylo při registraci nezaškrtnuté zaškrtávátko, kde by si člověk mohl zvolit, že ode mě chce dostávat e-maily, ale to oni tak úplně neumí. Je to až moc automatické :) Nechávám na jindy nebo na nikdy.


## Daně

Svého daňaře jsem se vyptal na spoustu věcí, které mi vrtaly hlavou. V jedné z odpovědí mi napsal následující:

> Jde ale o tak specifickou situaci pro někoho kdo není plátce DPH, že jsem se s něčím takovým ještě nesetkal.

Moje první reakce byla: _Challenge accepted!_

Pokud by někoho zajímalo, jestli musím automaticky vydávat doklady, tak podle zákona o ochraně spotřebitele je povinnost vystavit doklad o poskytnutí služby, pokud o to zákazník požádá. Stejná povinnost je i v živnostenském zákoně.

Pak jsem se ptal, jak to je, když může koncový zákazník samoobslužně nakupovat na mém webu kartou a já nejsem plátce DPH. Pokud přijde někdo ze Slovenska a nakoupí, velmi to neovlivním. Stanu se pak automaticky identifikovanou osobou nebo plátcem DPH? V podstatě jsem rozlišil čtyři situace:

1. Koncový zákazník z ČR, zaplatí kartou na webu, jednou za měsíc/za rok se mu strhne částka.
2. Firma/podnikatel z ČR, má IČO, domluvíme se přes e-mail a já pošlu fakturu z [Fakturoidu](https://www.fakturoid.cz/) a třeba za rok pošlu další.
3. Koncový zákazník ze SR nebo odkudkoliv jinud z celého světa. Platební brána bude na webu a kdo zaplatí, dostane členství. Logicky nemohu nijak omezit nebo ověřit odkud člověk je. Protože je má služba česky, mohu se domnívat, že ze zahraničních koncových zákazníků to bude zajímat hlavně Slováky, ale reálně to může být kdokoliv.
4. Firma/podnikatel mimo ČR. Ti nemohou nakupovat přes platební bránu, museli by se se mnou domluvit, takže jim snadno mohu říct, že službu neposkytuji mimo ČR, pokud se nechci stát ID osobou/plátcem DPH, a z obchodu nic nebude.

Případ 2. dělám odjakživa. Případ 1. je pro mě nový, takže nevím, jaké má náležitosti, ale nebojím se ho. Případ 4. mohu snadno ručně vyloučit, takže se ho taky nebojím. Co mě straší je případ 3., protože je de facto mimo mou kontrolu. Pokud bych jej měl mít pod kontrolou, musel bych nějak v platební bráně zamezit lidem platit, pokud nejsou z ČR, ale to mi moc nedává smysl.

Podle všeho, pokud nebudou prodeje do EU běžným smrtelníkům vyšší než 10 000 EUR/kalendářní rok, tak údajně DPH řešit nemusím. Po překročení bych se nejspíš stal identifikovanou osobou a musel bych se přihlásit do MOSS. Než budu mít vysoké výdělky, nemuselo by mě ani zajímat, odkud ti lidé jsou, ale pro jistotu je lepší si to někde evidovat, abych případně mohl prokázat, zda ty vysoké výdělky ze zahraničí (ne)mám. EU do směrnice k DPH zařadilo i demonstrativní výčet důkazů, které můžu použít k prokázání, ze kterého státu lidi jsou:

- Fakturační adresu příjemce,
- adresu internetového protokolu (IP) zařízení používaného příjemcem nebo jakýkoli způsob geolokalizace,
- bankovní údaje, například místo, kde je veden bankovní účet používaný k placení nebo fakturační adresa příjemce, již má uvedená banka k dispozici,
- mezinárodní směrový kód země (MCC) mezinárodní identifikace mobilního účastníka (IMSI) uložený na SIM kartě, kterou příjemce používá,
- místo pevné linky příjemce, jejímž prostřednictvím je mu služba poskytována,
- jiné informace důležité z obchodního hlediska.

Takže stačí i celkem vágní informace jako IP adresa. Super :) Pro mě je to důležité hlavně proto, že se teď ještě nechci stát plátcem DPH a také proto, že chci, aby formulář pro placení musel obsahovat co nejméně políček. Čím víc políček k vyplnění, tím menší šance, že formulář někdo dokončí a opravdu zaplatí.


## Další poznámky

- V nativním macOS terminálu, který teď zkouším používat místo iTerm2, mi zatím chyběla jediná věc, a to skákání šipkama po slovech se zmáčknutým altem/option. Zjistil jsem ale, že to jde [zapnout jediným zaškrtávátkem](https://osxdaily.com/2013/02/01/use-option-as-meta-key-in-mac-os-x-terminal/).
- Poděkoval jsem e-mailem někomu, kdo mi už vloni v létě radil něco v tom smyslu, že vydělat by se v mém případě dalo nejlépe asi na nějakém placeném členství apod. věcech. Trvalo mi jen tři čtvrtě roku na to přijít sám.
- Člověk, který prosazoval sponzorování JG v jedné firmě, měl teď prezentaci o tom, jak se jim ta investice vyplatila. Trochu jsem mu pomáhal s přípravou. Vypadá to, že výsledky dobrý! 40 % kandidátů byly ženy, 2 lidi přijali.
- Ozvala se korporace, že jsem jejich dodavatel a mám jim ihned poslat spoustu údajů. Údaje jsem dodal.
- Jako OSVČ jsem od ledna zvýšil pravidelnou zálohu na zdravotní pojištění.
- Spadl mi scraper na [WWR](https://weworkremotely.com/), protože měli v JSONu text, jehož součástí byla i sekvence znaků pro tzv. _shrug_, tedy krčení ramen, a nebylo to nijak ošetřeno (zpětné lomítko). Opravil jsem to tak, že když se něco takového stane, holt se nabídka práce přeskočí ¯\\\_(ツ)_/¯
- Měl jsem hovor s právničkou, kde jsme dolaďovali obchodní podmínky. To, že jsem vybral Memberful, nám zodpovědělo spoustu nevyjasněných otázek, takže další palec nahoru pro hotové řešení.

### Pyvec

- Upgrade knihoven na různých Pyvec projektech (přes Dependabot).
- Spadla hlavní větev na webu Pyvce, a to proto, že Twitter už definitivně odebral možnost přes jednoduché URL získat avatar uživatele. Musel jsem to celé odstranit a nyní mohou [obrázky členů Pyvce](https://pyvec.org/#members) pocházet už jen z Gravataru nebo GitHubu.
- Měli jsme pravidelnou schůzi výboru Pyvce. Pár věcí jsme vyřešili. Přijali jsme do spolku nového člena.

### Redis Collections

Kdysi dávno jsem napsal knihovnu [redis-collections](https://pypi.org/project/redis-collections/). Byl to můj první balíček na PyPI, napsal jsem k tomu svou první dokumentaci na ReadTheDocs, prostě můj první opravdový Open Source. Koukám se, že to bylo v lednu 2013, tedy před osmi lety. Knihovně jsem se věnoval, ale pak jsem změnil práci a už jsem ji nadále sám nepotřeboval, takže trochu umírala na nezájem. V roce 2016 se ale objevil nějaký [Bo Bayles](https://github.com/bbayles) z druhého konce zeměkoule a navrhl, že by se o to dál staral. Postupně jsme si předali žezlo a od té doby na tom zahradničí on.

Nedávno se ozval s tím, že by chtěl vyhodit Travis CI a vyměnit jej za GitHub Actions, ale nemá všechna potřebná oprávnění. Proto jsem se na to tento týden mkrnul:

- Přidal jsem současného správce jako spoluvlastníka balíčku na PyPI
- Vytvořil jsem organizaci na GitHubu: [github.com/redis-collections](https://github.com/redis-collections/)
- Nastavil jsem nás oba jako vlastníky
- Přesunul jsem repozitář pod novou organizaci

Pak jsem si říkal, že by byla škoda mít na organizaci výchozí náhodný obrázek, že by to chtělo nějaké logo. Takže jsem stáhl SVG logo Redisu, otevřel v Inkscape, dal _ungroup_, smazal text a různé detaily a přes červené destičky napsal v Arial Black iniciály projektu, RC. Zabralo to 5 minut. Dalších 15 minut zabralo správně nastavit rozměry dokumentu a vše vycentrovat a exportovat správně do PNG. I když jsem mu jasně řekl, že to byl jen pokus a klidně to můžeme zahodit, tak Bo napsal, že logo je nádherné a bude ho používat. Aby mi neleželo jen někde na disku, vytvořil jsem pro něj repo [logo](https://github.com/redis-collections/logo).

Ano, asi není úplně správné vzít něčí logo a derivovat z něj svoje. Dnes už třeba vím i to, že není správné ani pojmenovávat věci slovem "Redis", když nemám s Redisem nic společného, protože tím nejspíš porušuji jejich ochrannou známku. U nových projektů bych to už vymyslel jinak, ale tady mi přišlo, že logo vytvořené z loga Redisu bude konzistentní s názvem knihovny, který je vytvořený z názvu Redisu, a že to doteď nikomu nevadilo, tak snad OK. Pokud mi někdo z Redisu napíše, že to není OK, samozřejmě to odstraním nebo knihovnu přejmenujeme. Zatím jsme aspoň přidali [tuhle větu do README](https://github.com/redis-collections/redis-collections/commit/4dc6b6bfd57928f3d3ceb0ece6880148f900b8d4).

Když už jsem byl u takových detailů, po svém angažmá v Oracle jsem se [podíval i na licenci a věci kolem toho](https://github.com/redis-collections/redis-collections/pull/136).

### Vylepšení skriptu na týdenní poznámky

Ve volné chvilce jsem se podíval na skript [weeknotes.py](https://github.com/honzajavorek/honzajavorek.cz/blob/master/weeknotes.py), kterým generuji šablonu pro každé nové týdenní poznámky:

- Opravil jsem kód, který chybně vytvářel odkaz na minulé poznámky v prvním odstavci.
- Přidal jsem novou sekci "Co plánuji" (k vidění o kousek níž), která by mi měla pomáhat určovat si trochu priority na další týden a zpětně sledovat, jak se mi tyto plány drží dodržovat. Cílem není vyčerpávající seznam, ale napsat si tři nejdůležitější věci, které bych fakt měl udělat.

Napadlo mě, že by v poznámkách mohla být vždy jedna věta o tom, kolik jsem měl za poslední týden pohybu. Vám by to ukázalo, jak je každá odrážka v poznámkách vykoupená tím, že se nehnu od počítače. Mě by to třeba pomohlo víc se motivovat vyrazit ven na procházky, běhat, projet se na kole. Zjistil jsem ale, že [Strava](https://www.strava.com/) má API přístupné jen přes OAuth2, je tedy nutná interakce uživatele, abych mohl stáhnout data o svých aktivitách. Taková API úplně nenávidím. Jak to nemá API token, nejde to pořádně použít ze skriptu a nebo jde, ale je to hrozná otrava.

Zkusil jsem pak ještě přístup "když to nemá použitelné API, třeba se to dá scrapovat" a na pár řádcích se mi opravdu povedlo napsat Python skript, který se přes mé jméno a heslo přihlásil do Stravy a viděl moje poslední aktivity. Pak bych ale musel nějak přes CSS nebo XPath vysekávat jednotlivé kousky jako kolik km nebo datum a to už jsem si řekl, že se mi kvůli jedné větě v poznámkách dělat momentálně nechce.

Možná jsem si měl jít radši zaběhat?


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Propojit Memberful s webem junior.guru
2. Mít hotové obchodní podmínky
3. Pověnovat se [Visualbooku](https://juniorguru.visualbook.pro/), který jsem dostal k Vánocům od [Jirky](https://www.jirichlebus.cz/)

Myslím, že by se mi mohlo povést klub na přelomu ledna a února už spustit pro veřejnost.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Jan Lenart: Overtourismus v české přírodě. A co dál?](https://getpocket.com/redirect?&url=https%3A%2F%2Fekolist.cz%2Fcz%2Fpublicistika%2Fnazory-a-komentare%2Fjann-lenart-overtourismus-v-ceske-prirode.a-co-dal&h=b7bf181ddbb18f40c08f9dce090c4dc41a0a1e4bc4e00184ba1c5152977fea2a)<br>Bohužel bez vyhlídka na řešení, ale průlet problémy to je “hezký”. Chybí mi zmínka o elektrokolech nebo Vltavských vodácích.
- [Nový registr očkování dokazuje, že Andrej Babiš Čechy nenávidí](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F01%2Fnovy-registr-ockovani-dokazuje-ze-andrej-babis-cechy-nenavidi%2F&h=81f2a1b2630be9d713576dd2076267187b01bfc77bec05ae8f7488b547c55bee)<br>Nejhorší je, že lidi, kteří se nemotají kolem IT, si budou myslet, že takhle vypadá veškeré IT a jinak to ani udělat nejde. Že když je něco přes internet, je to prostě hnusné, nefunkční, nepoužitelné.
- [Rezervační systém je samozřejmě průšvih, ale nemalujme si příliš růžové alternativy](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.info.cz%2Fnazory%2Frezervacni-system-je-samozrejme-prusvih-ale-nemalujme-si-prilis-ruzove-alternativy&h=1986ebffa9584f0dcf6084461e1730dba9b92aca8e91288cecda0ed6aefe5f49)<br>Změna vlády by nejspíš neměla velký vliv na to, jak se (ne)povedl očkovací systém. Rozjímejme.
- [Studio N: Pomyslel jsem si, že už skoro všem hráblo, říká historik Putna o kauze údajného Ježíšova hřebu](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikn.cz%2F536688%2Fstudio-n-spise-nez-svaty-hrebik-potrebujeme-kriticky-rozum%2F&h=c057862d09bb0672912f98860c9c0c6742fc93c66fa893c13e566a4e7d797c71)<br>U tohoto jsem se teda dost pobavil. Ani jsem neočekával takovou pecku, zaujal mě titulek, říkám si pustím si to k domácím pracem, no a rozhovor paráda teda.
- [The Thucydides Trap: Are the U.S. and China Headed for War?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.theatlantic.com%2Finternational%2Farchive%2F2015%2F09%2Funited-states-china-war-thucydides-trap%2F406756%2F&h=82b5bfed34a00f632a5adff522dbb8a303d7aad1aa8fc2ee34d8b7ca093a4583)<br>Čína velmi brzy ohrozí USA jako světového lídra a bude chtít změnit světový pořádek. Pokud USA bude chtít zachovat status quo, čeká nás podle historických zvyklostí válka. Jen 4x se tak nestalo, a to jen díky velkému úsilí obou stran.
- [Why Tailwind Isn't for Me](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2FC65nwmCXO2%3Fssr%3Dtrue&h=7816846931234e041dc7040c0e36e32810d74db22f36b6f9b3c8acdffe441e6c)<br>Zajímavá kritika Tailwindu, už jen kvůli ukázkám toho, co všechno je dnes už přímo v HTML a CSS možné.
- [Building on Slack Saved Our Startup](https://getpocket.com/redirect?&url=https%3A%2F%2Fthinkgrowth.org%2Fbuilding-on-slack-saved-our-startup-94953fdaf27a&h=f3ba292aaf48ebfe4cb51dc3cc51f40996096fb542f5b60f2b0a63303b43ce09)<br>Zajímavý rozbor toho, jak lze stavět produkt na cizí platformě a vyhnout se tomu, aby byl v zajetí platormy a aby umřel s prvním jejím uprdnutím.
- [Zázrak na chanuku. K usmíření Maroka s Izraelem pomohl král, Trump a historie](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fkaleidoskop%2F423653-zazrak-na-chanuku-k-usmireni-maroka-s-izraelem-pomohl-kral-trump-a-historie&h=29e2f9c479f907f2c80427fecd529bbafe55d158ca0e9c2f07c94108be69dd6d)<br>Co má společného Maroko a Izrael
- [Why do mirrors flip horizontally (but not vertically)?](https://getpocket.com/redirect?&url=https%3A%2F%2Fyoutu.be%2FvBpxhfBlVLU&h=e374fcc92f04f0b2d505a814e49821ef065d133c8b588ba8f8350ccf7339c5e8)
- [V případu otravy Bečvy policie vyšetřuje, kdo dal Deníku Referendum informace](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikreferendum.cz%2Fclanek%2F32203-v-pripadu-otravy-becvy-policie-vysetruje-kdo-dal-deniku-referendum-informace&h=b7a9195ee4adc034cf9a58803a7ce577c960d6a203c3ff93ddbab7655c55b2f2)<br>Bečva houstne. Je PČR nezávislá? Deník Referendum spekuluje, že ne, a posílá věc na GIBS.
- [ARAGORN vs. Toxic Masculinity](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dpv_KAnY5XNQ%26feature%3Dyoutu.be&h=827bacb1609e924734cfff404f2e5d6e621033c763e35be4db504bb8a027d808)<br>Proč je Aragon tak skvělý hrdina? Netrpí toxickou maskulinitou. Skvělé video, na kterém by mohl toxickou maskulinitu pochopit každý. "You can decapitate orcs and write poetry. They're not mutually exclusive."

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
