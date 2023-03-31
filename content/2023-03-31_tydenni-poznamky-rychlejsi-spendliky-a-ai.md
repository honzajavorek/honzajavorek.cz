Title: Týdenní poznámky: Rychlejší špendlíky a AI
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/169

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-03-24_tydenni-poznamky-zamotany-v-kodu.md) už utekl nějaký ten týden (24. 3. až 31. 3.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Rychlejší špendlíky

Většinu týdne jsem se hrabal v kódu, ale na rozdíl od minula z toho mám při pátku dobrý pocit.
Když někdo v klubu přidá reakci špendlíku 📌 k nějaké zprávě, můj bot mu ji uloží do soukromých zpráv.
Je to užitečné, ale jak jsem psal minule, toto ukládání nebylo naprogramované dobře a trvalo už skoro 10 minut.
Během týdne se mi to povedlo zrychlit na 0.3 minut.

-   Z minulého týdne jsem měl hotové šifrování databáze, takže jsem do ní mohl začít ukládat i neveřejné věci.
-   Přebudoval jsem bota, aby stahoval do databáze i obsah soukromých zpráv.
    Díky tomu se nemusí špendlíky ověřovat přes API.
    Zprávy už jsou v databázi a lze v tom pohodlně lokálně hledat přes SQL.
-   Uložil jsem si ke každé zprávě, zda je veřejná nebo soukromá a upravil všechny dotazy a operace tak, aby to respektovaly.
    Jako soukromé jsem označil i zprávy, které jsou v kanálech, kam nemají přístup všichni z klubu.
    Všechen ostatní kód jsem upravil tak, aby počítal s tím, že kanály mohou být jak veřejné, tak i soukromé.
-   Kód celého „stahovače“ zpráv z Discordu do databáze jsem přebudoval od základů a nejspíš i zefektivnil.
-   Mnoho věcí jsem předělal tak, aby se děly už při ukládání do databáze a pak se mohly jen číst a prohledávat, ne aby se to řešilo za běhu.
-   Na ukládání globálního stavu, ať už jde o nastavení služeb, do kterých má program povolené zapisovat, nebo nastavení logování, jsem použil _environment variables_.
    Při použití [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) to bylo nejvíc [KISS](https://en.wikipedia.org/wiki/KISS_principle).
-   Moc jsem toho neotestoval, takže to bych měl v ideálním případě dodělat.

![Špendlík]({static}/images/screenshot-2023-03-31-at-17-04-29.png)

## Objevování asyncio

Když už mám ten Python 3.11, tak jsem chtěl použít místo `asyncio.gather()` novinku, _[task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)_.
Začal jsem se však dostávat do obskurních problémů, od _segmentation fault_ až po [visící program neschopný zpracovat výjimku](https://github.com/Pycord-Development/pycord/issues/1986) (pod _issue_ je komentář s vysvětlením, proč se to děje).
Zabil jsem s tím jedno dopoledne a pak jsem to z kódu raději vyházel.

Naučil jsem se však při tom, že nemusím na `asyncio` tasky čekat hned, že je mohu vytvářet a až postupně si sbírat jejich výsledky, klidně třeba zrovna přes `asyncio.gather()`.
Zní to triviálně, ale mě to původně fakt nedošlo.
Všechny příklady totiž vždy vypadají takto:

```python
import asyncio

await asyncio.gather(*[something(), something(), something()])
```

Takže až teď mi došlo, že můžu udělat tohle:

```python
import asyncio

tasks = []
tasks.append(asyncio.create_task(something()))
tasks.append(asyncio.create_task(something()))
tasks.append(asyncio.create_task(something()))

await asyncio.gather(*tasks)
```

A ty věci se začnou dělat už při volání `asyncio.create_task()`.
Aspoň teda myslím.

Taky jsem zjistil, že synchronní věci mohu velmi snadno volat pomocí [něčeho, co se jmenuje _executor_](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) a nebudou mi nic blokovat.
To je perfektní, protože tím můžu obalit volání do databáze, která mám synchronní.

Celé mě to přivedlo na myšlenku, že by možná měl být celý backend junior.guru asynchronní a do synchronních věcí by si to mělo jen odskakovat 🤯
Protože těch asynchronních věcí je tam čím dál víc a odskakuje se do nich dost složitě (v podstatě spouštím celý nový proces a v něm _loop_), zatímco z asynchronních do synchronních se odskakuje snadno.
Jenže to by znamenalo v podstatě všechno přepsat a to je samozřejmě blbost.
Uvidím, jestli mě napadne nějaké řešení, které by na to šlo postupně.

Každopádně se postupně víc a víc seznamuji s `asyncio`, které jsem ještě před nedávnem vůbec neuměl.
A vlastně se mi to celkem líbí.
Škoda, že zatím není víc high-level věcí jako např. `TaskGroup()`, které by obalily občas nevzhledné přehazování _tasků_ vidlema sem a tam.
A škoda, že když už něco jako `TaskGroup()` existuje, tak to dost zvláštně (ne)funguje.

Taky je škoda, že jsem se rozhodl použít [Peewee](http://docs.peewee-orm.com/), které sice má nějakou [asynchronní verzi](https://github.com/05bit/peewee-async), ale ta zase nepodporuje SQLite.
Věřím, že mainstreamovější SQLAlchemy by zvládla všechno.
Ani nevím, proč jsem kdysi vybral zrovna Peewee.
Možná jsem měl dojem, že na ty moje dvě tři tabulky bude stačit něco minimalistického.
Tak teď mám tabulek třicet nebo kolik, v nich desetitisíce záznamů…
Přejít z jednoho ORM na druhé by byla samozřejmě šílená práce.

## Objevování typů a Copilot

VS Code mi přestal z neznámého důvodu napovídat, tak jsem něco poklikal v nastavení a napovídat zase začal.
Ale zaškrtl jsem i něco, co se jmenuje _inlay hints_ a teď mi to ukazuje, co si VS Code myslí, že funkce vrací, nebo jaké mají parametry typy.
No a když už jsem to tam viděl, tak jsem tam ty typy začal dopisovat.
Poprvé v životě jsem sám od sebe v Pythonu použil typy.
A když jsem je tam už měl, tak, světe div se, začalo VS Code napovídat ještě o dost lépe!

![Inlay hint]({static}/images/screenshot-2023-03-31-at-17-06-02.png)

Je to návykové.
Zatím se to celé teprve učím, ale líbí se mi to.
Na malé programy nebo prototypy je to zbytečné, ale přesně na kód, který jsem teď psal, je to super.
Ukládání Discord `message` do databáze, vytahování `message` z databáze, proměnné se jmenují stejně, ale každá má jiný typ…
Zmatek.

No a když už jsem byl u toho, řekl jsem si, že zkusím i [GitHub Copilot](https://github.com/features/copilot).
Je to na 60 dní zdarma.
Když to bude dobré, budu za to klidně platit.
Kdo jiný než sólo programátor a podnikatel by měl víc benefitovat z toho, že mu bude AI napovídat?
V korporátech jim bude trvat roky, než vůbec svým lidem povolí takové věci používat.
Já to můžu používat hned a věřím, že vložené peníze se mi mnohonásobně vrátí.

První dojmy?
Nuže, napovídá to při psaní.
Bál jsem se, že mě to bude štvát, že mi bude každou chvíli napovídat nějakou blbost, ale vůbec.
A zatím většina věcí, co napoví, se mi celkem hodí.
Asi to vyladili tak, že napovídá jen když si fakt věří, že napovídá něco užitečného.

Akorát na to nejsem zvyklý, takže mě vždy strašně překvapí, když mi napoví celý kus kódu a já to odkliknu a je to napsané. Nejdřív na to čumím jako na zázrak, pak na to čumím, jestli je to fakt dobře.
Tím pádem se jakákoliv úspora zatím stírá 😀

![GitHub Copilot]({static}/images/screenshot-2023-03-31-at-17-08-00.png)
Tyto dvě funkce za mě napsal GitHub Copilot, stačilo začít názvem. A pak se podívat, zda nenapsal blbost.


## Objevování Notionu

O víkendu jsem se podíval na [Notion](https://www.notion.so/).
Vím o téhle věci už dlouho, ale vždy jsem to pouze viděl používat ostatní, nikdy jsem si s tím nezkoušel hrát sám.
Hned se mi to zalíbilo!

Přesunul jsem tam okamžitě svoje Tudů na běžné dny, udělal jsem si tam stránku s odkazy na dovolenou, zapsal jsem si tam nějaké úkoly související s úklidem v osobních a rodinných financích, apod.
Nejspíš to budu používat místo Apple Notes, které se mi nakonec nepoužívají moc dobře, a možná i místo Trella.

Také jsem si tam udělal seznam zajímavých odkazů k AI a seznam odkazů na články, které bych si mohl chtít přečíst.
Jak jsem psal minule, [Pocket](https://getpocket.com/) nemá z více důvodů použitelné RSS a má OAuth 2.0 API (tzn. API k ničemu), takže jsem to zkusil vytvořit s Notionem:

-   V Notion jsem si udělal databázi na odkazy.
-   Nainstaloval jsem si Notion na mobil a do prohlížeče jsem si dal jejich [Web Clipper](https://addons.mozilla.org/en-US/firefox/addon/notion-web-clipper/).
    Snadné přidávání vyřešeno.
-   Mrkl jsem na jejich API a byl jsem unešen z toho, jak jednoduše a prakticky je vyřešen přístup do něj.
    Jde to přehledně naklikat a vše je perfektně vysvětlené a zcela zřejmé.
    Pokud chcete přístup jen ke svým datům, tak nemusíte nic řešit a jedete přes token, žádné OAuth 2.0 s interakcí.
    A celá dokumentace k API je hodně promakaná.
-   Za chviličku jsem měl hotový [skript](https://github.com/honzajavorek/honzajavorek.cz/blob/main/blog/reading.py), který používá [notion-sdk-py](https://github.com/ramnes/notion-sdk-py) a [python-feedgen](https://github.com/lkiesow/python-feedgen).
    Přečte odkazy a vygeneruje RSS.
    Jádro programu má přesně 15 řádků.
-   Dal jsem si to na GitHub a jednou za čas se mi přes GitHub Actions vygeneruje RSS soubor.
    Ten jsem si přidal do [NetNewsWire](https://nnw.ranchero.com/) a hotovo!
    Teď mohu chodit po internetu a posílat si náhodné články do RSS čtečky a ještě mám jejich databázi v Notionu.

![Notion]({static}/images/screenshot-2023-03-26-at-16-14-39.png)
Databáze odkazů

![Screenshot nastavení přístupu do Notion API]({static}/images/screenshot-2023-03-31-at-16-07-01-notion-the-all-in-one-workspace-for-your-notes-tasks-wikis-and-databases.png){: .img-thumbnail }
Nastavení přístupu do Notion API

![Screnshot NetNewsWire]({static}/images/screenshot-2023-03-26-at-16-13-57.png)
Výsledek!

Když už jsem tyhle věci zkoumal, tak pokud by někdo chtěl vysypat věci z Notion nebo Apple Notes do SQLite, může se hodit [notion-into-sqlite](https://github.com/FujiHaruka/notion-into-sqlite) nebo [apple-notes-to-sqlite](https://datasette.io/tools/apple-notes-to-sqlite).


## MVP katalogu kurzů

Vymyslel jsem si MVP katalogu, na kterém bych chtěl začít co nejdříve pracovat.
Každý krok by mělo být něco, co mohu v rámci _continuous deployment_ hodit hned na produkci.

1.  Udělám stránku s kurzy, kam se přesune [současný seznam](https://junior.guru/handbook/practice/#kde-hledat-kurzy-a-workshopy), a která má svoje tlačítko v menu.
2.  Seznam bude abecedně.
3.  Menu přeteče, takže ho vyladím pro každé rozlišení.
    Možná ho budu muset celé předělat.
4.  Informace o kurzech přesunu na samostatné stránky, kde budu mít název, JEDNU VĚTU a upoutávku na klub.
5.  Stránky z `/topics/` ([příklad](https://junior.guru/topics/engeto/)) přesměruju na tyto nové stránky.
6.  Zvýrazním stránky, které jsou o partnerských firmách.
    Propojím je s [přehledem firemních partnerství](https://junior.guru/open/#firemni-partnerstvi).
7.  Seznam bude řazen tak, že první budou partneři a potom bude abecedně.
8.  Firmy začnu štítkovat a budu generovat stránky pro jednotlivé štítky.
    Díky tomu půjde mezi kurzy nějak filtrovat.
9.  Doplním postupně další a další data (odkaz, založení firmy, logo…).
10. Vymyslím ceník pro tyto firmy, skoro nic nedám zadarmo.
11. Ozvu se hned několika firmám, které mám rozjednané a de facto už jen čekají na to, až bude katalog existovat.
12. Vytvořím „návod“ na kurzy do příručky a propojím ho s katalogem.
    Popíšu obecně jejich výhody i úskalí.

**Bonus:** Převedu zbytek `/topics/` ([příklad](https://junior.guru/topics/python/)) někam do příručky a zabiju starou infrastrukturu, na které tyto stránky běží.


## Další

-   Propagoval jsem slevu na WebExpo a [svou Q&A, která bude po Velikonocích](https://www.youtube.com/watch?v=vN235cq8xP4).
    S tou Q&A jsem otapetoval všechny aspoň trochu relevantní skupiny na FB, kde jsem.
-   Z [LinkedIn API Supportu](https://linkedin.zendesk.com/hc/en-us) jsem dostal rychlé a užitečné odpovědi.
    Bohužel však o tom, že všechna jejich API, která bych chtěl použít, mají jen OAuth 2.0.
    Myslím, že napíšu článek o tom, proč jsou OAuth 2.0 API nejvíc na hovno a nepoužitelná API, která z hloubi duše nenávidím.
-   Green Fox Academy se rozhodli napsat článek na základě jedné z epizod [našeho podcastu](https://junior.guru/podcast/).
    Poslali mi text a já jim to schválil.
-   Existuje internetový tvůrce, kterého sleduji, obdivuji, žeru vše co dělá a čerpám z jeho výtvorů inspiraci pro směřování svého byznysu.
    Má svou vlastní stránku na Wikipedii.
    Teď jsem se oklikou přes kamaráda dověděl, že ví o mé existenci.
    A nejen to!
    Dokonce mi velmi fandí a sleduje, jak se mi daří.
    Tak jsem se s tímto svým internetovým hrdinou hned propojil.
    A on se mi hned ozval a domluvili jsme se na schůzce, že něco vytvoříme spolu.
    Těšte se!
-   Všiml jsem si [Občan GPT](https://obcan.petrbrzek.cz/) a přesně něco takového bych chtěl pro klub a junior.guru.
    Je to pecka.
    Bavil jsem se o tom s kamarádem [Mílou](https://milavotradovec.cz/), který do toho vidí trochu víc a vymýšleli jsme, co a jak by šlo v tomto směru udělat.
-   Tři firmy nejspíš neprodlouží partnerství s junior.guru.
    Jedna kvůli ochlazení na trhu, dvě spíš proto, že jsem změnil ceník a už to pro ně nebude dávat smysl.
    S takovou restrukturalizací jsem při změnách v ceníku počítal, chtěl jsem spíš méně firem za více peněz, než mnoho firem za méně peněz.
    Můj čistý měsíční příjem se mezitím dostal na 54.000 Kč.
-   Při pátečku jsem si naprogramoval stahování kurzovního lístku z ČNB a udělal jsem si [tady](https://junior.guru/open/#cisty-zisk) přepočet toho čistého měsíčního zisku do dolarů a eur.
    Občas si čtu o zahraničních podnikavcích, kteří taky otevřeně sdílí svoje výdělky.
    Mají to však v jiné měně, tak se mi to špatně srovnává.
    Už mě nebavilo to pořád přepočítávat ručně, tak jsem si to naprogramoval.
-   Věnoval jsem se anketě mezi juniory, kterou připravujeme s ENGETO Academy.
    Připravil jsem poslední kousek, který jsem měl na starost.
    Naplánovali jsme si na dnešek call i s [Bárou](https://www.linkedin.com/in/baradrb/) a doladili na něm jak a co bude dál.
-   Nainstaloval jsem si [DiffusionBee](https://diffusionbee.com/), ale neměl jsem čas ani náladu si s tím zatím nějak hrát.
-   Přidal jsem [logování](https://docs.python.org/3/library/logging.html) do souboru.
    Doteď jsem měl na produkci `INFO` a lokálně `DEBUG`.
    Produkce teď ale šifruje artefakty, tak se tam může `DEBUG` ukládat do souboru a třeba mi to jednou pomůže s laděním.
    Lokálně mi zas přišlo, že je těch `DEBUG` výpisů už moc, tak jsem je vypnul a pro detaily si buď půjdu do souboru, nebo si level dočasně snížím.
-   Povedlo se mi [zapnout TouchID na zadávání `sudo` hesla v terminálu](https://apple.stackexchange.com/questions/259093/can-touch-id-on-mac-authenticate-sudo-in-terminal).
    O dost pohodlnější!
-   Dal jsem nějaké věci do skupiny [Vše za odnos Žižkov](https://www.facebook.com/groups/1155320448138033/).
    Většina z domu zmizela v řádu hodin.
-   Dnes jsem byl naposled v „podarovaném“ coworkingu.
    Nový jsem zatím nenašel.
    Komunikuji s [Pracovnou](https://www.pracovna.cz/), ale na Velikonoce budeme pryč, tak budu pokračovat až se vrátíme do Prahy.
-   Zjistil jsem, že můj někdejší velmi oblíbený učitel španělštiny dnes [vystupuje v televizi](https://www.ceskatelevize.cz/porady/10435049455-dobre-rano/423236100071027/cast/967934/) a dělá všelijaké prospěšné věci kolem vzdělávání dětí.
-   Dostal jsem DIČ.
    Hned jak mu [začala platnost](https://ec.europa.eu/taxation_customs/vies/#/vat-validation), zadal jsem ho do Simple Analytics, ImprovMX, Memberful, a pro jistotu i na GitHub, kdyby mi poslal fakturu za Copilot.
-   Přepsal jsem skript, který zastavuje předchozí buildy na hlavní větvi na CircleCI, aby taky používal [pycircleci](https://github.com/alpinweis/pycircleci) (viz předchozí poznámky).
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
    Psal jsem si s doktory, firmami, připomínal jsem lidem jejich úkoly, proplácel jsem nějaká špatně zaplacená členství, přidával mentory, uděloval stipendia.
    Dělal jsem si pořádek v osobních a rodinných financích.
-   Odmítl jsem jednu neplacenou spolupráci, ve které jsem neviděl benefity pro junior.guru.
    Myslel jsem si, že si před tím projdu [How to say no](https://www.starterstory.com/how-to-say-no) a to mi dodá odvahu, ale nakonec jsem to zvládl i bez toho.
-   Koupil jsem si nosič na kolo, ale chyběly tam nějaké šrouby a nenamontuju ho.
    Tak ho dneska ponesu zpět do prodejny.
    Nemají skladem další, tak snad nebudu celé jaro čekat na vyřešení.
-   Během 8 dní jsem při procházkách nachodil 6 km, ujel na kole 18 km. Celkem jsem se hýbal 7 h a zdolal při tom 24 km.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Udělám si jarní velikonoční pohodičku na Moravě.
2.  Pokud budu pracovat, mohl bych dopsat testy na věci kolem špendlíků.
3.  Pokud budu pracovat, mohl bych si pohrát s AI:
    Šlo by použít AI na vítání nových členů v klubu?
    Nebo na analýzu pracovních inzerátů?

Až se vrátím, chtěl bych začít tvořit ten katalog.
Je duben, nejvyšší čas pověnovat se i věcem, které jsem označil za největší priority tohoto roku!

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Konec domácích úkolů? Děti přetěžují, znechucují jim školu a jsou diskriminační](https://www.seznamzpravy.cz/clanek/domaci-zivot-v-cesku-konec-domacich-ukolu-deti-pretezuji-znechucuji-jim-skolu-a-jsou-diskriminacni-225907)<br>Co si myslíte o domácích úkolech? Měly by být jen dobrovolné? Nebo nechat? Zrušit?
- [Atomový kufřík Petra Pavla](https://mimo-agendu.ghost.io/atomovy-kufrik-petra-pavla/)<br>Návod jak rozchodit OpenAI Whisper pro české texty. Super postřeh o tom, jak si politici mohou vytvořit vlastní médium, kde nebudou nikým konfrontováni. A když jsem četl úderné „wake up!“ v závěru, měl jsem dojem, že se v tu chvíli v Economii musely roztřát okenní tabulky.
- [Opinion | This Isn’t What Millennial Middle Age Was Supposed to Look Like](https://www.nytimes.com/interactive/2023/03/14/opinion/middle-age-millennials.html)<br>Krize středního věku neexistuje. A jestli vůbec někdy pro někoho existovala, tak mileniálové mají úplně jiné starosti. Nemají na krizi středního věku ani čas, ani klid, ani peníze.
- [The BIGGEST BREAKTHROUGH in Mac gaming!](https://www.youtube.com/watch?v=dgd88zE3O38&t=110s)<br>Windows hry na Macu! Možná si jednou to svoje oblíbené Original War fakt ještě zahraju 😄
- [twenty-five years of curl | daniel.haxx.se](https://daniel.haxx.se/blog/2023/03/20/twenty-five-years-of-curl/)<br>Curl má 25 let. „It just took 21 years to make curl my job.“ píše Daniel Stenberg, maintainer a držitel několika ocenění.
- [Wokeness is not a politics](https://samkriss.substack.com/p/wokeness-is-not-a-politics)<br>„The problem is that intellectuals—myself included—are a weird, clammy, undersocialised lot, who spend a lot more time floating around in the bubbly otherworld of ideas than engaging with actual people. What happens if you ask a woke person what wokeness is? They’ll tell you that actually, there’s no such thing as wokeness. It’s not an ideology. It’s not a belief system. It’s just basic decency. It’s just being a good person.
They’re right. Wokeness is an etiquette.“
- [The End of Front-End Development](https://www.joshwcomeau.com/blog/the-end-of-frontend-development/)<br>„At every company I've worked at, we had tons of stuff we wanted to do, but we were constrained by the number of developers we had. What would happen if developers suddenly became 2x more productive? More bugs would be fixed, more features would be shipped, more profit would be made. There's no shortage of stuff to build, and so it's not like we'd run out of work for the devs to do. I actually think that this could increase the total # of developer jobs.“
- [Pod čarou: Číst méně encyklopedií, víc beletrie. Jinak nad AI nezvítězíme](https://www.seznamzpravy.cz/clanek/kultura-pod-carou-cist-mene-encyklopedii-vic-beletrie-jinak-nad-ai-nezvitezime-228364)<br>„Řada programátorů také propadá panice při poznání, že AI systémy dokážou docela dobře psát kód. Teoreticky jim tak sice zbyde více času na přemýšlení o tom, jaké lidské potřeby má příslušný software naplňovat a jak celou věc dobře komunikovat s uživateli i samotnou umělou inteligencí, ale to je opět věc, ke které jsou potřeba ony nenahraditelné a beletrií vytvářené schopnosti ztotožnění s jinými lidmi a pochopení hlubších zákonitostí jazyka i neverbální komunikace… Pokud to začneme s psaním a čtením literatury faktu příliš přehánět na úkor beletrie a budeme ke knihám přistupovat jen jako ke zdroji rychle a prakticky využitelných informací, nakonec můžeme paradoxně skončit jako lidská obdoba AI systémů.“
- [The £100BN Railway Dividing a Nation](https://www.youtube.com/watch?v=FSD5ps9bLQ0)<br>V Británii staví mega vysokorychlostní železnici. Vůbec jsem o tom projektu nevěděl, toto je krátký dokument o tom, jak se to staví a jaké to má problémy. Dopadne české VRT podobně?
- [The Future of Work With AI - Microsoft March 2023 Event](https://www.youtube.com/watch?v=Bf-dbS9CcRU&t=912s)<br>Sledoval jsem to jak přistání na Měsíci. Změní se všechno. To, co je ve videu, je obdoba toho, když někdo dokázal vyrobit telefon bez drátu. Přemýšlíme v zajetých kolejích a AI si tam jen sypeme jako koření. Až doopravdy pochopíme, co všechno s tím můžeme dělat, to bude teprve jízda. Jako když přišel smartphone.
- [The maze is in the mouse](https://medium.com/@pravse/the-maze-is-in-the-mouse-980c57cfd61a)<br>V Oraclu bylo slovo customer o dost víc přítomné, ale jinak mi to přijde dost podobné. Některé věty přímo rozbrněly moje pozapomenuté PTSD z korporátu. „Does anyone at Google come into work actually thinking about “organizing the world’s information”? They have lost track of who they serve and why. Having worked every day at a startup for eight years, the answer was crystal clear for me — I serve our users. But very few Googlers come into work thinking they serve a customer or user. They usually serve some process or some technology. They serve their manager or their VP. They serve other employees. They will even serve some general Google technical or religious beliefs. This is a closed world where almost everyone is working only for other Googlers, and the feedback loop is based on what your colleagues and managers think of your work. Working extra hard or extra smart doesn’t create any fundamental new value in such a world. In fact, in a bizarre way, it is the opposite.“
- [NOTION AI IS HERE – 10 Mind-Blowing Examples!](https://www.youtube.com/watch?v=0DIn0Ws9yTE)<br>Notion už má taky AI. Týpek ve videu ukazuje hned několik věcí, na které se to hodí.
- [(něco na Twitteru)](https://twitter.com/TheAnkurTyagi/status/1638550570704224265)<br>Přesný
