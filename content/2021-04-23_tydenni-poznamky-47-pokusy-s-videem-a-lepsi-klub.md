Title: Týdenní poznámky #47: Pokusy s videem a lepší klub
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (19.4. — 23.4.) a tak [stejně jako minule]({filename}/2021-04-16_tydenni-poznamky-46-vyjednavani-lapace-hledajicich-alergie-na-uklizeni.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Pokusy s videem

Největším dobrodružstvím tohoto týdne bylo pokusné nahrávání videí s [Danem Srbem](https://coreskill.tech/). Myšlenka je taková, že ne každému vyhovuje vnímat informace skrze text, tak jestli by nešlo určité kousky [příručky](https://junior.guru/candidate-handbook/) nějak jednoduše a nízkonákladově namluvit a těmito videi pak příručku doplnit.

V rámci příprav na natáčení jsem si vykopíroval celou příručku do Google Dokumentu a začal ji zvrchu dolů číst. Když jsem našel něco, co bych rád změnil, doplnil, rozšířil, opravil, tak jsem si udělal komentář. Celé jsem to nestihl dočíst, ale už teď tam mám spoustu poznatků. Kdy to zpracuju, to nevím, ale jsem rád, že jsem to takto vzal při jednom.

V úterý jsme se spojili a zkusili něco nahrát. Byla to celkem sranda, tréma, hledali jsme v mém bytě pokoj s nejmenší ozvěnou, apod. Nemám žádné profi vybavení, takže to byl trochu boj. Každopádně něco jsme nahráli. Dan to ještě tentýž večer zpracoval a zkusil něco nastříhat. Už teď vidíme hromadu problémů a chyb, takže osud tohoto prvního pokusu není vůbec zatím jasný. Teď bych si to měl celé pustit (což není moc příjemné, koukat se na sebe a poslouchat se, ale zvykám si) a dělat si poznámky, co by šlo říct nebo udělat jinak. Pak uvidíme, co dál.

Až budeme mít nějaké aspoň trochu použitelné pokusy, asi to dáme nejdřív k okomentování lidem v klubu, než se to dostane do příručky.


## Trvalý pobyt

Ověřoval jsem, že nejdůležitější instituce (ŽÚ, FÚ, ČSSZ, zdravotní pojišťovna) si všimly, že jsem změnil trvalý pobyt. Protože se mi nechtělo nikam chodit ani volat, napsal jsem všem e-mail.

> Dobrý den,
> 
> jsem OSVČ a přestěhoval jsem se. Chtěl bych ověřit, zda {INSTITUCE} zaznamenala z centrálních registrů změnu mého trvalého pobytu z {STARÁ ULICE ČÍSLO} na {NOVÁ ULICE ČÍSLO}, oboje Praha 3-Žižkov, 13000, případně jestli tuto změnu musím ještě dodatečně nějak oznamovat.
> 
> Děkuji,
> Jan Javorek, IČO 74279858, tel. {TELEFON}

Prakticky do druhého dne mi všichni napsali nebo zavolali zpět, všichni milí a vše bez problémů. Vždy se to v pořádku zpropagovalo z rejstříku obyvatel, takže asi to fakt funguje :D Příště už tomu možná budu věřit natolik, že už nebudu psát ani ty e-maily.

Zajímavější byla jedna americká firma, kam bylo možné pouze zavolat, ale nakonec jsem zkusil nějaké [sociální inženýrství](https://cs.wikipedia.org/wiki/Soci%C3%A1ln%C3%AD_in%C5%BEen%C3%BDrstv%C3%AD_(bezpe%C4%8Dnost)) a vmanipuloval opět jedním pouhým e-mailem svého předchozího zaměstnavatele do toho, aby tam adresu změnil za mě :D

Chtěl jsem změnit adresu i u operátorů a bank, ale ti mě poslali k šípku, protože chtějí doklad a já novou OP ještě nemám. Kromě T-Mobile, tam to šlo online naklikat i bez dokladu. Na dotaz, proč můj druhý operátor vlastně potřebuje číslo OP, jsem dostal odpověď, kterou si vykládám jako „někdo tak navrhl náš systém a číslo OP v něm figuruje jako neopomenutelné IDčko“. Meh. Takže to potom někdy. Ne že by mi vlastně nebylo úplně fuk, jakou adresu u mě mají. Každá slušná banka jede už přes net a když chce poslat novou kartu, raději se ujistí, na jakou adresu to má poslat.

Adresu jsem změnil dále i na webu, ve Fakturoidu a ve Stripe, aby byla správná na dokladech vydávaných členům klubu.


## Google Analytics

Říkal jsem si, že teď v poslední době moc nesleduju GA, tak že bych si je měl pořádně projít a zkusit z nich něco vyčíst. Udělal jsem si pořádek v goals, abych sledoval jen „club engagement”, tedy když lidi kliknou na tlačítko, které vede k zakoupení členství. Věci jako přihlášení k newsletteru apod. jsem vypnul, to teď sledovat nepotřebuju.

Zda si členství opravdu zakoupí, to neměřím. Memberful má podporu pro nějaké Ecommerce cosik, ale to nevím jak funguje. Zkusil jsem to zapnout, ale podle [návodu](https://memberful.com/help/how-to/google-analytics/#set-up-manual-integration) to vypadá, že používám něco, co se jmenuje Google Tag Manager a ten když jsem otevřel, tak to vypadalo jako nějaké markeťácké peklo na sledování lidí, tak jsem to zase zavřel. Já ty konverze stejně nepotřebuju (zatím) měřit end-to-end, stačí mi vědět, že se někdo pokusil zakoupit členství. Proces samotného kupování v této fázi nijak neovlivním, konverzi ani Memberful, ani Discordu nezlepším. Důležité je pro mě teď hlavně zajistit, aby se co nejvíc lidí dovědělo o tom, že klub existuje, a byly jim jeho výhody vysvětleny tak, že budou mít chuť se pokusit do něj dostat. Na to Ecommerce měření nepotřebuju.

No takže si čtu GA, ale buď jsem moc lama, nebo tam prostě nic zajímavého není. Nejvíc lidí chodí napřímo. Pak z vyhledávání a z postů na sociálních sítích. Z toho vyvozuju, že posty má smysl dělat a že mám dál lapat hledače. Hodně lidí zřejmě JG už prostě zná. Vysledovat nějaký pohyb na stránkách, který by vedl ke konverzi, moc nejde. Vysvětluji si to tak, že lidi JG znají a chodí tam opakovaně, o klubu slyší opakovaně, ale trvá jim, než se rozhoupou a zkusí to. Takže když se rozhoupou, jdou už na jistotu (ti, kdo kliknou, mají jako landing page buď samotnou stránku klubu, nebo hlavní stránku). Není to spontánní rozhodnutí. V takovém případě mi nějaké flow uživatelů na stránce asi nepomůže. Můžu akorát koukat, jestli moc lidí neodpadá na cestě ke stránce s klubem, nebo jestli stránka s klubem lidi přesvědčí ke kliknutí. V obou případech je asi co zlepšovat, ale že bych v GA viděl nějaké zázračné indicie k tomu, co bych měl udělat, to se asi říct nedá.

No nic. Trochu mě to asi zklamalo. Možná bych se v tom měl víc vzdělat, ale druhá věc je, že mě to ani moc nebaví. Nechcu nahánět čísílka. Myslím, že vlastně tuším, co mám dělat: Zvyšovat hodnotu klubu pro jeho členy a umět tu hodnotu vysvětlit na [stránce o klubu](https://junior.guru/club/). Pak dělat PR, aby se povědomí o JG šířilo skrz bubliny. Nevím, co by v GA muselo být, aby toto bylo jinak.


## Zvyšování hodnoty klubu

První věc, kterou jsem chtěl už dlouho zvýšit hodnotu klubu pro jeho členy, je robot na nabídky práce. Ty se stahují a třídí každý den a vypisují [na webu](https://junior.guru/jobs/). Chtěl jsem mít v klubu speciální místnost, kam by robot nové nabídky sypal hned jak je najde, a kde by o nich šlo rovnou třeba i diskutovat. Jedna místnost, kde si lidi sdílejí nabídky práce, které někde najdou, už tam je, ale pro robota jsem chtěl separátní, aby si ji případně lidi mohli snadno vypnout, kdyby v ní bylo moc rušno.

Toto jsem nakonec vyrobil za pouhý jeden den, protože vše potřebné už jsem měl nebo uměl. Akorát jsem to v klubu oznámil a pak jsem jeden den počkal, jestli to opravdu funguje (nastavil jsem privátní kanál, kde testuju robota), než jsem to začal do kanálu sypat na ostro. Odezva mezi členy zatím fajn, uvidíme co dál.

Do budoucna by šlo nabídkám přidělovat emoji reakce podle toho, jestli jsou vytřízené dobře nebo špatně. Tím by šlo učit machine learning, jenž se snaží pro JG vytvořit [kamarád Míla](https://milavotradovec.cz/). Napadlo mě, že by to takto mohlo být lepší, než to mít na webu a hodnotit to přes posílání eventů v Google Analytics, přes klikání náhodných kolemjdoucích. Přece jen lidi v klubu jsou trochu víc zainteresovaní. V této fázi ale zatím nejsme a má to taky nedostatek v tom, že potřebujeme i vytahovat dobré nabídky z vyhozených, což ale znamená mít někde ohodnotitelné i to, co se vyhodilo. Kdo bude ale procházet a hodnotit stovky těch vyhozených, to nevím. Uvidíme. Možná pro masochistické zájemce. Nebo pro mě, že bych to občas prostě prošel. Zatím mám v klubu jen ty, které prošly. Lidi můžou hlasovat, zda se jim nabídka líbí nebo ne a toto se mi uloží do databáze. Toť vše.

Jako další věc chci udělat bota, který bude v klubu dělat nějakou statistiku zpráv a jednou za týden ji postne třeba do #meta kanálu, to je jedno. Cílem je zvyšovat zapojení lidí, ocenit trochu lidi co v klubu pomáhají nejvíc a mít něco trochu jako „weekly digest“ pro lidi, co vše nestíhají číst. Jak na to? Projdu zprávy za poslední týden nebo měsíc (a třeba i od počátku klubu, jakože „all time“) a hodím pár čísel jako kdo napsal nejvíc (spíš pro pobavení, není cíl) a kdo měl nejkladněji reagovaný příspěvek (vyhodnotím reactions „inteligentně“), tzn. nejužitečnější příspěvek. Tyto nejvíc užitečné příspěvky pak i vypíšu, aby se k nim případně lidi mohli vrátit (to je ten „weekly digest“ trochu). Hlavně mi jde o nějaký kredit pro ty, kdo jsou užiteční. Můžu jim i přidělit nějakou Discord roli, ať jdou vidět, to se dá pak ladit.

Co jsem udělal první, je postování pár čísel do privátního kanálu. Budu se na to pár týdnů dívat a přemýšlet nad tím, jaké emoce to ve mě vyvolává nebo jak by se měly formulovat texty kolem toho. Jaký popsek by byl lepší, nebo jaká čísla tam asi radši vůbec nedávat. Toto mám rozpracované, ale nejprimitivnější verze s pár čísly už něco posílá.

Protože jsem přidal už třetí skript ([pravidlo tří](https://andrewbrookins.com/technology/the-rule-of-three/) přebíjí [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)), který něco dělá s Discordem, přestal jsem rozkopírovávat podpůrný kód a začal jej zobecňovat do nějakých abstrakcí. Vytvořil jsem si soubor s funkcemi společnými pro více skriptů a otestoval jsem si je. S tím jsem si hrál půlku čtvrtka.


## Další poznámky

-   Přidával jsem na JG nově zaslané pracovní nabídky. Jednu, zaslanou v režimu „zdarma“, jsem musel odmítnout. Napsal jsem:

    > Dobrý den,
    >
    > díky za zaslanou nabídku práce. Pročetl jsem ji a požadujete v ní 2/3+ roky profesionálních zkušeností nebo třeba perfektní znalosti s HTML, CSS & SASS/SCSS. To bohužel cílová skupina https://junior.guru/jobs/ nesplní, pracovní nabídky tam se zaměřují vyloženě a co nejvíce na entry level, kdy člověk může nastoupit se zcela minimální praxí.
    >
    > Pokud byste vzali i začátečníka, pojďme zkusit vaši nabídku nějak přeformulovat, ale jinak bych doporučil inzerovat např. na https://www.startupjobs.cz/
    >
    > Díky,
    > Honza Javorek

    Odpověď jsem nedostal. I psaní takových mailů je součástí obsluhy nabídek práce na JG…

-   „Na sociálních sítích nelze být státotvornej. Je to jen nekonečné psaní písmenek do prázdna, u kterého vystřelí pár emocí, ale které si ani já, ani čitatel nebudeme za 10 minut už pamatovat. Jen nám bude divné, že před chvílí byl oběd a teď už je půl druhé.“ napsal jsem do komentáře na Facebook, a potom jsem si ho zablokoval. Ale pak jsem zase potřeboval něco vyřídit, a šup, už tam sázím nějakou geopolitickou analýzu toho, proč se Rusům nedaří akce tajných služeb. Dneska hledám logo yablka jako SVG, najdu jeho Facebook, tam odkaz na [tohle](https://www.youtube.com/watch?v=cO4ObcFTqfA). Ty vole! :D Ty sítě jsou strašná věc. Přilepí se to na mě a vybudí to ve mě pocit, že mám někam psát moudra o Rusku. A nejde se odlepit. Pomoc. Když otevřu Twitter nebo FB a vidím, co tam lidi řeší, tak je mi jich líto, protože vidím, jak se nachytali. A po 4 minutách tam něco píšu o tajných službách.
-   Nejsem spokojen se [sekcí o kurzech](https://junior.guru/practice/#courses). Jedním z cílů JG je vyřešit začátečníkům rozhodovací paralýzu a ukázat jim jasnou cestu, kde a s čím začít. Tato sekce jde proti tomu, je to snaha o vyčerpávající výčet a různé vzdělávací agentury jsou tam abecedně na jedné hromadě. Tento týden jsem tam přidal všechny, o kterých vím, a kterým tam chyběl odkaz. Jaká je budoucnost té sekce zatím nevím, ale v současné chvíli si myslím, že takový seznam nikomu moc nepomáhá. Bylo by podle mě lepší vysvětlit co je bootcamp, online kurz, prezenční kurz, jaké jsou v ČR/SR možnosti. Dodat lidem informace, které jim pomohou zjistit kontext a informovaně si sami z nějakého nezaujatého „katalogu“ vybrat to, co jim bude nejvíc vyhovovat - jinak se budou rozhodovat jen podle toho, kdo bude mít nejvytrvalejší PR.
-   Do [sekce pro ženy](https://junior.guru/learn/#ladies) jsem přidal odkaz na [Aj Ty v IT](https://ajtyvit.sk/).
-   Během minulého týdne jsem byl na online meetupu v Namibii (viz předešlé poznámky) a trochu mě to namotivovalo se zase ozvat lidem a trochu třeba s něčím pomoct. V podstatě víc jak rok jsem moc akční nebyl. Napsal jsem tedy Marianovi do Mozambiku, s kterým jsme něco vloni v únoru řešili, a Jessice do Namibie, které jsem nabídl, že bych s ní mohl přes WhatsApp udělat rozhovor tady na blog. Jessica souhlasila a nápad se jí líbil. Napadlo mě, že by to mohl být relativně jednoduchý způsob, jak jim vylepšit viditelnost, navíc s Muheuem [rozhovor](https://www.blog.pythonlibrary.org/2021/04/05/pydev-of-the-week-ngazetungue-muheue/) nebo přednáška sem tam je, ale s ní nic. Má to jen jeden problém, a to, že jsem nikdy v životě rozhovor nedělal. Budu si asi muset připravit nějaké vhodné otázky :D
-   O víkendu jsem vyzkoušel [Musi](https://apps.apple.com/us/app/musi-simple-music-streaming/id591560124) appku, která by snad mohla fungovat jako alternativní klient na YouTube. Sice tam občas vyskočí nějaká vizuální reklama, ale reklamy ve videu tam nejsou a hudba hraje dál na pozadí, i když se člověk přepne na jinou appku. Vyzkoušel jsem si na tom i schopnost nainstalovat mobilní appku přímo do macOS (což na M1 jde) a měl jsem z toho takovou radost, že jsme si se ženou jeden večer dali YouTube párty :D Ale možná existují i normální aplikace přímo pro macOS pro tento účel a nemusí se používat Musi, které je designované pro mobil, alternativy jsem nehledal.
-   Spadl mi stahovač nabídek práce na StackOverflow a řešil jsem celé jedno dopoledne opravu. Pak jsem si uvědomil, že všechny moje pokusy asi naráží na 24hodinovou cache a ať se snažím jak se snažím, nic z parametrů, které měním, nemá reálný dopad na průběh stahování. Takže jsem se pleskl do čela, udělal nějakou minimální úpravu, o které jsem si myslel, že by mohla pomoci, a nechal to být. Druhý den to prošlo a žádný problém nebyl. Ach jo. Dobré aspoň je, že se tím ověřila kontrola chyb, kterou jsem přidával nedávno. Bez ní bych o tomto problému vůbec nevěděl, teď aspoň vím, že umí vážné problémy detekovat. I když je otázka, zda bych si neušetřil jedno dopoledne, kdybych se konkrétně o této vůbec nedověděl :D
-   Přečetl jsem si o [FLoC](https://paramdeo.com/blog/opting-your-website-out-of-googles-floc-network) a pak na web přidal odpovídající meta hlavičku. Ale pak jsem zjistil, že pokud to není HTTP hlavička, ale jen HTML hlavička, tak že ji vlastně nic zatím neumí respektovat a možná to ani nikdy fungovat nebude, takže jsem ji zase odebral :D
-   Přidal jsem „lapač na hledače“ (viz předchozí poznámky), kteří hledají [Green Fox](https://junior.guru/topics/greenfox/).
-   V klubu jsem udělal orientační anketu o tom, kdo prošel jakými kurzy. 26 samostudium, 12 veřejná VŠ neIT obor, 10 veřejná VŠ IT obor, 10 Czechitas, 10 PyLadies, 7 Udemy, 5 Coursera, 3 Learn2Code, 2 Engeto, 2 ReactGirls, 2 edX, 1 VŠB rekvalifikační kurzy, 1 Django Girls, 1 DataCamp, 2 CoreSkill, 0 Green Fox Academy, 0 Coding Bootcamp Praha, 0 PrimaKurzy, 0 SDAcademy, 0 BeeIT.
-   Jedné vzdělávací agentuře jsem poslal fakturu, s druhou stále ještě vyjednávám.
-   Měli jsme schůzi výboru [Pyvce](https://pyvec.org/). Pár věcí se nám dokonce povedlo uzavřít a dokončit. Začali jsme pomalu připravovat členskou schůzi 2021.
-   Díky jedné recruiterce na LinkedIn, která má v popisu „Early Talent Program Manager“ jsem zjistil, že existuje klíčové slovní spojení „early talent“, které v řeči recruiterů nejspíš označuje přesně to, co jsem se jim snažím pomocí [nabídek práce](https://junior.guru/jobs/) dodat. Zajímavé. Zatím nevím, co s tímto zjištěním udělat. Našel jsem 5 dalších lidí na LinkedIn, kteří toto spojení měli v profilu, a přidal jsem si je. Třeba je okouzlí mé LI statusy a sami mi napíšou e-mail, že mě chtějí sponzorovat, haha :D
-   S jednou vzdělávací agenturou začínám pomalu spolupracovat na speciálním materiálu pro juniory, který budeme dohromady tvořit.
-   Nahromadily se mi nějaké věci, které by se hodilo naházet na sociální sítě, tak jsem polovinu pátku (dneška) strávil tím, že jsem připravoval posty. Asi pět postů mi zabralo půl dne. Snažím se těmi posty moc nespamovat, takže se posílají dvakrát týdně. Kamarád, který si dřív stěžoval, že moc spamuju, tak mi napsal, že si teď ani nevšiml, že nějaké promo posty posílám, takže asi dobrý. Akorát mám teď ve frontě třeba deset postů a kalendář to zaplnilo do konce května, tak nevím, jestli to vlastně nezahustit.
-   Upravil jsem různé texty uvnitř Discordu tak, aby odkazovaly na [stránku pro členy](https://junior.guru/membership/). Uvědomil jsem si, že zevnitř nikde prolinkovaná není.
-   Během 7 dní od 17.4. do 23.4. jsem ještě trochu kašlal, tak jsem kašlal i na pohyb :(


## Co plánuji

Uspořádal jsem si Trello tudů tak, aby odráželo moje aktuální priority: Zvyšovat hodnotu klubu pro jeho členy a umět tu hodnotu vysvětlit na [stránce o klubu](https://junior.guru/club/). Tři věci, které bych chtěl zvládnout udělat příště:

1. Doprogramovat robota na statistiky v klubu.
2. Provést odloženou [přednášku s Adinou](https://junior.guru/events/).
3. Naplánovat další událost a začít automatizovat věci kolem přednášek (výrobu plakátku, výpis na webu, apod.)

Bonus: Možná bych po skoro dvou letech mohl aktualizovat všechny screenshoty webů na JG? Některé mi přijdou už trochu prošlé :/


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Krize a zánik vlastnictví](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.marigold.cz%2Fitem%2Fkrize-a-zanik-vlastnictvi&h=39eb7aa841e327fd8236c73c6947c468384c724aa95c79ffcf90c3d017ae514f)<br>„Vznikne pronajatý život, který bude pro chudé drahý a ze kterého bude obtížné uniknout.“
- [PyDev of the Week: Ngazetungue Muheue](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.blog.pythonlibrary.org%2F2021%2F04%2F05%2Fpydev-of-the-week-ngazetungue-muheue%2F&h=50e724567b80fe08698c2b5e73878ee622600a6518387738544dd8affdf627d6)<br>Muheue je úžasnej. Měl jsem tu čest s ním před rokem strávit několik týdnů a je to člověk s velkou energií a vytrvalostí.
- [Everyone Is Beautiful and No One Is Horny](https://getpocket.com/redirect?&url=https%3A%2F%2Fbloodknife.com%2Feveryone-beautiful-no-one-horny%2F&h=1f719918d85271b804d182df9f8a307853baf670e1532c8846fb60d210fed63a)<br>Zajímavý článek o tělech a popkultuře. Hromada generalizací a rychlých závěrů „k zamyšlení”, na kterých něco je.
- [Choose Boring Technology](https://getpocket.com/redirect?&url=http%3A%2F%2Fboringtechnology.club%2F%2317&h=7844dd7df1096cbfc06c1d8cf87cec330b1adef752589d14dd1909a9aaa2e8c2)<br>Jak je možné, že jsem tuto prezentaci objevil až teď? :)
- [Elon Musk's "Loop" - It's bad, folks](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D4dn6ZVpJLxs&h=41eba368de697299db8c7694c96153ec590d772ba0d44151ec1aaa7fffe1c22f)<br>Náhodný youtuber kritizuje Elonovy hyperloopy. Sdílet náhodné youtubery hrozí tím, že to má stejnou váhu jako videa o placaté zeměkouli, ale přišlo mi, že to celkem dává smysl. Jde hlavně vidět, jak je USA jinde ve vnímání MHD a aut, a že na tom jsme v ČR vlastně ještě skvěle, ani si to neuvědomujeme :) Japonsko a Evropa staví vlaky, zatímco USA sní o hyperloopech, jen aby se lidi nemuseli nedejbože ani přiblížit k něčemu jako veřejně financovanému vlaku.
- [Spanish Conquest of the Incan Empire](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DxPm8E-zWwsQ&h=e758a7613fef0dd459ff7d89098e3e82394c107a2c9ade675cb0c2c667ce32ec)<br>Čtvrt hodinka o tom, jak španělé dobyli Inckou říši, část první. Něco z toho jsou celkem známá fakta, něco jsem netušil.
- [Great Inca Rebellion](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D813PlMo0-54&h=eae23b13da24cbb32b43fedbd3ebf28c0287145aa5df9e33b403d2ee5ddc988a)<br>Čtvrt hodinka o tom, jak španělé dobyli Inckou říši, část druhá. Z tohoto jsem netušil vůbec nic.
- [Is Success Luck or Hard Work?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fapp%3Ddesktop%26v%3D3LopI4YeC4I%26t%3D70s&h=40c1da7373f93696f9742370c0662f67880e58d34d299ef32851a660eda24248)<br>Abychom byli úspěšní, nesmíme si připustit, že štěstí hraje obrovskou roli v tom, jaký bude nakonec výsledek. Jestliže ale úspěšní budeme, musíme si naopak uvědomit, jak obrovskou roli štěstí hrálo, abychom byli schopni umožnit úspěch i dalším. Neintuitivní? Ano :)
- [Open Source is Broken](https://getpocket.com/redirect?&url=https%3A%2F%2Fdon.goodman-wilson.com%2Fposts%2Fopen-source-is-broken%2F&h=f51b261bdb4b6614ff3c70a7f74e8798e74133ecd220a43f0cb548455b70a1d2)<br>Článek o chybách Open Source tak, jak ho dnes provozujeme. Sdílím ho „k zamyšlení“, ale osobně nesouhlasím nebo přinejmenším zatím nesouhlasím hned s několika věcmi. Vliv OSS na hiring mi přijde přeceněný, ale třeba je to v USA jiné. Vliv na sociální kredit je jistě značný. Že jsem morálně zodpovědný za to, že někdo vezme SW a použije ke „zlu“ (Co je zlo? Spousta zla lze snadno definovat, ale ještě větší spousta bude subjektivní?), to mi přijde jako blbost. Jako by vynálezce motoru byl zodpovědný za to, že díky ním létaly Messerschmitty? Nebo vyrobím kuchyňský nůž a jsem najednou komplicem všech domácích vražd? Pokud dělám nějaký projekt pro radost, nevadí mi, že jej dělám zdarma. Když půjdu uklidit potok od odpadků, taky mě nikdo nezaplatí. Je to Tragedy of Commons? Nedá se to řešit byznys modelem? Pokud mě baví uklízet strouhy, můžu si založit úklidovou firmu. Pokud mě baví dělat OSS, můžu kolem toho vymyslet byznys model. Pokud mi vadí, že můj OSS používají velké firmy, mohu mu dát jinou licenci. Jednotlivcům to bude jedno, velkou firmu to odradí. A možná stačí velkou firmu odradit prostě i jen tím, že to bude GPL, což je pro spoustu případů použití kryptonit. No, nechám to ještě uležet.
- [Rebel na webe (Roman “yablko” Hraška) | Tech Talks](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dd9tjRCF-6SM&h=c4436ef2ee06caeb464b4d753d58657346c7dfe3cf54852a646e84d89c355397)<br>Fajn rozhovor s yablkem o tom, jak začal, o kurzech a o tom, co si myslí o učení programování :) A myslí si totéž, co si myslím i já! A říká to perfektně. Super story o původu přezdívky yablko.
- [Kolaps #1: Pavel Barša: Postavení Evropské unie v mezinárodní politice je trapné](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2020%2F02%2Fkolaps-1-pavel-barsa-postaveni-evropske-unie-v-mezinarodni-politice-je-trapne%2F&h=39f934a1468e9c4d30fb0e1cdd8cfa45f70d8219b6f8625874c06a700f1cd6a5)<br>Rok starý podcast se zajímavým hostem o geopolitice, EU, levici, Británii.
- [Esej Pavla Barši: Obrysy doby po covidu. Hrozí nám nová studená válka – tentokrát mezi USA a Čínou?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.novinky.cz%2Fkultura%2Fsalon%2Fclanek%2Fesej-pavla-barsi-obrysy-doby-po-covidu-hrozi-nam-nova-studena-valka-tentokrat-mezi-usa-a-cinou-40356330&h=0fe72dc8619aba1c48b6cc4798ce6397f79234bc75e8d005fe03411c69178897)<br>Asi lepší se na to jako na možnost psychicky připravit, než být potom překvapen.
- [The road from Rome](https://getpocket.com/redirect?&url=https%3A%2F%2Faeon.co%2Fessays%2Fhow-the-fall-of-the-roman-empire-paved-the-road-to-modernity&h=d4fcceafde44cbc02eb81ebc4bce7c68c4115e722c04f9a18576043921584d3e)<br>Těžko říct, zda rozpad Říma byl tak zásadní (proč nebyl tak zásadní rozpad jiných velkých impérií a nezpůsobil totéž?) a zda je to článek domyšlený do všech detailů nebo jen taková oslava jedné myšlenky, která se snaží všechno spojit dohromady a vyložit, nicméně trochu to smysl dává. Velká říše zamezuje pokroku. Pokrok vzniká díky konkurenci a fragmentaci. Rozpad Římské říše a následná extrémní fragmentace Evropy během středověku byly základem pro naši dnešní prosperitu. Nebo ne? Jak to je dnes? USA (fragementovanější) nebo Čína (centralizovanější) zvládají prosperitu i jako velké „říše“, zatímco EU působí ve své fragmentovanosti málo akčně. Třeba je to ale jen krátkodobý pohled?

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
