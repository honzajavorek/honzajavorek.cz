Title: Co s hudbou?
Date: 2012-01-22 20:00:00
Lang: cs
Tags: linux, management, software, ušima

Bohužel jsem multižánrový člověk a mám na disku 140 GB hudby. Nevím co s ní. Nedělám si iluze, že to všechno poslouchám nebo že to chci všechno nějak schraňovat. Poradíte mi?

Předem avizuji, že jsem [souborově založený člověk](https://github.com/Littlemaple/elk) a žádné divoké přehrávače s prohledávatelnými knihovnami nejenže neřeší níže nastíněný problém, ale ani nesmí na můj počítač.

Článek jsem uzrávat nenechával, nechtěl jsem tímhle trávit více času než je nutné. Proto je možná takový trochu *hrr* :-)

## Co bych s hudbou nejraději udělal

-   smazal bych radikálně vše, co neposlouchám
-   zrušil bych až na výjimky „sbírky“ (dilema *mít všechny Floydy* vs. *mít alba Floydů, která poslouchám*)
-   vyhledat duplicity a raději symlinkovat soubory, pokud je má opravdu smysl mít na více místech
-   vedle složky s alby a případnými kusovkami bych udělal složku s mixy, kde jsou pečlivě namíchané playlisty podle různé nálady
-   otagoval správně veškerou hudbu, irituje mě jak je všechno strašně nesourodé a neorganizované

## Problémy

-   jak poznat co neposlouchám?
-   jak vyhledat duplicity v písničkách (soubory nemusí mít stejný název ani velikost – např. když jsou v různém bitrate)
-   jak otagovat hudbu?

Popravdě, s tím mazáním bych si poradil. Duplicity jsou horší, ale i to jde algoritmicky řešit, můžu si za dvě hodiny napsat skript, který bude chytřejší než běžné hledače duplicitních souborů. Co ale s těmi tagy?

-   tagování, struktura a vše je naprosto chaotické
-   konvence pojmenování souborů je naprosto chaotická
-   žádný nástroj neproleze celou mou hudbu a neotaguje ji spolehlivě (ani [MusicBrainz Picard](http://musicbrainz.org/doc/MusicBrainz_Picard)), je nutná účast člověka a já s tím nechci strávit půl života ani to ručně udržovat
-   vyhovovala by mi netradiční struktura:
    -   `folk/Xavier Baumaxa/2003 - Fenkám/01 Nedělní chvilka poesie.mp3` pro umělce s více alby
    -   `pop/Kryštof - Poločas/01 Plán.mp3` pro umělce s jediným albem
    -   `pop/Mig 21/Mig 21 - Chci ti říct.mp3` pro kusovky zařaditelné k umělci, od něhož mám nějaká alba
    -   `mixes/.../Britney Spears - Toxic.mp3` pro úplné kusovky, které mám jen tak
    -   Žádné jiné informace než ty o umělci, albu, roku, čísla tracku a názvu tracku mě nezajímají. Nechci aby tam překážely nějaké komentáře typu *tohle je z iTunes, milujte iTunes a množte se* nebo *music from ultrawesome mega hyper ganjatorrent*.

## Řešení?

Nemám tušení. Není to algoritmizovatelné, je to šíleně **fuzzy**, není to řešitelné. Navíc mám spoustu alb neúplných nebo takových, které v žádných registrech nejsou (různé výběry, world music, čeští a slovenští interpreti, …).

Jeden můj kamarád údajně **smazal všechnu svou hudbu** – řekl si, že může poslouchat online rádia a že poslouchání stále téže hudby jej nikam dál neposouvá. OK, to už je hodně radikální, ale mojí sbírce by určitě nějaký podobný přístup prospěl.

### Mazání

Uvažuji, že bych promazal drtivou většinu věcí. Jen máloco z hudby není v tomto směru obnovitelné. Kritériem bude otázka:

> Jsem si stoprocentně jistý, že si tuto hudbu chci nechat, že se mi
> líbí a že ji poslouchám?

Odpověď **ne** vede ke klávese *delete*.

### Rušení alb

Potom bych zrušil drtivou většinu alb. Jen málokdy se mi líbí celé. Pouštím si sice hudbu po albech, ale vlastně mě to baví o dost méně než si ji pouštět namixovanou. Drtivá většina alb má 3 dobré písničky a zbytek je o ničem. Život je krátký na to poslouchat průměr. Kritériem ponechání či rozebrání a promazání bude otázka:

> Pouštěl bych si často toto album jako celek? Líbí se mi celé?

### Mixy

Tím mi zbude pár alb, jejichž existenci i obsah jsem si 2× obhájil a které zřejmě půjde ručně udržovat. Zbytek přesunu do mixů nebo smažu. Mixy potom nebudou nijak třízeny, bude to plochá struktura – např. bad mood, africa, good morning, reggae, classic rock, pop, club, sentimental… V každé složce budou prostě jen naházené soubory bez jakéhokoliv ladu, skladu, koncepčního tagování, pořadí (přehrávač má přece *shuffle*), atd.

## Správná cesta?

Hudba se změnila. Už nelze mít vše utřízené a organizované jako to šlo, když světu vládly gramodesky, kazety, nebo CD. Musím se zřejmě změnit taky. Změnit přístup a jestliže jsou data, která se snažím třídit, takto chaotická, tak potom musí zřejmě i mé třízení být co nejplošší a nejméně komplikované. Vlastně takové *netřízení*. Jinak bych se zbláznil nebo nedělal nic jiného, než že bych třídil hudbu. Nebo ne? Existuje jiná cesta?
