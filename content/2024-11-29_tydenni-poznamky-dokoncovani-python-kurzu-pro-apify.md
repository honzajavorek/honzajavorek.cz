Title: Týdenní poznámky: Dokončování Python kurzu pro Apify
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/334
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/113567013555647380

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-11-22_tydenni-poznamky-soutez-o-knihy-a-tyden-pro-digitalni-cesko.md) už utekl nějaký ten týden (22. 11. až 29. 11.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Stará „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md), nová teď nejsou.

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

O víkendu žena nabrala síly u babičky a já s kamarády. Já jsem si to moc užil, fakt jsem se bavil, odpočinul jsem si, a nabilo mě to. Máme teď doma trochu víc životní energie a třeba se nám povede někam posunout věci, které chceme posouvat, a ne jen absorbovat různé rány a sbírat se z nich. Hlavně abychom byli teď aspoň chvíli zdraví.

Pracovní týden proběhl celkem v poklidu. Snažil jsem se soustředit na práci pro Apify, ale nepřetahovat to a mít večer vždy i čas na rodinu a nějaký volný čas. Dařilo se mi trochu i přemýšlet o tom, do čeho bych se chtěl do budoucna pouštět. Je dobré, že si mohu od junior.guru díky Apify zase na chvíli odpočinout, a získat odstup.

![Reggae]({static}/images/img-3059.jpg)

![MIG 21]({static}/images/img-3105.jpg)

## Práce pro Apify

- Udělal jsem review na [tento PR](https://github.com/apify/apify-docs/pull/1283) upravující text o psaní README pro Actory.
- Dotáhli jsme review na mém [předešlém PR](https://github.com/apify/apify-docs/pull/1244/), který přidával dvě nové lekce do kurzu. Byly tam ještě nějaké drobnosti a velké obrázky.
- Pak jsem ještě šel a [optimalizoval i obrázky, které jsem přidával už předtím](https://github.com/apify/apify-docs/pull/1302).
- Zbytek týdne jsem pracoval na [přidání lekce o tom, jak při scrapování použít framework](https://github.com/apify/apify-docs/pull/1303). Zabralo mi to více času, než jsem myslel, protože jsem se trochu zasekl u vymýšlení cvičení. Aby cvičení dávala smysl, musí splňovat spoustu podmínek. Takže jsem zkoušel a zahazoval různé věci, než jsem byl s výsledkem spokojený.

Ještě si sem odložím, čím jsem optimalizoval ty obrázky. Byl to v podstatě jeden příkaz, akorát mi chvíli trvalo na to na něj přijít. Třeba můj oblíbený GIF lopaty přehazující hlínu to stáhlo o 46 %, bez toho, abych vizuálně poznal nějaký rozdíl.

```bash
$ npm x -- @funboxteam/optimizt ~/Projects/apify-docs/sources/academy/webscraping/scraping_basics_python/images/
```

Cítím se trochu divně, že mi jakoby jedna lekce zabrala týden, ale když se ohlédnu, bylo to fakt docela dost vymýšlení, zkoušení, a zahazování věcí, které jsem pak udělal jinak. Takže člověk prostě ve výsledku napíše pár odstavců, ale holt to vážně zabere skoro týden. Nicméně mám radost z toho, jak [kurz postupně roste](https://docs.apify.com/academy/scraping-basics-python) a myslím, že do Vánoc by mohl být hotový, pokud včas dostanu reviews.

![Vánoce v Apify]({static}/images/image-720.png)

## Další

- Propagoval jsem zítřejší (sobotní) [Obsidian workshop v klubu](https://junior.guru/events/47/), který povede [Lucie Lenértová](https://www.youtube.com/watch?v=JyyweqNkdZ0).
- Postupně propaguju i to, že začně [Advent of Code](https://adventofcode.com/), což tradičně vybudí v klubu velkou společnou aktivitu. Připravil jsem věci v klubu, např. vánoční roli.
- Volal jsem si s [Terkou](http://www.popitchimentoring.cz/) a hodinu jsme řešili mou prodejní stránku. Bavili jsme se o výsledcích anket a nakreslili jsme kousek wireframu.
-   Stavil jsem se ke kamarádovi pro reprák. [Nový reprák](https://usa.yamaha.com/products/audio_visual/desktop_audio/wx-030/index.html) je fajn, ale i ta samotná návštěva byla fajn. Stěhuje se a bylo prima si o všem popovídat.
-   Potkal jsem po delší době jiného kamaráda na oběd a taky bylo fajn se vidět a popodívat si.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 8 dní jsem při procházkách nachodil 5 km, na túrách nachodil 7 km. Celkem jsem se hýbal 4 h a zdolal při tom 12 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

Budu pokračovat v dokončování Python kurzu pro Apify, dokud ho nedodělám, abych měl už z tohoto pohledu pro letošek hotovo. Pak si udělám už nějaký konkrétnější plán ohledně toho, co a jak s junior.guru.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [The Ultimate Clever Dripper Technique - YouTube](https://www.youtube.com/watch?v=RpOdennxP24)<br>Ani jsem nevěděl, že Hoffmann má video na metodu přípravy kávy, kterou jsme si doma oblíbili a dá se zvládat i při rodičovském provozu. Když jsem se díval posledně, tak neměl, ale je to 3 roky staré, tak buď jsem se díval špatně, nebo je to už fakt dlouho, co jsem se díval naposled!
