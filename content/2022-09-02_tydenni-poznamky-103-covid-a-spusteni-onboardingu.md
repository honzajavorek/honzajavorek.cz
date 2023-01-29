Title: Týdenní poznámky #103: Covid a spuštění onboardingu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl zase nějaký ten týden (20.8. — 2.9.) a tak [stejně jako minule]({filename}2022-08-19_tydenni-poznamky-102-novy-cenik.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Cyklovýlet a covid

Jednou ročně jezdím se dvěma kamarády na víkendovou cykloexpedici. Předloni nám to docela propršelo a vloni to nevyšlo, částečně kvůli tomu, že jsme měli mimino. Letos se to tedy mělo konat po dvou letech a moc jsem se na to těšil.

V den odjezdu jsem ráno zaznamenal, že mi není úplně dobře. Pozoroval jsem to, ale nechal jsem tomu volný průběh, protože jsem nechtěl celou akci rušit kvůli bolení hlavy, když jsem se na to tak těšil. Odšlapal jsem pak 128 km na paralenech a během toho nakazil několik lidí covidem. Nejsem na to vůbec hrdý a v mnoha ohledech je to do budoucna velké poučení. K tomu všemu nám to zase propršelo, ještě víc než minule. Poslední den jsme museli úplně zrušit a odjet vlakem domů.

