Title: Týdenní poznámky: Čísla
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False
Twitter-Comments: https://twitter.com/honzajavorek/status/1271510681947443211
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158199180067707


Utekl další týden (8.6. — 12.6.) a tak [stejně jako minule]({filename}/2020-06-05_tydenni-poznamky-dohaneni-css-a-korporatni-balicky.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Sběr čísel

V tomto týdnu jsem se soustředil především na to, aby JG splnilo představy velkých firem o spolupráci. Řekl jsem si, že než toto vyřeším, nemá ani moc smysl oslovovat další firmy.

Zpětnou vazbu mám sice z jedné konkrétní velké firmy, ale jednak o ni dost stojím, jednak si neřekli o nic, co bych stejně nemusel řešit i pro jakoukoliv jinou větší firmu (viz [předešlé poznámky]({filename}/2020-06-05_tydenni-poznamky-dohaneni-css-a-korporatni-balicky.md)). Ze tří bodů jsem dva vyřešil už minule, takže jsem se soustředil na třetí problém, a to měření úspěšnosti inzerátů.


### Měření skrze korporátní software

Napsal jsem tvůrcům produktu pro HR velkých firem a ptal jsem se jich, jak s nimi jako malá ryba mohu integrovat svoji analytiku tak, aby klient, který jejich software používá, v něm mohl vidět, že konkrétní kandidát přišel zrovna z JG. Po pár e-mailech jsem se dostal přes vrátného až na relevantní osobu a s tou jsem nakonec našel jednoduché řešení. Kdo se bojí, nesmí do lesa. Velká firma, se kterou jednám, byla potěšena, že to půjde, a hned je o překážku méně.


### Jak dostat statistiky k inzerentům

Rozhodl jsem se ale, že by i JG samotné mělo mít nějak dostupná čísla, a to pro všechny svoje inzeráty. Nějaká čísla měřím pomocí Google Analytics a prokliky z newsletterů jsou v MailChimpu, takže šlo jen o to, jak to dostat ke klientům. JG jsou statické stránky, takže nějaká administrace nepřichází v úvahu.

Napadlo mě ale, že bych mohl recruiterům statistiky posílat e-mailem. Stejně bych jim chtěl něco posílat v případě, že se blíží vypršení nabídky, takže jsem to spojil dohromady a budu všem inzerentům posílat každé pondělí e-mail s detaily o tom, jak se jejich inzerátu daří. Pak už jen doprogramuju, aby byl text tím naléhavější, čím se bude blížit datum vypršení inzerátu, a aby obsahoval informace o tom, jak lze inzerát prodloužit. Zatím jsem se rozhodl posílat tato čísla:

- Počet dní od uveřejnění inzerátu (a datum)
- Počet dní do vypršení inzerátu (a datum)
- Jestli už byl inzerát v newsletteru nebo ještě ne (případně datum)
- Celkový počet návštěvníků stránky s inzerátem
- Celkový počet zobrazení stránky s inzerátem
- Celkový počet uchazečů (měřím kliknutí na tlačítko)

Protože mě vždycky štvou _noreply_ e-maily, dávám do každé zprávy ještě větu, že pokud příjemce cokoliv potřebuje, ať jednoduše odepíše, normálně mi to přijde. Taky pro jistotu přidávám varování, že čísla jsou podhodnocená, protože Google Analytics dnes kde kdo blokuje, a taky protože některé statistiky zatím měřím jen velice krátce.


### API, databáze a izolepa

Implementace začala hraním si s Google Analytics API a MailChimp API. Moc se mi do toho nechtělo, k mému překvapení jsem měl ale první prototyp celkem rychle. Na první API existuje PyPI balíček `google-api-python-client`, na druhé stačily `requests`. Auth do Google API je sice složité, ale zrovna to jsem měl už dávno vyřešené díky stahování dat z Google Spreadsheets přes `gspread` (ano, data o nabídkách práce jsou v Google Spreadsheets). V případě MailChimpu zase stačilo jen vytvořit nějaký API key a poslat jej v Basic auth. No a jak ví každý, kdo si chvíli hraje s API, jakmile se člověk dostane za auth, už to jde většinou celkem samo.

Jako první malý cíl jsem si vytyčil, aby čísla nahoře na [stránce pro firmy](https://junior.guru/hire-juniors/) byla dynamická, tzn. aby se počítala z reálných dat. Už jen číslo pro počet lidí v newsletteru jsem totiž musel měnit hned několikrát, jak to teď roste každým dnem. Šlo to celkem pěkně. Počty návštěvníků a zobrazení jsou průměrné počty za poslední 4 měsíce a pro zobrazení se zaokrouhlují.

Další krok byl získat čísla pro jednotlivé nabídky práce. To už byl větší oříšek, ale nakonec jsem vše nějak vyřešil (viz odstavec "Trik s generátory" níže) a pěkně otestoval. Metriky v SQLite ukládám do jiné tabulky než nabídky práce, takže mě čekal první `JOIN` v historii JG. Bohužel mě stál dost energie, nějak jsem [nepochopil jak mám modely strukturovat tak, abych se nedostával do konfliktu importů](https://stackoverflow.com/questions/62327182/) a s řešením této věci jsem bohužel zabil polovinu čtvrtka. Zatím jsem to nějak ošklivě obešel a uvidím, co do budoucna.


### Posílání e-mailů

Ke konci týdne jsem se dostal k samotnému posílání. Zapřáhl jsem freemium na [SendGridu](https://sendgrid.com/) a jejich `sendgrid` PyPI balíček, se kterým jsem měl první odeslaný e-mail prakticky hned. Pak jsem vymyslel robustní architekturu, která mi umožňuje ukládat e-maily do fronty (postavené nad Google Spreadsheets, hehe), ukládat chyby, pokud se neodešlou, posílat je znova, řešit freemium limit 100 e-mailů denně, apod.

Naštěstí jsem pak šel na oběd a tam jsem vystřízlivěl. Uvědomil jsem si, že vymýšlím hovadiny, a že nic z toho zatím nepotřebuji. Udělám co nejrychleji jednoduchý skript, který bude prostě v cyklu posílat e-maily, ten dám do produkce, a až zaznamenám problémy, tak budu teprve vymýšlet, jak je řešit. A tak se i stalo. Uf! Robustní řešení nakreslené na papíru jsem si vyfotil, archivoval do Trella a vyhodil do koše.

Do pátečního večera jsem skript vyrobil, odladil HTML podobu e-mailu, a zapojil to celé do nightly buildu na CircleCI. Zatím tam jsem jako příjemce všude já, abych to otestoval, a není to omezeno na pondělky, takže mi teď o víkendu asi přijde hodně e-mailů :D No ale co je na konci dne na produkci, to se počítá! Mám radost.

## Trik s generátory

Během programování stahování metrik z Google Analytics jsem narazil na to, že dotaz do API byl seznam "report requests", kde každý "report request" byl dotaz na data k jedné metrice, kterou chci sledovat. Pak mi přišel zpět seznam dat, které jsem zase musel nějak mapovat zpět a zpracovávat podle té které metriky. Pseudokód:

```python
data = request({'report_requests': [
    {...},  # složitý objekt, dotaz pro data ze kterých vypočítám metriku A
    {...},  # složitý objekt pro metriku B
    {...},  # složitý objekt pro metriku C
])

metric_A = sum_everything(data[0])
metric_B = calculate_something(data[1])
metric_C = aggregate(data[2])
```

Moc se mi to nelíbilo a s více metrikami už to bylo i hodně nepřehledné. Navíc byl kód pro jednotlivé metriky na různých místech a uprostřed všeho byl nějaký dotaz na API, který jakožto side-effect velmi znepříjemňuje testování.

Použil jsem tedy trik s generátory, který mi umožnil dát kód pro každou metriku na jedno místo:

```python
def metric_A(args):
    report = yield {...}  # složitý objekt pro metriku A
    yield sum_everything(report)

def metric_B(args):
    report = yield {...}  # složitý objekt pro metriku B
    yield calculate_something(report)

def metric_C(args):
    report = yield {...}  # složitý objekt pro metriku C
    yield aggregate(report)
```

Každá metrika je teď jednoduchá funkce, kde je vše hezky na jednom místě pro každou metriku a která nemá žádný side-effect, takže ji mohu i krásně testovat. Použije se takto:

```python
args = ...  # argumenty pro každou z funkcí, jen příklad
metric_fns = [fn(args) for fn in [metric_A, metric_B, metric_C]]

data = request({'report_requests': [next(fn) for fn in metric_fns])

metrics = {}
for i, fn in enumerate(metric_fns):
    name = fn.__name__.replace('metric_', '')
    value = fn.send(data[i])
    metrics[name] = value
print(metrics)  # {'A': 123, 'B': 345, 'C': 678}
```

Je to méně explicitní a pro méně zkušeného programátora zřejmě dost kryptické, ale zbytek kódu se zase se dost zjednodušil, hlavně psaní samotných funkcí pro metriky.


## Další poznámky

- Přidal jsem dalšího Tomáše [do seznamu podporovatelů](https://junior.guru/donate/#sponsors). Juchů!
- Četl jsem si [Marketing for Engineers](https://github.com/LisaDziuba/Marketing-for-Engineers/blob/master/README.md)
- V reakci na předchozí poznámky mi byl místo [IFTTT](https://ifttt.com/) doporučen [Integromat](https://www.integromat.com/). Hned jsem si tam zkusil něco naklikat a je to hodně dobrý! Vytvořil jsem si přes to zatím [tohle API](https://hook.integromat.com/z9sxy3t8k6hxp2bxs3b237a5rw1n7yt7), ve kterém se pokouším vypsat odkazy na své příspěvky na Facebooku a Twitteru, ve kterých jsem sdílel týdenní poznámky. Až se budu nudit, vyrobím druhou část, která tyto odkazy bude automaticky přidávat do článků jako odkazy na komentáře, ať to nemusím pokaždé dělat ručně. (Pokud teda ty odkazy na komentáře vůbec někdo používá… ale i tak je to dobré na to, abych viděl, co vše se dá s Integromatem udělat.)
- Vedl jsem na sociálních sítích diskuse pod statusy, které propagují připravovanou příručku. Zajímavé diskuse, některé určitě povedou i k úpravám v textu.
- Začal jsem zase chodit pravidelně cvičit do [KB5](https://www.kb5.cz/), takže mám dvakrát týdně tak o dvě až tři hodiny méně času na JG. Celkově jsem začal obnovovat vztahy s lidmi, takže jsem tu zašel s přáteli na pivo, tu s ~~manželkou~~ investorkou na večeři, stavil jsem se k holičce a jel se na půl dne projet na kole do Černošic, abych navštívil přátele. Možná začnou být teď po odeznění covidu-19 týdenní poznámky kratší?
- Měl jsem perfektní call s koordinátorem vzdělávacího programu v jedné velké firmě.
- Odepsal jsem na e-mail člověku, který chce jeden vzdělávací program ve velké firmě spustit. Je to fakt velká firma a ten člověk je _director of engineering_ takže jsem volil správná slova jedno celé ráno :D
- Měl jsem call s člověkem, který stojí za jedním bootcampem v Česku.
- Opravil jsem na JG nějaké rozbité externí odkazy.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [There Are No Bugs, Just TODOs](https://getpocket.com/redirect?&url=https%3A%2F%2Falmad.blog%2Fessays%2Fno-bugs-just-todos%2F&h=2f994af5d6fb1f55d3b38d1d91f307755a06bfad5efa43961b51eb67daee71ab)<br>Souhlas, že dělit úkoly na bugy a fičury by mělo být správně zbytečné, a že vývoj by měl být jeden ToDo seznam
- [7 Ways to Retain More of Every Book You Read](https://getpocket.com/redirect?&url=http%3A%2F%2Fjamesclear.com%2Freading-comprehension-strategies&h=cd4d804a2c96d3926b86884f70dd759faa6ebbd4c8fc2eb0d8a9908b70740ae7)<br>Fajn tipy, tak snad bych zase mohl něco konečně přečíst
- [Be a good mentor, not a dickhead](https://getpocket.com/redirect?&url=https%3A%2F%2Fdev.to%2Fmortoray%2Fbe-a-good-mentor-not-a-dickhead&h=1e969067c6a99b0cbbc67925ec8fe6793c488f80e981a766c3258ff0e9dd9d52)<br>Souhlas
- [A Five-Minute Guide to Better Typography](https://getpocket.com/redirect?&url=http%3A%2F%2Fpierrickcalvez.com%2Fjournal%2Fa-five-minutes-guide-to-better-typography&h=809370b78b93e6911db75dc68f4dcdf58836a0d61da0461bab0e04d6f4b68912)<br>Pár praktických rad — a je to
- [1:1, nejdůležitější nástroj team leadera](https://getpocket.com/redirect?&url=http%3A%2F%2Fwww.sw-samuraj.cz%2F2017%2F10%2F11-nejdulezitejsi-nastroj-team-leadera.html%3Fspref%3Dtw%26m%3D1&h=f8885a103e22da62316e497d087faab883989356762e07a7227cb3b6f1508688)<br>V Apiary jsme 1:1 poctivě dělali a už bych nikdy nechtěl jinak
- [Questions for our first 1:1](https://getpocket.com/redirect?&url=http%3A%2F%2Flarahogan.me%2Fblog%2Ffirst-one-on-one-questions%2F&h=0fc76d4db1ea50dbbc0585323cb6742cd725779583943a02a4be45f5aa3c4ee2)<br>Skvělé otázky na 1:1
- [Klid a mír na konci světa](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.respekt.cz%2Ftydenik%2F2017%2F17%2Fklid-a-mir-na-konci-sveta&h=e376b5791579cd9568049ed5cfb92ece1b8f62cee477609257934291cbbb50df)<br>Pokračování příběhu pro ty, kdo viděli seriál Narcos

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
