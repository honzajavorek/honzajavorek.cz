Title: PNG a Internet Explorer
Date: 2007-08-30 11:54:00
Tags: explorer, gamma, png, software, webdesign

Tak pozor milý čtenáři! Avizoval jsem sice předem, že o tvorbě webu psát nechci a nebudu, ale protože jsem přišel na **něco skvělého**, prostě se podělit musím :) . Amerika ještě nebyla objevena celá, a to ani ve webdesignu! B)

## Alfa, béta, gamma

Většina webu se zabývá v souvislosti s PNG a IE **průhledností**, s níž má Explorer velké potíže. Jsou již na světe samozřejmě způsoby, jak to obejít, a rozumnému člověku stačí k jejich odhalení [Google](http://www.google.cz/search?q=png+internet+explorer). O čem se však téměř nikde nepíše (alespoň tedy česky), je také zvláštní zpracování **gamma** hodnot obrázků PNG v IE. Pokud tentýž obrázek PNG zobrazíš ve Firefoxu, Opeře a IE, zjistíš (a to i v IE7), že nejrozšířenější browser holt grafiku zobrazí s mírně **odlišnými odstíny barev**. Jedná-li se o obrázek uprostřed textu, zřejmě ti to bude docela fuk. Jestliže potřebuješ obrázek zasadit do přesného pixelového layoutu, zjistíš, že ti nesedí do barev vykreslovaných prohlížečem pomocí CSS nebo barev ostatních souborů.

## Spása drcením

Řešení? Existuje program [PNGcrush](http://pmt.sourceforge.net/pngcrush/), jenž si umí s formáty PNG a MNG docela slušně pohrát. Jedna z věcí, které dokáže, je právě optimalizace gamma hodnoty tak, aby se s ním popral i IE. Program je ke stažení i pod Windows – jedna *exe binárka*, nemusí se samozřejmě instalovat a spouští se z příkazového řádku. Soubor **pngcrush.exe** si tedy nahraj do adresáře se všemi *postiženými* obrázky a pak za hlubokých meditací prones magickou formuli

    ::bash
    pngcrush -rem alla -d out *.png

## Výsledek?

Výsledek skvostný :) . Vše se zobrazuje, jak má. Můžeme již jen provolat slávu Internet Exploreru, jelikož bez něj by byl náš webdesignerský život zcela **nudný a nezáživný**, rutinní… Měli bychom spoustu zbytečného času a hlavně, o dost méně práce. A to přece nikdo nechceme, vždyť nás tahle práce živí a **baví**… ;)