Title: Lisa: HP EliteBook 8440p
Date: 2010-11-29 15:09:00
Tags: hračičkování, linux, práce, tech

Pořídil jsem si [nový laptop](|filename|2010-10-25_novy-laptop.md). Jak jste si přečetli v nadpisu, je to HP EliteBook 8440p a na rozdíl od předešlého jsem se rozhodl mu dát jméno a to hned. Nazval jsem ho *Lisa*, protože je na leasing :) Mám rád jména, která se nabídnou tak nějak sama, třeba *Netvor* pro moje kolo.

Co se mi na něm líbí? Že je nový, odolný, výkonný a fajn. Líbí se mi matný displej, lampička nad klávesnicí, opravdu odolná konstrukce a zajímavá výbava. Nerozplývám se nad procesorem nebo grafickou kartou, protože jim nerozumím a ani rozumět nechci. Oplývám se naopak nad tím, jak svižně systém jede na RAMku a na baterku, i když tu výdrž bych si asi představoval lepší. No a s tou RAMkou… můžu mít otevřené Eclipse, Firefox, virtuály, no prostě kdovíco a jede to parádně, přičemž System Monitor mi navíc dává jasně najevo, že swap oddíl jsem na disku vyhrazoval prakticky zbytečně. Tímto povídáním o paměti zdravím hlavně majitele strojů Mac, především pak [@svecmichal](http://twitter.com/svecmichal).

Hned jak jsem si laptop vezl z Prahy, nainstaloval jsem do něj ve žlutém autobuse nejnovější Ubuntu, 64bit. Rozhodl jsem se zahrnout do článku výčet toho, co jsem musel někde hledat nebo řešit, než jsem se na počítači zabydlel. A to jsem se rozhodl nezabydlovat se příliš – nemám čas na kraviny, tak jsem jen proletěl nastavení a programy nahazuji za běhu podle toho, jak je zrovna potřebuji. Je to i dobrý způsob jak zjistit, že některé programy vůbec nepotřebuji :D

## Návody

**Jak [zprovoznit touchpad](|filename|2010-11-08_hamachi-na-ubuntu.md) v novém Ubuntu, kde už není HAL:**

-   přečíst si [tento post](http://newyork.ubuntuforums.org/showthread.php?t=1603683)
-   a zapamatovat si, že magická formule zní `synclient RTCornerButton=2 TopEdge=3000`

**Jak vypnout otravné zvuky v Ubuntu:**

-   v Preferences / Sound
-   v Preferences / Startup Applications
-   v Administration / Login Screen

**Jak naučit Git svoje jméno a jak nastavit barvičky:**

-   [http://help.github.com/…heat-sheets/](http://help.github.com/git-cheat-sheets/) (hned nahoře, ty dva řádky v configuration)
-   [http://jblevins.org/log/git-colors](http://jblevins.org/log/git-colors)

**Jak se nerozčilovat, že i když mám tutéž verzi Apache a tytéž konfiguráky, že to zase nejede:**

-   `a2enmod rewrite` ;)

**Nezapomenout na řádek do `.bashrc`:**

-   `export PATH=${PATH}:/home/honza/workspace/android-sdk/tools:/home/honza/bin`

**Jak rozjet Hamachi:**

-   viz [můj návod](|filename|2010-11-08_hamachi-na-ubuntu.md)

**Jak vypnout notifikace statusů v Pidginovi:**

-   [https://bugs.launchpad.net/…/+bug/339370](https://bugs.launchpad.net/ubuntu/+source/pidgin/+bug/339370) (jde to naklikat, ale těžko se to hledá)

**Jak přidat uživatele do MySQL:**

-   [http://dev.mysql.com/…g-users.html](http://dev.mysql.com/doc/refman/5.1/en/adding-users.html)

**Jak zašifrovat home po instalaci:**

-   [http://ubuntu.shapado.com/…fter-install](http://ubuntu.shapado.com/questions/how-to-encrypt-home-directory-after-install)

**Jak nainstalovat ffmpeg i s restricted blbinama:**

-   `sudo apt-get install ffmpeg libavcodec-extra-52`

## Co funguje pěkně a testoval jsem

-   webkamera
-   čtečka karet

## Co stále řeším, co nefunguje, co se mi nelíbí, nebo co nevím

-   čtečka otisků prstů [bez šance](http://twitter.com/#!/littlemaple/status/9233187414740993) (nebo [ne](http://twitter.com/#!/martin_javorek/status/9239350004940800)?)
-   svítící tlačítka nahoře mi nejde moc ovládat ani přemapovat (*touchpad*, *web*… naopak *mail* jede, nechápu)
-   přepínání EN/CS klávesnice v Ubuntu mám postaru windowsácky vždy na alt-shift, jenže na tomhle laptopu mi to funguje jen když mačkám v pořadí shift-alt … to je poměrně velké WTF, ale poměrně snadno se na to dá převyknout, co už nadělám
-   tethering s Androidem jsem nezkoušel a GSM modul taky ne (ale ten asi ani jen tak nevyzkouším a ani si nedělám velké iluze)
-   vůbec jsem nepochopil, jak funguje numerická klávesnice a podezřívám ji z toho, že prostě nefunguje… čert ji vem

No kdybyste chtěli nějak pomoct, tak svoje problémy s klávesnicí jsem shrnul [sem](http://www.linlap.com/wiki/hp+elitebook+8440p#comment_b07fe68646b9dd791d986ad4371c82ef).

## Závěr?

No jsem určitě spokojený :) . Vždyť má pěkný displej, zdá se být nezničitelný, funguje F7 a hlavně písmeno Z… no a na posun kurzoru v Eclipse nečekám věčnost :) Mise splněna. Jde se do práce.