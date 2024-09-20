Title: Týdenní poznámky: Scrapování v Pythonu a vylepšování nabídek práce
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/328
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/113170135811776128

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-09-06_tydenni-poznamky-srpen-dovolene-sponzori-nove-cisla-a-grafy-nove-pracovni-inzeraty.md) už utekl nějaký ten týden (6. 9. až 20. 9.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Stará „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md), nová ještě nejsou.

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Píšu po dvou týdnech, protože ten první týden jsem celý věnoval psaní kurzu scrapování v Pythonu v rámci svého kontraktu s Apify.

## Kurz scrapování v Pythonu

Kromě různé režie a drobností jsem během svého „Apify týdne“ udělal tohle:

- Konečně jsme mergnuli [výkop kurzu scrapování v Pythonu](https://github.com/apify/apify-docs/pull/1197)! Výsledek je [tady v  Apify Akademii](https://docs.apify.com/academy/scraping-basics-python). Zatím je to jen pár lekcí, ale budu postupně přidávat další. Kdo byste si to chtěli projít, budu moc rád za jakoukoliv zpětnou vazbu.
- Konečně jsme mergnuli dvě velké úpravy napříč celou Akademií: [odstranění zmínek, že něco má být jednoduché](https://github.com/apify/apify-docs/pull/1201) a [oprava některých odkazů](https://github.com/apify/apify-docs/pull/1202). Tohle byly příliš velké změny, jejich review zabralo příliš mnoho času a musel jsem je několikrát rebasovat. Takové velké změny už nesmím dělat.
- [Opravil jsem jeden existující návod](https://github.com/apify/apify-docs/pull/1108), aby reflektoval změny, které mezitím proběhly, nebo do budoucna ještě proběhnou.
- Napsal jsem [lekci o ukládání dat](https://github.com/apify/apify-docs/pull/1205).
- Napsal jsem [lekci o následování odkazů](https://github.com/apify/apify-docs/pull/1214).

Kurz scrapování jsem pak sdílel na [LinkedInu](https://www.linkedin.com/feed/update/urn:li:activity:7239882990082822144/), [Mastodonu](https://mastodonczech.cz/@honzajavorek/113117962966123324), na [FB Pyonieri](https://www.facebook.com/groups/pyonieri/posts/8532530260092409/) a [FB Programátoři začátečníci](https://www.facebook.com/groups/144621756262987/posts/1544344902957325/).

![Kurz scrapování]({static}/images/screenshot-2024-09-20-at-14-48-00-web-scraping-basics-for-python-devs-academy-apify-documentation.png){: .img-thumbnail }

## Kino

Občas si odběhnu do kina. Chodím tam sám, je to příjemný relax. V blízkosti domova mám 2-3 kina, z toho jedno je multiplex, do kterých nechodím, pokud nemusím. Ještě o zastávku dál jsou další 2 malá kina, ale to už je jakoby „daleko“. Ve výsledku se stále dívám na tytéž dva programy a kopíruju si do kalendáře kdy co je, kdybych náhodou měl čas si odskočit do filmové temnoty během náročného týdne.

No a protože už mě to kopírovíní nebaví, jal jsem se vytvořit [kino](https://github.com/honzajavorek/kino). Ještě to není hotové, ale myšlenka je, že si scrapnu ty dva programy a vygeneruju z toho živý `.ical` export, který si dám přímo do kalendáře. Přesně a pouze s těmi informacemi, které potřebuji.

No a když už Apify vydalo to Crawlee pro Python, rozhodl jsem se to použít a napsat to v tom. Výsledkem mého snažení jsou zatím tyto issues na GitHubu:

- [O formátování JSONu](https://github.com/apify/crawlee-python/issues/526)
- [O architektuře scraperu a dependency injection](https://github.com/apify/crawlee-python/issues/525)
- [O architektuře scraperu a sdílení již nascrapovaných informací mezi handlery](https://github.com/apify/crawlee-python/issues/524)

## Vylepšování nabídek práce

Jako poslední na světě jsem doposlouchal [Levelse u Lexe](https://lexfridman.com/pieter-levels/).
Nakoplo mně to a i když byl můj pracovní týden kvůli rýmičkám rozházenější, než by mi bylo příjemné, dokázal jsem pracovní čas využít naplno.
Zkusil jsem si taky k práci pouštět techno a je to super, baví mě to 😀

Vytvořil jsem na [inzerátech](https://junior.guru/jobs/) zbrusu nové filtrování přes hashtagy. Nejdřív jednoduché, ale hned druhý den jsem ho vylepšil a [rozdělil hashtagy do třech kategorií](https://mastodonczech.cz/@honzajavorek/113164727554201322), které se filtrují jakoby zvlášť (AND vs. OR).

![Filtrování]({static}/images/screenshot-2024-09-19-at-16-34-33.png){: .img-thumbnail }

Do výpisu inzerátů jsem [nechal zobrazit](https://mastodonczech.cz/@honzajavorek/113160549894754983) i inzeráty, které někdo ručně vložil do klubu. Nejdřív byly zamíchané mezi ostatní nabídky, ale to vlastně moc dobře nefungovalo, zvlášť s těmi filtry. Taky odkaz vedl prostě na Discord a pro lidi by to nejspíš bylo dost matoucí. [Vytvořil jsem tedy nejprve dialog](https://mastodonczech.cz/@honzajavorek/113165056501100331), který po kliknutí upozorňuje, že odkaz míří na Discord a že je potřeba účet a přístup do klubu. A pak jsem tyhle inzeráty [úplně vyčlenil](https://mastodonczech.cz/@honzajavorek/113169490278084395) a dal je pod ty stažené z internetu. Zobrazil jsem u nich i kolik mají lajků a komentářů, nebo iniciály člověka, který je do klubu vložil.

[Nepoužil jsem žádný JS framework](https://mastodonczech.cz/@honzajavorek/113160505453107251) a napsal jsem asi jen 120 řádků JS celkem. I přesto si připadám jako kouzelník. Filtrování! Dialog!

S tímhle mám velké plány. Chci totiž s klubem víc propojit i ty stažené pracovní inzeráty. Tohle je jen začátek! Mám z vytvořených věcí ohromnou radost. Docela mě bavilo to tvoření průběžně dokumentovat na Mastodonu a bavit se tam o tom s lidmi (viz všechny ty odkazy průběžně v textu). Nakonec jsem se pochlubil i na [LinkedIn](https://www.linkedin.com/posts/honzajavorek_inzer%C3%A1ty-na-junior-guru-maj%C3%AD-nov%C4%9B-i-filtrov%C3%A1n%C3%AD-activity-7242856835391569920-iIVV/).

![Inzeráty]({static}/images/screenshot-2024-09-20-at-13-19-23-prace-pro-juniorni-programatory-a-testery.png){: .img-thumbnail }

![Dialog]({static}/images/screenshot-2024-09-20-at-12-44-02.png){: .img-thumbnail }

![Ručně vložené inzeráty]({static}/images/screenshot-2024-09-20-at-12-43-53-prace-pro-juniorni-programatory-a-testery.png){: .img-thumbnail }

## Další

-   Pozvali mně na snídani komuniťáků do panelu, budu si tam s Gabi Řehoutovou z Mews vykládat o… komunitách, překvapivě. Odkaz třeba [tady na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7239262808142467074/). Přijďte!
-   Byl jsem v sauně.
-   Volal jsem si po delší době s [Terkou](http://www.popitchimentoring.cz/), která mi pomáhá s prodejní stránkou klubu.
    Já jí zase pomáhám rozjet její komunitu pro copywritery a contenťáky.
    Musím už ukončit a vyhodnotit ty dotazníky, ale tento týden na to nebyla energie.
-   Z internetu zmizel web cybermagnolia.com, kde ale byly dobré články a rozhovory.
    Opravil jsem odkazy tak, že jsem tam dal verzi na [web.archive.org](https://web.archive.org/).
-   Opravil jsem jak se můj kód kolem nabídek práce vypořádá s typem úvazku „jiné“.
    Opravil jsem chybu při buildění scraperů.
    Opravil jsem buildění [seznamu kanidátů](https://junior.guru/candidates/) po tom, co se tam přidal někdo z lidu, kdo nemá účet v klubu.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 15 dní jsem naběhal 30 km, při procházkách nachodil 10 km. Celkem jsem se hýbal 6 h a zdolal při tom 40 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Běhat, protože [PMK](http://blanenskypulmaraton.cz/) se blíží.
2.  Natočím video na sociální sítě a určím datum, kdy ukončím dotazníky.
3.  Udělám jednotlivé pracovní inzeráty rozklikávací a dám tam kromě tlačítka vedoucího na URL inzerátu i tlačítko, které povede do klubu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [d&d is anti-medieval](https://www.blogofholding.com/?p=7182)<br>Dračák není středověk, ale Divoký západ: „…the D&D rules seem to be explicitly eschewing a medieval, feudal model in favor of a cash-based economy, a nonexistent or powerless government, and a social-classless society in a sparsely inhabited, unforgiving world.“ „But it’s very difficult to write a document with no cultural assumptions at all. Gygax consciously excluded the trappings of a medieval society, and filled that vacuum with “real life” American details.“
- [Vojtko: S dítětem i feministky spadnou do tradičních rolí — Chyba systému](https://www.mujrozhlas.cz/rapi/view/episode/7d1656e5-0234-35f8-8abf-f2d245d06fb6)<br>Tohle je hodně silná epizoda. Novináři a terapeut… Apolena Rychlíková přizná, že taky jednou přišla z práce a po manželovi, který byl celý den s dětmi, chtěla navařeno a uklizeno. David Klimeš přizná, že pracuje i o víkendech a nedokázali doma dokončit audit férové domácnosti. Spousta zajímavých postřehů, z makro hlediska rodinné politiky státu i z mikro hlediska soužití v rodině.
- [Why GitHub Actually Won](https://blog.gitbutler.com/why-github-actually-won/)<br>Proč GitHub zvítězil a začali jej používat všichni? Názor spoluzakladatele. Malé cameo tam má i Česko.
- [Nestojíme o vaše plyšáky aneb Jak vypadá skutečná pomoc obětem přírodních katastrof - VOXPOT: reportáže, které spojují Česko se světem](https://www.voxpot.cz/?p=26166)<br>Jak správně pomáhat obětem katastrof. https://www.voxpot.cz/nestojime-o-vase-plysaky-aneb-jak-vypada-skutecna-pomoc-obetem-prirodnich-katastrof-2/
- [Why are female wizards called "witches"?](https://english.stackexchange.com/questions/182876/why-are-female-wizards-called-witches)<br>„Even nowadays, if one reads these lines: John is a secretary. Mary is a secretary. There will be plenty of people assuming that John sits on a board or a committee, while Mary is a personal assistant.“ https://english.stackexchange.com/a/182883/333222
- [I Will Fucking Haymaker You If You Mention Agile Again — Ludicity](https://ludic.mataroa.blog/blog/i-will-fucking-haymaker-you-if-you-mention-agile-again/)<br>Tak jsem si zas přečetl Ludicity, tentokrát o „agile“. Boží. Tyhle články vyvolávají podobně smíšené pocity jako videa od KRAZAM. Mám se smát, nebo plakat?
- [Duny zisku. Z pašovaného písku stavíme i v Evropě - VOXPOT: reportáže, které spojují Česko se světem](https://www.voxpot.cz/duny-zisku-z-pasovaneho-pisku-stavime-i-v-evrope/)<br>Zajímavý report o tom, jak se nelegálně těží, krade a pašuje písek. A že může i dojít.
- [Proč je Josef Pepa?](https://www.procje.cz/josef-pepa)<br>„Odvozenina Pepa se k nám dostala z italštiny, kde je Josef Giuseppe. Giuseppe se v italštině zkracuje jako Beppe a odtud už je blízko k našemu Pepovi.“
- [Nový dokument o mladé generaci Ukrajinců - 10. září - Studio 6 | Česká televize](https://www.ceskatelevize.cz/porady/1096902795-studio-6/224411010100910/cast/1065931/)<br>Pusťte si tuhle reportáž ČT. Chtěli s Nikou natočit komentář, ale než to stihli, zabila ji raketa.
- [WebP: The WebPage compression format](https://purplesyringa.moe/blog/webp-the-webpage-compression-format/)<br>Nemám na takové věci čas a nejspíš ani inteligenci, ale je fascinující si o tom číst: Komprese textové webové stránky pomocí WebP, obrázkového formátu.
- [Green Notebook from Frutigen-Niedersimmental](https://joesaward.wordpress.com/2024/09/04/green-notebook-from-frutigen-niedersimmental/)<br>Zajímavé počty ve Formuli 1: „Time will tell, but one way or another, Red Bull is in danger of losing the Constructors’s title. Financially-speaking, losing the sponsorship that follows Perez might be worse than losing the prize money, but the problem with this argument is that racing people like winning and even if the books balance, the team does not want to be second.“
