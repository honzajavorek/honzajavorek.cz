Title: Týdenní poznámky: Testování scrapovacích cvičení a přípravy nového kurzu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 8 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/370
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115905959376368892

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2026-01-09_tydenni-poznamky-vanoce-a-tak.md) už utekl nějaký ten týden (9. 1. až 16. 1.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

V minulých poznámkách jsem se zamyslel nad budoucností junior.guru a nastínil, že bych letos potřeboval otočit trend. Pak jsem tam napsal, spíš ze vtipu, že kdo chce, ať [pošle LOVE](https://junior.guru/love/), a světe div se, tři lidi fakt poslali 🙀 Když jsem to viděl, tak mě to fakt dojalo. Dohromady teď mám přes GitHub Sponsors o $29 měsíčně víc, než před týdnem.

Když sponzorujete přes GitHub Sponsors, jde tam nastavit, že to nejde veřejně vidět, takže ne všichni mí sponzoři jdou veřejně vidět a tím se komplikuje, abych jim tady veřejně poděkoval 😀 Každopádně ale všem svým sponzorům moc děkuji, vaše podpora mi dodává sílu pokračovat. A koho by zajímalo, kdo sponzoruje veřejně, tak [tady je seznam](https://junior.guru/about/sponsors-partners/#github-sponsors).

Jinak tento týden jsem pracoval pro Apify, takže dnešní report je především o tom. Shrnutí v bodech:

- Prošel jsem všechny zprávy a e-maily, odpověděl jsem tady strašně milému borcovi @adamtheturtle pod [apify/apify-docs#2027](https://github.com/apify/apify-docs/pull/2027) a řešil další věci. Ověřil jsem, že [apify/apify-docs#2023](https://github.com/apify/apify-docs/pull/2023) lze zavřít.
- Opravil jsem část kódu v Python kurzu: [apify/apify-docs#2171](https://github.com/apify/apify-docs/pull/2171)
- Zařídil jsem si review [apify/apify-docs#2097](https://github.com/apify/apify-docs/pull/2097), mergnul to a založil [apify/apify-docs#2181](https://github.com/apify/apify-docs/issues/2181) do budoucna. Teď máme otestovaná cvičení ke kurzu! Testy se spouští jednou měsíčně. Uvidíme, jak to bude vypadat 1. února.
- Testy už našly několik rozbitých cvičení. V tomto týdnu jsem je opravil a vytvořil [apify/apify-docs#2180](https://github.com/apify/apify-docs/pull/2180). Při práci na opravách jsem narazil na bug v Crawlee [apify/crawlee-python#1673](https://github.com/apify/crawlee-python/issues/1673) a taky jsem založil [apify/apify-docs#2183](https://github.com/apify/apify-docs/issues/2183) do budoucna.
- Začal jsem analyzovat a připravovat nový kurz: nejdřív call s Tomem a Patrikem, pak jsem vytvořil [apify/apify-docs#2174](https://github.com/apify/apify-docs/issues/2174), přidal analýzu AI nástrojů k použití a navrhl osnovu lekcí. Na té budeme ještě příště trochu vyšívat.
- Udělal jsem review na [apify/apify-docs#2130](https://github.com/apify/apify-docs/pull/2130).

Po delší době jsem si taky potrénoval spolupráci v týmu, tzn. čekání na něco, připomínání se, domlouvání se, slaďování představ, apod. Jsem z toho po týdnu nějaký vyčerpaný, hurá zpět do samoty podnikání v jednom člověku 🤣

## Opravy cvičení

Pracoval jsem dost na testování kódu cvičení a opravování těch cvičení, která se stihla už rozbít. Některá cvičení byla o tom, že člověk stáhne stránku z Wikipedie a najde tam nějakou informaci, jenže Wikipedie se ukázala jako nespolehlivá – dost často scrapování zablokuje.

Což je v pořádku, ale já potřebuju, aby si studenti kurzu mohli věci osahat trochu v reálu, takže jsem pak hledal jiné weby, kam lze udělat jednotky nesofistikovaných školních requestů, které projdou, a zároveň které umožňují procvičit to, co se člověk v lekci naučil. To je kvůli všudypřítomým ochranám a dynamicky načítaným webům čím dál složitější. Zároveň potřebuju, aby to byly nějaké celosvětové a neutrální věci.

V tomhle se docela osvědčil sport a naopak se moc neosvědčily mezinárodní instituce. Takže tam mám nově cvičení s [tenistkami](https://www.wtatennis.com/), ale weby UNESCO, Mezinárodního měnového fondu, apod. jsem vzdal, protože to mají na nějakých strašně složitých CMSkách, které nejspíš generují jednu stránku na základě stovky dotazů do databáze a když jsem se snažil stáhnout jedinou stránku, odpověď trvala snad 60 sekund a dostával jsem často timeouty, ačkoliv jsem nedělal nic zatěžujícího.

## Nový kurz scrapování, tentokrát s AI

Nový kurz, který připravujeme, by měl být o tom, jak si člověk může vytvořit scraper s pomocí AI. Docela se na to těším, protože mě to donutí mnohem víc namočit si čumák ve vývoji asistovaném AI a do agentů, ale nejdřív musíme vyladit, pro koho přesně ten kurz bude a jak bude strukturovaný.

Každopádně už přípravy kurzu byly zajímavé. Na jeden krátký prompt v ChatGPT jsem dostal výsledek, ke kterému se student v předchozích kurzech propracovává několik lekcí. A to jsem se nesnažil. Kdybych předhodil nějaké slušné zadání agentovi, tak by to nejspíš zvládl vytvořit celé.

Je otázka, co má dnes smysl do detailu učit a co ne. Každopádně fakt, že můžu do kurzu napsat něco jako „pokud se ti nepovedlo správně nasetupovat vývojové prostředí, tak to oddebuguj s AI“, to mi teda vůbec nevadí! To je jedna fakt velká bolest z krku.

Taky se mi v hlavě rodí hodně myšlenek kolem toho, že kdybych dnes stavěl projekt na zelené louce, úplně přesně vím, jak bych to udělal, aby to bylo AI-friendly. Vlastně bych hned od začátku dělal spoustu věcí, které vedou k tomu, že je projekt junior-friendly, docs-first a tests-first. Jenže zatímco dřív by se nevyplatily, dneska by jejich hodnota byla díky AI agentům okamžitá.

## Schůzky

Během týdne jsem stihl hned dva obědy:

- S [Davidem](https://www.linkedin.com/in/dmajda/) jsme si popovídali o životě a o práci. Práci teď aktivně hledá, takže komu by se hodil ostřílený senior, máte jedinečnou šanci po něm chňapnout. David má úžasné znalosti a zkušenosti, viděl už všechno možné a v podstatě cokoliv je schopen se doučit. Myslím, že by zvládl roli elitního génia, který něco vymýšlí – už v roce 2014 jsem ho zval [přednášet na brněnské Pyvo o překladačích](https://pyvo.cz/brno-pyvo/2014-04/) – ale i tech leada, který dokáže odřídit [správu produktu po úvodní kolonizační fázi](https://honzajavorek.cz/blog/kolonizatori-a-spravci-kolonii/), kdy už je jasnější market fit a chtělo by to stabilní jádro. Pokud děláte na něčem, co se do světa snaží přidat trochu dobra, třeba to zbržďuje klimatickou změnu, tak je to příjemný bonus.
- S [Miou](https://www.linkedin.com/in/mia-bajic/) jsme si taky popovídali o životě a o práci, ale pak hlavně o tom, že by možná mohl vzniknout film o české Python komunitě. A jestli jsme schopni tomu přispět, a jak, a jestli jsme schopni najít další lidi, kteří by nám pomohli to realizovat.

Taky jsem si měl volat s [Terezou](https://www.linkedin.com/in/terezia-palascakova/), ale já to trochu zazdil, tak jsme si potom jenom psali. Poslali jsme si updaty co se komu povedlo, čím ve svých byznysech žijem a o co se snažíme, a probrali pak některé detaily.

## Další

-   Pozval jsem [Adélu](https://www.linkedin.com/in/adelapavlun/) do klubu a zadal jí první práci na rozhovoru. [Táni](https://www.linkedin.com/in/t%C3%A1%C5%88a-v%C3%A1chov%C3%A1-512981330/) jsem vysvětlil, co potom bude potřeba co se týče výběru a „dramaturgie“ rozhovorů do budoucna. Hned si na to udělala tabulku. Do publikace ji zaučím, až bude co publikovat.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech. Po Vánocích jsem oživil myšlenku životního pojištění, takže jsem si psal s pojišťováky a žhavil ChatGPT, aby mi vysvětlilo všechny „termity“ a porovnalo nabídky.
-   Byli jsme na dni otevřených dvěří ve spádové ZŠ. Sice se nás tohle bude týkat až za rok, ale říkali jsme si, že možná nebude na škodu si udělat nějakou představu už v předstihu, kdy nám je to zatím tak trochu jedno a nejsme z toho ve stresu. Nasáli jsme atmosféru a bylo to zajímavé. Prostory a vybavení mi přisly hodně viditelně podfinancované. Náplň a přístup mi přišly moderní, dobře promyšlené a s jasně nastaveným vzestupným trendem a s ředitelem, který se fakt snaží dělat věci dobře.
-   StartupJobs opravili export hned ještě minulý pátek, a psali mi hned asi hodinu po tom, co jsem vydal poznámky (tzn. v noci).
-   Přidal jsem do katalogu popis pro [Coders Lab](https://junior.guru/courses/coderslab/). Asi není vyčerpávající, ale to důležité tam snad je. Neočekávám, že z toho budou nadšení, ale kdo co seje, to i sklízí 🤷‍♂️ A jo, vím, že takhle si u mně asi sponzorství nekoupí 😅 Jenže junior.guru je tu v první řadě pro juniory a nemůže tyhle věci prostě přehlížet.
-   Za 8 dní jsem se nevěnoval žádné sportovní aktivitě.

## Plánuji

1.  Budu propagovat [Artemovu přednášku](https://junior.guru/events/58/).
2.  Podívám se na dotazník spokojenosti, který Táňa udělala pro online akce na junior.guru.
3.  Zdražím o klub pro nově příchozí.

A pak odjedu na prodloužený víkend na hory.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [European alternatives for popular services | European Alternatives](https://european-alternatives.eu/alternatives-to)<br>Alternativy nejsou nic moc, ale je fajn vědět, po čem v případě nouze sáhnout. Snad to nebude zapotřebí někdy velmi brzy.
- [Speciál: Startupy a značky, o kterých jste netušili, že jsou evropské](https://filipmolcan.substack.com/p/special-startupy-a-znacky-o-kterych?publication_id=992952&post_id=182945971&isFreemail=true&r=1d6l57&triedRedirect=true)<br>V Evropě inovovat umíme a možná byste se divili, kolik IT věcí, které běžně používáte, je ve skutečnosti z Evropy. I mne některé položky překvapily, např. že ElevenLabs jsou z Polska, nebo Wise z Estonska.
- [Pluralistic: The Post-American Internet (01 Jan 2026) – Pluralistic: Daily links from Cory Doctorow](https://pluralistic.net/2026/01/01/39c3/#the-new-coalition)<br>Hodně aktivistické, hodně od podlahy, hodně Cory Doctorow 😀 A hodně zajímavé! Docela sleduju věci kolem big tech monopolů, centralizaci internetu a tak, ale že by se to dalo rozbít něčím, co se jmenuje 'anti-circumvention law', a že tenhle zákon všude existuje hlavně díky tomu, že si to prosadily USA, to jsem teda netušil. (Na odkazu najdete video Coryho talku a i jeho přepis)
- [Don't fall into the anti-AI hype](https://antirez.com/news/158)<br>„Yes, maybe you think that you worked so hard to learn coding, and now machines are doing it for you. But what was the fire inside you, when you coded till night to see your project working? It was building. And now you can build more and better, if you find your way to use AI effectively. The fun is still there, untouched.“
- [I often hear Americans & rich brits justify buying oversized, polluting vehicles by claiming they need them because they live in the "countryside". I call bullshit, Ladies and Gentlemen, allow me to introduce, the Citroen C15](https://eupolicy.social/@jmaris/115860595238097654)<br>Nejlepší vlákno o SUVčkách ever 😀 „Ask yourself, reader, do you need to carry anything larger than multiple cows?“
