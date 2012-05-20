Title: Parametry Firefoxu
Date: 2008-01-23 11:58:00
Tags: firefox, linux, software, windows

![obrázek](images/37.jpg){: .right }Většina z nich klikne na ikonku modrého Exploreru. Většina z nás klikne na ikonku Firefoxu. Někteří z nás spustí [Launchy](http://blog.javorek.net/2007/12/29/launchy/) a na nic neklikají. Někteří se [nebojí příkazového řádku](http://blog.javorek.net/2007/08/30/png-a-internet-explorer/#comment-2514).

Firefox lze spouštět i z CLI, popřípadě jej obdařit parametry v zástupci. Co tím získáme? Můžeme vynutit nějaké chování nebo použít Firefox ve skriptech pro operační systém. Parametry samozřejmě fungují jak na Linuxu, tak ve Windows:

    ::bash
    firefox -p

Samozřejmě vám musí Firefox stát „v cestě“, čehož docílíte nejlépe tak, že před něj přidáte cestu k jeho instalaci/binárce. Ve Windows toho lze využít při tvorbě zástupců.

## Užitečné paramtery

-    `-profile <cesta>` spustí se s předaným profilem
-    `-CreateProfile <název> <cesta>` vytvoří nový profil
-    `-ProfileManager` spustí se se správcem profilů
-    `<internetová adresa>` otevře stránku
-    `-new-window <adresa>` spustí v novém okně
-    `-new-tab <adresa>` spustí v novém panelu
-    `-search <slova>` vyhledá slova ve výchozím vyhledávači
-    `-chat` spustí se s IRC klientem ChatZillou, pokud jej máte
-    `-safe-mode` spustí se v záchranném režimu (bez rozšíření apod.)
-    `-height <číslo>` spustí se s předanou výškou okna
-    `-width <číslo>` spustí se s předanou šířkou okna
-    `-setDefaultBrowser` Firefox se nastaví jako výchozí browser

Přesný seznam se všemi detaily lze samozřejmě najít [v angličtině v dokumentaci Mozilly](http://developer.mozilla.org/en/docs/Command_Line_Options).