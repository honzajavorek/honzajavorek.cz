Title: Týdenní poznámky: Čísla a přemýšlení
Image: images/img-4733.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/262

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-07-22_tydenni-poznamky-europython-a-stahovani-csv-z-memberful.md) už utekl nějaký ten týden (22. 7. až 4. 8.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Nádraží]({static}/images/img-4733.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Čísla

V minulých poznámkách jsem psal toto:

> Opravit metriky na [/open/](https://junior.guru/open/) a přidat nové, abych se mohl rozhodovat, co dál.
> Zdá se mi, že mi na několika frontách klesají čísla.
> Chtěl bych se zamyslet nad svými prioritami a zaměřit se na to, co nejvíc pomůže zvrátit trend.
> Ale k tomu potřebuju nejdřív vědět, co se přesně děje a mít na to čísla a grafy.

No a ve zkratce, přesně to jsem teď dva týdny dělal.
Bylo to trochu frustrující, protože jsem se stále nemohl dobrat konce a místo abych dělal nějaké pěkné věci pro juniory, patlal jsem se s čísly a grafy.
Zároveň jsem věděl, že bez nich žádné další hezké věci nevzniknou, že čísla a grafy potřebuju.

Vždy, když na junior.guru něco udělám, tak si to zapíšu do Trella jako kartičku, abych pak podle toho mohl sepsat na konci týdne poznámky.
Teď se koukám na asi 100 kartiček o tom, jak jsem řešil ty grafy:

-   Graf počtu clenu
-   oznacit co je trial
-   Příchody a churn je fakt hodne divny graf
-   Dlouho koukani na to jestli sedí čísla a pak jsem to vzdal
-   odchody, duration, churn
-   dat prichody a odchody do jednoho grafu?
-   cancellations
-   dat veci z csv do grafu na web
-   opravit pocty clenstvi v klubu - vic individualnich nez vsech, ehm
-   zdroje příchodů - v procentech?
-   labely a barvy pro pie chart
-   zdroje prichodu - ktery vedou k nejvic penezum?

A tak dále, a tak dále.
Nemá smysl rozepisovat, co za jednotlivosti jsem dělal a jak jsem se s tím pral.
Musíte mi prostě věřit, že to byla past vedle pasti.

Jedna z věcí, na které jsem se strašně zasekl, bylo psaní složitých SQL dotazů, resp. jejich reprezentací v Peewee.
Určité úkoly mi kvůli tomu zabraly i hodiny, a to i s ChatGPT a GitHub Copilotem.
Až po několika dnech mě napadlo, že to, co dělám, bych možná měl rychleji a přehledněji přímo v Pythonu, byť třeba ne tak efektivně.
Ta čísla se počítají jen jednou a i když to bude neefektivní, pořád je to nic.
Takže jsem místo všelijakých vnořených JOINů a SELECtů skončil u obyčejného Python cyklu s pár obyčejnými SELECTy.
Kód desetkrát primitivnější, napsaný hned, čitelnější.
Ach jo.
Proč mě to nenapadlo hned?

Výsledkem těch dvou týdnů je spousta opravených grafů a docela dost nových grafů na [/open/](https://junior.guru/open/).
Taky jsem si udělal nový tajný kanál na Discordu, #byznys, kam mi bot automaticky postuje, když lidi přichází do klubu a vyplní anketu odkud přišli, nebo když odchází z klubu.
Pomůže mi to okamžitě odchytnout chyby v klasifikaci těchto dat, a zároveň uvidím, co se děje a budu to moci hned řešit.

![Nový kanál #byznys]({static}/images/screenshot-2023-08-04-at-17-05-05.png)

Například jsem zjistil, že mi lidi psali při odchodu různé vzkazy, které jsem si přečetl až teď.
Nebo jsem šel a všem, kdo označili jako důvod k odchodu že na klub už nemají peníze, jsem napsal email a osobně jsem jim nabídl stipendium.

Na /open/ jsem prošel a aktualizoval i všechny texty a nakonec jsem přidal i tyhle poznámky 😀
Nevím, proč tam už dávno nebyly.

## Přemýšlení

Jedno celé odpoledne jsem šel a od začátku do konce přečetl [The Proven Path](https://www.feverbee.com/wp-content/uploads/2023/03/theprovenpath.pdf) a [Community Canvas](https://community-canvas.org/), které mi před časem doporučila [Šárka](https://www.linkedin.com/in/melicharova/).
Community Canvas už jsem znal i předtím, ale to nic nemění na tom, že jsem to doteď pořádně nečetl.
Udělal jsem si z toho spoustu poznámek, některé do budoucna, některé relevantní i pro mou aktuální situaci.

Taky jsem si otevřel všechny články o komunitách a podnikání, které jsem si v poslední době uložil, a přečetl jsem je.
Z těch jsem si moc poznámek neudělal a nebyly vlastně moc relevantní.
Jednoho autora jsem si ale do RSS čtečky uložil: [Max Pete](https://maxpete.substack.com/).

Následně jsem si odpočinul a celou tu stránku [/open/](https://junior.guru/open/) jsem si sjel shora dolů a pokusil jsem se interpretovat, co se mi snaží ten který graf říct.
Toto jsem si sepsal a začal se mi vykreslovat nějaký obrázek toho, kde mám asi problém.
A to už je jen krok k tomu, co bych měl teď s největší prioritou dělat.

Toto plánování ale dokončím asi až v pondělí a pak k tomu nejspíš vydám separátní článek.
Každopádně mě naplňuje radostí a optimismem, že už jsem konečně dodělal ty grafy, a že to celé k něčemu doopravdy bylo a jsem schopen z nich něco vyhodnotit.
A že přestávám tápat, že začínám mít nějakou představu, co budou další kroky.

## Pomoc s kóděním

Ozvala se mi kamarádka a nejspíš mi trochu pomůže s programováním na junior.guru.
Dohodli jsme se na úkolové finanční odměně.
Po dlouhé době jsme se i viděli a bylo to super.
A byla to aspoň záminka omrknout i [nový most](https://zdopravy.cz/dvacaty-most-pres-vltavu-v-praze-lavka-mezi-holesovicemi-a-karlinem-se-otevrela-verejnosti-169669/).

Když jsem se z kafe vrátil domů a koukal na seznam věcí, které bych potřeboval dokončit, než začnu nové věci, hned jsem ze dvou udělal nové issues: [#22](https://github.com/juniorguru/juniorguru-chick/issues/22) a [#23](https://github.com/juniorguru/juniorguru-chick/issues/23).
Možná totiž nemusím všechno dokončit já!

## Lepší propagace srazů v klubu

Něco jsem si ale nechal.
Dodělal jsem lepší propagaci srazů v klubu.
Už před časem jsem zařídil, aby bot automaticky zakládal Discord události pro srazy různých komunit.

Chtěl jsem ale, aby bot na srazy upozorňoval i v kanálu #pozvánky-a-promo.
Aby tam dal zprávu, ke zprávě udělal vlákno, a ve vlákně podporoval sdružování juniorů, diskuzi, koordinaci před akcí.
Asi lépe vysvětlit obrázkem.

![Promo akcí v kanálu]({static}/images/screenshot-2023-08-04-at-16-33-51.png)

Splácal jsem to za jeden osamělý večer.
A funguje to!
Druhý den jsem to refaktoroval a otestoval, hotovo, paráda.
Bot dokonce rovnou přes _mention_ přidává do vlákna lidi, kteří se přihlásili, že na akci možná půjdou.

Ještě mě napadlo, že v den akce by mohl bot do vlákna napsat, aby si to lidi užili a nezapomněli poslat i fotku, když se potkají 🙂
Třeba by ji fakt poslali a podpořilo by to zase trochu komunitního ducha.

Taky jsem napsal e-mail na několik srazů, abych zjistil, zda jde nějak strojově číst, kdy mají události.
Díky tomu budu nejspíš moci brzo přidat srazy v Budějcích nebo Java srazy.

## Fio banka a ukládání historie dat do gitu

Přišlo mi SMSkou, že Fio banka mění platnost tokenů na svém API.
Nyní budou časově omezené, ale jejich platnost se bude postupně prodlužovat, když se přihlásím do internetového bankovnictví.
Dobrá, sice divné, ale proč ne.

Pak mi API ze dne na den přestalo fungovat.
Podezíral jsem, že na vině je buď token, nebo že deploynuli novou verzi API a něco jim tam nefunguje.
Ani jedno!

Deploynuli totiž zcela záměrně i úplně jinou změnu, která mi všechno rozbila.
O té mi ale nijak vědět nedali.
Ani e-mail, natož SMS.
Přečetl jsem si ji až v HTTP odpovědi a následně v [PDF dokumentaci](https://www.fio.cz/docs/cz/API_Bankovnictvi.pdf).

> **Poskytnutí dat starších více než 90 dní**
>
> Pro získání dat mladších 90 dní není potřebná dodatečná silná autorizace v internetovém bankovnictví. Požadujete-li získat data starší 90 dní, tak je nutné dočasně odemknout přístup ke kompletní historii.
>
> Toto odemknutí se nastavuje v internetovém bankovnictví na záložce „Nastavení“ a zvolte složku „API“. Kliknutím na ikonku zámku se pro daný token vytvoří autorizační pokyn. Po úspěšné autorizaci budou historická data, po dobu 10 minut, přístupná.

Nemohu tedy (bez lidské asistence) stahovat transakce ze svého účtu za celou dobu podnikání.
To samozřejmě hodilo vidle do všech mojich grafů s finančními výsledky.
Co se dalo dělat, musel jsem to zrovna celé předělat.

Stalo se to samozřejmě ve stejný den, kdy jsem si jednak myslel, že už mám konečně za sebou veškerou práci na grafech, jednak kdy jsem zjistil, že mám průšvih s Mews (viz níže).
Neudržel jsem tedy emoce a vedl jsem s podporou Fio banky konverzaci s předmětem „API vrací pro dotazy na data 90 dní starší 422 - nejspíš vtip?“, která po pár výměnách skončila slovy „děkujeme za zpětnou vazbu, kterou jsem takto předala příslušnému oddělení“.

Co si budem, něco takového bylo do budoucna stejně nevyhnutelné.
Bylo to možné v začátcích junior.guru, ale po několika letech fungování už prostě nelze stahovat vše od začátku historie.
Buď to useknu a budu sledovat data např. jen za poslední rok, nebo holt musím ta data někam uložit.

Začal jsem si tedy transakce v minimální formě ukládat do gitu do `.jsonl` souboru, takže tam zůstává historie a stahuju si pouze nová data.
Je to rozhodně výzva co se týče toho, co jsem ještě ochotný dát někam veřejně.
Ale v zásadě tam není o moc víc, než co by nebylo už předtím v grafu…

![Transakce v gitu]({static}/images/screenshot-2023-08-04-at-16-56-05-record-transactions-skip-ci-honzajavorek-junior-guru-1fd1cdd.png){: .img-thumbnail }

Podobný princip ukládání historie jsem jedním vrzem udělal i pro data o předplatném, která rovněž už nebylo možné efektivně stahovat z Memberful od začátku (zhruba po 1000 požadavcích rychle za sebou mě vždy jejich API na několik hodin zablokovalo 😀) a také pro ukládání počtu followerů na sociálních sítích.
Celkově mám dojem, jako bych letos nedělal skoro nic jiného, než optimalizoval a optimalizoval, protože junior.guru už toho dělá hodně a dělá to dlouho.
Uf!

## Role „Aktivně hledám práci“

Přemýšlel jsem nad tím, jaká je nejkratší cesta k tomu poskytovat juniorům skrz klub co „nejtvrdší“ hodnotu.
Už dřív jsem měl plány, že by mohli mít junioři nějaké profily apod., ale viděl jsem to jako velmi vzdálenou budoucnost.
Teď mě napadlo nečekané spojení různých věcí:

-   Dobrovolná samoobslužná role na Discordu
-   [Connections & Linked Roles](https://support.discord.com/hc/en-us/articles/10388356626711-Connections-Linked-Roles-Admins) na Discordu
-   Profily juniorů…

Prostě mě napadla taková věc… A zeptal jsem se členů a vypadá to, že by byla poptávka…

![Role „Aktivně hledám práci“]({static}/images/screenshot-2023-08-04-at-16-25-33.png)

Nechci se pouštět do dalšího produktu pár týdnů po tom, co jsem dal na web katalog kurzů, ale svrbí mě teda dost prsty.
A vybuchla mi hlava co se týče nápadů, kam by to šlo až dovést.
S čím vším by to šlo propojit a co vše by to mohlo umět.

Byť je ten prvotní nápad starý už několik let, vrtá mi to teď dost hlavou a přemýšlím, jak by se to celé dalo udělat aspoň jako strašně jednoduché MVP.
Zatím jsem aspoň udělal tu roli.
Existuje jednotky dní a už si ji zakliklo 11 lidí.

## Průšvih s Mews

Před nedávnem jsem si začal ukládat informace o partnerstvích novým způsobem.
Ke každému smluvenému období jsem si uložil od-do datum.
Nedošlo mi, že když jedno období končí 2023-06-30 a nové začíná 2023-07-01, tak si to bot vyhodnotí jako „třicátého všem končí předplatné a vyhoď je“.
Kvůli technikálii, která by byla už moc detailní, se to stalo jen několika lidem z Mews.

Všiml jsem si toho, když jsem pracoval na číslech a viděl jsem tam, jak z ničeho nic spousta lidí z Mews v jeden okamžik odešla.
Hned mi došlo, co se děje.
Druhý den si toho všiml i Jan z Mews, se kterým partnerství řeším.
Shodou okolností v den, kdy psal [hezký status na LinkedIn](https://www.linkedin.com/posts/jan-meissner_i-do-many-calls-with-juniors-and-people-considering-activity-7090261521397612549-zNU2) o tom, co spolu děláme kolem stipendíí 🤦‍♂️

No, i takové věci se stávají.
Vše jsem napravil, poslal maily, omluvil se.

Kód jsem ještě neopravil.
Bude to součástí většího překopání toho, jak tahle věc funguje, protože jsem přišel už na několik nedostatků stávajícího řešení.
Ale nejbližší další firma prodlužuje až za 58 dní a ani nevím, jestli prodlouží, tak na to mám čas.

## Život

-   V pondělí jsem jel vlakem do Prahy, teď zase jedu vlakem z Prahy.
    A to jsem se dvěma cestám dokonce vyhnul.
-   Dostali jsme nezvykle velké číslo rodinných příslušníků na jedno místo a oslavili jsme tam dva roky naší dcerky.
    Bylo to náročné, ale bylo to fajn.
    Nemůžu uvěřit, že už je to dva roky.
-   Řešil jsem i nějaké doktory.
    Vypadá to, že ani jeden neví, co se mnou.
    U jednoho je to fuk a má plán, jak zjistit víc, který už realizujeme.
    U druhého je to důležitější a jen doufám, že má nějaký plán B.
    Teda vlastně už plán C.
-   Kvůli tomu, abych mohl v Praze k doktorům, jsem se rozdělil s rodinou a stejně jako [nedávno]({filename}2023-07-07_tydenni-poznamky-sam-doma.md) jsem byl několik dní doma sám.
    Na rozdíl od minule mi to tentokrát spíš nesedlo, raději bych kolem sebe tu rodinu měl.
    Aspoň mi to ale umožnilo užít si v [nejlepším kině](https://kinoaero.cz/) Barbenheimer double feature.
    Bylo to… intenzivní!
-   O víkendu jedu na otočku na nějakou šifrovačku do Brna, na kterou mě ukecal kamarád.
    Jsem zvědavý, jestli něco vůbec vyluštím.
    Taky má hodně pršet.
-   Zanesl jsem si konečně svetr k místní švadleně na opravu.
    Zkusil jsem si očistit fleky na kraťasích, ale bohužel je to asi smůla.
    Zatím jsem nehledal, jak se z oblečení sundává smůla, ale vzhledem k jejímu názvu nečekám nic snadného.

![Barbenheimer]({static}/images/img-4713.jpg)

## Arc

Na doporučení [Jakuba Zelenky](https://mimoagendu.cz/) jsem si hrál s prohlížečem [Arc](https://arc.net/).
Rozhodně zajímavý počin.
Jejich [YouTube kanál](https://www.youtube.com/@TheBrowserCompany) je i byznysovou inspirací, např. tam má jejich CEO svůj video deníček ve stylu těchto poznámek.

Arc mě stále ujišťoval, že nechce žádná má osobní data, ale zároveň nejde použít bez přihlášení a stále mi nabízel propojení s Google účtem, takže jsem ho smazal.
Navíc když jsem šel do nastavení, vykouklo tam na mě hodně integrací právě s Googlem a Google Chromium logo.
Chromium je open source projekt ze kterého vychází Chrome, ale stejně.
Není to můj šálek.
Asi jsem prostě navěky předurčen zůstat u Firefoxu.

## Přednášky

Budu v diskuzním panelu na [PyCon CZ](https://cz.pycon.org/2023/), tak jsem doplňoval údaje do systému.
Do bio jsem napsal následující:

> Originally a software engineer, now more of an entrepreneur. Creator of [junior.guru](https://junior.guru/), a project for Czech and Slovak beginners in coding. Long-term volunteer in the Czech Python community. Founded one meetup, led the communications working group of four [conferences](https://cz.pycon.org/), contributed to several Django Girls and PyLadies courses or workshops. Now helping mainly as a board member of the local Python nonprofit, [Pyvec](https://pyvec.org/). Sometimes also a self-appointed ambassador of [PyCon Namibia](https://na.pycon.org/).

Napsal jsem to anglicky, respektive okopíroval jsem to, co jsem [sepisoval před nedávnem už pro EuroPython]({filename}2023-07-22_tydenni-poznamky-europython-a-stahovani-csv-z-memberful.md).
Ale protože bude panel česky, dostal jsem za úkol to přeložit.
ChatGPT mi moc nepomohlo, tak jsem to musel udělat ručně, jako kdyby snad byl rok 2022.

> Původně programátor, dnes už spíš podnikatel. Tvůrce [junior.guru](https://junior.guru/), projektu pro začátečníky v programování. Dlouhodobý dobrovolník v české Python komunitě. Založil jeden sraz, vedl pracovní skupinu pro komunikaci na čtyřech [konferencích](https://cz.pycon.org/), přispíval k workshopům a kurzům Django Girls nebo PyLadies. Dnes pomáhá hlavně jako člen výboru v neziskovce [Pyvec](https://pyvec.org/), kde nejraději ze všeho dokumentuje, jak se mají věci dělat. Občas je taky samozvaným ambasadorem [PyCon Namibia](https://na.pycon.org/).

Vybírali jsme ještě někoho do panelu a nakonec vybrali.
Dohodl jsem se s [Miou](https://www.linkedin.com/in/mia-bajic/), která panel organizuje, že vymyslíme nějaký promo plakátek, který budou moci lidé sdílet na sociálních sítích.
Neuváženě jsem souhlasil i s tím, že to zkusím namalovat v Canvě.

Pak mi napsali i frontendisti, protože budu něco mít i na [FrontKonu](https://frontendisti.cz/konference).
Poslal jsem jim název přednášky a anotaci:

> **Junior jako investice: Proč je mít v týmu a jak je zaučovat**
>
> Junioři v týmu jsou investice, která vás bude něco stát, ale v dlouhodobém horizontu se může vyplatit. Jak najít juniory, kteří mají potenciál rychle růst? Jaké jsou konkrétní benefity juniorů pro tým programátorů a pro firmu jako takovou? A co dělat, nebo čeho se naopak vyvarovat, aby vaše investice nevyšla vniveč?

To jsem sám zvědav, o čem budu mluvit! Frontendisti samozřejmě taky chtěli bio:

> Původně programátor, dnes už spíš podnikatel. Tvůrce [junior.guru](https://junior.guru/), projektu pro začátečníky v programování. Dlouhodobý dobrovolník v české Python komunitě. Byl u začátků projektů jako Mergado nebo Pex, krásné chvíle prožil v Apiary. Na svůj blog [Javorové lístky](https://honzajavorek.cz/blog/) píše už 17 let. V Česku jsou jeho nejznámějším článkem nejspíš [Kolonizátoři a správci kolonií](https://honzajavorek.cz/blog/kolonizatori-a-spravci-kolonii/) o dvou programátorských povahách.

Napsal jsem to tak, aby to šlo zkracovat podle potřeby tím, že se vždy ubere jedna věta od konce.

Jak se to tak sešlo, tak mi došlo, že na různé konference píšu různá bio podle toho, co se tam hodí víc.
Napadlo mě, že by bylo zajímavé sledovat, jak se moje bio mění třeba i historicky.
Třeba na WebExpo v roce 2015 [jsem měl tohle](https://webexpo.net/prague2015/talk/designing-apis-mastering-http-is-just-beginning/):

> Former freelance developer and consultant, now helping Apiary with making API Blueprint the best format for describing web APIs. Passionate about API design, consistency, structured code, documentation. On top of that, Honza is Czech Python community mascot—but he not only promotes the language, he regularly also takes part in preparations of local meetups and workshops focused on Python.

Jak bude asi vypadat za dalších osm let?

## Další

-   Dal jsem prvním lidem otestovat anketu pro juniory, kterou jsme připravili s ENGETO Academy.
-   Vyšla nová verze MkDocs.
    Jsou tam zajímavé nové funkce, především kontrola odkazů, nový [katalog rozšíření](https://github.com/mkdocs/catalog), apod.
    Upgradnul jsem.
    Nic se nerozbilo.
-   Z úřadu práce mi odepsali „Dobrý den, toto bohužel možné není. Přeji pěkný den. PK“ na dotaz, zda lze data z [katalogu](http://www.jsemvkurzu.cz/) stáhnout přes nějaké otevřené API nebo z nějakého veřejného Excelu.
    Raději nebudu odepisovat, že už jsem to API našel, použil, a data mám dávno na webu jako součást svého katalogu kurzů.
-   Díky kamarádům mám přístup do API [Merk](https://www.merk.cz/).
    To mi umožní obohatit katalog kurzů daty o provozovatelích.
-   [Michal Cyprian](https://www.linkedin.com/in/michal-cyprian-b5b915127/) bude v Košicích zakládat technologický meetup.
    Pokud vás to zajímá, napište mu.
-   Naprogramoval jsem si příkaz, který přizpůsobí míru paralelizace na CircleCI podle toho, jak na sebe jednotlivé skripty zpracovávající data navazují.
    Tohle jsem doteď dělal ručně a bylo to hodně otravné.
-   Zhluboka jsem se nadechl a naznal, že by mi prospělo mít na codebase nějaký formátovač kódu.
    Že sice nějaké konvence dodržuji, ale zbytečně ztrácím čas ručním formátováním a kódu už je tolik a píšu ho tak dlouho, že ani v jednom člověku to už nedokážu udržovat konzistentní.
    Standardem je [black](https://github.com/psf/black), takže jsem ho přidal do projektu.
    Zatím neformátuju vše, začal jsem testy a postupně přidávám jednotlivé složky podle toho, jak si na to zvykám.
-   V plném počtu a na smluvený čas jsme se sešli na call výboru [Pyvce](https://pyvec.org/).
    Mám z toho radost.
    Daří se nám konečně scházet, po kouskách řešit věci, stihneme si u toho i pokecat a celé se to vleze pod hodinu.
-   Vyřidil jsem jedno stipendium.
    Další ještě čeká v mailu.
-   Udělal jsem konečně promo pro předchozí epizodu podcastu: [Matěj Kotrba (Fuckupy v IT, Očima ajťáka) o tom, jak se recruiterům dostat do hledáčku](https://www.linkedin.com/feed/update/urn:li:activity:7089159983702884352/)
    Pavlína mezitím [natočila další](https://junior.guru/podcast/).
    Tu jsem aspoň hned vydal, ale promo udělám později.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Během 14 dní jsem při procházkách nachodil 6 km, ujel na kole 21 km. Celkem jsem se hýbal 12 h a zdolal při tom 27 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Utřídit si priority a naplánovat další postup 😀
2.  Vyhodnotit zpětnou vazbu od pokusných králíků, kteří viděli anketu pro juniory.
3.  Napsat do různých firem z různých důvodů.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Stop Trying to Make Social Networks Succeed](https://ploum.net/2023-07-06-stop-trying-to-make-social-networks-succeed.html)<br>„Like every human endeavour, every social network is there for a limited duration and will be useful to a limited niche of people. That niche may grow to the point of being huge, like Facebook and WhatsApp. But, to this day, there are more people in the world without an account on Facebook than people with one. Every single social network is only representative of a minority.“
- [Splitting the Web](https://ploum.net/2023-08-01-splitting-the-web.html)<br>Dva oddělené světy na webu. Jeden plný reklam a notifikací a komerce, druhý plný adblockerů, fediverse, RSS a statického HTML bez JavaScriptu. Kterou si vyberete? A která je ta divná a která je ta normální? „Something strange is happening: it’s not only a part of the web which is disappearing for me. As I’m blocking completely google analytics, every Facebook domain and any analytics I can, I’m also disappearing for them. I don’t see them and they don’t see me!“
- [How to Kill a Decentralised Network (such as the Fediverse)](https://ploum.net/2023-06-23-how-to-kill-decentralised-networks.html)<br>Pamatujete Jabber a jak ho Google zabil? „But the Fediverse cannot be bought. The Fediverse is an informal group of servers discussing through a protocol (ActivityPub). Those servers may even run different software (Mastodon is the most famous but you could also have Pleroma, Pixelfed, Peertube, WriteFreely, Lemmy and many others). You cannot buy a decentralised network! But there’s another way: make it irrelevant. That’s exactly what Google did with XMPP.“
- [Past mikropráce: Ne, v metru ani v čekárně u zubaře vážně nepracujte](https://www.welcometothejungle.com/cs/articles/mikroprace-nevyhody)<br>„V danou chvíli máte radost, že „šetříte čas“, ale z dlouhodobého hlediska vaše kreativita trpí a jste pod čím dál větším stresem“
- [Ahoj vol. 56: Creator Economy](https://open.substack.com/pub/pavlinaspeaks/p/ahoj-vol-56-creator-economy)<br>Pavlína Louženská rozebírá trend ekonomiky tvůrců - do které patřím.
- [Auta se prodlužují o dva centimetry ročně. Před 12 lety se nafoukla i parkovací místa, dnes už nestačí](https://www.irozhlas.cz/zpravy-domov/auta-automobily-zvetsuji-suv-parkovaci-mista_2307280600_jab)<br>Ovládnou lidstvo stroje? Už ovládly. Jmenují se auta. Je jich stále víc a jsou stále větší.
- [Dvacátý most přes Vltavu v Praze. Lávka mezi Holešovicemi a Karlínem se otevřela veřejnosti - Zdopravy.cz](https://zdopravy.cz/dvacaty-most-pres-vltavu-v-praze-lavka-mezi-holesovicemi-a-karlinem-se-otevrela-verejnosti-169669/)<br>Už se těším, až to uvidím!
- [Why haven’t internet creators become superstars?](https://culture.ghost.io/why-havent-internet-creators-become-superstars/)<br>Proč nejsou internetoví tvůrci na červených kobercích, i když je sleduje víc lidí, než tradiční hvězdy?
- [Státní peníze za hvězdy od Michelinu — 5:59](https://www.seznamzpravy.cz/clanek/233926)<br>Nemyslel jsem si, že by mě bavilo povídání o jídle a kauze s Michelinskými hvězdami, ale někdo mi tento rozhovor doporučil a bylo to vlastně super. Kauza se sice probrala, ale zbytek byl o minulosti a budoucnosti naší stravy, nebo o tom, jak ve světě protlačit českou kuchyni.
- [CLI tools hidden in the Python standard library](https://til.simonwillison.net/python/stdlib-cli-tools)<br>Nevěděl jsem, že v standardní knihovně Pythonu je tolik CLI utilitek
