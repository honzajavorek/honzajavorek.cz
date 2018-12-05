Title: Hamachi na Ubuntu
Date: 2010-11-08 18:11:00
Tags: linux, práce, software

Opět využiju svého blogísku jako zápisníku, kam utrousím věci, jež nechci zapomenout. Brzy mě čeká zase instalace Ubuntu a tak budu potřebovat vědět, že pokud na něm chci mít funkční Hamachi (kvůli klientovi), musím…

## Jak nainstalovat Hamachi

Stáhnout [Hamachi pro Linux](http://files.hamachi.cc/linux/hamachi-0.9.9.9-20-lnx.tar.gz) a rozbalit. Potom:

    ::bash
    $ sudo apt-get install build-essential   # máme vše potřebné pro instalaci?
    $ sudo make install   # instalujeme
    $ sudo tuncfg   # nastavení tuneláže
    $ hamachi-init -f   # vytvoření metadat Hamachi v ~/
    $ hamachi start   # start Hamachi
    $ hamachi login   # přihlášení do Hamachi

## Jak používat Hamachi

Další práce s Hamachi, tedy nastavení jména, přihlášení do skupiny, nastavení online stavu a výpis toho co vidím:

    ::bash
    $ hamachi set-nick [nick]
    $ hamachi join [network] [password]
    $ hamachi go-online [network]
    $ hamachi list

## Zajímavé odkazy

-   [GUI pro Hamachi](http://www.webupd8.org/2010/05/script-to-install-hamachi-with-gui-in.html)
-   [Poměrně komplexní návod na Hamachi](http://www.supware.net/other-fun-stuff/hamachiubuntuhowto/) (vytisknout a přečíst v důchodu nebo na záchodě)
-   [Návod na UbuntuForums, Hamachi jako služba s VPN](http://ubuntuforums.org/showthread.php?t=135036)
-   [Oficiální návod](http://logmeinwiki.com/wiki/Hamachi:Install_on_Linux)
-   [Oficiální fórum](https://forums.hamachi.cc/viewforum.php?f=15)
-   [Jak odinstalovat](http://logmeinwiki.com/wiki/Hamachi:Uninstall_on_Linux)

## Zkušenost

Nejlepší způsob, jak používat Hamachi, je vyhnout se mu.