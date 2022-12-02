Title: Změny na blogu
Image: images/imattsmart-sm0bkoj5bna-unsplash.jpg
Lang: cs


Je to skoro dva roky od chvíle, kdy jsem naposledy předělával svou osobní stránku a blog. Většinou když to dělám, tak píšu článek o tom, co jsem změnil a proč. [Udělal jsem to minule]({filename}2019-12-31_reviving-my-blog.md) a dělám to i teď.

![Kladivo a klíč]({static}/images/imattsmart-sm0bkoj5bna-unsplash.jpg)
Fotka od [iMattSmart](https://unsplash.com/@imattsmart)

## Všechno česky!

Kdybych se snažil prorazit na celosvětovém trhu, asi by mělo smysl blog postupně posouvat blíž a blíž k angličtině jako k hlavnímu jazyku. Moje podnikání je ale pouze pro ty, kdo rozumí česky, a tak sem každý týden píšu v češtině týdenní poznámky, které nyní tvoří většinu obsahu zde vydaného.

Celkem je tady přes 500 článků a anglicky je jich 16. I většina všeho ostatního, co kde dělám, je v češtině, např. vystupování v podcastech nebo publikování v médiích. Moje publikum je prostě české, případně slovenské.

Velkou změnou na blogu je tedy rezignace na angličtinu jako výchozí jazyk. Neříkám, že občas nenapíšu anglický článek, ale výchozím jazykem bude čeština. Moje osobní stránka bude česky a úvodní stránka blogu taky.

Minule jsem psal o tom, že tradiční název blogu, **Javorové lístky**, zahazuji, a bude to prostě **HJ's blog**. Tak teď se zase vracím k tradici! Javorové lístky jsou zpět :)

## Úspěchy a největší pecky

Na své osobní stránce i na hlavní stránce blogu jsem vypíchl nějaké hlavní věci, o které by se lidi měli zajímat, když sem přijdou. Na mé osobní stránce je takhle několik mých kariérních milníků a úspěchů.

![Moje úspěchy]({static}/images/screenshot-2022-12-01-at-20.42.16.png){: .img-thumbnail }

Je tady archiv všech článků, ale tím se asi nikdo probírat nebude. Označil jsem si tedy interně některé články jako „největší pecky“, jejichž seznam je hned nahoře.

![Největší pecky]({static}/images/screenshot-2022-12-01-at-20.41.17.png){: .img-thumbnail }

## Sociální sítě a další profily

Na úvodní stránce webu jsem dal v záhlaví odkazy na pár míst, kde mě lidi mohou najít, ale dost jsem to osekal. Mám v plánu se totiž trochu stáhnout z některých sociálních sítí. Profily si nebudu rušit, protože se mi mohou občas hodit, ať už pro přístup k informacím, nebo pro občasnou propagaci svého podnikání.

O tom, kde hodlám být aktivní, a kde ne, jsem se pak rozepsal ve speciálním odstavci. Jestli to tak budu opravdu dodržovat, to je samozřejmě zatím ve hvězdách :)

![Moje další profily]({static}/images/screenshot-2022-12-01-at-20.49.57.png){: .img-thumbnail }

## Spolupráce

Napadlo mě, že bych mohl mít na webu přímo sekci, která vysvětluje můj aktuální přístup k nejrůznějším aktivitám, se kterými mě lidi sem tam oslovují. Cílem je, aby to některé odradilo a některé třeba zase povzbudilo.

![Možnosti spolupráce]({static}/images/screenshot-2022-12-01-at-21-03-20.png){: .img-thumbnail }

## Srdceryvný příběh

Úvodní stránka blogu nyní začíná dlouhým textem, který popisuje jeho historii. U nikoho jiného jsem nic takového neviděl. Původně jsem chtěl napsat dvě věty, ale nějak mi to přerostlo v delší text. Nakonec se mi to ale zalíbilo. Blog s patnáctiletou historií si pěkný úvod prostě zaslouží. Zkracovat to nebudu.

