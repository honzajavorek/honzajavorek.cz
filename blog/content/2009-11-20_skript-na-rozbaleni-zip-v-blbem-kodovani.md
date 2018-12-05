Title: Skript na rozbalení .zip v blbém kódování
Date: 2009-11-20 11:27:00
Tags: linux, software

.zip je dost primitivní formát a pokud v něm zabalíme složky a soubory **s diakritikou** na Windows a budeme rozbalovat jinde (kdekoliv, kde nebude kódování windows-1250), tak si na tom grafický rozbalovač vyláme zuby a `unzip` z terminálu rozbalí vše, ale s podivnými znaky (takže se soubory nejde nic dělat, musí se nejdříve přejmenovat). Podobný problém bude asi fungovat i opačným směrem – pokud já zabalím něco v Linuxu do .zip, pravděpodobně se to podobně rozbije ve Windows.

Už dlouhou dobu (i na Windows) mám nejraději [7zip](http://www.7-zip.org/), asi nejlepší program na archivy vůbec. Má vlastní formát .7z, který je hodně parametrizovatelný a má skvělou kompresi. Rozbalí i zabalí .zip, .rar a spoustu jiných dalších typů archivů. **Navíc je zadarmo a je na všechny platformy.** Když můžu, používám ho místo .zip a nemám žádné problémy.

Pokud ale nějaký .zip přijde, nedá se nic dělat. Napsal jsem skript, který problém řeší:

    ::bash
    #!/bin/bash
    dirname=`echo "$1" | sed -e 's/\(.\+\)\.zip/\1/'`
    unzip $1 convmv -f cp1250 -t utf8 -r $dirname --notest

Pokud jej uložíme jako třeba `unzip-win`, rozbalíme archiv jako `./unzip-win bidny-kojot.zip`. Přeji bezproblémové rozbalování
:) .