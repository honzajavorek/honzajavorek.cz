Title: Týdenní poznámky: Přepisování kurzu, přípravy na EuroPython a videotvorba
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-06-20_tydenni-poznamky-krucky-smerem-k-vytvoreni-newsletteru.md) už utekl nějaký ten týden (20. 6. až 4. 7.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Za poslední dva týdny se mi povedlo zajít na oběd se třemi kamarády, zajít do kina Aero na „naslepo“ (dávali [Kdo s koho](https://www.csfd.cz/film/96170-kdo-s-koho/prehled/) a bylo to super), několikrát si zaběhat, strávit s dcerou pěkné odpoledne na Vyšehradě („višněhradě“), strávit víkend s rodiči a zajít s nimi i do [muzea](https://muzeumfantastickychiluzi.cz/cs/), prožít blackout v Praze, zažít slunovrat a tedy i svůj svátek, nebo se dovědět na poslední fyzioterapii, že zbytek už prý zvládnu sám.

## Práce pro Apify

Ve svém červnovém týdnu pro Apify jsem pokračoval v práci na JavaScriptovém kurzu scrapování, který nevytvářím úpravami starého, již existujícího, ale překlopením svého nového Python kurzu do JavaScriptu. Mám k tomu otevřený [obrovský praso-Pull Request](https://github.com/apify/apify-docs/pull/1584), kam to všechno sázím, a z něj ukrajuji menší kousky ostatním na review.

- Zjistil jsem, že F1 změnila web, takže [se mi rozbila některá cvičení](https://github.com/apify/apify-docs/issues/1648).
- [Připravili jsme](https://github.com/apify/apify-docs/pull/1651) půdu pro nový kurz tak, že jsme mergnuli kopii Python kurzu, která zatím bude v Docusauru jako `unlisted`.
- Udělal jsem PR pro [intro](https://github.com/apify/apify-docs/pull/1653), [DevTools 1](https://github.com/apify/apify-docs/pull/1654), [DevTools 2](https://github.com/apify/apify-docs/pull/1655), [DevTools 3](https://github.com/apify/apify-docs/pull/1656), [downloading](https://github.com/apify/apify-docs/pull/1657).
- [Předělal jsem pořadí](https://github.com/apify/apify-docs/pull/1658) některých věcí v Python kurzu, aby to mohlo být v obou kurzech stejné.
- Designerka mi [dodala nové obrázky pro kurzy](https://github.com/apify/apify-docs/issues/1574#issuecomment-3019583731) a jsou pěkné, ale ještě jsem je nestihl implementovat.

Některé věci nelze úplně přímočaře z Pythonu předělat do JavaScriptu, ale nakonec jsem vše nějak vymyslel. Je to vlastně docela zajímavý úkol a baví mě to. Šlo mi to ale ke konci trochu pomaleji, než jsem čekal.

## Přípravy na EuroPython

Nevýhoda akcí, které se konají živě na nějakém místě a v nějaký čas, jsou termíny a z nich plynoucí stres. Jinými slovy, bylo potřeba zpropagovat konečně pořádně naši Beginner's Day Unconference a ideálně i celý Beginner's Day. Což jsou tři akce v jeden den a Unconference je jen jedna z nich. Ano, je to zamotané a vůbec to nejde vysvětlit tak, aby se v tom lidi orientovali.

EuroPython v rámci konference bude mít den, kam ale může přijít i člověk bez EuroPython lístku. Ten den je pro začátečníky a jedou v něm tři paralelní akce: Django Girls, Humble Data a ta naše Unconference. Protože nejde jít na všechno, musí si lidi vybrat. Takže se musí registrovat přes formulář, tam klikají priority na kterou z těch akcí chtějí a když se vlezou, mohou si koupit lístek za 5 euro a pak opravdu přijít. Mega komplikované!

Každopádně zpět k tématu. Bylo potřeba propagovat tu naši akci, aby na ni někdo přišel. Rozhodl jsem se, že když mě v poslední době tak baví stříhání videí, mohl bych na to nějaké video i vyrobit. Nebyl jsem si jistý, jak na to půjdu, ale pak mě ve sprše napadlo, že bych mohl jet kamerou přes lístečky, na které něco nakreslím, a něco u toho povídat. Nakonec jsem to celé vytvořil za zhruba 4h, kde 1h bylo natáčení a 3h bylo stříhání. Výsledkem jsou 2,5min, které si můžete pustit na:

- [Mastodonu](https://mastodonczech.cz/@honzajavorek/114750031774858668)
- [YouTube](https://youtube.com/shorts/jqokuIJjgQk)
- [Instagramu](https://www.instagram.com/reel/DLXc3WiMLKh/)
- [LinkedInu](https://www.linkedin.com/feed/update/urn:li:ugcPost:7343994345139695617/)
- v asi 7 Facebookových skupinách, kam jsem to dal
- v asi 5 Discordech, kam jsem to dal

Jsem si vědom, že má video mnoho nedostatků, ale nemohl jsem se s tím mazlit nekonečně dlouho, muselo to rychle ven. Takže jsem udělal to, co v daném čase šlo.

Jak je vidět, další dlouhé hodiny jsem strávil psaním statusů a sdílením videa na sítích. Bylo potřeba to stihnout ještě před začátkem prázdnin, než půlka lidí někam odjede. Dobrá zpráva je, že se to stihlo a že to mělo efekt a lidi už se nám sypou do formulářů.

Video [míří na redirect](https://junior.guru/bd/), který jsem na webu musel nejdřív vytvořit. Chtěl jsem, ať to má nějaké zapamatovatelné URL, které mám ideálně pod kontrolou a kdyby se něco změnilo, mohu změnit, kam posílá lidi. Taky jsem přidal na web nahoru i proužek, který na akci upozorňuje.

A ještě jsem zkusil [upravit web](https://junior.guru/events/53/) a Discord bota tak, aby dokázal evidovat nejen online akce, ale i živé akce v terénu. To bylo docela zamotané, narychlo jsem to naprasil, a nemám z toho dobrý pocit. Nějak mi to tam nesedí. Nechám to tam, aby se akce propagovala, ale až bude po všem, asi to celé odeberu, i s podporou pro IRL akce v systému, protože mi přijde, že se snažím naroubovat něco do místa, kam to nepatří a proto to všude vytváří spoustu nepříjemné komplexity.

![Stránka události]({static}/images/screenshot-2025-07-04-at-22-43-09-beginners-day-unconference-junior-guru-akce.png){: .img-thumbnail }

## Videotvorba

S videem jsem si hrál i dál. Nejdříve jsem dál ve volném čase stříhal blbiny a vzdělával se ve video editingu a ovládání DaVinci, ale pak mě napadlo, že bych mohl navázat na propagační video pro Beginners's Day a udělat něco užitečného.

Rozhodl jsem se, že konečně udělám video, které bude představovat a ukazovat klub. Už dlouho vím, že bych jej potřeboval, ale nikdy jsem se nerozhoupal k tomu, abych jej vytvořil, byť třeba i jen jako hodně přímočarý screencast.

No ale doba se změnila a teď mám chuť a schopnosti udělat dokonce něco pořádného. Takže poslední dny jsem strávil přípravami tohoto videa, ať už to bylo vzdělávání se, zkoušení různých věcí, příprava scénáře, konceptu, atd.

Asi jsou i důležitější věci, co bych mohl dělat, ale jsou prázdniny a léto a vůbec–měl bych využít toho, že jsem pro to zrovna zapálený a baví mě to. Příjemné s užitečným. Těším se, co z toho vyleze. Ale asi si to vezme hodně času, protože jak se znám, budu z toho chtít udělat Holywoodský blockbuster…

## Další

-   ČSFD se zřejmě začalo bránit scrapování, takže mi přestala fungovat kontrola rozbitých odkazů, přestal mi fungovat můj kalendář kin a přestal mi fungovat i můj Telegram bot „film2trello“, který po zadání odkazu na film nebo seriál tento smotá do Trello kartičky, kde si se ženou vedeme, co chceme vidět, nebo co jsme viděli. Budu plakat! Sice to má řešení, ale ošklivá řešení a já teď nemám ani čas, ani chuť to dělat.
-   Volal jsem si s Terkou copywriterkou, probírali jsme její věci a pak můj newsletter a EuroPython Beginners' Day video.
-   Opravil jsem jednu drobnou chybu v Discord botovi.
-   Zkouším používat Signal, ale něco tomu chybělo. Pak mi došlo, že tam není můj osobní sticker pack, který mi kdysi ze srandy vytvořil Dan Srb, když vystříhal moje hlavy z jednoho Q&A, které jsem dělal na YouTube. Takže jsem jej vzal a přenesl do Signalu. Můžete [instalovat](https://signal.art/addstickers/#pack_id=51b35289d5a24f0c4a6afb3e853e0ca3&pack_key=c9e1fac8f906f029e1998533729f721f10d313a056f6eb0cd9fcea047836431a).
-   Pracoval jsem na tom, abychom měli do budoucna nové bydlení.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Okurková sezóna, takže toho nebylo nějak moc. Mrknul jsem konečně na Pull Requesty aj. věci pro Pyvec.
-   Za 15 dní jsem naběhal 52 km. Celkem jsem se hýbal 6 h a zdolal při tom 52 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Tvořit video.
2.  Zvlonit tempo, dcerka má prázdniny.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Budapešťský Pride ukázal jedinou účinnou strategii, jak čelit omezování svobody](https://denikalarm.cz/2025/07/budapestsky-pride-ukazal-jedinou-ucinnou-strategii-jak-celit-omezovani-svobody/)<br>„Po zákazu Pridu stáhly svou podporu firmy, které se průvodu účastnily v minulých letech. Letos se ho neúčastnily a na otázky novinářů neodpovídaly. Korporáty budou podporovat otevřenost a toleranci jen, pokud to bude cool a bude se to vyplácet. Stejně jako všechny ostatní rádoby etické akcenty jim slouží i podpora LGBTQ+ nebo kohokoliv či čehokoliv jiného jako marketing.“
- [Nová tramvaj 52T v Praze: Nejpohodlnější a nejtišší jízda v historii MHD? - YouTube](https://www.youtube.com/watch?v=dJRxu2RHPyk)<br>Tak na tuhle tramvaj se těším!
- [Prague is a Parody of Europe - YouTube](https://www.youtube.com/watch?v=YZXzgIhFAXk)<br>Smutný, ale skvělý. A komentáře výživné.
- [Telegram, the FSB, and the Man in the Middle](https://www.occrp.org/en/investigation/telegram-the-fsb-and-the-man-in-the-middle)<br>„If someone has access to Telegram traffic and cooperates with Russian intelligence services, this means that the device identifier becomes a really big problem — a tool for global surveillance of messenger users, regardless of where they are and what server they connect to.“
- [Zápisky z pražského podzemí: jak zpeněžit komoditu zvanou turista  – Page Not Found](https://pagenotfound.cz/clanek/zapisky-z-prazskeho-podzemi-jak-zpenezit-komoditu-zvanou-turista)<br>„Čtyři roky jsem žil v paralelním vesmíru, kde jsou špinavé krámky s ušankami, matrjoškami a šperky spolu s falešnými "českými" restauracemi přísně – téměř geopoliticky – rozděleny mezi vlivné majitele východoevropského, balkánského a blízkovýchodního původu.“
- [Nezájem o mír. Co nám říká Trumpova neschopnost - VOXPOT: reportáže, které spojují Česko se světem](https://www.voxpot.cz/nezajem-o-mir-co-nam-rika-trumpova-neschopnost/)<br>„Nezbývá, než se ptát – pokud byla Bidenova administrativa slabá, co je potom ta Trumpova?“
- [Markdown is unformatted formatting](https://buttondown.com/blog/the-markdown-story)<br>Mile zpracovaná historie formátování plain textu na internetu.
