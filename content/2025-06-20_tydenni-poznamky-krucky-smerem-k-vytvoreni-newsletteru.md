Title: Týdenní poznámky: Krůčky směrem k vytvoření newsletteru
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/353
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/114716261401131225

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-06-13_tydenni-poznamky-prednaska-s-evou-pavlikovou-a-pokusy-s-ai.md) už utekl nějaký ten týden (13. 6. až 20. 6.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Nekonečné ladění LLM

Bylo to nekonečné, strašné ladění, ale skript na vytváření shrnutí dění v klubu za poslední měsíc teď fakt dokáže vracet něco použitelného. Už jsem tomu ani nevěřil, ale vážně jsem se teď dostal do fáze, že to je z 99% správně. Pomohlo mi zařadit _chain of thought_, vyčistit data od _low engagement_ kanálů, a uvědomit si, jak se ten výsledek vlastně bude prezentovat lidem, protože _wall of text_ nikdo číst nebude. Taky pomohlo přejít na lepší a dražší modely a rozdělit to celé do víc kroků, každý s jednodušším a přímočařejším zadáním.

Co se za poslední měsíc probíralo za nepodstatnější témata nelze změřit, takže nevadí, že to není deterministické. Zdá se ale, že vybírá vhodné věci. Pomohlo říct si o imaginární skóre engagementu. To mi sice do JSONu vygeneruje i nesmyslné číslo, které pak zahodím, ale výsledky to dává lepší 😀

I stylisticky jsem to nakonec taky dosochal do něčeho, co působí konverzačně a nešustí vyloženě papírem. Juchů! Takže velmi důležitý základ pro newsletter bych měl.

Taky jsem se naučil, jak do OpenAI posílat přímo strukturu přes Pydantic, to je docela hezké.

## Buttondown

Nejvíc se mi zamlouvá seskládat newsletter jednou měsíčně jako novou položku v nějakém RSS, a to nechat automaticky načíst do [Buttondownu](https://buttondown.com/). Tam vznikne draft ke schválení. Nebo to tam rovnou poslat přes API jako draft. Pak ručně zkontroluju, upravím, odešlu. Z Buttondown archivu si pak můžu vzít upravený obsah a uložit do svého archivu.

Podporují Django Templates, což je fajn. Ale stejně asi bude v RSS muset být něco, co se dobře zobrazí v emailových klientech 🤔 Kódování e-mailů je za trest, no ChatGPT mi s tím snad pomůže. Uvidíme, jak to dopadne.

Každopádně jsem se jal zkoumat, jak to celé teda funguje. Prošel jsem celou dokumentaci Buttondownu, jejich demo appku, četl jsem si jejich API dokumentaci, srovnával pricing s Ecomailem, apod. Taky jsem jim napsal dotazy mailem. Byli velmi milí.

Uvědomil jsem si totiž, že nemají češtinu. Takže jsme se i hned domluvili, že jim ji pomůžu přidat. Dali mi pár souborů do privátního repozitáře na GitHubu a když budu mít chvilku, můžu texty přeložit do češtiny. Super! Mnohem lepší, než na Memberful, kde mi sice češtinu přidali, ale mají v ní milion chyb a protože to outsourcují přes externí agenturu, nemůžou a nechtějí s tím nic dál dělat.

![překlady]({static}/images/screenshot-2025-06-20-at-16-11-12-buttondown-translations-cs-translation-into-czech-cs-cz.png)

## GDPR

No a ještě pak potřebuju vyladit jednu věc. Chtěl bych, aby newsletter dostávali lidi, kteří platí za klub. Teď tam mám jen ty, kdo se přihlásili k odběru na webu.

Jenže to je GDPR (?) bludiště. Lze newsletter považovat za informování o produktu, za který ti lidi platí? Podle mě jo. Možná nepotřebuju konsent. Ale možná jo.

Stávajícím členům to nejspíš nemůžu zapnout vůbec, novým musím nějak předělat registrační flow. Asi. Měl jsem v tom guláš. Tolik práce, přitom taková blbost!

No právník ChatGPT pomohl. Novým lidem jsem přidal zaškrtávátko do registračního flow. Starým pak pošlu jednorázové upozornění, že newsletter existuje, a mohou si jej přihlásit. Víc asi nezmůžu.

## Statistiky nabídek práce

Mám hromadu nápadů, co by v newsletteru mohlo být a dost času jsem strávil i tím, že jsem tyhle svoje představy ladil a zapisoval si je. Dost z těch věcí ale bude ještě vyžadovat přípravu.

Za normálních okolností bych udělal minimalistické MVP a pustil hned do světa, ale teď mám trochu jinou situaci. Sbíral jsem dlouhou dobu odběratele newsletteru, aniž bych jim nějaký posílal, až jich mám k dnešku 649. Klidně se [taky přidejte](https://junior.guru/news/), mrk mrk.

Předpokládám, že až pošlu první „dopis“, hromada z nich se hned odhlásí - a je to tak dobře, pokud pro ně tohle už není relevantní. Ale chtěl bych tuhle příležitost využít k tomu, abych přece jen co nejvíc lidí zaujal tím, co jim přijde. Chci, aby to bylo potenciálně užitečné, ne aby to byl jen nějaký reklamní letáček do koše.

Jedna z věcí, které by mohly být užitečné, jsou statistiky nabídek práce na junior.guru. Jenže já je nesbírám. Takže jsem naprogramoval to, aby se sbíraly. Zkoušel jsem různé věci, ale nakonec mi z toho vylezlo aspoň tohle:

Každé pondělí se udělá a uloží _snapshot_ pár čísel. Je tam počet stažených nabídek, které prošly sítem, počet zahozených, počet ručně vložených na Discord, a pak počty pro jednotlivé technologie.

Teď se to bude každý týden ukládat a než připravím newsletter, tak už budu mít aspoň pár „puntíků do grafu“ a můžu lidem ukazovat nějaký trend v čase. Mohlo by to pomáhat lidem s přehledem, jak se vyvíjí situace a jaké technologie jsou žádané.

## Kutění na p3news

Projekt [p3news](https://github.com/honzajavorek/p3news) stahuje zprávy radnice Prahy 3 a dělá z nich RSS a publikuje je na Mastodon. Napadlo mě přidat tam aktuality z [Nové Trojky](https://www.nova-trojka.cz/), tak jsem to během jednoho večera udělal. Ale pak mě napadly další věci a nemohl jsem se nějak s myšlenkama zastavit.

V hlavě jsem ukul plán na malý startup, který by byl užitečný pro hodně lidí v sousedství, mě by dělal radost jako služba veřejnosti, technicky by nebyl moc složitý, a jako obvykle, nejspíš by vůbec nic nevydělal. Nemám paralelní život na jeho vytvoření, ale asi se stejně neubráním tomu, abych to po kouskách nezkusil realizovat.

Při úpravách jsem nově použil Crawlee a hned jsem při tom založil [jedno filozofické issue](https://github.com/apify/crawlee-python/issues/1261).

## Další

-   Zkusil jsem si nainstalovat [Signal](https://signal.org/). Kdo tam jste a máte moje číslo, přidejte si mně. Akorát to někdy nezobrazuje žádné informace o druhé straně, takže neposílejte do té první zprávy smajlíky a stickery, ale raději napište, kdo jste 😀
-   Aktualizoval jsem [záznam v katalogu o SDA](https://junior.guru/courses/sdacademy/), protože se zdá, že přestali existovat.
-   Dvě firmy chtěly na junior.guru inzerovat nabídky práce, tak jsem jim sepsal do mailu nějaké varianty a podmínky. Zatím bez odezvy.
-   Lítali jsme se ženou po obhlídkách bytů a možná máme úlovek, ale uvidíme.
-   Táňa mě uháněla, abych hledal přednášející na další měsíce, tak jsem je hledal a předhazoval je Táni na zpracování.
-   Daria jede jak drak na přípravách EuroPython Beginners' Day Unconference, tak mě taky s pár věcmi uháněla. Hlavně bychom měli přitlačit na marketing, protože se nám zatím registrovalo dost málo lidí. Hledal jsem panelistky a panelisty, teď z nich mámím fotky, dolaďujeme web.
-   Z Mews mi zatím neodpověděli co se týče podzimní akce, tak jsem to do Týdne pro digitální Česko založil aspoň tak napůl, jako že to bude, ale spousta detailů ještě chybí. Doladíme časem. Název akce bude nejspíš tento: „Jak pracovat s AI jako junior v IT? Čím si pomoci a čeho se vyvarovat?“
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Vyřídil jsem dvě stipendia.
-   Za 8 dní jsem naběhal 22 km, při procházkách nachodil 8 km. Celkem jsem se hýbal 10 h a zdolal při tom 30 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Budu mít Apify týden. Chtěl bych v rychlosti dodělat JavaScriptový kurz.
2.  Zpropaguju znova EuroPython Beginners' Day Unconference.
3.  Přeložím Buttondown do češtiny.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Markdown is unformatted formatting](https://buttondown.com/blog/the-markdown-story)<br>Mile zpracovaná historie formátování plain textu na internetu.
- [Města bez plánů / Order without Design](https://smichovreviewofcities.substack.com/p/mesta-bez-planuorder-without-design)<br>„…při návštěvě nového města jděte nejdřív do úplného centra a potom pěšky zhruba stále rovně až na úplný okraj, ať máte plnou představu o tom jak celé skutečně vypadá a funguje, mimo možná zavádějící terárium turistického centra.“
- [Čtvrtinu Čechů ohrožuje dopravní chudoba](https://www.irozhlas.cz/zpravy-domov/ctvrtinu-cechu-ohrozuje-dopravni-chudoba_2506160642_kma)<br>Zajímavé grafy a příběhy. „…když zaspíte ve městě, přijdete do práce pozdě o tolik, o kolik jste zaspali. Kdežto když zaspíte na venkově o pět minut, spoj vám ujede a můžete přijít pozdě i o tři hodiny. Jsou to neuvěřitelné nervy a potíže, které to přináší.“
