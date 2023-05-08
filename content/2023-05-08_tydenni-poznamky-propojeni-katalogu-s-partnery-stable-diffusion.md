Title: Týdenní poznámky: Propojení katalogu s partnery, Stable Diffusion
Image: images/00009-457809728-4.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/201

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-04-28_tydenni-poznamky-clanek-o-ai-webexpo-a-katalog-kurzu.md) už utekl nějaký ten týden (28. 4. až 8. 5.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Cyklistky]({static}/images/00009-457809728-4.jpg)
Cyklistky, výsledek mého hraní si se Stable Diffusion. Nemají kolo, protože na tom si AI naprosto vyláme zuby.

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Glance Media](https://junior.guru/jobs/b5bb05d439c71b800ca520b63c5ae9ab261d10d19681ff2bc2acce0c/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Frontendová přednáška s Martinem Kolářem

V klubu proběhla přednáška od [Martina Koláře](https://martinkolar.eu/) o tom, jak si nastavit nový projekt.
Dalo nám práci najít termín, dokonce jsem to i posouval.
Promo na přednášku jsem pak dělal trochu na poslední chvíli, ale účast byla slušná.

Nic se nepokazilo a bylo to fajn.
Martin to měl jako trénink na nějaké konference, které bude objíždět, takže se snažil vlézt do půl hodiny.
Díky tomu byl velký prostor pro otázky a lidi měli dotazů spoustu, takže paráda.

![Martin Kolář]({static}/images/20230502-3f3aaec5b7c5e252772147bbd1c1050b64fc6e43ee24e27d09bc9fb8502270de-dc.png){: .img-thumbnail }

## Katalog kurzů: Zápasení s Peewee

Pokračoval jsem ve vylepšování katalogu kurzů, ale můj postup se výrazně zasekl při pokusu propojit dvě databázové tabulky.
Možná to bylo i tím, že když jsem se do toho pustil, měl jsem zrovna den s trochu rozstřeleným soustředěním, ale prostě jsem se do toho strašně zamotal a nemohl jsem uvěřit tomu, že něco takového řeším déle než hodinu.
Řešil jsem to nakonec několik dní.

Zjistil jsem, že když chci propojit databázovou entitu „poskytovatel kurzů“ s entitou „partnerská firma“ skrze 1:1 vztah, dostanu se s [Peewee](https://docs.peewee-orm.com/en/latest/) do zacyklujících se importů.
Vždy jsem vymyslel nějaký jiný způsob, jak to udělat, a vždy mě to zase hryzlo.
Zabil jsem různým refactoringem a drbáním na hlavě několik dní.
Ani AI mi nepomohlo.
Prohledával jsem řešení na internetu, ale bez úspěchu.
Našel jsem akorát několik issues přímo na Peewee repozitáři, kde se autor knihovny konzistentně a opakovaně [vyjadřuje v tom smyslu](https://github.com/coleifer/peewee/issues/1158), že tohle celé je tzv. „problém někoho jiného“ a ty, kdo to potřebují vyřešit, háže přes palubu:

> Your issue is a circular import. That's not really an issue peewee is designed to solve.
>
> — Charles Leifer

Týden se prostě nesl v duchu opraváře traktoru („kvůli jediné pi*ovince musíš rozebrat celý traktor“).
Bylo velice frustrující zjistit, že v SQLAlchemy by stejná věc byla [na pět minut a mají ji přímo v dokumentaci](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-one).
Došlo to tak daleko, že jsem dokonce zvažoval, kolik by reálně vzalo času celé junior.guru přepsat na SQLAlchemy.

Peewee jsem kdysi vybral proto, že to bylo malé sympatické ORM a na webísek se třemi stránkami jsem „žádný větší overkill nepotřeboval“.
Dnes bych se vytahal za uši.
SQLAlchemy je standard, který používají všichni, návodů je plný internet (tzn. napovídal by mi to GitHub Copilot), umí to všechno.

Každopádně nakonec jsem to nějak vyřešil přes cizí klíč, překopání návrhu modelů a iterace přímo v Pythonu místo toho, aby se určité věci děly přímo v SQL dotazech.
Efekt na výkon to má nulový, bavíme se o desítkách záznamů.
Možná jsem se měl zastavit už v začátku a udělat to nejrychlejší možnou cestou, byť ne teoreticky nejsprávnější, ale prostě mě zaskočilo, že ta nejsprávnější cesta je v mém ORM prakticky neuskutečnitelná a nemohl jsem tomu několik dní uvěřit.
Radost z toho celého nemám, ale je to vyřešeno a je na čase se posunout dál.

![Zvýrazněné firmy]({static}/images/screenshot-2023-05-05-at-20-05-15-kurzy-programovani.png){: .img-thumbnail }

Po týdnu snažení mám katalog, kde jsou partnerské firmy označeny a seřazeny jako první podle tarifu, který mají zaplacený.
Zaplacené kurzy mají odkaz bez _nofollow_.

## Relaxování se Stable Diffusion

Snažím se dodržovat státní svátky, takže včetně dneška mám dva dny volna navíc.
První prodloužený víkend jsme podnikali rodinné výlety, druhý víkend bylo horší počasí i zdraví, tak jsme byli spíš doma.
Sice se jela F1 v Baku a Miami, ale oboje byla strašlivá nuda.
Takže jsem relaxoval hlavně u Stable Diffusion.

![Klobouky]({static}/images/00009-457809728-2.jpg)
Holky v klobouku, výsledek mého hraní si se Stable Diffusion.

Jede mi to hodně pomalu, takže vždy zadám nějaké vstupy, spustím to a jdu něco dělat.
Pak se vrátím a podívám se, co tam na mě vyjelo za překvapení.

![Žehličky]({static}/images/00009-457809728.jpg)
Se ženou jsme zkoušeli generovat chlapa v havajské košili, který žehlí. AI má zjevně s žehličkami problém a dost jsme se u toho nasmáli.

Pokoušel jsem se vyřešit tu rychlost, ale je to zapeklité.
Na M1 MacBooku to jede, ale nedokáže to využít celý potenciál jeho HW.
Navíc je potřeba strašně moc RAM a já mám jen 8 GB.
Protože M1 strašně rychle a efektivně swapuje na strašně rychlý disk, můj běžný provoz málo paměti vůbec neomezuje a vše je velmi rychlé, ale na Stable Diffusion tenhle trik neplatí.

![Star Wars]({static}/images/00009-457809728-1.jpg)
Moje pokusy vygenerovat něco jako Star Wars bojovnici, která běží džunglí.

### InvokeAI

Nejdřív jsem si dělal naději, že by mohlo pomoci [InvokeAI](https://invoke-ai.github.io/InvokeAI/), které navíc na videích vypadá fakt dobře.
Instaloval jsem to půl dne, nastahoval gigabajty dat, ale nakonec jsem s tím nic nevyprodukoval.
Cokoliv jsem zkusil, napsalo mi to akorát, že mi vytekla aplikační paměť a mohl jsem akorát restartovat celý MacBook.
Tohle se mi s [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) ani [DiffusionBee](https://diffusionbee.com/) nikdy nestalo.

### CoreML

Všiml jsem si, že [existují způsoby](https://twitter.com/pcuenq/status/1620080393226706945), jak využít plný výkon M1.
Jmenuje se to CoreML a využívá to čip, který má M1 přímo na výpočet věcí kolem machine learningu.

Zkusil jsem [Diffusers](https://github.com/huggingface/swift-coreml-diffusers), ale nejdou tam dát vlastní modely a výsledky byly rychlé, nicméně mizerné.
Když jsem pátral dál, našel jsem [MochiDiffusion](https://github.com/godly-devotion/MochiDiffusion), appku, která je někde mezi DiffusionBee (skoro tak dobrá) a tím Diffusers (využívá CoreML).
Podporuje vlastní modely, ale aby šlo použít CoreML, je potřeba je konvertovat do Applího formátu.
Na to jsou nějaké skripty, což vyžaduje nějakou znalost Pythonu, je potřeba mít nainstalované Xcode, což vyžaduje stáhnout další gigabajty na disk, a ještě to trvá strašně dlouho.
Šťoural jsem do toho víc a víc a pochopil jsem, že CoreML jde pouštět i přímo z příkazové řádky.
Dost mi pomohl návod [Fast Stable Diffusion using Core ML on M1](https://mybyways.com/blog/fast-stable-diffusion-using-core-ml-on-m1) od C. Y. Wonga.

Povedlo se mi to rozběhat!
Vytváření obrázků bylo fakt rychlé a šlo použít vlastní model.
Jenže výsledky opět mizerné, až bych řekl směšné.
Lze použít jen velmi krátký prompt a jen jedno rozlišení, nelze nastavit sampler.
Oproti tomu, co umí AUTOMATIC1111, je to jako se z moderní doby vrátit někam k otesávání pazourků.

Své zkušenosti jsem popsal [do issue na repozitáři DiffusionBee](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/issues/416#issuecomment-1532359672), které jsem původně založil, abych autory namotivoval tuhle technologii přímo zahrnout do jejich appky.
Většina omezení plyne přímo z toho, co (ne)podporuje samotné CoreML od Applu, takže je nikdo hned tak nevyřeší.
Tím jsem uzavřel své pátrání co se týče rychlejšího výkonu a smířil se s tím, že jestli chci kvalitu a nejrůznější triky, musím se smířit s rychlostí a možnostmi, jaké nabízí AUTOMATIC1111.
Na M1 je to v současnosti nejfunkčnější řešení.

### PyTorch v2

Nakonec jediné zrychlení, které se mi povedlo dosáhnout, měl na svědomí samotný AUTOMATIC1111.
Vydal novou verzi, kde se používá PyTorch v2 a je to u mě znatelně rychlejší!
Stačilo udělat `git pull` a aktualizovat závislosti.
A [vyřešit jeden zásek v tom](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/10096#discussion-5161302), že původní nastavení výkonu se muselo smazat.

### Vychytávky

-   [Liner](https://liner.ai/), appka na trénování vlastních modelů.
    Nezkoušel jsem zatím.
-   Zajímavá galerie pro inspiraci: [joelparkerhenderson/stable-diffusion-image-prompt-gallery](https://github.com/joelparkerhenderson/stable-diffusion-image-prompt-gallery/tree/main)
-   Napsal jsem si krátký Python skript, který mi monitoruje složku, kam se generují obrázky, a pošle mi nové obrázky na Telegram.
    Můžu tedy nastavit generování hromady obrázků, nechat to běžet, jít třeba ven a v pauzách se na mobilu těšit z toho, co to generuje.
    Většinu toho skriptu mi pomohl napsat GitHub Copilot.
-   Naučil jsem se [dynamic prompts](https://www.youtube.com/watch?v=bQK5diN59NA) a je to super.

### Co neumím

Zatím jsem si hrál pouze s tzv. txt2img, protože je to nejrychlejší.
Zároveň je to ale dost omezené co se týče toho, co jde vygenerovat.
V podstatě všechny osoby akorát pózují jak na instáči.

![Pózičky]({static}/images/00009-457809728-3.jpg)
Vygenerovat holku, která drží zmrzlinu, nebo si ji třeba kupuje, je problém. Holky sedící ve vlaku se mi dařily víc, ale polovina z nich sedí bokem jako v metru.

Různými triky jde dosáhnout toho, že generované osoby mají relativně normální ruce, správný počet rukou, nebo celkem pěkný obličej.
Udělat ale cokoliv navíc, třeba dát jim do ruky zmrzlinu, mobil, žehličku, knížku, nebo kolo, je nadlidský úkol.
Zkoušel jsem se [ptát na Redditu](https://www.reddit.com/r/StableDiffusion/comments/138frrr/tips_on_prompting_other_than_pinup_or_portrait/) a odpověď je, že mám používat img2img a control nets.
[Tenhle návod](https://www.youtube.com/watch?v=zmobGnOjnAE) ukazuje, co vše s tím jde dělat.
Takže budu teď asi zkoušet tohle.
Při psaní poznámek jsem zkusil první obrázek a trvalo to věčnost, ale vypadá to celkem slibně.
Na první pokus jsem takový úspěch rozhodně nečekal!

![Elfka]({static}/images/screenshot-2023-05-08-at-13-23-25-stable-diffusion.png){: .img-thumbnail }
Z lučištnice Elfka pomocí img2img.

## Heroes na macOS přes Porting Kit

Díky náhodnému čtení Redditu jsem narazil na [komentář, který zmiňuje Porting Kit](https://www.reddit.com/r/macgaming/comments/1325he7/comment/ji407pn/?context=3).
Myslel jsem, že znám už snad všechny způsoby, jak se dají na macOS rozběhat staré Windows hry, ale zjevně ne.
O Porting Kitu jsem doteď neslyšel!

Žena si už několikrát posteskla, že na macOS nejedou Heroes of Might and Magic, které má celý život moc ráda.
Tak jsem zkusil ten Porting Kit a ono to fakt funguje!
Hru jsme koupili přes GOG, nainstalovali přes Porting Kit podle jejich návodu, a hotovo.

Ne že bychom měli při výchově malého dítěte na cokoliv moc čas, ale když už se někde půlhodina najde, je dobré, pokud máme každý nějakou možnost relaxovat.
Tohle je nová pecka v repertoáru manželky a mám velkou radost z toho, že se to povedlo rozjet.

Bohužel moje vysněná hra nejede ani přes tenhle Porting Kit.
Zkoušel jsem to a smůla.
Jak na macOS, navíc Apple Siliconu, bez Windows rozběhat [Original War](https://www.gog.com/en/game/original_war), to zůstává nedořešenou otázkou století.

## Další

-   Do Prahy se stavil kamarád z Indie, resp. nyní z Londýna, a jeden večer jsme propařili.
-   Sešel jsem se s Martinem Kavkou a dlouho jsme si povídali.
    Brzo někde něco vyjde!
    Sledujte [newslettery.cz](http://newslettery.cz) a [Tvůrcast](http://tvurcast.cz)!
-   Psal jsem autorům filmu [Nová šichta](https://dafilms.cz/film/12793-nova-sichta), zda si ho můžeme nějak pustit společně online v klubu.
-   Dělali jsme spolu s Red Hatem v klubu anketu, která zjišťovala mezi juniory zájem o part time a důvody.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
    V klubu byl fakt velký provoz, takže jsem strávil hodně hodin jen čtením a odpovídáním.
-   Zaregistroval jsem se do nějakého nového Strava Developer programu.
    Mám obavu, že můj skript na analýzu kolik jsem toho naběhal a najezdil na kole za poslední týden, nevyhodnotí jako něco, co je pro ně zajímavé, nebo co [dodržuje jejich branding guidelines](https://developers.strava.com/guidelines/), a zaříznou mě.
    [Přidal jsem si do README jejich logo](https://github.com/honzajavorek/honzajavorek.cz#-weeknotes), bude to stačit? 😅
-   Během 11 dní jsem ujel na kole 36 km. Celkem jsem se hýbal 6 h a zdolal při tom 36 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Napsat čtyřem firmám, kterým bude končit partnerství s klubem.
2.  Propojit výpis kurzů s podstránkami, zvýraznit partnery na podstránkách.
3.  Vymyslet speciální ceník pro vzdělávací agentury.

Hned zítra jdu na jeden ranní event a taky bych neměl zanedbávat administrativu a čtení klubu.
No, bude toho zase nějak hodně.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Jak se ničí novináři](https://mimo-agendu.ghost.io/r/d3ffb1ed?m=66ba468d-5bc9-4c14-bd0c-21f5c52e7ed0)<br>„Říct, že novinářka a moderátorka Linda Bartošová ‚odešla‘ z Twitteru, by bylo v lecčem nepřesné. Linda totiž neodešla. Lindu z této sociální sítě vyštvaly dlouhodobě nenávistné, toxické a útočné reakce, které by se bez nadsázky daly označit za kyberšikanu.“ „Byl jsem svědkem situací, kdy se novináři po takové kampani zhroutili či skončili na antidepresivech. Faktem je, že neexistuje způsob, jak říct dost. S útočníky se nedá domluvit. Jde jen doufat, že si brzy najdou nový terč, vydržet to, nebo se stáhnout z veřejného prostoru.“
- [„Svou obec si zastaví a k nám se chodí rekreovat.“ Únětice trápí nával turistů a nedostatek peněz - VOXPOT](https://www.voxpot.cz/svou-obec-si-zastavi-a-k-nam-se-chodi-rekreovat-unetice-trapi-naval-turistu-a-nedostatek-penez/)<br>„Největší rozdíly mezi lidmi nejsou v tom, kdy a kde se kdo narodil nebo co dělá. Ale v tom, že někoho prostě vůbec nezajímá, co se děje za jeho plotem. Vysadí si vysoké túje a za nimi je schovaný. A někdo to má úplně naopak. Ne proto, že by se chtěl nějak obětovat, ale prostě ho to zajímá. Naplňuje ho, když kolem sebe vidí pěkné věci. A ty, které pěkné nejsou, chce samozřejmě změnit.“
- [Vztah není švýcarák pro život – nevyřeší vše. O singles s poradenským psychologem Jiřím Procházkou — Balanc](https://www.mujrozhlas.cz/rapi/view/episode/8e596841-4b25-351a-b975-4a5f5159fc43)<br>Dobrý postřeh s tím, že člověk by měl mít hlavně rád sebe a být v pohodě sám (se sebou). A do toho teprv míchat vztah s někým.
- [Martin Reiner: O strašlivé gentrifikaci brněnského Bronxu I. Literární reportáž z cyklu České bolesti - Novinky](https://www.novinky.cz/clanek/kultura-salon-martin-reiner-o-straslive-gentrifikaci-brnenskeho-bronxu-i-literarni-reportaz-z-cyklu-ceske-bolesti-40406158)<br>Dva díly zajímavého pojednání o gentrifikaci brněnského Bronxu. „Chceme být fér? Pak je naší povinností říct, že ten Bronx, co dnes Bára Bažantová a někteří další hájí před gentrifikací, je Bronxem, jenž právě skrze gentrifikaci, která začala před patnácti lety, dospěl k vysoké formě integrace.“
- [Mojo Lang… a fast futuristic Python alternative](https://www.youtube.com/watch?v=V4gGJ7XXlC0)<br>Dost dobrý!
- [Stanislav Biler: Brno, hřbitov veřejného prostoru. Literární reportáž z cyklu České bolesti - Novinky](https://www.novinky.cz/clanek/kultura-salon-stanislav-biler-brno-hrbitov-verejneho-prostoru-literarni-reportaz-z-cyklu-ceske-bolesti-40409035)<br>„Snižte svou perspektivu do výše očí dětí a náhle přestanete přes hradby aut vidět. Svět zmizí a veškerý výhled zablokují kapoty. Ze světa se stane obludné místo.“
- [Za prodej osobních údajů dostal český Avast rekordní pokutu 350 milionů korun](https://www.seznamzpravy.cz/clanek/ekonomika-za-prodej-osobnich-udaju-dostal-cesky-avast-rekordni-pokutu-350-milionu-korun-229885)<br>Asi by nemělo zapadnout, jak se ke svým uživatelům choval Avast. Kam se ve sledování a prodávání dat hrabou žabaři jako Facebook a spol.
