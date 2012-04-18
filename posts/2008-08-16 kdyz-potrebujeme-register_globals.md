Title: Když potřebujeme register_globals
Date: 2008-08-16 15:27:00
Tags: php

Stalo se tuším od jedné z podverzí PHP4 dobrým zvykem
**vypínat v PHP direktivu register\_globals**. Naštěstí. Díky tomu
pak nemáme přístup k příchozím datům přes různě pojmenované
proměnné, ale máme je hezky v globálních polích, třízena podle
způsobu, jakým k nám přišla. To je nejen o dost přehlednější, ale
také bezpečnější.

Co ale dělat, když máme nějaký starý projekt napsaný se zapnutými
register\_globals? Určitě je jednodušší je zapnout a případně si
pohlídat bezpečnostní rizika, než přepisovat celý kód. Máme tři
možnosti:

## Apache

Serveru řekneme co potřebujeme v souboru `.htaccess`.

    php_flag register_globals 1

## Změna nastavení přímo v PHP

Použijeme
[ini\_set](http://cz2.php.net/manual/en/function.ini-set.php).

    ini_set('register_globals','on');

## Nastavení na serveru nelze změnit

V tomto případě nám nezbyde, než si ručně proměnné vytvořit.

    extract($_REQUEST);