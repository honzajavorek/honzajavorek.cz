Title: Kolonizátoři a správci kolonií
Date: 2016-12-18 13:43:00


Vyměňme na chvíli vánoční čepičky za přilby [conquistadorů](https://cs.wikipedia.org/wiki/Conquista). Propůjčím si imperialistickou terminologii k tomu, abych odlišil dvě skupiny programátorů a upozornil na nešvary, které vznikají, když toto rozdělení ignorujete.

## Kolonizátor

![Kolonizátor]({filename}/images/conquistador.png){: .right }[Cortés](https://cs.wikipedia.org/wiki/Hern%C3%A1n_Cort%C3%A9s)! [Pizarro](https://cs.wikipedia.org/wiki/Francisco_Pizarro)! Tihle chlapíci se s tím moc nepárali. Na mapě bylo bílé místo a jejich pověřením bylo zjistit, co tam je, a zařídit, aby to bylo za každou cenu co nejdříve pod španělskou vlajkou.

Kolonizátor pracuje rychle a efektivně. Dostal polovičaté zadání, ale není tady od toho, aby se na něco ptal. Jeho úkolem je doručit výsledek. Vytvořit [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product). Sestrojit prototyp, aby se dal validovat trh. Dokončit něco, protože zítra je demo.

Chtějte nemožné a kolonizátor vám to doručí. Sice přes mrtvoly, ale doručí. Agenturní práce? [Noviny](https://www.zdrojak.cz/clanky/co-se-vyvojar-nauci-v-novinach/)? První rok startupu? Žádný problém. Rychle měnící se zadání? Jednorázová práce? Tihle ostří hoši nehnou brvou.

## Správce kolonií

![Správce kolonií]({filename}/images/governor.png){: .right }Na mapě dobytého území už jsou první osady, domorodé obyvatelstvo je zpacifikované, Cortés se posunul někam dál za obzor. Co teď? Nastupuje správce. Zatímco kolonizátor nešel daleko pro nějakou tu genocidu, úkolem správce je spíš domluvit se s místními na kompromisech a situaci stabilizovat. Podpořit rozvoj krajiny, rozjet výnosy, udělat místo pro nové osadníky.

Správce hledá řád. Navrhuje, refaktoruje, rozvažuje, uklízí, pětkrát měří, než něco uřízne. Sv. Linter a Sv. Coverage dostanou kostely uprostřed osady. Dbá na čitelnost kódu a dokumentaci, protože ví, že jsou to základy týmové spolupráce. Většinu chatrčí strhne a postaví domy z kamene, jež se budou do budoucna lépe udržovat.

Tenhle budovatel sem nepřišel na jedno léto. Sice by od srdce nejraději něco pořád dokola začínal na zelené louce, ale sám tuší, že nejlépe mu je na produktu s validovaným trhem a jasnými představami o dalším směřování. Potřebuje se rozhlédnout po osadě a cítit ve vzduchu, že až odejde, zůstane po něm město s hradbami a katedrálou.

## Honza šel do světa

Abychom se nemotali pouze v opisech, přiložím dojemné příběhy z vlastního života.

Hloupý Honza šel do světa a zavadil v roce 2013 o firmičku s názvem Skypicker. Skládala se asi ze tří lidí a měla hotový prototyp svojí služby. Už tehdy si Honza uvědomoval, že existuje buďto krásný a upravený kód, nebo kód, který vydělává peníze. Jenže to, co viděl ve Skypickeru, ho i tak překvapilo. Firma byla navíc nastavená čistě na výsledky, takže co neprodukovalo uchopitelné hodnoty, to nebylo zaplaceno. Honza tam vydržel měsíc.

Dnes už je Honza o něco méně hloupý a ví, že je správce. A správce ve startupu o třech lidech nemá co dělat. Taková firma potřebuje kolonizátory. Skypicker si je sehnal, neslevil ze svého přístupu a dnes je z něj [Kiwi.com](http://kiwi.com/). S šedesáti (?) vývojáři dnes už zaměstnávají i nějaké budovatelské povahy. Občas za Honzou chodí a říkají, že pod sedimenty narazili na jeho commit.

Honza nyní pracuje v [Apiary](https://apiary.io/), kam přišel zhruba v době, kdy začínalo mít smysl investovat do nějakých prvních správců. Produkt Apiary má více částí a firma historicky vždy vyslala nějaké kolonizátory vytvořit prototyp, aby se zjistilo, zda má něco vůbec smysl. Ve chvíli, kdy trh ukázal, že je o danou věc zájem, přesunuli se dobyvatelé jinam a nastoupili správci, kteří začali uklízet po válce a budovat.

## Střet dvou světů

Je problém, pokud správce dostane za úkol kolonizovat území a naopak. Také vznikají třenice, když mají lidé na něčem spolupracovat nebo si třeba i jen předávat práci a neuvědomují si přitom své "imperialistické" role.

### Těžký život kolonizátorů

Dobyvatelé jsou často šikanováni kolektivem, který jejich práci přebírá. Lidé komentují kvalitu dřevěných chatrčí, místo aby si uvědomili, že nebýt onoho chlapíka v zakrvaveném brnění, nestálo by tam nic a nemělo by to ani jméno. Že to, na co koukají, bylo napsáno ve tři ráno den před termínem nebo v době, kdy nikdo nevěděl, jestli má smysl v projektu vůbec prokračovat. Pro nové osadníky je to "prasokód" a "legacy". Kolonizátor končí s nízkým sebevědomím nebo v neustálé defenzivě.

### Kolonizátor správcem

Když necháme dobyvatele spravovat nově založenou kolonii, dokáže to. Klidně několik dalších let. Jenže už nikdy se k němu nikdo nepřidá. Kód nebude ve stavu, že by mu mohl porozumět ještě někdo další. Projekt po technické stránce začne fárat do nekonečné šachty. Z té není cesty ven - dá se pouze sjet ještě hlouběji, nebo začít odznova a věc bolestivě přepsat. Pokud se kolonizátor přestane projektu věnovat, je to často konec - nikdo jiný není schopen na témže území operovat.

### Pyšní správci

Správci vidí, že píšou lepší kód než kolonizátoři, ale nedokážou odhadnout, kde je jejich vlastní strop. Každý správce si myslí, že právě on je nejlepším správcem a zorganizuje věci nejlépe. Navrhne nejlepší strukturu, rozmyslí nejlepší řešení. Zatímco kolonizátor vždy udělá jen nejnutnější, správci mají problém pochopit daný kontext a odlišit důležité od zbytného. Řešení správců mohou nesmyslně nabobtnat do předimenzovaných, příliš robustních, příliš obecných. Správce sám o sobě tedy nezaručuje, že projekt půjde dobrou a rentabilní cestou.

### Správce kolonizátorem

Správce kolonie najmutý na dobytí neznámého území je jako koule na noze. Místo, aby chrlil prototypy, které ověří myšlenku a potvrdí, že v blízkých horách lze těžit zlato, bude se týdny točit v opravování style guide warnings a refaktorování toho, co napsal předchozí den. Pokud misi úplně nezabije, tak ji minimálně zbrzdí a propálí hromadu peněz.

### Házení špíny

Správci kolonie jsou mistři v práci s `git blame`. Sice by bez kolonizátora vůbec nemohli existovat, ale to jim nedochází. Dobývání neznámých obzorů by běžný správce buď nechtěl dělat nebo vůbec nezvládl. Jenže bez prvotních osad by nebylo co spravovat. Nic by se nerozjelo, nikdo by správce nezaplatil. Správně by tihle budovatelé měli být kolonizátorům vděční, měli by obdivovat jejich odvahu, výdrž a ochotu vrhat se do krvavých bitev. Místo toho na ně u kafe v odpolední pauze hážou špínu.

## Výzvy

Velkou výzvou pro kolonizátora je nenechat se zlikvidovat kolektivem, uvědomit si vlastní hodnotu, svoje slabiny a sám se snažit podílet na projektech, na nichž může svoje schopnosti nejvíce uplatnit. Může se učit rozvaze a disciplíně, aby z něj mohl být jednou správce, ale není to nutné. Svět potřebuje i střelce.

Obrovskou výzvou pro správce kolonií je pokora. Nedělat z `git blame` nástroj šikany, ale podívat se na čas commitu (ranní hodiny?), dohledat původního autora, poplácat ho po zádech a doptat se jej na co nejvíce kontextu. Nesázet tolik na to, že všechno ví nejlépe. Najít hranici mezi tím, co se bude do budoucna hodit a co je v dané fázi projektu zbytečná optimalizace, overegnineering, přiliš brzké DRY, apod. Nejet dakonicky podle pouček z knížek.

## Poznali jste se?

Jste dobyvatelé nebo budovatelé? A co vaši současní nebo minulí kolegové? Nebo je to složitější? Diskutujte pod článkem!
