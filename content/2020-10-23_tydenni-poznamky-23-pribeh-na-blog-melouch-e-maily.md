Title: Týdenní poznámky #23: Příbeh na blog, melouch, e-maily
Image: images/hrobky.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekly dva týdny (12.10. — 23.10.) a [stejně jako minule]({filename}2020-10-09_tydenni-poznamky-novy-vzhled-stranek-s-nabidkami-prace.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

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

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Dneska je toho logicky víc, protože je to za dva týdny, z nichž jeden jsem se jen válel a četl věci. Od posledních poznámek jsem sdílel toto:

- [Další SPECIÁL se vzácným hostem a výslovnost hudebních nástrojů v angličtině!](https://www.youtube.com/watch?v=n27PZDg64bI)<br>Tenhle YouTube kanál už chvíli sleduju a přijde mi to jako fajn způsob, jak si zkusit vylepšovat výslovnost.
- [THE TYRANNY of STRUCTURELESSNESS](https://www.jofreeman.com/joreen/tyranny.htm)<br>Já už jsem to četl dávno, ale vy jste to určitě ještě nečetli! Teď to na mě vyskočilo na Twitteru, takže mě napadlo to nasdílet sem. Je to perfektní text o tom, jaké nevýhody mají organizace tvářící se jako nehierarchické a rovnostářské. K vidění na vašem pracovišti nebo ve vaší zájmové komunitě.
- [Ozonový alarmismus a ozonová skepse](https://vesmir.cz/cz/casopis/archiv-casopisu/2020/cislo-7/ozonovy-alarmismus-ozonova-skepse.html)<br>“Ozonová krize si prošla povědomým cyklem: jev neexistuje – jev není způsoben člověkem – řešení způsobí více škody než užitku”
- [Please stop using CDNs for external Javascript libraries](https://shkspr.mobi/blog/2020/10/please-stop-using-cdns-for-external-javascript-libraries/)<br>Používání JS knihoven z CDN je přežitek
- [Chřipková epidemie v roce 1995 si v České republice nevyžádala 12 000 mrtvých](https://napravoumiru.afp.com/chripkova-epidemie-v-roce-1995-si-v-ceske-republice-nevyzadala-12-000-mrtvych)<br>Dvojsmyslná formulace způsobila hoax o 20 let později
- [Boření mýtů a užitečné rady pro každého začátečníka. Honza Javorek vydává příručku o hledání první práce v IT](https://www.czechcrunch.cz/2020/10/boreni-mytu-a-uzitecne-rady-pro-kazdeho-zacatecnika-honza-javorek-vydava-prirucku-o-hledani-prvni-prace-v-it/)<br>Příručka na CzechCrunch! 🤩 V článku najdete takové TL;DR příručky a hlavně je v něm zdůrazněno, co jsou ty opravdu nejdůležitější věci a co jsou ty největší mýty.
- [The culture war at the heart of open source](https://steveklabnik.com/writing/the-culture-war-at-the-heart-of-open-source)<br>Free Software vs Open Source a co bude dál?
- [Michal Bláha: Premiére, ministři, žaluji vás, selhali jste](https://hlidacipes.org/michal-blaha-premiere-ministri-zaluji-vas-selhali-jste/)<br>Michal Bláha dovozuje přímou zodpovědnost konkrétních lidí za současný stav.
- [Pokud nezměníme kurz, živí budou závidět mrtvým](https://denikn.cz/450196/pokud-nezmenime-kurz-zivi-budou-zavidet-mrtvym/)<br>Covid-19 je jen trailer na to, co teprve přijde.
- [Proč nediskutovat s rasisty, antisemity a xenofoby](https://denikn.cz/283027/proc-nediskutovat-s-rasisty-antisemity-a-xenofoby/)<br>Já osobně s lidmi vždy spíš diskutuju, než abych je na první dobrou odsoudil. Je to ale vždy ten nejlepší přístup? Naštěstí se osobně setkám spíše s obětmi dezinformací než prapůvodci nenávisti.
- [Ještě jednou o tom, zda diskutovat s hlasateli nenávisti](https://denikn.cz/288211/jeste-jednou-o-tom-zda-diskutovat-s-hlasateli-nenavisti/)
- [Babiš může být v klidu, Trump si jde pro znovuzvolení i přes mrtvoly v chladicích návěsech. Na vlastní selhání populisté nedoplatí](https://denikn.cz/439836/babis-muze-byt-v-klidu-trump-si-jde-pro-znovuzvoleni-i-pres-mrtvoly-v-chladicich-navesech-na-vlastni-selhani-populiste-nedoplati/)<br>Pokud čekáte, že covid-19 Babiše smete, možná čekáte marně. Může se udržet i přes mrtvoly. Skvělý rozbor!
- [Čekání na koronavirovou katastrofu: reportáž novináře, který uvízl v nešťastném koutě Jižní Ameriky](https://denikn.cz/323287/cekani-na-koronavirovou-katastrofu-reportaz-novinare-ktery-uvizl-v-nestastnem-koute-jizni-ameriky/)<br>Ať se u nás bude dít teď cokoliv, vzpomeňte si, co se asi v tu chvíli děje ve Venezuele.
- [Tajemný muž, který na jaře „zachránil Česko“? Exředitel České pojišťovny](https://www.seznamzpravy.cz/clanek/tajemny-muz-ktery-na-jare-zachranil-cesko-exreditel-ceske-pojistovny-124767#dop_ab_variant=0&dop_req_id=ji937Jy8uNN-202010170614&dop_source_zone_name=zpravy.sznhp.box&source=hp&seq_no=1&utm_campaign=&utm_medium=z-boxiku&utm_source=www.seznam.cz)<br>Už to sdíleli asi všichni, tak to teda sdílím i já, i když je to hlavně reklama na knihu. Pokud je tohle pravda, je to fakt šílený.
- [Meanwhile in CZECHIA](https://youtu.be/hJ800HrNrv8)<br>Pobavilo
- [Making data accessible to everyone at Productboard](https://link.medium.com/C0YDsBUErab)<br>Článek o Páji z PyLadies v Praze! Pracovala jako analytička, naučila se díky PyLadies Python, spoluorganizovala pražské kurzy PyLadies, vzali ji do Facebooku, dnes pracuje v ProductBoardu s daty.
- [Jsou všichni ajťáci k0k0t1?](https://www.linkedin.com/pulse/jak-recruite%C5%99i-sm%C3%BD%C5%A1lej%C3%AD-o-aj%C5%A5%C3%A1c%C3%ADch-pavel-%C5%A1imerda/), ale je asi jen otázka času, než zmitzí i tam.
- [Nebezpečný domov - osobnosti pro ACORUS](https://www.youtube.com/watch?v=uvuiHYu9a5w&feature=youtu.be)<br>Lockdown zvyšuje pravděpodobnost domácího násilí. Nebojte se zavolat policii, nechat pachatele vykázat a zabránit mu v dalším násilí.
- [Válka jako obchodní artikl. Česká zahraniční novinařina, „attention whores" a prodej emocí — HlídacíPes.org](https://hlidacipes.org/valka-jako-obchodni-artikl-ceska-zahranicni-novinarina-attention-whores-a-prodej-emoci)<br>Zajímavý komentář k práci Markéty Kutilové a Lenky Klicperové
- [Testosteronové mýty. Proč na jeden hormon svádíme mužnost, agresivitu i charakter](https://www.heroine.cz/spolecnost/3261-testosteronove-myty-proc-na-jeden-hormon-svadime-muznost-agresivitu-i-charakter?)<br>Zajímavý článek o tom, co je a a co není způsobeno testosteronem
- [How Discord Won](https://t.co/DCnxXVAu7w?ssr=true)<br>Konečně mi někdo vysvětlil Discord
- [Neviditelné pouště v regionech, které dusí českou demokracii](https://t.co/gDl3evswYO?ssr=true)<br>Proč mizí lokální média a proč je to špatně

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
