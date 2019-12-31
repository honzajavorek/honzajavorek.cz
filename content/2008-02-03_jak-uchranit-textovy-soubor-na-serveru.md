Title: Jak uchránit textový soubor na serveru
Date: 2008-02-03 12:30:00
Lang: cs
Tags: apache, php, projekty

Dnes jen krátce malý trik, jak uchránit soubory textového typu na serveru. Pokud si na `www.example.com` nahraji nějaký `velikost-poprsi.txt`, pak si jej logicky každý může přečíst na adrese `www.example.com/velikost-poprsi.txt`. Někdy je to ale nežádoucí – např. pokud si uchováváme [konfigurační data aplikace v XML](http://interval.cz/clanky/konfiguracni-soubor-v-php-ve-formatu-xml/) nebo v textovém souboru (třeba [INI soubor](http://en.wikipedia.org/wiki/INI_file), zpracovávaný
pomocí [parse\_ini\_file](http://cz2.php.net/manual/en/function.parse-ini-file.php)).

## Nastavení serveru přes .htaccess

Konfigurační `velikost-poprsi.txt` si například dáme do nějakého adresáře, do něhož umístíme i .htaccess soubor s obsahem

    :::apache
    deny from all

Server pak **všechny vnější požadavky** na soubory ve složce **zamítne** (HTTP Error 403 – Forbidden).

## Nemáme .htaccess

Co když nemáme nastavení přes .htaccess k dispozici? Použijeme malý trik, kdy soubor přejmenujeme na `velikost-poprsi.php` a znemožníme přístup zvenčí okamžitým **ukončením vykonávání skriptu** hned na začátku. Aplikace soubor načítá lokálně, takže jí to nijak nemusí vadit, pokud samozřejmě PHP kód řádně zakomentujeme.

    :::ini
    ; <?php exit; ?> leve = A prave = C

Pro XML by mělo fungovat něco podobného.

    :::xml
    <!-- <?php exit; ?> --> <conf> <const name="leve">A</const> <const name="prave">C</const> </conf>

Samozřejmě, pokud použijete XML deklaraci, přijde vám na pomoc také [parse error]({filename}2007-12-20_xml-deklarace-a-php.md). **Nelze se však na něj spoléhat** a určitě je dobré vše pojistit oním PHP v komentáři, protože parse error může, ale nemusí nastat (nedojde ke kolizi, když má vaše PHP direktiva `short_open_tag` hodnotu `0`).
