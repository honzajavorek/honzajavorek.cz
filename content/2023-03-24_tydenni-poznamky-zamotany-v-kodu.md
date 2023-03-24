Title: Týdenní poznámky: Zamotaný v kódu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-03-17_tydenni-poznamky-pruzkumy-pripravy-a-podcast.md) už utekl nějaký ten týden (17. 3. až 24. 3.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Programování nesmyslů

Minule jsem psal:

> Pak jsem ještě přepracoval způsob, jakým vypínám a zapínám, zda může bot zapisovat do různých služeb.
> Chci totiž, aby se muselo explicitně zapnout, že může zapisovat změny do Discordu nebo do Memberful API.
> Na produkci je to vše zapnuté, ale při vývoji mi to brání udělat nevratné chyby ledabylým spouštěním příkazů.
> Nebudu to tady rozepisovat, bylo by to dost technické, ale s výsledkem jsem dost spokojen.

Samozřejmě to nebylo tak jednoduché.
Našel jsem v tom spoustu nedomyšleností a chyb.
Strávil jsem s tím postupně pondělí, úterý, středu…
Poznatky:

-   Když mám v Pythonu globální proměnnou a pak si přes `multiprocessing` udělám proces, tak ten ji nemá.
    Tohle jsem zjistil při debugování, proč mi nic nefunguje a byl to velký heuréka moment, ale radost jsem vlastně moc neměl.
    Data si explicitně předávám mezi procesy a už to nechávám tak, ale zpětně si říkám, zda nakonec nebyly přepínače přes _environment variables_ víc [KISS](https://en.wikipedia.org/wiki/KISS_principle).
-   Povedlo se mi napíchnout do Discord klienta a při vypnutém zapisování do Discordu nechat kód spadnout, pokud se pokusí přes HTTP poslat nějakou metodu, která není [idempotentní](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent).
    Perfektní pojistka!
    Hned mě to upozornilo na několik situací, které jsem neošetřil.

Asi vám nemusím popisovat, zda mám po tomto týdnu pocit z dobře odvedené práce.
Zamotal jsem se do kódu, seděl nad tím dny a výsledkem je akorát „lepší kód“, místo abych dokončil něco, co má reálně dopad na uživatele.


## Anketa

Z ENGETO Academy přišly poslední dílky ankety, ale já jsem nezvládl dodat svůj poslední dílek.
Zato jsem sepsal vše pro [Báru](https://www.linkedin.com/in/baradrb/), která nám má s anketou pomoci.

Mezitím koukám, jak vychází ankety [všude možně jinde](https://www.czechitas.cz/blog/dvere-do-it-maji-juniori-otevrene-zajem-o-it-je-podle-firem-dulezitejsi-nez-diplom).


## Přednáška a YouTube

[Propagoval jsem](https://www.linkedin.com/posts/honzajavorek_daedtafx-djangogirls-python-activity-7043536893803667456-bWYS) úterní přednášku v klubu s [Nasťou Sedlákovou](https://www.sedlakovi.org/) o tom, jak zvládat kariéru s dětmi za zády.
Přednáška vyšla parádně, opravovali jsme pak akorát trochu zvuk, ale i to zajistil můj pomocník Tinuki.
Ohlasy [nadšené](https://witter.cz/@banterCZ/110068564967005849).

![Nasťa]({static}/images/20230321-44f42c2275ac69c98bd565bff92ffd41b19644079e3cfd8155a76067ef13521d-yt.png){: .img-thumbnail }

Našel jsem kanál [YouTube Creators](https://www.youtube.com/channel/UCkRfArvrzheW2E7b6SVT7vQ), kde vychází novinky pro tvůrce na YouTube.
Přidáno do RSS čtečky.
YouTube se snaží se svými Shorts čelit nástupu TikToku, teď chystají [velkou ofenzivu na podcasty](https://www.youtube.com/watch?v=feMd_GvZSf4) (zatím nedostupné v ČR), z čehož asi nemá radost Spotify.
Už teď tam mám přednášky (pro členy), podcast (přes [Headliner](https://www.headliner.app/)), budou tam moje live Q&A.
Čím dál víc mi dává smysl rozvíjet tam [kanál](https://www.youtube.com/channel/@juniordotguru) a publikum, bez ohledu na formáty, kterým se chci do budoucna věnovat.

![Moje Q&A]({static}/images/20230411-2882f31d997e2dc52be20720fdcb875c5d608d57f4a0c66de27147cd55918894-dc.png){: .img-thumbnail }

PyLadies jsem slíbil, že do konce týdne poskytnu informace k chystané Q&A.
Doladil jsem tedy titulek, popisek a plakátek.
Výsledek k vidění přímo na YouTube: [Honza Javorek: Programování jako kariéra? Ptej se! (Q&A)](https://www.youtube.com/watch?v=vN235cq8xP4)
Sdílejte všem, kdo by se mě mohli chtít na něco zeptat 😅


## Pracovní místo

S koncem března mi bude končit „podarované“ pracovní místo v Karlínském coworkingu.
Bylo perfektní, že jsem to mohl vyzkoušet a donutilo mě to zkusit přeskládat každodenní režim.
V práci odjinud než z domova bych rád pokračoval, ale ne tam, kam jsem teď chodil.

Uvažoval jsem o [Pracovně](https://www.pracovna.cz/en/cowork), ale Nasťa mi dala tip, že v [Radosti nabízí levné kanceláře](https://www.dumradost.cz/cs/pronajem/kancelare), tak to omrknu nejdřív tam.
Poslal jsem jim poptávku.
Pobavilo mě, že „malá zasedačka“ je pro 25 lidí, velká pro 70–100 osob.


## Špendlíky a šifrování

Když někdo dá v klubu reakci špendlíku k libovolné zprávě, bot mu ji uloží do soukromých zpráv.
Tato funkce je implementovaná příšerně.
V listopadu 2021 jsem si udělal poznámku, že zpracování špendlíků trvá moc dlouho, 2,5min.
A že to mám přepsat.

Pak mám poznámku z června 2022, že to trvá 6min.
Teď to trvá 7,2min a bot mi kvůli tomu čím dál častěji spadne.
Tak jsem si řekl, že jsem chtěl sice dělat jiné věci, ale tohle už hoří, tak to předělám.

Jeden z problémů je, že bot neumí efektivně pracovat s historií soukromých konverzací, které vede s členy klubu.
Bylo by snadné zprávy uložit do SQLite, ale jsou to soukromé zprávy a i když jsou mezi botem a uživatelem, členové si nejspíš nemyslí, že když tam něco napíšou, objeví se to pak někde v zipu ke stažení.

Jako první jsem tedy přistoupil k tomu, co jsem chtěl stejně udělat už dávno, a to k zašifrování záloh databáze.
Pro jednoduchost jsem zvolil symetrické GPG.
Nechal jsem 1Password vygenerovat silné heslo a napsal jsem si nové příkazy do svého CLI v [click](https://click.palletsprojects.com/)u, které umí zašifrovat zip, odšifrovat, stáhnout z CircleCI.

-   Chtěl jsem použít nějakou „novou“ šifru `ed25519`, ale nepovedlo se mi to na macOS rozchodit, tak jsem to vzdal.
-   ChatGPT mi pomohlo správně formulovat jednotlivé GPG příkazy.
-   Nejdřív jsem chodil na CircleCI API jen tak z `requests`, ale čím víc toho bylo, tím to byla větší otrava.
    Použil jsem místo toho [pycircleci](https://github.com/alpinweis/pycircleci/).
-   Příkaz na zašifrování a rozšifrování si dokáže heslo přečíst z mého 1Passwordu.
    Není to sice moc přenositelné, ale pro mě velice pohodlné a se svým týmem vývojářů, čítajícím pouze mou osobu, jsme se shodli, že to tak být může.

![ChatGPT a GPG]({static}/images/screenshot-2023-03-24-at-17-58-10.png){: .img-thumbnail }


## Daně

Odeslal jsem daně a přehledy za rok 2022.
S datovkou a [MojeID](https://www.mojeid.cz/) to bylo za 10 minut hotové.

Daňař mi poslal dokument k podepsání.
Do PDFka jsem na jeden klik plácl [podpis v macOS Preview](https://support.apple.com/guide/preview/fill-out-and-sign-pdf-forms-prvw35725/mac) a pak jsem to prohnal přes [lookscanned.io](https://github.com/rwv/lookscanned.io).
Hotovo!
Od 25.3.2023 jsem [identifikovanou osobou](https://www.jakpodnikat.cz/identifikovana-osoba-k-dph.php#anid0), další velký úkol splněn.


## Doktoři

Zhoršily se mi vrozené potíže s kůží.
Nejdřív jsem to nějak „jako vždycky“ odbýval, ale najednou to nestačilo, tak se to vymklo kontrole.
Pokorně jsem tedy najel na přísný režim, zrušil sporty, nasadil masti.
A jal se najít dermatologa, který by mě po letech přijal do dlouhodobé péče.
Doktora jsem našel.
Na květen 😀
Naštěstí ale režim zafungoval a už to mám zase pod kontrolou.

Obvodní lékařka mi neodepisovala na e-mail (prosbu o recept), tak jsem jí zavolal.
Minulý týden měla dovolenou.
Tohle se mi stalo už poněkolikáté, přitom je to vždy u ní na webu v aktualitách.
Napadlo mě, zda nemají RSS.
Mají!
Takže už ve své RSS čtečce odebírám i aktuality své obvoďačky.
Moc jich není, ale o to důležitější bývají.

![Aktuality]({static}/images/screenshot-2023-03-24-at-18-00-12.png){: .img-thumbnail }


## Rozbilo se samo

Blbla mi instalace projektu, tak jsem upgradoval na nejnovější [Poetry](https://python-poetry.org/).
To způsobilo [další problémy](https://github.com/python-poetry/poetry/issues/7184).
Tak jsem upgradoval Python z 3.10 na 3.11, na hlavním repozitáři i na realtime botovi.

Přestala fungovat normalizace adres u pracovních inzerátů.
Seznam totiž [přesunul HTTP API Mapy.cz na jiné místo a změnil režim přístupu](https://developer.mapy.cz/rest-api/).
Psal jsem si s nimi, ale během „beta“ režimu neumí zatím nabídnout menší balíček, než [800 Kč/měs](https://developer.mapy.cz/cena/cenik-premioveho-uziti/).
To pro mě nedává vůbec smysl.
Mám prý počkat, až to bude pro veřejnost a sledovat [developer.mapy.cz](https://developer.mapy.cz/).
Tak jsem to nějak zatím hacknul a čekám.

![API zmizelo]({static}/images/screenshot-2023-03-21-at-14-23-12.png)

V pátek GitHub [změnil SSH host klíč](https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/) a rozbil tím půl vývojářského internetu.
Musel jsem to opravit lokálně a na CircleCI upgradovat [git-shallow-clone-orb](https://github.com/guitarrapc/git-shallow-clone-orb), kde autor naštěstí urychleně vydal novou verzi.


## Další

-   [Zaznamenal jsem](https://github.com/juniorguru/juniorguru-chick/issues/) pár dalších nápadů pro realtime bota.
-   Dočetl jsem [The Middle Ages: A Graphic History](https://www.goodreads.com/book/show/52930474-the-middle-ages).
    Pěkné to bylo!
-   Experimentuji s [Pocketem](https://getpocket.com/).
    Napadlo mě, že bych si tam mohl posílat náhodné články z internetu a pak je přes RSS vytáhnout do své RSS čtečky.
    Bohužel jejich RSS má jen 30 položek (na supportu mi potvrdili, že to je _feature_ a ne _bug_).
    A není tam nic než nadpisy a odkazy.
    Neznáte jiný nástroj, kam jde snadno z počítače i z mobilu posílat odkazy a pak je dostat jako neomezené RSS?
-   Sešel jsem se s kámošem Jožou, probrali jsme spolu drby ze světa práce, plány s junior.guru mentoringem nebo katalogem kurzů, vypili kafe, půjčil mi komixy.
-   Navštívila nás babička, tak jsem byl na rande s manželkou.
-   Zavolal jsem si s Iry, které jsem potkal v listopadu díky kamarádům z Afriky, kteří jeli do Prahy na Ubuntu Summit.
    Bavili jsme se o životě a o tom, jak zvládáme podnikání.
    Oni ve dvou lidech dělají [Zorin OS](https://zorin.com/).
    Poradili mi, že až budu řešit rozúčtovávání DPH do každé země zvlášť, jako musí oni, může se mi hodit vědět, že existuje [Paddle](https://www.paddle.com/).
-   Narazil jsem na článek na [blogu portálu Navolnénoze.cz](https://navolnenoze.cz/novinky/blog/).
    Ten blog znám, vychází tam dobré věci, ale v RSS čtečce jsem ho neměl.
    Tak si ho jdu přidat a najednou koukám, že [Novinky](https://navolnenoze.cz/novinky/) jsou úplně přesně to, co jsem v předešlých poznámkách popsal jako svůj „záměr s newslettery“ 😀
-   Svůj postup při plnění [svých plánů]({filename}2022-12-26_strategie-na-2023.md) jsem přesunul do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
    Když jsem naposledy zkoušel používat GitHub Projects, vůbec to nebylo tak nabušené jako teď!
    Příjemné překvapení, používá se to suprově.
-   Udělal jsem změny v šabloně pro týdenní poznámky, abych ji co nejvíc zestručnil a změnil jsem úvodní obrázek, aby si lidi všimli, že je něco jinak.
    Poznámky samotné se mi bohužel opět nepovedlo napsat kratší.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
    Napsal jsem (konečně) firmám, kterým bude brzy končit partnerství.
    V Python komunitě jsem věnoval hodně času formulování svých myšlenek co se týče účelu a budoucnosti [blog.python.cz](https://blog.python.cz/).
    Řešil jsem jeden ztracený login na Discord a dvě stipendia.
-   Během 8 dní jsem při procházkách nachodil 5 km, na túrách nachodil 6 km, ujel na kole 18 km. Celkem jsem se hýbal 7 h a zdolal při tom 29 km.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Přebuduji funkci na špendlíky.
2.  Rozmyslím MVP katalogu vzdělávacích agentur.
3.  Promo mojí Q&A a poslední epizody podcastu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [20 let od invaze do Iráku. Vedla k chaosu i nástupu Islámského státu, Ameriku stála důvěryhodnost, říká analytik - VOXPOT](https://www.voxpot.cz/dvacet-let-od-invaze-do-iraku-vedla-k-chaosu-i-nastupu-islamskeho-statu-ameriku-stala-duveryhodnost-rika-analytik/)<br>„…ať už šlo o ten nepravdivý argument zbraněmi hromadného ničení, či o invazi bez souhlasu Rady bezpečnosti OSN, Abú Ghrajb nebo rozpad iráckého státu – to vše poměrně výrazně podlomilo roli, kterou USA měly na začátku 21. století.“
- [Kara Lawson: Handle Hard Better](https://www.youtube.com/watch?v=oDzfZOfNki4)<br>Motivační formulka 💪
- [(něco na Twitteru)](https://twitter.com/brdskggs/status/1637114268876144640)<br>GPT usnadnilo rozesílání necíleného spamu, protože dokáže bez vynaložení jakékoliv energie vytvořit zprávu, která cíleně vypadá. Vypadá to však, že to jde řešit 😄
- [(něco na Twitteru)](https://twitter.com/jacksonfall/status/1636107218859745286)<br>AI dostala $100 a úkol co nejrychleji z nich udělat co nejvíc peněz. Twitter vlákno.
- [Nasa reveals new spacesuit for Artemis moon landing](https://www.theguardian.com/science/2023/mar/16/nasa-reveals-new-spacesuit-for-artemis-moon-landing)<br>Nové astronautské obleky NASA
