Title: Tahák na syntaxi: PHP VS. Java
Date: 2008-03-30 18:05:00
Tags: java, php

Ano, můžeme si otevřít knihy, můžeme zkoumat [PHP syntaxi](http://en.wikipedia.org/wiki/PHP_syntax_and_semantics) nebo [Java syntaxi](http://en.wikipedia.org/wiki/Java_syntax) na Wikipedii, číst si v referenčních webech… Ale to je zdlouhavé. Nabízím malý tahák pro stejně konvertované jako já – z PHP na Javu.
Nesnažil jsem se o nic komplexního, Javu se z toho nenaučíte. Jde jen o výčet nejzákladnějších rozdílů v syntaxi, které se mohou plést, zvláště když jsou zažité…

<table>
    <tr>
        <th>část syntaxe</th>
        <th>PHP</th>
        <th>Java</th>
    </tr>
    <tr>
        <td>konstruktor</td>
        <td>`__construct()`, `Class()`</td>
        <td>`Class()`</td>
    </tr>
    <tr>
        <td>toString</td>
        <td>`$object->__toString()`</td>
        <td>`object.toString()`</td>
    </tr>
    <tr>
        <td>přístup ke statické proměnné/metodě</td>
        <td>`Class::$name`, `Class::name()`</td>
        <td>`Class.name`, `Class.name()`</td>
    </tr>
    <tr>
        <td>přístup k vlastní statické proměnné/metodě</td>
        <td>`self::$name`, `self::name()`</td>
        <td>`name`, `Class.name`, `name()`, `Class.name()`</td>
    </tr>
    <tr>
        <td>přístup k proměnné/metodě</td>
        <td>`$object->name`, `$object->name()`</td>
        <td>`object.name`, `object.name()`</td>
    </tr>
    <tr>
        <td>přístup k vlastní proměnné/metodě</td>
        <td>`$this->name`, `$this->name()`</td>
        <td>`name`, `this.name`, `name()`, `this.name()`</td>
    </tr>
    <tr>
        <td>(statická) konstanta</td>
        <td>`const NAME`</td>
        <td>`static final type NAME`</td>
    </tr>
    <tr>
        <td>přístup ke konstantě</td>
        <td>`self::NAME`, `Class::NAME`</td>
        <td>`NAME`, `Class.NAME`</td>
    </tr>
</table>

Mimochodem, když jsem hledal něco takového jako tento článek na internetu, narazil jsem na [pěkný tahák pro PHP](http://www.blueshoes.org/en/developer/php_cheat_sheet/).