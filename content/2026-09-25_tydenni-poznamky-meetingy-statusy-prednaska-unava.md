Title: Týdenní poznámky: Meetingy, statusy, přednáška, únava
Image: images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Description: Týdenní poznámky! Jak se mi daří pracovat na junior.guru a dalších věcech? Tentokrát je to na 11 min čtení 🧐
Telegram-Comments: https://t.me/honzajavorekcz/389
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/117331992256178141

Jak se mi daří pracovat na [junior.guru](https://junior.guru/) a dalších věcech?
Od [posledních poznámek]({filename}2026-09-18_tydenni-poznamky-zaucovani-v-apify-a-klid-pred-bouri.md) už utekl nějaký ten týden (18. 9. až 25. 9.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Byl to takový zvláštní týden. Když jsem viděl, kolik meetingů mě čeká v Apify, tak jsem naznal, že to sežere celý ten půlúvazek a nic jiného ani neudělám. V druhé půlce času jsem žongloval různé věci kolem junior.guru a chození do školky, ze školky, a jiné rodinné záležitosti.

Dcera měla nějakou rýmu, tak zůstala pondělí a úterý doma. Docela dobře jsme se domluvili, ona si hrála a já jsem pracoval, takže pohoda. Pak začala zase chodit do školky, jenže ta rýma mezitím skočila na ženu a mně taky začalo být divně.

Ale zabral jsem a zvládl vše, co bylo potřeba. Všechny meetingy do Apify, večerní přednášku v klubu… chodil jsem úplně zničený spát už v deset, ale v noci jsem se vždycky kvůli něčemu probudil a pak nemohl usnout, i když jsem pořád ještě byl zničený. Takže každé ráno totální zombie. Chvílemi jsem měl knedlík v krku nebo ucpaný nos a chvílemi zase vůbec.

A do toho všeho mě nenapadlo nic lepšího, než každou volnou chvilku vyplnit tím, že popoženu AI agenty, aby na něčem vyšívali.

Vlastně nějak nedokážu říct, jestli na mě opravdu něco leze, nebo to je z nějakého stresu, nebo co to vlastně je. Těším se, až dneska přijdu domů, lehnu si a nebudu prostě chvíli nic muset dělat. Třeba si přes víkend víc odpočinu a samo to nějak odejde.

Nejspíš už příští týden se nám může narodit mimino, ale že bych na to byl teď nějak skvěle připravený co se týče nabitých baterek, to teda úplně ne, no 😵‍💫

## junior.guru

Začal jsem si sepisovat text o tom, kam by mohlo směřovat junior.guru, a bylo to smutné čtení. Uspořádal jsem si u toho ale myšlenky a vlastně mě to trochu, spolu s odstupem, který si od léta postupně dělám, nakoplo.

Rozhodl jsem se místo psaní smutných textů začít pracovat na pár věcech, které by mohly pomoct.

První z nich je přidání AI do štítků v pracovních nabídkách. To se mi povedlo a teď jsou na [junior.guru/jobs](https://junior.guru/jobs/) čtyři nové štítky: #ai, #agenticengineering, #buildingai, #vibecoding

Když už jsem se vrtal v detekci technologií z textu, tak jsem při tom udělal i hodně dalších oprav v knihovně beak, která to řeší:

-   [Fix C language detection to exclude C# and C++](https://github.com/juniorguru/beak/pull/108)
-   [Honor the mapping argument in beak()](https://github.com/juniorguru/beak/pull/109)
-   [Emit tags in deterministic sorted order](https://github.com/juniorguru/beak/pull/110)
-   [Remove dead databáze regex pattern](https://github.com/juniorguru/beak/pull/111)
-   [Drop stale rule_template ruff exclude](https://github.com/juniorguru/beak/pull/112)
-   [Expose public API from jg.beak package root](https://github.com/juniorguru/beak/pull/113)
-   [Use re.Pattern\[str\] instead of deprecated typing.Pattern](https://github.com/juniorguru/beak/pull/114)
-   [Update copyright year to 2026](https://github.com/juniorguru/beak/pull/115)
-   [Convert from Poetry to uv (src layout, Python 3.13)](https://github.com/juniorguru/beak/pull/116)
-   [Add AI detection: chat, agents, build, vibecoding tags](https://github.com/juniorguru/beak/pull/118)
-   [Move tag-matching rules into a declarative mapping.toml](https://github.com/juniorguru/beak/pull/119) ([#117](https://github.com/juniorguru/beak/issues/117))
-   [Guard-rail tests for mapping.toml (+ sort rules, simplify \w-ending rules)](https://github.com/juniorguru/beak/pull/120)
-   [Consolidate mapping logic and cache default rules](https://github.com/juniorguru/beak/pull/121)
-   [Move AI tags into TechTag and rename AI hashtags](https://github.com/juniorguru/beak/pull/122)
-   [Support Beak AI tags in Discord and website job listings](https://github.com/juniorguru/junior.guru/pull/1753) ([#1750](https://github.com/juniorguru/junior.guru/issues/1750))
-   [Sharpen the main job board’s search presentation](https://github.com/juniorguru/junior.guru/pull/1755)
-   [Fix indentation in jobs page lead text](https://github.com/juniorguru/junior.guru/pull/1767)

Založil jsem pár issues o věcech, které mě při tom všem napadly:

-   [Handbook: add an "AI without code" angle to the no-code page](https://github.com/juniorguru/junior.guru/issues/1747)
-   [Add AI job analysis](https://github.com/juniorguru/junior.guru/issues/1754)
-   [Make the jobs_scraped relevance prompt AI-aware (agents / vibecoding / AI-assisted coding)](https://github.com/juniorguru/junior.guru/issues/1749)
-   [Switch job-posting classification to GPT-5.6 Luna](https://github.com/juniorguru/junior.guru/issues/1756)

Ty poslední jsou o tom, že bych upravil prompt, kterým filtruju nabídky práce, a možná že bych vyměnil i model, kterým se to dělá. Jenže abych to mohl udělat a mohl u toho sledovat, jak to pohlo s výsledky, potřebuji nějaký "eval", a ten nemám. Takže jsem ho začal dělat (začal jsem se učit jak mám něco takového vůbec udělat), ale pak mě zavalily bugy a už jsem se k tomu nedostal:

-   [Create an offline eval for the jobs_scraped LLM relevance prompt](https://github.com/juniorguru/junior.guru/issues/1748)
-   [feat(jobs): add offline eval for llm_opinion relevance prompt](https://github.com/juniorguru/junior.guru/pull/1757)

Co se týče věcí, které se náhodně rozbily, tak šlo o různé odkazy, network retries, scrapery… a taky optimalizaci použávání Fakturoid API, protože moje naivní implementace žrala moc API requestů:

-   [Add retry logic to geocoding API calls](https://github.com/juniorguru/junior.guru/pull/1743)
-   [Exclude sifrovacky.cz from link checking](https://github.com/juniorguru/junior.guru/pull/1746)
-   [Link PyCon SK card to pycon.sk again](https://github.com/juniorguru/junior.guru/pull/1764)
-   [Add lib/retrying with project defaults over tenacity](https://github.com/juniorguru/junior.guru/pull/1745)
-   [Fix close button alignment on wrapped job titles](https://github.com/juniorguru/junior.guru/pull/1752) ([#1751](https://github.com/juniorguru/junior.guru/issues/1751))
-   [Add --todos-since filter for Fakturoid todos sync](https://github.com/juniorguru/junior.guru/pull/1762) ([#1761](https://github.com/juniorguru/junior.guru/issues/1761))
-   [Restore Firefox as the screenshot browser](https://github.com/juniorguru/crowing/issues/7)
-   [Fix followers scraper: Facebook wording changed from "sledujících" to "sledující"](https://github.com/juniorguru/plucker/pull/176) ([#175](https://github.com/juniorguru/plucker/issues/175))

Taky jsme s Táňou přidávali detaily k narychlo připravované přednášce a já jsem si přidával poznámky k příručce:

-   [Revise event details for Martin Rapavý's talk](https://github.com/juniorguru/junior.guru/pull/1760)
-   [Fix malformed event entry from PR #1758](https://github.com/juniorguru/junior.guru/pull/1759)
-   [Handbook notes](https://github.com/juniorguru/junior.guru/pull/1744)

Dnes jsem dál přemýšlel nad tím, co by mohlo junior.guru v současné chvíli pomoci, a zaměřil jsem se na to, že jedna z mála věcí, které na junior.guru rostou, je počet automatických zpětných vazeb na GitHub profil.

Vypadá to, že vychází moje předtucha, že v současné situaci je potřeba nabídnout nástroje a ne obsah. Akorát že můj nástroj sice funguje, ale nepřivádí lidi do klubu. Takže dvě malé úpravy, aby jednak přiváděl, jednak abych mohl lépe sledovat, co přesně se děje a co by mohlo mít smysl řešit:

-   [Invite to the club in GitHub profile check results](https://github.com/juniorguru/eggtray/pull/446)
-   [Track GitHub profile check form submissions](https://github.com/juniorguru/junior.guru/pull/1766)

Jsem tak trochu uprostřed všech těch analýz, ale zatím mi krystalizuje něco takovéhoto:

-  Vylepšit junior.guru/jobs, protože to roste a chodí tam lidi (je to _tool_, ne _content_). Přidat tam AI, přidat upoutávky na klub.
-  Přidat výsledkovou stránku pro automatické kontroly GitHub profilů. Ty taky rostou, lidi to používají stále více. Opět, je to _tool_, ne _content_. Výsledková stránka bude přímo na junior.guru na webu, lidi nebudou zbytečně odcházet z webu pryč, když už jsem je tam dostal, a budu mít plně pod kontrolou, jak tam vypadá upoutávka na klub.
-  Předělat junior.guru/love, přidat tam obyčejný QR kód, zrušit nabídku firemních tarifů (nechat firmy prostě ať mi napíšou a že se nějak domluvíme).
-  Nabídnout kurzům, že budou mít free vstup do klubu pro absolventy, aspoň na měsíc. Nebudou za to nic platit. V současné situaci nejspíš win-win, a je to cílovka nejcílovkovatější.
-  Nabídnout referral program, kdy pokud někdo z klubu doporučí někoho dalšího, dostanou oba měsíc zdarma.
-  Připomínat kandidátům na junior.guru/candidates, že se mají stát členy klubu a proč, pokud jimi ještě nejsou.
-  Vymyslet, co bude s příručkou. Její rozvoj je dále neudržitelný. Dá ohromnou práci ji tvořit, ale čtou si ji už jen AI scrapery. Google mi na příručku lidi už neposílá, stránky přesně tohoto typu jen sešrotuje do svých AI shrnutí, takže jako lákadlo do klubu to už vůbec nefunguje. Příručka navíc významně zastarala. Začít ji teď přepisovat je splachování mojí energie do záchodu. Nejspíš z ní stále mám nějaký rank důvěryhodnosti na Google a jinde, ale možná to nejlepší, co s ní můžu v tuhle chvíli udělat, je nějakým způsobem ji zaarchivovat a nic nového už nepřidávat.
-  Co se týče rad, které by dříve skončily v příručce, největší smysl by dávalo natočit je na video a postovat to na YouTube kanál. Tam search ještě funguje a lidi na edukativní videa dál koukají. Zapomenout na to, že to budu někde nějak udržovat a aktualizovat, prostě dělat kdyžtak novější videa.

Co myslíte, jsou to rozumné kroky? Je to sice svým způsobem smutné, ale vlastně si dovedu docela dobře představit, že by junior.guru bylo hlavně o nástrojích a komunitě, a ne o příručce. Stejně ji vůbec nezvládám doplňovat a psát a když už pracuju na junior.guru, baví mě nakonec spíš to programování. Umím si představit třeba rozšířit automatickou zpětnou vazbu, a doplnit tam podporu pro LinkedIn nebo i PDF CVčko. To by mě bavilo dělat. Ale když si představím, že přepisuju příručku, tak mě jímá úzkost z toho, jak nekonečný projekt to je. A v roce 2026 nejspíš i zbytečný, nebo minimálně nerentabilní.

## Přednáška v klubu

V klubu jsme měli [přednášku s Martinem Rapavým](https://junior.guru/events/65/). Bylo to dost narychlo. Nedokázali jsme včas sehnat někoho na září, tak se sám přihlásil, že by mohl udělat intro do jazykových modelů, jaké dává lidem na školení v bance, kde pracuje. Přišlo mi to super. Tak jsme to rychle uplácali, přednášku oznámili, a báli se, jestli vůbec někdo přijde. Nebo jestli nebude u nás doma porod a nebude tam ve čtvrtek večer Martin sám, bez moderátora.

Vyšlo to nakonec dobře. Udělal jsem ještě rychle statusy na sociální sítě a upoutávky na přednášku v klubu, a přišlo nakonec skoro 20 lidí, což je moc pěkná účast. Technické problémy nebyly, moje zdraví mě na chvíli podrželo, Martin povídal dobře a dobře se to poslouchalo, dotazů byla spousta, takže paráda.

Kdo jste nebyli, určitě si to pusťte ze záznamu, stojí to za to!

## Camoufox a osobní projekty

Ze dne na den CSFD.cz nahodilo nějakou brutální ochranu proti scrapování včetně Anubis a přestaly mi fungovat dva hobby projekty pro osobní potřebu, „film2trello” a „kino”.

U obou by mi bylo líto, kdybych to musel zaříznout, tak jsem tomu dal šanci a poštval na to AI agenty. Opravit se mi to podařilo, ale sežral jsem tím svůj týdenní příděl tokenů za jediný den.

Nechal jsem na tom AI pracovat průběžně, zatímco jsem se snažil dělat i jiné věci, ale neustálé přepínání kontextu mě teda dost vyčerpávalo.

Naučil jsem se ale zase nové věci. Použil jsem poprvé [Camoufox](https://camoufox.com/) a optimalizoval jsem oba projekty tak, aby na CSFD.cz chodily co nejméně.

Asi nemá smysl zabrušovat do detailů, každopádně ta práce je tady: [film2trello#349](https://github.com/honzajavorek/film2trello/pull/349), [film2trello#350](https://github.com/honzajavorek/film2trello/pull/350), [film2trello#351](https://github.com/honzajavorek/film2trello/pull/351), [film2trello#352](https://github.com/honzajavorek/film2trello/pull/352), [film2trello#353](https://github.com/honzajavorek/film2trello/pull/353), [film2trello#355](https://github.com/honzajavorek/film2trello/pull/355) ([#354](https://github.com/honzajavorek/film2trello/issues/354)), [film2trello#358](https://github.com/honzajavorek/film2trello/pull/358), [film2trello#359](https://github.com/honzajavorek/film2trello/pull/359), [film2trello#360](https://github.com/honzajavorek/film2trello/pull/360) ([#357](https://github.com/honzajavorek/film2trello/issues/357)), [kino#88](https://github.com/honzajavorek/kino/pull/88), [kino#89](https://github.com/honzajavorek/kino/pull/89), [kino#90](https://github.com/honzajavorek/kino/pull/90), [kino#91](https://github.com/honzajavorek/kino/pull/91), [kino#92](https://github.com/honzajavorek/kino/pull/92), [kino#94](https://github.com/honzajavorek/kino/pull/94), [kino#95](https://github.com/honzajavorek/kino/pull/95) ([#93](https://github.com/honzajavorek/kino/issues/93)), [kino#96](https://github.com/honzajavorek/kino/pull/96)

Po tom, co jsem si vyzkoušel Camoufox s vestavěným AdBlock Origin, napadlo mě, že bych to mohl použít i na screenshoty v příručce, kde mám teď hromadu kódu na to, aby na screenshotech nešly vidět různé cookie lišty apod., tak jsem si do budoucna založil ještě tohle issue:

- [Screenshotter: use Camoufox's bundled uBlock Origin instead of a hand-maintained HIDDEN_ELEMENTS list](https://github.com/juniorguru/junior.guru/issues/1765)

Jen aby bylo jasno, chodit někomu na web a stahovat si z tama informace je legální, nota bene pokud je to pro vlastní potřebu. Jeden ten projekt používáme jen já a žena, abychom si trackovali co jsme viděli, a druhý je program několika pražských kin obohacený o další data, který mám přímo v Google Kalendáři, abych věděl, kam můžu jít spontánně do kina, když na to mám zrovna čas. CSFD.cz se brání proti scraperům jiného kalibru, proti konkurenci, proti AI shrnutím, a kdo ví čemu všemu. Moje hobby projekty jsou v téhle válce jen collateral damage. Takže nemám žádný morální problém s tím, když ty jejich ochrany obejdu.

## Apify

Tento týden jsem svůj poloviční úvazek zaplnil meetingy. V pondělí jsme řešili, co bude dál s Akademií, v úterý dělali roadmapu pro celý dokumentační tým, ve středu 1-1, a ve čtvrtek i v pátek dopoledne sada přednášek v rámci onboardingu.

Chce se mi věřit, že tohle se jen tak sešlo a k tomu ještě dobíhá ten onboarding, takže do budoucna to takhle vypadat nebude. Mnoho z toho je jen jednou za čas, nebo pouze jednou za kariéru v Apify 😅

Každopádně kromě výše uvedeného jsem už stihl jen pár ne příliš podstatných drobností.

## Další

-   Promoval jsem přednášku s Martinem Rapavým v klubu. Promoval jsem pak i FrontKon, protože jsem jim to ještě slíbil za tu soutěž o lístky.
-   Postavil jsem věšák a botník. Vybral a koupil jsem vysavač.
-   Byl jsem u holiče a s kamarádem Tomem na obědě a na kafi.
-   Vylepšili jsme s dcerou polystyrenovou loď do vany, má teď nákladní prostor a kabinu.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. 11 upgradů závislostí na všech projektech. Domlouvání přednášek. Aktuálně domlouváme na leden.

## Plánuji

1.  Připravovat sebe a byt na příchod mimina.
2.  Zrealizovat něco z těch nápadů ohledně vylepšení junior.guru.
3.  Dokončovat onboarding v Apify.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- ["Čekali jsme na termín 7 měsíců. Syn se do té doby oběsil." Psychiatrická péče pro děti je v těžké krizi, chybí lékaři i lůžka – Page Not Found](https://pagenotfound.cz/clanek/cekali-jsme-na-termin-7-mesicu-syn-se-do-te-doby-obesil-psychiatricka-pece-pro-deti-je-v-tezke-krizi-chybi-lekari-i-luzka)<br>Brutální čtení. Ale z různých stran se mi už delší dobu potvrzuje, že takhle to fakt je. Sehnat psychologickou pomoc pro dítě je v ČR prakticky nemožné. A nikdo s tím nic nedělá.
- [Proč už dnešní děti nechodí do školy samy? - YouTube](https://www.youtube.com/watch?v=x4z8JdwOzU0)<br>Proč už dnešní děti nechodí do školy samy? Protože rodiče.
- [The Latest Model (2006) - YouTube](https://www.youtube.com/watch?v=n1gaylKtM0s)<br>The Latest Model (2006, 2 minuty)
- [AI-generated posters don’t have to be horrible | ‘ERE I AM - JH!](https://ukslim.github.io/2026/06/07/ai-event-posters.html)<br>Protože nemá smysl snažit se, aby to vůbec nebylo, šiřme aspoň návody, jak to dělat líp. Pro vlastní dobro! Potřeba vyškrábat si oči bude pak třeba přicházet méně často… Zdravíme Comic Sans s WordArtem a nově je vítáme v kategorii „roztomilé retro“.
- [AI fatigue is real and nobody talks about it · Siddhant Khare](https://siddhantkhare.com/writing/ai-fatigue-is-real)<br>„The tech industry has a burnout problem that predates AI. AI is making it worse, not better. Not because AI is bad, but because AI removes the natural speed limits that used to protect us.“