Covid jsem si nejspíš odnesl z [Pyva](https://pyvo.cz/praha-pyvo/) několik dní předtím, ale důkazy pro to žádné nemám. Doma jsme lehli celá rodina, včetně děcka. Za normálních okolností bychom to prostě prospali jako chřipku, ale nemít sílu a muset se u toho starat o malé děcko, které je samo taky nemocné a brečí celý den, to nebylo vůbec nic příjemného a přivedlo mě to na pokraj zhroucení nejen fyzického, ale i psychického. Teď už je covid naštěstí pryč a začínáme se vracet do normálního života.


## Dohánění zameškaného

Jako první jsem procházel klub, maily, a tak dále. Covid volně navázal na mou krátkou dovolenou (tedy spíš „dovolenou“) a během covidu jsem taky neměl sílu číst moc věcí, takže se všeho nahromadilo milion a četl jsem to pak dva dny. Zase jsem to využil k tomu, abych odpověděl na dlouho odkládané maily tetám a vzdáleným strejdům.

V klubu jsem mrknul na jedno CVčko, uvítal všechny nové lidi, podíval jsem se na jedno stipendium. U stipendia jsem oznámil Mews, že už mi nebudou proplácet členství v klubu pro ty, kdo stipendium dostanou. V novém režimu ceníku už to nedává moc smysl takto řešit. Budu to prostě udělovat já a oni ať proplácí jen ty věci navíc, které k tomu případně přidáme.

Reagoval jsem na mail ohledně partnerství s [ajtyvit.sk](https://ajtyvit.sk/) a [profesia.sk](https://www.profesia.sk/), které pomaličku pečeme. Odpověděl jsem jedné firmě na poptávku po výkonnosti [junior.guru/jobs](https://junior.guru/jobs/). Poslal jsem jim veřejné statistiky a nějak jsem to okecal. Zatím bez odpovědí.


## Prokrastinace

Prioritně jsem měl pracovat na dokončení onboardingu, ale to by bylo příliš zodpovědné, takže jsem se pustil do jiných věcí. Nejdřív jsem opravil chybu v botovi na Discordu, který neuměl při vítání nových členů v kanálu #ahoj přeskakovat starší a už archivovaná vlákna.

Pak jsem se podíval na svou knihovnu [czech-holidays](https://github.com/honzajavorek/czech-holidays). Nějaký borec z KPMG mi napsal mail, že mám v knihovně chybu a mě se zrovna chtělo prokrastinovat, tak jsem to nejen opravil, ale celou knihovnu jsem i oživil a předělal. Víc jsem o tom napsal do [vlákna na Twitter](https://twitter.com/honzajavorek/status/1564907198832152576). Na své nové řešení jsem byl hrdý do chvíle, než bráchu napadlo, že by knihovna [mohla umět ještě i otvírací doby](https://github.com/honzajavorek/czech-holidays/issues/14). U toho jsem si uvědomil, že kdybych je přidal, byla by to asi breaking change, jelikož teď knihovna vrací tuples a ty nejsou jednoduše rozšiřitelné :D Každopádně bych stejně nechtěl přidávat něco jen tak, u čeho nemám ověřeno, že by to doopravdy použili aspoň tři lidi, takže jsem jen založil issue a počkám, jaký bude zájem. Já si nejsem vůbec jistý, jestli celé czech-holidays vůbec používají aspoň tři lidi ¯\\\_(ツ)\_/¯

Pak už nezbývalo než prokrastinovat pomocí upgradů. Knihovna ics konečně [vydala novou verzi na PyPI](https://pypi.org/project/ics/0.8.0.dev0). Dověděl jsem se o tom, protože jsem sledoval patřičná issues na GitHubu. I když je to pre-release, stále lepší, než instalovat z gitu, takže jsem na to hned upgradoval.

Další věc byla py-cord, kde zavřeli [moje issue](https://github.com/Pycord-Development/pycord/issues/1491), s kterým jsem před několika týdny strávil moře času. Upgradoval jsem na nejnovější verzi a hurá, vše fungovalo. Radost.


## Spuštění onboardingu

Pak jsem se zastavil a uvědomil si, že takhle ten onboarding nikdy nedodělám. Prostě to jen prokrastinuju. A protože už mám něco odžito, vím, že na to je dobrá jedna konkrétní léčba: _continuous delivery_.

Já sice _continuous delivery_ dělat chtěl, vytvořil jsem MVP a stačilo napsat pět prvních tipů a ty pak pustit do prvních beta testerů, ale to psaní mi prostě takhle nešlo. Takže jsem se rozhodl, že když to nejde skrz _continuous delivery_, půjde to skrz **větší** _continuous delivery_.

Dal jsem si úkol, že do konce dne to spustím. S tím jedním tipem, který mám napsaný. A prostě budu dopisovat další tipy a vždy, když nějaký dodám, tak se lidem pošle. A že mě to tak bude bavit víc, protože hned uvidím výsledek. A že ty tipy budou i lepší, protože při psaní dalších hned uvidím, jak lidi reagují na ty první.

Povedlo se a do konce dne jsem měl tipy spuštěné. A hned jsem přišel na několik chyb a opravil je. Oznámil jsem v klubu, že onboarding spouštím a že sice bot slibuje posílání tipů „zhruba jednou za den“, ale že to bude asi chodit pomaleji a možná i zmateněji, protože to teprve ladím. A hotovo.

Čtvrtek jsem strávil psaním dalších tipů a úplně jsem se do toho ponořil. Najednou mě to hrozně bavilo, protože jsem věděl, že viditelný výsledek je jeden git push daleko. Akorát že jsem na konci dne ten git push udělal a celé to spadlo. Zjistil jsem, že Discord má nějaké limity na počet kanálů a tento fakt mi rozšlapal bábovičky.


## Co s tím?

Při onboardingu bot založí privátní kanál pro nového člověka, přidá do něj moderátory a posílá do něj postupně tipy. S těmito kanály jsem měl velké plány i do budoucna. Musí to být privátní kanály, protože:

- Do **soukromých zpráv** by viděl jen bot, ne já nebo jiný moderátor. Bot může posílat soukromé zprávy, ale musel bych nějak ošetřit, aby mu tam lidi neodepisovali, nebo aby mi to přeposlal, nebo aby jim na to něco odepsal a poučil je, že jejich zprávu nikdo neuvidí.
- Taky by se mi dost špatně ladilo, co přesně komu bot do soukromých zpráv posílá.
- Někteří uživatelé mají striktní nastavení a neumožňují doručování soukromých zpráv od účtů, které nemají v přátelích. Bot by, pokud by se mu soukromá zpráva nepovedla poslat, musel vytvořit něco přímo v klubu a poprosit uživatele, aby si jej přidal do přátel.
- Soukromé zprávy jsou mimo Discord servery, pouze mezi uživateli. Proto v nich neexistuje kontext klubu a nelze tam dělat plnohodnotné odkazy na místnosti, lidi, nebo role v klubu. Na tipy to reálně použít prostě nejde.
- Na Discordu nově existuje koncept **privátních vláken**, který by možná šel využít. Kdyby neměly jednu vlastnost, a to, že pokud tam je nějaký odkaz na někoho, automaticky ho to do vlákna přidá jako účastníka diskuze. Tedy kdybych poslal tip, ve kterém bych chtěl zmínit, že existuje nějaká role a označil ji tam, tak by se do vlákna přidali všichni, kdo tu roli mají. Na tipy to reálně použít prostě nejde.
- Privátní vlákna by se po nějaké době neaktivity automaticky archivovala, což by mohlo být dobře nebo špatně.
- Privátní vlákna by se tvářila jako privátní, ale ve skutečnosti, kdyby tam kdokoliv omylem někoho označil, např. „Honzo, tady ten uživatel @pepíček je na mě hnusný, pomož mi“, tak by to pepíčka přidalo do diskuze. To si nemusí při psaní člověk uvědomit a byla by to potenciálně nebezpečná díra do soukromí.

Musí to tedy být **privátní kanály**! Ty nemají žádné z uvedených nevýhod, ale Discord umožňuje mít v jedné kategorii pouze 50 kanálů a na Discord serveru pouze 500 kanálů celkem (včetně kategorií, které Discord bere jako kanály). Údajně je i limit na 1000 aktivních vláken, ale to je mi asi celkem jedno.

Zatím jsem vymyslel jen to, že se tedy musím nějak spokojit se zhruba 400 privátními kanály, když 100 si nechám na zbytek klubu. V době psaní těchto poznámek má klub 370 členů, takže je jasné, že kanály nemohou zůstávat a budou podléhat nějaké retenci, to se nedá nic dělat. Jejich jediný účel bude onboarding uživatele a potom se smažou. Na velké plány do budoucna mohu zapomenout, nebo je prostě musím vyřešit jinak než privátním kanálem pro každého uživatele zvlášť. Pokud se budou kanály zavírat, limit na 400 by měl stačit, protože předpokládám, že nebudu nikdy onboardovat 400 uživatelů zároveň. Tipy se budou posílat dva až tři týdny, pak se kanál zavře. Měsíčně teď přijde klub vyzkoušet do 80 lidí, maximum v historii bylo kolem 100.

Jak vyřeším, že v jedné kategorii může být jen 50 kanálů? Vytvořím víc kategorií stejného jména. Lidem se zobrazí pouze jedna kategorie a jeden kanál, protože jen tam mohou vidět. Já bohužel uvidím 8 kategorií pro 400 kanálů, ale to je můj boj. Discord naštěstí podporuje to, že kategorie i kanály se mohou jmenovat totožně (liší se IDčkem).

Jak si uložím, že někdo prošel onboardingem a už se může kanál smazat a nemá se znova vytvořit? Zatím mě napadlo jen poslat člověku do soukromé zprávy nějakou gratulaci, podle které to pak poznám. Pokud člověku nepůjde psát soukromé zprávy, vytvoří bot privátní vlákno v kanálu #klub a poprosí člověka, aby si přidal bota do přátel. Toto nemusím programovat hned. Obecně, permanentně platné věci budou muset být vidět někde v klubu, nebo se musí poslat do soukromých zpráv. Uvítací kanál se po nějaké době smaže.

Původně jsem počítal s tím, že když napíšu nový tip, přijde i lidem, kteří jsou v klubu už dlouho. To už nebude možné. Co s tím? Asi nic. Takový člověk bude muset holt sledovat novinky v klubu, číst si oznámení, vnímat změny. Onboarding bude sloužit jen zcela novým členům.


## Aspoň hotfix na páteček

Teď v pátek jsem do kódu nějak narychlo doplácal, aby se kanály vytvářely do více kategorií a aby mi všechno přestalo aspoň padat. Takže už se umí založit více jak 50 kanálů, aktuálně 61 ve dvou kategoriích. Objevil jsem u toho další chyby, např. že některé tipy měly přes 2000 znaků a to je zase na Discordu přes limit na příspěvek. To mi ale zase tolik nevadilo, aspoň to byla dobrá motivace texty zkrátit.

V klubu jsem při oznámení spuštění onboardingu napsal, že kdo to chce ze starších členů vyzkoušet, ať dá na zprávu emoji s (pokusným) králíkem, že je přidám mezi beta testery. Jenže jak se tam stále klikali, přestalo mě bavit je přidávat ručně. Doprogramoval jsem tedy pár řádků, které se na tu zprávu podívají, přečtou kdo dal emoji králíka a tyto uživatele zařadí do onboardingu.


## Další poznámky

- [Python sprint](https://docs.google.com/document/d/1mEInB4EOzyQkDbcs8BTEqDhtV-9IAIDPKirjmcH5jaA/edit#) se konal a já tam nebyl, protože jsem doma ležel s covidem. Zjevně to ale lidi nakoplo. Možná bude komunita zase organizovat [PyCon CZ](https://cz.pycon.org/).
- Advokátka [Pyvce](https://pyvec.org/) se ozvala s tím, že soud díky novým papírům konečně úspěšně přijal výsledek našich voleb a máme zase všechno v pořádku a funkční nový výbor. Hned jsem ji poprosil, aby nám připravila nějaké věci do budoucna, které by nám umožnily se takovým situacím pro příště vyhnout. Na schůzi výboru jsem tentokrát nebyl kvůli covidu, ale prý do spolku přijali novou členku, což je super.
- Měl jsem call s velkou firmou, která chtěla prodloužit spolupráci s klubem. Rozjížděl se mi už covid a tak jsem to absolvoval s paralenem. Přesto se mi podle nového ceníku podařilo prodat jim ten nejvyšší tarif. Už jsem dokonce poslal fakturu a mám z toho celého radost.
- S jinou firmou jsme si o prodloužení spolupráce zatím jen psali. Upozornil jsem na nový ceník a čekám na odpověď.
- Na sociální sítě jsem zase nic nepsal, nebaví mě to.
- Během 14 dní od 20.8. do 2.9. jsem při procházkách nachodil 4 km a ujel na kole 128 km. Celkem jsem se hýbal 17 hodin a zdolal při tom 132 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Čtyři věci, které bych chtěl zvládnout udělat příště:

1. Pracovat dál na onboardingu.
2. Posunout vpřed věc, která souvisí se spoluprací s Ataccama.
3. Udělat za junior.guru letáček pro [Red Hat Research Day 2022](https://research.redhat.com/red-hat-research-day-europe-2022/)
4. Být hostem ve dvou podcastech a účastnit se jednoho až dvou komunitních eventů.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Proč mnoho evropských iniciativ na podporu žen v IT nefunguje? Je třeba začít od nejmladších dívek](https://cc.cz/proc-mnoho-evropskych-iniciativ-na-podporu-zen-v-it-nefunguje-je-treba-zacit-od-nejmladsich-divek/)<br>Do černého.
- [“Jak my v té filosofii říkáme”: bytostné žvanění Anny Hogenové (nekrácená verze stati otištěné v LN jako “Žena za pultem filosofie” s hyperodkazy)](https://hip.ff.cuni.cz/2022/08/06/jak-my-v-te-filosofii-rikame-bytostne-zvaneni-anny-hogenove-nekracena-verze-stati-s-hyperodkazy/)<br>Nevím, proč jsem to četl, ale nelituji toho, protože jde o naprosto úžasné dílo.
- [Co všechno Putin zamlčel. Vyprávíme dějiny Ukrajiny, jak se skutečně odehrály](https://denikn.cz/837812/dejiny-ukrajiny-1500-let-na-krizovatce-civilizaci/?utm_source=www.seznam.cz&utm_medium=sekce-z-internetu)<br>Longread, který mi posloužil jako zajímavý eskapismus během trpění s covidem v posteli.
- [76 - Are Aircraft Carriers Becoming Obsolete?](https://theredline.libsyn.com/76-are-aircraft-carriers-becoming-obsolete)<br>Mají v dnešní době vlastně ještě nějaký smysl letadlové lodě? A pokud ano, dá se tím smyslem obhájit jejich neskutečná cena? Jak moc jsou navíc zranitelné? Potopí je jedna střela nebo ponorka? Co by potopení znamenalo pro prestiž USA?
- [M&M22 176: Back to school](https://bigvilik.com/2022/08/29/mm22-176-back-to-school/)<br>Pastelky v obchodech se školními hesly v půlce srpna mi vždy zaručeně pokazily prázdniny. Dnešní děcka to nemají jinak. Horší než vánoční výzdoba v říjnu.
- [M&M22 175: Himaláje!](https://bigvilik.com/2022/08/29/mm22-175-himalje/)<br>Lol
- [Stable Diffusion is a really big deal](http://simonwillison.net/2022/Aug/29/stable-diffusion/#atom-entries)<br>Že nebudou jako první mít co žrát ilustrátoři, grafici a jiní umělci, to asi od uměle inteligence čekal málokdo.
- [Uspěchaná ukrajinská ofenziva u Chersonu může skončit katastrofou](https://www.tydenikhrot.cz/clanek/ukrajinska-ofenziva-u-chersonu-muze-skoncit-katastrofou)

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu jsem použil vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
