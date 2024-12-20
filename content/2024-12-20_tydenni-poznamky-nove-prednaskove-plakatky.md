Title: Týdenní poznámky: Nové přednáškové plakátky
Image: images/img-7295-copy.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-12-13_tydenni-poznamky-ani-nevim-jak-to-pojmenovat.md) už utekl nějaký ten týden (13. 12. až 20. 12.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/img-7295-copy.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Stará „předsevzetí” jsou v článku [Plán na Q2 2024]({filename}2024-04-06_plan-na-q2-2024.md), nová teď nejsou.

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Nějak rychle to uteklo! Poslali jsme dítě do školky, tak byl čas na práci, ale řešili ještě nějaké vánoční dárky, výzdobu, a tak, no a práci přerušovaly i různé další pochůzky. Ani nevím, jak se stalo, že už je pátek.

## Přednáška v klubu

V klubu se v úterý odehrála přednáška, více méně bez zádrhelů. Bylo to o AI asistentech při kódění a přišlo mi to dost zajímavé, jen nevím, kdy mám mít čas na to si s tím vším pohrát a naučit se s tím. Na přednášce byla velká účast, přišlo zhruba 30 lidí, což je pěkný. Udělalo mi to radost.

![Přednáška]({static}/images/screenshot-2024-12-17-at-18-22-54.png)

## Pyvo

Byl jsem na tom „Home Assistant“ Pyvu. Dotáhl jsem tam i bráchu, který doma Home Assistant má. Byl na Pyvu podruhé v životě, asi po sto letech. Byl tam pub quiz. Myslel jsem, že nebudu ani soutěžit, protože o HA nic nevím. Brácha ale začal odpovídat a nadepsal to za nás oba. Musel brzo odejít, tak že já budu pokračovat. Nic o HA jsem nevěděl, ale on docela jo, vyplňoval to v podstatě sám. Pak byla druhá část, tu jsem dělal sám zase já. Brácha už byl pryč. Druhá část byla o Pythonu, takže tam jsem zase docela dost věděl já. No takže jsme vyhráli [Home Assistant Green](https://www.home-assistant.io/green/) 😀 Jenže brácha už HA má a já ho nejspíš nepotřebuju, nemám doma co automatizovat. Tak uvidím. Ještě to prozkoumám, ale teď jsem na to neměl vůbec čas, jen jsem to zapnul a koukl, co to doma najde. Našlo to jen reprák.

![Pyvo]({static}/images/img-3434.jpg)

![Home Assistant Green]({static}/images/img-3453.jpg)

## Nové plakátky k akcím a nové og:image

Začal jsem pracovat na nových plakátcích k akcím v klubu. Odstartoval jsem tím, že jsem se chtěl zbavit desetitisíců warningů, které mi produkuje Sass spolu s Bootstrapem ([#40849](https://github.com/twbs/bootstrap/issues/40849), [#40962](https://github.com/twbs/bootstrap/issues/40962)). Sass plugin to [posílá](https://github.com/glromeo/esbuild-sass-plugin/pull/135) do esbuildu a ten by to měl umět vypnout přes [logging](https://esbuild.github.io/api/#logging) (podobně jako třeba [tady](https://github.com/twbs/bootstrap/issues/40962#issuecomment-2448214806)), ale vůbec mi to nefungovalo. Nakonec jsem to vzdal a pinnul jsem prostě verzi toho Sass balíčku, aby dal pokoj.

Pak jsem si udělal skript, který přes automatizovaný prohlížeč a screenshot generoval nový plakátek z HTML a CSS. Abych mohl rychle iterovat a dívat se na výsledek, [zjistil jsem si](https://apple.stackexchange.com/a/74516), jak z terminálu spustit QuickLook na jeden obrázek:

```
$ python generate_poster.py && /usr/bin/qlmanage -p images/posters/*.png
```

Pak jsem se trápil s elipsou, aby byl v plakátku jakoby zakulacený výřez. Trochu mi trvalo to odladit, protože neumím úplně z hlavy dělat elipsy a i s tím QuickLookem byly iterace dost pomalé. Nakonec jsem ale zjistil, že příklady na MND můžu živě editovat a projeví se to, tak jsem si přímo na [stránce s dokumentací elipsy](https://developer.mozilla.org/en-US/docs/Web/CSS/basic-shape/ellipse) měnil hodnoty tak dlouho, až to dělalo, to co chci, a pak jsem to jen překopíroval do CSS k obrázku.

Plakátek jsem ladil a ladil a nakonec jsem do něj nějak dal všechno, co jsem chtěl, jen ne logo nebo jakýkoliv jiný brand junior.guru, kromě barev. Nikam se mi to moc nehodilo. Ale přijde mi, že to vlastně nevadí. Jde i o to, v jakém kontextu se ty obrázky budou objevovat - nikdy ne zcela samostatně, ale jako součást nějakého statusu, nějakého UI k události, nebo jako og:image u odkazu. No posuďte sami.

![Plakátek 1]({static}/images/1dc25695bb08042ebd541fc0e379af6251e0ff1a74cd70364b7c951b68a730f6.png)

![Plakátek 2]({static}/images/2f662038f56ec6048a6f21696c787dee1b57b4a80c8be666e27bd6194d2a588e.png)

![Plakátek 3]({static}/images/9feba0978d8d4a21c158eec196ff346ee4c3382e16f0fef27231dba087952ec0.png)

No a pak jsem se vrhnul na všechny ostatní og:image. Chci to sjednotit tak, aby og:image a plakátek k přednášce byly jedna a tatáž věc. Na webu má každá přednáška svou stránku, takže se to tak dá udělat. Totéž platí pro podcast, ale pro ten stejně ještě budu muset dělat i čtvercové plakátky. No každopádně jsem pak zpracoval nové og:image i pro spoustu dalších typů stránek. Příklady:

![Podcast]({static}/images/9cda3129fddf28c3c35c1273fe7e2ecce5fbb1ec4596c3033e2423a7c85720a5.png)

![Příručka]({static}/images/6c7efb4ae239c0f7e0ee1f799d238eef051ee5a4b2767249f0330cd1b6996d22.png)

![Stipendium]({static}/images/92670a49d8d1e6a054fd3703149a2233e1a893655ccc085672148b40aae8470c.png)

Mám pár nápadů, co bych s tím chtěl ještě udělat, ale přijde mi to už dost dobré na to, aby to mohlo na produkci. Takže jsem to dnes nasadil. Hodně práce bude ještě v kódu, kde se chci spousty věcí zbavit a sjednotit to tak, aby se plakátky generovaly jen na jednom místě, když už budou podle stejné šablony.

Mám radost, že se mi povedlo udělat univerzální plakátek, který se dá použít skoro všude. Předtím jsem totiž generoval zvlášť obrázek pro YouTube a zvlášť pro Discord a zvlášť og:image, každé s jinými rozměry a tak. Teď mám jeden formát, který by měl zvládnout i ořez pro úzký obrázek na Discord.

![Ořez na Discordu]({static}/images/screenshot-2024-12-17-at-14-27-09.png)

## Další

-   Napsal jsem [náhodný komentář pod náhodný status na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7275063271676678144?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7275063271676678144%2C7275071912123285504%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287275071912123285504%2Curn%3Ali%3Aactivity%3A7275063271676678144%29) a k dnešnímu dni má 52 reakcí. Zajímavé!
-   Koupili jsme dnes stromeček.
-   Stavil jsem se za jedním doktorem a pocítil nedostatky v digitalizaci českého zdravotnictví, když potřeboval něco vědět, ale to něco leží na papíře někde úplně jinde, takže mě vyšetřil bez toho, aby něco věděl. Radost.
-   Zavolal jsem si s Janem z Mews a domluvili jsme se ohledně mentoringu v klubu.
-   Obíhal jsem obchody nebo boxy a vyzvedával dárky.
-   Protřídil jsem fotky za celý podzim a udělal jsem zálohy.
-   Díky sranda videu na YouTube od Fireshipa jsem narazil na produkty, které by možná mohly být alternativou Discordu, kdyby šlo do tuhého: [Revolt](https://github.com/revoltchat/awesome-revolt), [Rocket](https://www.rocket.chat/). Ale nestihl jsem to zatím moc prozkoumat.
-   Obědval jsem dnes s kamarádem Mílou, kterého jsem už delší dobu neviděl. Dělá Advent of Code v Elixiru a říkal, že je to zajímavý jazyk a že mu to přijde ekosystémem víc v pohodě než [Haskell]({filename}2020-01-14_courting-haskell.md).
-   Včera jsem obědval s kámošem Peťou, který mi na poslední chvíli zavolal, že je v Praze, a jestli nedám rychlý oběd. Zrovna jsem chtěl jít na oběd, tak to vyšlo a viděli jsme se. Bylo to fajn.
-   Pověnoval jsem se po delší době Pyvci. Prošel jsem maily, mentions na [Pyvec Slacku](https://docs.pyvec.org/operations/support.html#sit-kontaktu), poslal jsem účetnímu Benevity report za nějaký předešlý rok, řešil jsem s účetním [pokladnu](https://github.com/pyvec/docs.pyvec.org/pull/206#issuecomment-2545212838), zval jsem lidi do našeho Vaultwardenu na hesla. Mergnul jsem [opravu odkazu na webu Pyvce](https://github.com/pyvec/pyvec.org/pull/437).
-   Dával jsem kamarádovi feedback na nové logo pro [Rector](https://getrector.com/). Když to prohlásil za finální, aktualizoval jsem to i na junior.guru, protože je to jeden ze sponzorů.
-   Byl jsem na vánoční besídce ve školce.
-   Upravil jsem kontrolu rozbitých odkazů tak, aby se těsně před ní v kontrolované složce s HTML přepsaly Cloudinary URL na obrázky a místo nich se daly původní URL mířící na junior.guru. Dělalo to totiž nedobroty. Nevěděl jsem, jak to udělat, ale tušil jsem, že to bude nějaký oneliner v Bashi, takže mi to napsalo ChatGPT (je to [tady](https://github.com/juniorguru/junior.guru/blob/bcd1688d0be785ee30b47a48670949556978013c/.circleci/config.yml#L285)). Nejvíc trhání vlasů pak přišlo, když jsem řešil, že na macOS a na Linuxu je potřeba ten příkaz napsat jinak, protože BSD `sed` nefunguje jako GNU `sed` 🤦‍♂️
-   [Simple Analytics](https://simpleanalytics.com/junior.guru) mi poslali omylem nějaký špatně vygenerovaný e-mail, kterým mě vyděsili, protože tam bylo, že nově budu platit 2.000 éček měsíčně, nebo tak něco. Naštěstí to byla jen chyba, vzápětí se mi omluvili, ale hodinu jsem zabil proklikáváním účtu, abych se ujistil, zda někde něco nepřeteklo.
-   Borec, který byl v klubu přes stipendium, si našel práci. Poděkoval mi v soukromé zprávě. Udělalo mi to radost!
-   V klubu se objevil nový člen, který mi je trochu podezřelý, tak jsem měl trochu moderátorské práce a zjišťoval jsem, co má za lubem. Zahrnovalo to i soukromou komunikaci s dalšími členy, kteří s ním přišli do styku.
-   Přečetl jsem komplet [klubový Discord](https://junior.guru/club/). Řešil jsem i nějakou režii kolem klubu - především manipulaci s předplatným a s účty u různých lidí.
-   Odstranil jsem ze scraperů nabídek práce [WeWorkRemotely](https://weworkremotely.com/). Není to relevantní pro české juniory. Dlouho jsem to tam nechával z milosti, ale teď tam z toho skočila do výběru nějaká úplná volovina, tak mi došla trpělivost a zabil jsem to. Časem ještě musím smazat kód scraperu.
-   E-maily, zprávy na LinkedIn.
-   Za 8 dní jsem při procházkách nachodil 8 km. Celkem jsem se hýbal 3 h a zdolal při tom 8 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

Flákat se a užívat si Vánoce. Nevím, kdy budu psát další poznámky, jestli za týden nebo za dva. Během vánočního klidu bych si rád našel čas na nějaké plánování - života i práce.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [What Is Your Dream for Mozilla?](https://mozillafoundation.tfaforms.net/100)<br>Tady má Mozilla (taková ta organizace, která vyrábí třeba Firefox) anketu, kde můžete vyplnit, co byste si přáli, aby dělala a na co aby se zaměřovala. Já vyplnil!
- [Deciphering Glyph ::](https://blog.glyph.im/2024/12/dangit.html)<br>„This is what social media does. It is context collapse as a service.“
- [If Not React, Then What? - Infrequently Noted](https://infrequently.org/2024/11/if-not-react-then-what/)<br>Císař je nahý! Celou dobu, co existují SPA frameworky, se mi nelíbí jejich používání na všechno. Preferoval bych progressive enhancement, ale tím se zabývali akorát v UK GOV a možná v 37signals. Zůstal jsem u toho, že „tomu nerozumím“, nejsem frontendista a nekecám do toho, jen jsem si bručel pod vousy. Tady je konečně někdo, kdo tomu rozumí a natvrdo píše, že frameworkismus není cesta. A důvody, proč nepoužívat React, se za celou dobu moc nezměnily.
- [Neremcejte nad českou železnicí. Letos prošla největší proměnou za poslední roky - Zdopravy.cz](https://zdopravy.cz/neremcejte-nad-ceskou-zeleznici-letos-prosla-nejvetsi-promenou-za-posledni-roky-230735/)<br>„Zjednodušeně řečeno, pravděpodobnost, že pojedete nějakým opravdu špatným vlakem, je s novým jízdním řádem opět výrazně nižší. Je přitom zajímavé sledovat reakce cestujících, když po letech v regionovách nasedají například do úplně nové jednotky odpovídající 21. století… I na těch nejprofláknutějších rychlících pověstných nejstaršími vozy se začínají objevovat modernější vozidla.“
- [Humans may not have survived without Neanderthals](https://www.bbc.com/news/articles/cwydgyy8120o)<br>„New studies show that only humans who interbred with Neanderthals went on to thrive, while other bloodlines died out.“
- [Review: Outsourcing academia](https://continent.substack.com/p/review-outsourcing-academia)<br>„Kenya is host to a thriving army–about 40,000 strong–of college graduates who work as academic writers. These “shadow scholars” are commissioned and paid by students in the most prestigious institutions in the western hemisphere to produce essays, papers, scholarly articles and graduate theses on their behalf. Worth around $7-billion, this shadow industry is built on the wide economic gulf that exists between wealthy nations and a developing country like Kenya.“
