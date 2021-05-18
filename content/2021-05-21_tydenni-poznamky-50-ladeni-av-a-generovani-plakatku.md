Title: Týdenní poznámky #50: Ladění AV a generování plakátků
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (10.5. — 16.5.) a tak [stejně jako minule]({filename}/2021-05-07_tydenni-poznamky-49-cenik-ama-vylepsovani-klubu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Akorát že není pátek, je pondělí. Padesáté poznámky jsem nestihl napsat v pátek a o víkendu na to nějak nebyla chuť a čas.

## Audio video

S [Danem Srbem](https://coreskill.tech/) jsme si jeden den spontánně zavolali, abychom si něco rychle řekli, ale vyústilo to v call na celé odpoledne, kde jsme řešili detaily nahrávání, učil mě pořádně ovládat a nastavovat [OBS](https://obsproject.com/), apod.

Řešili jsme hlavně zvuk a to, aby se nestala stejná chyba, jako při AMA s Jirkou Psotkou. Nastavil jsem [Apple VT H264 Hardware Encoder](https://obsproject.com/forum/threads/%E2%80%9Capple-vt-h264-hardware-encoder-unlocked-for-apple-silicon-m1.138433/), který by měl být lepší pro M1, zvyšovali bitrate audia, koukali jsme na [různé filtry](https://www.izotope.com/en/learn/audio-dynamics-101-compressors-limiters-expanders-and-gates.html), které mi mohou pomoci ladit zvuk, předělali jsme způsob, jakým se posílá zvuk do [BlackHole](https://github.com/ExistentialAudio/BlackHole/). Předtím jsem měl multi-output device, kde audio z počítače bylo nastaveno tak, aby šlo do něj. Z něj šlo do mých sluchátek a do černé díry, na které poslouchalo OBS. Teď to bude tak, že v Discordu nastavím výstup na černou díru a v OBS budu mít zapnutý odposlech, takže ve sluchátkách uslyším přímo to, co se nahrává (kromě sebe, protože slyšet se mluvit, zatímco mluvím, není moc užitečné). Také díky tomu můžu přímo v OBS nastavovat hlasitost svoji a zvuku z Discordu, aby byla stejná. Změny jsem si hned poznačil do [svého seznamu úkonů](https://gist.github.com/honzajavorek/b1a77651e566cb6405a131bbf1fb0692). Zvažovali jsme i nahrávat do různých stop, aby šlo případně dělat postprocessing pro každý hlas zvlášť, ale nechci s tím trávit víc času, než je nutné. Bude muset stačit, že to nahraju na první dobrou prostě dobře.

Dále jsem s Danem a bráchou a probíral mikrofony a sluchátka, poznačím si tady odkazy na věci, o kterých byla řeč:

- [Sennheiser PXC 550 II Wireless](https://sluchatka.heureka.cz/sennheiser-pxc-550-ii-wireless/)
- [Cooler Master MasterPulse MH751](https://sluchatka.heureka.cz/cooler-master-masterpulse-mh751/)
- [Marantz Pro Pod Pack](https://kytary.cz/marantz-pro-podpack1/HN220994/)

Kupovat zatím nic nebudu, je to dost peněz. Možná ten mikrofon. Sluchátka mám blbá, ale to mi přijde zatím dost drahý špás na to, že pro výkon při přednáškách není tolik podstatný. Ale na běžné domácí poslouchání by se mi lepší hodily: ANC by bylo fajn, nicméně chci Bluetooth (na poslech při domácích pracech) i jack (na nahrávání přednášek) a hlavně aby mi neskřípaly moc hlavu, protože to ty moje teď dělají a moc dlouho v nich nevydržím.

Dan také pracoval na opravě zvuku u AMA s Jirkou Psotkou. Dohodli jsme se, že pokud to nepůjde automaticky, tak 2 hodiny záznamu ručně procházet nebude, řekne mi co a jak a já to jako dělník naklikám. Ale nakonec to udělal celé sám, za což bych mu chtěl ještě jednou velice poděkovat! V jednu chvíli mi poslal „opravený“ záznam, který jsme pak ale zjistili, že je nějaký vadný. Jenže mezitím jsem ho už nahrál na YouTube a dal členům klubu, takže pak jsme dělali ještě jedno kolečko. Trochu Pat a Mat, nicméně finální, třetí video je už opravdu to nejlepší, co z toho vyždímeme. Dali jsme tam i sekce, na které jde klikat.

Záznamy běžně nikde neuveřejňuji, jsou jen pro členy klubu a jejich „kamarády“. To znamená, že je mohou volně poslat i někomu jinému, zhruba stejně, jako by odemykali článek v novinách za paywallem. AMA s Jirkou byla ale tak dobrá, že na ni [dám odkaz i tady](https://www.youtube.com/watch?v=-POZC63Chuk). Stejně ty moje grafomanské poznámky nikdo nečte, takže to nebude žádný velký leak. A kdo to čte, je můj kamarád. Asi.

A pokud to leak bude, aspoň lidi uvidí, co se v klubu odehrává a budou chtít do něj. Nebo budou chtít svou firmu prezentovat podobně a bude z toho další hezká AMA!

## Umělá inteligence pro nabídky práce

Nedávno jsem jel s [Mílou](https://milavotradovec.cz/) na kole na výlet, abychom se domluvili, co dál s nabídkami práce. Plán byl, ale čekalo to na mě. Priorita to není, jenže když se čeká na maintainera moc dlouho, contributorům opadne nadšení a najdou si jiné vyžití. Machine learning se musí kout, dokud je Míla žhavý.

Takže jsem se do toho pustil a připravil mu podhoubí pro jeho další změny. Vytvořil jsem tajnou místnost na Discordu, kam padají nabídky, na kterých se můj robot a Mílova ML magie neshodnou. Tam je můžu já a případně další dobrovolníci hodnotit pomocí palců nahoru dolu, jestli si myslíme, že jsou juniorní nebo ne. To bude zpětná vazba pro učení. Naprogramoval jsem posílání nabídek do místnosti a sosání palců zpět do databáze. Míla by to asi dokázal udělat taky, ale já už přesně věděl jak a co, protože jsem tyhle věci všechny nedávno dělal, takže jsem to měl docela rychle. Nejsem na to nějak hrdý, je to celkem naprasené, ale zatím to bude stačit a snad to zajistí, že Mílovo nadšení neuhasne.

Následně vždy, když tam něco přibylo, tak jsem se to snažil poctivě rozklikávat a ohodnotit. Dobré je, že to jsou jen jednotky nebo desítky nabídek, takže je to v mých silách. Kdybych měl hodnotit vše, co můj robot vyřadí, tak to je třeba jen za dnešek 344 nabídek. To by mi trvalo projít celý den. To není odhad, to vím, protože když jsem robota programoval, tak jsem to fakt procházel a projít nízké stovky nabídek spolu s úpravami v robotovi mi trvalo zhruba jeden pracovní den.

Při rozklikávání nabídek jsem si všiml, že LinkedIn u některých ukazuje i osobu, která nabídku zadala. Proaktivně jsem si osoby vždy rozkliknul přidal si je, když už jsem se na danou nabídku koukal. Pokud si mě přidají, budou se jim zobrazovat moje statusy o JG a třeba z toho bude byznys.

## Generování plakátků

Začal jsem pracovat na automatizaci úkonů, které dělám kolem každé přednášky. Ideální bylo začít automatickými zprávami, které budou upozorňovat na blížící se přednášku, protože bych je hned vyzkoušel na úterní přednášce s Vildou. Jenže to se mi nechtělo, tak jsem pracoval na generování plakátků, které teď nutně nepotřebuji.

Díval jsem se, jak lze z HTML a CSS vygenerovat obrázek. Inspirovala mě k tomu zpráva, že Google Documents [se budou nově renderovat přes canvas](https://workspaceupdates.googleblog.com/2021/05/Google-Docs-Canvas-Based-Rendering-Update.html). Třeba existují nějaké voňavé nové technologie, které by mě zbavily nutnosti spouštět prohlížeč a dělat screenshot? Našel jsem [tuto hezkou odpověď](https://stackoverflow.com/a/46243263/325365), kde je spousta nástrojů a API. Různé jsem zkoušel, ale nakonec jsem došel k tomu, že nic není rychlejší, lepší nebo jednodušší než to, co už používám na náhledy stránek (tzv. `og:image`), tedy že vygeneruju HTML přes Jinja2 a uložím screenshot přes [pageres](https://github.com/sindresorhus/pageres). Takže jsem si hezky početl a pohrál, ale používám dál to, co už jsem dávno měl.

Doplnil jsem [data o přednáškách](https://github.com/honzajavorek/junior.guru/blob/master/juniorguru/data/events.yml) tak, aby z nich šlo generovat plakáty. Ještě se z nich negeneruje ani [tahle stránka](https://junior.guru/events/), ale jednou určitě bude. Plakáty jsou zábavnější!

Začal jsem generovat HTML ze šablon, ale při tom jsem se rozhodl překopat půlku repozitáře, protože jsem najednou potřeboval tyto obrázky generovat v první fázi buildu webu, která pracuje jen s daty, ne během samotného sestavení stránek. Tu první fázi jsem přejmenoval z `fetch` na `sync`, protože mi přišlo, že už je tam hromada věcí, které nejen data stahují, ale i posílají, např. do Discordu. Mám ale pravidlo, že tam smí být jen věci, které jsou [idempotentní](https://cs.wikipedia.org/wiki/Idempotence), což moje skripty nad Discordem zásadně jsou. Posílání e-mailů je jinde, aby se omylem třeba neodeslaly duplicitně. Taky jsem si konečně napsal ty dva řádky, které zajistí, že pokud chci spustit jen část z té první fáze, nemusím psát `pipenv run python -m juniorguru.fetch.stories`, ale stačí `pipenv run sync stories`.

Přehazoval jsem vidlema soubory sem a tam, protože jsem přemýšlel, kde bude nejlepší mít obrázky a kde styly, když už najednou nejsou záležitostí webu, ale i jiných částí JG. Připravil jsem si fotky speakerů a napsal skript, který je automaticky zmenší na požadovanou velikost, takže mi bude u nových stačit je oříznout na čtverec libovolné velikosti a hodit do složky. Stahování avatarů z Discordu pro speakery, kteří by svou fotku neměli, jsem zatím zavrhl jako YAGNI. Plakátky se generují hezky a generuju i čtvercové pro sdílení na Instagramu, což jsem doteď taky dělal ručně. Zatím to není nikde vidět a nemám to ostylované, takže to není hezké, ale základ funguje:

- [Vilda](https://junior.guru/static/images/posters/5f41c3bf961b1f2b4256fd5e5b1ea899db69f0770ca42bde719ad346502a2ff5.png)
- [Vilda jako čtverec](https://junior.guru/static/images/posters/5f41c3bf961b1f2b4256fd5e5b1ea899db69f0770ca42bde719ad346502a2ff5-ig.png)

S tímto jsem v pátek skončil a myslel jsem si, že napíšu poznámky a bude hotovo. Jenže jsem pak objevoval spoustu drobných chyb, které jsem při těch velkých změnách ve struktuře projektu nadělal. Web JG třeba najednou neměl CSS. Postupně jsem je opravoval, ale narazil jsem na chybu, kterou jsem vyřešit neuměl. Chyběly některé obrázky. To jsem řešil následující 2 hodiny bez velkých úspěchů a než jsem si vytrhal všechny vlasy, opravil jsem to nakonec tím, že jsem downgradoval Flask z nové v2 na menší, což tedy byla věc, která se odehrála už před několika dny a s pátečním překopáním webu vůbec nesouvisela.

Downgrade Flasku samozřejmě neproběhl jen tak, protože `pipenv install` si začalo najednou stěžovat na nějaký problém s kompilací SciPy. Musel jsem číst pomalu darknet, abych našel řešení, které zjevně na M1 je:

```
$ brew install openblas gfortran
$ export OPENBLAS=$(/usr/local/bin/brew --prefix openblas)
$ export CFLAGS="-falign-functions=8 ${CFLAGS}"
```

A pak teprve instalovat SciPy. Poté jsem mohl pokračovat debugováním původního problému. Naštěstí downgrade Flasku opravdu pomohl. Chyba je někde tam, Frozen-Flask asi nepočítá s některými změnami v novém Flasku, ale nešlo to naprvní pohled nijak vidět ani to nikde neskončilo chybou, pouze _občas_ zmizely _některé_ obrázky!

Hned bych to nahlásil maintainerům Frozen-Flask, kdybych nebyl maintainerem Frozen-Flask. Bezmoc. Aspoň jsem to pak trochu zdokumentoval [tady](https://github.com/Frozen-Flask/Frozen-Flask/issues/112#issuecomment-841629172). Mimochodem zrovna tento týden se mi ozval nějaký člověk, který se chce stát maintainerem Frozen-Flask, tak jsem mu odepisoval, že na to nemám čas, stejně jako všichni maintaineři přede mnou, tak ať se klidně přidá. Možná bych se mohl pověnovat aspoň tomuto zákeřnému bugu a napsat na něj test nebo jej lépe zdokumentovat, uvidíme.

Když už jsem myslel, že jsem vše opravil, zjistil jsem, že jsem si sice hezky pohrál s CSS [custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) pro barvy, ale dal jsem je i do `linear-gradient()`, kde mi nefungují pro hex čísla, do `rgba()` musím dávat jednotlivé složky. Když jsem barvy měl původně v SCSS proměnných, fungovalo to.

No jinými slovy, vše jsem rozbil a pak jsem to celý večer lepil a byl jsem následně zralý na velké klikání na [Miluji práci](http://milujipraci.cz/). Na poznámky nedošlo. Už jsem jen odpadl, pustili jsme si s investorkou seriál a šli spát. Super pátek. Naštěstí to vyvážila párty neděle, kdy se kamarádi stavili k nám na Žižkov na partičku [Bangu](http://www.bang.cz/).

## Další poznámky

- Zjistil jsem, že i když nemám nějak extra boostnutý Discord server, v základu můžeme mít 50 custom emojis. Pár jsem jich přidal a to dále spustilo lavinu všelijakých požadavků na emoji :D Máme [gumovou kachnu](https://en.wikipedia.org/wiki/Rubber_duck_debugging) i hlavu [yablka](http://robweb.sk/).
- Na [python.cz](https://python.cz/) jsem opravil pokažený auto-deploy. Z nějakého důvodu se skriptu nedařilo přepsat `gh-pages` větev, tak jsem zkusil nějaký nový GitHub token a ještě jsem větev ručně smazal a vyrobil znova. To zabralo ¯\\\_(ツ)\_/¯
- Člen klubu nasdílel [svůj projekt](https://github.com/SveterCZE/justice), kde si hraje s daty ze státních rejstříků. Prošel jsem jej, nainstaloval, stáhl data, napsal mu na to poctivě feedback, to mi zabralo tak hodinu nejmíň.
- Díval jsem se na [Show & Tell](https://cesko.digital/show-and-tell) Česko.Digital. To mi připomenulo, že jsem chtěl dodělat API na pracovní nabídky. Otevřel jsem [PR s otázkami ohledně dokumentace](https://github.com/cesko-digital/cd-tools/pull/9). Taky jsem si vzpomněl, že jsme chtěli na blogu Česko.Digital vydat článek o tom, jak se může juniorka zapojit, ale ten někde uvízl ve schvalovacím procesu. Šťouchl jsem do toho opět, ale zatím bez výsledku. Je to škoda, protože pokud to chápu dobře, tak už je připravený a napsaný. Holt budu čekat dál. Nechci zas lidi moc otravovat a stále to připomínat.
- Naplánoval jsem zase nějaké statusy na sociální sítě.
- Pročetl jsem příběhy o career switchers na blogu Mews a všechny tři se mi nakonec líbily: [Mike](https://developers.mews.com/a-different-kind-of-magic-mike/), [Daria](https://developers.mews.com/meet-the-mewsdevs-daria/), [Markéta](https://developers.mews.com/marketa-linguist-who-found-love-in-sql-and-portugal/). Přidal jsem je na JG. Pokud máte nějaké další příběhy a nejste vzdělávací agentura, sem s nimi! Success stories vzdělávacích agentur nepřebírám v rámci nezávislosti, byť nijak nechci umenšit autentičnost jednotlivých životních příběhů a povedených kariérních změn, příběhy v režii agentur jsou psány s určitým zadáním. Pokud je to ale na blogu firmy, kterou neživí kurzy, tak v pohodě.
- Přišel inzerát prácovní nabídky, takže jsem ho přidal a vyfakturoval. Jupí!
- Volal jsem si s právničkou a vymysleli jsme spolu, jak upravíme obchodní podmínky. Poslal jsem jí pak nějaké dokumenty a prý to bude další týden hotové. Uvažoval jsem, zda místo kupónu neřešit zpětné proplácení členství vzdělávacími agenturami přes speciální typ předplatného, ale nakonec jsem zůstal u kupónů, protože jinak, pokud by členům vypršelo proplacené předplatné, nemohli by tak snadno přejít na předplatné, které si platí sami. Když je to přes kupón, stačí když zadají kartu a jedou dál za svoje.
- V souvislosti s tím jsem si psal s Memberful supportem a snažil se lépe pochopit to, jak fungují kupóny, protože jsem některé věci nechápal. Samozřejmě mají všechno v [dokumentaci](https://memberful.com/help/how-to/create-a-coupon/), ale chtěl jsem jim dát trochu i zpětnou vazbu, jak jsou některé věci neintuitivní nebo i matoucí.
- Levels na remoteok.io [změnil chování API](https://twitter.com/levelsio/status/1391701746615918595), což rozbilo můj scraper. Nevím, k čemu je dobré, že jeho JSON umí detekovat robota na náhledy a v takovém případě vrátí HTML, jestli je to nějaké lepší SEO, ale jako člověku, který trochu rozumí API, mi to přijde jako velké kacířství. Dobré bylo, že přímo v HTTP odpovědi bylo aspoň hned napsáno, jak to mohu opravit: _Getting this page as an API reply? Make sure your User Agent string does not contain the words "bot" or "google". Or add ?api=1 to force the JSON reply._ Scraper jsem tedy opravil. Můj `User-Agent` je standardně `JuniorGuruBot (+https://junior.guru)`.
- V robotovi na pracovní nabídky jsem opravil chybu, která u některých nabídek odkazovala přímo na „apply“ formulář místo na popis nabídky.
- ČSFD mají novou verzi webu, takže už mi zhruba týden nefungovalo přidávání filmů do Trella přes [film2trello](https://github.com/honzajavorek/film2trello). Opravil jsem to a smazal spoustu kódu, protože teď je přímo na stránce s filmem i odkaz na Aerovod, takže nemusím zvlášť scrapovat katalog Aerovodu a párovat filmy. Občas nicméně přidání filmu timeoutuje, protože scrapnutí stránky a interakce s Trello API trvá a děje se to všechno během requestu, zatímco Vercel, kde to jede, má pro free uživatele limit [jen 10s](https://github.com/honzajavorek/film2trello/issues/57). Řešit jiné cloudy kvůli takové blbosti se mi nechce. Prostě to bude timeoutovat, pokud to bude trvat dlouho ¯\\\_(ツ)\_/¯ Dost často to dlouho netrvá a funguje to správně.
- Aby nebylo málo změn v repozitáři JG, které mohou něco rozbít, sloučil jsem build steps pro linter a testy. Samozřejmě to rozbilo minimálně seznam build steps, které když projdou, tak na základě nich GitHub považuje Pull Request za zelený bez ohledu na to, jak dopadly ty ostatní build steps (vhodné např. pokud chci kontrolovat rozbité odkazy, ale nechci, aby se kvůli nim nemergnul Pull Request od dependabotu).
- Narazil jsem na Open Source alternativu ke [Google Fonts](https://docs.xz.style/fonts/). Sympatické! Bohužel (?) na JG nemám jediný custom font, takže zatím nevyužiju. Moje fonty nikoho netrackují a načtou se okamžitě.
- Skript, který stahuje a analyzuje zprávy na Discordu, se mi rozbil, protože jsem přidal private místnost na nabídky práce, kam nemá můj bot přístup. Uvědomil jsem si, že to nemám moc dobře vyřešené, že by měl takové věci umět sám přeskakovat a číst jen místa, kde je public přístup. Skript jsem upravil. Bohužel to nejde udělat jednodušeji, než kontrolovat oprávnění u každého kanálu, ale aspoň to nejsou další API cally, jde to pomocí [discord.py](https://github.com/Rapptz/discord.py) zjistit z už dostupných dat.
- Udělal jsem první promo na [konferenci Frontendistů](https://frontendisti.cz/konference), ale ještě budu dělat další. Asi bude i překvapení pro členy klubu, ale musím ho domyslet.
- Propagoval jsem [přednášku s Vilibaldem Wančou o „životě HTTP požadavku“](https://junior.guru/events/#planned), která bude zítra.
- Chtěl jsem už konečně začít pracovat na materiálu, který připravujeme společně s Engetem, ale úspěšně jsem to prokrastinoval. Jenže jsem koukal, že ani oni nic nemají, tak že asi dobrý. V pátek přišel status check, jestli stíhám, že oni si to připravují v dokumentu vedle a do toho společného dají jen věci, kterým mám udělat review :D Takže fail, nestíhám a jsem pozadu. Každopádně jsem ještě v pátek i přes debugování všeho, co se mi na webu rozbilo, stihl do dokumentu dát aspoň základní draft odstavců, na kterých budu dál pracovat. Nejtěžší je začít, že? Tak jsem začal.
- Vyprší mi lítačka a vlastně nevím, jestli chci novou, nebo ne. Mám pocit, že jsem nikam rok nejezdil a když už jsem někam jel, tak na kole. Bydlím na místě, kde vše zařídím pěšky. Zkusím to bez lítačky a nechám se překvapit.
- Během 10 dní od 8.5. do 17.5. jsem naběhal 26 km, při procházkách nachodil 37 km, na túrách nachodil 1 km. Celkem jsem se hýbal 17 hodin a zdolal při tom 64 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Pracovat na materiálu, který připravujeme společně s Engetem.
2. Přednáška s Vildou, automatizovat dál věci kolem přednášek.
3. Promovat dál [konferu Frontendistů](https://frontendisti.cz/konference).

**Bonus:** Shánět někoho dalšího na přednášku, ale možná si dám i chvilku pauzu, ať stíhám dělat i jiné věci. Chlapů mám pár v zásobě, bral bych spíš ženy.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Jak to mají mileniálové s bydlením? Často mizerně. Rodiče jim ale vštípili, že stát to řešit nemusí](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F05%2Fjak-to-maji-milenialove-s-bydlenim-casto-mizerne-rodice-jim-ale-vstipili-ze-stat-to-resit-nemusi%2F&h=a56166608737415e3f036e9fcf94a1e69542faa05f69f65aac1d84b167571eca)<br>„Zdejší mentalita, utvářená tradicí dědit byty po rodičích a přesvědčením, že každý se musí snažit a pomoct si sám, nedává mnoho prostoru pro hledání řešení, jež by pomohlo zlepšit kvalitu života velkého počtu lidí.“
- [Jay Clouse 📍](https://getpocket.com/redirect?&url=https%3A%2F%2Ftwitter.com%2Fjayclouse%2Fstatus%2F1389313659600506885&h=bda3506996991d551774d13a2f7cc729895884397797af2f776cda7629c3dfca)<br>Vlákno o tom, jak obtížné je vytvořit funkční placenou komunitu a jak nemáte nic pod kontrolou. Říkám si, že je to trochu takové zemědělství, déšť a slunce nelze ovlivnit stejně, jako nelze ovlivnit lidi.
- [Avoid These Common Mistakes Junior Developers Make!](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D5g3dK2DgW-k&h=db77adb41c55bd6949e1158d58140ff7024417d2fa46015036ede52b23528553)<br>8 zajímavých rad od mého oblíbeného youtubera, které osvětlují několik základních aspektů práce vývojáře
- [Pavel Barša: Ve Vrběticích k žádnému teroristickému útoku nedošlo](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F05%2Fpavel-barsa-ve-vrbeticich-k-zadnemu-teroristickemu-utoku-nedoslo%2F&h=fb67b2864b31045974499880fed0b40e69398caf1a0d76d1f5513271b29fa1ee)
- [Komentář: Opozice pořád nepochopila, proč vyrazit mezi lidi](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Fkomentar-opozice-porad-nepochopila-proc-vyrazit-mezi-lidi-153463&h=d63f1da8592d7f7b06de037c6d463cb82bec2960bb02ad10e47281b5a2e70f3e)<br>Jak se strany připravují na volby
- [Inside the mind of a master procrastinator](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.ted.com%2Ftalks%2Ftim_urban_inside_the_mind_of_a_master_procrastinator%3Flanguage%3Den&h=ce29ce6713d5457dbc1aee1d99ff7a4ca3483856793e1cfbb0fb13b834a8c077)
- [Ani pro školu nezbylo slušné místo. Příběh nové čtvrti u Nákladového nádraží Žižkov ](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F05%2Fani-pro-skolu-nezbylo-slusne-misto-pribeh-nove-ctvrti-u-nakladoveho-nadrazi-zizkov%2F&h=5d741e44ba71dc3d6be5671a47ceee10250d0d20c24b8468d59c76e8213cb62f)<br>Zajímavý pohled na novou čtvrť na Žižkově a průlet historickými návrhy, jak mohla vypadat (uf…)
- [A Game Designer’s Analysis Of QAnon](https://getpocket.com/redirect?&url=https%3A%2F%2Fmedium.com%2Fcuriouserinstitute%2Fa-game-designers-analysis-of-qanon-580972548be5&h=9d2496419afb91d236e242e52afe6a5c985cdd99a05d09a50d0aac28b1db70fb)<br>QAnon jako alternativní žitá realta, rozbor od herního designéra
- [Babel is used by millions, so why are we running out of money?](https://getpocket.com/redirect?&url=https%3A%2F%2Fbabeljs.io%2Fblog%2F2021%2F05%2F10%2Ffunding-update.html&h=13c68645d1daffb715c30da657814eeea2f0377959180fcc72a462796eb3bf8a)<br>„Babel continues to be used by thousands of companies all over the world. It's integrated into all kinds of frameworks in the JavaScript ecosystem, whether it's React, Next.js, Vue, Ember, Angular, etc. We are hitting over 117 million downloads/month.“ A přesto nejsou schopni sehnat dost peněz. Je Open Source fakt odsouzeno k Tragedy of the commons?
- [Pro voliče SPD přestala současná podoba demokracie dávat smysl. Věří tomu, kdo zájem o jejich problémy aspoň předstírá](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F05%2Fpro-volice-spd-prestala-soucasna-podoba-demokracie-davat-smysl-veri-tomu-kdo-zajem-o-jejich-problemy-aspon-predstira%2F&h=6a185b1e4badded0364dfd12a0a1ad72b6806724df1eb5115ec8376dbb376e89)<br>Ještě se budeme divit. Mnozí tleskají pádu ČSSD a neuvědomují si, že ti lidé nepůjdou místo toho volit Piráty.
- [The one where writing books is not really a good idea](https://getpocket.com/redirect?&url=https%3A%2F%2Fellegriffin.substack.com%2Fp%2Fcreator-economy-for-fiction-authors&h=4fc241ee591f8f649b70ea74360a4ee38c80ffd06f245e1336148cc710851e3a)<br>Autorka zkoumá, jestli se dnes dá uživit beletrií a pokud, tak jak.
- [Komentář: Daň z nemovitosti je kapitalistická. Víc než česká pravice](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Fkomentar-dan-z-nemovitosti-je-vic-kapitalisticka-nez-ceska-pravice-154336&h=d768ce664615b6ec57ce2b97ad8ae0fd837d4484ff8382881d8336748f69acae)<br>Ano prosím: „I majetkové daně mohou být progresivní, mohou se zvyšovat s každou další vlastněnou nemovitostí.“ Akorát nemovitost lze předpokládám koupit i na firmu a firem může mít každý kolik chce. Ještě by se to muselo domyslet, nicméně přesně takto bych si myslel, že by to mělo fungovat.
- [„Otázky ženské není...“ České prezidentské soužení](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.heroine.cz%2Fspolecnost%2F4719-otazky-zenske-neni-ceske-prezidentske-souzeni&h=84a61fa36c3b00eaff73d57057418f9976f5b019caff5f21eb375c507bbcd3ce)<br>Budeme mít někdy prezidentku nebo premiérku?
- [The Church of Interruption](https://getpocket.com/redirect?&url=https%3A%2F%2Fsambleckley.com%2Fwriting%2Fchurch-of-interruption.html&h=1773a1fb0a1c9661616d7b79b330efa5b8d4db816782cccacbbae4b6399a660a)<br>Jak konverzujete vy? Já se na tuto otázku bojím odpovědět :(

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
