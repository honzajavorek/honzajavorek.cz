Title: Týdenní poznámky #52: Špendlíky a další vylepšení klubu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (24.5. — 28.5.) a tak [stejně jako minule]({filename}/2021-05-21_tydenni-poznamky-51-psani-textu-a-komunita.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Vylepšování klubu

Tento týden jsem chtěl na delší dobu završit zvelebování klubu, abych se posléze přesunul zase zpátky k webu, pracovním nabídkám, příručce. Prošel jsem si nápady, které mám v záloze a vyšly mi z toho hlavně dvě věci.

Špendlíky. Někoho napadlo, že by se mohlo připínat v kanálech víc příspěvků, aby se k nim šlo vracet a viděli zajímavé věci i noví lidi, kteří přijdou. Jenže já nevím, co je pro většinu členů tímto způsobem zajímavé. Nakonec jsem to udělal tak, že když má nějaký příspěvek hodně emoji se špendlíkem, bot příspěvek připne. Jenže proč by to dělali, že? Pouze vyhlídka toho, že příspěvek se možná připne, to nestačí. Chtěl jsem, aby to mělo i nějakou hodnotu pro každého daného člověka. A to už byl jen krok k tomu, abych vymyslel, že když dá člověk špendlík na příspěvek, bot mu jej uloží do soukromých zpráv. Člen, který si takto něco připíchne, z toho přímo sám benefituje, může si ukládat zajímavé příspěvky a vracet se k nim, zároveň pokud to udělá hodně lidí (procento z počtu členů v klubu), příspěvek se připne pro všechny. Podle mě ideální synergie individuálně užitečné funkce s komunitně užitečnou funkcí, fakt se mi to líbí, ale uvidíme, jak se to uchytí. Při tvorbě této funkce jsem udělal vtipnou chybu - když se to poprvé pustilo, poslalo to soukromou zprávu, kde bylo každé písmenko na svém vlastním řádku :D Ale už to je opraveno.

Další věc byla automatické posílání pozvánek na Pyvo a na srazy Frontendistů. To by nebylo nic moc složitého, oba srazy mají iCal feed, který by šlo načíst, zpracovat, ládovat budoucí srazy do kanálu. Jenže když jsem si dělal úvodní analýzu a přemýšlel, jak to vyrobím, došlo mi, že je to celé mnohem složitější. Srazy jsou původně vázané na různá města, Brno, Praha, Plzeň, atd. Tak je to u Pyva i Frontendistů. To, že nyní probíhají online, je přechodný stav. Můj klub je online a lidi v něm jsou ze všech koutů republiky. Někteří nikdy nebudou moci jen tak přijít na nějaký sraz v Praze nebo Brně. Posílat všechny srazy do nějakého kanálu by bylo irelevantní pro velkou část členů. Upozornění na sraz v Praze hezký, ale zajímavé pro 10 lidí. V Brně? Zajímavé pro 5 lidí. Cílem klubu je vyloženě být online komunitou pro začátečníky, kteří kolem sebe komunitu nemají. Pro ty, kteří nemohou snadno dojít na sraz, ať už kvůli rodinnému životu nebo tomu, že jsou z vesnice. Pozvánkami na prezenční akce bych vlastně podrýval smysl celého klubu. Proto jsem tuto funkci nakonec zavrhl. Do budoucna bych to viděl tak, že bych tam klidně agregoval online akce, ale prezenční spíš ne. Budu to muset produktově lépe promyslet. Každopádně bude strategičtější si počkat i na to, jak se srazy vyvinou do budoucna a tuto funkci řešit třeba až uvidím, jak to funguje napodzim a ne teď nebo v létě.

Dále jsem zase trochu přeuspořádal kanály v klubu podle toho, jak je lidé používají, založil nové, aktualizoval pravidla a popsal do nich nejrůznější tipy na to, jak se v klubu orientovat. Do kanálů k jednotlivým technologiím jsem přidal vysvětlující připnuté příspěvky. Pokusil jsem se lépe a viditelněji objasnit, jak přesně používat kanály na mentoring.

