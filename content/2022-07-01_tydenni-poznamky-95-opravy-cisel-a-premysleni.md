Title: Týdenní poznámky #95: Opravy čísel a přemýšlení
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl zase nějaký ten týden (25.6. — 1.7.) a tak [stejně jako minule]({filename}2022-06-24_tydenni-poznamky-94-premysleni-psani-a-cisteni.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Opravování chyb v grafech

Snažil jsem se opravit různé chyby na [stránce s grafy](https://junior.guru/open/). Neseděl mi počet členů z API a počet členů na Discordu. Nelíbilo se mi, že poslední měsíc vždy vypadal nějak divně. Na něco jsem přišel, něco jsem spíš jenom pochopil proč tak je a vysvětlení jsem si dopsal do textu u grafu. Rozdělil jsem grafy s příchody a odchody. Přidal jsem do grafů procentuální _churn_, konečně. Opravil jsem graf s délkou setrvání v klubu.

Zjistil jsem, že se mi nezapočítávají lidi, kteří jsou na dárkovém předplatném (taková ta vánoční akce). Vzhledem k tomu, že s těmito dárky do budoucna nepočítám, rozhodl jsem se místo debugování tyto zhruba tři lidi v Memberful konvertovat na standardní roční členství a to dárkové jsem smazal ¯\\\_(ツ)\_/¯


## Výpomoc na marketing

[Inzerát na marketingovou výpomoc]({filename}2022-06-24_vypomoc-na-socialni-site.md) jsem nad rámec tohoto blogu nebo klubu záměrně nikde nepropagoval. Ozvalo se mi několik lidí. Pár lidí mi někoho doporučilo a já se pokusil ty doporučené lidi kontaktovat.

Nakonec jsem to ale spíš pozastavil, protože inzerát jsem sice sepsal hezký, ale v důsledku vyvstala spousta otázek, na které si ve skutečnosti neumím odpovědět. Kolik na to mám peněz? Hledám profíka, který bude přicházet s vlastními nápady a řešeními, nebo čistě výpomoc, kterou třeba i zaučím? Jak důležitý je pro mě marketing na sociálních sítích? Za jakým účelem ho dělám a jak bych popsal „úspěch“ této své činnosti?

Ve výsledku nejenže neumím vybrat člověka, který by zaplácl mou nechuť dělat dál marketing na sociálních sítích sám, ale spadla na mě i tíha všech otázek výše a nechuť je řešit. Pak někde někdo nasdílel [videa z letošního WebExpa](https://slideslive.com/webexpo/webexpo-2022) a já tam zahlédl přednášku [Outsourcing Your Marketing? Do Your Homework First](https://slideslive.com/38984420/outsourcing-your-marketing-do-your-homework-first) od Jany Dolejšové. Podíval jsem se na [její web](https://www.janadolejsova.cz/) a uvědomil jsem si, že to, co nabízí, je nejspíš přesně něco, co potřebuju. Chci jednorázovou konzultaci od profíka, která by mi pomohla uspořádat si myšlenky, nastavit strategii, případně i vybrat člověka na výpomoc nebo změnit, jak to celé dělám.

Aktuálně pracuji na tom, abych taková konzultace proběhla a pak se uvidí. Do té doby budu stále rád za tipy na výpomoc, ale samotné „výběrové řízení“ jsem tímto ze své strany pozastavil.


## Výkop onboardingu

Začal jsem realizovat onboarding nových členů v klubu. Vytvořil jsem skript, který umí vyrobit nový privátní kanál na Discordu a dát do něj oprávnění určitým rolím nebo lidem.

Předtím jsem se ještě podíval na skript, který analyzuje obsah Discordu. Zefektivnil jsem jeho průběh a místo 4.5min teď trvá 3.7min. Udělal jsem to tak, že se už klub neanalyzuje v rámci celé své historie, ale jen za poslední rok. Některé kanály navíc nově přeskakuji úplně, některé jsem omezil na pouhý měsíc zpět. Tím by se také mělo zabránit narůstání délky trvání tohoto skriptu.


## Co můžu zrušit

Pokračoval jsem s přemýšlením, co můžu do budoucna zefektivnit, zrušit, nebo dělat jednodušeji a jinak. Už minule jsem psal:

- Nebudu už vzdělávacím agenturám nabízet program pro jejich studenty
- Nejsem zatím přesvědčen o tom, že má smysl dělat nějaké velkolepé plány kolem stipendia
- Omezím režii kolem dobrovolných příspěvků
- Zkusím delegovat nějakou práci na marketingu na sociálních sítích

Dále mě napadlo:

- Zrušit outbound marketing kromě Q&A pro komunity a podcastů, kde je dobrý poměr cena/výkon
- Zjednodušit ceník pro firmy
- Mít spolupráce s firmami a komunitami jasně zabalené jako balíčky, které jsou pro všechny stejné a mají jasné mantinely a není kolem nich žádná „speciální“ komunikace
- Možná zavést _free plan_ pro firmy, které nechtějí členství, ale nabízí nějaký _barter_ (sleva pro klub, marketing) a dát tomu opět jasné podmínky a mantinely
- Automatizovat některé maily firmám
- Natočit screencast jako demo toho, jak vypadá klub a co se v něm dá dělat, což zjednoduší nebo zruší „sales cally“
- Umět na většinu mailů odpovědět odkazem někam do FAQ
- Zrušit spreadsheet, kde mám seznam členů klubu - důvody, proč jej mám, lze myslím už plně řešit přímo přes admina Memberful


## Další poznámky

- Domlouvám se s jedním mentorem, že si zavoláme a řekne mi feedback z mentorování v klubu.
- Uzavřeli jsme spolupráci s Engetem. Bude to mít více úrovní, ale pomůžu jim s propagací jedné věci a společně připravíme průzkum mezi juniory.
- Řešil jsem faktury s několika dalšími firmami.
- Domlouval jsem přednášku v klubu od Codeac, na září.
- Byl jsem na dentální hygieně.
- Koukal jsem se na možnosti půjčení vozíku na dítě za kolo (chariot).
- Uměle jsem prodloužil členství hned několika firem až do 1.9., ať s nimi nemusím komunikovat teď v létě, kdy jsou všichni na dovolené, a ať mám přes léto trochu klid na práci. Navíc od září chci mít už i jiný ceník.
- Přidal jsem se do [skupiny pro kariérové poradce](https://www.facebook.com/groups/karieroviporadci/).
- Řešil jsem stipendium pro jednu členku.
- Sepsali jsme spolu s Jakubem z Processandu [inzerát](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/). Ještě na ten text sbírám feedback i v klubu mezi juniory, ale už jsme to dali ven, ladit to můžeme za pochodu.
- Sešel jsem se s [Lucií Václavkovou](https://lucie.vaclavkova.com/) a povídali jsme si o svých byznysech.
- Na zanedbanou [stránku s přednáškami](https://junior.guru/events/) jsem aspoň doplnil jména přednášejících a opravil jeden odkaz.
- Jeli jsme do zookoutku v Milíčově.
- Zvýšil jsem svou základní poslechovou rychlost pro většinu podcastů na 2,5x
- Vyzvedl jsem si oblek v čistírně
- Sociální sítě: Propagoval jsem [podcast s Pájou](https://www.programhrovani.cz/1843229/10874390-dev-stories-4-paja-fronkova-z-pyladies-do-irska-a-zase-zpatky).
- Klub, maily, a tak dále.
- Během 7 dní od 25.6. do 1.7. jsem naběhal 11 km, při procházkách nachodil 7 km. Celkem jsem se hýbal 6 hodin a zdolal při tom 18 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Programovat onboarding.
2. Vymyslet nový ceník.
3. Seznam co zrušit, delegovat, nebo automatizovat přeměnit na konkrétní úkoly.

**Bonus:** Naplánovat si pořádnou dovolenou.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [The Left-NIMBY canon](https://t.co/az0WjVgkYN?ssr=true)<br>Různé pohledy na řešení krize bydlení. Levicové NIMBY vs YIMBY.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