Lidi se většinou přes sdílené odkazy dostanou na konkrétní články. Na hlavní stránku blogu podle mě moc nechodí. Když už tam zabloudí, nejspíš je zajímá, kde se ocitli, a budou mít možná chuť si o tom trochu přečíst.

![Úvodní stránka blogu]({static}/images/screenshot-2022-12-01-at-21-04-10.png){: .img-thumbnail }

V minulém designu blogu byl odkaz na hlavní stránku blogu hodně potlačen. Teď jsem jej dal viditelně doprava nahoru, tak třeba tam zabloudí lidí víc.

![Odkaz na blog]({static}/images/screenshot-2022-12-01-at-21-05-09.png){: .img-thumbnail }

## Čas čtení

Stává se mi, že napíšu článek a je strašně dlouhý. Někdy to za to stojí, někdy ne. Například nemá smysl, aby čtení mých týdenních poznámek někomu zabralo 20 minut. Nehledě na to, že jejich psaní mi pak zabere půl dne.

Abych měl trochu představu, zda jsem to s psaním nepřehnal, obohatil jsem svůj [Pelican](https://getpelican.com/) o plugin, který pro každý článek vypočítá čas čtení. Ten se pak zobrazuje v záhlaví každého článku.

```python
WORDS_PER_MINUTE = 200
words_count = len(re.split(r'\s+', article_text))
readtime = math.ceil(words_count / WORDS_PER_MINUTE)
```

Pomohl mi [tento článek](https://www.craigabbott.co.uk/blog/how-to-calculate-reading-time-like-medium). Testoval jsem to a přijde mi, že minimálně mojí rychlosti čtení to zhruba odpovídá.

## Návštěvnost

Do záhlaví každého článku jsem přidal také odkaz na grafy s návštěvností, které mám už nějakou dobu veřejně na [Simple Analytics](https://referral.simpleanalytics.com/honza-javorek). Odkaz se generuje tak, aby zobrazil návštěvnost pro tu konkrétní stránku na mém blogu, od data vydání článku.

![Návštěvnost článku Volím marketing]({static}/images/screenshot-2022-12-01-at-21-13-53-simple-analytics-the-privacy-first-google-analytics-alternative.png)

Návštěvnost moc nesleduju, ale někdy mě zajímá u konkrétních článků. Vyfiltrovat si je rucně v Simple Analytics byla trochu pruda. Tak třeba když teď budu mít odkaz, tak se na to budu dívat častěji.

## Telegram místo Pocketu a sociálních sítí

Jsem aktuálně uprostřed něčeho jako digitálního úklidu. Zamýšlím se nad tím, které sociální sítě už mi přijdou tak toxické a neužitečné, že je opustím. Vyčistil jsem si seznam podcastů nebo subredditů, které chci sledovat. Čtu [Four Thousand Weeks](https://www.oliverburkeman.com/books) a přemýšlím, jak moc věcí v mém životě jsou nekonečné seznamy „úkolů“ a zda s tím mohu něco udělat.

Jedna z prvních věcí, kterou jsem se rozhodl „zabít“, je [Pocket](https://getpocket.com/). Nainstaloval jsem si místo toho [RSS čtečku](https://nnw.ranchero.com/), kam jsem si dal některé oblíbené zdroje. Když narazím na náhodné články, které mi přijdou zajímavé, čtu si je jednoduše v prohlížeči. Využívám při tom _Reader View_ ve Firefoxu nebo v Safari, které mi čtení zpříjemňuje. A když si článek přečíst nezvládnu, zapadne prostě v mých tabech v prohlížeči a možná ho pak jen zavřu. A bude mi to jedno. Aspoň tak si myslím, že by to teď mohlo fungovat.

Jenže co s funkcí sdílení zajímavých článků? Upřímně, některé věci jsem stejně do Pocketu posílal jen uměle, abych je pak mohl vysdílet a objevily se v poznámkách. Například podcasty. Stačilo by mi něco, kam prostě hodím odkaz, když mě zaujme, a potom ty odkazy nějak automaticky sesbírám při psaní týdenních poznámek.

Sledoval jsem chvíli na Telegramu kanál [Filipa Horkého](https://t.me/FilipHorky) (na který jsem narazil na Discordu projektu [Mimo agendu](https://mimo-agendu.ghost.io/)) a přišlo mi, že by to mohlo být celkem zajímavé řešení. Založil jsem si tedy [Honza Javorek sdílí](https://t.me/honzajavorekcz) a zatím se mi to líbí. Pro mě je to takhle navíc pohodlné, protože Telegram používám denně. Mám tam nejvíc kontaktů mezi přáteli i rodinou.

![Kanál na Telegramu]({static}/images/screenshot-2022-12-01-at-22-24-53.png)

Napsal jsem si skript, který nové články na blogu přes GitHub Actions automaticky hodí do toho mého kanálu. Toto třeba s osobním Facebookovým profilem vůbec nejde a musel jsem tam odkazy dávat vždy ručně.

Nakonec jsem obohatil skript, který mi připravuje šablonu článku pro týdenní poznámky, aby se na ten kanál podíval, co jsem od minule sdílel, a vložil odkazy do patičky poznámek. Stejně, jako to dřív bylo s Pocketem. Hotovo :)

Pocket má mimochodem vtipný [export dat](https://getpocket.com/export). Vyjede prostě jeden dlouhý HTML soubor s odkazy na věci, které jste si uložili.

## Komentáře

Lidi si občas stěžovali, že nemám na blogu komentáře. Myslel jsem, že budu prostě dostávat reakce na sociálních sítích a přímo tady nic být nemusí. Ale jak se chci ze sítí stáhnout a být na nich méně závislý, hledal jsem, zda by nemohlo existovat nějaké jiné řešení. Třeba aspoň něco, co by využívalo věci, které používat chci. Telegram, Discord.

A zjistil jsem, že Telegramové kanály umožňují mít pod každou zprávou i komentáře. Tak jsem to zapnul. A pak přišel velký objev. Tyhle komentáře jde i přímo vložit na web! Propojil jsem to tedy s blogem úplně a pod článkem teď bude mít každý článek brzy po svém publikování tlačítko, které Telegramové komentáře načte. Kdo má účet na Telegramu, může je tam dokonce rovnou i psát. Kdo nechce psát, může dávat aspoň palce nahoru a jiné reakce.

![Komentáře na Telegramu]({static}/images/screenshot-2022-12-01-at-22-31-15.png)

Nechtěl jsem, aby se komentáře načítaly automaticky, protože je to externí služba (pomalu se to načítá, nezapadá to do designu webu, může to sledovat uživatele), takže je to na tlačítko. Vyžádalo si to zhruba 12 řádků JavaScriptu a je to jediný JavaScript, který na tomto webu teď mám.

![Komentáře na webu]({static}/images/screenshot-2022-12-01-at-22-32-16.png){: .img-thumbnail }

## Další články

Sice jsem přidal odkaz na úvodní stránku blogu do hlavičky každého článku, ale přišlo mi to nějak málo. Pod každý článek jsem tedy dal sekci s odkazy na další moje články. Je to opět můj vlastní plugin do Pelicanu. Články se vybírají podle magického algoritmu, jehož recepturu nikdy nikde neodhalím!

![Upoutávka na další články]({static}/images/screenshot-2022-12-01-at-22-34-22.png)

## Reklama na junior.guru

Jeden z důvodů, proč jsem si chtěl předělat web, bylo odstranění odkazů na GitHub Sponsors nebo Patreon z patičky článků a aktualizace prezentace mojí osoby. Moje podnikání, [junior.guru](https://junior.guru/), se za tři roky existence posunulo a myslím si, že už by mělo být schopné normálně vydělávat. Pokud nevydělá, měl bych to řešit jako podnikatel. Lidi o dobrovolné příspěvky žádat už nechci, byť mi v rozjezdu hodně pomohly a vážím si jich. Pod články jsem nově dal zcela přímočarou reklamu na junior.guru, která by mohla mít ten správný efekt.

![Upoutávka na junior.guru]({static}/images/screenshot-2022-12-01-at-22-43-45.png)

## Zjednodušené vkládání obrázků

K mnoha změnám na blogu mě inspiroval [Lukáš Augusta](https://www.lukasaugusta.cz/tydenni-zurnal). A dokonce se shodou náhod taky rozhodl předělávat si vlastní web:

> Na můj osobní web chodí dost lidí a je škoda, že tam o Landing page odshora až dolů™ není ani zmínka. Proto jsem se rozhodnul vytvořit nový web a souběžně s tím aktualizovat, čemu se věnuji a třeba doplnit portfolio.
>
> — Lukáš Augusta, [#13: První přemýšlení nad propagací rozborů webů](https://www.lukasaugusta.cz/tydenni-zurnal/13-prvni-premysleni-nad-propagaci-rozboru-webu)


Jedna z věcí, které se mi u něj líbily, bylo časté využívání obrázků v článcích. Lukáš je designer, tak má přirozeně blíž k tomu, aby místo tisíce slov použil jeden obrázek. Mě by to taky neuškodilo.

Proč vlastně obrázky běžně do článků nedávám? Protože je to pruda. Abych nacpal obrázek do staticky generovaného blogu běžícího na Markdownu a Pelicanu, je to strašně moc kroků. Stáhnout. Dát na správné místo. Zmenšit. Odkázat správně z Makrownu. Uf.

Řekl jsem si, že udělám vše proto, aby bylo vložení obrázků co nejjednodušší. Co třeba _Drag & Drop_? Šlo by to nějak? Šlo. Stačilo trochu hledat a zjistil jsem, že [VS Code přímo podporuje přetažení obrázku do Markdownu](https://www.youtube.com/watch?v=gYoZ9QHM-uU), jen je potřeba při tom podržet <kbd>Shift</kbd>.

Vloží se ale s cestami, které povedou buď někam na internet, nebo někam jinam na můj disk. Vytvořil jsem tedy ještě skript, který projde soubory a hledá v nich takto vložené obrázky. Když na nějaký narazí, „vcucne“ ho do blogu. Nakopíruje na správné místo, zmenší, opraví cestu ve zdrojovém souboru.

Povedlo se mi zjednodušit bariéru pro nahrávání obrázků do článků? Posuďte sami :)

## Týdenní poznámky

Zvažuji, že přestanu týdenní poznámky číslovat, ale zatím jsem to nezrušil. Už nevím, proč jsem je číslovat začal a nepřijde mi, že je to vlastně k něčemu dobré. Přestat s číslováním 11.11., kdy vyšly 111. poznámky, by navíc bylo celkem vtipné.

Jak jsem už psal, můj skript pro vytvoření šablony článku s týdenními poznámkami jsem změnil tak, aby hledal mnou sdílené věci na Telegramu místo na Pocketu.

Podíval jsem se ještě, jestli by nešlo nějak elegantněji řešit napojení na Stravu, kde skript vždy zjišťuje, jak moc jsem daný týden sportoval, nebo jak jsem se flákal. Našel jsem skvělý projekt [strava-offline](https://github.com/liskin/strava-offline/), který je dokonce od autora, kterého znám :) Našel jsem hned jeden [malý bug](https://github.com/liskin/strava-offline/issues/8), ale Tomáš jej okamžitě opravil.

Nástroj umožňuje stáhnout si data ze Stravy do lokální SQLite a pak je třeba i inkrementálně aktualizovat. Řeší veškeré ofuky s přihlašováním do API, tokeny, apod. Skvělé! Mohl jsem smazat spoustu vlastního kódu. Navíc mám teď na disku data ze Stravy hezky v SQLite souboru a ten jsem si přidal do seznamu věcí, které se mi budou zálohovat.

## Nový design a Bootstrap

S designem jsem strávil nejspíš nejvíc času. Chtěl jsem k tomu opět přistoupit minimalisticky, ale rozhodl jsem se nahradit vlastní CSS frameworkem [Bootstrap](https://getbootstrap.com/), přes který jen přeplácnu pár vlastních barev a komponent. Na junior.guru používám Bootstrap a [Bootstrap Icons](https://icons.getbootstrap.com/) taky a chtěl jsem k sobě tyto mé dva hlavní projekty přiblížit, ať moje hlava nemusí moc přepínat (i když teda na junior.guru to mám v SCSS).

Poprvé jsem se odvážil více využít v designu _utility_ třídy místo samostatných komponent. Bohužel se to [stalo nějak samo](https://www.youtube.com/watch?v=cCnKiGfxSHI) uprostřed stylování webu, takže půlka toho CSS je zbytečně „překomponentovaná” a druhá je spíš „tailwindovsky naprasená“ přímo přes třídy v HTML. Rád bych se k tomu někdy vrátil a některé komponenty zrušil na úkor pár ad-hoc tříd v HTML.

Experimentoval jsem s tím, že z úvodních obrázků článků vytáhnu dominantní barvu a ta někde bude, ale nakonec jsem to nevyužil. Překvapilo mě však, [jak jednoduše to jde v Pythonu udělat](https://stackoverflow.com/a/61730849/325365).

Poprvé jsem použil `<meta name="theme-color" content="#457E31">`, což umí obarvit vršek prohlížeče v Safari na iOS. Možná i jinde.

![Theme Color v Safari]({static}/images/img-022c48d5f8e7-1.jpg){: .img-thumbnail }

Výsledný design rozhodně není a nemá být revoluce. Některé prvky jsou dokonce návrat k nápadům, které už jsem na blogu dřív měl.

## Změny v kódu

Abych neměl v kódu už moc velký nepořádek, začal jsem tam používat [click](https://click.palletsprojects.com/) a všechno uklidil do balíčku. Super je, že strava-offline taky používá click, takže jsem mohl commandy sloučit a teď mohu napsat `blog strava` a ovládat přes to vše, co mi strava-offline nabízí.

```
$ blog strava
Usage: blog strava [OPTIONS] COMMAND [ARGS]...

Options:
  --config-sample  Show sample configuration file
  --help           Show this message and exit.

Commands:
  gpx                  Download gpx for your activities
  report-bikes         Show all-time report by bike
  report-yearly        Show yearly report by activity type
  report-yearly-bikes  Show yearly report by bike
  sqlite               Sync bikes/activities to sqlite
```

Projekt jsem převedl z `requirements.txt` na [Poetry](https://python-poetry.org/). Zajímalo mě, zda jde Python knihovnu označit tak, aby nešla publikovat na PyPI. Matně si pamatuji, že u npm balíčků to nějak udělat šlo. Zjistil jsem, že PyPI na to [má speciální klasifikátor](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#classifiers): `Private :: Do Not Upload`

## Proč?

Svou osobní stránku a blog jsem předělal ze dvou důvodů. Předně, už delší dobu mě štvalo, že web nemám v mnoha ohledech obsahově aktuální a že nepomáhá dostatečně mé osobní značce, ani mému podnikání, ačkoliv by mohl a měl. Za ty dva roky se dost věcí změnilo a chtěl jsem víc propagovat junior.guru přímo pod každým článkem. Také už se vidím víc jako podnikatel a [mluvící hlava](https://cestina20.cz/slovnik/mluvici-hlava/) než programátor.

Zároveň jsem se v posledních týdnech z různých důvodů pustil do toho digitálního úklidu a tohle s tím oklikou souvislo. Potřeboval jsem si taky odpočinout od práce a předělávání vlastních webovek mi poskytlo hezkou náhradní činnost, do které jsem se mohl na dva týdny ponořit a prostě si chvíli jenom hrát. Celé to teď o víkendu završím výletem do hor.

Budu rád, když mi dáte vědět, jak se vám nová podoba blogu líbí a co je tady na prd. Třeba to opravím. Napište do komentářů, nebo [založte issue](https://github.com/honzajavorek/honzajavorek.cz/issues) :)
