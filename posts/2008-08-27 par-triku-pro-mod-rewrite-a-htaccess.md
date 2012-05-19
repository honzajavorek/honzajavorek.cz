Title: Pár triků pro mod_rewrite a .htaccess
Date: 2008-08-27 08:10:00
Tags: apache, mod_rewrite, php, projekty, webdesign

Velmi často je součástí webového serveru tzv. `mod_rewrite`, který
nám povoluje přepisovat jakékoliv požadavky od uživatele na jiné.
Například přepsat nebo přesměrovat adresu. Více o `mod_rewrite` a
souboru `.htaccess`, jenž s ním úzce souvisí, najdete třeba na
[Jak psát web](http://www.jakpsatweb.cz/server/htaccess.html). Ta
nejlepší helpka je však velmi pěkně napsaný
[originální manuál](http://httpd.apache.org/docs/2.0/mod/mod_rewrite.html).
Já se zkusím podělit o několik užitečných *code snippets*, které
jsem časem nashromáždil…

## Lomítka na koncích

Přesměruje adresy `tralala.com/venku/je/tma` na
`tralala.com/venku/je/tma/`.

    ::apache
    ## endslashes
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{ENV:REDIRECT_STATUS} ^$
    RewriteCond %{REQUEST_URI} !\/$
    RewriteRule (.*) $0/ [R=301,NE,L]

## Hezká a všelijaká URL pro aplikaci v PHP

Žádných složitých 50 regulárních výrazů na to, co vlastně s těmi
adresami chceme… Stačí jeden kouzelný řádek, který úplně vše
přesměruje na `index.php` a potom si adresu rozparsujeme přímo
v PHP (dostupná v `$_SERVER['REQUEST_URI']`).

    ::apache
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule . /index.php [L]

## Přesměrování RSS na FeedBurner

Chcete [statistiky přístupů](http://www.feedburner.com) na vaše
RSS, ale nechcete obtěžovat odběratele článků se změnami adresy?
Přesměrujte je. Není to tak snadné jak se zdá, protože přesměrování
se nesmí provést, když se na váš *feed* snaží dostat samotný
FeedBurner (to se pak logicky zacyklí). Sofistikovanější postupy
pro WordPress najdete
v [článku na AskApache](http://www.askapache.com/htaccess/redirecting-wordpress-feeds-to-feedburner.html),
já jsem si vystačil s tímto:

    ::apache
    ## feedburner
    RewriteCond %{HTTP_USER_AGENT} !^.*(FeedBurner|FeedValidator|Recent) [NC]
    RewriteRule ^feed/?$ http://feeds.feedburner.com/javorovelistky [R=302,L]

## Chybové stránky

Pokud zadáte relativní cestu, původní URL zůstane v adresním řádku
prohlížeče a zobrazí se vám tato chybová stránka. Pokud zadáte
absolutní, přesměruje se chyba zcela na soubor s chybovou stránkou
(což podle mě není dobrý nápad).

    ::apache
    ## errorpages
    ErrorDocument 404 /joss/?doc=_404
    ErrorDocument 403 /joss/?doc=_403

## Tatíček .htaccess

Neodolal jsem a nakonec ještě přidám několik osvědčených kousků
i pro samotný `.htaccess`. Někdy je dobré na web jen na oko zamezit
přístup, alespoň přes hlavní stránku. Jelikož ta se většinou volá
přes `index.php`, teoreticky stačí vložit do rootu webu
`index.html` a něco do něj napsat. Toto zajistí, že se určitě bude
HTML verze zobrazovat prioritně:

    ::apache
    DirectoryIndex index.html index.php

Skryté soubory by se neměly nikomu dostat do rukou. Správný server
má toto už v globálním nastavení, ale člověk nikdy neví…

    ::apache
    <Files ~ "^[\.]">
        Order allow,deny
        Deny from all
        Satisfy All
    </Files>

Nevíte jestli na cílovém serveru bude `mod_rewrite` a nechcete
riskovat *Internal Server Error 500*? Stačí vše obalit podmínkou…

    ::apache
    <IfModule mod_rewrite.c>
        RewriteEngine on
        ...
    </IfModule>

A co tak si nastavit PHP?

    ::apache
    <IfModule mod_php5.c>
        # development setting
        php_flag display_errors 1
        # safety
        php_flag register_globals 0
        # allowed stealing from other websites ;)
        php_flag allow_url_fopen 1
        # fu*king quotes...
        php_flag magic_quotes_gpc 0
        php_flag magic_quotes_runtime 0
        php_flag magic_quotes_sybase 0
        # yes, I love short open tags!
        php_flag short_open_tag 1
        # utf forever
        php_flag default_charset utf-8
    </IfModule>

## Závěrem

Pokud byste měli nějaké další dobré tipy, podělte se v komentářích.
Doufám, že se vám tyto útržky kódu budou hodit a usnadní vám život.
Ne že bych byl expert na `mod_rewrite` nebo nastavení Apache přes
`.htaccess`, ale už z toho co umím mohu usoudit, že jsou to opravdu
silné a velmi užitečné nástroje, bez nichž bych si dneska pohyb po
hostinzích nebo vlastním serveru představil jen stěží. Mnohdy je
sice možné řešit totéž jiným způsobem, ale touto cestou je to
mnohdy rychlejší, elegantnější a na pohled hezčí :) . Takže kdo
s nimi ještě nezačal… Hurá do toho!