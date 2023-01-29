Title: Týdenní poznámky #70: Nová příručka
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl zase nějaký ten týden (11.10. — 17.10.) a tak [stejně jako minule]({filename}2021-10-10_tydenni-poznamky-69-oprava-robota-zprovozneni-api-domluva-prednasek-a-clanku.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Dokončení přerodu příručky

Již dlouho jsem připravoval nový design příručky. Ten neměl být pouze pokračováním [redesignu z klubové stránky](https://junior.guru/club/) a tedy samoúčelným přepisem, ale především pomalým posunem příručky vstříc k lepší udržovatelnosti, protože nyní je veškerý text v Markdownu a ne HTML, a k tomu, aby se jako příručka začaly označovat souhrnně všechny čtyři současné contentové stránky na webu. Na oboje navazují velké plány.

Díky Markdownu může různé kusy příručky udržovat snadno i někdo jiný než já. Zároveň i pro mne samotného bude psaní nových částí nebo nějaká restrukturalizace jednodušší. Nový design také nerozbíjí nástroje jako Pocket nebo Send to Kindle aj., měly by nyní správně detekovat, co je hlavní obsah stránky. Celkově se mi díky tomuto přesunu povedlo z kódu vyházet spoustu smetí.

Díky tomu, že nyní funguje navigace jinak a všechny čtyři stránky jsou teď souhrnně pod tlačítkem Příručka, je celý web najednou přehlednější. Má jasné sekce, které mají jasné cíle. Loga partnerů příručky jsou nyní na všech čtyřech stránkách, takže v ceníku podražily. Do budoucna chystám úvodní rozcestník pro tuto novou příručku v širším slova smyslu a začnu jednotlivé stránky - dlouhé nudle - rozsekávat na kratší. Každá větší kapitola by ideálně měla do budoucna svou vlastní stránku. Od toho se odvíjí i změna navigace, která už nejde do podkapitol. To bude pro začátek znepřehledňovat orientaci, ale do budoucna mi to odblokuje velké zpřehlednění.

Taky zmizely ilustrace, ale to jen proto, že jsem je ještě nenakreslil. Rozhodně s nimi počítám. Citace jsou naopak barevnější, mají teď ksichtíky. Navigace na mobilu ještě není dořešená a budu ji muset předělat, ale nechtěl jsem tím už zdržovat překlopení do nové verze. Nakonec jsem nepřistoupil k tomu, abych měnil odkazy a strukturu URL, nechal jsem původní. Také jsem si zabránil vytvořit rozcestník příručky. Rozhodl jsem se, že v této fázi jen a pouze překlopím design a že i tak to bude hromada práce. Změny budou později. Aspoň si lidi pomalu zvyknou na trochu novot a nebude to všechno hrr brr najednou.

Překvapilo mě, jak jsem nakonec zvládl poslední ze čtyř stránek, tedy samotnou nekonečně dlouhou původní [příručku o hledání první práce v IT](https://junior.guru/candidate-handbook/), přehodit do nového. Dost jsem se bál, že to bude nekonečný úkol. Pomohlo, že jsem na jedno odpoledne zůstal doma sám a mohl se na to plně soustředit.

Markdown nyní generuje jiné kotvy k nadpisům, než původně byly. Vím, že jsou všude po internetu a nechtěl jsem tyto odkazy rozbít, tak jsem celkem dlouho pracoval na tom, aby zůstaly zachovány. Ke každému nadpisu jsem přidal `<span id="puvodni-id"></span>`, což naštěstí v Markdownu dobře funguje, takže tohle bylo jednoduché vyřešit, ale vyřešit to pro stovku nadpisů už bylo dost ručního vyšívání. V začátku mi pomohl s některými věcmi skript, ale většina byla ruční práce.

V rámci dolaďování designu jsem ještě upravoval vzhled bočního menu, šířku sloupců při různé šířce okna prohlížeče a ladil jsem ještě různé další drobné detaily, což si také vzalo nějaký čas. Dále jsem řešil několik problémů s [kartami](https://www.designui.cz/lekce/kartove-komponenty-v-ui), které beru z Bootstrapu, ale musel jsem si je přiohnout, aby plnily moje požadavky. Původně jsem také měl místo štítků jen ikony, ale nešlo vůbec poznat co je co, takže teď to jsou ikony a text. Dodělat jsem musel i komponentu na vypisování dvou tří nabídek práce na příhodných místech, což se používá právě v oné příručce o hledání první práce.

Píšu to tady trochu zmateně, protože je pondělí deset večer a už se s těma poznámkama moc nemažu, ale věřte mi, mám to promyšlený! Cílem bylo prostě přehodit vše tak jak je do nového designu a od toho se odrazit. Jediná nová věc je sloučení stránek pod _table of contents_ vlevo a souhrnný název „Příručka“. Ale musel jsem se strašně plácat přes prsty, abych nezačal přidávat stránky, aktualizovat texty, atd.

Než jsem to pustil ven, zkontroloval ještě jednou celý text a všechny odkazy a pak jsem šel mazat. Smazal jsem velké množství starých věcí na webu, snad kromě starého CSS, do toho radši nerýpu, abych neovlivnil nějaké stránky, které zatím zůstávají. To je vám vždycky taková radost, když mažu nepotřebný kód! Čím víc, tím líp :)

![Příručka před a po]({static}/images/prirucka-pred-po.png)

Když jsem si to naposled procházel, ještě jsem se rozhodl udělat pár minimálních úprav v CSS starého hodního menu. Posunul jsem odkazy doleva, aby aspoň připomínaly novou hlavičku a místo tlačítka na klub jsem upravil jak se indikuje aktivní položka, opět aby to co nejvíc připomínalo novou navigaci, i když jsou jiné velikosti fontů apod. Snad to povede k lepšímu propojení starého a nového, než překlopím vše.

No a teď už vlastně na webu zbývá jen pár ošklivých kačátek. Především úvodní stránka, stránka s eventy a pak jedna velká část, nabídky práce, ale ty přijdou na redesign asi až jako poslední. Pak odeberu nesmysly jako tiskové zprávy pro média nebo stránku [donate](https://junior.guru/donate/). Dobrovolné příspěvky už nechci propagovat, chci aby šli lidi spíš do klubu a podpořili mě tím.


## Příprava na časopis

Zabýval jsem se ještě nemalým množstvím komunikace kolem shánění podkladů pro články do časopisu a propojování různých lidí a firem. Kamarád se mě ptal, proč neplatím za reklamu. Že to přináší peníze.

Tak já jednak nemám rád reklamu, všude si ji blokuji, je otravná. A jak se říká, nedělej druhým to, co sám nerad. Taky nemám rád Google a Facebook a nechci jim posílat peníze. No a třeba ten časopis. Nabízeli mi, ať zaplatím desetitisíce za reklamu. Místo toho tam budu autor. Složitější cesta, budu psát pět článků, spousta komunikace, atd. Místo abych na promo hodil peníze, hážu na to čas. Jenže ono se to podle mě vyplatí. Vždycky se mi to vyplatilo. Potkám spoustu super lidí, vybuduju si spoustu důvěry, pomůžu tam a tam… a lidi si na mě později vzpomenou, doporučí mě, atd. Tyhle vztahy se budují déle a složitěji než když se hodí pár peněz na reklamu, ale jsou hlubší a pak umožňují s odstupem času lepší věci.

No, dal jsem si do kalendáře termíny na pět článků pro časopis a od té doby je sleduju pouze periférním pohledem a jinak dělám, že je nevidím. První je 24.10., takže ten nadcházející týden budu muset přitlačit.


## Další poznámky

- Nakonec po dlouhých besedách nevyšla ona avizovaná spolupráce s jednou neziskovkou, ani v omezenější podobě. Potřebují naopak někoho víc naplno, což naprosto chápu. I tak bylo hezké se poznat víc a nějaké důsledky v podobě malých splupráciček to stejně mít bude.
- Sečetl jsem hlasy, na jaké téma má mít [Honza Král](https://twitter.com/honzakral) přednášku/AMA a vyhlásil, co vyhrálo. Zároveň jsem připravil hned popis a propagaci na sociálních sítích a v klubu. Přednáška bude už teď v úterý večer.
- Volal jsem si s lidmi, kteří chtějí udělat přednášky pro klub. Jupí! Na co se můžete těšit? To si lze přečíst v zakomentovaných kusech [tohoto souboru](https://github.com/honzajavorek/junior.guru/blob/main/juniorguru/data/events.yml).
- Robot narazil u nějakých nabídek práce na CAPTCHA. V URL té stránky s CAPTCHA byl ale parametr, který odkazoval na stránku s inzerátem ¯\\\_(ツ)\_/¯ Takže toto jsem opravil poměrně rychle, stačilo správné URL přečíst z parametru.
- Do [ceníku pro firmy](https://docs.google.com/document/d/1keFyO5aavfaNfJkKlyYha4B-UbdnMja6AhprS_76E7c/) jsem přidal informaci o tom, že klub je jen česky a proč. Několikrát se mě na to už z firem ptali. Opět vyniká výhoda toho, že jsem ceník zatím nenakódil, ale je pouze jako online dokument.
- Řešil jsem jeden problém, kdy členka klubu s vypršenými 14 dny zdarma potřebovala aplikovat kupón, ale nešlo to.
- Odpovídal jsem lidem v klubu.
- O víkendu jsem našel chviličku času na přesun své aplikace na ukládání filmů do Trella, [film2trello](https://github.com/honzajavorek/film2trello) z Vercel na [Fly](https://fly.io/). Překvapilo mě, jak rychle jsem to měl vyřešené a jak skvěle to funguje! Vercel dřív umožňoval `Dockerfile` atd., ale pak pivotovali na frontend a backendové projekty např. v Pythonu tam začaly hrát čím dál tím víc druhé housle. Sice je to podporované, ale zařezávali mi delší requesty a hlavně, stále se cosi rozbíjelo, jak to měnili. Fly je oproti tomu víc jako Heroku, ale je to scale to zero a podporuje Dockerfile a requesty mi zařezávat nemusí, protože se tam odehrávají tak rychle, že nestačím čumět. Jsem mile překvapen a jsem zvědav, jak s tím budu spokojen dál. Kdyžtak bych tam přehodil i ukázkové projekty z [cojeapi.cz](https://cojeapi.cz/), které jsou teď spíš rozbité než funkční - protože běžely na Vercelu a ten cosi zase změnil a rozbil to.
- OpenAlt [uveřejnil program](https://www.openalt.cz/2021/program.php) a vypadá to, že jsem se dostal! A jsou tam i PyLadies. Takže dojdite! No a já abych připravoval přednášku :-O
- Uveřejnil jsem na JG inzerát s nabídkou práce, tentokrát placený, juchů. Pětistovka k pětistovce!
- Napsala mi firma z USA, že chce roční tarif na inzeráty na JG. Tak jsem se jich opatrně otázal, zdalipak opravdu myslí JG. Prej jo. Jsem zvědav, co z toho bude :D Napsal jsem svému daňaři, aby mě ujistil, že fakturací do USA se nestanu plátcem DPH, identifikovanou osobou, nebo jinak finančákem stíhanou osobou.
- Nakupoval jsem v neděli na Rohlíku a nebyly banány. Zuzka říká: „To je jak za komunistů.“ Tak jsem to [tweetl](https://twitter.com/honzajavorek/status/1449665370630017027) jako vtip a zabýval se dál zbytkem neděle. V osm večer nebo kdy se podívám na Twitter a má to 900 srdíček. Myslel jsem si, že je to chyba. Ale fakt. 900 srdíček! Kdybych chtěl dostat 100 lajků, třeba [tady na tomto tweetu](https://twitter.com/honzajavorek/status/1430187105246973957), tak je nikdy nedostanu. Pokusil jsem se to ještě nějak [stočit na JG](https://twitter.com/honzajavorek/status/1449820481809440770), ale asi marný pokus :) Teď když píšu poznámky, tak se koukám, že to má už přes 2000 lajků. Každých pár sekund přibývají další a už to takhle jede víc jak jeden celý den. Tohle se mi v životě nestalo, nejvíc lajkovaný tweet, co jsem kdy měl, byl třeba se 150 lajky :D Už jen čekám, až si mě pozvou do DVTV jako autora toho tweetu o banánech. Paradoxně se to teda celé stalo v týdnu, kdy jsem si pochvaloval, jak mi se soustředěním pomohlo zablokovat si zase všechny sociální sítě.
- Během 7 dní od 11.10. do 17.10. jsem při procházkách nachodil 27 km. Celkem jsem se hýbal 8 hodin a zdolal při tom 27 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Napsat článek do časopisu.
2. Ladit zbylé detaily na příručce.
3. Napsat různým firmám.

Bonus: [Vybrat si konečně bezdrátová sluchátka](https://www.facebook.com/honzajavorek/posts/10159276712692707) a koupit.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [The Czech Left Is Being Punished for Its Disastrous Record in Government](https://jacobinmag.com/2021/10/czech-republic-andrej-babis-social-democrats-communists-ano-election/)<br>Zajímavý, číst si o ČR v angličtině i o něčem jiném, než průšvizích premiéra. Třeba o průšvihu levice.
- [Revealed: Czech PM used offshore companies to buy £13m French mansion](https://www.theguardian.com/news/2021/oct/03/revealed-czech-pm-used-offshore-companies-to-buy-13m-french-mansion)<br>Konečně jsem našel čas přečíst si to.
- [Prohra Babiše je největším úspěchem i pro mladou generaci – Simindr.cz](https://www.simindr.cz/prohra-babise-je-nejvetsim-uspechem-i-pro-mladou-generaci/)<br>Zajímavý komentář k volbám. „A v případě, že vláda půjde sociálně necitlivým směrem, je pro Piráty to nejsnadnější, co se dá, po dvou letech z ní čestně odejít, aniž by ohrozili její existenci.“
- [Armády světa mají nového nepřítele: klima](https://www.voxpot.cz/armady-sveta-maji-noveho-nepritele-klima/)<br>Velice zajímavý rozbor toho, jak práci a vytíženost armády ovlivňuje klima. „Mladé muže a ženy postupem času nebude do stejnokroje lákat plakát hrdiny s puškou v ruce, ale voják odklízející trosky. Tahle činnost se zřejmě stane hlavní náplní jeho práce.“
- [Milion, který bude ještě slyšet. Nazlobení lidé ztratili své poslance](https://nazory.aktualne.cz/komentare/milion-ktery-bude-jeste-slyset-nemaji-sve-poslance-a-zlobi-s/r~b31c502029da11ec9106ac1f6b220ee8/)<br>„Asi jsme tu ještě neměli sněmovnu, která by tak málo odrážela vůli lidu z hlasování.“
- [Je po volbách. Konečně. Co z toho?](https://www.konzervativninoviny.cz/je-po-volbach-konecne-co-z-toho/)<br>Zajímavý komentář k volbám z konzervativních pozic.
- [Český dobrodruh přežil ztroskotání i v brazilské džungli. Nacisti ho zabili injekcí](https://zpravy.aktualne.cz/domaci/dobrodruh-a-spisovatel-otakar-batlicka-byl-jednim-z-mnoha-vy/r~5dd8b1e4250211eca7d3ac1f6b220ee8/)<br>Jeho povídky jsem jako malý kluk úplně žral.
- [Fila: Belmondo byl největší hvězda evropského filmu, suploval nám Hollywood](https://magazin.aktualne.cz/kultura/film/fila-belmondo-byl-nejvetsi-hvezda-evropskeho-filmu/r~879efe640fdd11ec98380cc47ab5f122/)

<small>Upozorňuji, že to není vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu jsem použil vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
