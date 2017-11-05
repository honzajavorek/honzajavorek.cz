Title: Code review
Date: 2017-11-05 15:40:00


_Code review_ je kontrola změn v kódu před tím, než jsou začleněny do projektu. V praxi dnes code review vypadá nějak takto:

- Uršula chce udělat změnu v projektu. Změny provede na své [větvi](https://git-scm.com/book/cs/v2/V%C4%9Btve-v-syst%C3%A9mu-Git-V%C4%9Btve-v-kostce) kódu a vytvoří [Pull Request](https://help.github.com/articles/about-pull-requests/), tedy žádost o začlenění těch to změn.
- Uršula najde vhodného člověka, který by jí mohl udělat code review. Kdo je vhodným člověkem záleží na tom, jaké jsou procesy nebo zvyklosti ve firmě či na tom daném projektu. V tomto případě to je Věnceslav. Pokud Uršula používá GitHub, může tam Věnceslava [přímo naklikat](https://help.github.com/articles/requesting-a-pull-request-review/) jako někoho, od koho chce review.
- Věnceslav si přečte popis Pull Requestu. Díky tomu zjistí, čeho se týká a co je vlastně účelem změn. V tomto kontextu pak prohlédne kód. Může komentovat jednotlivé části a když je hotov, poskytne nějaký verdikt - buďto PR schválí, nebo zamítne.
- Uršula diskutuje s Věnceslavem o změnách. Nakonec jde a opraví nalezené chyby (nejčastěji tím, že přidá další _commity_ do téže větve, tedy i do téhož PR).
- Jestli začlenění schválených změn (_merge_) nakonec provede Uršula nebo Věnceslav, je opět na dohodě.

Jak bylo zmíněno, GitHub dnes člověka [celkem pěkně tímto procesem vede](https://github.com/features/code-review/). Kolem této základní kostry, jenž je všem společná, je ovšem spousta věcí, které si rozhodujeme sami. Kdo poskytuje review? Jak review probíhá? Jak probíhá diskuse kolem PR?

## Kdo kontroluje

Jedna z věcí, které jsou zcela zakořeněny v softwarové kultuře [Apiary](https://apiary.io/), jsou právě code reviews. Natolik, že pokud se vyjímečně stane, že začleňuji kód, který review nedostal, cítím se stejně provinile, jako bych použil `goto`, `eval`, nebo jinou věc, která programátory od mala budí ze spaní. Jak to u nás funguje?

Když nás bylo málo a neměli jsme firmu rozdělenou na týmy, dělal každý zrovna to, co bylo potřeba. Každý rozuměl každé části produktu, a uměl komukoliv udělat code review. Velmi brzy po tom, co jsem nastoupil, jsem dělal review ostříleným mazákům a oni mě. V code review neexistovala žádná hierarchie, která by říkala, že zkušenější dělají review méně zkušeným. Díky tomu se znalost codebase a schopnost code review hezky rozprostřela. Také nikdo neměl pocit, že by byl chytřejší než ostatní, nebo neomylný. Rovní s rovnými. Ono totiž pokud vám dělá review začátečník a nepochopí váš kód, není to jeho chyba. Napsali jste příliš komplexní a nepochopitelný kód. Až tam bude chvíli ležet a vy se k němu po čase vrátíte, budete ho také číst jako začátečník.

Když jsme vytvořili týmy kolem produktových oblastí ([_bounded contexts_](https://en.wikipedia.org/wiki/Domain-driven_design#Bounded_context)), změnilo se akorát to, že reviews si dělají lidé převážně v rámci týmu.

## Co se kontroluje

Code review se dělá zcela na všem, co má být začleněno do hlavní větve. I ve chvíli, kdy jsem ve tři ráno musel v rámci služby vstát a opravit produkci kvůli nějakému průšvihu, nechal jsem si udělat code review. Samozřejmě ne zcela vždy (někdy na to prostě nebyl čas) a také pomůže, když máte i ve tři polovinu firmy vzhůru, protože jsou v San Franciscu :-D

## Kdy se kontroluje

Toto nemáme úplně pevně dáno, ale slušností je udělat code review co nejdřív, kdy má dotyčný Věnceslav kousek volného času. Nevytrháváme se tedy z programátorského _flow_, ale v zásadě se očekává, že review proběhne aspoň do 24 hodin. Jestliže se totiž na review čeká dlouho, začně to příliš blokovat Uršulu. Někde (zdroj jsem nedohledal) jsem četl, že reviews by se měly dělat ihned, protože neblokovat někoho, kdo má práci hotovou, má vyšší hodnotu než chodit po špičkách kolem _flow_ někoho, kdo programuje. Svým způsobem mi to smysl dává.

## O čem se (ne)diskutuje

Zde záměrně smíchám to, co ve firmě děláme všichni, a to, co dělám já. Nebo co bych si přál, aby bylo běžné. Když přijdu k PR jako někdo, kdo má dělat review, postupuji následovně:

- Přečtu si popis PR. Pokud jej nemá nebo nevysvětluje _proč_ jsou změny prováděny, PR zavřu, nezajímá mě.
- Podívám se, zda prošly testy v _Continuous Integration_. Pokud ne, PR zavřu, nezajímá mě. Autor mě měl pozvat k review až ve chvíli, kdy je vše zelené. Mám-li dobrou náladu, podívám se proč testy spadly a napíšu komentář, který autorovi pomůže s vyřešením problému.
- Jestliže se změna týká něčeho, co ovlivňuje API nebo chování produktu, podívám se na změny v dokumentaci. Pokud žádné změny nejsou, PR zavřu. Pokud jsou, přečtu si dokumentaci a snažím se z ní pochopit, co změna dělá. V kontextu tohoto porozumění potom dělám review všeho ostatního. Jestli se něco od popisu liší, je to zásadní problém.
- Jako první hned po dokumentaci se podívám na testy. **Testy jsou nejdůležitější část PR.** Pokud chybí, PR zavírám. Důkladně čtu testy a přemýšlím nad tím, zda to, co testují je opravdu to, čeho chtěl autor změn dosáhnout a co je v popisu změn. Není nic horšího, než testy, které testují nesmysly.
- V tuto chvíli už přesně vím, jak má věc fungovat. Přečetl jsem totiž dokumentaci a testy. Mohu tedy pokračovat k vlastnímu kódu. Snažím se držet podstaty změn.

Začínání testy považuji po čase jako jednu z nejdůležitějších kvalit toho, kdo dělá code review. Začlenění špatných testů totiž dává falešný pocit bezpečí, že něco funguje tak jak má a je to do budoucna tikající bomba. To už je lepší nemít žádné testy, protože potom aspoň víte, že o funkčnosti daného kódu nevíte vůbec nic, a jednáte s opatrností.

## Jak se hodnotí

Po celou dobu review si v hlavě připomínky dělím na tři kategorie:

- _nitpick_ - Něco, co není vůbec důležité, ale [OCD](https://cs.wikipedia.org/wiki/Obsedantn%C4%9B_kompulzivn%C3%AD_porucha) mi nedovolí o tom nenapsat komentář.
- _blocking_ - Zásadní problém, kvůli kterému nemůže být PR začleněn a proč mu dávám zamítavý verdikt.
- Ostatní připomínky jsou buďto méně důležité, nebo k diskusi, ke zvážení.

Připomínky podle toho jasně označím. V negativním závěřečném hodnocení zopakuji, co přesně bylo tak problematické, že jsem kvůli tomu PR nepustil dál. Nejsou-li ale v kódu žádné _blocking_ připomínky, dám mu zelenou. Je na autorovi, zda má čas se se mnou vybavovat, zda chce opravovat drobnosti, nebo jestli naopak musí mít tento kód nutně zítra na produkci a raději udělá okamžitě _merge_. Běžně se stává i to, že autor souhlasí s připomínkami, ale kód potřebuje co nejdříve začlenit, takže to udělá a k připomínky později opraví v dalším, dedikovaném PR, nebo pro ně založí issues - aby se na ně nezapomnělo.

Mnoho _nitpick_ připomínkám se lze vyhnout, pokud se používá nějaký _coding style guide_ a vynucuje se pomocí linteru (např. [PEP8](https://www.python.org/dev/peps/pep-0008/)/[pycodestyle](https://github.com/PyCQA/pycodestyle), [Airbnb](http://airbnb.io/javascript/)/[ESLint](https://eslint.org/)). Přitom s linterem doporučuji neotravovat při lokálním vývoji - tam ať si ho každý nainstaluje a zapne/vypne dle libosti - ale v Continuous Integration. Při prototypování totiž linter spíše překáží. Pokud ale neprojde linter v CI, nemůže být kód začleněn do společné _codebase_. Díky linteru se také lépe udržuje téma diskuse v PR. Nebavíme se o mezerách a závorkách, ale o tom, jestli kód dělá to, co dělat má. A o jeho architektuře.

## Jak se diskutuje

Code review je psaná komunikace mezi dvěma lidmi a jako taková trpí množstvím příležitostí k tomu, aby se dotyční začali nenávidět. Stručně doporučím dvě věci:

- Pravidlo číslo jedna je odosobnit se od svého kódu. Pokud někdo píše, že váš kód je špatně, neznamená to, že chtěl ranit vaše city, že neumíte psát dobrý kód, že vás vyhodí z práce, že jste idiot, nebo že celý váš život nestojí za nic. Nejspíš chtěl jen napsat, že váš kód je špatně.
- Přečtěte si [Humanizing among coders](https://ana-balica.github.io/2017/05/28/humanizing-among-coders/). Nebo si to [pusťte na YouTube](https://www.youtube.com/watch?v=npyB5Oz-v-I).

## Kdo začleňuje

Kdo začlení schválený PR? To záleží na tom, co je navázáno na začlenění kódu do hlavní větve. Často _merge_ způsobí, že se někde automatiky nasadí nová verze aplikace, nebo že se vydá nová verze knihovny. Co když ji ještě vydat nechceme? Co když tato změna nejdříve vyžaduje nějaké změny na produkční databázi? Tyto věci ví autor kódu, tedy Uršula. Proto by měla udělat _merge_ ona. Věnceslav akorát "dá zelenou".

Kromě této ale existuje ještě jedna teorie, která říká, že v momentě, kdy je PR přijat, tak má být i začleněn. Pokud je při tom potřeba udělat něco speciálního, má to být napsáno v popisu PR a Věnceslav to má udělat a změny hned nasadit. Pokud Uršule napsal nějaké neblokující připomínky, ta je může adresovat v novém PR. Tento přístup zrychluje doručování nového kódu, protože se odstraňují některá čekání mezi Uršulou a Věnceslavem. Zároveň to klade nároky na Věnceslava - má zodpovědnost za nasazení aplikace, takže si bude dávat pozor, aby review udělal dobře.

## Deset nejčastějších chyb

Když jsem si s lidmi vyprávěl o code review, narazil jsem často na to, že jej dělají, ale vždy v nějaké z mého pohledu "jednonohé" formě. Vždy tomu něco chybělo k tomu, aby to fungovalo jako ta pěkná kontrolní mašinérie, jakou máme v práci. Rozhodl jsem se tedy o naše zvyklosti z Apiary a moje vlastní zkušenosti podělit.

Není to vyčerpávající, ale to ani být nemělo. K dnešnímu dni jsou jen na Zdrojáku na téma code review [tři články](https://www.zdrojak.cz/n/code-review/) a mimo český internet je určitě také spousta zdrojů, jak se v kontrole kódu zdokonalit. Jeden z nejlepších článků na toto téma je za mě jednoznačně [Top ten pull request review mistakes](https://blog.scottnonnenberg.com/top-ten-pull-request-review-mistakes/), kde Scott Nonnenberg rozebírá časté chyby při review a musím přiznat, že minimálně v rámci mojí praxe jsou to zásahy do černého.

Jak děláte code review vy? Schválili byste tento článek? A věděli jste, že k němu [taky můžete udělat code review]()? :-)
