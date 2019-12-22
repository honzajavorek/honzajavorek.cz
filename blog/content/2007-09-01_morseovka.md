Title: Morseovka?!
Date: 2007-09-01 05:56:00
Tags: projekty, tábor

Něco málo o Morseovce a nakonec jeden bonus pro ty, jimž něco říká PHP. Na Wikipedii je [moc pěkný článek](http://cs.wikipedia.org/wiki/Morseova_abeceda) o Morseovce a bylo by k ničemu jej sem opisovat. Mohu ale informace o Morseovce rozšířit o nějaké své zkušenosti z [tábora](http://www.taborprekvapeni.net/).

## Jak zmást

Morseovka je tak známá a lehce prokouknutelná, že se většinou nepoužívá sama o sobě. Buď se ona sama do něčeho skryje, nebo v sobě skrývá text, který není řešením, ale má se dále luštit.

### Prohození

Můžeme zmást prohozením teček a čárek. Rozpoznat takové prohození lze i jednodušeji, než tím, že ti výsledný text nedává smysl. Stačí si všimnout, že některá písmena nemají svůj prohozený ekvivalent. Např. C je -.-., písmeno s kódem .-.- však neexistuje. Když takové najdeš v morseovkou psaném textu, mělo by ti být hned jasné, že tečky a čárky jsou prohozeny.

### Přepis do jiných znaků

Tečky a čárky vyloženě vybízejí k tomu, aby se zaměňovaly za něco jiného a tím se znesnadnilo čtení textu. Např. když namaluji místo teček hřiby a čárek stromy, hned je to o dost horší na rozpoznání. Nicméně, taková výměna je dost bídná, protože jen malinko zkušenější táborník to hned prokoukne a navíc se při kreslení stromečků člověk hrozně nadře.

Přepisovat se dá čímkoliv. Jedny z tužších šifer mohou např. považovat za čárku samohlásky textu a za tečku souhlásky. Moje oblíbené ;-) .

## Místo

Morseovka má určité vlastnosti. Jednou z nich je náročnost na místo. Text, kterým popíšete jeden odstavec, bude v Morseovce několikrát delší. Holt zabírá více místa, je to roztahanější.

Proto ale není třeba se leknout, když ti někdo podá velký papír popsaný Morseovkou. Ve skutečnosti budou písmenka ubíhat rychle a ač se toho zdálo na začátku moc, vyluštěno to budete mít za pár minut, protože textu v tom moc schovaného není.

## Rychlost

Morseovka není těžká a velmi snadno se lze naučit tak, že ji dokážeš číst nebo psát zpaměti, rychlostí, která se vyrovná rychlosti psaní/čtení běžného textu (chce to ale trénink a když vyjdete ze cviku, zase vám to chvíli trvá). Naučit se takto psát/číst Morseovku není vůbec nic k zahození a není to žádná hrůza – chce to jen často psát texty v Morseovce a cvičit a cvičit. Potom to můžeš dokázat i za několik dní (!). Morseovka byla navržená k tomu, aby mohla plnohodnotně nahradit text a kdyby ji lidé nemohli rychle číst a psát, nestala by se tak slavnou a rozšířenou.

## Morse v PHP

Protože jsou ale všichni programátoři líní, napsal jsem si v php5 třídu na převod Morseovky do českého textu a naopak. Umí všechny různé zápisy (lomítka, trubky, tečky, hvězdičky…), ale moc jsem to netestoval a moc jsem si s tím nehrál. Vydávám ji tímto pod [GPLv2](http://cs.wikipedia.org/wiki/GNU_General_Public_License).

Není to nic světoborného, napsal jsem to za 2 hodiny, protože na internetu jsem žádný dokonalý převaděč dle mých představ nenašel. Víc času tomu věnovat ani nechci, nehodlám to dále moc vyvíjet, poskytovat na to podporu apod. Pokud to použijete nebo budete rozvíjet dále, dejte mi prosím vědět nebo mi aspoň pošlete nové verze.

[Stahuj zde, morse.zip]({static}/files/morse.zip) (balíček s třídou, příkladem, licencí…)
