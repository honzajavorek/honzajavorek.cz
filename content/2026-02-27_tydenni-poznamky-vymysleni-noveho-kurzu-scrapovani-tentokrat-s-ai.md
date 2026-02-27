Title: Týdenní poznámky: Vymýšlení nového kurzu scrapování, tentokrát s AI
Image: images/img-0903.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2026-02-23_tydenni-poznamky-seznam-kandidatu-hory-ai-a-mnoho-dalsiho.md) už utekl nějaký ten týden (23. 2. až 27. 2.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Žižka]({static}/images/img-0903.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Nový kurz pro Apify

Tento týden byl můj jeden týden měsíčně pro Apify. Připravujeme nový kurz scrapování, který bude využívat Apify jako platformu a bude se snažit co nejvíce využívat AI. Zatím je v plánu, že ten, kdo tím kurzem projde, nebude muset umět vůbec programovat, tak jsem zvědav, jak a jestli to půjde.

- Něco jsem si vyzkoušel už v předchozích týdnech na [honzajavorek/karolakvido](https://github.com/honzajavorek/karolakvido) a tento týden jsem z toho těžil.
- Dostal jsem review na [opravy cvičení v existujících kurzech](https://github.com/apify/apify-docs/pull/2180), tak jsem to dodělal a mergnul. Opravil jsem ještě i pár věcí v [dodatečném PR](https://github.com/apify/apify-docs/pull/2268).
- Mrknul jsem na to, [jestli existující kurzy správně vysvětlují jednu věc](https://github.com/apify/apify-docs/issues/1900), a zjistil, že ano.
- Začal jsem [tvořit nový kurz](https://github.com/apify/apify-docs/pull/2275). Připravil jsem pro něj místo, nahodil strukturu lekcí, základní popisky, pořadí lekcí, úvod kurzu. Pak jsem přidal ještě první lekci. Tam jsem se pral s nastavením tónu kurzu a s tím, kde nasadím laťku pro studenty, abych nevysvětloval základní práci s počítačem, ale zase abych neopomenul něco, co ani pokročilejší uživatel nezná a je to už spíš doména vývojářů. Prošel jsem několika slepými uličkami, které mi pomohly to vyladit.
- Při tvorbě první lekce jsem chtěl odzkoušet, jestli mnou navrhovaný postup funguje, ale nechtělo se mi rozjíždět Docker apod., abych měl čistý systém bez Node.js aj. vývojářských věcí. Takže jsem si vytvořil nového uživatele normálně ve svém macOS, přihlásil se na něj a na takovéto „čisté instalaci“ jsem odzkoušel sekvenci příkazů z kurzu. Všiml jsem si pár věcí:
    - Poslal jsem [malou úpravu do Apify CLI](https://github.com/apify/apify-cli/pull/1026), aby tam bylo něco kompatibilní i s příkazovým řádkem ve Windows.
    - [Zdokumentoval jsem](https://github.com/apify/apify-cli/issues/1027), že instalace Apify CLI může být pro některé uživatele v některých případech zbytečně složitá.
- Taky jsem strávil dost času tím, že jsem se snažil ChatGPT donutit určitým způsobem editovat soubor s kódem. Bohužel se ChatGPT tvářilo, že soubor v příloze vidí, jenže vůbec, [všechno si cucalo z prstu](https://mastodonczech.cz/@honzajavorek/116136592937021311). Když jsem ale přišel na to, co je příčinou mých frustrací, tak už jsem se ke kýženému výsledku dopracoval docela rychle.
- Dnes jsem se pak ještě během čekání na zpětnou vazbu na kurz vrátil k nějakým starším úkolům a [upravil jsem příklady v existujících kurzech](https://github.com/apify/apify-docs/pull/2293), aby používaly Crawlee router, protože je to přehlednější, a ještě jsem [předělal celé jedno cvičení](https://github.com/apify/apify-docs/pull/2295), protože bylo nespolehlivé.

## Phishing

Stal jsem se obětí phishingu. Vrátil jsem se z oběda, otevřel s plným bříškem e-maily a vidím, že VZP něco chce. Tak klikám a sice to bylo trochu podezřelé, ale ne dost, a než mi došlo, co vlastně dělám, a že to je blbost, už jsem měl odeslané detaily o kartě.

Hned jsem ji zablokoval a nic se nestalo, ale banka mi pak pro jistotu ještě zablokovala úplně všechno ostatní, takže jsem musel na pobočku, musel jsem si vygenerovat nový API token pro všechny svoje integrace s bankovním účtem, a teď jsem dva týdny nebo jak dlouho bez karet. Nicméně vzhledem k tomu, co se mohlo stát, to vlastně dopadlo celé dobře.

A pokud si myslíte, že vám phishing nehrozí, tak hrozí každému. Mně stačilo to, že Gmail tenhle e-mail pustil až do inboxu, což se většinou nestává (docela spolehlivě to padá do spamu), a to, že se to trefilo do mojí chvíle nepozornosti a nebylo to hned dostatečně podezřelé.

Na druhý pohled je ten e-mail úplně jasný, nesedí doména, e-mailová adresa, nic. Stačilo se nad tím na pár sekund pozastavit a hned by to bylo jasné. Ale takhle racionálně to nefunguje vždy a člověk prostě má někdy slabší chvilku.

Nejsem zrovna hrdý na to, že se mi to stalo. Popravdě, připadám si jako debil. Ale od odborníků na bezpečnost stále slýchám, že se to fakt nestává jen důvěřivým dědečkům a babičkám, že se to fakt může stát komukoliv, takže se snažím nepřipadat si jako debil, a ještě to tady schválně takhle veřejně napíšu, abyste i vy všichni ostatní viděli, že se to může stát komukoliv, včetně IT experta s mnoha lety v oboru, který ví jak fungují e-maily, že existuje phishing, a má i nějakou expozici do bezpečnostní komunity.

## Další

-   Mám novou sponzorku na GitHubu! Velký dík, [Karolino](https://github.com/befeleme)! Buďte jako Karolina a [sponzorujte taky](https://github.com/sponsors/honzajavorek) 😀
-   Opravoval jsem scraper na data o kurzech z úřadu práce, kterými se obohacuje [junior.guru/courses](https://junior.guru/courses/). Opravil jsem to, ale vlastně nevím, čím to bylo. Jen jsem aktualizoval pár věcí a opravil doménu, protože ÚP přešel z uradprace.cz na up.gov.cz. Tak možná to bylo tím 🤷‍♂️
-   Co se týče bydlení, během tohoto týdne jsme dostali dispoziční studii a trávili nad ní večery, abychom doladili detaily. Dnes už to asi uzavřeme. Taky jsme sepisovali dopis pro sousedy, aby věděli, co že jsme to za vetřelce a že se z našeho bytu budou celé jaro linout industriální kakofonie.
-   Testoval jsem [Spotube](https://github.com/KRTirtho/spotube), ale je to podobně nedokonalé jako [Psst](https://github.com/jpochyla/psst). Vedle oficiálního Spotify klienta to jsou dohromady tři programy, z nichž každý je bídný jiným způsobem. Krásný výběr 😀
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), upgrady závislostí na všech projektech. Domlouval jsem spolupráci klubu s [mDevCampem](https://mdevcamp.eu/). Zprávy na LinkedIn jsem nestíhal, ale vím, že mi tam víc lidí něco psalo.
-   Naběhal jsem 7 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Nasypu Adéle respondenty na rozhovory, Táni speakery na klubové akce, napíšu sponzorům. Podívám se, na jaké e-maily jsem ještě zapomenul odpovědět. Dám po týdnu zase trochu lásky klubu.
2.  Předělám celou patičku junior.guru a když to půjde rychle, začnu předělávat homepage.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Raghav Agrawal: „He set out to apply the principles of open-sourc…“ - Mastodon](https://mastodon.social/@impactology/116139011890932933)<br>Borec staví základní technologické kameny moderní civilizace jako open source, který lze snadno vyrobit z běžně dostupných dílů… Traktor, dům… „Jakubowski envisions a future in which the GVCS parallels the Linux infra, with custom tools built to optimize agriculture, construction, and material fabrication in localized contexts.“ „Any intelligent fool can make things bigger, more complex, and more violent. It takes a touch of genius—and a lot of courage—to move in the opposite direction.“ „A GVCS tractor costs $12,000 to build, commercial tractor averages ~$120,000 to buy. If you’ve got a wrench, you’ve got a tractor. More than 110 machines had been built by enthusiasts from around the world.“ „Seed Eco Homes are human-sized modular houses complete with a biodigester, a thermal battery, a geothermal cooling system, and solar electricity. Each house is energy independent and can be built in 5 days, at a cost of ~$40,000. Over 8 of these houses exist.“
- [We need to talk about naked mole rats - The Oatmeal](https://theoatmeal.com/comics/naked_mole_rats)<br>Pohlazení v těžkých časech komplikovaného světa.
- [I Asked an AI Chatbot for My Data. I Didn't Expect a Psychological Profile.](https://thelocalstack.eu/posts/ai-chatbot-gdpr-data-request/)<br>Všechno, co pošlete do AI, je zaznamenáno. Poskytovatelé se liší v tom, jak to dělají, ale neliší se v tom, že to dělají, a to i přesto, pokud za službu platíte slušné peníze. U Facebooku nebo Googlu jsme si mohli říkat „když neplatíš, tak jsi produkt“. Tady už jsme produkt i přesto, že platíme. Kapitalismus si ukrojil další kolečko salámu.
- [The Biggest Mistake in the History of Hollywood - YouTube](https://www.youtube.com/watch?v=yN0H_WfWOp4)<br>Pokud si připlácíte za 4K UHD, nejspíš to děláte úplně zbytečně.
- [How will OpenAI compete? — Benedict Evans](https://www.ben-evans.com/benedictevans/2026/2/19/how-will-openai-compete-nkg2x)<br>„You can make the rendering engine better in a browser and you can make the LLM better in a chatbot, but the browser itself, and the chatbot itself, are just an input box and an output box. The ChatGPT app, like all the chatbot apps, is just a ‘thin wrapper’ - how could you make yours different? In browsers, the answer was that you couldn’t - the last successful product innovations were tabs and merging search with the URL bar. Chatbots today have the same problem - how many more little buttons can you add, and how can you tell them apart?“
- [The 30-Mile Barrier Preventing Russia From Taking More of Ukraine | WSJ - YouTube](https://www.youtube.com/watch?v=pls6Btwm6Qo)<br>Doněck.
