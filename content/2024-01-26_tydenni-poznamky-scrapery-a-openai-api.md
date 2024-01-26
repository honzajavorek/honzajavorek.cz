Title: Týdenní poznámky: Scrapery a OpenAI API
Image: images/img-7403.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/305
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111822679943390987

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-01-19_tydenni-poznamky-hory-a-scrapery.md) už utekl nějaký ten týden (19. 1. až 26. 1.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/img-7403.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)
</div>

## Apify na produkci

Dokončil jsem [přesun scraperů na Apify](https://github.com/juniorguru/plucker), opravil jsem jeden zásadní scraper, a pak jsem na Apify připojil produkci junior.guru.
Pracovní inzeráty se stahují z Apify API, místo aby se scrapovaly přímo u mně.
[Výsledný Pull Request](https://github.com/juniorguru/junior.guru/pull/1285) odebral z kódu junior.guru skoro 21.000 řádků kódu a přidal 230.
To mi dělá ohromnou radost.

O jednotlivostech se asi nemá smysl moc rozepisovat.
Řešil jsem monitoring, cachování, no různé věci.

Klukům z Apify jsem dál koukal pod ruce, otravoval je na Discordu, a [dokonce jsem se zapletl do jednoho code review](https://github.com/apify/apify-sdk-python/pull/178/).

## OpenAI API

Po přesunu scraperů jsem hned začal napojovat junior.guru na OpenAI API.
Chci pracovní inzeráty posílat GPT na vyhodnocení.
To se mi povedlo hned, s krásnými výsledky, jenže pak začala bitva o _rate limiting_.
Abych projel stovky inzerátů, nasázel je do GPT a dostal výsledky, potřebuju se nějak vlézt do limitů, které mi OpenAI dává.
[A to byl problém](https://mastodonczech.cz/@honzajavorek/111811236793735383).

Zkoušel jsem knihovnu [openlimit](https://pypi.org/project/openlimit/), která plus minus fungovala, ale nebyla v dobré kondici.
Musel jsem ji instalovat z nějakého forku apod.
Nakonec jsem to [podle návodu přímo od OpenAI](https://cookbook.openai.com/examples/how_to_handle_rate_limits) předělal na [tenacity](https://pypi.org/project/tenacity/), což je pěkné, obecné řešení.

Ale stále to ještě ladím.
Hloupé je, že to párkrát spustím a je konec, dosáhnu limitu 10.000 požadavků na den.
Takže někdy na tom prostě musím v půlce přestat pracovat, jít dělat jiné věci, a pokračovat druhý den.

Jsem už schopen projet všechny inzeráty a dostat se na konec skriptu, ale celé to trvá 10 minut, což je příšerné.
Možná to tak ale budu prostě muset dělat.
Leda že bych našel [alternativní API](https://replicate.com/), kde to funguje jinak.

## Další

-   Sepsal jsem konečně [článek, kde jsou mé aktuální plány]({filename}2024-01-25_plan-na-q1-2024.md).
-   Měl jsem rýmu a některé dny jsem pracoval z postele.
-   Byli jsme na LEGO výstavě.
-   Optimalizoval jsem, jak se v mém kódu pracuje s _asyncio loops_.
    Místo procesů jsem vrazil vlákna a hned je vše rychlejší.
-   Řešil jsem, jak udělat _progress bar_, když mám hromadu _asyncio tasků_ a posílám je do _asyncio.gather()_.
    Našel jsem [toto milé řešení](https://superfastpython.com/asyncio-tasks-show-progress/), ale nakonec jsem to udělal stejně jinak (přes _asyncio.as_completed()_).
-   Připravil jsem podklady pro zpracování daňového přiznání.
    Když už jsem lezl do všech účtů a stahoval dokumenty, spočítali jsme si s manželkou, kolik máme celkem peněz, což několikrát ročně děláme.
-   Podíval jsem se na nespárované platby ve Fakturoidu a spároval je.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 8 dní jsem se nevěnoval žádné sportovní aktivitě.

## Plánuji

1.  Doladím nějak třídění inzerátů přes LLM.
    Ideálně pak smažu veškerý kód, který řeší třídění inzerátů teď.
2.  Přidám podporu pro slovenštinu.
3.  Vyberu a naplánuju klubové přednášky na rok 2024.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [59: Ladislav Miko: Půda je živý organismus — 2050](https://audioboom.com/posts/8427357)<br>Fakt borec, jak to dokáže podat! Parádní povídání o půdě, jak to v ní funguje, co v ní žije, a tak. Půda mě nijak zvlášť nevzrušuje, nemám ani zahrádku, ale tohle jsem si vážně užil.
- [Jak jsme z těžítek udělali užitečné notebooky pro žáky - Python v ČR bloguje](https://blog.python.cz/jak-jsme-z-tezitek-udelali-uzitecne-notebooky-pro-zaky)<br>„Předem připravený návod na reinstalaci, ochota si maximálně pomáhat, dobrá káva a skvělá organizace celé akce udělaly z různorodé skupinky lidí, z nichž se někteří viděli úplně poprvé, dobře organizovanou pracovní sílu s jasným cílem, který se dařilo velice rychle plnit.“ „Až na pár strojů, které budou ještě vyžadovat speciální péči, se celá akce vydařila na výbornou a co bylo zbytečným těžítkem ve skříni, už opět slouží žákům.“ Síla Python komunity v praxi!
- [Stuff we figured out about AI in 2023](https://simonwillison.net/2023/Dec/31/ai-in-2023/)<br>Simon sepsal pěkné shrnutí toho, co jsme za rok 2023 zjistili o AI (respektive LLM)
- [Tallow to Margarine](https://www.scopeofwork.net/tallow-to-margarine/)<br>Zvířecí lůj. Najdete ho ve spoustě plastů, i v nových plastových bankovkách. A jak vlastně vznikl margarín?
- [Glow up krajní pravice. Stavidla nenávisti otevřelo 11. září 2001 — PULS](https://podcasters.spotify.com/pod/show/jolana-humplov/episodes/Glow-up-krajn-pravice--Stavidla-nenvisti-otevelo-11--z-2001-e2ejnvr)<br>Hodinová přednáška o krajní pravici, o jejím vzniku, důvodech vzniku, strategii, a o tom, proč je na vzestupu.
- [Výsledky práce společenských věd jsou dnes potřeba naléhavěji než přírodovědné objevy a technické vynálezy](https://denikn.cz/1329656/zbytecne-skodlive-naopak-spolecenske-vedy-a-absolventy-jejich-studia-potrebujeme-vic-nez-si-mnozi-uvedomuji/?cst=19c2e920f19e8e352de71a0b93cbab16ec5355b8c541245cca7a369adc42b4fd)<br>„Hlavní problémy lidstva dnes nevyřeší přírodní ani technické vědy samy o sobě. Můžete vymyslet sebelepší vakcínu proti pandemii, ale co je to platné, když se jí lidé bojí a odmítají ji? Můžete navrhnout mnoho dílčích technických řešení zmírňujících klimatickou krizi, ale k čemu jsou, když je neprosadíte proti krátkodobým zájmům velké části lidstva?“ „Společnost, nikoli příroda či technika, je dnes nejnaléhavější záhadou.“
