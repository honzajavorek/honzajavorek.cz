Title: Týdenní poznámky: Nová homepage, PyCon CZ, dovolená a únava
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/286
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111150368673873389

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-09-08_tydenni-poznamky-nastenka-mouder-a-prvni-pribeh.md) už utekl nějaký ten týden (8. 9. až 29. 9.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [teď plánuji]({filename}2023-08-07_letni-pit-stop.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/3/).
</div>

## Mastodon

Ve volném čase jsem přemístil, kam dávám odkazy, které mě zaujmou.
Už je nedávám na Telegram do kanálu, ale na Mastodon.
Upravil jsem [svoje skripty](https://github.com/honzajavorek/honzajavorek.cz/blob/8e2489701f678ee576ebb9ae38ae7b99fbae21e7/blog/weeknotes.py) tak, aby se na konec poznámek dávaly [odkazy, které dám na svůj Mastodon s hashtagem #links](https://mastodonczech.cz/@honzajavorek/tagged/links).
Bylo to překvapivě jednoduché.
O dost jednodušší, než předtím ten Telegram.

Své _tooty_ si pravidelně zálohuju [do souboru v repozitáři](https://github.com/honzajavorek/honzajavorek.cz/blob/8e2489701f678ee576ebb9ae38ae7b99fbae21e7/content/data/toots-links.json).
Pak už to jen v Pythonu načtu a do poznámek dám ty, které jsem napsal od posledně.

Stejně tak jsem si [začal ukládat](https://github.com/honzajavorek/honzajavorek.cz/blob/8e2489701f678ee576ebb9ae38ae7b99fbae21e7/content/data/toots-replies.json) odpovědi na _tooty_, ve kterých sdílím článek z blogu.
Ještě to nemám hotové, ale chtěl bych je zobrazovat pod články jako komentáře.

A odstranil jsem všude z webu odkazy na Telegramový kanál, aby se tam už nepřidávali další lidi.
Rušit ten kanál ale zatím nebudu.
Dokud mi bude fungovat automatické posílání, tak ho nechám žít.
Pokud se něco rozbije, asi budu mít velmi malou motivaci to opravovat.

## Rušení sociálních sítí

Rozhodl jsem se, že sociální sítě, které jsem skoro před rokem nechal ležet ladem, bych měl nějak „ukončit“.

-   FB skupinu pro „fanoušky junior.guru“ jsem chtěl zrušit, ale nakonec jsem našel nějaké tlačítko _pause_, které umožňuje skupinu pozastavit.
    Tak jsem to udělal, ale vlastně nevím, jestli to má nějaký efekt.
-   Zaslepil jsem účty na Instagramu.
    Do bio jsem napsal, kde jinde mě nebo junior.guru lidi najdou, a dal jsem účty jako _private_.
-   Na svůj FB i Twitter profil jsem dal zprávu, kde jinde mě lidi mohou najít, a tu jsem tam „připnul“.

![Twitter profil]({static}/images/screenshot-2023-09-11-at-23-07-05-honza-javorek-honzajavorek-x.png){: .img-thumbnail }

![FB skupina]({static}/images/screenshot-2023-09-11-at-22-55-30-junior-guru-programatori-zacatecnici-navody-prace-v-it-mentoring-facebook.png){: .img-thumbnail }

![IG profil]({static}/images/screenshot-2023-09-11-at-22-23-08-junior-guru-juniordotguru-instagram-photos-and-videos.png){: .img-thumbnail }

## Nová úvodní stránka

Těsně před PyCon CZ jsem se hecnul a zkusil jsem vyrobit novou úvodní stránku junior.guru.

Cílem bylo udělat cokoliv, co bude lepší než to, co tam je.
Dát si laťku nízko a prostě udělat nejmenší možný krok k něčemu, co bude aspoň o kousek lepší.

![Původní homepage]({static}/images/screenshot-2023-09-12-at-18-20-58-jak-se-naucit-programovat-a-ziskat-prvni-praci-v-it.png){: .img-thumbnail }
Původní úvodní stránka

![Nová homepage]({static}/images/screenshot-2023-09-12-at-18-18-30-jak-se-naucit-programovat-a-ziskat-prvni-praci-v-it.png){: .img-thumbnail }
Nová úvodní stránka

Své odhodlání a postup jsem průběžně sdílel na Mastodon a taky v komunitě [Tvůrcastu](https://tvurcast.cz).
Bylo fajn to mít kde probrat a kde dostat podporu.

Největší radost mám asi z toho nového titulku a sloganu.
Původně jsem tohle ani nechtěl přepsat, ale nějak se to omylem stalo.
Chtěl jsem něco napsat k těm boxíkům níže, ale jak jsem ten text ladil a ladil, tak jsem dospěl k tomu, že přesně tohle má být vlastně napsané rovnou tam úplně nahoře.

Ten kreativní proces za tím byl hodně náhodný (např. mě napadlo že si udělám srandu ze sloganu MasterCard a to mě pak inspirovalo), a o to větší radost mám, jak to dopadlo.
Je tam všechno co potrebuju - člověk okamžitě ví, co ta stránka dělá a k čemu je.
Okamžitě ví, že to není kurz, a přesto mám v největší titulek na webu nejklíčovější slovní spojení na SEO, „kurz programování“ 😀

Zároveň je to rejpnutí do kurzů, což je konzistentní s tím, ze junior.guru je nezávislý hráč, který tak trochu rejpe do všech a snaží se z toho celého dělat menší divoký zapad.
Inspirací mi byla trochu Scrimba, která rejpe hodně.

![Úvodní stránka Scrimby]({static}/images/screenshot-2023-09-12-at-17-29-34-learn-to-code-with-interactive-tutorials-scrimba-com.png){: .img-thumbnail }
Scrimba se s tím nemaže!

Celé jsem to vykutil za jeden pracovní den.
Víc jsem na to neměl, _scope_ jsem jasně ohraničil časem.
Možná bych měl takhle dělat věci častěji 😀

Asi je ale dobré zmínit, že bych to nikdy neměl tak rychle, kdybych to předtím několik let nenosil v hlavě a po kouskách neladil představu, jak to má vlastně vypadat.
Ještě tam toho spousta chybí.
Je to ale lepší, než to, co tam bylo, a to je fajn.

## PyCon CZ

![Společná fotka klubu junior.guru]({static}/images/dscf5781.jpg)
Toto je jen jedna z fotek, které jsme v průběhu konference udělali. Ta nejprofesionálnější 😀

Byl [PyCon CZ 23](https://cz.pycon.org/2023/).
Před konferencí jsem měl velký shon.
Spolu s [Miou](https://www.linkedin.com/in/mia-bajic/) jsme ladili otázky pro panelovou diskuzi.
Chtěl jsem se potkat s [Juhou](https://hamatti.org/) na oběd.
Kamarádka [Domi](https://domicanhelp.cz/) se mnou chtěla naposledy nanečisto zkusit svou přednášku.

Den před konferencí jsem dorazil na místo konání a vymýšlel a instaloval jsem tam nástěnku s [moudry pro juniory](https://junior.guru/wisdom/).
Juha měl dobrý nápad, že by to mohly být takové ty nalepovací papírky (_post-it_).
Myslel jsem, že mi to zabere hodinu, ale zabralo mi to půl dne.
Hledal jsem vhodné místo, navrhoval a tiskl doprovodné letáčky, šel jsem do papírnictví pro materiál, přepisoval vzkazy ve dvou jazycích, lepil to…
S přepisováním a překladem mi pomohli Mia a Timothy.
Odcházel jsem s tím, že to do rána určitě všechno z těch stěn popadá.

![Psaní psaníček]({static}/images/img-5040.jpg)

Další den jsem měl na konferenci vést diskuzní kroužek, ale na jeho přípravu jsem měl nakonec zhruba 10 minut.
Večer byl _speakers' dinner_, kam jsem přišel dost unavený a hladový, ale nakonec to bylo moc fajn.

Během konference to nakonec moc ani nepadalo.
Když jsem šel kolem, snažil jsem se průběžně odchlíplé vzkazy přilepovat.
Až po konferenci jsem si uvědomil, že zvolené místo bylo sice fajn z hlediska toho, že se tam hemžili lidi, ale bylo to na schodech, takže nikdo na vozíku se k tomu nedostal.
Příště na to musím myslet.
Jinak lidi přidávali vzkazy a dostával jsem na to pozitivní zpětnou vazbu, takže se to asi povedlo.

![Psaníčka]({static}/images/img-5124.jpg)

Teď bych měl to, co přibylo, přepsat zase z papírků na web, případně přeložit, pokud je to anglicky.
Leží mi to zatím na stole a nevím, kdy se k tomu dostanu.

Konference byla strašně fajn, ale taky dost náročná.
Asi nemám sílu sem rozepisovat všechny přednášky nebo konverzace, které jsem si užil.
Bylo fajn potkat staré známé po mnoha letech, ale i známé z internetu, které jsem viděl poprvé naživo.

Byl jsem na roztrhání a moc jsem o sebe nepečoval, takže jsem byl po dvou dnech úplně vyšťavený.
Mnohokrát jsem zapomněl na jídlo, nebo jsem si pro něj šel ve chvíli, kdy už nebylo.
Nedával jsem si žádné tiché, introvertní pauzy, a vlastně jsem jen vlál od konverzace ke konverzaci.
Přišlo mi, že znám 80 % účastníků na konferenci, protože jsou buď z Python komunity, z junior.guru, nebo z Namibie.
Což bylo krásné, jak se to celé spojilo v jeden velký guláš, kde se všichni poznávali, ale já jsem byl ve víru toho všeho a fakt jsem se nezastavil.
Ani jsem nedokončil jednu debatu a už mě táhli k další.
A vlastně jsem ani neměl čas vidět moc přednášek, ačkoliv jsem vlastně některé fakt vidět chtěl.

![Domi]({static}/images/img-5112.jpg)

Na Mastodonu a na LinkedIn jsem před konferencí propagoval [sbírku na děti v Namibii](https://mastodonczech.cz/@honzajavorek/111058814539709858).
Domi o tom měla nakonec na PyCon CZ i _lightning talk_.
Napadlo to Miu, a Domi že jo, že to je dobrý nápad.
Když zjistila, že LT jsou v hlavním sále, zmohla se jen na: „oh gosh“
Byla to její první přednáška před větším publikem v životě, ale zvládla to skvěle!
Druhý den měla svou přednášku o Python komunitě v Namibii a ta se taky moc povedla.

![Namibie]({static}/images/img-5125.jpg)

Do toho jsme organizovali srazy junior.guru klubu na dvorečku, kde ze mě dělali úplného sultána 😅
Moc jsem nevěděl, jak s tím naložit, neměl jsem připraveny žádné proslovy, ale dojímalo mě to a byl jsem strašně rád, že se z klubu na konferenci sešlo kolem 30 lidí, že se naživo poznají, a že klub bude najednou zas o něco méně virtuální.

![Sraz klubu]({static}/images/img-5063.jpg)

Na konferenci jsem měl k tomu všemu i svůj vlastní program, který byl sice nenáročný na přípravu, ale i tak to bylo něco, na co jsem se musel soustředit, hlídat si čas, a určitě to byl i stres.

Vedl jsem úplně nový formát, který na PyCon CZ nikdy nebyl, a který jsem nikdy nedělal - [diskuzní kroužek](https://cz.pycon.org/2023/program/panels/122/).
Nevěděl jsem vůbec, co od toho čekat, ale nakonec jsem nějak na místě vymyslel, jak to uvedu a povedu.
Myslím, že to vyšlo skvěle.
Místnost byla narvaná k prasknutí a diskuze jela jako po másle.
Lidi se i ukázněně střídali a nemluvili nijak moc dlouho, nebo se nehádali, takže jsem nemusel nic moc moderovat, jen jsem občas přihodil něco svého a vyvolával jsem, kdo bude mluvit.
Původně jsem nevěděl, jestli není hodina moc, ale vtipně jsme stačili za tu hodinu probrat zhruba jedno z těch deseti témat, které jsem si na to připravil.
Bylo to fakt zajímavé a empatie opravdu tekla proudem.
Zpětná vazba, která se ke mě dostala, byla v podstatě pouze pozitivní, až nadšená.
Jediné, na co si lidi stěžovali, bylo, že to bylo krátké.
Přemýšlím, zda jde takový formát někde zopakovat, protože si myslím, že velkou zásluhu na úspěchu mělo „publikum“.
Koktejl lidí, kteří se na letošním PyConu sešli, byl začátečnickým trackem a velkou účastí členů junior.guru klubu hodně nakloněn k tomu, aby byli na konferenci jak junioři, tak senioři, které navíc junioři zajímají 😀

![Diskuzní kroužek]({static}/images/p-20230915-130713.jpg)
Najdete mě na fotce?

Další věc, které jsem se účastnil, byla [panelovka](https://cz.pycon.org/2023/program/panels/87/).
Ta byla myslím taky zajímavá.
Konečně jsem naživo potkal yablka.
I když jsem si tématem panelovky nebyl původně zcela jistý, nakonec to celkem sedlo.
Každý jsme měli trochu jiné názory, Lucie házela bomby, yablko to měl krásně člověčí, Šárka - juniorka - nám rozbíjela hračky a mluvila z pozice té, která neháže moudra z obláčku, ale žije ty věci.
Jak jsem mluvil já, to nechť vyhodnotí někdo jiný 😀
Zpětná vazba?
Udělal jsem vtip, že vyhořelí seniorní ajťáci odcházející z oboru by potřebovali nějaké „senior.guru“ a pak si mě odchytil borec, který by takové „senior.guru“ chtěl udělat, protože má zkušenosti s psychologickou pomocí vyhořelým lidem.
Taky se prý líbilo, když jsem naznačil, že senioři peníze už moc neřeší, že řeší akorát to, jestli budou mít v práci jogurty zdarma.
A že jestli senior dostává 100 nebo 120 tisíc, to je mu docela jedno, ale jestli junior dostává 30 nebo 50 tisíc, to mu fakt jedno není.

![Panelovka]({static}/images/14ce3350-ce61-46b8-8296-b849850a2de3.jpg)

Akorát škoda, že těsně před PyConem dcera dostala ukrutnou rýmu, takže nevyšel plán, že tam se ženou budou a že se budem nějak střídat, aby si taky užila staré známé.
Jeden den vůbec nešli, druhý jen na chvilku.
Perfektní _child care_, který na konferenci byl, jsme ani nestihli využít.

Závěr konference byl, jako vždy, [dojemný](https://www.youtube.com/watch?v=1kaJPyTDghY).
Doufám, že tahle akce Python komunitu v Česku nakopne a budou noví dobrovolníci na spoustu krásných věcí, aby si ti staří mohli po covidu, kdy to často táhli z posledních sil, konečně odpočinout.

![Hraní]({static}/images/img20230917034445.jpg)
Kluci hrajou na struny, já buším na mini [cajón](https://cs.wikipedia.org/wiki/Caj%C3%B3n), který ale na fotce není vidět, tak tam vypadám asi dost směšně.

Co jsem měl možnost pozorovat, zpětná vazba na PyCon CZ všude možně po sociálních sítích i při osobním kontaktu byla extrémně pozitivní.
Během konference jsem měl pocit, že organizační tým dobrovolníků maká jak mravenci a nezastaví se od pěti ráno do půlnoci.
Tak snad je potěší, že to stálo za to.
Že se díky nim letos PyCon CZ po dlouhé covidové pauze vrátil ve velkém, grandiózně, se vší parádou, a že se to strašně moc lidem fakt strašně moc líbilo.
Asi nejlépe to celé ilustruje [tenhle _toot_ od Miro Hrončoka](https://floss.social/@hroncok/111092967515065846).

## Dovolená

![Naložené kolo]({static}/images/img_5391.jpeg)
Jak jezdíte na dovolenou vy? Taky balíte dva dospělé a dvouleťáka do kombíka?

Hned po konferenci jsme se sbalili a odjeli na dovolenou.
Sbalili jsme se na kolech, malou jsme vzali do cyklosedačky.
Vlakem jsme se dopravili k Třeboni a tam jsme byli na statku s krávama a ovcema a především polopenzí.
Myslím, že tenhle styl dovolené byl mnohem víc dovolená, než ta Itálie na jaře, a že jsme si tam mnohem víc odpočinuli.

Možná by byla dovolená autem jednodušší. Zabalit dva dospělé a dvouleťáka na kolo není jen tak.
Ale stále nám to takhle nepřijde zásadní opruz na to, abychom řešili auto.
Nechám se překvapit, jestli příští dovolená bude s carsharingem, nebo přikoupíme velké zadní brašny.

Během dovolené jsem zjistil, že přednáška naplánovaná na další úterý se nějak hroutí.
Rozhodl jsem se, že to nebudu řešit a prostě jsem ji posunul, abych měl na dovolené klid.
Jsem na sebe hrdý, že jsem se nenechal strhnout do módu „mimořádná událost, tohle musím řešit i na dovolené“.

## Dohánění po dovolené

Když jsem se vrátil z dovolené, čekala na mě záplava mailů a nepřečtených zpráv všude možně.
Začal jsem taky chodit na léčbu, kterou mám každý den po obědě.

V rámci prokrastinace jsem se postaral o přijetí nového člena do Pyvce, [aktualizoval dokumentaci české Python komunity](https://github.com/pyvec/docs.pyvec.org/pull/345), apod.

Po týdnu se mi povedlo projít maily, ale klub ještě celý přečtený nemám.
Přivedlo mě to na myšlenku, zda bych neměl upustit od toho, že čtu v klubu všechno, protože to už možná není udržitelné.
Měl bych se nejspíš naučit prostě některé konverzace přeskočit a neřešit.

Řešil jsem prodloužení partnerství s Red Hatem.
K tomu [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, apod.
[Promoval jsem](https://www.linkedin.com/feed/update/urn:li:activity:7112710388894289921/) svůj nadcházející talk na [Frontkonu](https://frontendisti.cz/konference), další konferenci, která se blíží.

Na Frontkon si mám do včera připravit slajdy, takže jsem je ještě dnes dodělával.
Je 22:30 a stále jsem je ještě neposlal.
Pak mám ještě tři lístky do soutěže pro klub, tak to udělám asi příští týden.
Soutěž jsem neřešil, protože jsem měl PyCon CZ a dovolenou, během toho ale stoupla jejich cena, protože Frontkon se mezitím vyprodal 😀

Na Václava jsme se jeli s Mílou projet na kole, ale trochu jsme to možná přestřelili, protože dnes se nemohu hýbat.
Mám pocit, že po týdnu řešení e-mailů, zpráv a nejrůznějšího promování a domlouvání schůzek potřebuji zase dovolenou.
Ale bude teď víkend, tak snad mě to trochu osvěží.
A příští týden musím zase něco naprogramovat, u toho si odpočinu.

![Na kole]({static}/images/img-5473.jpg)

## Další

-   Vláda konečně spustila web [Týdnu pro Digitální Česko](https://budoucnostjedigitalni.gov.cz/)!
    A junior.guru je partner, protože budu v rámci toho pořádat Q&A na YouTube. Stejnou, jako jsem dělal už jednou na jaře, ale tentokrát v rámci této celorepublikové akce pro širokou veřejnost, tak jsem na to dost zvědavý 😅
    Taky jsem se nechal ukecat, že tam půjdu do nějakého panelu.
    Budou v něm i lidi z MPSV, takže je otázka, jestli tam budu mít co říct, nebo budu jen [zpívat](https://www.youtube.com/watch?v=jz9w0wv9EBw).
    Logo TDČ jsem dal mezi další partnerská loga [na stránku o klubu](https://junior.guru/club/).
-   Přišla nám postel pro dceru, tak jsem ji s ní postavil.
    Pak jsme ještě celá rodina předělávali organizaci ložnice, aby se tam všechno vešlo.
    Při té příležitosti jsem vyčistil všechny podlahy v bytě.
-   Zjistil jsem, že vítací kanály s tipy pro nováčky jsou nějaké pokažené.
    Nechci to opravovat, chci to celé předělat.
    Tak snad se k tomu brzo dostanu.
-   Když jsem něco promoval, dával jsem to na LinkedIn a na Mastodon.
    Nevím, jaký to má na Mastodonu dosah, ale pár lidí to tam asi čte.
    Účet nemám dlouho, tak uvidím, jaké publikum se tam nabalí.
    Můj odhad je, že tam budou spíš senioři, kteří mi fandí, a které bude zajímat zákulisí toho, jak junior.guru vyrábím.
    Zkouším tam občas něco dát i z toho zákulisí, ale nevím, jak dlouho to vydržím dělat, protože pak skoro totéž píšu i sem do poznámek.
    Tam mám zase rychlou odměnu, pokud na to někdo reaguje, nebo to lajkne.
-   Začal jsem pár korunami pravidelně přispívat [Davidu Klimešovi na jeho newsletter](https://davidklimes.cz/).
-   Oslavili jsme narozeniny.
    Dostal jsem super nová světla na kolo!
-   Zjistil jsem, že existuje [Consent-O-Matic](https://github.com/cavi-au/Consent-O-Matic), ale nevím, jestli dobře funguje pro české weby.
    Každopádně je fajn, že to jde nainstalovat i do iPhonu.
-   Měl bych se kouknout, jestli mi [tohle](https://fedi.simonwillison.net/@simon/111054918019075740) nepomůže s paralelizací na CI, když sestavuji webovku junior.guru.
    Teď to dělám tak, že se paralelně zapisuje do různých SQLite a ty se pak nějakým mým vlastním algoritmem sloučí.
    Pokud bych mohl použít něco, co už někdo vymyslel, tak by to bylo ideální.
-   Nabídl jsem DigiKoalici pomoc s jejich [katalogem kurzů](https://digikoalice.cz/kurzy/), pokud by je napadlo, jak si můžeme pomoci.
    Taky jsem jim psal ještě kvůli partnerství v jedné věci, ale zatím bez odpovědi.
-   Opravil jsem report, který mi chodí o končících členech klubu.
    Původně se mi to posílalo jen v případě, že vyplnili nějakou textovou zpětnou vazbu, ale upravil jsem to tak, aby se mi to posílalo vždycky.
    Díky tomu mám přehled, když mi odchází konkrétní lidi, nebo pokud někdo ruší členství proto, že je pro něj moc drahé.
-   Dělal jsem kamarádce code reviews na [realtime botovi](https://github.com/juniorguru/juniorguru-chick/).
    Povedlo se jí tam přidat pár nových fičur, je to super.
    Sice se na chvíli něco i rozbilo, ale nebyl to problém.
    Aspoň jsem si otestoval, že lidi tu fičuru používají, chtějí, a že se svět nezboří, ani když jsem na dovolené.
-   [Čtvrtkon](https://ctvrtkon.cz/) má nový web a s ním i nové API, přes které jde sosat budoucí události.
    Přidal jsem to tedy do klubu a vždy, když mají novou událost, objeví se i v klubu na Discordu.
-   Smazal jsem [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) na úkor [Draw Things](https://drawthings.ai/).
    Na macOS nemá smysl používat nic jiného, je to bezkonkurenční.
-   Během 22 dní jsem na túrách nachodil 7 km, ujel na kole 146 km. Celkem jsem se hýbal 20 h a zdolal při tom 153 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Udělat soutěž na Frontkon.
2.  Překopat kanály s vítacími tipy v klubu.
3.  Publikovat success story s Romanem Viktorem Dvořákem.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to na [svém Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [The End of the Subscription Era is Coming - Nick Hilton - Medium](https://nickfthilton.medium.com/the-end-of-the-subscription-era-is-coming-ed197f252c6a)<br>Soumrak předplatných a ekonomiky tvůrců?
- [London to Prague by train | Times, fares, how to buy tickets](https://www.seat61.com/Czech.htm)<br>Neznal jsem. Borec z Londýna, který roky jezdí po světě vlakama a píše na web tipy jak na to.
- [Eliška a Damián jako nejhorší seriál všech dob? Spíš slavnost bezvýznamnosti](https://www.seznamzpravy.cz/clanek/kultura-eliska-a-damian-jako-nejhorsi-serial-vsech-dob-spis-slavnost-bezvyznamnosti-237176)<br>„Penetruje a podmaní si opět jednoho dne klasika postmodernu?“ Fila o Elišce a Damiánovi.
- [AskHistorians Podcast Episode 212 – Public Transport in North America with Jake Berman — The AskHistorians Podcast](https://askhistorians.libsyn.com/askhistorians-podcast-episode-212-public-transport-in-north-america-with-jake-berman)<br>Proč USA a Kanada téměř nemají MHD? Způsobila to složitá kombinace faktorů, která navíc byla v každém městě jiná. Na začátku soukromé monopoly provozující a ruinující MHD (mafie included), a potom 2. světová, po které nebyla Amerika zničená. Měli čas a peníze realizovat utopistické plány, tak všude postavili dálnice.
- [Pod čarou: Není nutné mít koníčky. Natož si z nich dělat práci](https://www.seznamzpravy.cz/clanek/nazory-komentare-pod-carou-neni-nutne-mit-konicky-natoz-si-z-nich-delat-praci-236604)<br>„Pokud si tedy odmítneme z koníčku udělat práci s tím, že by se z něj vytratila radost a spontánnost, je to jistě dobře, ale jde jen o začátek hlubší reflexe. Musíme se totiž sami sebe ptát i na to, proč a jak v nás vlastně díky koníčkům ona radost vzniká.“
