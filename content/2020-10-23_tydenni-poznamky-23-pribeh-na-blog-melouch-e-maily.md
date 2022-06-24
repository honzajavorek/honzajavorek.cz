Title: Týdenní poznámky #23: Příbeh na blog, melouch, e-maily
Image: images/hrobky.jpg
Lang: cs
Home: False


Utekly dva týdny (12.10. — 23.10.) a [stejně jako minule]({filename}/2020-10-09_tydenni-poznamky-novy-vzhled-stranek-s-nabidkami-prace.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

## Minulý týden

Minulý týden jsem byl na dovolené v Krkonoších. Bylo tam hnusně a většinu času jsme se ženou četli [knihy](https://www.goodreads.com/user/show/16842985-honza), hráli [hry](https://store.steampowered.com/app/236850/Europa_Universalis_IV/), nebo se na něco dívali. Bylo to ale super a kdybychom nejeli teď, asi by nám dovolená zůstala do konce roku nevybraná, nebo bychom ji museli nějak vybrat v době lockdownu a temna (krátké dny).

![Krkonoše]({static}/images/krkonose.jpg)
Černohorské rašeliniště

## Tento týden

Tento týden nějak utekl, ani nevím jak. Vzal jsem jeden malý melouch pro kamaráda, připravit podhoubí pro nějaké jejich Python balíčky. Myslel jsem, že to bude na pár hodin, ale vypadá to, že stav balíčkování v Pythonu, byť to pokročilo, je stále strašný - zkuste si např. udělat poetry balíček, který ale půjde nainstalovat i jako editable… Dnes (v pátek) jsem se moc nevyspal, celé dopoledne debugoval balíčky, odpoledne zjistil, že to stejně nefunguje, rozlil jsem kafe po celém stole a nestíhal dokončit e-maily (viz další sekce), ale naštěstí mě kamarád vzal na procházku Olšanskými hřbitovy a tam jsem se nějak uklidnil.

![Hrobky]({static}/images/hrobky.jpg)
Vždycky může být hůř

## E-maily

Jak jsem tady už dříve psal, SendGrid mi nedoručuje maily spolehlivě a já si vyhodnotil, že vzhledem k počtu, který posílám, bych jej mohl nahradit Gmailem. Našel jsem knihovnu [yagmail](https://github.com/kootenpv/yagmail) a tento týden jsem se na to chtěl podívat.

Knihovnu jsem nakonec nepoužil, rozhodl jsem se prostě a jednoduše posílat ty maily přes SMTP. Odebral jsem tedy SendGrid a použil [smtplib](https://docs.python.org/3/library/smtplib.html) a [email](https://docs.python.org/3/library/email.html), které jsou přímo ve standardní knihovně v Pythonu. Pokud máte zapnuté 2FA, musíte si pro připojení ke googlímu SMTP [vygenerovat aplikační heslo](https://security.google.com/settings/security/apppasswords). Pak už to funguje jako každé jiné posílání mailů z Pythonu.

Blbé je, že [email](https://docs.python.org/3/library/email.html) zjevně prošel nějakým překopáním a má nový interface a starý interface. Návodů na ten starý je plný internet a všechno se to motá dohromady. Navíc ta dokumentace, tak jak je ve standardní knihovně, je strašná. Totální _wall of text_ a jako by to psal nějaký maniak, který si myslí, že chci vědět úplně všechno o MIME. Je tam naštěstí [pár příkladů](https://docs.python.org/3/library/email-examples.html), ale i s nimi je to za trest, pokoušet se s tím něco vyrobit. Přitom ten interface asi není špatný, jen je pro laika složitý a chybí nějaký 1 2 3 tutoriál jak rychle udělat, co potřebuju, i bez toho, abych přečetl pět RFC.

Každopádně tohle celé mě trochu motivovalo překopat moje posílací skripty. Oddělil jsem od sebe hlavně logiku vytváření zpráv a logiku debugování odesílání e-mailů. Mělo by to teď být testovatelnější, méně by se měl opakovat kód a mělo by to všechno být míň zamotané do sebe. Objekt [EmailMessage](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage) jsem původně chtěl použít napříč programem, ale nakonec jsem vyhodnotil, že je tak blbě zdokumentovaný a tak málo abstrahuje detaily MIME specifikace, že budu raději jednotlivé zprávy připravovat jako obyčejný slovník a tuhle věc vytvořím až těsně před odesláním. Výhodou je, že ten objekt nemusím už dále studovat a můžu ty skripty jednodušeji testovat.

Tož uvidíme v pondělí, co všechno jsem rozbil a kolik se toho pošle. Taky bych si měl na to asi vytvořit nějakou speciální Gmail schránku, aby mi Google nezablokoval osobní účet, kdyby mi někde ujela nekonečná smyčka a omylem jsem poslal tisíc mailů, ale na to už tento týden nebyl čas.

## Další poznámky

- Ze [své homepage](https://honzajavorek.cz) jsem odebral týdenní poznámky, moc to tam plevelily. Na [homepage blogu](https://honzajavorek.cz/blog/) zůstávají všechny články.
- Jelikož je z poznámek už celkem tradice a nezařízl jsem to po pár týdnech, přidal jsem si do skriptu pro jejich generování i číslování. Toto jsou tedy poznámky číslo 23.
- Mám nové doporučení od juniora, který přečetl příručku. Zatím si ty doporučení skladuji [sem](https://junior.guru/hire-juniors/#handbook), než vymyslím, jak je jednou zobrazím lépe. Nové doporučení je pod číslem čtyři.
- Na radu z dopisů čtenářek jsem přidal do [sekce o angličtině](https://junior.guru/learn/#english) Italki. Vím, že existuje i Blabu, ale nevím, jaký je mezi nimi rozdíl. Všichni kolem mě jedou Italki. Já nepoužívám ani jedno.
- Na radu kamaráda jsem přidal k Italki i Duolingo také affiliate odkazy. Přidávají kredit jak mě, tak vám. Jsou vždy v popisku jako bonus, odkaz přes obrázek vede normálně bez affiliate. Protože Italki nepoužívám, dal jsem tam pozvánkový odkaz z účtu bráchy, jehož děti Italki používají dost a učí se přes to jazyky. Pokud teda chcete Italki zkusit, můžete jít přes [tento odkaz](https://www.italki.com/i/6fGdDG?hl=en-us) a budete mít $10 slevu a bude ji pak mít i můj brácha.
- Pořešil jsem zase po nějaké době upgradování dependencies na pár Pyvec projektech.
- Přišel mi [Pull Request na fiobank knihovnu s nějakou opravou](https://github.com/honzajavorek/fiobank/pull/25), tak jsem to mergnul. U toho jsem zjistil, že se knihovna nereleasuje a Travis CI nějak nefunugje, takže jsem to pak celé ještě opravoval a releasoval.
- Přidal jsem na JG [příběh o Páji](https://link.medium.com/C0YDsBUErab), která prošla PyLadies a pak ji vzali do Irska do Facebooku. Je [mezi ostatními na hlavní stránce](https://junior.guru/#stories).
- Během mého pobytu v Krkonoších vyšel článek o [příručce](https://junior.guru/candidate-handbook/) na CzechCrunch, juchů! [Boření mýtů a užitečné rady pro každého začátečníka. Honza Javorek vydává příručku o hledání první práce v IT](https://www.czechcrunch.cz/2020/10/boreni-mytu-a-uzitecne-rady-pro-kazdeho-zacatecnika-honza-javorek-vydava-prirucku-o-hledani-prvni-prace-v-it/). Už bych si měl založit sekci "napsali o nás". Zatím jsem jen přidal logo CzechCrunch [sem](https://junior.guru/hire-juniors/). Vlastně jsem ho jen odkomentoval, protože jsem ho tam přidal už dřív a jen jsem čekal, až článek vydají :D
- Jeden junior mi napsal delší e-mail o tom, zda bych mu neporadil s kariérním směřováním. Poradil jsem mu, nějakou tu hoďku mě to stálo. Nic jsem si za to nevzal, protože zatím jen zkoumám terén - pokud by takto junioři chodili nějak častěji, možná bych z toho vytvořil nějaký produkt nebo to prostě nabízel jako službu, ale zatím toho není dost a nevidím v tom ani úplně nějaký vzorec.
- Jiný junior se mě v podobném duchu zeptal, zda bych neprošel jeho CV a LinkedIn a nepomohl mu to vyladit. Pověnoval jsem se tomu, zabralo to několik hodin a ještě jsme to pak spolu probírali dlouho do večera. Sám jsem nevěděl, co od toho čekat. Překvapilo mě, jak relevantní rady jsem mu vlastně dokázal dát :D Je to pro mě potvrzení, že toto bych mohl dělat i za peníze. Zatím jsem to udělal tak, že mi může dotyčný poslat na můj [donate účet](https://junior.guru/donate/) tolik, kolik si myslí, že si zasloužím.
- Domluvil jsem si jednu malou přednášku o JG pro účastníky jednoho bootcampu. Blbé je, že teď ji budu muset připravit :) Naštěstí je na to celkem dost času.
- Úplně omylem jsem na ČT zahlédl reportáž o tom, [jak Radůza uvažuje i o kurzu webových stránek](https://ct24.ceskatelevize.cz/kultura/3208318-raduza-mozna-vymeni-harmoniku-za-tu-autobusovou-i-dalsi-umelci-si-hledaji-jinou). Byl bych raději, kdyby Radůza mohla hrát a zpívat, ale doba je, jaká je, takže jsem jí napsal e-mail, ať mrkne na JG, protože tam všechno najde. Zatím to vypadá jako jeden z mnoha e-mailů, které jsem někam někomu naslepo napsal, a na které nikdy nedostanu odpověď, ale asi mě to baví zkoušet :) Třeba z toho někdy bude nějaká haluz.
- Ozval se mi borec, kterého jsem před rokem náhodou potkal v čajovně, že je z něj teď teda programátor a všechno to hezky sepsal do článku. Domluvili jsme se, že jej vydáme na blogu Python komunity a tak se i stalo. Než jsme vše doladili, pár hodin si to vzalo. [Programátorem za 365 dní a zadarmo? Tak určitě!](https://blog.python.cz/programatorem-za-365-dni-a-zadarmo-tak-urcite). Přidal jsem to hned po vydání i [na hlavní stránku](https://junior.guru/#stories) JG mezi příběhy.
- Když už jsem byl na blogu, zahléhl jsem tam [rozpracovaný článek od Baru z Kanady](https://github.com/pyvec/blog.python.cz/pull/69). Řekl jsem si, že to zkousím prošťouchnout. Nic jsem od toho nečekal, ale Baru se ozvala a článek nejspíš doděláme! To by byl hned další příběh hodný hlavní stránky JG :)

![CzechCrunch]({static}/images/czechcrunch.jpg)


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Dneska je toho logicky víc, protože je to za dva týdny, z nichž jeden jsem se jen válel a četl věci. Od posledních poznámek jsem sdílel toto:

- [Další SPECIÁL se vzácným hostem a výslovnost hudebních nástrojů v angličtině!](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dn27PZDg64bI&h=291f02a930ca53fae3780028ff812d7e523de78428f8f172ef2ae2fc2d87792d)<br>Tenhle YouTube kanál už chvíli sleduju a přijde mi to jako fajn způsob, jak si zkusit vylepšovat výslovnost.
- [THE TYRANNY of STRUCTURELESSNESS](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.jofreeman.com%2Fjoreen%2Ftyranny.htm&h=74e000b1a909f114989c554ec7cbbadc61f7f9737d66b066eb3f55d058f8b108)<br>Já už jsem to četl dávno, ale vy jste to určitě ještě nečetli! Teď to na mě vyskočilo na Twitteru, takže mě napadlo to nasdílet sem. Je to perfektní text o tom, jaké nevýhody mají organizace tvářící se jako nehierarchické a rovnostářské. K vidění na vašem pracovišti nebo ve vaší zájmové komunitě.
- [Ozonový alarmismus a ozonová skepse](https://getpocket.com/redirect?&url=https%3A%2F%2Fvesmir.cz%2Fcz%2Fcasopis%2Farchiv-casopisu%2F2020%2Fcislo-7%2Fozonovy-alarmismus-ozonova-skepse.html&h=89eedaa39ffc0b892703d075eea03047ade5132a3ea89bb043501878d0b84a0a)<br>“Ozonová krize si prošla povědomým cyklem: jev neexistuje – jev není způsoben člověkem – řešení způsobí více škody než užitku”
- [Please stop using CDNs for external Javascript libraries](https://getpocket.com/redirect?&url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2020%2F10%2Fplease-stop-using-cdns-for-external-javascript-libraries%2F&h=617f8a5b4dcc1770d53912db71f75c8ab214a8f16ed4308cfa9b9b340cce5699)<br>Používání JS knihoven z CDN je přežitek
- [Chřipková epidemie v roce 1995 si v České republice nevyžádala 12 000 mrtvých](https://getpocket.com/redirect?&url=https%3A%2F%2Fnapravoumiru.afp.com%2Fchripkova-epidemie-v-roce-1995-si-v-ceske-republice-nevyzadala-12-000-mrtvych&h=1f28ca09c6ac1af7189614b62e127b83dc25f5b8828941d9af3e83b8e2dd4e64)<br>Dvojsmyslná formulace způsobila hoax o 20 let později
- [Boření mýtů a užitečné rady pro každého začátečníka. Honza Javorek vydává příručku o hledání první práce v IT](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.czechcrunch.cz%2F2020%2F10%2Fboreni-mytu-a-uzitecne-rady-pro-kazdeho-zacatecnika-honza-javorek-vydava-prirucku-o-hledani-prvni-prace-v-it%2F&h=660384da77c958745aede0b5672084e2b54fc19b3d782cbd6d2a6c8eb4921bb3)<br>Příručka na CzechCrunch! 🤩 V článku najdete takové TL;DR příručky a hlavně je v něm zdůrazněno, co jsou ty opravdu nejdůležitější věci a co jsou ty největší mýty.
- [The culture war at the heart of open source](https://getpocket.com/redirect?&url=https%3A%2F%2Fsteveklabnik.com%2Fwriting%2Fthe-culture-war-at-the-heart-of-open-source&h=8714b92bcf083f605d95dad36664897f9168586807be0956078b1f343724f327)<br>Free Software vs Open Source a co bude dál?
- [Michal Bláha: Premiére, ministři, žaluji vás, selhali jste](https://getpocket.com/redirect?&url=https%3A%2F%2Fhlidacipes.org%2Fmichal-blaha-premiere-ministri-zaluji-vas-selhali-jste%2F&h=ee022b961968d1ee1a63f7ae187eb8b035a09a8db268949dd0206f2b7d997760)<br>Michal Bláha dovozuje přímou zodpovědnost konkrétních lidí za současný stav.
- [Pokud nezměníme kurz, živí budou závidět mrtvým](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikn.cz%2F450196%2Fpokud-nezmenime-kurz-zivi-budou-zavidet-mrtvym%2F&h=9a874263fd748b0a7a6ca479d132a26b1d4e12dc49d459463bfbc196e400efc7)<br>Covid-19 je jen trailer na to, co teprve přijde.
- [Proč nediskutovat s rasisty, antisemity a xenofoby](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikn.cz%2F283027%2Fproc-nediskutovat-s-rasisty-antisemity-a-xenofoby%2F&h=c9d083de737cb118e1632b5a817711cdc9affd376bdf22e1dbaf581d645db1b3)<br>Já osobně s lidmi vždy spíš diskutuju, než abych je na první dobrou odsoudil. Je to ale vždy ten nejlepší přístup? Naštěstí se osobně setkám spíše s obětmi dezinformací než prapůvodci nenávisti.
- [Ještě jednou o tom, zda diskutovat s hlasateli nenávisti](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikn.cz%2F288211%2Fjeste-jednou-o-tom-zda-diskutovat-s-hlasateli-nenavisti%2F&h=465a2378ecbc1a17942216bdd4bee82ea1b988a425ca13abf77b0b8ccef54e6f)<br>Druhý díl předchozího komentáře (který mě ujistil, že jsem ten první pochopil správně)
- [Babiš může být v klidu, Trump si jde pro znovuzvolení i přes mrtvoly v chladicích návěsech. Na vlastní selhání populisté nedoplatí](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikn.cz%2F439836%2Fbabis-muze-byt-v-klidu-trump-si-jde-pro-znovuzvoleni-i-pres-mrtvoly-v-chladicich-navesech-na-vlastni-selhani-populiste-nedoplati%2F&h=344fb882202fa7e9ff50e389ad503d495d38f3783c0a8bb932069eab9020e30a)<br>Pokud čekáte, že covid-19 Babiše smete, možná čekáte marně. Může se udržet i přes mrtvoly. Skvělý rozbor!
- [Čekání na koronavirovou katastrofu: reportáž novináře, který uvízl v nešťastném koutě Jižní Ameriky](https://getpocket.com/redirect?&url=https%3A%2F%2Fdenikn.cz%2F323287%2Fcekani-na-koronavirovou-katastrofu-reportaz-novinare-ktery-uvizl-v-nestastnem-koute-jizni-ameriky%2F&h=03ca36214b52fdaf186acbfaaa6d1de63ce17efb7def8ea7504c68ac45712147)<br>Ať se u nás bude dít teď cokoliv, vzpomeňte si, co se asi v tu chvíli děje ve Venezuele.
- [Tajemný muž, který na jaře „zachránil Česko“? Exředitel České pojišťovny](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Ftajemny-muz-ktery-na-jare-zachranil-cesko-exreditel-ceske-pojistovny-124767%23dop_ab_variant%3D0%26dop_req_id%3Dji937Jy8uNN-202010170614%26dop_source_zone_name%3Dzpravy.sznhp.box%26source%3Dhp%26seq_no%3D1%26utm_campaign%3D%26utm_medium%3Dz-boxiku%26utm_source%3Dwww.seznam.cz&h=8c7835d57ff72f08f5d7be70e33ad74e5be19d95022a44024432650458d09ed2)<br>Už to sdíleli asi všichni, tak to teda sdílím i já, i když je to hlavně reklama na knihu. Pokud je tohle pravda, je to fakt šílený.
- [Meanwhile in CZECHIA](https://getpocket.com/redirect?&url=https%3A%2F%2Fyoutu.be%2FhJ800HrNrv8&h=6c401af6c8761dcac5e101f99a58ff23216abd5384994d722e374e54c7f0635f)<br>Pobavilo
- [Making data accessible to everyone at Productboard](https://getpocket.com/redirect?&url=https%3A%2F%2Flink.medium.com%2FC0YDsBUErab&h=f381230e00204bab2e2973d9857efb07ecf933504e64a685a91e19937f428bdd)<br>Článek o Páji z PyLadies v Praze! Pracovala jako analytička, naučila se díky PyLadies Python, spoluorganizovala pražské kurzy PyLadies, vzali ji do Facebooku, dnes pracuje v ProductBoardu s daty.
- [Jsou všichni ajťáci k0k0t1?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fjak-recruite%25C5%2599i-sm%25C3%25BD%25C5%25A1lej%25C3%25AD-o-aj%25C5%25A5%25C3%25A1c%25C3%25ADch-pavel-%25C5%25A1imerda%2F&h=9b5b1c50920f7a07c6ddde45d9da4f8729ddc303b40d8768321ac1631e60e45a)<br>Recruiterské hvězdy si v podastu vylily srdíčko o tom, jak je nábor v IT hrozný. Martina znám, je v podcastu jako host a jeho výroky mě velmi nepobuřují. Naopak mi přijde, že se skoro nedostává ke slovu a dvojici moderátorů ve výrocích spíš mírní. Ti dva ale působí jak prodejci amway v umělohmotných oblecích, kteří si na pivu honí ega nad tím, jací kokoti jsou lidi, kterým prodávají. Věřím, že takhle mohlo HR vypadat v devadesátkách, ale dnes? Doufám, že Martin se z této kauzy oklepe a že o těch dvou už nikdy neuslyšíme. Podcast s osudovým číslem 42 zatím stáhli ze všech platforem, [poslechnout si jej lze na už jediné](https://talk.youradio.cz/porady/nelidske-zdroje/42-jsou-vsichni-ajtaci-k0k0t1-s-it-recruiterem-martinem-gazem), ale je asi jen otázka času, než zmitzí i tam.
- [Nebezpečný domov - osobnosti pro ACORUS](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DuvuiHYu9a5w%26feature%3Dyoutu.be&h=38d987f0f4aeeaeb927ff68490e78cb2db37182a9270331ef1c0cffa39dd6c6b)<br>Lockdown zvyšuje pravděpodobnost domácího násilí. Nebojte se zavolat policii, nechat pachatele vykázat a zabránit mu v dalším násilí.
- [Válka jako obchodní artikl. Česká zahraniční novinařina, „attention whores" a prodej emocí — HlídacíPes.org](https://getpocket.com/redirect?&url=https%3A%2F%2Fhlidacipes.org%2Fvalka-jako-obchodni-artikl-ceska-zahranicni-novinarina-attention-whores-a-prodej-emoci&h=b8df8c1005c1274bb7354d44e8cf7e986640e791b59d7cbcb40141744eb844ef)<br>Zajímavý komentář k práci Markéty Kutilové a Lenky Klicperové
- [Testosteronové mýty. Proč na jeden hormon svádíme mužnost, agresivitu i charakter](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.heroine.cz%2Fspolecnost%2F3261-testosteronove-myty-proc-na-jeden-hormon-svadime-muznost-agresivitu-i-charakter%3F&h=ec4861d8d1fe98da9db6590b289f61abae684169e4ed22a0951b1b2a4489e288)<br>Zajímavý článek o tom, co je a a co není způsobeno testosteronem
- [How Discord Won](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2FDCnxXVAu7w%3Fssr%3Dtrue&h=2ce99b6c6ba3229169ad060a9453b3b83176ce0c67cc07713086f90e8ab7a9bc)<br>Konečně mi někdo vysvětlil Discord
- [Neviditelné pouště v regionech, které dusí českou demokracii](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2FgDl3evswYO%3Fssr%3Dtrue&h=7f4fb0aa847424e3a0f34699463cbe4a55be2f975b0b21bb8c555cd4b87817b3)<br>Proč mizí lokální média a proč je to špatně

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>