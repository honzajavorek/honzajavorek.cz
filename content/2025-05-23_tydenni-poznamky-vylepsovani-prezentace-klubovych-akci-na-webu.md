Title: Týdenní poznámky: Vylepšování prezentace klubových akcí na webu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-05-19_tydenni-poznamky-svatky-na-morave-prevazne-s-apify.md) už utekl nějaký ten týden (19. 5. až 23. 5.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Klubové akce na webu

Tento týden jsem se snažil hlavně vylepšit prezentaci klubových akcí na webu, tedy stránku [junior.guru/events](https://junior.guru/events/) a její podstránky.

Nejdřív jsem si udělal náčrtky na papír, jak by to mělo vypadat, a co všechno by tam mělo být. To mi hodně pomohlo ujasnit si myšlenky.

Věděl jsem, že budu určitě chtít data o tom, jak je který záznam dlouhý. Takže jsem to šel nějak zjišťovat z YouTube. To si vyžádalo dost změn v kódu junior.guru a přidání části, která projede odkazy na přednášky a podívá se, jak jsou dlouhé.

Má zkušenost velí, že jakmile je někde API, které má složité přihlašování, jako třeba to od Googlu, bývá někdy rychlejší a jednodušší si tu věc scrapnout. Takže první verzi jsem udělal pomocí `yt-dlp`, které je v Pythonu a lze použít i jako knihovna, a umí stahovat i pouze metadata. Fungovalo to skvěle přesně do chvíle, než jsem to dal na produkci a zjistil, že YouTube blokuje IP adresy mého CI, takže se build nepovede. Musel bych s tím za nějakou proxy, třeba na Apify, a to už by byla zase komplikace.

Takže jsem hodil ručník do ringu a šel na to přes YouTube API. Nadechl jsem se, jak bude složité vyřešit auth, ale pak jsem zjistil, že můžu použít totéž co už používám u stahování dat z Google Sheets a stačí dva řádky kódu a frčí to 😀 Tak jsem to přepsal a už to funguje. Teď mám u každého záznamu i data o jeho délce a další detaily.

Pak jsem vylepšil výpis akcí. Přidal jsem tam tlačítka jako na stránce pro podcast, včetně iCalendar exportu, a pak mě napadlo přidat tam i tým za akcemi, když už to nedělám sám. Přidal jsem nově i odkazy na LI, ať z toho něco mají, když už mi pomáhají v dobrovolně. Samotný výpis jsem pojal jinak, než to bylo a využil komponentu na kartu, která se používá pro různé odkazy napříč junior.guru.

Ten iCalendar export jsem měl už dlouho pro vlastní potřebu, ale vlastně nebyl nikdy na webu pro ostatní, ani nevím proč. Trochu jsem ho vylepšil, aby obsahoval víc informací.

Jenže co do obrázku? Samotné obličeje přednášejících vypadaly divně a karty jako čtverečky taky. Když jsem tam dal plakátek s namalovaným tlačítkem, vypadalo to taky divně. Tak jsem vygeneroval pro každou přednášku ještě i plakátek bez tlačítka a to bylo hned lepší. CSS jsem upravil tak, aby byly karty širší a přepsal jsem ho z flexu a marginu na CSS grid. Teda přepsalo to ChatGPT spíš, já jsem se s tím nepatlal 😀

S výpisem jsem teď docela spokojený, teď bych měl dodělat ty podstránky, ty jsou příšerné. Bude to dost práce, protože přednáška se může nacházet v různých stavech (plánovaná, proběhlá, s veřejným záznamem, se záznamem jen pro členy…) a zároveň bych chtěl, aby z těch stránek bylo zřejmé, o co jde, jak se člověk může připojit, atd. Chci tam _call2action_ do klubu. Uf.

![Nové /events/]({static}/images/screenshot-2025-05-23-at-20-00-48-online-akce-pro-zacatecniky-v-programovani.png){: .img-thumbnail }

## Další

-   Napsal jsem do dvou firem, jestli prodlouží sponzorství. Jedna napsala, že neprodlouží (což jsem trochu tušil), u druhé čekám na odpověď.
-   Propagoval jsem [Beginners' Day Unconference](https://mastodonczech.cz/@honzajavorek/114558198633271824). Na LinkedInu vyjde status v neděli večer, ale už je naplánovaný.
-   Domlouval jsem tři lidi do panelovky v rámci [Beginners' Day Unconference](https://mastodonczech.cz/@honzajavorek/114558198633271824), takže zprávy, maily, a tak.
-   Byl jsem na delší dobu naposledy na fyzioterapii. Je to na dobré cestě.
-   Zlobilo mně generování náhradních obrázků s počátečními písmenky pro pracovní inzeráty, kde chybí logo firmy. Taky jsem si všiml, že u StartupJobs nemám loga, protože mají v exportu špatné odkazy na loga a napsal jsem jim. Proč zlobí to generování nevím, začal jsem víc logovat v kódu, který to řeší, ale je to divné - někdy to projde, jindy se to zasekne na dlouho a CI timeoutuje 🤷‍♂️
-   Do katalogu jsem přidal na Vláďovu žádost [Scripteo](https://junior.guru/courses/scripteo/).
-   Patrik dodal záznam Štěpánovy přednášky a Táňa skvěle zvládla všechny následné úkoly - napsat do oznámení, editovat YAML, atd.
-   Řešil jsem nějaký [bug s Lychee](https://github.com/lycheeverse/lychee/issues/1709). Dělali [nějaké změny v kontrole fragmentů](https://github.com/lycheeverse/lychee/pull/1675) a funguje mi to teď nějak zvláštně.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Dohnal jsem nějaké maily, které delší dobu čekaly, ale pořád je tam ještě tak 10 dalších, které už trochu hnijou. Klub jsem po delší době zase skoro celý přečetl.
-   Za 5 dní jsem naběhal 3 km. Celkem jsem se hýbal 1 h a zdolal při tom 3 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Pokračovat v překopávání webu pro klubové akce.
2.  Napsat návod pro seniory - jak mohou v klubu pomáhat, jak se mohou zapojit.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Duševní zdraví a hraní. Počítačové hry vás mohou s dětmi sblížit i ublížit — Balanc](https://www.mujrozhlas.cz/rapi/view/episode/e1e9a8c1-9775-32fc-957d-d61efa8c174c)<br>Pěkný pokec o tom, jaký efekt mohou mít hry a jak s tím jako rodič pracovat
- [Pocket is saying goodbye - What you need to know | Pocket Help](https://support.mozilla.org/en-US/kb/future-of-pocket)<br>Byla jen otázka času, kdy se to stane. Už před lety to nemělo žádné nové fičury, neopravovalo žádné bugy, přišlo mi to v kómatu na přístrojích. Takže jsem přešel jinam. A teď Pocket končí.
- [Peter Hanecak (@phanecak@mastodon.social)](https://mastodon.social/@phanecak/114552785464573897)<br>„Slovenka porazila aj mužov, v Himalájach vyhrala jeden z najťažších triatlonov na svete. Dokázala to ako prvá žena v histórii. Trénuje v Bratislave popri práci a hovorí, že nie je vrcholová športovkyňa. V Nepále však dosiahla prelomový úspech.“
