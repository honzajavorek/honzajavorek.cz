Title: Týdenní poznámky #101: Yak shaving
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (6.8. — 12.8.) a tak [stejně jako minule]({filename}2022-08-05_tydenni-poznamky-100-marketingova-konzultace-a-psani-tipu-do-onboardingu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tento týden byl ve znamení _yak shaving_ a mám z toho smíšené pocity. Sice jsem udělal spoustu zajímavé práce, která mě i bavila, ale zda to bylo důležité, to je dost pochybné a to nejdůležitější jsem neudělal.

Co přesně znamená _yak shaving_ si buď vyhledejte, nebo si pusťte [těchto nesmrtelných 42 sekund](https://www.youtube.com/watch?v=8fnfeuoh4s8) a pochopíte.


## Dovolená ve Žďáře nad Sázavou

Přes Žďár nad Sázavou jsem několikrát v životě jel, třeba na kole, ale nikdy jsem neviděl zámek, kostel, atd. A [že je na co koukat](https://www.mall.tv/gebrian-prekvapive-stavby/poutni-kostel-sv-jana-nepomuckeho-na-zelene-hore). Udělali jsme si tam prodloužený víkend s kamarády a bylo to fajn.

Z Regiojetu tam a zpět jsem měl trochu smíšené pocity, ale o tom napíšu třeba někdy jindy. Ač jsem vyhejtil bídné sobotní MHD ([po vzoru Hajzlera](https://blog.tomashajzler.com/clanek/o-dalsi-ceste-bez-auta-aneb-tragedie-ceske-verejne-dopravy)), nebo ulici u zámku, kde na několika kilometrech není přechod (a tam, kde asi byl nebo brzo bude, je vyloženě zákaz vstupu chodcům bez alternativy, jak se dostat na druhou stranu frekventované cesty), tak jinak je Žďár celkem pěkný a jde tam vidět snahu o zlepšování veřejného prostoru, což cením. Viděl jsem tam hezká nově upravená místa v centru, kolem zámku a kostela, dobrý je rekreační areál Pilák (připomnělo mi to [Piláta](https://twitter.com/BitchfaceKam/status/1431330071965470723)), kde jsme na pískovišti strávili fakt hodně času.

Několikadenní dovolená s ročním děckem byla hodně o tom, jakou náladu mělo zrovna děcko a jestli chtělo usnout nebo ne, ale i tak jsme si to myslím užili. Žena má teď nohu v ortéze a kdyby byla pohyblivější, asi bychom si to užili víc, ale i tak se to dalo, cestování s kočárkem, batohama a berlema vlakem bylo nakonec jednodušší, než to původně znělo.

Povedla se nám zlomit nějaká tenká tyčka na kočáru, asi proto, že jsme ho po roce poprvé nějak víc skládali a rozkládali a neuměli jsme to ve spěchu udělat správně ([nemáme auto]({filename}2021-08-28_bez-auta.md), tak kočár skládat v 99 % nepotřebujeme). Výrobce (X-Lander) hned napsal, že nám to opraví, což je fajn.


## Psaní tipů na onboarding

Největší prioritou týdne bylo dopsat tipy na onboarding nových členů. Jenže jsem asi neměl vůbec chuť něco psát a měl jsem strašnou chuť ponořit se do programování, takže jsem nenapsal ani písmenko, zato jsem naprogramoval spoustu nedůležitých věcí. Následuje vše, co jsem udělal místo tipů, rozděleno do dvou kategorií: Jednak prokrastinace, jednak finalizace nové stránky o psychickém zdraví během cesty do IT.

### Prokrastinace

- Uklízel jsem si taby v prohlížeči. Myslím, že teď jich mám místo 200 už jen tak 20.
- Koukal jsem na [pyright](https://github.com/Microsoft/pyright) a pak jsem zjistil, že už ho dávno používám, protože je zabudovaný přímo ve VS Code ¯\\\_(ツ)\_/¯
- Pročítal jsem si [newcreatormanifesto.com](https://newcreatormanifesto.com/).
- Opravoval jsem rozbitý build u kódu webů [pyvec.org](https://github.com/pyvec/pyvec.org) a [python.cz](https://github.com/pyvec/python.cz). Dalo mi to celkem práci, nakonec jsem zjistil, že nějaký linter vydal novou verzi a něco jiného s tím nepočítalo. Udělal jsem různé další upgrady, vyřešil některé staré resty a na jednom místě jsem linter prostě odebral, protože jsem neměl morál na to to řešit. Stejně by tam jednou měl být všude [black](https://pypi.org/project/black/).
- Upgradoval jsem Python na JG a u sebe v počítači z 3.8 na 3.10.
- Pyenv jsem přeinstaloval tak, aby nepoužíval na mém M1 macOS Rosettu, ale byl nativně na Siliconu.
- Upgradoval jsem Node.js na JG a u sebe v počítači ze 14 na 16.
- Upgradoval jsem legacy Docker images v CircleCI na nové.
- Čistil jsem nepotřebné závislosti z projektu a upgradoval jiné.

### Finalizace stránky o psychickém zdraví

Tady přichází onen _yak shaving_. V rámci prokrastinace psaní tipů, ale taky v rámci svých priorit na tento týden, jsem se pustil do finalizace stránky o psychickém zdraví, která už byla celá napsaná, stačilo jen překopírovat texty z Google Docs do Markdown souboru. Práce na 15 minut, že?

Text jsem prošel a udělal ještě pár kosmetických editací. Začal jsem pak text předělávat do Markdownu. Bylo tam hodně seznamů s užitečnými odkazy, které v příručce na JG mají vždy boxík a v boxíku je i screenshot.

Proces vytváření screenshotů byl doteď manuální: Vytvořit kartu v Markdownu, dát tam URL, dát tam cestu k budoucímu obrázku, Přidat URL do texťáku se seznamem URL, spustit skript na screenshoty. To mě teď brzo přestalo bavit a hlavně jsem zjistil, že jak jsem různé věci upgradoval, [nejsem schopen knihovnu na screenshoty už nainstalovat](https://github.com/sindresorhus/pageres/issues/420).

Rozhodl jsem se, že to takhle dál nejde a šel jsem ty screenshoty předělávat. Autor knihovny `pageres` má novější, `capture-website`, ale pak jsem si vzpomněl ještě na to, že Simon Willison [psal o nějakém udělátku na screenshoty](https://simonwillison.net/2022/Mar/14/scraping-web-pages-shot-scraper/) a tak jsem to šel prozkoumat. Trocha studování, jak to funguje a nakonec jsem teda použil přímo [playwright](https://playwright.dev/) přes jeho Python knihovnu. Funguje to krásně a dokonce to zjednodušuje i proces instalace browseru, který se na screenshoty použije a nemusím instalaci nikde komplikovaně řešit, ať už je to u mě na počítači, nebo na CircleCI.

Začal jsem kompletně předělávat, jak funguje screenshotovací skript, jak se vyhodnocuje co se stáhne a jak, předělal jsem stahování cover obrázků FB skupin, ladil jsem různé CSS selektory, díky kterým na screenshotech nejsou cookies lišty apod. smetí, no prostě vložil jsem do toho hodiny a hodiny času. Vždy jsem o něco zavadil a zjistil, že to musím předělat taky. Řešil jsem také, jak by to mohlo dělat screenshoty samotného JG, protože na dvou (a v budoucnu na víc) místech to potřebuji.

Každopádně ten playwright je super a díky Python knihovně můžu jednoduše ovládat browser na pár řádcích, nemusím nad tím moc přemýšlet (na rozdíl od Selenia) a nemusím pouštět žádný JavaScript jako subprocess, nebo něco podobného. Screenshot to umí vrátit rovnou jako bajty, což je fajn, pokud jej chci před uložením ještě upravit, apod. Slibuji si od toho zrychlení některých operací a zjednodušení kódu, méně žonglování mezi procesy.

Nakonec jsem do playwrightu předělal i kód, který mi z HTML generuje obrázky (např. náhledy pro sociální sítě, plakátky pro přednášky v klubu, plakátky pro podcasty, apod.) a `pageres` úplně vyhodil.

Pak jsem ještě dodělal kód, který prochází všechny vygenerované HTML soubory webu a hledá odkazy na screenshoty. Tyto pak bere skript na screenshoty jako „požadavky na screenshot“. Když screenshot existuje, tak v pohodě, když ne, tak ho udělá.

Dva měsíce staré screenshoty automaticky expiruje, takže na to nemusím myslet a stačí prostě čas od času skript na screenshoty ručně pustit (třeba když potřebuju screenshotovat nový odkaz) a on vše vyřeší za mě. Tím pak ještě vznikl prostor pro to, abych vůbec nemusel do Markdownu psát cestu k souboru se screenshotem. Vygeneruje se sama přímo z URL a screenshotovací skript už ji jen použije jako cestu k souboru, který má hledat a případně vytvořit.

Ještě jsem měl v kódu skript, který ve výsledném HTML hledal rozbité odkazy na #idčka v textu. Ten jsem rozšířil a přidal kontrolu všech odkazů mezi stránkami a k tomu potom ještě kontrolu obrázků, jestli existují. To mi pomohlo vychytat, jestli jsem při všech těch změnách na něco nezapomněl. Frozen-Flask totiž rozbité odkazy tak nějak kontroluje sám od sebe a spadne, když odkaz nikam nevede, ale MkDocs, mám dojem, už moc ne, prostě tam vygeneruje klidně hloupost a neřeší to.

Pak jsem teda stránku o psychice dosázel do Markdownu, radoval se jak vše hezky funguje, a poslal to [Nele](https://www.nelaprovazi.cz/), se kterou jsme to psali. Nela řekla, že je to super, ale ať počkám se spuštěním, takže to teď ani neukážu, ten skvost, ale je už připravený. V plánu je spustit to brzy, za týden nebo dva.

Tož to bylo zhruba tři dny místo patnácti minut. Selhání? No jako jo, sice jsem si škrtl jednu věc, kterou jsem dlouho odsouval, ale tři dny zabrat fakt neměla a neměl jsem komplet předělat, jak se dělají na JG screenshoty. Ale mě se asi fakt nechtělo zrovna nic psát a to programování mě doopravdy bavilo. A čím jednodušší budou editace v příručce, tím častěji je budu dělat a něco přidávat. Chtělo by se mi napsat, že se díky tomu všemu zrychlil build na CircleCI, protože se věci instalují rychleji a screenshoty se dělají rychleji, ale není to rychlejší. Jestli, tak třeba o minutu. No nic, příští týden už opravdu ten onboarding dodělám.


## Další poznámky

- Půjčil jsem Danovi elektrický kávový mlýnek, aby mohl vařit kafe na [RealUXCamp](https://realuxcamp.com/) 2022. Dal mi na víkend ruční mlýnek. Myslel jsem, že to bude romantické, mlít to zase rukou, ale je to spíš nekonečné. Škoda, že to nemůžu naučit naše batole, které by to asi bavilo víc. Dan ode mě dostal i JG samolepky a doufám, že jich tam rozdá co nejvíc.
- Zabýval jsem se dalším stipendiem. Napadlo mě u toho, že je to teď skoro jedno stipendium týdně a že „stipendium _is new_ nový pracovní inzerát na junior.guru/jobs“, tedy manuální činnost, kterou dělám už příliš často na to, aby to takhle šlo dělat dál. Mám nějaké nápady, jak to automatizovat, ale všechno je to moc práce, tak počkám, jak se to bude vyvíjet, nebo jestli mě nenapadne něco ještě jednoduššího.
- Dostal jsem pozvánku na [hackercamp.cz](https://www.hackercamp.cz/), ale nebudu nejspíš v té době vůbec v ČR. Aspoň doufám. Větší dovolenou jsem pořád nedokázal vymyslet a naplánovat. Ortéza teď navíc vše komplikuje.
- Koukal jsem, že Discord to myslí s komunitami vážně a vytvořil pro ně [celý speciální portál](https://discord.com/community) a video pro začínající komunitní adminy .
- Sociální sítě jsem zanedbával a nic na ně nedával. [Posteskl jsem si na Twitteru](https://twitter.com/honzajavorek/status/1555639353740853248), že už mě moc nebaví. Pak už jen pár storíček o tom, jak ve Žďáře nad Sázavou chybí přechody nebo tweet o tom, jak [starostka Prahy 5 zbytečně brání výstavbě](https://twitter.com/honzajavorek/status/1557012318134976515). To si vysloužilo skoro 170 srdíček. Dělám to dobře, tu kampaň, že? Škoda, že srdíčka nejsou hlasy. A škoda, že nekandiduju ani ve Žďáře, ani na Praze 5, ale na Praze 3.
- Upravil jsem ještě dvakrát uvítací zprávu, kterou bot posílá novým členům. Vylepšuju krůček za krůčkem podle toho, jak to (ne)funguje na lidi.
- Klub, maily, a tak dále. Tento týden byl v tomto směru naštěstí celkem klidný.
- Během 7 dní od 6.8. do 12.8. jsem při procházkách nachodil 19 km. Celkem jsem se hýbal 14 hodin a zdolal při tom 19 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Dvě věci, které bych chtěl zvládnout udělat příště:

1. Dodělat první verzi zpráv pro onboarding a pustit je do první testovací skupiny lidí.
2. Vymyslet nový ceník pro firmy.
3. Zpracovat poznámky z hovoru s mentorem a prodiskutovat je s ostatními mentory.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [#30 - s Marií Šabackou o klimatické změně](https://anchor.fm/heroine/episodes/30---s-Mari-abackou-o-klimatick-zmn-e1bo7iv)<br>Fajn rozhovor, celkem střízlivý pohled.
- [Will Taiwan Trigger WW3 by 2027?](https://www.youtube.com/watch?v=p6sCsOdqXQw)
- [Ukrajina tlačí na Rusko. Přebírá strategii a nutí Moskvu přemisťovat vojska, uvádí analýza](https://www.irozhlas.cz/zpravy-svet/online-valka-na-ukrajine-rusko-studium-pro-valku-vojska_2208051024_ban)<br>Naděje
- [China's Catastrophic Oil & Gas Problem](https://www.youtube.com/watch?v=ISHHe1Hu6d4)<br>Tohle vysvětluje fakt hodně věcí, které se kolem Číny dějí.
- [Čínská armáda je na nohou a cvičí kolem Tchaj-wanu. O jaké vojsko jde?](https://www.voxpot.cz/cinska-armada-je-na-nohou-a-cvici-kolem-tchaj-wanu-o-jake-vojsko-jde/)
- [Productivity Porn](https://calebschoepp.com/blog/2022/productivity-porn/)<br>„I just learned something new, you tell yourself. And while this is true, you never actually did the thing you were setting out to do in the first place.“

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
