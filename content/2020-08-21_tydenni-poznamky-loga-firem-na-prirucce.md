Title: Týdenní poznámky: Loga firem na příručce
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Twitter-Comments: https://twitter.com/honzajavorek/status/1296850831602585601
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158396227362707


Utekl další týden (17.8. — 21.8.) a tak [stejně jako minule]({filename}/2020-08-14_tydenni-poznamky-konecne-spokojen-s-toc.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Jak jsem psal minule, tento týden jsem pracoval jen pár dní, protože se mi sešlo jednak volno, jednak nějaké rodinné události. V neděli jsem uběhl [10 km v Kozojedech](https://www.facebook.com/events/252296662521351/), byl to prima závod a už se těším na příští ročník. Naposledy jsem činnost typu běh vykonával podle mých záznamů před rokem, a to jsem se šel ještě jen proběhnout za barák, takže už jen dokončení závodu považuji za velký úspěch. 10.82 km, čas 1:10, tempo 6:32, nastoupáno 175 m.

## Loga firem

Čtvrtek i pátek jsem více méně finišoval vzhled příručky a to hlavně proužku, který by měl zobrazovat loga firem. Prvotní nápad naštěstí celkem fungoval, ne jak u ToC (viz minulé poznámky), jen jsem si hrál s tím, jestli se mají loga nějak zvětšovat nebo přeskládávat, když člověk scrolluje. Nakonec jsem od všech animací a přesunů upustil, protože to v nějakém prohlížeči vždy nevypadalo dobře, chovalo se to divně, nebo to prostě celé působilo přeplácaně.

Loga jsou `position: sticky` a s malou pomocí JavaScriptu při pozicování a detekci v jaké fázi scrollování člověk je, jsou celé v CSS. Kvůli proužku s logy se musel taky zvětšit "offset" pro odkazy "na kotvu", tzn. nárazník, který zaručuje, že když někdo jde v prohlížeči na `#odstavec`, tak nadpis a kus toho odstavce nebude skrytá pod všemi těmi proužky nahoře, ale bude odsazená od vrchu stránky. Bylo naštěstí jednodušší to vyřešit, než jsem čekal, stačilo pár dalších řádků JS a CSS.

Nakonec jsem přidal reálná loga firem, které si je předplatily a zkoumal, jak to vypadá. Myslím, že to ujde.

![Loga]({static}/images/loga.png)

Na obrázku vidíte loga v jednom proužku. Když se scrolluje, tento proužek se nalepí pod další vrchní proužky, dostane stín, a s nimi pak cestuje.

Ještě jsem přidal nějaké to měření přes Google Analytics, jestli a kolik lidí na loga kliká, ať to pak můžu firmám posílat, a přidal automaticky UTM parametry k odkazům. K tomu jsem si napsal novou "knihovničku", která tohle bude umět dělat i jinde a lze ji instruovat skrze `data-` atributy v HTML, ale zatím jsem se neobtěžoval s tím předělávat na ni staré věci. Nějaké posílání statistik taky zatím nemám, na to bude čas po vydání příručky, ale hlavně aby se to od začátku měřilo.

## Další poznámky

- Na JG se objevil [nový inzerát](https://junior.guru/jobs/d0175235aeab461c2adb9a0796f40cf8c54ca085fb657ce5b14c367b/), tak snad se to opravdu s podzimem zase rozjede.
- Upgradoval jsem závislosti na některých projektech Python komunity.
- Snažil jsem se na [docs.pyvec.org](https://github.com/pyvec/docs.pyvec.org) vyřešit commitování do chráněné hlavní větve tak, že bych pomocí GitHub Actions automaticky vytvořil spíš Pull Request, ale zatím neúspěšně. Věnoval jsem tomu hodinku v pátek a zase se k tomu vrátím jindy.
- Na příručku jsem přidal datum, kdy byla naposledy aktualizovaná, aby lidi viděli, že text časem opravdu upravuju. Informace se vytahuje přímo z Gitu.
- Opravil jsem jeden (až dva) podivné bugy v zobrazování věcí v Safari.
- Napsal jsem Czechitas e-mail, jestli mají zájem nakouknout do příručky před jejím vydáním výměnou za to, že o ní něco napíšou na svůj blog.
- Po minulých neúspěších s různými pokusy o tiskovou zprávu jsem zatím zkusil něco, co mě stojí nejméně energie: [tweet](https://twitter.com/honzajavorek/status/1296808683419193345), kde se ptám, jestli někdo nechce přístup k příručce dřív, výměnou za publicitu. Sice jsem dal omylem mention na slovenské Nko, ale to se snese :) Tato výzva platí i pro jednotlivce, takže pokud máte blog nebo někde nějakých pár followers, napište mi a domluvíme se.
- Začínám si psát rozvrh činností, které musím postupně udělat v souvislosti s uvěřejněním příručky. Bude to maso.
- Poslal jsem první větší fakturu!

![Peníze]({static}/images/faktura.jpg)
Hluboký lidský příběh

V grafu nejsou [příspěvky přes GitHub Sponsors nebo Patreon](https://junior.guru/donate/), s nimi by to vypadalo méně tragicky.


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Mozilla: The Greatest Tech Company Left Behind](https://getpocket.com/redirect?&url=https%3A%2F%2Fmedium.com%2Fyoung-coder%2Fmozilla-the-greatest-tech-company-left-behind-9e912098a0e1&h=5a11641d498e87918aaca84524bc33da48704949aee3f7eabf7abf132d5ad4fd)<br>Mozilla propustila další várku lidí a tentokrát i z MDN nebo Serva (Rust). Tento článek je předčasný nekrolog. Za to, aby tyhle věci mohly pokračovat a Mozilla se nezhroutila jako domeček z karet, bych klidně platil nějaké předplatné, ale Mozilla si o to nikdy neřekla :(
- [Are you as smart as a toddler?](https://getpocket.com/redirect?&url=https%3A%2F%2Fvicki.substack.com%2Fp%2Fare-you-as-smart-as-a-toddler&h=1f79a82304d9076e0e8b1f3a391db704f99e9f9b3a7d3e5308248f48c240318a)<br>Budoucnost AI, batolení, GPT-3, peníze.
- [„A to pro vás má Putin poslat Specnaz?“ Bizarní příběh lodi, která do Bejrůtu dovezla výbušný náklad.](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.voxpot.cz%2Fa-to-pro-vas-ma-putin-poslat-specnaz-bizarni-pribeh-lodi-ktera-do-bejrutu-dovezla-vybusny-naklad%2F&h=3ffe919283f765857945095f399cffeabaea44776cba3430649ac4400855b572)<br>Spletitý příběh libanonských výbušnin
- [Google and the Nothing](https://getpocket.com/redirect?&url=https%3A%2F%2Fvicki.substack.com%2Fp%2Fgoogle-and-the-nothing&h=4d1441ad0eca81fcc1f70d7f8dcd059d6ce61cad21ae2e6f64ccfb81c26cc968)<br>Jak Google požírá internet a doprovází ho neužitečná nicota. A jak všichni děláme weby tak, aby to pokračovalo, protože bez toho nemůžeme vydělat peníze.
- [Obloha po Muskovi: Jak začal nový souboj států a korporací o ovládnutí nebe.](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.voxpot.cz%2Fobloha-po-muskovi-jak-zacal-novy-souboj-statu-a-korporaci-o-ovladnuti-nebe%2F&h=7cf6b3b8eea0b1e17b774a7273d30f9bf372011f14efaa3696081ede042e9fd7)<br>SpaceX privatizuje oblohu a zároveň prorůstá se státními zájmy USA
- [After 10 Years in Tech Isolation, I’m Now Outsider to Things I Once Had Mastered](https://getpocket.com/redirect?&url=https%3A%2F%2Fforklog.media%2Fafter-10-years-in-tech-isolation-im-now-outsider-to-things-i-once-had-mastered%2F&h=48ec26889a7dfb2e80f941eb3ad7ff8fdbc3942b3098256d3759fe705f165433)<br>Hacker, který byl 10 let ve vězení bez kontaktu s realitou, píše o tom, jak se mu jeví dnešek
- [The Return of the 90s Web](https://getpocket.com/redirect?&url=https%3A%2F%2Fmxb.dev%2Fblog%2Fthe-return-of-the-90s-web%2F&h=3f89706f184c646e45987ae56a647b8c7f12772a80d83658a96080e01da8653e)<br>Návrat do budoucnosti na webu :)
- [Amelia Wattenberger: What does 100% mean in CSS?](https://getpocket.com/redirect?&url=https%3A%2F%2Fwattenberger.com%2Fblog%2Fcss-percents&h=fcf04e6b232c8154bd72f7b5ef143ff6dbe1f68d11e26431868583b211896aba)<br>Přehled toho, jak v CSS fungují procenta
- [Effective testing for machine learning systems.](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2FD5ck6fzk72%3Fssr%3Dtrue&h=7d206bfdef469a874f0f046122f41e04bea73fb679983529e0688fbb2a27b8dd)<br>Zajímavý rozbor o tom, jak lze testovat ML modely. Klasicky píšeme logiku a testujeme pomocí příkladů. Tady na základě příkladů vznikne logika. Je možné ji testovat? Jak?

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
