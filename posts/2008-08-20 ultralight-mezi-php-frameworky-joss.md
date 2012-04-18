Title: Ultralight mezi PHP frameworky: Joss
Date: 2008-08-20 07:54:00
Tags: joss, php, projekty

![image](http://blog.javorek.net/image/64/)Před časem jsem se na
blogu zmínil, že se
[narodil Joss](http://blog.javorek.net/narodil-se-joss/). Dneska
bych chtěl konečně napsat, co
[Joss](http://code.google.com/p/joss-cms/) je, proč se narodil a
proč byste si ho měli stáhnout a používat. Od 14. srpna navíc ve
[zcela nové verzi 1.1.1](http://joss-cms.googlecode.com/files/joss1.1.1.zip),
která přináší opravy a mnohé nové funkce a pokud jste něco vyvinuli
na starém Jossu, asi vám dá trochu do těla (**není** zpětně
kompatibilní).

## Specialista na malé weby

Joss je takový… ultralight mezi frameworky. A jednou možná
i redakčními systémy v PHP(5). Nejpůvodnější jádro aplikace vzniklo
na základě nápadu za dva dny, zbytek se pak asi půl roku vyvíjel,
ladil, upravoval a doplňoval.

Jeho výhodou je to, že skoro nic neumí :) . Umí přesně jednu
jednoduchou věc, ale pořádně. Nevystavíte nad ním sice tedy portál
s fotogalerií, fórem a blogem, ale web o pěti stránkách s ním
zvládnete sakramentsky rychle.

Joss navíc vytvoří web **hezky**. Tak, jako kdybyste ho udělali
ručně za spoustu hodin, kdybyste si s tím chtěli fakt vyhrát a
nezapomenout na každý detail. Programoval jsem ho proto, že mi
chyběl „framework“ na velmi jednoduché weby. Takové, kde
nepotřebuji formuláře, kde neřeším žádné složitosti, ale chci na
nich mít pěkně kódovaný obsah a nechci je dělat otrocky v `.html`
souborech. Takové, kde mohu velmi pohodlně editovat obsah stránek –
zcela jednoduše na bázi textových souborů zapsaných
v [Texy!](http:www.texy.info). Když přidám soubor, vytvořím
automaticky stránku. Když jej upravím, upravím ji. Smažu? Smažu
stránku! :)

## Proč použít Joss?

-   umožňuje **bleskové vytvoření malých a středních webů** bez
    klikací uživatelské administrace
-   framework **lze pochopit asi za hodinu** čtení dokumentace a
    hrátek s kódem
-   framework má **jen pár set kilobajtů**
-   malé požadavky, instalace a konfigurace na **pět minut**,
    přesun webu jinam je na **tři minuty**
-   pro psaní vlastního obsahu webu **nemusíte znát HTML** – web je
    kompletně v Texy! souborech

## Co umí, čeho je schopen, co v sobě skrývá

-   umožňuje více jazykových verzí webu
-   rozšiřitelnost syntaxe na bázi pluginů (+ několik již
    připravených)
-   řeší základní a notoricky známé i méně známé nástrahy PHP a
    HTTP/HTML
-   cachuje výstupy (tzn. je rychlý)
-   obsahuje [Texy!](http://www.texy.info) a některé části
    z [Nette](http://nettephp.com) (cca 4 :) )
-   obsahuje jednoduchý RSS agregátor, snadno pracuje s XML
-   automatické generování sitemap.xml, robots.txt, .htaccess, …
-   tvoří pěkný a validní XHTML kód
-   automaticky generuje hlavičku webu, sám připojí styly, favicon,
    skripty, …
-   stará se o chybové stránky (404, 403, …)
-   podpora pro hierarchická menu
-   konfigurace (dříve v INI, teď v XML)

## Co nikdy umět nebude

-   formuláře, dynamické prvky, … (Joss nikdy nebyl k těmto
    činnostem zamýšlen a proto by jejich implementace do návrhu nebyla
    moc dobře možná)

## A co se chystá?

Mno, už nic moc, já jsem spokojen ;) . Ještě by se mi šikl
jednoduchý a snadno ovladatelný backend na jedno heslo, kde bych si
já nebo třeba i klient mohl upravit web i bez handlování se soubory
a FTP. Ale to je spíš daleký horizont, moc jsem to nepromýšlel a
hlavně bych k tomu chtěl použít jen vrstvu obsahující
JavaScript/AJAX (ano, bez něj si prostě web přes prohlížeč
neupravíte, holt smůla). A to já zatím neumím :) .

## Ale co ty složitější věci?

Na složitější věci použijte jiný, robustní PHP framework. Joss byl
vytvořen k tomu, aby neuměl nic, ale aby to nic zvládal perfektně.
Já se teď učím Nette, ale frameworků je spousta (dokonce, na rozdíl
od Nette, s dokumentací ;) ).

-   [CodeIgniter](http://codeigniter.com/)
-   [CakePHP](http://cakephp.org/)
-   [Zend Framework](http://framework.zend.com/)
-   [Nette](http://nettephp.com/)

## Takže?

Jak se vám líbí? Napsal jsem k Jossu českou dokumentaci (za chyby
neručím, je složité udržovat v ní aktuální změny ve funkčnosti… ale
snažil jsem se…), kousek anglické, testoval jsem ho, stavěl na něm
weby. Máte chuť se nějak podílet (třeba… anglická dokumentace),
testovat, diskutovat? Nikdo vám nebrání! Je poptávka po kompletní
anglické dokumentaci? Máte nějaký nápad na novou funkci?
Napište mi!

Přeji do života Jossu hodně štěstí a doufám, že bude líbit.
A hodit! :P