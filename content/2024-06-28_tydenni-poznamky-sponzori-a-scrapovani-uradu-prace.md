Title: Týdenní poznámky: Sponzoři a scrapování Úřadu práce
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/322
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/112695202781271724

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-06-21_tydenni-poznamky-cerven.md) už utekl nějaký ten týden (21. 6. až 28. 6.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
</div>

Tak konečně jednou píšu zase poznámky po týdnu! Nic speciálního se nedělo, nebyl jsem nemocný, nikam jsem nejel a ničeho se neúčastnil. Hurá. Akorát jsme si jako rodinka udělali o víkendu výlet na kole.

![Kladruby]({static}/images/img-0348.jpg)

## Dodělávání stránky pro sponzory

Většinu týdne jsem pracoval na úpravách a vylepšování [stránky pro sponzory](https://junior.guru/love/).
Takhle to zní docela blbě, ale ono je tam spousta věcí „pod povrchem“, které bylo potřeba doladit a promyslet.
A taky v tom je spousta ladění CSS.

Propojil jsem konfiguraci sponzorů a tarifů s Group Plans na Memberful. Cena a různé jiné parametry se teď berou přímo z věcí, které naklikám v administraci Memberful, a nemusím je mít zvlášť tam a zvlášť někde v YAMLu. Zároveň je tam podpora pro různé bartery apod. A zároveň by to mělo být vše „ploché“, „ohebné“ a jednoduché, ne jako minule.

Vypsal jsem tam nejznámější sponzory junior.guru za celou existenci projektu, jako důkaz, jaké firmy se mnou už byly ochotné pracovat.

Zrušil jsem dvě tlačítka vpravo nahoře na webu, která vedla na klub a na ceník pro firmy. Místo nich jsem přidal pulzující srdíčko, které vede na onu stránku pro individuální a firemní sponzory.
Stránce jsem dal nakonec i novou adresu, `/love/`, aby to bylo v souladu s nadpisem a s „tlačítkem“, které tam vede.

![srdíčko]({static}/images/screenshot-2024-06-28-at-18-16-03-jak-se-naucit-programovat-a-ziskat-prvni-praci-v-it.png){: .img-thumbnail }

Jestli bude v praxi fungovat stránka, která se snaží oslovit jak jednotlivce, tak firmy, to netuším. Jedni mají možnost posílat dobrovolné příspěvky, firmy zase mohou zakoupit sponzorské balíčky. Jenže ta hranice není tak ostrá. Například přes GitHub Sponsors mohou sponzorovat i firmy a minimálně dvě to v mém případě už udělaly. Tak uvidím, zkouším to teď takhle. Všechny předchozí adresy jako `/donate/`, `/pricing/`, `/sponsorship/`, apod. jsem přesměroval na tuhle novou „lásku“.

Na stránku jsem se snažil přidat nějaký _social proof_, _testimonials_, vložil jsem tam kreslené srdíčko (které mám ještě z dob `/donate/` stránky), přidal jsem velké pulzující tlačítko s e-mailovým kontaktem, a pod nabídku jsem sepsal odpovědi na základní otázky, které by lidi mohli mít. Tam jsem vložil živý graf s _pageviews_ relevantních stránek, kde se zobrazují loga firem a spoustu nějakých citací. Propracovával jsem jednotlivé texty, aby říkaly, co chci říct, a zároveň nebyly extrémně ukecané.

Uvažoval jsem, jestli nezaložit i `github.com/sponsors/juniorguru`, ale zatím jsem se rozhodl netříštit to a nechat vše jen [u sebe](https://github.com/sponsors/honzajavorek/).

Nové tarify už nenabízí inzerci práce na junior.guru. Nechám doběhnout ty, co na webu jsou od Red Hatu, nové už tam nechci. Do budoucna počítám s tím, že hlavní budou profily juniorů a pracovní inzeráty budou vedlejší. Celou problematiku sponzorství chci sjednotit a zjednodušit.

![sponzorství]({static}/images/screenshot-2024-06-28-at-18-15-55-podpor-junior-guru.png){: .img-thumbnail }

## Scrapování Úřadu práce

Stahuji data o kurzech z [katalogu Úřadu práce](http://jsemvkurzu.cz/), ale nějak to přestalo fungovat a blokovalo mi to build, tak jsem to operativně přepsal jako [scraper, který běží na Apify](https://github.com/juniorguru/plucker/blob/main/jg/plucker/courses_up/spider.py). Při té příležitosti jsem opravil i nějaké věci na [pluckeru](https://github.com/juniorguru/plucker/). Zabralo mi to celý jeden den. Předešlá implementace měla nějaké nedostatky, které jsem při tom vyřešil a mám teď tím pádem kompletnější data. Mám z toho radost!

![Jsem v kurzu]({static}/images/screenshot-2024-06-28-at-18-15-34.png){: .img-thumbnail }

## Crawlee

Apify mají veřejně první verzi [Crawlee pro Python](https://github.com/apify/crawlee-python)! Crawlee je jejich open source scrapovací framework, ale doteď byl jen v JavaScriptu. Teď to přepsali i do Pythonu a chystají se konkurovat [Scrapy](https://scrapy.org/), které hojně používám, ale které přece jenom působí trochu těžkopádně.

Letmo jsem si Crawlee zkusil a vypadá to slibně. Je obdivuhodné, kolik fičur se vlezlo už do této první verze, kterou chtěli stihnout ještě před pražským [EuroPythonem](https://ep2024.europython.eu/). Rozhodně to budu sledovat a případně na tom zkusím provozovat nějaký menší scraper, abych viděl, jak se to chová a jestli na to časem ze Scrapy nepřejdu.

![Crawlee]({static}/images/screenshot-2024-06-28-at-18-20-23.png)

## Úpravy katalogu kurzů

[Katalog kurzů](https://junior.guru/courses/) na webu junior.guru existuje už rok, ale jeho vylepšování nějak spadlo z mých priorit - místo kurzů jsem se začal s horším trhem zaměřovat na to, jak udělat na webu profily juniorů a jak je tlačit do firem. Proto v katalogu dodnes chybí popisky a další data k jednotlivým firmám.

Paradoxem tedy budiž, že první firmou, která popisek ode dneška má, je [ta, která už neexistuje](https://junior.guru/courses/greenfox/). Někdo mi totiž napsal mail, že GFA už zkrachovali. To samozřejmě vím, ale nechtěl jsem je (ještě) mazat z webu. Tak jsem dnes doplnil podporu pro ty popisky a něco tam k nim napsal.

Díky tomu teď bude jednodušší přidat popisek i k dalším subjektům. Přidal jsem do katalogu [Lucii](https://junior.guru/courses/dokazesprogramovat/) a hned jsem tam k ní něco napsal.

Když už jsem se v katalogu vrtal, konečně jsem taky přidal podporu pro to, aby se na detailu poskytovatele kurzu zobrazovalo logo firmy, pokud sponzoruje junior.guru. Přece jenom to už nějakou dobu nabízím v benefitech 😅 Není to graficky nic úžasného, ale celý katalog je jen jeden velký prototyp, takže nebylo ani účelem, aby to bylo nějak krásné. Jen aby to tam někde bylo.

![logo v katalogu]({static}/images/screenshot-2024-06-28-at-18-15-25.png){: .img-thumbnail }

## Další

-   Dotáhli jsme s Nelou poslední aktualizace na stránce o [psychice na cestě do IT](https://github.com/juniorguru/junior.guru/pull/1388), juchů!
    [Mergnul jsem to](https://github.com/juniorguru/junior.guru/pull/1388) zrovna při psaní této věty do poznámek 😀
-   Aktualizoval jsem po čase zase screenshoty v rámci celého junior.guru.
-   Vyjádřil jsem se organizačnímu týmu, že bych měl zájem účastnit se letošního [Týdne pro digitální Česko](https://budoucnostjedigitalni.gov.cz/).
-   Mrknul jsem na jednu podivnost v pycordu, která mi dlouho někde ležela, ale bohužel jsem to [nikam neposunul](https://github.com/Pycord-Development/pycord/issues/2399#issuecomment-2196404295).
-   Kupoval jsem si nové vybavení na kolo. Helmu, dres, lepení na duše…
    Nakonec skoro vše z Dekáče.
-   Sdílel jsem [upoutávku na EuroPython](https://www.linkedin.com/feed/update/urn:li:share:7210950019405778946/), ale vlastně už pozdě.
    Nedá se nic dělat, nestíhám holt všechno včas.
-   Šli jsme se podívat na školku, kam má malá napodzim nastoupit. To to letí!
-   Udělil jsem dvě stipendia a jedno neudělil.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Konečně jsem prošel všechny pracovní maily, co na mě čekaly.
    I ty, co někde ležely měsíce.
    V klubu to docela žilo, takže mi dalo celkem práci dostat se v pondělí na nulu nepřečtených věcí.
    Je konec týdne a je tam toho zase k přečtení hromada.
    Na Slacku i na LinkedIn už jsem byl aktivnější než v předchozích týdnech a na vše jsem hned odpovídal.
-   Za 8 dní jsem ujel na kole 52 km. Celkem jsem se hýbal 10 h a zdolal při tom 52 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Dodělat ještě pár detailů na sponzorech, pokračovat konečně v profilech juniorů.
2.  Sepsat plán na Q3 2024.
3.  Koupit knihy do dotazníkové soutěže.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Entering a New Phase of the Web, with Citation Needed’s Molly White](https://flipboard.video/w/ovAsDRovkgbihkZa3wMcUA)<br>Fajn rozhovor s Molly White o webu, internetu, Mastodonu, blogování, sociálních sítích, walled gardens, interoperabilitě a suverenitě, byznys modelech pro tvůrce, Wikipedii…
- [Příprava na 113 tisíc aut za den. ŘSD chystá rozšíření D10, na okraji Prahy chce až 12 pruhů - Zdopravy.cz](https://zdopravy.cz/priprava-na-113-tisic-aut-za-den-rsd-chysta-rozsireni-d10-na-okraji-prahy-chce-az-12-pruhu-210601/)<br>Los Angeles v Praze. Přidáváme pruhy, místo abychom posílili hromadnou dopravu nebo cyklostezky. Dopravní indukce zřejmě neexistuje.
- [Removing ad trackers and cookies  - the technical perspective](https://blog.sentry.io/removing-ad-trackers-and-cookies-the-technical-perspective/)<br>V Sentry sepsali, jak se zbavovali cookies. A pokud na jejich webu nějaké najdete, odmění vás. Docela hustý.
- [Announcement: The Upcoming Version 2.0 Will Be Released Under Dual-License: AGPLv3 License / UAParser.js "PRO" License · Issue #680 · faisalman/ua-parser-js](https://github.com/faisalman/ua-parser-js/issues/680)<br>Interesting and inspirational attempt how to get paid for open source maintenance.
- [I Will Fucking Piledrive You If You Mention AI Again — Ludicity](https://ludic.mataroa.blog/blog/i-will-fucking-piledrive-you-if-you-mention-ai-again/)<br>„Everyone is talking about Retrieval Augmented Generation, but most companies don't actually have any internal docs worth retrieving. Fix. Your. Shit.“ Haha! „Having your team type in import openai doesn't mean you are at the cutting-edge of AI no matter how you embarrass yourself on LinkedIn… Your business will be disrupted exactly as hard as it'd have been if you had done nothing, and much worse than it'd have been if you just got your fundamentals right.“
