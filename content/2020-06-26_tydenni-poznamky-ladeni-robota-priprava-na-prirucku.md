Title: Týdenní poznámky: Ladění robota, příprava na příručku
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158248549477707
Twitter-Comments: https://twitter.com/honzajavorek/status/1277587291670749184


Utekl další týden (22.6. — 26.6.) a tak [stejně jako minule]({filename}/2020-06-19_tydenni-poznamky-cisla-a-e-maily.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


Tento pracovní týden jsem si vzal v pátek dovolenou a odjel kamarádům na svatbu, takže poznámky jsem začal psát v neděli večer a dopsal až v pondělí 29.6.


## Pondělní odpadnutí

V pondělí na začátku týdne (22.6.) jsem neudělal vůbec nic, protože mi nebylo dobře a celý den jsem prospal. Takže jsem tento týden vlastně odpracoval jen tři dny z pěti.

Měl jsem asi nějaký obří spánkový deficit a cokoliv jsem si ten den přečetl, zpětnou vazbu, e-mail atd., tak jsem to vnímal strašně negativně a byl jsem celkově hodně skleslý. Měl jsem dojem, že vše co dělám je nesmysl, že celé JG je hloupost, kterou jsem si vycucal z prstu a ekonomicky nikdy nemůže fungovat, akorát na něm propálím hromadu času a peněz. Přitom postupně se ozubená kolečka stroje na peníze roztáčet začínají, ale jde to pomalu, protože spousta firem má hiring freeze, a nějak to na mě v to pondělí dopadlo.

Naštěstí jsem rozpoznal, že to je asi celé jen únavou, a na žádný e-mail raději neodpovídal. Když jsem se tomu věnoval o den později, hezky vyspaný a čerstvý, vše jsem viděl úplně jinýma očima, mnohem pozitivněji.

**Poučení:** Nedostatek spánku strašně ovlivňuje vitalitu a psychiku přes den, a když je celý svět kolem vás na hovno, je velká pravděpodobnost, že za to nemůže ten svět, ale vaše hlava. V takovém případě je lepší nic nedělat, už vůbec ne to lepit nějakým kafem, ale prostě to jít dospat a některé věci raději dělat úplně jiný den. Když už mám tu svobodu, že nemám šéfa a termíny a nemusím nikam chodit.


## Ladění robota

Vrátil jsem se po delší době k [robotovi, který stahuje nabídky práce odjinud](junior.guru/jobs/#jobs-bot). Ladil jsem kritéria, která rozhodují o tom, zda se nabídka dostane do výpisu, nebo se zahodí, protože je moc seniorní. Jednak jsem opravil pár chyb v detekci, jednak jsem se snažil vyřešit, aby bylo méně _false negatives_, tedy juniorních nabídek, které neprojdou. Robot byl moc přísný.

Problém byl hlavně s nabídkami, o kterých nedokázal nic moc zjistit. Pokud zdetekoval méně než dva příznaky, nastavil jsem jej tak, že to vyhodnotil jako nulu a inzerát neprošel. Bál jsem se, aby se tam neobjevovaly špatně vyhodnocené seniorní inzeráty jen proto, že robot omylem vyhodnotí jeden příznak, a ten bude mít pro nedostatek dalších příznaků příliš velkou váhu. Prostě jako kdyby film na ČSFD měl 100%, ale hodnotili ho jen dva lidi.

Vyřešil jsem to nakonec tak, že se málo příznaků nevyhodnocuje automaticky na nulu, ale umenšuje se chytře váha různých příznaků a zdá se mi, že to teď celkem funguje. Je dobře, že jsem to předtím neřešil a raději zahodil víc inzerátů. Teď jsem aspoň viděl jak se to chová a mohl jsem to už jen podle toho doladit.


## Další ladění e-mailů

- Odpovídal jsem e-mailem na ohlasy, které přišly jako odpovědi na pondělní automaticky rozesílané statistiky pro inzerenty. Dolaďoval jsem podobu e-mailů a jejich text.
- Dodělal jsem expiraci inzerátů a výzvu k jejich prodloužení přidal do pondělních e-mailů se statistikami. Netrvalo mi to [15 minut jako Levelsovi](https://mobile.twitter.com/levelsio/status/1190169746408267776), spíš půl roku, ale mám to!
- Protože šablona na e-maily už začínala být plná ifů a elsů, napsal jsem raději testy, abych lidem neposílal nesmysly.


## Příprava navigace na příručku

Abych mohl vydat příručku, potřebuji ji nějak zasadit do designu stránek a hlavně vyřešit navigaci mezi stránkami a třeba i mezi odstavci. Udělal jsem tedy několik návrhů, jak by to mohlo fungovat, a potom jsem se jal překopávat hlavičku. To hlavní, co jsem udělal, byl její přepis do samostatné komponenty v BEMu, aby to nebyly špagety, a dalo se v ní vůbec něco měnit. Taky bylo menu doteď dělané dost "ručně", tak jsem ho předělal, aby se automaticky generovalo z kódu.

Jako vedlejší efekt jsem změnil způsob, jakým se menu zmenšuje na mobilech. Pořád ještě nevedu "hamburger", ale místo aby se tři odkazy zmenšily na čísla 1 2 3, udělal jsem to tak, aby tam byl vždy text, byť třeba kratší. Takže místo "Nauč se základy" se objeví jen "Základy", apod. Patlal jsem se s tím celé čtvrteční odpoledne, aby to menu bylo hezké na všech zařízeních. V dalších týdnech chci ve změnách navigace pokračovat.


## Další poznámky

- Uzavíral jsem obchody a vystavoval jsem faktury, jupí!
- [Upravil jsem skript na kontrolu nefunkčních odkazů](https://github.com/honzajavorek/junior.guru/commit/918a3becdeae3814652225ab2af569b87dd86781) tak, aby mi na konci vypisoval shrnutí. Bylo to rychlejší a jednodušší, než jsem myslel a nemusím už řešit/čekat na [tohle staré issue](https://github.com/stevenvachon/broken-link-checker/issues/169).
- Opravil jsem nějaké nefunkční odkazy.
- Odebral jsem dolní pruh s prosbou o příspěvek z hlavní stránky JG a ze stránky o zpracování osobních údajů.
- Odblokovali mi Instagram, hurá.
- Napsal jsem jedné internetové celebritě, jestli se mnou nechce v jedné konkrétní věci spolupracovat na JG.
- Přidal jsem UTM parametry i do odkazů, které vedou z inzerátů na stránky firem.
- Zjišťoval jsem, kolik stojí tisk vizitek. Občas by se mi hodily, vysoko postavené lidi ve velkých firmách se moc nehodí oslovovat se samolepkou v ruce.
- Opravil jsem pár chyb v CSS.
- [ImprovMX](https://improvmx.com) si z ničeho nic začal stěžovat, že moje domény jsou špatně nastavené, přitom při kontrole `MX` záznamů jsem žádný problém neviděl. Pak jsem si všiml, že tam něco (nově?) píšou i o `TXT` záznamu. Doplnil jsem ho a časem mi napsali, že je vše OK. Tuto změnu jsem [zmínil i v README pro JG](https://github.com/honzajavorek/junior.guru/commit/66a124fcbfc320058ad1d97e4a71e5d0ea50eee4).
- Vyřešil jsem dilema s _circular imports_ s Peewee modely a prostě dal věci, které na sebe potřebují odkazovat, do jednoho souboru. [Šílenost, kterou jsem vymyslel předtím](https://stackoverflow.com/a/62404730/325365), jsem odstranil.
- Po víkendové svatbě v lese, kde se bubnovalo a mluvilo o slunovratu a svatojánské magii, jsme si v neděli konečně pustili [Slunovrat](https://aerovod.cz/katalog/slunovrat). Dokonale natočené a fakt zajímavý film, ale jak se běžně zcela vyhýbám hororům, tak bude asi ještě chvíli trvat, než některé obrazy vyženu z hlavy a než se to nějak vstřebá. Rozhodně asi nebyl dobrý nápad si to pustit akorát před spaním.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Minulý i tento víkend jsem hodně cestoval, tak jsem toho i hodně přečetl. Od posledních poznámek jsem sdílel toto:

- [UTC is Enough for Everyone, Right?](https://getpocket.com/redirect?&url=https%3A%2F%2Fzachholman.com%2Ftalk%2Futc-is-enough-for-everyone-right&h=39ec219b5b7ee28aa1ff4746d34436bc2207f3d906b15412ccc97b27af4d8e40)<br>Hezké shrnutí toho, na co si dávat pozor při práci s časem na webu
- [Všechno zrušit?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.jestevetsikritik.cz%2Fkomentare%2F1045-vsechno-zrusit&h=b2e1735f4960e13d1b41487d1a36afb7a3f156d9267add5c1a0cdb940e144446)<br>Poctivý rozbor toho, proč teď některá díla mizí z Netflixu a spol.
- [Brňan jedl v rámci sázky půl roku guláš, litovat začal velmi brzy](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.novinky.cz%2Fmuzi%2Fclanek%2Fbrnan-jedl-v-ramci-sazky-pul-roku-gulas-litovat-zacal-velmi-brzy-40328132%23seq_no%3D5%26source%3Dhp%26dop_ab_variant%3D298111%26dop_req_id%3DGBm5qgdwUXT-202006191809%26dop_source_zone_name%3Dnovinky.sznhp.box%26utm_source%3Dwww.seznam.cz%26utm_medium%3Dz-boxiku%26utm_campaign%3D&h=9948b49febb67d8d06a76b2490034dd15145e24cd5a73047a360084de5a1e34f)<br>Nejlepší rozhovor
- [The Return of the 90s Web](https://getpocket.com/redirect?&url=https%3A%2F%2Fmxb.dev%2Fblog%2Fthe-return-of-the-90s-web%2F&h=3f89706f184c646e45987ae56a647b8c7f12772a80d83658a96080e01da8653e)<br>Dělal jsem věci zastaralým způsobem tak dlouho, že začaly být zase v kurzu!
- [Šest zlidovělých figur českého antifeminismu](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikreferendum.cz%2Fclanek%2F31353-sest-zlidovelych-figur-ceskeho-antifeminismu&h=9d53479e237ac47aca164c67466c679187596e8040751833b7ce038415647549)<br>Vrátný pobavil hodně - a osobně se divím, že je figur jen šest, napadají mě i další
- [Praha bez turistů: místo pomočeného vnitrobloku rajčata na pavlači a obavy, co bude dál](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2020%2F06%2Fpraha-bez-turistu-misto-pomoceneho-vnitrobloku-rajcata-na-pavlaci-a-obavy-co-bude-dal%2F&h=5fc866706646f36b6531026fddc89eb76f924aa1f63fb9ddd10fa61274245651)<br>Život na Praze 1 v době, kdy zmizeli turisti
- [Amerika nestaví chodníky. Ještě by po nich chodili černí](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2F9XAxc33FXm%3Fssr%3Dtrue&h=616c81bf8e2b8487dd60c62fa818048a066a0d6b537459df0a2089d750f5f899)<br>Průlet systematickým rasismem a segregací v USA
- [Vydali jsme se špatnou cestou, vládě chybí jasná strategie, kritizuje rektorka Nerudová půlbilionový deficit](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.irozhlas.cz%2Fzpravy-domov%2Fekonomika-deficit-koronavirus-schodek-schillerova-babis-investice-nerudova_2006210700_sto&h=434a1bed93f00e3a70687a675e9731570c9c1bece568373a993c615221c2bb99)<br>Jinde hotovost poskytli a teprve zpětně zkoumali, zda subjekt splnil podmínky. Pokud nesplnil, byla to půjčka, když splnil, byl to grant.
- [Black Lives Matter znamená, že záleží i na životech Romů](https://getpocket.com/redirect?&url=https%3A%2F%2Fwave.rozhlas.cz%2Fblack-lives-matter-znamena-ze-zalezi-i-na-zivotech-romu-8222178&h=6373126faecac46a6a190b45623a143528a3e8a393b87cd2e5ba94619c105183)<br>Diverzita se u nás dělá tak, že se mezi bílé zamíchají černí. Ve skutečnosti bychom ale měli do života přimíchávat Romy.
- [Always bet on HTML](https://getpocket.com/redirect?&url=https%3A%2F%2Fgomakethings.com%2Falways-bet-on-html%2F&h=97296f23847d61b4e134a36c2f266ccb1fe34501dc76ea7aa6e401a9bcffcad9)<br>Velkej souhlas
- [Čechům není výměna slova master v Gitu srozumitelná, říká Petr ‚Pasky‘ Baudiš](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2FQZDfvgWmbr%3Fssr%3Dtrue&h=c2f53856757c3c74da933b5a64ddf559ac74470d560151d5532078cd00bcdfb4)<br>Rozhovor s Petrem, který byl u vzniku Gitu, o tom, jak je to s tím “master”
- [On Four Types of Development Companies](https://getpocket.com/redirect?&url=https%3A%2F%2Falmad.blog%2Fnotes%2F2020%2Fon-four-types-of-dev-companies%2F&h=69ce0a5c6bd36d0a1249a419b27cb91ff64d7a1a9cc4c772e866923ebf366f07)<br>Typy IT firem podle toho, jakým způsobem pracují. Lukáš toto dělení zmínil už dříve v přednášce, čímž mě inspiroval, abych toto téma rozebral v připravované příručce pro juniory. To zase inspirovalo jeho k tomu, aby to sepsal do článku na blog :) Prostě — kvalitní materiál, čtěte!
- [V Čestlicích hořel vůz s elektrickým pohonem. Hasiči vložili auto na několik dní do kontejneru s vodou](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.irozhlas.cz%2Fzivotni-styl%2Fauto%2Fpozar-elektromobilu-praha-skoda-dva-miliony-korun_2006250738_vin&h=7dceee898498f41e07ec582d17f659ffe40f54a36b80a229c2800aef44a53660)<br>Jak se hasí elektromobil
- [Práce v IT na volné noze](https://getpocket.com/redirect?&url=https%3A%2F%2Fnavolnenoze.cz%2Fblog%2Fit%2F&h=09e0d38597a78e47c0e632381b5766bdd2364b50f5541d82800ac738ec4ea060)<br>Vše o práci v IT na volné noze — super článek! Typy firem, projektů, jak a co, ceny, práce na dálku, korporace…

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
