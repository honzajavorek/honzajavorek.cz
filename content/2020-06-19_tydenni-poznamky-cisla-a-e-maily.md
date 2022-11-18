Title: Týdenní poznámky: Čísla a e-maily
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False
Twitter-Comments: https://twitter.com/honzajavorek/status/1274046841311629321
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158219052052707


Utekl další týden (15.6. — 19.6.) a tak [stejně jako minule]({filename}/2020-06-12_tydenni-poznamky-cisla.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Posílání čísel

Tento týden jsem z velké části strávil přípravou pravidelného zasílání statistik inzerentům. To hlavní sice už bylo naprogramováno, ale než nechám posílat e-maily lidem, chtěl jsem to pořádně odladit. Každý den mi tedy přišlo pár desítek e-mailů, které jsem vždy prošel a snažil se na ně dívat očima inzerenta. Díky tomu jsem objevil spoustu věcí. Pomohlo, že jsem e-maily otevíral ve vlastním Gmailu, v různé doby, na odlišných zařízeních, v nejrůznějším rozpoložení.

-   Otevřel jsem si e-maily i na mobilu a zjistil, že spousta slov v tabulce s čísly se na úzkém prostoru škaredě zalamuje. Přidal jsem tedy spoustu `&nbsp;` (nedělitelných mezer).
-   Opravil jsem, aby odesílací skript vracel kód 1 nebo 0 podle toho, jestli alespoň jeden odeslaný e-mail selhal nebo ne. Selhání jednoho e-mailu by samozřejmě nemělo zastavit odesílání ostatních. Správný kód zaručí, že když se něco nepovede, dovím se o tom (CircleCI mi dá vědět, že něco spadlo).
-   Jelikož počet uchazečů se měří teprve pár týdnů, rozhodl jsem se jej v e-mailu nezobrazovat, dokud je roven nule. Pokud se zobrazí, tak s poznámkou, že se neměří dlouho. Text poznámky jsem několik dní ladil.
-   E-mail nedělám nijak krásný, nechávám ho jako čistě užitkovou záležitost. Ono taky dělat HTML a CSS pro e-mail je velká a bolestná magie, kterou se rozhodně zabývat nechci. Rozhodl jsem se nicméně, že do e-mailu dám logo ve žlutém pruhu, ať to je aspoň na "hlavičkovém papíře" a má to nějaký branding. Na tom se nedá nic pokazit, že? Je to jen žlutý pruh a jeden obrázek! No, zjistil jsem, že Gmail aplikace pro iPhone v "dark mode" tento pruh zobrazí jako fialový, [protože invertuje všechny barvy](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers/). Kašlu na to, nechám to tak!
-   Chtěl jsem zobrazit relativní procenta, jak si vede konkrétní inzerát vůči jiným inzerátům. Inspirovaly mě podobné statistiky, které ukazuje u kampaní MailChimp. S tímto jsem průběžně strávil několik dní. Nakonec jsem to bohužel smazal. Stále jsem přicházel na to, že jsem pro to potřeboval specifická podkladová data, že to vlastně musím přepočítat podle toho kolik dní je inzerát venku, atd., až jsem vytvořil docela ošklivý slepenec, nicméně fungoval. Jenže inzeráty na JG se zatím ještě automaticky neexpirují a některé jsou tam fakt dlouho, některé krátce. Navíc se spousta statistik měří až od určitého data. No, co vám budu povídat, i když jsem to nakonec správně počítal, vycházela čísla, která byla pro inzerenty naprosto neužitečná. Vzdal jsem to tedy a třeba se k tomu někdy vrátím později, až budou pro všechny inzeráty platit stejné podmínky ohledně expirace a naměřených hodnot. Potom budou statistiky mít větší význam a nebude to porovnávání hrušek s jabkama.
-   Díky práci na relativních procentech jsem ale objevil pár chyb ve výpočtech běžných statistik - třeba jsem špatně určoval období na některá čísla a "okrádal" se tak o skoro měsíc údajů.
-   Opravil jsem hned několik hloupých chyb v samotném posílacím skriptu.


### Zpětná vazba

Napadlo mě (ve sprše, viz článek o Anti-Flow, odkaz dole), že bych mohl do každého e-mailu ještě přidat i odkaz na formulář se zpětnou vazbou. JG totiž už nějakou dobu provozuji a občas se dovím, že díky němu někdo sehnal práci, ale systematicky žádné informace nemám, ani moc žádné kontakty na konkrétní lidi, takže nemůžu publikovat doporučení nebo _success stories_. A to je problém, protože se _success stories_ by se prodávalo mnohem líp. Jasně, každý mi může na e-mail se statistikami prostě odpovědět, ale proč by to dělal? Přišlo mi, že výzva k vyplnění nějakého formuláře by mohla lidi nějak psychologicky motivovat víc. Vytvořil jsem tedy formulář na Google Forms:

-   Formulář má jen jednu povinnou otázku, a to **Jak byste hodnotili vaši celkovou zkušenost?** Následují čísla 1 až 5 jako ve škole.
-   **Jaký byl výsledek vaší inzerce?** Jestli se povedlo díky JG zvýšit počet kandidátů nebo dokonce nějaké najmout. Přidal jsem tuto poznámku:

    > Jestliže jste přijali kandidáty, kteří na vaši inzerci narazili na junior.guru, dejte jim prosím vědět, že se mohou ozvat na ahoj@junior.guru a Honza Javorek s nimi rád udělá rozhovor nebo zpropaguje jejich příběh. Pro vaši firmu to bude reklama a pomohou dalším lidem, kteří se snaží v oboru prorazit.

-   **Máte chuť napsat doporučení?** S příkladem a poznámkou, že toto doporučení se spolu s odkazem na firmu může objevit na junor.guru.
-   **Odkaz na web firmy nebo název firmy** - políčko, díky kterému se dovím, odkud vítr vane. Nepotřebuji přímo nějaké ID inzerátu, ani kontakt, to už si dohledám. Chtěl jsem s tímto políčkem lidi co nejméně otravovat.

Následně jsem si nicméně všiml, že Google Forms umožňují předvyplnit políčka! [Není to vůbec těžké.](https://trevorfox.com/2015/06/dynamically-pre-fill-google-forms-with-mailchimp-merge-tags/) Za odkaz na formulář se přidá `?usp=pp_url&entry.ČÍSLO=HODNOTA`, kde číslo je nějaké ID políčka a hodnota je to, čím chci políčko předvyplnit. Číslo se nejjednodušeji zjistí tak, že se v pravém horním rohu při úpravách formuláře klikne na tři tečky a vybere _Get pre-filled link_. Následující klikačka člověka vším provede a vytvoří odkaz s hodnotou, kterou chce. Já v každém e-mailu generuji jinou adresu na formulář a nastavuji vždy jinou hodnotu, konkrétně tedy jméno firmy, která zadala inzerát. Pokud na odkaz někdo klikne, bude mít políčko už předvyplněné a je větší pravděpodobnost, že formulář odešle. Já se dovím, z jaké firmy to je, a všichni jsme spokojení. Parametrizovatelné Google Forms! Pecka! Díky tomu bude moci JG zůstat ještě pěkně dlouho jako statická stránka.

### Ostrý provoz

V pátek jsem skript upravil tak, aby se e-maily posílaly na opravdové adresy inzerentů (doteď se posílaly jen mě) a omezil jsem to tak, aby se to spustilo jen v pondělky. No a teď děj se vůle bohů! Celý víkend budu trnout, jestli se to v pondělí odešle a jestli správné e-maily na správné adresy. A co teprve odpovědi, které mi na to kdo pošle, ajaj!


## Námluvy

Námluvy s velkou firmou pokračují. Zdokumentoval jsem způsob, jakým mohou trackovat lidi z inzerátů a udělal jsem _sales call_ s _velkým šéfem_. Šlo to dobře a jde to dál k ještě větším šéfům.

Jsem introvert a videohovory pro mě byly vždy trochu stres, zvláště pokud byly nějak důležité. Za poslední dobu jich ale bylo tolik, že už jsem si nějak zvykl. A ty důležité se taky dají zvládnout. Je to jako s přednášením. Stačí se prostě dobře připravit a nakonec většinou všechno dobře dopadne a za ten stres to stojí. Na videohovory se připravuji tak, že si dělám rešerši o člověku, se kterým mám volat, o jeho aktivitách, a sepíšu si všechna čísla a informace, na které by se mohl ptát. Někdy si i připravím odpovědi na otázky, které si myslím, že by mohl mít. To celé mi dodává dost sebevědomí, takže jsem pak při hovoru v pohodě. Dobré je, že se u videohovoru snadno nenápadně kouká do poznámek nebo poznámky píše :) Možná to vypadá, že ta čísla sázím z hlavy, ale já je teda většinou čtu :D


## Další poznámky

- Jak stále přidávám nové [podporovatele](https://junior.guru/donate/#sponsors), řekl jsem si, že už si to zaslouží vlastní YAML soubor, do kterého se mi to bude dobře psát a do něhož se případně bude lidem lépe dělat Pull Requesty. Soubor je [tady](https://github.com/honzajavorek/junior.guru/blob/master/juniorguru/data/supporters.yml), i s komentáři co znamená co. Načítám ho klasicky přes [StrictYAML](https://hitchdev.com/strictyaml/) a díky tomu, že mám podporovatele v systému jako data, můžu je řadit podle příjmení automaticky. Na samotné stránce jsem trochu upravil design a výrazněji rozlišil, proč někdo má odkaz a někdo ne.
- A brzy po úpravách jsem díky [tweetu Tomáše Ehrlicha](https://twitter.com/honzajavorek/status/1273172305280217088) získal další dva podporovatele, Jakuba a Vojtu! Juchů!
- Kontaktoval jsem několik dalších firem ohledně [nabídky na sponzorství příručky pro juniory, kteří si chtějí hledat svou první práci v IT](https://junior.guru/hire-juniors/#handbook). A některé firmy se ozvaly i samy.
- O víkendu jsem pár věcí opravil (a pár rozbil) na [film2trello](https://github.com/honzajavorek/film2trello). Hlavně jsem přidal lepší podporu pro [Aerovod](https://aerovod.cz/), z něhož si poslední dobou pouštíme stále více filmů. Posledně [Parazit](https://aerovod.cz/katalog/parazit) a [Portrét dívky v plamenech](https://aerovod.cz/katalog/portret-divky-v-plamenech).
- Vytvořil jsem [comments.py](https://github.com/honzajavorek/honzajavorek.cz/blob/master/comments.py), skript, který se podívá na mnou sdílené týdenní poznámky na Twitteru a Facebooku, a přidá odkazy k článkům jako odkazy na komentáře. Využívá API, které jsem vytvořil [už před týdnem]({filename}/2020-06-12_tydenni-poznamky-cisla.md) přes [Integromat](https://www.integromat.com/). Skript se spouští pravidelně na [GitHub Actions](https://github.com/honzajavorek/honzajavorek.cz/blob/be1c687e7c51a1ad0cc5d83ea0384952d9073371/.github/workflows/build.yml#L34). Zdá se, že to celkem funguje, zkoušel jsem to už na minulých poznámkách. Takže teď už mám vše zautomatizované tak, že mi stačí poznámky napsat, publikovat je, a ručně nasdílet na Facebook. Vše ostatní se udělá samo. Normálně bych si s tím tak nehrál, ale když to mám dělat každý týden, [už se automatizace vyplatí](https://xkcd.com/1205/).
- Zablokovali mi [účet na Instagramu](https://www.instagram.com/juniordotguru/) a nevím, jak jej mohu odblokovat. Mohu nahrávat obrázky, ale nemohu nic jiného, dokonce k nim nemohu ani psát popisky. Bylo tam tlačíko, že se můžu odvolat, ale není na něj žádná odezva. Celé to byl spíš experiment, tak přemýšlím, že pokud se to nevyřeší, asi ten účet zruším, abych s ním netrávil zbytečně čas.
- Když si nemůžu hrát s Instagramem, začal jsem se víc věnovat [LinkedIn](https://www.linkedin.com/in/honzajavorek/). Tam se pohybuje hodně lidí z HR a recruitmentu. Zkoušel jsem najít zajímavé lidi, které by mohlo povědomí o JG obohatit, a přidávat si je, i když je přímo neznám. To byla doteď moje politika na LinkedIn, přidával jsem si jen lidi, které jsem aspoň trochu znal nebo odněkud pamatoval. Teď jsem to rozvolnil a přidávám si i lidi, kteří by se mohli hodit při šíření JG. Vytvořím tak větší publikum pro své LinkedIn statusy, pod nimiž to už cekem žije. Osobně mě vždy překvapí, kolik lidí LinkedIn opravdu používá jako plnohodnotnou sociální síť :D
- Sem tam mi někdo pošle odkaz na juniorní nabídku práce, na kterou narazil na internetu. Pár se jich takto už nasbíralo. Všechny jsem prošel a kontaktoval firmy s nabídkou toho, aby inzerovali na JG.
- [Přál jsem si, aby existovalo řešení na cookie lišty.](https://twitter.com/honzajavorek/status/1273510273979211780) Taková blbost, ale k dnešnímu dni to má 170+ lajků :D
- Jeden den jsem zcela věnoval tomu, že jsem jel za kamarádem do Pardubic a potom zašel na [první živé pražské Pyvo tohoto jara](https://twitter.com/naPyvo/status/1273311588372615171).
- Napadlo mě, že bych mohl natvrdo spamovat Google Analytics všech ostatních :D Nevím, jestli je na to nějaká etiketa, ale začal jsem ke všem nabídkám, které odkazují na stránky inzerentů, automaticky přidávat měřící [UTM](https://blog.hootsuite.com/how-to-use-utm-parameters/) parametry `&utm_source=juniorguru&utm_medium=job_board&utm_campaign=juniorguru`. To znamená, že když lidi klikají na tyto odkazy, zaznamenává se na stránkách inzerentů, že přicházejí z JG. Pokud to chápu dobře, druhá strana nemusí na svém Google Analytics účtu mít nic extra nastaveno, aby to tam pak viděla. JG se jim do statistik samo tímhle vecpe. Pokud tedy používají Google Analytics.
- Vyladil jsem 404 stránku, tzn. stránku, která se objeví, když někdo jde na neexistující adresu, třeba [junior.guru/baf/](https://junior.guru/baf/). Doteď tam byla jen nějaká ošklivá hláška z [Vercelu](https://vercel.com/). Nyní se zobrazí hezká stránka. Je prošpikovaná JavaScriptem, protože je statická. Zjišťuje tedy informace až za běhu. Vypisuje, kde že přesně se to člověk ocitl, a poskytuje nějaké alternativy, kam může jít. Pokud je to 404ka někde na `/jobs/`, třeba [junior.guru/jobs/baf/](https://junior.guru/jobs/baf/), je prakticky jasné, že člověk následoval odkaz na nabídku, která vypršela. Stránka toto detekuje a vypíše jiný text. Toto byl i hlavní důvod, proč jsem se 404ce začal vůbec věnovat. Ideálně by v budoucnu vypsala třeba i rovnou alternativní nabídky práce, ale s tím jsem se teď nepáral.
- Konečně jsem měl čas se vrátit zase k [robotovi, který stahuje nabídky z jiných zdrojů](https://junior.guru/jobs/#jobs-bot). Prošel jsem všechny nabídky - ty, které prošly, i ty, které vyhodil jako nedostatečně juniorní. Našel jsem hned několik chyb, které jsem doladil. Je to taková mravenčí práce, trvalo mi to jedno celé odpoledne. Robot momentálně zahodí 142 nabídek a na web pustí 16. Zjistil jsem, že robot je v několika případech dost přísný, a vyhazuje víc nabídek, než by musel. Něco jsem vyřešil hned, nad řešením některých situací ještě přemýšlím.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Taking photographs ruins the memory, research finds](https://www.telegraph.co.uk/news/science/science-news/10507146/Taking-photographs-ruins-the-memory-research-finds.html)<br>Když už si věci fotíte, měli byste si fotky taky někdy procházet
- [Hiring and the market for lemons](http://danluu.com/hiring-lemons/) Dan Luu o pracovním trhu v IT
- [Anti-Flow](http://randsinrepose.com/archives/anti-flow/)<br>Taky mám nejlepší nápady ve sprše
- [UTC is Enough for Everyone, Right?](https://zachholman.com/talk/utc-is-enough-for-everyone-right)<br>Hezké shrnutí toho, na co si dávat pozor při práci s časem na webu
- [Všechno zrušit?](https://www.jestevetsikritik.cz/komentare/1045-vsechno-zrusit)<br>Poctivý rozbor toho, proč teď některá díla mizí z Netflixu a spol.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
