Title: Týdenní poznámky #68: Odstranění Vercelu, cally, pracovní inzeráty
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (27.9. — 3.10.) a tak [stejně jako minule]({filename}/2021-09-26_tydenni-poznamky-67-stourani-se-v-nabidkach-prace-a-clanek-o-volbach.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Výpadek JG zhruba na den

Měnil jsem deployment JG a samozřejmě se mi to nepovedlo bez výpadku. Pokud vás zajímá, jak je možné vytvořit výpadek u statických stránek, tak čtěte!

Už delší dobu mi přišlo, že Vercel mi přináší jen zbytečné problémy. Co potřebuju pro JG je build na CI a z tohoto CI pak pushnout kód na úložiště statických souborů. Před časem toto Vercel velmi zkomplikoval, tak jsem vymyslel něco, co sice nějak funguje s jejich GitHub integrací, ale byl to velký hack. V podstatě jsem udělal skript, který když se spustil u nich na serveru, tak předstíral, že buildí stránku, ale ve skutečnosti jen čekal na CircleCI až dojede a pak si z tama stáhl artefakt s HTML soubory a ty rozbalil ze zipu do Vercelu. Bylo to i proto, že nad CircleCI runtimem mám plnou kontrolu a mohu tam jako člověk nainstalovat např. browser nebo jakoukoliv systémovou knihovnu, což na Vercel nemůžu. Navíc výhody, které má Vercel přinášet, například náhledy feature branches, vůbec nepoužívám, protože nebranchuji a dělám continuous deployment.

Prostě z více důvodů jsem se už dřív rozhodl, že Vercel půjde pryč, ale odsouval jsem to. V poslední době se mi prodloužila délka buildu na CI a to způsobilo, že velmi často Vercel zařízl můj skript dřív, než se dočkal artefaktu a deploy neproběhl. Takže jsem to prioritizoval a tento týden plně přesunul JG z Vercelu na GitHub Pages.

Už z dřívějška jsem měl připravený dvojtý deployment, takže každá verze JG už nějakou dobu byla jak na Vercelu, tak na GH Pages. Teď šlo jen o to přehodit doménu. Tu mám u [Subregu](https://subreg.cz/), takže jsem tam do DNS nastavil vše, co jsem viděl ve Vercelu v DNS. Pak jsem přidal záznamy pro GH Pages [podle dokumentace](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Pak jsem dal přesunout DNS na doméně z Vercelu na Subreg. Pak jsem zapomněl přepnout v GitHub nastavení projekt na custom doménu, takže zhruba jeden den JG vůbec nefungovalo. Naštěstí byl státní svátek, tak si toho nevšimlo tolik lidí, ale pár mi jich do různých zpráv nakonec napsalo, že JG nejede. Zmáčkl jsem tedy jedno tlačítko v nastavení GitHubu a bylo to, ehm. Pak už jen doplnit CNAME soubor, ale skoro se mi zdálo, že to jede i bez něj.

Kdybych měl udělat incident report, tak za chybu může nezkontrolovaný výsledek po pár hodinách (odezva sítě je pomalá, DNS se kešují, atd.) a absence něčeho jako uptime robot. Jenže kromě změny deploymentu, která se děje jen jednou za sto let, by jinak uptime robot měřil pouze dostupnost GitHub Pages, která je 99.něco% a jako malému podnikateli je mi šumák, takže notifikace z robota by byly jen šum. Asi zbytečné to nějak do budoucna víc řešit, spíš bych si měl po sobě věci lépe kontrolovat.

V návaznosti na přechod z Vercelu pryč jsem mohl z kódu a CI smazat všechny hacky, skripty, environment variables a další zbytečné smetí.


## Překopávání dat kolem pracovních inzerátů

Stále ještě nemám hotové překopání pracovních inzerátů. Vždy udělám nějakou změnu a zjistím, že způsobila mnoho jiných změn, s nimiž jsem nepočítal. Tento týden se mi povedlo vyndat z API pro Czechitas inzeráty, které nejsou juniorní a evidovat v tabulkách správně skóre juniornosti. Rovněž se ukládá informace o tom, jestli je nabídka na dálku nebo ne, typy zaměstnaneckého poměru, apod.

Dále jsem pracoval na tom, aby se jednodušeji v klubu hlasovalo o tom, zda je nabídka juniorní, nebo do výběru nepatří. Toto hlasování by mělo informovat AI. Jenže spolu s překopáním dat to začalo zlobit a při pokusech opravit to jsem zjistil, že to asi vzdám a musím to celé udělat znovu. Tím, že má hlasování informovat AI a AI by mělo už používat nový datový model, mělo by stačit tyto věci napojit již na nové tabulky a starýma se vůbec nezabývat. Proto jsem spoustu věcí smazal a skript významně zkrátil.

Informování AI o špatně vyhozených nabídkách hlasováním v tajném kanálu jsem nakonec pro jednoduchost vypnul, stejně se to bude muset udělat nakonec trochu jinak a v poslední době se tam nedařilo nabídky správně párovat a tedy se tam třeba naházelo 100 nabídek denně, třeba i duplicitně. Tím kanál zatím ztratil smysl a oprava není jednoduchá ani rychlá, takže příště.

Házení vybraných inzerátů do klubu ovšem dál funguje a jakmile se rozjede, bude mít každá nabídka pod sebou už rovnou reakci palce nahoru a palce dolů, což by mělo lidi víc podnítit k hlasování. Sice blbost, ale nedošlo mi původně, že aby někdo hlasoval, musí to emoji najít, což je pruda, takže lidi asi nehlasují i proto, že to není na jeden klik.


## Rozbitý build JG

„Jakmile se rozjede“ znamená jakmile opravím průšvih, jež se stal potom. Různými změnami jsem došel k tomu, že build na CI už trvá 30 minut a hlavně má 1.5 GB textu jako výstup do logů. O víkendu jsem se snažil aspoň zjistit, v čem je úzké hrdlo.

Je to tím, že do logů standardně ve Scrapy frčí veškerý objem scrapovaných nabídek, tedy i texty. No a já jednak v poslední době výrazně zvýšil počet nabídek, jednak jsem zdvojnásobil objem každé nabídky, protože jsem vedle `description_html` přidal i `description_text`, což využívá AI a kde je obsah inzerátu očištěný. Taky jsem zjišťoval, jak mohu lépe paralelizovat scrapery.

JG je teď rozbité, nedokáže se vybuildit znova, na webu je několik dní stará verze. Mým úkolem je to co nejrychleji opravit, ale zároveň přesně s touto situací architektura JG počítá, pořád jsem jen jeden smrtelník, takže nejrychleji může být i týden, nejhorší co se stane je, že se neaktualizují nabídky práce a bot neudělá svoje domácí práce v klubu. Což není tak hrozné.

Nejpomalejší věci, které mi tam jedou, je analýza zpráv v klubu 4.1min, tvorba tabulky s historickými a současnými nabídkami práce 8.5min, špendlíky v klubu 3.1min, stahování nabídek práce 19.0min. Celkový čas i se zbytkem je 37.3min. Cílem je tedy zrychlit scrapery a omezit textový výstup. K tomu mám otevřené následující taby v prohlížeči:

- [Running multiple spiders in the same process](https://docs.scrapy.org/en/latest/topics/practices.html)
- [suppress Scrapy Item printed in logs after pipeline](https://stackoverflow.com/questions/14390945/suppress-scrapy-item-printed-in-logs-after-pipeline)


## Hovory

Sešlo se nějak hodně hovorů. Jednak jsem si volal s časopisem o tom, jak to bude s mými články. Potkal jsem zbytek týmu a domluvili jsme se, kdo bude psát o čem, jak to bude probíhat a jaké jsou termíny. Pak jsem si volal s tou onou organizací, o které jsem psal minule, že jsem pro ni mohl pracovat. Popovídali jsme si a možná pro ni budu nakonec stejně pracovat :D Ale v nějakém úplně mini úvazku, spíše jako konzultant, mentor. Dále jsem měl hovor se vzdělávací agenturou a řešili jsme, kde vázne posílání jejich studentů do klubu (na čemž je shoda) a jak dále ještě můžeme spolupracovat nebo si jinak pomoct.


## Další poznámky

- Měli jsme v klubu AMA [mentorů na frontend](https://coreskill.tech/), Dana a Kate. Proběhlo to hezky. Dan se sám ujal čtení otázek, takže jsem to měl celkem bez práce, otázek bylo dost, takže výsledek za mě pěkný. Dokonce si to chtěl i sám sestříhat, takže video je o něco hezčí, než obvykle, byť to o pár dní zdrželo dostupnost záznamu, který mám na YT většinou do hodiny od konání akce.
- Prodloužení kontraktu s korporací vyústilo v dokument o milion stranách, který jsem zatím nestihl přečíst. Písmenka OSVČ znamenají „ručím celým svým majetkem“, takže si to přečíst chci.
- Dělal jsem review na [nový článek na blog.python.cz](https://github.com/pyvec/blog.python.cz/pull/73).
- Řešil jsem tradičně spoustu mailů a další komunikace, včetně psaní s lidmi v klubu.
- Ekolist vydal i můj [starší článek o autech](https://ekolist.cz/cz/publicistika/nazory-a-komentare/honza-javorek-bez-auta).
- Během 7 dní od 27.9. do 3.10. jsem při procházkách nachodil 36 km. Celkem jsem se hýbal 13 hodin a zdolal při tom 36 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Opravit build a dodělat konečně API pro Czechitas.
2. Začít portovat příručku hledání práce do Markdownu.
3. Domluvit další přednášky.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Pět důvodů, proč odstoupení Zelených z voleb nedává smysl](https://berg.blog.respekt.cz/odstoupeni/)<br>Proč jsou výkřiky o odstoupení Zelených z voleb nesmysl. A odkazuje i nejlepší článek na světě!
- [Česko je skanzen, chováme se jako blázni, úředníci jsou odtržení od reality, říká šéf IPR Boháč](https://www.youtube.com/watch?v=yjjUQ_NB3wE)<br>Perfektní rozhovor o bytech, dopravě, urbanismu, městě.

<small>Upozorňuji, že to není vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
