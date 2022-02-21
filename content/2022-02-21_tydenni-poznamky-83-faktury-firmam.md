Title: Týdenní poznámky #83: Faktury firmám
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (16.2. — 21.2.) a tak [stejně jako minule]({filename}/2022-02-15_tydenni-poznamky-82-skalovani.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tyto poznámky píšu brzo po těch posledních, zas tak moc se toho nestalo, tak to zkusím stihnout napsat do hodiny.


## Heroine

Ještě dlužím do Heroine jeden článek, ale nemám teď energii ho psát. Vzhledem k tomu, co všechno jsem pro projekt udělal a taky kvůli různým změnám v tématech, rozhodla se mi šéfredaktorka dát volnou ruku a prostor i pro čistě PR článek upoutávající JG. Já PR článek napsat neumím a asi bych chtěl, aby to bylo nějak užitečné, takže zatím i vymýšlím, jakou formu by to mělo mít.

Se šéfredaktorkou a ještě jednou autorkou jsme se sešli v kavárně v Praze, dávali si nějakou zpětnou vazbu a domlouvali jsme se co bude. Souhlasil jsem, že mi dává smysl pokračovat, ale že teď potřebuji pauzu a i potom bude ode mě třeba jen jeden článek měsíčně. Jednak jsem trochu vyčerpal témata, jednak potřebuji vlastně už řešit zase jiné věci.

## Marketing

Rozhodl jsem se, že kromě Heroine už nebudu dělat žádný další marketing nad rámec sociálních sítí, nebo aspoň ne v dohledné době. Heroine chci podpořit jakožto feministický časopis a taky už je to prostě nějak rozjeté, ale další věci bych teď už měl odmítat, protože aktuálně potřebuji škálovat klub a ne do něj přivádět další a další lidi :)

A to jsem si vlastně pořád nevytvořil ani ten marketingový plán, jak jsem o tom psal napodzim :D Změnil jsem od té doby pouze svou strategii ohledně sociálních sítí, které jsem začal dělat víc ručně a víc osobně. A psal jsem články do Heroine.

A začal vycházet podcast, díky kterému JG objevilo hodně lidí. Ale to není jen moje zásluha, to je zásluha především Pavlíny.

## Sekání Discordu

Zabýval jsem se tím, proč se mi Discord seká na mobilu. Mám iPhone X a mám ho celkem krátce na to, aby se mi na něm jen tak sekaly aplikace. Discord se ale zdá být dost náročná appka. Škoda, že je to teď můj hlavní pracovní nástroj.

Našel jsem nějaké tipy, co mám povypínat. Objevení Ameriky pro mě bylo nastavení _background refresh_, tedy jestli aplikace mohou na internet i když je zrovna nepoužívám. Zjistil jsem, že to mám skoro u všeho povoleno. Tak jsem to skoro u všeho zakázal.

Trochu to pomohlo. Občas se to pořád sekne, ale není to už tak strašné.

## Podcast na YouTube

