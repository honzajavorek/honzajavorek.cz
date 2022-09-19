Title: Týdenní poznámky #105: Zlínsko a nástěnka
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (13.9. — 19.9.) a tak [stejně jako minule]({filename}/2022-09-12_tydenni-poznamky-104-vsechno-mozne.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Byli jsme u babičky a pořád pršelo, takže jsem měl spoustu času na práci a všechno, co jsem si minule vytyčil, se mi povedlo. Moc jsem se ani neúčastnil kampaně a pro klid duše moc nečetl ani sociální sítě, pokud šlo o politiku.

I když jsem se neubránil a na FB skupinu obce, kde babička bydlí, jsem vznesl dotaz ohledně křižovatky a přechodů, který v předvolební atmosféře nakonec vyústil v 50 komentářů :D Překvapivé pro mě bylo, že ač má v obci auto každý, většina komentujících chtěla zklidnit dopravu, víc přechodů, nebo dokonce cyklostezku napříč obcí. Reakce vedení byly zase převážně o tom, že rekonstrukce jedné ulice jsou miliony korun a ty obec nemá kde vzít, takže se musí hlásit na dotace a pokud žádné na tento typ investic vypsané nejsou, nebo je obec nedostane, nemohou nic dělat. Jsem laik, ale za mě: Něco dělat mohou (dočasná opatření, která moc nestojí a hotová jsou hned, viz pražské montované obrubníky nebo zelené balisety) a stav, kdy obec nemá na vlastní rozvoj, je tragický a jako hlavní příčinu vidím směšnou daň z nemovitosti.

[Kozojedská desítka](https://www.facebook.com/events/340873144838343) byla fajn a i když jsem měl skoro stejný čas jako před dvěma lety, mnohem lépe jsem si rozložil síly a v závodě jsem neumíral, ale užil jsem si ho. Překvapilo mě, že tempo jsem měl dost pomalé a sotva jsem se držel prošedivělého pana Leoše. Asi nemám naběháno moc kopců, takže mě ničily. To bych měl zlepšit. A taky bylo všude hodně bahna a já byl asi moc opatrný.

## Peníze!

Všiml jsem si, že jsem dosáhl rodinného cíle a můj čistý měsíční příjem se [poprvé vyšplhal na závratných 40.000 Kč](https://twitter.com/honzajavorek/status/1569640794931306497). Jupí! Trvalo to jen tři roky od začátku podnikání. Z velké části mohu děkovat novému ceníku.

## Adresy a přesměrování

Ceník je stále v Google dokumentu, ale napadlo mě, že bych si pro něj mohl vytvořit nějakou hezčí adresu.

Udělat redirect na webu, který nemá backend, znamená přečíst si [dokumentaci Googlu](https://developers.google.com/search/docs/crawling-indexing/301-redirects) a využít starý dobrý meta refresh. Podle dokumentace je okamžitý meta refresh považován za permanentní redirect, ale pokud je tam prodleva, bere se jako dočasný. Já pro ceník vybral adresu [junior.guru/pricing](https://junior.guru/pricing) a jednou bych tam třeba ceník mít opravdu chtěl, takže jsem tam chtěl dočasné přesměrování.

Koukal jsem zase na [mkdocs-redirects](https://github.com/mkdocs/mkdocs-redirects), ale pak jsem si řekl, že přece stačí vytvořit jinou hlavní šablonu, dát do ní potřebné značky a použít ji pak v dokumentu pomocí `template`. Tak jsem to i vyřešil.

Chvíli jsem zápasil s tím, že redirect by měl mít absolutní URL a to jsem v kódu zatím nikde nepotřeboval, ale udělal jsem si na to v jinja2 filtr `absolute_url` a vyřešil to celkem rychle.

Když už jsem se patlal s redirecty, hecnul jsem se a zkusil přesunout jednu z prapůvodních stránek příručky do chlívku „handbook“, ve kterém bych je jednou chtěl všechny mít. Vybral jsem tu, která má nejmenší návštěvnost (a paradoxně největší důležitost pro úspěch juniora, lol), tedy `/practice/` a přesunul jsem ji na `/handbook/practice/`, opět pomocí redirectu s meta refresh, tentokrát ale permanentního. Uvidím, jakou škodu tím natropím, třeba v SEO, a poté začnu postupně opatrně přesunovat i další původní stránky, jako jsou `/motivation/`, `/learn/`, nebo `/candidate-handbook/`.

## Pravidla klubu

Chtěl jsem napsat další tip pro onboarding nových členů a vysvětlit v něm systém rolí v klubu. Jenže rolí už máme hodně a vysvětlení bylo strašně dlouhé a nepřehledné. Tak jsem se rozhodl udělat něco, co jsem na později stejně plánoval - překopat to, jak v klubu vypadají tzv. „pravidla“.

Na Discordu je hned několik míst, kam se dají pravidla dávat. Např. uvítací obrazovka, kterou jsem taky prošel a změnil, ale hlavně kanál, který admin označí, že v něm pravidla jsou a ten pak dostane speciální ikonku. Ve stávajících pravidlech jsem popisoval hodně věcí, které by teď měly vysvětlovat tipy pro nováčky. V plánu jsem tedy měl celý kanál změnit na něco, co bude spíš sloužit jako místo s permanentními infomacemi, které je dobré mít stále po ruce. Přejmenoval jsem ho na #nástěnka a místo ručně psané zprávy jsem nechal celý obsah kanálu spravovat bota.

Ten tam dává a aktualizuje hned několik zpráv: základní tipy, seznam a popis rolí v klubu, seznam firem spolupracujících s klubem, seznam odkazů na záznamy klubových akcí a pak nějaké drobné info ze zákulisí klubu, např. odkaz na moje poslední týdenní poznámky, počet členů v klubu, odkaz na kód na GitHubu, na statistiky, atd. Vyrobení tohoto kanálu, se vším všudy, mi zabralo většinu týdne.

Snažil jsem se, aby tam byly fakt jen věci, které je dobré mít při ruce a lidé budou vědět, kde je najdou, když je budou hledat. Málokdo chodí z Discordu na web a zpět, takže dát takové věci jen na web není vždy řešení. Mít vše v nějakých opakujících se zprávách nebo připnutých příspěvcích, které nikdo nikdy neobjeví, také není ideální. Pro každou informaci se ale hodí trochu jiná forma, takže jsem rád, že teď mám v klubu forem hned několik (kanál s oznámeními, nástěnka, opakující se zprávy, tipy pro nováčky, web…) a mohu vždy vybrat tu ideální pro daný případ.

Při vytváření nástěnky jsem zjistil, že Discord umožňuje mít v tzv. embedech u jedné zprávy v součtu pouze 6000 znaků, takže jsem nakonec musel jednotlivé sekce nástěnky rozsekat do více zpráv.

## Nefunkční suppress

S jásotem jsem sice objevil parametr `suppress` při posílání a editaci zpráv, který zabrání načtení obrázků pro URL vložené ve zprávě, ale pak mi záhy spadlo CI a z chyby bylo patrné, že při posílání zpráv ten parametr neexistuje. To bylo podezřelé, ale na GitHubu pycordu [mi vysvětlili](https://github.com/Pycord-Development/pycord/pull/1587#issuecomment-1245961350), že tahle pár dní stará funkce ještě není ani v nejnovější verzi.

Protože u editace to funguje, pokrčil jsem rameny a přidal v kódu druhý řádek, který po odeslání zprávy tutéž zprávu hned edituje a obrázky potlačí. Třeba to jednou půjde najednou. Na to, jaká je to blbost, už jsem s tímhle strávil fakt hodně času. Je to fascinující :)

## Oslovování firem

Jak jsem měl v plánu, oslovil jsem všechny firmy, kterým má končit spolupráce s klubem. Některé už se ozvaly, že chtějí pokračovat, některé se ozvaly, že pokračovat neplánují. Jsem zvědav, jak to celé dopadne!

Někde jsem doháněl staré resty, třeba u aktualizace [inzerátu pro Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), kde jsme chtěli upravit pár vět. U jedné firmy jsem se připomenul s tím, že stále nedodali svůj inzerát, ale ujistili mě, že mám být v klidu, vědí o tom a jakmile budou mít vymyšlenou strategii, uděláme, co bude potřeba. A že se jim líbí co dělám a rádi JG podporují.

## Domlouvání přednášek

Ozval jsem se pár lidem s tím, zda by neměli chuť udělat pro klub přednášku. U jednoho člověka jsem si dokonce všiml, že jsme ji měli i naplánovanou, a to na 20.9. Což jsme oba úplně zazdili, škoda. Přeplánujeme, doladíme. Každopádně se snažím opět přednášky nějak rozjet a je to na dobré cestě.

## Další poznámky

- Pozvali mě na jednu startupovou party a asi tam půjdu. Pozvánka byla vyrobená přes něco, co se jmenuje [lu.ma](https://lu.ma/). Protože mě překvapilo, jak příjemně se na party registrovalo, využil jsem to hned při organizaci vlastních narozenin.
- Opět chtěl někdo platit jinak než kartou a posílal jsem odpověď, že to nejde. Musím to už dát aspoň do [FAQ](https://junior.guru/faq/), ať to nevymýšlím pokaždé znova a mohu jen poslat odkaz. Je to jediná věc, která je opravdu častý dotaz a nemám ji v častých dotazech :D
- Občas spadlo CI kvůli nějaké prapodivné chybě při stahování nabídek práce. Zřejmě to trvalo moc dlouho, nebo to možná jen dlouho nic nepsalo do konzole, jelikož jsem měl v logu hodně debug výpisů a málo info výpisů, ale na CI je zapnuté jen info. Trochu jsem to poladil a uvidím, co se bude dít.
- V některých zprávách se začal projevovat bug s cachováním u Discord klientů, který už znám, ale myslel jsem, že v textu zpráv se neprojevuje. Našel jsem toto [issue](https://github.com/discord/discord-api-docs/issues/2126) a tam je vysvětlené, že se to může stát u kterékoliv mention, i v textu, pokud není notifikující. To vysvětluje ono podivné chování. Zároveň je to _wontfix_, takže to Discord ani nehodlá opravit. Zajímavé.
- Na sociální sítě jsem pomáhal Engetu sdílet [výzvu, aby k nim lidi šli lektorovat](https://engeto.cz/spoluprace/?utm_source=ext-jg).
- Jeden večer jsem se zamýšlel nad tím, co s nimi do budoucna. Pročítal jsem si [Markeťákův průvodce po sociálních sítích](https://duckduckgo.com/?t=ffab&q=+Marke%C5%A5%C3%A1k%C5%AFv+pr%C5%AFvodce+po+soci%C3%A1ln%C3%ADch+s%C3%ADt%C3%ADch+site%3Amediaguru.cz&ia=web), abych měl lepší představu o tom, co od které sítě čekat a nezakládal to jen na svých předsudcích, nebo své bublině. Chtěl bych se časem hlavně rozhodnout, které sítě vynechám a vůbec na nich nebudu, protože to dává nejmenší smysl. Závěry zatím nemám.
- Pája natočila [nový díl podcastu](https://junior.guru/podcast/) a bot o tom napsal do klubu. Akorát když se na to hned klikne, člověk díl nevidí, jelikož bot ještě nedokončil svou práci a nepublikoval novou verzi webu s novou epizodou. Opravil jsem to zatím jen tím, že jsem změnil texty u zprávy, kterou bot posílá a napsal tam, že díl se objeví do půl hodiny.
- Discord konečně umožnil běžným smrtelníkům používat tzv. [fóra](https://www.youtube.com/watch?v=y4MxuHNIIg0), speciální kanály, kde se dají zakládat vlákna jako ve fóru a se spoustou dalších užitečných funkcí. Přesně to se nám bude hodit na poradnu, ale zatím jsme to jen s Danem zkoumali a zjišťovali, jak přesně to funguje. Než to v klubu zapnu, budu muset naučit bota jak s tím pracovat a vymyslet, jaký tam bude panovat režim.
- Klub, maily, a tak dále. Vyřešil jsem dvě stipendia. U jednoho jsem se doptal na informace a nedostal odpověď. Jedno jsem udělil.
- Během 7 dní od 13.9. do 19.9. jsem naběhal 28 km, při procházkách nachodil 3 km, ujel na kole 19 km. Celkem jsem se hýbal 8 hodin a zdolal při tom 50 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Pracovat dál na onboardingu nových členů do klubu.
2. Plánovat přednášky v klubu.
3. Kampaň, párty, pivo s kamarádem, narozeniny…


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Jan Žižka v novém filmu není Čech a vlastenec. Jak to stráví zdejší publikum?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.kinobox.cz%2Fclanek%2F22613-jan-zizka-vnovem-filmu-neni-cech-a-vlastenec-jak-to-stravi-zdejsi-publikum&h=b87dd28d996e1a82e50f1b1f7856503368b1af63166833be0975c8be7a625d92)<br>Zajímavý komentář k novému filmu.
- [Brněnský rekord v počtu mrtvých a těžce zraněných chodců není náhoda, ale důsledek nečinnosti](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2022%2F09%2Fbrnensky-rekord-v-poctu-mrtvych-a-tezce-zranenych-chodcu-neni-nahoda-ale-dusledek-necinnosti%2F&h=11500fa5504d2f816dc8c86e0bc4b5bf3f741458f10ac9339e5ddf43a2340157)<br>Smutný příběh města, které jsem míval rád. Posledních několik návštěv pro nás - chodce s kočárkem - bylo spíš peklíčko.
- [Praha je centrem postkomunismu, u volebních uren uctívá minulost](https://getpocket.com/redirect?&url=https%3A%2F%2Fnazory.aktualne.cz%2Fkomentare%2Fpraha-je-centrem-postkomunismu-ve-volbach-uctiva-minulost%2Fr%7Edcfccbcc32da11eda25a0cc47ab5f122%2F&h=71bbed3a44cc5eb8f4898d611d314c0b5e5d64806ad70e02c42ca14b4501fcdf)<br>„Je pravicový, jeho strana vystupuje proti Babišovi, komunistům a Putinovi - tím pádem má rád svobodu a demokracii. Je dobrým kandidátem, bez ohledu na to, co konkrétního říká nebo dělá.“
- [An Unarmed Putin Wants a Culture War With the West](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.bloomberg.com%2Fopinion%2Farticles%2F2022-09-14%2Fan-unarmed-putin-wants-to-fight-a-culture-war-with-the-west&h=c68e1356a3555655fe0494e7ce0e8230c25c031f46ef8c65a12be69a237a2836)<br>„Putin’s Russia has produced few, if any, cultural products of note. In a world far more receptive to non-English entertainment, there are no famous Russian soap operas, no R-Pop craze. Rollywood isn’t a thing.“
- [„Bez vůdce to nejde.“ Omyl, který se o Ukrajině šíří Západem, připomíná expertka](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.voxpot.cz%2Fbez-vudce-to-nejde-omyl-ktery-se-o-ukrajine-siri-zapadem-pripomina-expertka%2F&h=f214ac32663b3bbde00a65a4af156c54fbc3c5d1bb669513d0976e4e81837196)<br>Důvod, proč (jako jiní) nenosím Zelenského na tričku – demokracie nemá černobílých hrdinů.
- [Vysílač](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2Blh3Lggi54&h=5ebcd9978dfb71bd11dec83035018fa35252928568a69e089742cb3200128fdd)<br>Díl o konunálních volbách - smysl, co se řeší, jak významný bývá starosta, politické strany, atd.
- [Pod čarou : Hra na dospělost nemá smysl. Mileniálové na to přišli jako první.](https://getpocket.com/redirect?&url=https%3A%2F%2Fseznam-zpravy.u.mailkit.eu%2Fmc%2FVVQWVPLV%2FUABNPZPTQVAWHKJBJR%2FCCLPUCLPIMP&h=c8e2c9f20609f00cf729caa61625d120a5f9e91bf34a767d83e5a7451675b728)<br>„Pokud dřina v kanceláři k ničemu nevede, je možná lepší trávit čas víc v klidu věcmi, které člověka baví (bez ohledu na věk), a v nejisté situaci je prostě potřeba přijmout jiné životní strategie.“
- [#18 - Stanou se geneticky upravené hyperinteligentní děti normou?](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BjBlMsFdhE&h=9bc1b4cd85170bb37d943ea90e8a04de3ea937cc570e341e8e89bcb4993c0382)<br>Celkem husté, co dnes vlastně už umíme. Dokážeme modifikovat lidi, ale chybí nám k tomu etika a vůbec netušíme, co to muže všechno spustit.
- [Kopeček: Zeman byl dítě z rozvrácené rodiny, Dagmar zachránila Havlovi život, ale škodila jeho pověsti - Prostor X podcast](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BWv2TLXxN0&h=7af2b62a1f6dac13b5c43b26f3ac2b95de714d3eb1e06640f52b39f9facc8faf)<br>Zajímavý pokec o českých prezidentech.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