V nějakém článku o budování komunit jsem četl několik tipů, co bych měl dělat. Článek už nenajdu, ale dělal jsem si z něj poznámky. Myslím, že následující se mi nějak povedlo v klubu udělat:

> Establish rewards for engaged members. Building an active community can take time — but rewarding special roles or privileges to active users can help incentivize more activity. This can be like a special color for their name, high spot on a list of users, or the ability to react to messages with emotes.

> Build hooks into your community to boost engagement. Everything Marketplaces and Compound send weekly digests. Trends Pro Members join conversations after receiving weekly reports.


## Dětské domovy a další

Moje kontaktáž dětských domovů z minula se trochu posunula. Napsal mi na LinkedIn jeden ředitel DD, napsala mi jedna neziskovka do mailu, komunikuju s jedním insiderem na Messengeru. Nicméně jsem nic z toho tento týden nedotáhl, bylo to na vedlejší koleji. Třeba se k tomu zvládnu vrátit příští týden.

[IG JG](https://www.instagram.com/juniordotguru/) začal sledovat účet [Fosa](https://www.instagram.com/fosaops/), tak jsem jim taky cvičně napsal, odepsali, ale já už nezvládl něco odpovědět. Mail jsem ale četl a z jeho formulace vyplývá, že si myslí, že dělám kurzy programování. Budu muset vylepšit formulace na webu nebo v e-mailech tak, aby bylo jasnější, co dělám a jakou to má přesně hodnotu. Komunikace s neziskovkami, které jsou z úplně jiných oborů, je zajímavý způsob, jak si natrénovat vysvětlování mého projektu na lidech, kteří o něm předem nic neví.


## Práce pro JG

Členka klubu, [Mia](https://www.linkedin.com/in/mia-bajic/), mi navrhla, že bych se o nějaké činnosti mohl podělit s více lidmi a nechat je pracovat na JG, aby to víc odsýpalo, třeba formou dobrovolnictví, brigády. Je to dobrý nápad a měl bych nad tím přemýšlet víc a někam si bokem odkládat věci, kde mi mohou lidé pomoci.

Blbé je, že jsem ten web teď vykutil takovým způsobem, že tam prostě všechno narychlo nějak peču a půlka je připálená a v kuchyni je spousta kouře a štípou z toho oči. Potřeboval bych ten repozitář víc připravit na to, aby do něj mohl někdo přispět, a tak. Taky mi přijde blbé nechat lidi pracovat přímo na věcech, které mi mají generovat nějaký zisk, např. lákat lidi do klubu.

Neplacená stáž na Open Source projektu s pozitivním vedlejším efektem, proč ne, ale asi ne na věcech jako nový ceník pro firmy nebo nová úvodní stránka pro klub, což jsou věci, které teď potřebuji nejvíc.


## Rešerše kolem budoucnosti pracovních nabídek

Stále uvažuji, jak do budoucna vylepšit pracovní nabídky. Napadlo mě, že by nemuselo být „těžké“ mít program, který je schopen z libovolného URL extrahovat text pracovní nabídky a analyzovat jej. Šlo by použít totéž, co používá _reader view_ ve Firefoxu nebo věci jako Pocket, Instapaper, atd. Udělal jsem si k tomu úvodní rešerši, zde si ukládám odkazy:

- [python-readability](https://github.com/buriy/python-readability)
- [ReadabiliPy](https://github.com/alan-turing-institute/ReadabiliPy)
- [goose3](https://github.com/goose3/goose3) a [goose wiki](https://github.com/jiminoc/goose/wiki)
- [readability](https://github.com/mozilla/readability), které zajišťuje _reader view_ ve Firefoxu


## Lepší administrace

Vytvořil jsem skript, který mi stáhne data z Memberful o platících uživatelích, stáhne data z Discordu, spojí je a přehled mi hodí do Google Sheets do tabulky, kde si to můžu analyzovat a filtrovat. Už při prvním koukání do tabulky jsem zjistil, že je to zajímavé počtení, např. z toho jde vidět úspěšnost různých slevových kupónů a tak. Musím to lépe prostudovat, už se těším. Management kupónů není v Memberful moc dobrý, nebo dobrý je, ale ne pro moje specifické kupónové čachry, takže toto mi pomůže v lepší orientaci.

Také mohu hned kontrolovat podezřelé uživatele. Ve středu do klubu v jedné minutě přišlo asi šest nových členů, což jsem moc nechápal a bál jsem se, že je to nějaký hack, útok, nějaká díra v systému, že mi někdo zneužívá kupóny. Ale z dat v tabulce jasně vyplývá, že jsou to všechno smrtelníci a výpis v klubu je asi jen nějaká chyba v Discordu, možná měl chybu a neposílal uvítací zprávy a když to opravili, poslal je všechny najednou pro několik členů, kteří mezitím přišli.

Také se chystám projít si [tuto stránku](https://memberful.com/help/how-to/give-free-access/) a podle návodů v ní dát oficiální přístup do klubu lidem, kteří na Discordu byli ještě dříve než Memberful a nejsou s Memberful propojení. Chtěl bych v tom mít pořádek.


## Další poznámky

- Naprogramoval jsem [losovací skript](https://github.com/honzajavorek/junior.guru/blob/master/scripts/draw_winners.py) a [vylosoval výherce](https://youtu.be/43wgNpMNYow) volňásků na sobotní [FrontKon](https://frontendisti.cz/konference). Konferenci jsem propagoval na sociálních sítích.
- Sdílel jsem na sociálních sítích [přednášku o juniorech z SREconu](https://www.youtube.com/watch?v=GB31aubcjno).
- Ptal jsem se lidí, [zda neznají další české programátorské Discordy](https://twitter.com/honzajavorek/status/1397798482287734786). O žádných, o kterých bych nevěděl, jsem se nedověděl. Možná špatná bublina, měl bych se ptát mezi mladýma a ne na sítích pro páprdy, Twitteru a Facebooku. Ty Discordy, které znám, jsem nalinkoval z klubu.
- Nasbíralo se mi zhruba milion různých mailů, tak jsem se jimi probíral a všechny jsem doteď ani neprošel.
- Odpovídal jsem různě v klubu, na jeden dotaz jsem napsal několik příspěvků o objemu článku na blog. Nechám to uzrát a třeba to pak učešu a někdy vydám i na blog.
- Jsem na pokraji uzavření partnerství s [Mews](https://github.com/MewsSystems/developers), na stránku klubu už jsem dal i jejich logo.
- [JetBrains](https://www.jetbrains.com/) přidali na JG tři nabídky na stáže. Wow! :)
- Popohnal jsem právničku s aktualizací obchodních podmínek.
- Zkoušel jsem jen tak cvičně, jak těžké by bylo vytvořit nový scraper na nabídky práce z dalšího zdroje. Nedokončil jsem to a nevím, kdy se k tomu vrátím.
- Refaktoroval jsem v kódu věci kolem načítání dat z Discordu, byl to maglajz v jednom souboru, teď je z toho souborů asi pět.
- Vytvořil jsem lapač hledačů na [Unicorn University](https://junior.guru/topics/unicorn/).
- Rozeslal jsem na Slacku a e-mailovou pozvánkou do kalendáře členům Pyvce pozvánku na členskou schůzi.
- Řešil jsem s pár dalšíma lidma člena klubu ze základky (viz minulé poznámky), ale brzy se vše vyřešilo tak nějak samo. Klukovi došla trpělivost a programování vzdal, odešel sám jak z klubu, tak i z jiných programovacích Discordů. Nedokázal překonat to, že při programování člověk stále debuguje a řeší, proč mu něco nefunguje. Nepomohlo ani to, že jsme se mu snažili pomáhat a motivovat jej.
- Několikrát za týden jsem procházel nabídky práce a hodnotil je, aby se mohla umělá inteligence učit. Ke konci týdne jsem trochu upravil vyhledávací dotazy v některých zdrojích inzerátů a výsledkem bylo nárazově velké množství dalších položek na ohodnocení. Vše jsem poctivě prošel. Zahlédl jsem věty jako „Alespoň základní znalost Pythonu plus nějaký programovací jazyk“ nebo „mladý dynamický kolektiv“, což jsem myslel, že už se objevuje jen ve vtipech. Teď už jen aby se to hodnocení opravdu nějak promítalo do učení té AI, to by bylo super. Ale tímto na tebe Mílo nechci rozhodně nijak tlačit :D
- Dále jsem pracoval na tom, abychom s Engetem připravili společný materiál. Píšeme texty, dělal jsem tento týden hodně reviews.
- Během 7 dní od 22.5. do 28.5. jsem naběhal 19 km, při procházkách nachodil 11 km. Celkem jsem se hýbal 6 hodin a zdolal při tom 30 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Dát si dopořádku evidenci firemních dohod, faktur, předplatných, mít hezkou tabulku a přidat do klubu roli „Sponzorujeme klub“. Dát dopořádku členství přes Memberful pro ty, kteří jsou v klubu, ale Memberful nemají.
2. Udělat rozhovor s Jessicou Upani.
3. Dokončovat materiály spolu s Engetem.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Tento týden samý Feri. Sorry! Od posledních poznámek jsem sdílel toto:

- [We Wrestle Not With Flesh And Blood, But Against Powers And Principalities](https://getpocket.com/redirect?&url=http%3A%2F%2Fslatestarcodex.com%2F2013%2F03%2F07%2Fwe-wrestle-not-with-flesh-and-blood-but-against-powers-and-principalities%2F&h=c664f537783bad072ec4088b4aef3498030108bb85c3160caf035c873df23644)<br>Jsme jen loutky ve hře technologického pokroku, který přináší nové možnosti a nové problémy, na něž se následně jako společnost adaptujeme skrze progresivní nápady. Může vám být nepříjemné, že existuje feminismus, ale nezastavíte jej umlčením feministek. Museli byste vrátit technologický pokrok do 19. století, což není možné. Minulá uspořádání společnosti byla dobře přizpůsobena na tehdejší úroveň pokroku, dnes by zcela selhávala. Namlouvat si, že ne, je nostalgie a romantika.
- [How Hindu supremacists are tearing India apart](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.theguardian.com%2Fworld%2F2020%2Ffeb%2F20%2Fhindu-supremacists-nationalism-tearing-india-apart-modi-bjp-rss-jnu-attacks&h=fee0973b9b9dcde873f20081feb8e28f64ea8956a3a2f5017a55224e3944e2d0)<br>Vhled do toho, co dělá Modi v Indii, jak to začalo, jak to může pokračovat. Některé věci jako přes kopírák (Trump, Brexit, ale i Česko), některé unikátně indické, vzhledem k historii, počtu obyvatel, kastovnímu systému, mnohonárodnostnímu a mnohonáboženskému uspořádání, ke kterým se těžko hledají paralely.
- [Chlapi sobě. Pirátky a starostky nemáme](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.irozhlas.cz%2Fkomentare%2Fpirati-stan-rovnopravnost-zeny_2105191635_pj&h=2af228c9b2999b99dc84fbc7cb945fa72edc878b218aaeaf6c97b1bb7e64caa8)<br>Šídlo: „Ne, ve 20. letech 21. století už není úplně normální, aby společnost, v níž je zastoupení mužů a žen rovnoměrné, reprezentovala ve sněmovně většina 78 procent mužů.“
- [Ženy mají v české politice slabý hlas, lidé z nižších vrstev skoro žádný](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F05%2Fzeny-maji-v-ceske-politice-slaby-hlas-lide-z-nizsich-vrstev-skoro-zadny%2F&h=aea23242c2b31ef1861abe1523c94077bc179d76c3a7bcb5661a13b93503e575)<br>Toto je zajímavé zamyšlení nad problémem, který zatím nemá řešení. Spolu s tím, jak nižší vrstvy nemají žádné zastoupení, nevěří establishmentu a přiklánějí se k SPD a lidem jako Volný. Bude-li tato tendence pokračovat, může nás to jednou dost překvapit - až těmto lidem bouchnou saze, abychom se nedočkali zase toho, že se bude stavět další „most inteligence“ a do parlamentu budou moci jen traktoristi. Zajímavý je i postřeh, že zástupce menšiny, který je ze vzdělané třídy, zastupuje tuto vzdělanou třídu a ne lidi ze stejné menšiny, kteří jsou chudí a žijí v ghettu.
- [Jednotná jízdenka oneticket.cz – kdy se vyplatí?](https://getpocket.com/redirect?&url=https%3A%2F%2Fcestavlakem.cz%2Fjednotna-jizdenka-oneticket%2F&h=3bd20efd8fb499559456c0f52f3a38c02009bafd6b55ae453139640b5e76041a)<br>Kdy se vyplatí nová jednotná jízdenka?
- [Adversarial Interoperability: Reviving an Elegant Weapon From a More Civilized Age to Slay Today's Monopolies](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.eff.org%2Fdeeplinks%2F2019%2F06%2Fadversarial-interoperability-reviving-elegant-weapon-more-civilized-age-slay&h=813c2022246c6b35ec2e81072da6d1081e5eec5e331d1957e0d656c5795c2170)<br>Cory Doctorow o „Adversarial Interoperability“, která technologickým firmám fungovala v konkurenčním boji dřív, a možná by fungovala i dnes.
- [Google and Facebook’s “Kill Zone”: “We've Taken the Focus Off of Rewarding Genius and Innovation to Rewarding Capital and Scale”](https://getpocket.com/redirect?&url=https%3A%2F%2Fpromarket.org%2F2018%2F05%2F25%2Fgoogle-facebooks-kill-zone-weve-taken-focus-off-rewarding-genius-innovation-rewarding-capital-scale%2F&h=333bc123eee4c348387c8658fa7a681d9bb2b64599b45000d299e4b737e2ab99)<br>Opáčko z roku 2018. Existuje „kill zone“ okolo velkých technologických firem. Žáby na prameni inovace. Pokud můžete konkurovat Amazonu, nikdo do vás nebude investovat. Pokud konkurujete a neprodáte, zničí vás. Změny v patentovém zákoně způsobují, že menší firmy jsou na straně slabšího. Chybějící antimonopolní (Google + DoubleClick a další) aj. regulační zásahy (API, interoperabilita).
- [The 2021 Python Language Summit: Making CPython Faster](https://getpocket.com/redirect?&url=http%3A%2F%2Ffeedproxy.google.com%2F%7Er%2FPythonSoftwareFoundationNews%2F%7E3%2FMb7GnQBu9NY%2Fthe-2021-python-language-summit-making.html&h=28e0df6d3c06c720eb92761885d233fe222e72d927a1863555c81c9f652974cf)<br>Python bude rychlejší
- [„Chování Dominika Feriho je veřejné tajemství.“ Ženy popsaly traumatizující zkušenosti s mladým politikem](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F05%2Fchovani-dominika-feriho-je-verejne-tajemstvi-zeny-popsaly-traumatizujici-zkusenosti-s-mladym-politikem%2F&h=111b5b14af9f716b931fec2ecc239cbb3295ec67fb97c02d393737f06632ef9d)<br>Uf
- [Feriho kauza: Bod nula pro změnu přístupu k sexuálnímu násilí](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikreferendum.cz%2Fclanek%2F32743-feriho-kauza-bod-nula-pro-zmenu-pristupu-k-sexualnimu-nasili&h=b9244ce0545cdcc455d23a49fb89e343e84714a73c24f138974ba2f91f26f00a)<br>„Až v českých zemích praskne další kauza sexuálního predátorství ze strany veřejně známé osoby, ale potlesk bude pro změnu směřovat k obětem, případně novinářům, bude to signál, že jsme se jako společnost posunuli.“
- [Feriho kauza je jen jedno z dlouhodobých novinářských tajemství. Je dobře, že se žurnalisté přestali bát. Přijdou další odhalení](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.info.cz%2Fnazory%2Fferiho-kauza-je-jen-jedno-z-dlouhodobych-novinarskych-tajemstvi-je-dobre-ze-se-zurnaliste-prestali-bat-prijdou-dalsi-odhaleni&h=3835d51954f3059b0c551e290b57d3c771783b600414d44e7cda087cb7d6cdd9)<br>„O podezření jsme věděli několik týdnů i v INFO.CZ, ale nepodařilo se nám informaci dostatečně ověřit, tudíž jsme ji nemohli vypustit. Pokud někdo vidí za celou kauzou politický boj, neví, o čem mluví.“
- [Novinářka Rychlíková o kauze Feri: Jsme si jistí, že nejde o předvolební manipulaci. Svědkyně se neznají](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.irozhlas.cz%2Fzpravy-domov%2Fpodcast-vinohradska-12-feri-rychlikova-alarm-denik-n_2105270600_bar&h=6891fe77f830b3029746f34e23a2b39c548f8f11d35d0aa34ceccee86394a1a8)<br>Rozhovor o zákulisí článku o Ferim
- [It's probably time to stop recommending Clean Code @ Things Of Interest](https://getpocket.com/redirect?&url=https%3A%2F%2Fqntm.org%2Fclean&h=61b3d242524d1fb0788292aeea4ae65045aa4f1520a8a7549af2d906d5dd2c6a)<br>Kritika Clean Code
- [Po 24 letech na šachtě se Tomáš stal ajťákem. Obor můžete změnit v každém věku, říká](https://getpocket.com/redirect?&url=https%3A%2F%2Fzpravy.aktualne.cz%2Fdomaci%2Ftomas-hisem-z-hornika-programatorem%2Fr%7E927d3882bc9a11ebaedf0cc47ab5f122%2F&h=2a7d5538eea7e4757aa4d5df68718b415764d8b1167294a0c3a4acdfe9dc96b9)<br>„Mně se zdálo o závorkách - složené závorky, dvě složené závorky, ty p**o, jak to tam mám dát?“
- [Zelenka a Rychlíková: Nesetkali jsme se s člověkem, kterého by Feriho chování překvapilo](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F05%2Fzelenka-a-rychlikova-nesetkali-jsme-se-s-clovekem-ktereho-by-feriho-chovani-prekvapilo%2F&h=e7eb2ca0faeefa7004e4ec9b286b50262e3a81d22c0270c25a7ee3bea4fac358)<br>Obsah z velké části probírá totéž co rozhovor na Rozhlasu, ale navíc je tam zajímavá pasáž o tom, jak se Feriho chování nedostalo napovrch, ale promítalo se do memů a náznaků v internetových diskuzích, protože to je primární způsob, jakým Feriho generace komunikuje. Taky zajímavá zmínka o tom, že pokud toto téma nepovažují za zajímavé novináři nebo jejich šéfové, na prostor nedostanou. Bude Feriho objíždění škol se záměrem inspirovat mladé k politice nakonec paradoxně důvodem, proč tytéž školy teď začnou lépe vyučovat témata kolem konsenzuálního sexu?
- [Máme třicet zdrojů a další přibývají. Nikdo neřekl, že ho to překvapilo a kam jsme přišli, tam jsme narazili na brutální příběh, říkají novináři, kteří odstartovali kauzu Feri](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.info.cz%2Fpodcasty%2Finsider-podcast%2Fmame-tricet-zdroju-a-dalsi-pribyvaji-nikdo-nerekl-ze-ho-to-prekvapilo-a-kam-jsme-prisli-tam-jsme-narazili-na-brutalni-pribeh-rikaji-novinari-kteri-odstartovali-kauzu-feri&h=6fde9e2eb1fadcb96ff2ed4d761a0a5de3a76094dfc020056a0aff2afd642238)<br>A ještě! Tentokrát rozhovor s otázkami zprava, díky kterým se probírají zase trochu jiné věci, víc pozadí vzniku článku, řeší se jak moc je to celé neprůstřelné, řeší se následné reakce politiků a meetoo.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
