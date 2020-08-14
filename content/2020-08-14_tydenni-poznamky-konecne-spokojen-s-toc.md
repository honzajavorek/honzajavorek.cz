Title: Týdenní poznámky: Konečně spokojen s ToC
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs


Utekl další týden (10.8. — 14.8.) a tak [stejně jako minule]({filename}/2020-08-10_tydenni-poznamky-css-pro-prirucku.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Aktuální strategie

Srpen mám nabitý různými prodlouženými víkendy a dovolenými, ale tento týden jsem mohl celkem nerušeně věnovat práci. I proto se trochu rozepíšu o dlouhodobější strategii, kterou teď mám.

### Léto

Po koronaviru má hodně větších firem z opatrnosti stále _hiring freeze_ a i pokud nemají, mají různá jiná omezení, která ústí v to, že nemají chuť najímat juniory. Proto dost spadl počet nabídek práce na JG poté, když staré inzeráty expirovaly a v důsledku působí [stránka s nabídkami](https://junior.guru/jobs/) dost neutěšeně. Během druhé půlky července a dále srpna jsem navíc viděl velký pokles zájmu tak nějak o všechno. Léto se naplno projevilo a kdo na jeho začátku váhal, jestli někam vyjet, tak váhat přestal a vyjel.

V souvislosti s tím jsem si řekl, že posunu vydání [příručky](https://junior.guru/candidate-handbook/) na 1.9. a nebudu do té doby dělat žádný velký marketing ani sales. Místo toho se soustředím na programování: Připravuji příručku na její vydání a pak bych chtěl zapracovat na té stránce s inzeráty.

### Co chci dokončit

Příprava příručky musí skončit zhruba týden před koncem srpna, abych ji mohl rozeslat lidem z [newsletteru](http://eepurl.com/gyG8Bb) dřív, než oficiálně vyjde. Tento týden jsem do toho trochu šlápl, takže je to na dobré cestě, ač tedy příští týden mám trochu volna a trochu rodinných událostí a nevím, nakolik budu zvládat dodělat poslední kousky.

Na stránce s nabídkami práce musím hlavně spojit nabídky z JG a [nabídky z robota](https://junior.guru/jobs/), a ty z JG nějak zvýraznit. Potom chci dodělat filtr na město a mít pro každé město stránku zvlášť, např. juniorní nabídky v Praze, juniorní nabídky v Brně, atd. To by, myslím si, mohlo pomoct jak uživatelům v orientaci v inzerátech, tak SEO. Vrátit bych se měl i k samotnému robotovi a opravit v něm chybky.

### Co dál?

Jak budou tyto dvě věci hotové, tzn. asi někdy v září, nejspíš přestanu úplně programovat. JG bude v podobě, v jaké už prostě musí začít fungovat a něco vydělávat. Začnu se prakticky plně soustředit na marketing a sales, udělám si základní propočty příjmy/výdaje, a uvidím, kam až se dostanu s návštěvností a jestli začnou firmy inzerovat nebo mi více lidí [přispěje](https://junior.guru/donate/), tzn. zaplatí za příručku z pozice čtenáře. Těžko se srovnávat třeba s Ondřejem ([GitHub Sponsors](https://github.com/sponsors/ondrejmirtes/), [Patreon](https://www.patreon.com/phpstan)), který má [celosvětově užitečný projekt](https://github.com/phpstan/phpstan), ale zase proč to nezkusit. Nevím, kde má můj počet přispěvatelů strop a třeba to nakonec může fungovat lépe, než platby za nabídky práce :D


## Table of Contents

Tento týden byl ve znamení tvorby _Table of Contents_ pro příručku. Sice by se zdálo, že z minulého týdne už to bylo skoro vyřešené, ale když jsem pak zkusil do onoho řešení obléct ToC příručky, která je fakt dlouhá, prasklo to ve švech a bylo jasné, že ve skutečnosti řešení nemám. Bylo to celkem frustrující. Taková blbost a já se s tím mažu už pár týdnů (ano, prošpikovaných dovolenýma, ale stejně).

### Jak to začalo

Původní problém, který jsem se snažil vyřešit, byl orientace čtenáře v příručce, protože si na to víc lidí stěžovalo. Dalo se to vyřešit různě:

- Přepsat příručku z HTML třeba do Markdownu a použít hotové řešení, udělat něco jako [docs.pyvec.org](https://docs.pyvec.org/) nebo [cojeapi.cz](https://cojeapi.cz/) a třeba to jen vhodně integrovat a zasadit do JG designu.
- Rozsekat příručku na více stránek, přidat nějaké menu a nechat navigaci na starých dobrých technologiích, jako jsou HTML a HTTP.
- Nechat příručku na jedné stránce (dlouhé nudli), přidat nějaké menu a okořenit to trochou JavaScriptu, aby se podle scrollování ukazovalo, kde člověk zrovna je.

Vybral jsem si poslední možnost, přišla mi nejjednodušší. Původně jsem myslel, že rozšířím stránku a ToC tam prostě napíšu a jen napozicuju vedle textu. Jenže jsem se vydal na nějakou slepou uličku co se týče designu a technického zpracování a dospěl jsem k nějakému otevírátku a kdo ví čemu.

Verze z minulého týdne skončila na tom, že když byla ToC delší než výška obrazovky, neexistovalo na to žádné řešení. Tak jsem to zkusil upravit tak, aby se ToC otevírala jako výsuvný panel z boku celé stránky, což by celkem mohlo fungovat jak na počítači, tak na mobilu.

### Obluda

Když to bylo hotové, vypadalo to strašně, neukazovalo to hned člověku kde je - musel něco rozkliknout, rozklikávátko nešlo dobře na stránce vidět, na mobilu to nenavigovalo dobře, neobarvovalo se jako aktivní co se obarvovat mělo a celé to při manipulaci problikávalo. K tomu všemu byla každá další věc neočekávanou komplikací - třeba přidání podnadpisů. S vysouvací ToC taky začalo dělat dost problém schovávání hlavičky, když se scrollovalo dolů, takže jsem ho zrušil. Jenže byla pak velká, takže jsem vynalezl důmyslný systém animovaného zmenšování hlavičky při pohybu na stránce. Prostě, z jednoduché ToC vylezla komplexní, nefunkční, animovaná obluda. Měl jsem tam i [pulsující](https://reactgo.com/css-pulse-animation/) šipku, která upozorňovala na tlačítko pro rozkliknutí obsahu, LOL! (Ale teď aspoň umím v CSS pulsovat, heč!)

Po úterku, kdy jsem to dodělal a koukal na výsledek, se mi chtělo JG smazat a vrátit se do Oraclu, ale udržel jsem emoce, zavřel počítač a nechal si to projít hlavou do druhého dne :D

![Obluda]({static}/images/obluda.png)
Obluda

### Krása v jednoduchosti

Ve středu jsem vymyslel statičtější a jednodušší přístup k ToC. Dokonce jsem zvažoval stránku rozsekat na několik podstránek. Obludu jsem smazal a vrátil se k původní myšlence: Obsah odsadit a ToC zobrazit vedle něj. Oproti předchozím pokusům se mi povedlo celkem rychle vymyslet, jak to udělat, a ToC jsem napozicoval doleva, což mi vizuálně hned sedlo, oproti všem předchozím pokusům ji mít vpravo. Celé to začalo nějak fungovat a dobře vypadat a já se zaradoval, že to konečně mám. Později jsem už jen dodělal detaily jako mizení ToC když člověk odscrolluje úplně dolů nebo zobrazování aktuálního nadpisu. Minimum JS, vše důležité se řeší v CSS. Příště si musím hned uvědomit, že když mám více jak 20 řádků JS, tak to je slepá ulička a ne způsob, jakým chci JG tvořit.

Zkoušel jsem si sice hrát chvíli s [History.pushState()](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState) (aby se při scrollování měnila adresa v prohlížeči), ale hned jsem viděl, že to šťourá do přirozeného chování browseru a musel bych ošetřovat všelijaké speciální případy, takže jsem se na to vykašlal.

Zmenšování nebo schovávání hlavičky jsem nakonec úplně vyhodil. Verze pro mobil se nakonec nějak vyloupla sama. Lištu pod hlavičkou, která ukazuje aktuální nadpis, jsem zachoval jen pro mobil, a když už tam bylo to tlačítko na otevírání obsahu, jen jsem jej předělal na odkaz a ten čtenáře pošle na ToC tak jak je na stránce. ToC na mobilu není nijak pozicovaná, je prostě na začátku dokumentu v rámci jeho flow. A přijde mi, že to funguje překvapivě dobře. A tak jednoduché to bylo!

A hotovo. Vyřešil jsem akorát ještě bug, že se špatně detekoval aktuální nadpis v případě "schovaných" sekcí (např. [Co způsobí koronavirus?](https://junior.guru/learn/#covid19)) s podnadpisy. Nepřišel jsem úplně na příčinu, ale když jsem schované podnadpisy vyhodil z detekce aktuální pozice, tak to přestalo zlobit.

### JG roste do šířky

No a nakonec jsem JG odladil pro větší displeje, než mám já. Pracuji na 12" s 2304x1440 retina (takže 1280x800), ale hodně lidí má větší displej a na nich asi vypadalo JG dost jako nudle uprostřed obrazovky. Do teď jsem to nějak neměl chuť řešit, ale s ToC na boku se už hodilo přidat do stran místo. V Google Analytics jsem zjistil, že nejčastější rozlišení návštěvníků jsou 1920x1080 a 1536x864. Toto jsem si přidal do [Responsive Design Mode ve Firefoxu](https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode), připojil externí širokoúhlý monitor co máme na filmy, a tam poladil ideální maximální šířku stránky.


## Další poznámky

Teď už jen vymyslet zobrazování log sponzorů a příručka bude připravená. A i ta loga už mám trochu rozdělaná a myslím, že je to na dobré cestě. Co jsem ještě stihl kromě ToC?

- Udělal jsem něco málo na [docs.pyvec.org](https://docs.pyvec.org/)
- Jedna mentoring session
- Napsal jsem [skript](https://github.com/honzajavorek/junior.guru/blob/09eab071caeaefe3acb62dace6d3ffe7207af9af/scripts/generate_toc.py), který vezme HTML šablonu, zparsuje ji jako HTML, najde v ní nadpisy a vygeneruje HTML s ToC. Tu následně prostě copy-paste dám do oné šablony. Asi by se to mohlo generovat nějak dynamicky, ale přišlo mi, že tohle je dostatečné quick & dirty řešení pro to, jak mám ty šablony a obsah teď udělané (vše je v HTML). Aby se mi to nerozsynchronizovalo, napsal jsem i [kontrolní test](https://github.com/honzajavorek/junior.guru/blob/09eab071caeaefe3acb62dace6d3ffe7207af9af/tests/test_toc.py).
- Pulsovací animaci jsem nakonec využil! Když se přesunu na nějaký nadpis, tak se skrze pulsující animaci mírně zvýrazní.
- Zjistil jsem, že existuje [vh](https://css-tricks.com/fun-viewport-units/) :D Užitečné, spoustu věcí to usnadňuje! Škoda, že jsem o tom nevěděl od začátku, co dělám JG.
- Dolaďoval jsem "předmluvu" příručky.
- Na [tip od Simona Willisona](https://twitter.com/simonw/status/1279212166571159552) jsem zkusil editor [Figma](https://www.figma.com/), abych upravil SVG pro ikonu ToC tlačítka. Spokojenost! Pro nějakou občasnou editaci vektorových věcí to vypadá o dost líp než Inkscape na macOS nebo cokoliv podobného.
- Dostal jsem nabídku, že by kamarád na svých webech _pro bono_ zobrazil reklamní banner JG. Slíbil jsem, že ho připravím, ale tento týden jsem to nestihl. JG bude mít první opravdovou reklamu! :)


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Česko je gerontokracie. Všichni jsou relikty devadesátých let, mladí nemají šanci](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.info.cz%2Fpodcasty%2Finsider-podcast%2Frychlikova-durcak&h=f17366ff095d81779650db4ab3f00a03f8ec43d376351a677ac6582b6765a692)<br>Málokdy se stane, že v jednom studiu sedí tak pestrá sestava. Místy se překřikovali jak andulky a skoro to nešlo vydržet, ale bavilo mě to.
- [How Racism Shapes My Habits](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.jowanza.com%2Fblog%2F2020%2F6%2F1%2Fhow-racism-shapes-my-habits&h=f722aa7606ecc57083ff30642ed3ba315e02f5679858c39b3de86a3e948fb36b)<br>Můžete mít VŠ titul a stejně v USA zažívate denně tisíc drobných projevů rasismu, které formují a omezují vaše každodenní chování
- [Hybaj do polí](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fbydleni%2F419465-hybaj-do-poli&h=2b06bb32ab311d89b67afce242981dd910ac0f9fe63b2e59651740bec90c8c1b)<br>“Monofunkční budovy na nevhodných místech vytvářejí příliš velké vzdálenosti pro vznik hodnotných celků i v prosperujících oblastech, drancují krajinu a nechávají lidi zcela odkázané na dojíždění autem do blízkého města, kde doprava přespolních ničí to, co je na něm hezké, a v obyvatelích vzbuzuje pocit, že by měli větší klid za městem… v monofunkčních budovách na nevhodných místech.”
- [Masová vražda v Bohumíně. Ale co když „to byli cikáni“?](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2020%2F08%2Fmasova-vrazda-v-bohumine-ale-co-kdyz-to-byli-cikani%2F&h=2e6016e33507485e56c876459bfc749340236559fd321e31813483af2e09f68d)<br>"V Bohumíně došlo k největší masové vraždě od roku 1989. Politické ani mediální reakce však závažnosti situace neodpovídají."
- [J.K. Rowling and the Limits of Imagination ❧ Current Affairs](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.currentaffairs.org%2F2020%2F07%2Fjk-rowling-and-the-limits-of-imagination&h=d3ac7d69f6857c5c9e7cb4da5b41169708fc3e88b6beaf83413a0618f683f936)<br>Dlouhý rozbor díla a osoby JK Rowling, která se pro mnohé stala tím, čím u nás Nohavica — morálním selháním.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
