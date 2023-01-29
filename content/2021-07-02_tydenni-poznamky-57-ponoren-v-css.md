Title: Týdenní poznámky #57: Ponořen v CSS
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl další týden (28.6. — 2.7.) a tak [stejně jako minule]({filename}2021-06-25_tydenni-poznamky-56-bootstrap-a-namluvy-s-firmami.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Překopání MkDocs

Hned z kraje týdne jsem se rozhodl, že z projektu vyhodím [mkdocs_macros_plugin](https://github.com/fralau/mkdocs_macros_plugin), který mi umožňuje používat Jinja2 i přímo v Markdownu. Je to pěkný plugin s dokumentací a aktivním maintainerem, ale je na můj vkus nakonec možná až příliš univerzální, komplikovaně navržený a zároveň nepokryje celou jednu velkou část potřeb, kterou mám.

Vrátil jsem se k [mkdocs-simple-hooks](https://github.com/aklajnert/mkdocs-simple-hooks), které jsem už dřív objevil, ale prozatím nepoužil. Vše, co souviselo s mkdocs_macros_plugin jsem vyhodil a přebudoval do pár svých vlastních hooků. Výsledek? [53 řádků vlastního kódu](https://github.com/honzajavorek/junior.guru/blob/94f994af55f9846b8509b18993c8bf1ea98ffb1a/juniorguru/mkdocs/hooks.py), které řeší naprosto vše, co potřebuji, vím přesně co od nich čekat a které plynule navazují na to, jak byly MkDocs navrženy a nevymýšlí vlastní vesmír, což byla u mkdocs_macros_plugin tak trochu bolest.

Jinja2 template filters si teď můžu [deklarovat hezky v konfiguráku](https://github.com/honzajavorek/junior.guru/blob/94f994af55f9846b8509b18993c8bf1ea98ffb1a/juniorguru/mkdocs/mkdocs.yml#L32) a tvorbu kontextu pro šablony mám relativně [přehledně v jednom souboru](https://github.com/honzajavorek/junior.guru/blob/94f994af55f9846b8509b18993c8bf1ea98ffb1a/juniorguru/mkdocs/context.py), vždy zvlášť co je sdílené, co je přístupné jen v Markdownu a co je přístupné jen v šabloně patřící k „theme“ webu.

Samozřejmě mě to celé zase trochu zdrželo, utopil jsem v tom minimálně den a hodnota žádná velká, je to jen přehazování kódu vidlema z hromádky na hromádku. Jenže s tím mkdocs_macros_plugin to prostě už delší dobu skřípalo a já jsem si řekl, že když už dělám v2 celého webu, měla by chvíli vydržet funkční a raději do toho říznu teď hned, než v tom tu v2 udělám celou a sotva vytvořím novou věc, budu z ní hned rozmrzelý. Teď jsem spokojený a mám opět dojem, že to jde všechno správným směrem a že vytvořím něco, co pak dlouho nebudu muset zase měnit :)


## Nová patička webu

Snažil jsem se dokončit vzhled a obsah nové patičky webu. Výsledek lze živě vidět [tady](https://junior.guru/club2/). Několik dní jsem ležel v CSS a posouval věci o pár pixelů doleva a pak zase doprava. Ladil jsem barvy, nadpisy, responzivitu pro mobily, atd. Neříkám, že je to finální verze, ale už jsem s tím docela spokojený a nerad bych do toho už moc šťoural.

![Patička]({static}/images/footer.png)


### Informace o výdělcích

Nová patička webu by měla transparentně vypisovat informaci o tom, kolik zrovna vydělávám, takže jsem si dopsal kód, který tyto informace stáhne z mého Google Sheetu (kde jsou data přímo z mého účtu díky mé vlastní knihovně [fiobank](https://github.com/honzajavorek/fiobank)) a uloží do databáze jako metriky. V takovéto podobě je při skládání webu dohromady zase z databáze vytáhnu a vypíšu v šabloně. Čísel mám hromadu, no nakonec jsem se rozhodl vypsat 2 věci, které mi přijdou nejužitečnější pro náhodného kolemjdoucího:

- Můj aktuální čistý zisk měsíčně (20881 Kč)
- Jaké jsou mé zdroje příjmů, v procentech (54 % firemní členství, 27 % individuální členství…)

První číslo by lidem mělo dát představu o tom, jak moc na tom celém rejžuju a jestli se teda uživím nebo ne, nebo co. Mohlo by je to motivovat mi přispět členstvím v klubu. Co se stane, až to číslo bude jednou větší, pokud by se mi ho tedy zvýšit povedlo, tak to nevím :D Prodavači v Lidlu si mohou vybrat, zda mi budou závidět, nebo fandit mému úspěchu. Seniorní programátoři mě budou litovat a ťukat si na čelo, že se dobrovolně snažím žít o almužně. Jako seniorní vývojář bych dokázal sehnat něco jako 100k hrubého měsíčně. Jenže takhle nemám standup, sprint planning, ani meetingy, a za to mi to zatím stojí :D

Rozpad příjmů na procenta je věc, která odkrývá moje karty co se týče skrytých motivací. Říkám tím, kdo jsou mí klienti a co mě živí z kolika procent, takže si každý může vyhodnotit, jaký mám aktuálně _bias_. Nejvíc příjmů mi teď například dělají firemní členství, což je jistě fajn, ale znamená to, že nemusím mít takovou snahu ty firmy třeba kritizovat, na rozdíl od toho, kdyby mě z většiny živili jednotlivci. Osobně bych chtěl, aby se do budoucna podíl jednotlivců zvýšil, ideálně třeba i dorovnal s firmami (teď když sečtu členství a dobrovolné příspěvky, je to 54 % pro firmy a 45 % pro jednotlivce, takže to není nemožné).


## Stylování komponent v obsahu nové stránky o klubu

Kromě patičky jsem stihl ještě nastylovat dvě komponenty přímo z obsahu nové stránky:

- Citace,
- srovnávací tabulku.

Výsledek lze opět živě vidět [tady](https://junior.guru/club2/). S citacemi jsem celkem spokojen. Zkusil jsem přidat obrázky. Mnoho lidí si také stěžovalo, že citace, jak jsou na JG teď, se špatně čtou, protože jsou pouze velkými písmeny. To by mělo být s tímto novým designem vyřešeno.

![Citace]({static}/images/blockquote.png)


## Další poznámky

- SCSS už mi pocitově přetékalo z jednoho souboru, tak jsem jej rozdělil do více a propojil přes importy.
- Nainstaloval jsem si [stylelint do VS Code](https://github.com/stylelint/vscode-stylelint), abych na nedostatky přicházel hned v editoru a ne až na CI.
- Z Engeta se mi ozvali ohledně postprodukce materiálů, které jsme spolu předtím měsíc tvořili. Měl bych na to mkrnout a všechno si to projít.
- Pomaličku se posouvám co se týče domlouvání nových přednášek. Komunikuju na všechny strany.
- Pomaličku se posouvám i co se týče domlouvání budoucího Financial Aid pro lidi z různých znevýhodněných skupin. Komunikoval jsem kvůli tomu s Mews, Engetem, SDAcademy, ale ještě na tom bude spousta práce. Mews ale přišli zase s dalším skvělým nápadem, tak z toho mám radost.
- Dnes jsem z lidí v klubu vylosoval dva volňásky na [WebExpo](https://www.webexpo.net).
- Poslal jsem [červnový newsletter](https://us3.campaign-archive.com/?u=7d3f89ef9b2ed953ddf4ff5f6&id=3c16672ca8).
- Uklidil jsem si v Trello boardu, kde si eviduji úkoly a nápady k JG. Strávil jsem s tím několik hodin, ale bylo to už potřeba. Prošel jsem nekonečnou hromadu kartiček a přeuspořádal si sloupce, do kterých si je třídím, aby odrážely způsob, jakým nad projektem aktuálně přemýšlím. Ve sloupci s nápady na vylepšení nebo rozšíření příručky je aktuálně něco přes 470 kartiček. Kolik má kartiček celý ten board, to ani raději nechci vědět :)
- Konfiguroval jsem [Markdown pluginy](https://python-markdown.github.io/extensions/#officially-supported-extensions) v MkDocs.
- Ozval se mi Vojta Mádr z [.NET.CZ Podcast](https://www.dotnetpodcast.cz/) a domluvili jsme se, že bychom mohli natočit díl se mnou jako s hostem. Domluva byla rychlá, ve čtvrtek ráno jsme to provedli a prý to brzo vyjde :) Byl to moc příjemný pokec. Už se těším!
- Mnoho času mi zabralo probírání se maily a odpovídání, procházení konverzací v klubu a odpovídání, připravování příspěvků na sociální sítě.
- Šel jsem s kamarádkou na kafe, volal jsem si se starými kamarády, s bývalými kolegy jsem šel na krásný dlouhý oběd nezaměstnaných lidí a jeden celý večer jsem jiného kamaráda stěhoval z jediného správného bydliště (Žižkov) někam do Středočeského kraje (Bořislavka). Pokud mohu aproximovat podle dalších bývalých kamarádů-sousedů, tento tah způsobí, že od teď se budeme vídat už maximálně čtvrtletně. Praha ¯\\\_(ツ)\_/¯
- Na webu JG je věta, že ajťáci už dávno nejsou asociálové někde ve sklepním doupěti. Někdo mi doporučil, ať se [podívám](https://www.youtube.com/watch?v=xg7xv6adtmI), jak vlastně takové doupě vypadá, že mu to přijde sociální dost, akorát jinak, než je třeba běžné. Tak jsem se podíval a pravda, formulaci asi trochu upravím :)
- Stále mi nechodily peníze z Patreonu, tak jsem se podíval na PayPal, co se děje. Děje se to, že na rozdíl od Stripe, který mi posílá peníze na účet sám, se u PayPalu musí kliknout na tlačítko a ručně si je poslat, na což jsem tak nějak zapomněl. Takže jsem klikl na tlačítko a mám zase o něco víc pěněz :)
- Odebral jsem [minifikaci HTML](https://www.npmjs.com/package/gulp-html-minifier) na JG. Možná to ušetří pár bajtů, ale výsledné HTML neodpovídá tomu HTML, které mám při vývoji (což někdy vede k chybám, které zjistím až na produkci) a je nečitelné pro juniory, kteří by se třeba na JG chtěli podívat do kódu stránky a zjistit, jak je vyrobená. Já se učil HTML kdysi tak, že jsem zkoumal cizí weby a učil se z toho, jak tam mají co udělané. Nechci to zamezovat nové generaci.
- V redakci Česko.Digital se konečně povedlo schválit a vydat [článek Martiny Hytychové](https://blog.cesko.digital/2021/06/zkuste-open-source) o tom, jak může i junior začít v open source, právě zrovna díky komunitě jako je č.d. Hurá! Nasázel jsem o tom příspěvky na sociální sítě, ale ještě bych jej chtěl časem taky odcitovat různě na webu, přidat do příběhů, atd.
- [Benevity](https://www.benevity.com/) se ozvalo, že máme za Pyvec naklikat čestné prohlášení, že nejsme církev, politická strana ani teroristi, tak jsem to proklikal. Je potřeba to takhle vždycky udělat, mám pocit že zhruba jednou za rok. Některé firmy dávají možnost zaměstnancům přispívat na neziskovky s tím, že k tomu i něco přihodí. Benevity je systém, který na to občas používají. V minulosti nám takhle někdo už několikrát přispěl, tak to udržujeme při životě.
- Fíha, nějak mi uniklo, že první poznámky jsem napsal 8.5.2020, to znamená už víc jak před rokem :-o A já se bál, že mi to vydrží tak dva týdny :D
- Během 7 dní od 26.6. do 2.7. jsem naběhal 9 km. Celkem jsem se hýbal 1 hodin a zdolal při tom 9 kilometrů.


## Co plánuji

Příští týden si plánuji vzít dovolenou. Cílem je neudělat nic. Pokud se mi něco udělat přesto povede, bude to velké osobní selhání!


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Global Baby Drought of Covid-19 Crisis Risks Population Crunch](https://www.bloomberg.com/news/articles/2021-03-14/global-baby-drought-of-covid-19-crisis-risks-population-crunch)<br>Zdá se, že pandemie udělala díru do porodnosti. Zhoršila se ekonomická situace lidí, nemohli se stýkat, randit, žijí v nejistotě, posunují své plány a pak jim bude hrozit neplodnost v pozdějším věku. Lidé, kteří spolu zůstali zavření rok doma a nezbylo jim než dělat děti, statistiky zdaleka nevyrovnají. V některých zemích už vidí 9 měsíců po pandemii drastický propad. Spolu se stárnoucí populací je to koktejl, který může v budoucnu zhroutit už tak napjaté sociální systémy a splacení státních dluhů v mnoha vyspělých zemích.
- [The obesity era](https://aeon.co/essays/blaming-individuals-for-obesity-may-be-altogether-wrong)<br>Velmi zajímavé čtení o tom, zda je současná epidemie obezity vůbec něčím, co jsme schopni individuálně tak moc ovlivnit, jak nám to všichni tlačí. Je možné, že jde o vliv globálních příčin nebo dokonce něco, co si předáváme z generace na generaci?
- [Čeští novináři zamrzli na Twitteru. Jiné sociální sítě nechávají napospas politikům a marketérům — HlídacíPes.org](https://hlidacipes.org/cesti-novinari-zamrzli-na-twitteru-jine-socialni-site-nechavaji-napospas-politikum-a-marketerum/)<br>Zapomeňte na „pražskou kavárnu“, zajímavější je „novinářská Twitter bublina“.
- [K násilí na ženách v politice dochází i v Česku. Jeho cílem je političky zastrašit a vytlačit](https://a2larm.cz/2021/06/k-nasili-na-zenach-v-politice-dochazi-i-v-cesku-jeho-cilem-je-politicky-zastrasit-a-vytlacit/)<br>Tolik k tomu, zda mají ženy v politice stejné podmínky, jako muži.
- [Esej Kateřiny Smejkalové: Různé světy české společnosti](https://www.novinky.cz/kultura/salon/clanek/esej-kateriny-smejkalove-ruzne-svety-ceske-spolecnosti-40364443)<br>Klenot! Studie Jedna společnost – různé světy. Přečtěte si, proč lidé volí SPD, na čem se dva hlavní názorové tábory neshodnou a na čem se naopak shodnou, proč může být kritické myšlení elitářským chucpe, proč tu nejsme jako v Německu. Děsivé zrcadlo, ale asi nám nezbývá, než do něj pohlédnout a říct si sestimsmiř. Toto se jen tak nezmění a proto tady ještě dlouho nebudeme moci mít hezké věci.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
