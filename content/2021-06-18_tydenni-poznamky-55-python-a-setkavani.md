Title: Týdenní poznámky #55: Python a setkávání
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl další týden (14.6. — 18.6.) a tak [stejně jako minule]({filename}2021-06-11_tydenni-poznamky-54-ockovani.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tento týden byl ve znamení outdoor akcí a potkávání lidí, ať už kvůli práci, na nějakém srazu, nebo i jen tak na oběd. Je velmi osvěžující zase vídat lidské tváře naživo a ne přes obrazovku počítače. Co osvěžující zas tak není je naše objevování faktu, že nový byt není zas tak moc odolný proti slunci, ačkoliv se zdálo, že je to starý, památkově chráněný pavlačák na náměstíčku, tak by v něm mohl být chládek. Nic takového, pečeme se za živa!


## Cesta do Brna

Hned v pondělí jsem vyrazil na otočku do Brna, abych navštívil [Engeto](https://engeto.com/) a abychom tam udělali nahrávky toho, co jsme připravovali několik předchozích týdnů. Teď nás čeká postprocessing a snad do měsíce to bude venku, těšte se na tu parádu. Jsem vážně zvědavý, co z toho bude. Přinejhorším to někdo pak aspoň zremixuje do memů.


## Uzavření dohody s další vzdělávací agenturou

Cestou vlakem z Brna jsem dokončil dokument, který sepisoval dohodu nad rámec obchodních podmínek. Tu jsme nakonec tento týden podepsali a tím jsem splnil dlouho táhnoucí se úkol, dokončil jsem přípravy na partnerství se [Software Development Academy](https://sdacademy.cz/), která nedávno na českém trhu otevřela pobočku. Těsně předtím, než jsem začal psát poznámky, jsem přidal jejich logo na stránku o klubu.

Pokud jejich absolventi projeví zájem o dlouhodobější podporu při hledání práce a rozjezdu nové kariéry, SDA jim zajistí 3 měsíce v klubu. Podobnou spolupráci už mám i s Engetem a je otevřená i jiným vzdělávacím agenturám.


## Nové CSS a stránka o klubu

Začal jsem vytvářet novou [stránku klubu](https://junior.guru/club/). Jedu _continuous deployment_, takže to, co jsem zatím vytvořil, je normálně na produkci, akorát na [přísně utajené, zcela náhodné adrese](https://junior.guru/club2/). Jeden celý den jsem se soustředil čistě na to, co na stránce bude za texty a jak bude vypadat a to jsem si kreslil na papíry.

Stránku předělávám proto, že ta původní je z ledna a je dnes už prostě slabá. Když jsem ji dělal, klub prakticky ještě neexistoval a já jsem do té stránky spíše promítl svou představu, o čem by klub měl být. Dnes už je po měsících provozu vše jinak a mohu stránku vystavět s mnohem konkrétnější _value proposition_.

Zároveň to beru jako příležitost udělat zase trochu něco pro přesun JG na MkDocs, takže nová stránka už bude tam. V souvislosti s tím jsem si vzpomněl, že plugin na makra do MkDocs už [opravil jednu věc s tím, co je v jakém scope](https://github.com/fralau/mkdocs_macros_plugin/issues/81), takže jsem překopal svoje makra, aby už jely podle nového systému, což je zjednodušilo.

A aby toho nebylo málo, chci pro tuto novou stránku i zcela nové CSS. Dal jsem si call s [Danem Srbem](https://coreskill.tech/) a bavili jsme se o tom, jak a co, protože má hodně zkušeností a ví, kam se vyvinul Bootstrap, který chci použít.

Rozhodl jsem se, že chci určitě už použít nějaký CSS framework, protože převážně ruční způsob, jakým CSS dělám, už není úplně efektivní a udržitelný. Navíc, od frameworku si slibuji, že mi dá konvence a třeba i nějaké komponenty zadarmo. Zprvu jsem myslel, že Bootstrap použiju jen jako Tailwind, akorát tak trochu naopak, to znamená, že si do svého SCSS importuji reset, [proměnné](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss) a podkladovou vrstvu z Bootstrapu a [dál už si budu vše psát sám](https://getbootstrap.com/docs/5.0/customize/overview/), v BEMu a za využití proměnných z BS jako stavebních bloků, ale nakonec asi podlehnu zcela a využiju i komponent a dalších věcí z BS. Systém, jakým to budu dělat, si teprve sedá a bude se vyvíjet, ale víceméně jsem se už rozhodl, že opustím i ten BEM a podřídím se tomu, jak třídy dělá BS, [aby mi to prostě nikde nedřelo](https://github.com/getbem/getbem.com/issues/152), nechám si to hezky všechno nadiktovat.

Pro ty, kterým se zdá, že BS žádné konvence nemá, tak to sice není tak promakané a praktické jako BEM, ale nějaké konvence má:

- [Bootstrap: Approach](https://getbootstrap.com/docs/5.0/extend/approach/)
- [twbs/stylelint-config-twbs-bootstrap](https://github.com/twbs/stylelint-config-twbs-bootstrap) (Stylelint nastavení)
- [Code Guide](https://codeguide.co/) (od autora Bootstrapu)

Rozhodl jsem se teda začít s CSS úplně nanovo, což jsem si už delší dobu přál. Upravil jsem Gulp a vše tak, aby mi to generovalo ze separátních SCSS souborů zvlášť bundle, který připojuji zatím pouze v této jediné nové stránce, ale později ji chci rozšířit postupně na všechny stránky, které už jedou pod MkDocs. Tam vytvořím zcela nové HTML s prvky z BS a ostyluji si je podle svého. Moc toho potřeba není: navbar, content, patička. To bude zatím stačit a potom budu přidávat, co budu potřebovat.

Přidal jsem i [Stylelint](https://stylelint.io/), abych to všechno už psal hezky a podle BS konvencí. Sice jsem do teď na JG žádný linter de facto neměl, pouze na kontrolu vyložených chyb a ne stylu psaní kódu, aby mě to nezdržovalo, ale toto už bude vážně míněná verze JG, taková ta „druhá verze“, tak ať to má už kulturu.

Abych náhodou nezvětšil CSS bundle, zapojil jsem i [PurgeCSS](https://purgecss.com/), ale jako minimalista a purista jsem zas nechtěl přidat těch npm balíčků moc najednou a tak jsem se zasekl a [Autoprefixer](https://github.com/postcss/autoprefixer), který se má s BS správně použít, jsem tam zatím nedal. Dan mě ukecává, ať ho tam dám, ale já to zatím nechávám uležet. Jednak vyžaduje mít v projektu ještě PostCSS, což je zase o nástroj víc, jednak bych byl raději, kdybych psal prostě pouze to CSS, které funguje všude a novějším věcem se prostě vyhnul. Viz [starší diskuze na stejné téma o JS](https://www.facebook.com/groups/frontendisti/permalink/2746238622254311/?__cft__[0]=AZVZJuSpm7zGGaVDL8NhCXZVp5bZNa7GSIgdaqv38ktWV8hkiDgH8s4mD60_D_OP7Cedka39cf_ZU4PRfmLpHyUTAcEyvky-r_S4OsXOdslKcAYmA2uFM5ubpOeBRiQ3BO3GIOZHDt4QJqfQTVoRg7QJ&__tn__=%2CO%2CP-R). Pokud vám to přijde nepochopitelné, tak se nedá nic dělat, jsem už prostě takový svéráz, který počítá, kolik má npm balíčků v projektu, sestimsmiř. Co taky čekat od člověka, který píše HTML v Jinja2 a ne v Reactu, a který má na projektu tak nemoderní věc, jako je Gulp, že? No ale zatím jsem ten Autoprefixer úplně nevyloučil, jak jsem psal, nechávám to uležet.

Abych mohl použít BS, musel jsem taky přejít ze starého parseru SCSS na nový. Ten starý stejně už dělá problémy ([díky čemuž](https://stackoverflow.com/a/67303155/325365) jsem teda na StackOverflow za poslední týdny nabral snad stovky bodů a stále přibývají :D ), tak jsem ho konečně zahodil a pořídil si [gulp-dart-sass](https://github.com/mattdsteele/gulp-dart-sass).

Taky bych si sem chtěl poznačit [bootstrap.build/app](https://bootstrap.build/app), který v klubu doporučila [Martina Hytychová](https://martinahytychova.github.io/), ale zatím jsem to teda nepoužil.


## Makefile

Jedna z věcí, které umí pipenv a [Poetry](https://github.com/python-poetry/poetry) je neumí, jsou tzv. scripts, tedy sekce v konfiguračním souboru, kam lze napsat různé příkazy a lze je pak skrze pipenv spouštět. Vlastně totéž jako [npm scripts](https://docs.npmjs.com/cli/v6/using-npm/scripts). Osobně naprosto rozumím tomu, že Poetry to oficiálně považuje za „out of scope“ a budu raději, když udělají perfektní nástroj na instalaci a vývoj projektu a tímto se nebudou zatěžovat. Jednou bych chtěl na Poetry přejít, takže jsem tento týden udělal první krok a zkusil jsem místo pipenv scripts přejít na starý dobrý [Makefile](https://github.com/honzajavorek/junior.guru/blob/master/Makefile). Zatím mě to neuráží.

Jediné, na co jsem narazil, je neohrabanost přidávání dalších parametrů (např. nemohu udělat `make test -- -vvx`, aby se spustil `pytest -vvx`, musím tam šaškovat s nějakou proměnnou `make test TESTOPTS=-vvx`, což mi jako klukovi z 21. století prostě přijde takové moc… fousaté…

> Neví někdo o nějakém návodu na Makefile, který nevytvořili C/C++ programátoři před 50 lety tesáním do hliněných tabulek, ale vypadá jako moderní a čitelná dokumentace pro lidi?<br>
> — Honza Javorek v [klubu junior.guru](https://junior.guru/club/)

Odložím si tady [jediný existující pěkný návod na Makefile na internetu](https://www.gnu.org/software/make/manual/make.html#Simple-Makefile), za odkaz děkuji [Petrovi Messnerovi](https://www.messa.cz/).


## Python komunita

Tento týden se to všechno sešlo a poměrně dost jsem se po dlouhé době pověnoval Python komunitě, ať už české, pražské, nebo té v Namibii :)

- Schůze výboru [Pyvce](https://pyvec.org/), kde jsme se připravovali na
- historicky první členskou schůzi Pyvce, kde jsme trénovali scházení se, hlasování, dotazování,
- následně první [Pyvo v Praze](https://pyvo.cz/praha-pyvo/), které se odehrálo naživo, v parku na Štvanici,
- následně [PyCon NA](https://na.pycon.org/), který běží teď v pátek a sobotu.

Z Pyva jsem se vrátil za rozbřesku, takže čtvrtek byl náročnější, ale stálo to jednoznačně za to. Přišla hromada lidí, některé jsem neviděl snad i roky, bylo strašně příjemné se zase vidět naživo, popovídat si, potkat se. Přišli i někteří členové JG klubu, což je strašně super, protože takhle se začátečníci zapojí do dalších programátorských komunit a nasbírají víc kontaktů a kamarádů v oboru, než kdyby byli jen v klubu. Jeden člen byl tak hladový po setkávání s lidmi, že přijel na otočku vlakem z Hodonína.

Jak jsem psal už dřív, chtěl jsem udělat rozhovor s [Jessicou Upani](https://twitter.com/JessicaUpani), hlavní organizátorkou Python komunity v Namibii, ale bylo to složité, protože jsem s tím vyrukoval dost na poslední chvíli a ona fakt neměla vůbec čas se tomu věnovat. Nakonec mi poslala odpovědi ve čtvrtek ráno, takže skoro celý čtvrtek jsem strávil tím, že jsem dával dohromady ten rozhovor, editoval to, vybíral fotky, atd. Snažil jsem se to stihnout vydat do odpoledne, abych chytil Evropany ještě „živé“ a Amíky „už vzhůru”, tzn. aby měl článek co největší dopad. Samozřejmě to má zafungovat nejen jako rozhovor, ale i jako reklama na PyCon NA, na jejich Patreon, apod. Nakonec se to povedlo a vydal jsem to: [Jessica Upani about Python events in Namibia: You have to be pure in terms of your why]({filename}2021-06-17_jessica-upani-about-python-events-in-namibia-you-have-to-be-pure-in-terms-of-your-why.md). Článek na začátku popisuje i můj vztah k Namibii.

Zatím samé nadšené ohlasy, tak snad to trochu pomůže! PyCon NA je online a je i v sobotu, takže i když jste třeba promeškali dnešek, můžete se připojit ještě zítra. Pokud chcete pomoci se sdílením, pod článkem jsou odkazy na sociální sítě, třeba [tweet](https://twitter.com/honzajavorek/status/1405532488504516617) a tak.

Vtipné je, že kvůli slunci jsem v těchto dnech vytáhl i klobouk, který jsem v únoru 2020 pořídil na hlavní třídě ve Windhoeku před cestou do pouště. Funguje skvěle, v poušti i rozpálené Praze :)


## Další poznámky

- Vyprázdnila se mi fronta v [Bufferu](https://buffer.com/), takže jsem se pověnoval sociálním sítím a dal tam věci aspoň na další dva týdny. Většina toho se točí kolem filmu [Nová šichta](https://www.csfd.cz/film/892942-nova-sichta/), který se teď konečně dostává do kin.
- Juchů! Mám novou [sponzorku na GitHubu](https://junior.guru/donate/)! Tajnou, jméno nevyzradím. To je přímo funkce GitHub Sponsors, můžete tam někoho sponzorovat bez toho, aby to bylo veřejně vidět a sám už několik takových sponzorů mám. Sice tento způsob sponzorství už moc aktivně nepromuji, ale výzvy k tomu ještě jsou pod stránkami, které se přímo týkají příručky, tak to tam asi našla. Chci spíš, aby lidé šli do klubu a podpořili mě tam, ale je fakt, že přes GitHub Sponsors nebo Patreon mi člověk může poslat víc peněz než stovku měsíčně :) A když se mi povede sponzorujícího člověka kontaktovat, posílám mu link na členství do klubu, protože kdo mi jakýmkoliv kanálem pravidelně posílá peníze, nárok na členství prostě má.
- Někdo zjistil, proč Frozen-Flask nefunguje správně s Flaskem v2 a [poslal PR s opravou](https://github.com/Frozen-Flask/Frozen-Flask/pull/115). Tento týden jsem si našel čas, koukl na to a vydal [novou verzi knihovny](https://pypi.org/project/Frozen-Flask/0.18/), která už by tedy s Flask v2 fungovat měla.
- [Zpropagoval jsem trochu WebExpo](https://twitter.com/honzajavorek/status/1404735521948147717) a domlouváme se i dál na spolupráci, ze které by mohly plynout nějaké výhody pro členy klubu. Stay tuned!
- JetBrains inzerovali na JG nabídky letních stáží, tak jsem je zkusil oslovit, zda by nechtěli spolupracovat i nějak víc.
- Volal jsem si s Mílou ohledně jeho práce na AI robotovi na třídění pracovních nabídek. Připomenuli jsme si, co jsme zapomenuli a domluvili jsme se, co dál. Míla pak [udělal PR](https://github.com/honzajavorek/junior.guru/pull/579), ale ještě jsem se na něj nestihl podívat.
- Dávám si občas do kalendáře všelijaká obskurní data z vlastního života a pak na mě vyskakují jako výročí. Třeba tento týden to bylo 7 let, co mám řidičák. Skoro celou tu dobu je neplatný, protože záhy po jeho obdržení jsem se přestěhoval z Brna do Prahy a bylo mi zatěžko si jít pro nový jen proto, že se tam má změnit město. (Proč to tam vůbec je?) Použil jsem ho na skútru ve Vietnamu (kde neplatil už tuplem), na Mallorce a na Azorách. Jedinkrát jsem řídil auto přes 2 vesnice u Zlína, měsíc po obdržení řidičáku. Pak už jsem auto nikdy neřídil. Jsem zvědav, jestli se to někdy změní a případně kdy :)
- Našel jsem papíry s poznámkami z ledna, kdy jsem připravoval rozjetí klubu. Přišlo mi to najednou jako cesta do pravěku, úplná věčnost. Bylo strašně osvěžující číst si, co jsem měl za problémy a co jsem v té době řešil a nevěděl jak udělat. Všechny ty věci dnes mám už vyřešené a beru je jako automatické a že to tak i vždycky bylo. Možná bych si měl starší poznámky číst častěji :)
- Moc jsem tento týden nestíhal odpovídat na zprávy a maily, i klub jsem trochu zanedbával, ale v pátek jsem se to pokusil všechno dohnat.
- Během 7 dní od 12.6. do 18.6. jsem při procházkách nachodil 10 km. Celkem jsem se hýbal 4 hodiny a zdolal při tom 10 kilometrů.


## Co plánuji

Dvě věci, které bych chtěl zvládnout udělat příště:

1. Pokračovat v budování nové stránky klubu.
2. Naplánovat po pauze nějaké další přednášky v klubu.

Třetí bod není, chci se soustředit na tyto dvě věci a hlavně tu první nabušit co nejdřív.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Další ženy promluvily o traumatizujících zážitcích s Dominikem Ferim. Problémy měla i nezletilá](https://a2larm.cz/2021/06/dalsi-zeny-promluvily-o-traumatizujicich-zazitcich-s-dominikem-ferim-problemy-mela-i-nezletila/)
- [Don’t Feed the Thought Leaders](https://earthly.dev/blog/thought-leaders/)<br>Jak si nechat radit od druhých - čí rady brát s rezervou a čí následovat?
- [Do You Need Redis? PostgreSQL Does Queuing, Locking, & Pub/Sub](https://spin.atomicobject.com/2021/02/04/redis-postgresql/)<br>Potřebujete pro své use-cases Redis? Nestačilo by vám PosgreSQL?
- [In Support of the Fifteenth Standard](https://smizell.com/posts/2021/06/in-support-of-the-fifteenth-standard/)<br>Až vám zase někdo pošle XKCD 927, odpovězte odkazem na tento článek.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
