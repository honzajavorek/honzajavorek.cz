Title: Týdenní poznámky: Zaučování v Apify a klid před bouří
Image: images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří pracovat na [junior.guru](https://junior.guru/) a dalších věcech?
Od [posledních poznámek]({filename}2026-09-04_tydenni-poznamky-odpocivani-a-nove-starty.md) už utekl nějaký ten týden (4. 9. až 18. 9.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Víkend v Blansku u kamaráda byl super. Sranda, zábava, dospělí, děti, sluníčko, hraní na kytaru, pivo, zpěv, řev, dobroty, sport, a ještě jsme se omylem objevili i na „Zažít Blansko jinak”. Vypnul jsem v mozku všechny starosti a bylo mi dobře.

Uplynulé dva týdny se jinak nesly hlavně v duchu zaučování se do rozšířeného pracovního úvazku pro Apify. Během toho jsem stíhal různé práce i na junior.guru, ale moc jsem to nehrotil. Do toho se mi povedlo potkat dost lidí, nových i starých, různě na obědech a na kafíčkách. Taky jsem před týdnem zvládl skvělou páteční Apify párty – kolaudačku nových kanclů, kde jsem potkal spoustu nových zajímavých lidí, ale i starých známých, což mi udělalo velkou radost.

I když jsem práci na junior.guru nehrotil, takže jsem technicky měl míň než 100% úvazek, tak mi přišlo, že se od rána do večera stejně nezastavím, protože s novým školním rokem na mě spadla většina cest do školky a ze školky, přičemž cestu ze školky většinou, částečně dobrovolně, přetavím prostě v odpoledne s dcerou a doma jsme až na večeři.

Čas s dcerou si užívám, protože už dokáže spoustu věcí, které mě baví, a ještě u toho vtipně hláškuje. Třeba jsem s ní zkusil dojet na kole do školky a zpět, což je 5+km jedna cesta, a měl jsem velkou radost z toho, že jsme to bez zádrhelů dokázali. Moc rychle jsme nešlapali, prudké kopce jsme šli pěšky, a bylo to zhruba stejně rychlé, jako to jet tramvají 😆

Za chvíli ale budeme čtyři a s miminem začne úplně jiný kolotoč. Takže jsem do titulku napsal „klid před bouří”, ale vlastně si už ani neumím představit, jak ta bouře bude vypadat, jenom tuším, že něco jako bouře asi přijde. Za těch pět let už jsem kolem mimin všechno úspěšně zapomněl. Na jednu stranu je to dobře, protože díky tomu mám odvahu do toho jít znova 😆 ale možná by se hodilo i trochu vědět co a jak. No, to se nějak vstřebá.

## junior.guru

Probíhalo hlavně (úspěšné) shánění speakerů na přednášky pro další měsíce. Kromě toho nejrůznější průběžné opravy:

-   [junior.guru#1734](https://github.com/juniorguru/junior.guru/pull/1734) – Add location rewrite rule for České Budějovice
-   [junior.guru#1736](https://github.com/juniorguru/junior.guru/pull/1736) – Fix dead umimeto.org research link in handbook
-   [junior.guru#1738](https://github.com/juniorguru/junior.guru/pull/1738) – Make pin storage idempotent
-   [junior.guru#1739](https://github.com/juniorguru/junior.guru/pull/1739) – Retry Discord read timeouts
-   [junior.guru#1742](https://github.com/juniorguru/junior.guru/pull/1742) – New template for easier copy paste
-   [junior.guru#1743](https://github.com/juniorguru/junior.guru/pull/1743) – Add retry logic to geocoding API calls
-   [junior.guru#1745](https://github.com/juniorguru/junior.guru/pull/1745) – Add lib/retrying with project defaults over tenacity

## Automatizace postování na sociální sítě

Snažil jsem se do [crowing](https://github.com/juniorguru/crowing) přidat podporu pro popisky reelsek, abych je nemusel vymýšlet. Všechno se dalo vzít přímo z podkladů pro video, tzn. z webu junior.guru, ale hashtagy bylo nutné vždy vymyslet. Napadlo mě, že bych mohl v subprocesu zavolat Claude CLI s promptem a nechat si je vygenerovat, čímž obejdu API, které se platí přes tokeny a ne přes předplatné. Funguje to.

Horší je to s postováním na sítě. Myslel jsem, že bych automatizoval postování na YouTube, Instagram, a tak, ale většina těch sítí podobnou automatizaci strašně komplikuje. Nedává smysl si to programovat (ani s AI). Automatizace přes browser taky nedává smysl, protože bych to stále jen opravoval. Pak jsou služby, které to řeší a daly by mi jedno souhrnné upload API, ale ty jsou zase mířeny na velké ryby a jsou na můj vkus hrozně drahé. Vzalo mi to vítr z plachet a spolu s mizivým ROI dosavadního postování na sítě mě přestalo bavit na tom dál dělat.

## Apify

Velkou část těch dvou týdnů jsem strávil nad _onboarding checklistem_ a pak nad sepisováním _white paperu_ o tom, kam by měla směřovat Apify Academy do budoucna. Sledoval jsem nejrůznější videa o tom, jak se co v Apify dělá, kam Apify míří, jaká je strategie, jaké jsou priority… Kromě toho jsem dodělával dvě lekce pro připravovaný kurz na základě připomínek v _code review_ a ještě jsem stihl tohle:

-   [apify-docs#2984](https://github.com/apify/apify-docs/pull/2984) ([#2979](https://github.com/apify/apify-docs/issues/2979)) – Kódím do dokumentace novou komponentu na zobrazování promptů
-   [apify-docs#2972](https://github.com/apify/apify-docs/pull/2972) – Čištění zbytečností
-   [apify-docs#2954](https://github.com/apify/apify-docs/pull/2954) – Review nějakých změn kolem dokumentace Docker imagů
-   [apify-docs#2955](https://github.com/apify/apify-docs/pull/2955) – Review změn kolem adaptivních SVG obrázků

## Používání skillů

V Apify jsem si všiml, že s agentama používají skilly, tak jsem se konečně rozhoupal přečíst si, co to přesně je a jak se to používá. Zjistil jsem, že jsem něco podobného už sám dávno vynalezl, akorát jsem si to pojmenoval „guidelines” a vyvolával to na sílu přes AGENTS.md/CLAUDE.md. Takže jsem šel a na junior.guru to předělal na skilly rovnou: [junior.guru#1735](https://github.com/juniorguru/junior.guru/pull/1735), [junior.guru#1737](https://github.com/juniorguru/junior.guru/pull/1737)

## Další

-   Šel jsem na očkování proti covidu. Překvapilo mě, že to bylo zadarmo.
-   Byl jsem na obědě s několika kamarády. Byl jsem na zmrzlině v Apify a potkal u toho zajímavé lidi. Byl jsem na párty v Apify, nonstop jsem si tam s někým povídal, a přišel jsem domů kolem 3 ráno. Byl jsem na kafíčku v [Diversight](https://www.diversight.ai/).
-   Konečně jsem dostavěl PAX skříně v ložnici. Navštívil jsem při tom jedno svérázné žižkovské železářství, kde mi dobře poradili, jak mám opravit něco, co se mi tak úplně nepodařilo. Výsledek je pěkný a vypadá tak, jak jsme chtěli, včetně pár hacků oproti tomu, co IKEA ve výchozí verzi umožňuje. Celá stavba mi zabrala pár týdnů (čistého času pár dnů, samozřejmě). Bylo to epochálnější, než jsem čekal.
-   Oslavili jsme v rodině decentně další narozeniny.
-   Objevil jsem [Camoufox](https://camoufox.com/).
-   Opravoval jsem rozbitý „czap” scraper: [czap#39](https://github.com/honzajavorek/czap/pull/39), [czap#41](https://github.com/honzajavorek/czap/pull/41)
-   Opravil jsem jeden test na svojem blogu: [honzajavorek.cz#423](https://github.com/honzajavorek/honzajavorek.cz/pull/423)
-   Přidal jsem si do AdBlocku pravidla, která vyblokují otravné výzvy Slacku, abych jej měl nainstalovaný jako aplikaci a nepoužíval jej v tabu prohlížeče 🤷‍♂️
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. 23 upgradů závislostí na všech projektech.

## Plánuji

1.  Dodělávat AI kurz a dál plánovat co s Apify akademií do budoucna.
2.  Dokončovat onboarding v Apify.
3.  Udržovat junior.guru. Sepsat na blog, co bude s junior.guru dál.
4.  Připravovat sebe a byt na příchod mimina.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Keynote: Was, Is, Will Be: Python History, Software Engineering, And AI Our Way - Paul Everitt - YouTube](https://www.youtube.com/watch?v=F7pc-YxxZAc)<br>Paul Everitt na EuroPython keynote přichází s plánem, jak vzít AI do vlastních rukou.
- [Lightning Talks - Saturday May 16, 2026 PM - YouTube](https://www.youtube.com/watch?v=VA3O7UxuZO4&t=872s)<br>Pěkný lightning talk (celkem 5 min, odkaz vede přímo na začátek v rámci delšího streamu) o tom, jak mluvit ve skupině lidí. Vychází to z Pac-Man Rule pro konference, že lidi v kroužku vždy mají nechat místo i pro někoho dalšího, akorát je to převedeno na čas.
- [Europe Won’t Live By Deporting | Dark Thoughts](https://dark.ronacher.eu/2026/7/17/live-by-deporting/)<br>„An ambitious young European who leaves for the US, and an ambitious person abroad who decides not to come in the first place, are both losses we seem strangely unwilling to take seriously …those people are not leaving because of a Syrian immigrant on the street, but because they find better starting conditions elsewhere. In fact, the same fundamental forces that make a Syrian leave to Europe, makes a European move to the US or Dubai.“
- [Čím míň Romka, tím líp. Film Pramen o nucených sterilizacích selhává – VOXPOT: reportáže, které spojují Česko se světem](https://www.voxpot.cz/clanky/cim-min-romka-tim-lip-film-pramen-o-nucenych-sterilizacich-selhava)<br>Chtěli natočit film o Romech, ale pak si uvědomili, že je vlastně o Romech, takže to nakonec udělali raději o někom úplně jiném.
- [Ed Zitron's AI prediction track record](https://danluu.com/zitron/)<br>V začátku jsem Eda Zitrona četl a párkrát i sdílel. Pak jsem ho přestal číst, protože byl na můj vkus příliš naštvaný. Kopal do všeho kolem sebe a přišlo mi, že se AI fakt zlepšuje a on to ignoruje. Raději jsem se šel podívat, jak to teda funguje, co se s tím dá dělat, a jak a v čem mi AI může pomoct. A teď Dan Luu (známý tím, že si všechno rád propočítá, než něčemu začne věřit) publikoval tohle, kde se podíval na různá Zitronova tvrzení…
