Title: Týdenní poznámky: Ladění robota, příprava na příručku
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158248549477707
Twitter-Comments: https://twitter.com/honzajavorek/status/1277587291670749184


Utekl další týden (22.6. — 26.6.) a tak [stejně jako minule]({filename}2020-06-19_tydenni-poznamky-cisla-a-e-maily.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

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

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Minulý i tento víkend jsem hodně cestoval, tak jsem toho i hodně přečetl. Od posledních poznámek jsem sdílel toto:

- [UTC is Enough for Everyone, Right?](https://zachholman.com/talk/utc-is-enough-for-everyone-right)<br>Hezké shrnutí toho, na co si dávat pozor při práci s časem na webu
- [Všechno zrušit?](https://www.jestevetsikritik.cz/komentare/1045-vsechno-zrusit)<br>Poctivý rozbor toho, proč teď některá díla mizí z Netflixu a spol.
- [Brňan jedl v rámci sázky půl roku guláš, litovat začal velmi brzy](https://www.novinky.cz/muzi/clanek/brnan-jedl-v-ramci-sazky-pul-roku-gulas-litovat-zacal-velmi-brzy-40328132#seq_no=5&source=hp&dop_ab_variant=298111&dop_req_id=GBm5qgdwUXT-202006191809&dop_source_zone_name=novinky.sznhp.box&utm_source=www.seznam.cz&utm_medium=z-boxiku&utm_campaign=)<br>Nejlepší rozhovor
- [The Return of the 90s Web](https://mxb.dev/blog/the-return-of-the-90s-web/)<br>Dělal jsem věci zastaralým způsobem tak dlouho, že začaly být zase v kurzu!
- [Šest zlidovělých figur českého antifeminismu](https://denikreferendum.cz/clanek/31353-sest-zlidovelych-figur-ceskeho-antifeminismu)<br>Vrátný pobavil hodně - a osobně se divím, že je figur jen šest, napadají mě i další
- [Praha bez turistů: místo pomočeného vnitrobloku rajčata na pavlači a obavy, co bude dál](https://a2larm.cz/2020/06/praha-bez-turistu-misto-pomoceneho-vnitrobloku-rajcata-na-pavlaci-a-obavy-co-bude-dal/)<br>Život na Praze 1 v době, kdy zmizeli turisti
- [Amerika nestaví chodníky. Ještě by po nich chodili černí](https://t.co/9XAxc33FXm?ssr=true)<br>Průlet systematickým rasismem a segregací v USA
- [Vydali jsme se špatnou cestou, vládě chybí jasná strategie, kritizuje rektorka Nerudová půlbilionový deficit](https://www.irozhlas.cz/zpravy-domov/ekonomika-deficit-koronavirus-schodek-schillerova-babis-investice-nerudova_2006210700_sto)<br>Jinde hotovost poskytli a teprve zpětně zkoumali, zda subjekt splnil podmínky. Pokud nesplnil, byla to půjčka, když splnil, byl to grant.
- [Black Lives Matter znamená, že záleží i na životech Romů](https://wave.rozhlas.cz/black-lives-matter-znamena-ze-zalezi-i-na-zivotech-romu-8222178)<br>Diverzita se u nás dělá tak, že se mezi bílé zamíchají černí. Ve skutečnosti bychom ale měli do života přimíchávat Romy.
- [Always bet on HTML](https://gomakethings.com/always-bet-on-html/)<br>Velkej souhlas
- [Čechům není výměna slova master v Gitu srozumitelná, říká Petr ‚Pasky‘ Baudiš](https://t.co/QZDfvgWmbr?ssr=true)<br>Rozhovor s Petrem, který byl u vzniku Gitu, o tom, jak je to s tím “master”
- [On Four Types of Development Companies](https://almad.blog/notes/2020/on-four-types-of-dev-companies/) Prostě — kvalitní materiál, čtěte!
- [V Čestlicích hořel vůz s elektrickým pohonem. Hasiči vložili auto na několik dní do kontejneru s vodou](https://www.irozhlas.cz/zivotni-styl/auto/pozar-elektromobilu-praha-skoda-dva-miliony-korun_2006250738_vin)<br>Jak se hasí elektromobil
- [Práce v IT na volné noze](https://navolnenoze.cz/blog/it/)<br>Vše o práci v IT na volné noze — super článek! Typy firem, projektů, jak a co, ceny, práce na dálku, korporace…

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
