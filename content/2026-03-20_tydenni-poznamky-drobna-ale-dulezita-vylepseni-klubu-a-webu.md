Title: Týdenní poznámky: Drobná, ale důležitá vylepšení klubu a webu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2026-03-13_tydenni-poznamky-kutna-hora-brno-a-yak-shaving-vzhledu-webu.md) už utekl nějaký ten týden (13. 3. až 20. 3.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Změna fungování skupinek

Jak jsem už dřív avizoval, bylo potřeba zase upravit fungování zájmových skupinek v klubu. Nakonec to dopadlo takhle:

- `/unfollow` slash command do bota, který umožní lidem snadno a rychle odhlásit se, když ztratí zájem o nějaké téma
- `/follow` symetricky opačný command
- Změnil jsem způsob, jak bot přidává lidi do skupinek. Pod svícnem největší tma! Že mě to nenapadlo dřív. Udělal jsem to přes přímé mentions, takže konkrétní lidi dostanou notifikaci, ale přidají se všichni v jedné krátké zprávě. A tu po sobě bot po čase navíc i sám smaže. Takže zmizí tapetovací spam systémových zpráv a zároveň je notifikace zcela cílená a relevantní. Navíc jsem díky jednomu členovi klubu zjistil, jak něco naformátovat malými písmenky, a hned jsem to použil, aby ta zpráva od bota vypadala jako nativní Discordová „system message“.
- Upravil jsem informační soukromé zprávy, které bot posílá. Upravil jsem všechny možné hlášky a nápovědy, aby odrážely nový způsob fungování skupinek.

Pak stačilo opravit jeden bug, který jsem nedomyslel, a od té doby to funguje novým způsobem a zatím bez ztížností 🙏

![screenshot]({static}/images/screenshot-2026-03-20-at-17-24-56.png)

## Přednáška se Štěpánem

Napsal jsem promo statusy na přednášku se Štěpánem. Zkoušel jsem k tomu využít AI, ale stálo to za prd. Asi bych to musel nějak líp na setupovat, ale to se mi vůbec nechtělo. Myslel jsem, že se to chytne tak dobře, jako se to chytlo nad kódem, ale i když jsem dodal dost kontextu a příklady, tak to bylo mizerné. Takže jsem si to napsal zase sám.

Přednáška proběhla ve středu a kromě zlobící Štěpánovy kamery (která ale nebyla potřeba, důležité bylo co říkal a ukazoval na sdílené obrazovce) nedošlo k žádným technickým potížím. Přišla příjemná skupinka lidí a další se těšili na záznam. Atmosféra byla pěkná, dotazů bylo hodně, takže super.

![Štěpán]({static}/images/20260318-7ff3c43f261ac744bcd617a65d176eff9f0fe96e55c37cdc6f230b7b4e6d9f53.png){: .img-thumbnail }

## Doporučení na klubové stránce

Když vás lidi chválí, tak to sice zahřeje u srdíčka, ale pokud jste jako já, už druhý den zas dál se sklopenou hlavou bušíte na svém podnikání a ani už nevíte, že to proběhlo.

Tak jsem si to před časem posbíral a dal do jednoho dlouhého dokumentu v Obsidianu. To rozhodně pomohlo tomu, abych měl víc zvědomené, že odvádím dobrou práci a můj produkt fakt lidem pomáhá.

Ale hádejte co? Nijak to nepomohlo tomu, aby se to dověděl i kdokoliv jiný! 😀

Tak jsem konečně po letech sedl a nasázel na [klubovou stránku](https://junior.guru/club/) několik nových doporučení, co kolem mně za poslední dobu prolítly. Doteď tam byly zhruba 4, z roku 2019. Teď jich tam bude asi 16 nebo kolik.

Další den jsem k tomu ještě vymyslel o něco lepší design, AI agent to za mně naprogramoval. Kdybych to dělal já ručně, tak to není dodnes. Ještě jsem pak i vylepšil design deníčků, které se na klubové stránce vypisují.

![doporučení]({static}/images/6905eae096da7ca2.png){: .img-thumbnail }

## Diskutovaná témata

Chtěl jsem pokračovat v tom, abych pod stránky příručky mohl dát nějaké informace o tom, jak moc se dané téma diskutuje v klubu. Ale jak jsem to připravoval, napadlo mně, že by se to vlastně dalo nějak využít i na klubové stránce. Takže jsem tam nahodil toto:

![screenshot]({static}/images/screenshot-2026-03-20-at-17-46-48-klub-pro-zacatecniky-v-programovani.png){: .img-thumbnail }

Ty modré boxíky dole tam nebyly. Není to 1:1 ke kanálům na Discordu, to by byl svět příliš jednoduchý. Jsou to nějaké balíky kanálů vždy pro určité téma, a je to seřazené podle toho, jak moc se co probíralo za posledního půl roku. Takže když se něco bude řešit víc, automaticky se to vypíše v jiném pořadí. Nevím, jestli je tohle nejlepší způsob, jak to na webu odprezentovat, ale nepřijde mi to úplně blbé.

Pak jsem teda zapracoval na tom, aby nějaká informace byla i v té patičce pod kapitolami příručky. Zatím jsem vymyslel tohle, můžu ladit do budoucna:

![screenshot]({static}/images/screenshot-2026-03-20-at-17-51-10-jak-na-zivotopis-pro-juniory-v-it.png){: .img-thumbnail }

Je tam nová ta věta, že „Konkrétně v kanálu #cv-github-linkedin se v poslední době napsalo 13.236 písmenek měsíčně.” Upřímně, nevím, jestli 13.236 písmenek měsíčně někomu něco řekne. Ale já nic moc jiného v ruce nemám. Možná to bude působit aspoň tak, že tam je prostě aktivita v tom klubu. Reálné nezaokrouhlené číslo nechávám proto, aby bylo jasné, že jsem si to nevycucal z prstu.

Ještě jsem teď v pátek odpoledne zkoušel, jestli bych tam mohl přidat i třeba dvě tři nějaké bubliny přímo s textem nějakých příspěvků. Nejdřív jsem zkoušel příspěvky, které si lidi připínají špendlíkama. Potom příspěvky s nejvíc pozitivníma reakcema. Ale ani jedno nedávalo dobré výsledky, tak jsem tuhle myšlenku zatím odložil.

Kdyby tam byly reálné ukázky toho, co řešíme v klubu, jistě by to byl pro lidi tahák, ale jak (automaticky?) vybrat vhodné příspěvky? A jak zároveň nekompromitovat určité soukromí v klubu? Těžké otázky. Vrátím se k nim jindy.

## Další

-   Prošel jsem si úkoly na nejbližší měsíce a trochu je promazal a srovnal. Mám teď jasnější priority a snad si zachovám větší tah na (tu správnou) branku i přesto, že při kódění s AI agentem působí každý úkol jako něco, co se dá udělat hned 😅
-   Dal jsem do našeho #ai kanálu v klubu anketu o tom, kolik juniorů už si zkoušelo AI s chatem a kolik s libovolným agentem. Docela zajímavé výsledky, ale ještě zajímavější byla následná diskuze, kde jsme se snažili vymyslet praktické tipy pro dnešní juniory, jak se v aktuální situaci orientovat a kde je minimální laťka, co by měli umět. Mám z toho hodně poznámek pro příručku!
-   Drobná čistění na webu: Odebral jsem z kódu některé partnery, kteří už nejsou partnery. Přidal jsem rámeček tam, kde se mi zdálo, že by rámeček být měl.
-   Věnoval jsem se záležitostem kolem našeho současného bytu, kde se majitelé začínají starat o jeho budoucnost, i kolem našeho nového bydlení, kde se pracuje o sto šest a my sotva stíháme dodávat vstupy a shánět potřebné kontakty a informace na věci kolem domu. Zrovna dnes odhadem tak 15 telefonátů s minimálně 5 lidmi. Taky jsme zajeli do studia s podlahama a koukali na dveře.
-   Poslal jsem daňařovi podklady pro daňové přiznání. Taková jednoduchá věta, a kolik práce to bylo…
-   Zdeněk Koutský na LinkedInu sypal statusy o kariérní situaci na IT trhu doplněné ebookem. Hned se to objevilo v klubu a hned jsem to prolítl, abych viděl, co tam píše a co doporučuje. Hned jsem na to pak reagoval: [tady](https://www.linkedin.com/feed/update/urn:li:ugcPost:7439358346345738241?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7439358346345738241%2C7439610021107240960%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287439610021107240960%2Curn%3Ali%3AugcPost%3A7439358346345738241%29) a [tady](https://www.linkedin.com/feed/update/urn:li:activity:7440035392243920896?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7440035392243920896%2C7440101552004128768%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287440101552004128768%2Curn%3Ali%3Aactivity%3A7440035392243920896%29). Překvapila mě vlna reakcí, které se mnou souhlasily. Možná to opravdu s tou situací juniorů není tak špatné! Vzalo mi to ale dost času, který jsem myslel, že využiju na jiné věci.
-   Kamarád v klubu inzeroval pracovní nabídku pro juniory, tak jsem mu malinko pomáhal to tam vložit.
-   Staral jsem se o soutěž na lístky na mDevCamp. Bylo to napínavé, protože lidi moc nesoutěžili, ale nakonec se „vylosovat“ výherkyni povedlo. Mikromanagement téhle soutěže mi ale zabral trochu víc času, než jsem doufal.
-   Volal jsem si s Terkou Palaščákovou a dali jsme si po dlouhé době update o tom, jak se kdo máme. Následně jsem po delší době nakoukl do její komunity pro contenťáky a napadlo mě napsat [Eriku Lerchovi](https://eriklerch.cz/), který je tam aktivním členem, abych prozkoumal zas nějakou novou cestu ve věci „potřebuju aby junior.guru vydělávalo víc“. Zavoláme si za týden.
-   Pokazilo se mi [film2trello](https://github.com/honzajavorek/film2trello/), asi protože ČSFD.cz se začali zase nějak bránit proti botům. Dal jsem tomu malou chvilku opravování, ale pak jsem to nechal být, protože na to nemám čas. A nemám čas ani sledovat filmy.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech.
-   Za 8 dní jsem naběhal 10 km. Celkem jsem se hýbal 3 h a zdolal při tom 10 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1. Můj březnový Apify týden.
2. Udělat v klubu soutěž o Java učebnici od Pavla Ponce.
3. Řešit bydlení.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Astral to join OpenAI](https://astral.sh/blog/openai)<br>Oooops!
- [Why ATMs didn’t kill bank teller jobs, but the iPhone did](https://davidoks.blog/p/why-the-atm-didnt-kill-bank-teller)<br>Tohle bylo hodně zajímavé čtení. V kontextu toho, kam by mohlo směřovat AI v IT jde o jednu z nejzajímavějších analogií, kterou jsem v poslední době četl. „When a technology automates some of what a human does within an existing paradigm, even the vast majority of what a human does within it, it’s quite rare for it to actually get rid of the human, because the definition of the paradigm around human-shaped roles creates all sorts of bottlenecks and frictions that demand human involvement. It’s only when we see the construction of entirely new paradigms that the full power of a technology can be realized. The ATM substituted tasks; but the iPhone made them irrelevant.“
- [AI-Written Code: Armin Ronacher on AI Agents and the Future of Programming [Full Episode] - YouTube](https://www.youtube.com/watch?v=4zlHCW0Yihg)<br>Hodně zajímavý rozhovor s Arminem na téma agentů a AI, ale i na spoustu dalších témat, která se teď týkají našeho oboru. Je to z loňského EuroPythonu, takže červen 2025, ale Armin byl dost napřed, takže mluví o věcech, které lidi často objevují až teď.
- [AI And The Ship of Theseus](https://lucumr.pocoo.org/2026/3/5/theseus/)<br>„…it combines two very heated topics, licensing and AI, in the worst possible way.“
