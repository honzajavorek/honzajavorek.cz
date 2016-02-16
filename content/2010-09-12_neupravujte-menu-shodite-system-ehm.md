Title: Neupravujte menu, shodíte systém... ehm
Date: 2010-09-12 10:31:00
Tags: fail, linux, software, windows

Jelikož mě [předchozí geekovina]({filename}2010-07-24_kdyz-je-na-disku-malo-mista.md) od té doby co jsem ji napsal asi tak 10× znova zachránila, padám sem honem napsat další.

Nevěřili byste, kam se můžete v GNOME dostat pouhou editací menu. Přestože mám GNOME a Linux rád, nebudu zastírat, že tohle je naprostá idiocie systému. Od začátku: Zdálo se mi, že nemám menu pro aplikace až tolik hezké a že bych mohl pár položek přejmenovat a nějaké vyházet. To jsem udělal a následně mi zkolaboval systém a při spuštění se nenačtaly okraje okýnek. Nedařilo se mi za boha najít příčinu, restartoval jsem několikrát celý okenní manažer, Metacity, přeinstalovával co se dalo. Bez reakce. Jediné co pomáhalo bylo dát Metacity do programů po spuštění, ale to bylo dost blbé řešení, něco jako kdybych díru na autě zalepil izolepou.

Nebudu vás napínat, po ztracené hodině času jsem [našel na fórech problém](http://ubuntuforums.org/showpost.php?p=7610738&postcount=4) který jasně říká, že když se v menu odstraní ty špatné věci, tak se přesně tohle stane. Smazal jsem nějaká lokální nastavení v `~` a najednou se to rozjelo… Uff… WTF?!

Protože se tím menu vrátilo do zcela prehistorického stavu a spolu s ním se *vyčistilo* i menu od Wine, tady je příkaz, kterým lze win aplikace do menu vrátit:

    export WINEPREFIX=~/.wine; find $WINEPREFIX/drive_c/ -name "*.lnk" -exec wine winemenubuilder '{}' \;

Našel jsem ho [tady](http://forum.winehq.org/viewtopic.php?t=3769). To se nehodí jen v těchto krizových případech, ale kdykoliv se vám povede přes editor menu to Wine menu rozkopat.

Závěr: Mezi Windows a Linuxem žádný rozdíl není. Co vás nenasere v jednom, nasere vás v druhém. Prašť jak uhoď. Ale Linux je zadarmo, líp se v něm programuje a má hezčí okýnka :D
