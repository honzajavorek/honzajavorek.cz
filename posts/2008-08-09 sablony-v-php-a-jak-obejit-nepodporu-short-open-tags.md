Title: Šablony v PHP a jak obejít nepodporu short open tags
Date: 2008-08-09 16:26:00
Tags: joss, php, projekty

Jestliže vás nalákal nadpis a nechcete číst širší úvod do problému
šablon v PHP, poskočte o něco níže, tam už to tak široké není a
článek lze ve zdraví přebrodit celkem rychle ;) .

Píšete-li aplikaci v PHP a nejste-li v programování vepř, sele,
prasnice nebo něco k tomu blízkého (vyjma kance, kanec být můžete),
dříve či později pocítíte přinejmenším touhu
**oddělit prezentační vrstvu od zbytku**. Nabízí se několik
přístupů, co s touto touhou…

## Jamalalicha, paprťála, chánua, chánua, chánua

**Žádná** prezentační vrstva. Napaprťálujem to všechno do jednoho
klubka, PHP do HTML, XML do PHP, CSS nějak k tomu a budeme mít
binec, ale budeme to mít za 40 minut. Pokud po nás někdo kód
dostane do rukou, nemá šanci s ním něco provést. Jestliže chceme
oslovit kodéra, aby dělal na projektu úpravy, platíme mu poté pobyt
v Bohnicích nebo, pro jihomoravské, Černovicích. Člověk by se
divil, ale na takovém přístupu dnes stojí velké procento
existujících webů a to i takových, do nichž byste to při pohledu
zvenčí ani neřekli (nebo by vás napadlo, že je to sebevražda).
Autoři těchto projektů neřeší dilema Smarty vs. PHP (viz dále),
protože většinou ani nevědí, že taková řešení existují.

## Když vrstva, tak vrstva

Použijete **robustní šablonovací systém**, který vytváří opravdovou
vrstvu ve vaší aplikaci, možná bude větší než ona a dal by se
označit jako takový pseudojazyk někde mezi HTML a PHP. Dle mého
názoru nepříliš šťastná cesta, na můj vkus málo elegantní a
minimalistická. Nicméně hojně používaná a má davy zastánců.
Nejrozšířenějšími šablonami jsou [Smarty](http://www.smarty.net/)
([pěkný český návod](http://smarty.ronnieweb.net/)), ale existují
desítky.

## PHP je šablonovací systém – zlatá střední cesta?

Napíšete si
**jednu třídu v PHP, která vám vytvoří plně funkční šablony** a
místo pseudojazyka v nich použijete PHP. Zní to zvláštně, ale
opravdu to jde a dle mého názoru je to nejelegantnější řešení.
Nesmíte samozřejmě tahat logiku aplikace do šablon, ač je to
možné – v šabloně použijete PHP jen k nějakému tomu echo a foreach.
Alternativní syntaxe PHP jako *short open tags* nebo *if/endif*
přímo k takovému použití vybízí. Více
[třeba zde](http://massassi.com/php/articles/template_engines/).

## Ano, zlatá střední

Ve vodách internetu najdete neplodné, plodné, těhotné a i jinak
objemné diskuse o tom, jestli použít PHP jako šablonovací jazyk,
nebo nasadit moloch typu Smarty. Asi jak na co. Já mám zatím
jasno – jsem zastáncem **hbitých a chytrých řešení** a tyto
požadavky splňuje ona střední cesta, jak jsem ji vylíčil
v předešlém odstavci. Nechci se hádat co je lepší – prostě jen
napíšu, že pro mě je lepší tato varianta a proto mám rád takové ty
na první pohled obskurní věci, jako například short open tags:

    ::php
    <?= $var ?> je totez jako konvencni <?php echo $var ?>
    <? ... ?> je totez jako delsi <?php ... ?>

V běžném PHP je to celkem na uškrcení, ale v šablonách dle mého
názoru k nezaplacení.

## JTemplate

Ve svých projektech používám šablony postavené na vlastní třídě
[JTemplate](http://code.google.com/p/joss-cms/source/browse/trunk/class/JTemplate.php)
(tady se vyplatí kliknout, vážně). Spolu s dalšími
**umí výstupy cachovat** a tím razantně zvyšovat výkon aplikace.
V zásadě je postavená na myšlence popsané ve výše odkazovaném
článku Briana Loziera.

Čím je ale zvláštní? Funkcí `fetch`. Ta je jádrem zpracování a jde
v ní běžně o to, že se do aktuálního kontextu rozbalí proměnné
uložené do šablony (funkce
[extract](http://cz.php.net/manual/en/function.extract.php)), začne
se odchytávat výstup na obrazovku
([ob\_… funkce](http://cz.php.net/manual/en/ref.outcontrol.php)) a
vloží se (obyčejný include) soubor se šablonou jako PHP. V něm se
použijí rozbalené lokální proměnné a vše se poslušně vytiskne ven.
No ven úplně ne, protože výstup samozřejmě odchytáváme, takže vše
co jde ven hezky sbalíme do *output control pytle* a necháme
uložené jako string v nějaké proměnné, kterou vrátíme jako výsledek
funkce (a obsah pak v aplikaci vytiskneme později kdykoliv
chceme).

## Pro změnu… Short open tags!

„Takové krásné šablony,“ řekli byste. Ale pak to nahrajete na první
hosting a **celé se vám rozsypou**, protože tam mají
**vypnutou podporu short open tags**, které samozřejmě hojně a
s radostí používáte. Co s tím? Buď je nepoužívat (což je škoda),
nebo přidat jeden *požadavek* navíc a snížit tak možnost nasazení
aplikace. Nebo vymyslet něco chytrého ;) .

    ::php
    if (!ini_get('short_open_tag')) { // explicit short open tags support
        eval('?>' . preg_replace(
            array('~<\\?(\\s)~', '~<\\?=~'),
            array('<?php\\1', '<?php echo'),
            $this->tpl->content));

    } else {
        include($this->tpl->file); // include the file
    }

První větev testuje, jestli jsou krátké značky vypnuty. Jestli ne,
přejde plynule do `else`, kde proběhne zpracování přes `include`
běžným způsobem. Pokud jsou vypnuty (tzn. server je tvrdohlavý a
nepovolí je i přesto, že je v .htaccess a
[ini\_set](http://cz.php.net/manual/en/function.ini-set.php)
nastaveno aby zapnuty byly), dojde na slušné využití jedné
z tabuizovaných funkcí v PHP,
[eval](http://cz2.php.net/manual/en/function.eval.php) :) . Už
ten název…

Jeden kouzelný řádek totiž způsobí, že se vezme text zdrojového
souboru šablony, regulárním výrazem se v něm nahradí krátké značky
za klasické dlouhé s `<?php` apod. a předhodí se funkci `eval`,
která následně kód PHP vykoná. Ne, čistěji to nejde a přijde mi to
jako oprávněné a elegantní využití této funkce, které řeší významný
problém a stírá rozdíly v nastavení serverů. No jak by řekl Béda
Trávníček: „A to se vyplatí!“

Cachování samozřejmě zcela
**maže handicap většího potřebného výkonu**. Navíc, narazit na tak
tvrdohlavý server se jistě jen tak nepoštěstí… Ale za tu jistotu to
samozřejmě stojí. Teď už si můžeme pohodlně psát short open tags,
velmi rychle, přehledně a efektivně s nimi kódovat šablony a
nemusíme se ohlížet na nic a nikoho.