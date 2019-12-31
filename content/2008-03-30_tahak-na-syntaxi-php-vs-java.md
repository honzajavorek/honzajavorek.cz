Title: Tahák na syntaxi: PHP VS. Java
Date: 2008-03-30 18:05:00
Lang: cs
Tags: java, php

Ano, můžeme si otevřít knihy, můžeme zkoumat [PHP syntaxi](http://en.wikipedia.org/wiki/PHP_syntax_and_semantics) nebo [Java syntaxi](http://en.wikipedia.org/wiki/Java_syntax) na Wikipedii, číst si v referenčních webech… Ale to je zdlouhavé. Nabízím malý tahák pro stejně konvertované jako já – z PHP na Javu. Nesnažil jsem se o nic komplexního, Javu se z toho nenaučíte. Jde jen o výčet nejzákladnějších rozdílů v syntaxi, které se mohou plést, zvláště když jsou zažité…

<table>
    <tr>
        <th>
            část syntaxe
        </th>
        <th>
            PHP
        </th>
        <th>
            Java
        </th>
    </tr>
    <tr>
        <td>
            konstruktor
        </td>
        <td>
            <code>__construct()</code>, <code>Class()</code>
        </td>
        <td>
            <code>Class()</code>
        </td>
    </tr>
    <tr>
        <td>
            toString
        </td>
        <td>
            <code>$object->__toString()</code>
        </td>
        <td>
            <code>object.toString()</code>
        </td>
    </tr>
    <tr>
        <td>
            přístup ke statické proměnné/metodě
        </td>
        <td>
            <code>Class::$name</code>, <code>Class::name()</code>
        </td>
        <td>
            <code>Class.name</code>, <code>Class.name()</code>
        </td>
    </tr>
    <tr>
        <td>
            přístup k vlastní statické proměnné/metodě
        </td>
        <td>
            <code>self::$name</code>, <code>self::name()</code>
        </td>
        <td>
            <code>name</code>, <code>Class.name</code>, <code>name()</code>, <code>Class.name()</code>
        </td>
    </tr>
    <tr>
        <td>
            přístup k proměnné/metodě
        </td>
        <td>
            <code>$object->name</code>, <code>$object->name()</code>
        </td>
        <td>
            <code>object.name</code>, <code>object.name()</code>
        </td>
    </tr>
    <tr>
        <td>
            přístup k vlastní proměnné/metodě
        </td>
        <td>
            <code>$this->name</code>, <code>$this->name()</code>
        </td>
        <td>
            <code>name</code>, <code>this.name</code>, <code>name()</code>, <code>this.name()</code>
        </td>
    </tr>
    <tr>
        <td>
            (statická) konstanta
        </td>
        <td>
            <code>const NAME</code>
        </td>
        <td>
            <code>static final type NAME</code>
        </td>
    </tr>
    <tr>
        <td>
            přístup ke konstantě
        </td>
        <td>
            <code>self::NAME</code>, <code>Class::NAME</code>
        </td>
        <td>
            <code>NAME</code>, <code>Class.NAME</code>
        </td>
    </tr>
</table>

Mimochodem, když jsem hledal něco takového jako tento článek na internetu, narazil jsem na [pěkný tahák pro PHP](http://www.blueshoes.org/en/developer/php_cheat_sheet/).
