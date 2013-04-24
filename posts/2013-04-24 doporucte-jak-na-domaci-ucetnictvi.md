Title: Doporučte jak na domácí účetnictví
Date: 2013-04-24 22:35:17

Pokud si chce člověk vést nějaké základní domácí účetnictví, má několik možností.

1.  Vést si **ručně psaný sešitek** a vše si do něj zapisovat, pak to sčítat, apod.
    Funguje, ale vyžaduje to hodně energie. Vhodné outsourcovat u manželky,
    pokud ji máte, ale i tak musíte schovávat každý lístek z Billy a nechat
    barmana zapisovat vám piva na hřbet ruky, abyste mohli provádět kvalitní
    kolekci dat.
2.  Platit většinu věcí kartou, **stahovat si výpisy z internetového bankovnictví**
    a cpát to do nějakého programu. Strávíte tři dny vybíráním programu, zavrhnete
    [ty online](http://www.smoneybox.com), protože jsou pro USA, jsou moc jednoduché,
    nebo prostě proto, že nechcete posílat informace o svých účtech nikam dál než
    k vodnímu příkopu svého opancéřovaného domu. Zkusíte [pár klasických](http://www.gnucash.org/),
    ale zjistíte, že mají 2000 tlačítek a 400 funkcí, z nichž jste pochopili jen křížek
    v pravém horním rohu.
3.  **Vzdáte to** a budete věřit svému třetímu oku a šestému smyslu. Už léta přece
    dokážete i bez excelů, grafů a virgulí cítit vibrace svých peněžních toků a
    na sekundu přesně poznáte moment, kdy byste si v baru už neměli dát dalších
    osm Jamesonů, protože byste pak už nemuseli zaplatit zálohy sociálce za aktuální
    měsíc. Když se jakožto mistr tesař náhodou utnete, vždy to nějak vyžehlíte metodou
    [Not Giving a Fuck!](https://www.youtube.com/watch?v=6wS5xOZ7Rq8)

Ujasnil jsem si, že od svého účetnictví chci těchto pár věcí. V nejlepším případě
nechci vůbec nic navíc.

-   Umět **načíst data z internetového bankovnictví**. Klidně si napíšu skript, který
    si to vezme z exportu nebo z [API](http://www.fio.cz/bank-services/internetbanking-api)
    (Fio, heč) a hodím ho do cronu, ale nehodlám řešit rozpoznávání položek
    (např. sMoneybox položky nepáruje, klidně je naimportuje duplicitně) a jiné
    záludnosti.
-   Musí to být **pružné**. Když jeden měsíc nezaplatím nájem a ten další zaplatím
    dva, musí být možnost nějak systému říct, aby jednu platbu započítal spíše
    k tomu prvnímu měsíci, aby měla výsledná čísla smysl. Stejně tak aby mi
    grafy nekazily průtokové platby, apod. Počítám s tím, že budou tyto úpravy
    ruční, ale musí být možné.
-   Zobrazit **koláč výdajů podle typu** - kolik utratím za jídlo, kolik za mobil,
    kolik prohýřím v hospodě a co jde státu. Představuju si to tak, že nastavím
    nějaké filtry na vstupní položky (jako v Gmailu), které mi je podle obsaženého textu
    (*Billa*) zařadí do kategorie (*jídlo*). Tyto filtry budu postupně ladit, aby
    odchytaly většinu věcí a ty 3 položky co propadnou si už nějak ručně zařadím.
    Mohlo by to nějak v grafu zvýraznit "mandatorní" výdaje, které musím platit
    každý měsíc, ale tohle beru jako úplný bonus. Kdyby to umělo podobně zobrazit i příjmy,
    bylo by to taky fajn. Jako volnonožník mohu mít pestrou příjmovou stránku a
    opět by se dalo i zvýrazňovat - tentokrát aby se odlišily pasivní a aktivní příjmy.
-   Čáru, která když půjde v čase dolů, tak je to špatný a prodělávám. Když půjde
    nahoru, je to dobrý a vydělávám. Zřejmě tedy nějaký **graf závislosti zisku na čase**.
    Mělo by to být opět nějak odolné k případům, které mohou v realitě nastat - např.
    když si odliju několik tisíc na spořící účet (a třeba nějak ručně takovou
    položku označím jako interní přesun), nemělo by mi to ty peníze zřejmě
    vůbec započítat jako výdaj a ukazovat v takovémto nějakém grafu.
-   Kdyby byl ten systém úplně boží, doplnil bych do něj pár konstant podle
    aktuálních zákonů a ukázal by mi k těm dvěma grafům ještě **pár orientačních
    čísel k příštímu daňovému přiznání**. Nemusí mi jej vypočítat na korunu přesně,
    spíš by mě jen tak orientačně zajímalo, zda mi v březnu vyjde na přehledu
    pro sociálku úplně jiná částka než jakou jsem jim zaplatil na zálohách a čeká
    mě třeba nějaké překvapní v podobě desetitisícového doplatku.

To je vše. Mám podezření, že by to ve své podstatě zvládl jakýkoliv tabulkový terminátor,
ale moc mě nenapadá, jak jednoduše implementovat import položek, filtry na jejich
utřízení, apod.

Co byste mi doporučili? Jak řešíte své finance vy? Programujete při tom v nějakých
obskurních frikulínských jazycích, jako třeba [zde](https://plus.google.com/u/0/111783114889748547827/posts/BZnsgkYdkA4)?
Myslíte, že existuje nějaký program, který mi ty tři věci dokáže zobrazit,
aniž bych si při tom udělal manuální epilaci těla? Mám napsat do [JIC](http://www.jic.cz/),
[Stártapjárdu](http://startupyard.cz/) nebo na [Tywoetrh](http://webtrh.cz/),
aby mi to natěšení klučíci za víkend zbouchali přesně podle mých představ?

Předem děkuji za všechna doporučení! (A dodávám:
Používám [Fio](http://www.fio.cz/), [Fakturoid](http://www.fakturoid.cz/),
[Linux](http://xubuntu.org/), programuju v [Pythonu](http://python.cz), neštítím
se nějak výrazně věcí jako Google Docs.)
