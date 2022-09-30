Title: Týdenní poznámky #106: Onboarding členů, volby a půlmaraton
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (20.9. — 30.9.) a tak [stejně jako minule]({filename}/2022-09-19_tydenni-poznamky-105-zlinsko-a-nastenka.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Byl nějaký ten státní svátek, volby a tak různě, takže píšu až po dvou týdnech. Aby se to dalo číst, zkusím to tentokrát fakt stručně a dávám si na psaní maximálně hodinu.


## Chyba s vytvářením kategorií na Discordu

Jak jsem psal v některých předchozích poznámkách, jedna kategorie na Discordu může mít maximálně 50 kanálů a tak musím kanály s tipy pro nové členy v klubu rozdělovat do víc kategorií. Způsob rozdělování měl ale chyby a padalo mi to.

Zkusil jsem to naprogramovat jinak, ale po celém dni předělávání jsem došel opět k řešení, které mělo nějaké vady a nefungovalo dobře. Protože jede práce na tipech paralelně a dělá rovnou změny na Discordu, nedařilo se mi ani najít jednoduchý způsob, jak algoritmus izolovat od I/O, abych ho mohl nějak neprůstřelně otestovat.

Nakonec jsem do toho prostě bušil tak dlouho, až jsem vynalezl něco, co vypadá, že funguje.


## Vítání nových členů

Uvědomil jsem si, že mě nebaví vítat nové členy, protože je to vysilující. Spolu s Danem jsme hned u každého pod jeho přivítáním rozebrali kariérní možnosti a ptali se na otázky, které měly druhou stranu dovést k nějakému posunu. Jenže to neškáluje a cítil jsem, že já na tom vyhořívám a Dan na tom prokrastinuje, ale asi by časem taky vyhoříval. Navíc se nikdo další velmi nezapojoval, protože si netroufl předvádět tam podobné rozbory jako my s Danem.

Přijde mi, že nemůžeme každému příchozímu hned rozebrat kariéru. Není to v našich silách a vlastně mi ani nedává smysl dávat každému, kdo zrovna nakoukne do klubu a má dva týdny zdarma, plný servis kariérového poradenství. Zároveň nechceme, aby vítání ztratilo lidský rozměr.

Budeme se tedy s Danem snažit vítat „povrchněji“. Uvidíme, jak nám to půjde, protože nejen Dana, ale i mě, samozřejmě svrbí vždy prsty a hned bychom radili. Budeme prostě hlavně **vítat** a méně **radit**, případně lidi směrovat do kanálů, které je mohou zajímat. Toto je navíc činnost, se kterou nám může snadno kdokoliv pomoci.

Pohrávám si s myšlenkou, že by bot pro každého nového člena losoval někoho ze stávajících členů - např. těch, kdo jsou v klubu už rok a déle a vědí, jak to tam chodí, a poprosil ho, aby se zapojil a napsal nově příchozímu třeba i jen jednu, klidně krátkou, ale hezkou lidskou větu. Vlastně skoro takový lehký _buddy_ program.

Lidé se pak sami mohou na cokoliv zeptat v příslušných kanálech, pokud chtějí. Donutí je to možná zformulovat obecnější dotaz a zároveň kanály čte víc lidí, takže se rozproudí diskuze, kde k tomu může něco říct víc členů.

Píšu to tu jako hotovou věc, ale reálně mi trvalo třeba týden, než jsem si toto řešení v hlavě ujasnil. Probíral jsem to hodně s Danem, probíral jsem to s kamarádem na pivu, myslel jsem na to ve sprše, prostě si to vzalo hodně přemítání a ujasňování. Nakonec jsem to navrhl členům a ti mi stvrdili, že to je dobrý směr.


## Dva tipy pro nové členy

Konečně se mi povedlo pohnout i s dalšími tipy pro nové členy a dopsal jsem tip, který vysvětluje Discord role v klubu. Potom jsem začal psát tip, který se zabývá tím, jak mají lidi v klubu komunikovat a kam mají co psát, ale ten mě přivedl na myšlenku, že ještě před ním by měl jít tip o pravidlech chování a respektujícím a podporujícím prostředí v klubu. Takže ten jsem pak psal většinu dneška.


## Půlmaraton

Před několika měsíci mě kamarádi vyhecovali, abych se přihlásil na Půlmaraton Moravským krasem, který se běžel 28.9. v Blansku. O víkendu jsem si teda šel zaběhat a natáhl jsem to na 20 km, abych tušil, jestli na půlmaratonu teda spíš umřu, nebo spíš ne.

Pak jsem sjel do Blanska, kam jezdí přímý vlak z Prahy, setkal se s kamarády, zaběhli jsme to, večer dali v Brně pivko, přespal jsem u kamaráda a odjel zpátky do Prahy. Autobusem, protože ten je teď bohužel výrazně méně zoufalý, než výlukový vlak přes Vysočinu. Autobusem jsem nejel hodně dlouho, všude jezdím vlakem, takže mě fascinovalo, jak tam sedíme jako sardinky a jak ta věc může jezdit i doleva nebo doprava a předjíždět jiné hýbající se věci.

Závod mi sedl. Cítil jsem se strašně fajn, vtipkoval jsem se spoluběžci i s fanoušky podél trati, celou dobu se mi běželo dobře a cítil jsem se dobře. Bylo to na hranici mých sil, ale strašně jsem si to užil a v závěru jsem si ještě i zasprintoval. Neoficiální čas naměřený Stravou mám 1:49:16, délka byla 20.43 km, tempo 5:21 na km.


## Volby

Proběhly volby. Já sice kandidoval, ale záměrně na nevolitelném místě, pouze jsem chtěl Zelené na Praze 3 svou kandidaturou podpořit. Celkem jsem dostal 1.237 hlasů. Shrnutí voleb za sebe jsem [napsal na Facebook](https://www.facebook.com/honzajavorek/posts/pfbid02EbxJML2KR964jVYznvFcwdWqp779TsWWkgLozn65pz8Jaudh7FxM6RDLkcUnt13yl), zde kopie:

> Tak, a je to. Jsem rád, že mnou podporovaní [Zelení Praha 3](https://praha3.zeleni.cz/) zůstávají na radnici a snad to dopadne dobře i se skládáním progresivní koalice.
>
> Vyzkoušel jsem si, jaké to je podpořit veřejně nějakou politickou stranu, jaké to je být na její kandidátce, jaké to je dostat od nich tričko a stát s nimi na ulici a bavit se s voliči.
>
> Překvapilo mě, že dění v městské části sleduji zjevně natolik, že jsem lidem byl schopen v pohodě říct, kde se co plánuje, kde bude jaká stavba, nebo že existuje [Čistá Trojka](https://www.cistatrojka.cz/), [Antigrafitti program](https://www.praha3.cz/projekty/antigraffiti-program), apod. Přitom jsem obyčejný občan a jen čtu sociální sítě, kam se tyhle věci dávají. Lidi, zajímejte se o svoje okolí! 🙂 Sledujte aspoň profily své městské části, jako je [Praha 3](https://www.facebook.com/praha3.cz/). Možná se budete méně divit, možná se o spoustě věcí dovíte mnohem dřív, než vám vyrostou za domem, možná k tomu budete moci i něco říct.
>
> Teď si snad dám od politiky zase chvíli klid. Volby přímo v místě, kde žiju, a které na další 4 roky ovlivňují, jak se nám tu bude bydlet, chodit po ulici, hrát na pískovišti, apod., pro mě byly nakonec hrozné nervy. Možná mi na výsledku záleželo až příliš, ačkoliv mě osobně o nic nešlo.
>
> Sice budou brzo volby prezidentské, ale ty jsou mi naštěstí dostatečně jedno a tak snad nebude problém si je co nejvíc vyblokovat a věnovat se teď zas víc tomu, co se děje v mojem podnikání, co aktuálně frčí na pískovištích a kdo vítězí na okruzích Formule 1.

Pokud vím, koalice na Praze 3 ani na velké Praze nejsou zatím dojednány, takže výsledky voleb jsou sice známy, ale kdo bude vládnout, to jisté zatím vůbec není. Volby jsem sledoval s velkým napětím a nemohl jsem na to vůbec přestat přemýšlet. Stále jsem něco psal do sousedských aj. skupin na Facebooku, kde to taky různě vřelo, až jsem si v jeden moment musel sociální sítě vyloženě zablokovat, abych vůbec něco udělal.

Po volbách jsem měl plnou hlavu myšlenek o tom, co se dalo udělat jinak nebo nad čím se zamyslet, včetně teorií, proč jaká místní strana dostala kolik hlasů. To jsem nakonec všechno napsal do polointerní skupiny pro příznivce Zelených na Praze 3 a tím jsem téma na chvíli ve své hlavě uzavřel a uložil k ledu, přesně jak jsem napsal do toho statusu na Facebooku. Zkusím si teď dát od politiky trochu detox.


## Chyby, které neumím vyřešit

Z ničeho nic mi začalo `gulp-purgecss` vyhazovat toto:

```
[18:26:01] 'minifyCSS' errored after 333 ms
[18:26:01] Error in plugin "gulp-purgecss"
Message:
    Cannot read properties of undefined (reading 'hasOwnProperty')
Details:
    domainEmitter: [object Object]
```

Nepřišel jsem na to, jak to debugovat. Jak mám udělat, aby se vypsala celá stacktrace. Taky se to děje jen když to mám lokálně ve _watch_ módu a ne při jednorázovém buildu nebo na produkci. Vzdal jsem to a minifikaci CSS jsem z _watch_ módu zatím vyhodil.

Další věc, chodí mi nějaké chyby kvůli emailům. Robot posílá inzerentům každé pondělí informace o inzerátu. Používá k tomu SMTP mého osobního mailu na Gmailu, `jan.javorek@gmail.com`. Do kopie dává `honza@junior.guru`, což je ale jen [ImprovMX](https://improvmx.com/) alias pro tentýž Gmail. Aby mi ty maily taky přišly. Inzerentům to přijde, ale mě se to vrací s chybama:

```
There was a problem delivering your message to honza@junior.guru. See the technical details below, or try resending in a few minutes. From jan.javorek@gmail.com to honza@junior.guru:

550 5.7.1 Message considered as SPAM (Score of 5.0/5 with DKIMWL_WL_MED, DKIM_SIGNED, DKIM_VALID, HTML_IMAGE_ONLY_24, HTML_MESSAGE, HTML_MIME_NO_HTML_TAG, MIME_HEADER_CTYPE_ONLY, MIME_HTML_ONLY, RCVD_IN_DNSWL_BLOCKED, SPF_PASS, T_REMOTE_IMAGE) - ImprovMX
```

Emailům nerozumím, takže nevím, co dělám špatně a co můžu opravit. ImprovMX si platím, nemám jejich free verzi.

## Další poznámky

- Přidal jsem do hlavního menu na JG odkaz na Podcast jako na čtvrtou hlavní věc, kterou JG produkuje (tři další jsou Příručka, Práce, Klub). Dalo trochu práci to odladit v novém i starém designu a na malých obrazovkách.
- Publikoval jsem stránku [Psychika na cestě do IT](https://junior.guru/handbook/mental-health/), na které spolu s [Nelou](https://www.nelaprovazi.cz/) děláme dlouhé měsíce a teď se nám ji konečně povedlo dodělat a dát ven. Zatím kolem toho nebudu dělat humbuk, takže jen větička tady, promo uděláme později.
- Upravil jsem skript, který mi generuje šablonu pro týdenní poznámky. Nyní do ní přidává odkazy na aktuální nabídky práce inzerované na junior.guru.
- Upgradoval jsem MkDocs a zjistil jsem, že věc, na kterou jsem měl plugin, [dali přímo do jádra projektu](https://github.com/mkdocs/mkdocs/pull/2978). Super! Plugin [mkdocs-simple-hooks](https://github.com/aklajnert/mkdocs-simple-hooks) jsem odinstaloval a přešel na nativní řešení.
- V autobuse z Brna mě napadlo, že bych si mohl udělat skript, který přes RSS a youtube-dl stáhne díly jednoho video pořadu, kde jsou hlavně rozhovory a obraz tam není podstatný, vyseká jen zvuk a ten naservíruje přes podcastové RSS, které si přidám do [Overcastu](https://overcast.fm/). Díky tomu to budu moci poslouchat offline, v aplikaci, která mi vyhovuje a rychlostí, která mi vyhovuje (aktuálně 2,5x). Trvalo mi to trochu déle, než jsem chtěl, ale i tak jsem to měl hotové za pár hodin a sám se divím, ale funguje to. Akorát ty zvukové soubory hostuju na GitHub Pages a to asi není úplně ideální. A nejspíš to celé ani není legální, ale dělám to výhradně pro svou osobní potřebu, takže vám tu ani neřeknu, kde to celé je a co to je za pořad.
- Předal jsem jedné člence klubu a shodou okolností teď i spoluorganizátorce pražského Pyva projekt Telegram bota, který lidem oznamuje, že bude Pyvo. Měl jsem ho [napsaný v Haskellu](https://github.com/honzajavorek/pyvo_bot) (viz [článek o Haskellu tady na blogu]({filename}/2020-01-14_courting-haskell.md)), neudržoval jsem ho a nedávno jsem ho dokonce vypnul. [Mia](https://www.linkedin.com/in/mia-bajic/) ho chce přepsat do Pythonu v rámci [Hacktoberfestu](https://hacktoberfest.com/). Udělal jsem jí na to [repo na Pyvci](https://github.com/pyvec/pyvo-bot).
- Byl jsem na [Deepnote](https://deepnote.com/) párty a potkal jsem tam hodně zajímavých lidí, nových i „starých“. Netlačil jsem na pilu, takže z toho vyloženě nejsou nějaké _dealy_ s firmama, ale minimálně jsem si udělal některé důležité kontakty. Taky jsme tam nejspíš s kamarádkou upekli jeden z příštích dílů podcastu.
- Dověděl jsem se, že existuje nějaká profesní síť [Polywork](https://www.polywork.com/), jakože „LinkedIn, ale lepší“. Zatím jsem neměl čas to vůbec prozkoumat.
- Napsala mi docentka z University of Economics in Bratislava, že chce používat materiály na junior.guru ve výuce.
- Kamarád [Muheue](https://twitter.com/muheuenga/), pythonista z Namibie, pojede do Prahy na Ubuntu Summit a tak jsme řešili, jestli a jak se uvidíme.
- Vyrazili jsme se ženou na nákupy. Z lovu jsem si přinesl ponožky a bundu.
- Propagoval jsem nový díl podcastu: [#8 Michal Matuška (SUPERKODERS) o leadershipu a juniorech](https://junior.guru/podcast/)
- Sháněl jsem přednášející do klubu a domlouval termíny. Rozjel jsem takhle asi pět konverzací. V klubu se začaly šířit memy o tom, jak špatně kdo sedí, tak jsem zkusil najít někoho, kdo rozumí ergonomii. Expert, kterého jsem oslovil, nemá bohužel kapacitu, ale třeba najdu někoho jiného.
- Uspořádali jsme v [Atriu](https://www.kafeatrium.cz/) se ženou společnou narozeninovou oslavu pro pár přátel. Myslel jsem, že u lidí, kteří mají děti, se musí počítat s tím, že nepřijdou, protože se z hodiny na hodinu může stát cokoliv. Nakonec, i když to mělo být tak půl na půl, skoro všichni lidi s dětmi dorazili a skoro nikdo bez dětí nedorazil. Takže z toho byla odpolední školka párty, ale užili jsme si to.
- Namontoval jsem žárovky do koupelny.
- Povedlo se mi na Facebook Marketu prodat monitor i se stojanem. Hurá! Několik hodin mi zabralo to celé připravit, natočit video že funguje, najít všechny šroubky.
- Potřebuji teď spát v místnosti, kde je celkem hluk a nemáme tam zatemňovací závěsy. Zjistil jsem, že se mi spí mnohem lépe, když si vezmu takovou tu škrabošku na oči z letadla a špunty do uší.
- Odpovídání v klubu, maily, a tak dále. Udělal jsem v klubu review jednoho celého juniorního projektu.
- Během 11 dní od 20.9. do 30.9. jsem naběhal 41 km. Celkem jsem se hýbal 5 hodin a zdolal při tom 41 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/). Nabídky práce pro juniory teď inzerují: [Credo Ventures](https://junior.guru/jobs/356c084cae33eaaffec2ab9c79fb583f7c1271f730acc612fa2dbfb8/), [Monitora media, s.r.o.](https://junior.guru/jobs/2b1ab731247b03b291bd7c4a0177e052df5ae4a5937144b4f2ce9d11/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/34fa3ec07892dd3ff64458e2ccbf12578e00860483427e9e7c4847bc/)


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Onboarding nových členů: Předělat mazání kanálů, doplnit další tipy.
2. Propagovat [novou kapitolu v příručce](https://junior.guru/handbook/mental-health/) a [epizodu podcastu Street of Code](https://streetofcode.sk/podcast/juniorguru/), kde vystupuju.
3. Vymyslet klubovou soutěž, ve které rozdám knihu [CSS: moderní layout](https://www.vzhurudolu.cz/css-layout/) od Martina Michálka.

**Bonus:** Dát si klid od politiky a od akcí. Zavřít se doma v teplákách, pít čaj, programovat. Všeho teď bylo nějak moc.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Kopeček: Zeman byl dítě z rozvrácené rodiny, Dagmar zachránila Havlovi život, ale škodila jeho pověsti - Prostor X podcast](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BWv2TLXxN0&h=7af2b62a1f6dac13b5c43b26f3ac2b95de714d3eb1e06640f52b39f9facc8faf)<br>Zajímavý pokec o českých prezidentech.
- [Kameny, klacky a desítky obětí: Rozhoří se doutnající konflikt mezi Čínou a Indií?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.voxpot.cz%2Fkameny-klacky-a-konflikt-nejlidnatejsich-zemi-sveta%2F&h=3eaf2079215d5aa36adff41e8d45b57a6eacd41c042fb63c647b1fcdc539e041)<br>Vůbec jsem netušil, že Indie má tolik sporných území se svými sousedy. Neshody s Pákistánem ohledně Kašmíru jsou známé, ale je toho mnohem víc.
- [The kids have killed the reply GIF](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.jwz.org%2Fblog%2F2022%2F09%2Fthe-kids-have-killed-the-reply-gif%2F&h=df114eca588628a0247212928250cb4b8ab2605e9f7c154967da87fbfcc68a14)<br>Gify vyšly z módy.
- [](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.novinky.cz%2Fclanek%2Fkultura-salon-stanislav-biler-brno-hrbitov-verejneho-prostoru-literarni-reportaz-z-cyklu-ceske-bolesti-40409035&h=1c786a2c4408d65e71e0d9ba311ba46479cf180227715d7804b7a277aafd5729)<br>Je to spíš rant jak z nějakého postu na FB, ale pár vět by se tam dalo tesat: „Snižte svou perspektivu do výše očí dětí a náhle přestanete přes hradby aut vidět. Svět zmizí a veškerý výhled zablokují kapoty. Ze světa se stane obludné místo. Něco jako Brno.“ Nebo: „Jsou to hlavně auta, všechna ta auta, co činí veřejný prostor českých měst a maloměst nepoužitelným. Veřejným se stává jen nárazově či omylem. Když se někde něco takzvaně koná. Pivní slavnosti, jarmark, předvolební či protestní setkání. Mě ale zajímá jiný veřejný prostor. Prostor, ve kterém chcete být, protože je příjemný, přestože se v něm vůbec nic neděje. Třeba chodník před domem.“
- [Pražský okruh, vrchol autosocialismu. Silnice kolem měst vůbec nic neřeší](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fpolitika%2F436863-prazsky-okruh-vrchol-autosocialismu-silnice-kolem-mest-vubec-nic-neresi&h=2d8d67d929771c86765163d8f54c83aa9b1818a2a78420636e6a9025126f2f89)<br>Bednár cupuje okruh. „Řada měst, která v minulosti okruhy stavěla, je nakonec raději nedokončila, částečně zbourala, obestavěla novými domy, zakopala je velmi draze pod zem nebo po nich poslala tramvaj.“
- [Byla to prohra, ale stálo to za to, říká po návratu z USA exposlanec Farský. Co se naučil a jak to využije Česko? - Prostor X podcast](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BWv2SuRpn8&h=01f03c4a1f1de28da4de39afae6e3ad228c14b7df5247d7375f515df55e4e44c)<br>Ukecaný, ale zajímavý rozhovor.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