Z podpory [Headlineru](http://headliner.app/) mi odepsali do druhého dne a můj problém vyřešili, takže jsem nemusel nic měnit, na YouTube se mi publikovala všechna podcastová videa. Velké a příjemné překvapení. Poučením budiž, že i příšerný a polofunkční produkt může vytvořit příjemně překvapeného uživatele, když máte kvalitní a rychlý support.

Prozřetelně jsem předtím nastavil, aby se to publikovalo vždy _unlisted_ a že teprve já to dám vždy ručně jako veřejné. Díky tomu jsem mohl přeházet pořadí videí, i když se na YouTube nahrál nejdřív druhý díl s yablkem a až potom první díl s Jirkou Psotkou. Jirku jsem publikoval hned a yablka jsem nastavil ať se publikuje až druhý den. Zafungovalo to a pořadí je pro veřejnost správně.

## Firmy a kupóny

Když firma zaplatí za členství v klubu, dostane kupóny, přes které na Discord posílají lidi. Kupóny mi řeší Memberful, stejně jako vše ostatní okolo členství. Není to standardní použití kupónů, je to vlastně spíš zneužití kupónů.

A s tím souvisí zádrhel, na který jsem přišel. Když firma prodlouží po roce členství, začne v tom být trochu nepořádek. Nejlepší, co jsem zatím vymyslel, jsou různé prefixy a doplňky ke kupónům, např. s IDčkem faktury. Udělal jsem podle toho už nové kupóny.

Jenže na kupóny mám navázány i další věci, např. role na Discordu atd., takže bylo potřeba upravit všude kód tak, aby se vypořádal s faktem, že jedna firma může mít kupónů víc. Udělal jsem si parsovací funkci, která vezme řetězec s kupónem a dokáže z jeho formátu vyzobat podstatné informace, kterými se pak může kód dál řídit.

## Robot na stahování nabídek práce

S robotem na nabídky práce jsem se bohužel moc neposunul. Vyřešil jsem akorát jak se budou řešit nabídky přímo z JG. Dostanou svou vlastní, úplně oddělenou tabulku v databázi. Pak udělám nějakou další, třetí tabulku, kde bude samotný výběr inzerátů, které se mají zobrazit na JG a ten pak bude 1:1 odkazovat na řádky z tabulek pro inzeráty z JG a pro inzeráty stažené odjinud. Nebo se informace při výběru položek překopírují, jako se to dělá v eshopech, když se vytváří objednávka, to už je asi jedno.

Překopal jsem opět skripty na synchronizaci a napsal nový, který se stará o nabídky z JG. Ty tedy vůbec nepůjdou přes scrapery a nebudou se tvářit, že jsou totéž, jako inzerát stažený např. ze StartupJobs.

Nabídky jsou uložené v Google Spreadsheets a občas se mi stalo, že špatně zadané URL probublalo až na web. Např. začínalo www a ne https. Tak jsem na to rovnou udělal kontrolu a když tam taková blbost bude, mělo by to spadnout.

Taky jsem vrátil hromadu testů zpátky do _codebase_. Ještě jsem nevrátil všechny, ale aspoň ty, které pokrývají samotné scrapery, už jsou zpět.

Teď potřebuji vyřešit, jak stahovat loga firem. Původně se to dělo v rámci Scrapy pipeline, ale tam to už nechci. Z uložených stovek nabídek totiž budu potřebovat stáhnout loga jen pro pár firem, navíc i pro firmy z inzerátů na JG, no prostě je to proces, který by měl být trochu nezávislý na zbytku a souvisí spíše s výběrem vhodných nabídek na web a jejich zobrazením, než s čímkoliv jiným.

Scrapy využiju, protože je tam pěkná [media pipeline](https://docs.scrapy.org/en/latest/topics/media-pipeline.html), ale navržené to ještě nemám. Popravdě mě to trochu zaskočilo, když jsem si uvědomil, že musím rozbombardovat i tohle. Pro většinu věcí jsem měl v hlavě nějaký plán, ale tady si to vezme ještě pár procházek s kočárkem a sprch, než přijdu na dobré řešení.

## Peníze!

- [Fakturoid](https://www.fakturoid.cz/) prodloužil svou nehynoucí podporu JG, včetně loga na příručce. Láska!
- Zahájili jsme spolupráci s [Jetveo](https://jetveo.io/), low-code platformou se C#. Poslal jsem fakturu (hned proplacená), na úterý chystáme demo platformy v klubu, logo [už je na webu](https://junior.guru/club/), brzo o tom napíšu i na sociální sítě. Na web jsem dal související [success story juniora Jakuba](https://jetveo.io/blog/articles/jakub-interview).
- Volali jsme si s [Pure Storage](https://www.welcometothejungle.com/en/companies/pure-storage) a brzo taky zahájíme spolupráci. Domluvili jsme se, že přijdou do klubu mentorovat, tak se těším!
- Juicymo prodloužilo své nabídky práce na JG: [Učenlivý junior Ruby on Rails vývojář](https://junior.guru/jobs/4187002b6a511f690f8827c3d6811f362fc73c0fa31682f38c67d5ae/), [Učenlivý junior analytik/architekt](https://junior.guru/jobs/a48eb9ba324ddbbb1c7fc291128d7727246aef32b13e8808cf0c9f0a/), [Učenlivý Android vývojář](https://junior.guru/jobs/5d41b691a09b074c0324a3fb86031903c2756ca668725ea3e3162187/)
- V neposlední řadě bych chtěl na tomto místě poděkovat svému nejvěrnějšímu podporovateli, který mi na účet s železnou pravidelností posílá 6 Kč se zprávou „ať se daří“. Miluju tě!

Díky tomuto všemu se únorový sloupeček v [grafu](https://junior.guru/open/) hezky zvedl a já poprvé přesáhl magickou hranici 30.000 Kč čistého měsíčně!

## Organizace práce a života

Rozhodl jsem se, že je aktuálně moje práce příliš chaotická a zkusím tomu dát nějaké mantinely. Prozatím chci využít _timeboxingu_ různých činností na určité dny. Ten daný den prostě stihnu z určitého balíku věcí jen to, co stihnu, a hotovo. Nebudu se tím pak dál trápit. Pokud nepůjde o něco urgentního, nebudu si rozbíjet další dny.

V pondělí chci řešit různou administrativní a komunikační agendu, psaní poznámek, apod. Na středu bych si rád dával cally a pokud by to nešlo, tak aspoň na pondělí. V úterý, čtvrtky a pátky chci mít soustředěnou práci. V pondělky a čtvrtky mám hodinu na sociální sítě, ale to možná rozhodím jinak. A když je večer akce v klubu, nebudu ten den dopoledne pracovat, abych vynahradil večerní ztrátu rodině.

Uvidím, jak se mi to povede dodržovat. Taky stále hledám nějaký nový životní režim s dítětem, takže plánuji i nějaké změny do budoucna a taky se musím naučit nějak aktivně relaxovat. Možná budu zase běhat, možná budu dělat jiné věci, ale tak jak jsem to dělal doteď, to dělat dál prostě nejde.

## Opravování buildu

Moje CircleCI buildy ne a ne procházet. Vždy se najde něco, kvůli čemu to spadne a musím to řešit. Ach jo.

- Z nějakého důvodu občas failuje skript, který stahuje avatary členů, abych z nich mohl generovat pár náhodných do [vrchní části stránky o klubu](https://junior.guru/club/). Že prý _unknown member_. Zvýšil jsem logování skriptu, abych tušil, co se tam děje, až se to zase stane.
- Skript, kterým generuji XML pro podcast, analyzuje i zvukové stopy a protože to trvá déle, stáhnout velké soubory, dělá to paralelně v procesech. Teď, když už jsou venku 3 díly, začaly GitHub Pages, kde podcast hostuju, timeoutovat :D Tak nevím, jestli je to nejlepší hosting na podcast, možná to budu měnit dřív, než jsem myslel. Počet stahovačů jsem snížil na nanejvýš dva a zatím to funguje.
- Ještě mám v kódu stále skript, který z Google Analytics stahuje nějaké metriky o inzerátech na JG, aby je mohl posílat firmám mailem. Už dávno jsem ho chtěl zmigrovat na [Simple Analytics](simpleanalytics.com/junior.guru), žel, nebyl čas a síla. Teď to začalo failovat, GA vrátily pro něco nula dat a moje funkce s tím nepočítala. Zatím jsem to jen narychlo opravil. Přidal jsem test s daty, které vracelo API, a funkci pak upravil tak, aby test prošel.

I když jsem všechno tohle vyřešil, spadlo mi to zase třikrát po sobě na nějaké chybě v _asyncio_, že prý task nemá tu správnou _loop_ nebo co. Já mám totiž hromadu skriptů, které něco dělají. Spustí se, něco dělají a pak skončí. Ty pak mám naházené do jednoho velkého, všechno běží v jednom procesu (pokud se to přes [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) nějak nerozdělí) a všechno shora dolů sekvenčně, jedno po druhém. A tohle se vůbec nedá dělat, když máte něco asynchronní, protože to spustí nějakou tu svou slavnou smyčku a neskončí to, dokud smyčku nezabijete. Ale ta potom už nejde restartovat, prostě šmitec. Takže když máte 10 skriptů imperativního synchronního kódu a pak 5 skriptů, které každý izolovaně něco řeší, ale jsou asynchronní (protože knihovna na práci s Discordem je asynchronní), nemůžete to prostě nasázet za sebe a spustit.

A před časem jsem vymyslel, jak to u té knihovny na Discord udělat a jak si spustit vždy novou smyčku. Pak jsem tam měl scrapery a ty jedou na Scrapy, které jede na Twisted a tam je zase nějaký Twisted reaktor, zase smyčka, ale ta teda spustit ani znova vytvořit nejde, ani za nic. Takže už tam jsem narazil a musel to vytáhnout do procesu vedle přes [multiprocessing](https://docs.python.org/3/library/multiprocessing.html). Tenhle vedlejší proces si jede se smyčkou asynchronně a hotovo, pak to skončí, původní proces neposkvrněn žádným asynchronním bincem:

```python
process = Process(target=_task, args=[...])
process.start()
process.join()
if process.exitcode != 0:
    raise RuntimeError(f'Process for running async code finished with non-zero exit code: {process.exitcode}')

def _task(...):
    pass  # tady jsou asynchronní věci
```

No a delší dobu jsem pozoroval, jak mi asi zlobí i to řešení pro Discord. Že prý task nemá tu správnou _loop_, i když mít měl. A teď se to nasbíralo a popadalo. Tak jsem to vzdal. Ta _loop_ prostě asi není na tohle dělaná. Tak jsem si řekl ok, vytáhnu to zase do procesu vedle, na hodinu práce.

Houby! Celý den jsem to dělal. Zjistil jsem, že [do procesu nejde poslat nic, co má dekorátor](https://stackoverflow.com/questions/9336646/python-decorator-with-multiprocessing-fails). Jenže já přes dekorátory řeším připojení k databázi a vůbec, chtěl jsem se od té blbosti abstrahovat a ne řešit, jestli někde můžu dát dekorátor nebo nemůžu.

Stále jsem ladil, jak se to bude používat. Nakonec jsem skončil u něčeho jako:

```python
def main():
    run_discord_task('juniorguru.sync.script.do_something')

@db.connection_context()
async def do_something(discord_client):
    pass
```

Funkce `run_discord_task()` si bere importovací cestu k funkci jako řetězec a ta se vyřeší až v samotném spuštěném vedlejším procesu. Takže `do_something()` se ani nemusí picklovat a někam posílat, prostě se naimportuje až potom, v procesu, přes `importlib`.

Když potřebuju databázi, můžu použít dekorátor. Jupí. Až na to, že Peewee nezvládne dekorovat asynchronní funkci, jak jsem zjistil :D A ani se to neplánuje, autor Peewee nemá rád asyncio. Takže jsem si musel přečíst kód Peewee a doprogramovat si to:

```python
import asyncio
from peewee import Model, SqliteDatabase as BaseSqliteDatabase, ConnectionContext as BaseConnectionContext

class ConnectionContext(BaseConnectionContext):
    """Supports async functions when used as decorator"""
    def __call__(self, fn):
        if asyncio.iscoroutinefunction(fn):
            async def wrapper(*args, **kwargs):
                with self:
                    return (await fn(*args, **kwargs))
            return wrapper
        return super().__call__(fn)


class SqliteDatabase(BaseSqliteDatabase):
    def connection_context(self):
        return ConnectionContext(self)


db = SqliteDatabase(DB_FILE, pragmas={'journal_mode': 'wal'})
```

Pak jsem musel upravit všechny skripty, které něco dělají s Discordem, aby fungovaly novým způsobem. No jako hrdý na to nejsem, ale funguje to, třeba to někdy udělám hezčí, ale už tak jsem se s tím patlal moc. Možná existuje nějaké skvělé, elegantní řešení, jak spustit asynchronní kód opakovaně za sebou v rámci synchronního, ale já ho neznám.

Možná existuje nějaký task runner, který by to za mě všechno vyřešil a byl schopen pustit jak synchronní, tak asynchronní kód v pořadí, jaké si určím (a na sobě nezávislé skripty pusit klidně paralelně, to by bylo hezké). Třeba by mi to usnadnilo práci a mohl bych hodně kódu smazat. Já ale nic takového neznám. Možná bych si to měl celé napsat v asyncio.

Nevím, dál. Buildy přestaly failovat, to je teď hlavní :)

## Další poznámky

- Promoval jsem [nový díl podcastu s yablkem](https://junior.guru/podcast/). I yablko [promoval](https://twitter.com/yablko/status/1494389432249688067)!
- Nakonec jsme se domluvili se Seznamem a jeho podcasty.cz. Vyplnil jsem .docx smlouvy a poslal jim je. Provozuji a svým podnikáním zaštiťuji JG, ale podcast je autorsky v režii Pavlíny, tak jsem se pro tento účel do smluv zapsal jako „sekretář podcastu“. Snad to bude znít lépe než kulisák.
- Odpovídal jsem na různé věci v klubu a vítal občánky, kteří přišli. Rozjela se zajímavá diskuze o zakládání startupů nebo o tom, jestli pracovat na IČO nebo ne. Taky bokem trochu řešíme cyklistiku.
- Pustil jsem cvičně `poetry update` a zjistil, že to updatuje víc věcí, než které mi pohlídal dependabot na GitHubu. Tak jsem to commitnul a začalo mi všechno fungovat nějak napůl a padat. Tak jsem to revertnul a udělám to později, jednu knihovnu po druhé :D
- Kontaktoval jsem dalšího speakera, který by si měl připravit přednášku do klubu.
- Odeslal jsem po poslíčkovi samolepky pro pražské PyLadies.
- Zkusil jsem zábavu z klubu [přenést na Twitter](https://twitter.com/honzajavorek/status/1493599032635281410), ale nemělo to žádné reakce ani pokračovatele :D Teda brácha myslím pokračoval, tak pokračovatele to teda jednoho mělo.
- Během 6 dní od 16.2. do 21.2. jsem naběhal 9 km, při procházkách nachodil 19 km. Celkem jsem se hýbal 9 hodin a zdolal při tom 28 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Pracovat dál na botovi, který stahuje a třídí pracovní nabídky.
2. Neflákat sociální sítě a propagovat nová partnerství s firmami.
3. Vyúčtovat studenty jedné vzdělávací agentuře, která mi je posílá do klubu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Google Search Is Dying](https://getpocket.com/redirect?&url=https%3A%2F%2Fdkb.io%2Fpost%2Fgoogle-search-is-dying&h=c4a5144c491457555df711bf042bb9c747619fe08e0ad1d5c967b1a2eea585d7)<br>Dává vám Google vlastně ještě nějaké užitečné výsledky, nebo na vás už sype jen reklamy a přeoptimalizované stránky?
- [Pokud Biden neříká o Rusku pravdu, dozvíme se to. Putinovy lži ale nikdo nehlídá](https://getpocket.com/redirect?&url=https%3A%2F%2Fnazory.aktualne.cz%2Fkomentare%2Fnew-york-times%2Fr%7E30d496ea8fe211eca9b1ac1f6b220ee8%2F&h=9232d7ddf48bf63ae9e5635ad5b678c8564aeabf8e3325e1728f95847b593aaf)<br>Komentář o tom, jak i Bílý dům může vypouštět účelové informace, ale na rozdíl od Putina pak dostane přes prsty od svobodných médií.
- [Ukrajina mezi „šílenstvím“ Ruska a „hysterií“ Západu. Pohled zpravodaje listu Guardian z Kyjeva](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BRZMi-r8VU&h=553008e007f96f1abdab9722d58733c17f9b36743dd3a646fc876b37319c96b0)<br>Pěkný komentář k aktuálnímu dění na Ukrajině.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
