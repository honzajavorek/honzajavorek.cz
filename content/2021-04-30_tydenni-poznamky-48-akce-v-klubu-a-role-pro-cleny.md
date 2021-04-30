Title: Týdenní poznámky #48: Akce v klubu a role pro členy
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (26.4. — 30.4.) a tak [stejně jako minule]({filename}/2021-04-23_tydenni-poznamky-47-pokusy-s-videem-a-lepsi-klub.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Akce v klubu

V úterý se odehrála posunutá přednáška Adiny Foxové. Před přednáškou jsem dojel svůj [přednáškový checklist](https://gist.github.com/honzajavorek/b1a77651e566cb6405a131bbf1fb0692) a navíc ještě znova všude upozornil, že to bude. Přednáška byla moc fajn a dokonce po ní živelně vznikla delší diskuze na různá témata, takže super. Vše se mi opět povedlo nahrát pro ty členy, kteří přednášku nestihli. Adinu vykolejilo, že Discord při sdílení obrazovky nějak schoval všechno ostatní, takže nevěděla, jestli je vůbec připojená na call. Techniku jsme sice před přednáškou zkoušeli, ale na 1-1 callu, ne v místnosti, kde se to asi chová jinak. Příště budu vědět, přidal jsem si to do checklistu.

Účast v čase přednášky nebyla dle mých očekávání (byť mě Adina i další v klubu ujišťovali, že to nijak špatná účast nebyla), tak jsem se zkoušel ptát, proč lidi na přednášku nepřišli. Nikdo jako důvod nezvolil „venku bylo hezky“, i když bylo. 7 lidem nevyhovovalo datum/čas, 4 se spoléhají na záznam, 7 vědělo o přednášce, nicméně ji neuhlídalo nebo nestihlo. 2 nezajímalo téma. Největší problém je zřejmě prostě vybrat datum a čas, které sednou všem. Nakonec jsme se dohodli, že zkusím aspoň víc používat mention @everyone na všechny členy klubu, aspoň v souvislosti s přednáškami, aby si všimli, že začala, když už jsou třeba zrovna online na Discordu. „Víc používat“ je asi nadnesené, nepoužil jsem to zatím ještě nikdy.

Počet lidí neovlivním a nevím, kolik jich přijde, do poslední minuty. Z toho pak mám vždy stres. Přemýšlel jsem, jak jej umenšit. Jednak bych rád, aby chodilo víc lidí. Jednak jde i o očekávání. Když přijde málo lidí, vím, že se ostatní podívají na video, ale prostě to vypadá blbě před speakerem. Cítím se blbě, že si něco připravoval pro 10 nebo 15 lidí. Budu to do budoucna řešit tím, že speakera na tuto možnost připravím, aby o tom předem věděl. Tím se smaže můj blbý pocit, když tato varianta nastane. Zároveň se budu dál snažit, aby přišlo lidí co nejvíc. Budu taky počítat s variantou, že nepřijde skoro nikdo, a např. na nadcházející AMA si připravím i vlastní otázky.

AMA je nový formát, který zkoušíme. [První AMA bude s recruiterem Jiřím Psotkou](https://junior.guru/events/) a těším se na ni. Zároveň samozřejmě trnu, aby byly otázky, protože bez nich se dělá AMA blbě. Nabádám lidi, aby se klidně ptali už předem v textové místnosti na to určené, ale zatím otázky nejsou. Takže to možná zase budou nervy a trochu překvapení :) Ale jak už to tak bývá, mám nervy nervy nervy, ale nakonec to dopadne dobře. Budu připraven na vše a uvidíme.

Celou středu jsem věnoval domlouvání Jirkovy AMA, přípravě plakátku, dolaďování popisu přednášky, propagaci přednášky na sociálních sítích. Blbé na [Bufferu](https://buffer.com/) je, že tam nejde naplánovat zprávu na LinkedIn, kde jsou funkční mentions na lidi a firmy, takže vždy musím jít na LinkedIn dodatečně a příspěvky editovat a mentions přidávat. V některých případech to nejde ani u FB statusů, ale to jen někdy, většinou to jde. Předpokládám, že za to nemůže Buffer, ale nějaká blbá omezení LinkedIn API. Na radu investorky jsem zkusil jeden nový trik: [FB event](https://www.facebook.com/events/464597201515797/). Pokud to pomůže šířit info o akcích, tak to budu dělat i do budoucna (časem ideálně pomocí nějakého skriptu).

## Bitva o auto-merge v Dependabotu

Probudil jsem se a v mailu jsem měl 14 notifikací o Pull Requestech, které udělal [Dependabot](https://dependabot.com/) na mých repozitářích. Žádá mě, abych upgradoval z původního Dependabotu na verzi, kterou udělali už pod křídly GitHubu, jenž je před časem koupil. Jenže tato nová verze neumí auto-merge, který používám na 12 z 14 uvedených projektů.

[Tweetoval jsem](https://twitter.com/honzajavorek/status/1387691480375046145), proč se mi to nelíbí, ale u toho jsem nakonec nezůstal a začal i [komentovat a reagovat přímo v issue](https://github.com/dependabot/dependabot-core/issues/1973#issuecomment-829083554), kde se to řeší. Vypadá to, že s jejich názorem nikdo nepohne, ale do srpna, kdy se stará verze vypne, je ještě čas. Jejich argumenty mi přijdou nekonzistentní a nerozumím tomu, jak odebrání této funkce vyřeší cokoliv z toho, co oni si myslí, že to vyřeší.

Lidi mi poslali spoustu alternativních řešení, ale já nechci alternativní řešení. Já chci, aby auto-merge podporoval přímo Dependabot. Důvody si přečtěte ve výše odkázané diskuzi (nemyslím tím pouze můj příspěvek, ale i ty pod ním).

## Czech Community of Community builders

Ocitl jsem se na meetupu [Czech Community of Community builders](https://www.meetup.com/Czech-Community-of-Community-builders/), který jsem si někde nějak náhodou vyhlídl a říkal jsem si, že tam asi patřím, když teď provozuju klub. Bylo to online. A bylo to super! Příjemný pokec a hned jsem získal i velmi dobré kontakty na lidi, které zajímá, co dělám. S jedním člověkem si doteď píšu na LinkedIn, s druhým jsme měli dnes call o možné spolupráci mezi jejich firmou a klubem. Přidal jsem se i do komunity kolem tohoto meetupu na Slack.

Použil jsem díky meetupu taky poprvé [Around](https://www.around.co/). Auto-mute super, to bylo o dost lepší než kdekoliv jinde mi přišlo. Ještě by mě zajímalo jak by to fungovalo kdyby vedle mě sedel někdo na stejným meetingu. Jinak hodně dobré funkce jako poznámky ve stylu Google Dokumentu, které se pak účastníkům pošlou. Na prd je, je že to nefunguje ve Firefoxu, takže jsem musel zas něco instalovat.

## Robot na statistiky v klubu a přidělování rolí

Dokončil jsem robota, který počítá statistiky příspěvků jednotlivých členů klubu. Nakonec nikam statistiky neposílá jako čísla, ale uděluje Discord role. Některé jsou jen nenápadné štítky, některé jsou důležité a viditelné a obarvují lidi nebo je oddělují v seznamu členů.

Nakonec mám lidi, kteří mají nejvíc příspěvků (od začátku existence klubu a za posledních 30 dní), potom lidi s nejvíce pozitivně hlasovanými příspěvky (od začátku existence klubu a za posledních 30 dní), lidi, kteří jsou v klubu krátce (do 15 dní), lidi, kteří mají profilovku a příspěvek, kde se představili (takoví jakože „občani“, rozeznatelní). Plánuju i speciální roli pro speakery z akcí a pro sponzory klubu.

## Impulzivní láska

V pátek jsem si šel zaběhat a všude byly rozkvetlé stromy, jaro, lidi v parku. Taky pár čarodějnic. Vzpomněl jsem si na to, jak jsem byl v roce 2009 ve Finsku a prožil tam Vappu. Chtěl jsem přiběhnout domů, odeslat dubnový newsletter, napsat poznámky a mít hotovo. Už tak jsem byl ve skluzu. Jenže mě zalila impulzivní chuť experimentovat a láska a vůbec, takže jsem vymyslel, že udělám slevový kupón na dnešek a zítřek (30.4. a 1.5.), s 50 % slevou, což je teda dost. Slevový kupón jsem poprvé zkoušel na MDŽ a pár lidí to do klubu přivedlo, ale jak jsem se bál, aby jich nepřišlo moc, nerozšoupl jsem se zas tak moc v tom, co jsem nabízel. Teď zkouším, co udělá, když nabídnu větší slevu. Co od toho čekám? Hele vlastně vůbec nevím. Asi pár lidí v klubu a pár rychlých peněz navíc, ale spíš je to prostě impulzivní páteční sváteční experiment. Snad se počet lidí bude nějak regulovat tím, že je víkend, a nepřijde do klubu 500 nových lidí :D

První máj, lásky čas! [Tady to je!](https://juniorguru.memberful.com/checkout?plan=59574&coupon=LASKA2021) Použijte při registraci do klubu kód **LASKA2021** a dostanete **roční členství v klubu jen za 599 Kč**. Pokud už členství máte, můžete kupón někomu z lásky darovat. Platí pouze 30.4. a 1.5. 2021.

No a tohle než jsem připravil a nasdílel a trochu ještě promyslel, tak to trvalo, pak ten newsletter, že, takže teď je pátek čtvrt na jedenáct večer, já teprve píšu poznámky a investorka je velmi nespokojená. Čím víc lásky na prvního máje pro vás, tím míň u mě doma. Ajaj!

## Newsletter

Ke konci měsíce posílám newsletter. Chci časem roli newsletteru umenšovat. Postupně ho asi stáhnu z webu, přestanu nabízet firmám jako způsob propagace nabídek, lidi budu přesměrovávat spíš na sociální sítě a do klubu. Nicméně zatím stále existuje.

Zjistil jsem, proč byl ten poslední nějaký divný. Já jej totiž v Mailchimpu nějak špatně okopíroval a posílal se jen na určitý segment odběratelů! Úplně omylem jsem to poslal jen 100 lidí místo skoro 400. A málem se mi to stalo znova, ale všiml jsem si toho počtu odběratelů, kterým to má jít a nějak mi to nedalo, začal jsem do toho šťourat, no a zjistil jsem, že březnový newsletter byl úplně špatně. Ach jo.

Tak tady je [březnový](https://us3.campaign-archive.com/?u=7d3f89ef9b2ed953ddf4ff5f6&id=4d3b35637d) a [dubnový](https://us3.campaign-archive.com/?u=7d3f89ef9b2ed953ddf4ff5f6&id=c1a74c1d08). Tím dubnovým jsem si vytvořil tak trochu šablonu, kterou už asi nebudu moc měnit. Dřív jsem dolů psal různé novinky, ale teď už se mi moc nechce a asi tam budu mít permanentně info o tom, že nabídky práce jsou teď v klubu lépe než v newsletteru a že novinky mají lidi sledovat na sítích.

## Další poznámky

- Aktualizoval jsem všechny screenshoty v náhledech na junior.guru. Doplnil jsem speciální kód, který místo screenshotu FB skupiny stáhne její cover obrázek, podobně jako se nedělají screenshoty YT videí, ale stahuje se náhledový obrázek videa. Založil jsem u toho [tohle issue na Pageres](https://github.com/sindresorhus/pageres/issues/411). Schovávat na screenshotech různé cookie lišty a popupy, nebo obcházet různé ochrany proti scrapování, to je fakt past vedle pasti. Naštěstí Pageres zvládá hodně věcí a co nezvládne ani on, to prostě [cvaknu z Firefoxu](https://support.mozilla.org/en-US/kb/take-screenshots-firefox?redirectslug=firefox-screenshots&redirectlocale=en-US) na jedno tlačítko a uložím do složky, ze které si to můj skript vezme a upraví na požadovaný formát a velikost.
- Vysvětlil jsem kamarádovi jak fungují streamy a file-like objekty v Pythonu.
- Přečetl jsem si [tento tweet](https://twitter.com/patrickwardle/status/1386732292224155648) a ihned aktualizoval macOS. V souvislosti s tím mi přestaly fungovat Xcode věci a musel jsem je [přeinstalovat](https://medium.com/flawless-app-stories/gyp-no-xcode-or-clt-version-detected-macos-catalina-anansewaa-38b536389e8d). Udělal jsem i update věcí v Homebrew a při tom se mi aktualizoval Node na verzi 16. Protože jsem nepoužíval nvm, tak se mi vše rozbilo. Při hledání řešení jsem našel [tuto SO otázku](https://stackoverflow.com/q/67241196/325365), která přesně popisovala můj problém, řešení tam nebylo. Tak jsem řešení [našel](https://github.com/sass/node-sass/issues/3077) a napsal [odpověď na SO](https://stackoverflow.com/a/67303155/325365), kde jsem popsal, co se stalo a že nemá autor otázky používat „systémový“ Node, ale vlastní přes [nvm](https://github.com/nvm-sh/nvm). A potom jsem to tak šel udělat i u sebe.
- Opravil jsem drobnou chybu v robotovi, který posílá nabídky práce přímo do klubu.
- Opravil jsem chybu ve stahovači nabídek práce z LinkedIn.
- Loga na [stránce klubu](https://junior.guru/club/) jsem rozdělil na firemní a komunitní.
- Do komunitních log jsem přidal yablka. Poslal mi logo v PSD, tak jsem poprvé použil [Photopea](https://www.photopea.com/) a super.
- Vyměkli jsme a přestali trápit náš aku šroubovák. Objednali jsme seriózní elektrický mlýnek na kafe. Tento čin v nás vyvolal smíšené pocity, zda jsme se tím nestali příliš seriózními a dospělými lidmi. Mele ovšem skvěle.
- Vítal jsem nové členy v klubu. Už je nás 143 členů za 3 měsíce provozu klubu. Na stránku klubu jsem napsal přesně takovouto větu. Předtím tam bylo 20 náhodných profilovek lidí z klubu a pak slova „a 123 dalších“, ale i mě samotnému se to strašně špatně vnímalo. Podle mě by nikoho nenapadlo to sčítat, vidí akorát číslo. Takže jsem tam nejdřív napsal přímo „143 členů“ a potom to ještě změnil na „143 členů za 3 měsíce provozu“, aby to číslo bylo v nějakém kontextu.
- Během 7 dní od 24.4. do 30.4. jsem naběhal 8 km, při procházkách nachodil 16 km. Celkem jsem se hýbal 6 hodin a zdolal při tom 24 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Napsat si s firmou, která má zájem o členství v klubu, dořešit konečně partnerství s jednou vzdělávací agenturou.
2. Úspěšně uspořádat AMA s Jirkou.
3. Pokračovat ve tvorbě věcí, které zvyšují hodnotu klubu pro jeho členy.

Bonus: Včas vypnout kupón se slevou. Zajít si na úřad pro novou občanku.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Get the FLoC out](https://getpocket.com/redirect?&url=https%3A%2F%2Fadactio.com%2Fjournal%2F18046&h=78be6cf7a25deb67cfba235fda349e9f2129e1209400dea3ac948c125b217a16)<br>Google chce pokračovat ve sledování uživatelů i potom, co zmizí 3rd party cookies. Článek popisuje, jak Google Chrome kvůli tomu zrazuje své uživatele a jde na ruku čistě svému monopolnímu majiteli. Přitom bychom se všichni nejspíš bez sledování obešli - Facebook i Google by se uživili i obyčejnější reklamou.
- [Novinky Standy Dvořáka](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.jestevetsikritik.cz%2Fkomentare%2F1136-novinky-standy-dvoraka&h=6a82a53b5db60214619053271c745c835015596e18e2493169bc2e883623cd4b)<br>Kamil Fila šel za nás na Novinky a dokonce i do komentářů. V textu usvědčuje konkrétního autora Novinek z povrchního, systematického šíření zloby a nasranosti mezi lidmi. Zajímavý způsob - chytit konkrétního autora za ruku a prohlásit „co to tady čmáráš na ty zdi?! já tě vidím co tady děláš!“ Se zástupy trolů to udělat nejde, s redaktorem rádoby seriózního zpravodajství ano.
- [Hotwire: Ze serveru na klienta a zase zpět](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.vzhurudolu.cz%2Fblog%2F195-hotwire&h=a788404becdbc39889c479ec4ff4d620d2df4ee475c59172f82bf04f09d24081)<br>Kdo jste o tom ještě neslyšeli. Mě se to líbí.
- [Komentář: Jsme pracovitý národ, jenom nám šéfují nemehla](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Fkomentar-jsme-pracovity-narod-jenom-nam-sefuji-nemehla-151150&h=6029aaf8686be9323f482a592d7b03df1f81dcc92f19de3563de1d8573938cc1)
- [Křiváci a poctivci](https://getpocket.com/redirect?&url=https%3A%2F%2Fhoudekpetr.blogspot.com%2F2021%2F04%2Fkrivaci-poctivci.html&h=0d913ec56e4534e8f66cc957079780263508c162b2f3d19ac0b1fa16a97aa3a2)<br>Jak je to s nezájmem o druhé ve městech? S poctivostí? Proč lidé přihlíží a nepomůžou, když se něco děje? Česko je sedmá nejčestnější země na světě!
- [Henry Ford, Innovation, and That “Faster Horse” Quote](https://getpocket.com/redirect?&url=https%3A%2F%2Fhbr.org%2F2011%2F08%2Fhenry-ford-never-said-the-fast&h=35bbb06ae92f081fe7675d0eb73485782cb6f9b4e4122e993c95c8b0daaed554)<br>Ford nikdy neřekl citát s rychlejšími koňmi a ignorování zákazníků způsobilo jeho firmě katastrofální propad podílu na trhu, i když předtím měl velký náskok.
- [The Money Talk Meetup](https://getpocket.com/redirect?&url=https%3A%2F%2Fcybermagnolia.com%2Fblog%2Fthe-money-talk-meetup%2F&h=9ace9f3fa671fe5dd96f5c676e98bff1776e1976b2281fe67d6ccfc24e2b38b2)<br>Jak si říct o větší peníze? Jak vyjednávat o mzdě?

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
