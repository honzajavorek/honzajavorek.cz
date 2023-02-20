Title: Týdenní poznámky: Schůzky a nekonečná administrativa
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/118


Utekl zas nějaký ten týden (10. 2. až 17. 2.) a tak [stejně jako minule]({filename}2023-02-10_tydenni-poznamky-famozni-prednaska-a-evidence-firem.md) sepisuji, co jsem dělal a co jsem se naučil.
Tvořím [junior.guru](https://junior.guru/) a nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/) a členy by mohlo zajímat, co dělám.
Psaní poznámek mi taky pomáhá nezbláznit se a nepropadat pocitu, že je konec týdne a já jsem nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


Celý týden se nesl v duchu nejrůznějších akcí a schůzek.
Skákal jsem od jednoho k druhému, ať už šlo o kafíčka a obědy s kamarády, vyzvedávání balíčků, přebírání klíčů nebo zapíjení narozených dětí.

K tomu se mi nahromadila nejrůznější administrativa a aktivita v klubu.
Až dnes jsem odpověděl na některé dva týdny staré e-maily.

S evidencí firem jsem za uplynulý týden bohužel moc nepokročil.
Doladil jsem stránky pro jednotlivé firmy, tady například [Red Hat](https://junior.guru/open/redhat/).
Ještě tam není všechno, ale už to trochu připomíná něco užitečného.
Hned s několika firmami jsem diskutoval podobu té stránky.


## Valentýnský dáreček od Discordu

Zjišťovali jsme, jak využít _push-to-talk_ na Discordu k tomu, aby se do přednášek nepřipojovali lidi se zapnutým mikrofonem a nerušili.
Využít to nejde, protože by si každý jeden uživatel musel pro tuto funkci nejdřív nastavit klávesovou zkratku.
Z hlediska použitelnosti to nic neřeší.

Zasnili jsme se o tom, že by bylo super, kdyby Discord umožnil video a sdílení obrazovky ve _stage_ kanálech, kde je správa práv k mluvení během události řešená dokonale.
Bohužel doteď byly tyto _stage_ kanály jen hlasové, po vzoru někdejšího Clubhouse, sociální sítě, která byla populární během covidu, zhruba měsíc nebo dva, ehm.

No a pak jsem se druhý den koukl do RSS čtečky a tam nový článek na blogu Discordu:
[Introducing Video, Screen Share, and Text Chat Support for Stage Channels](https://discord.com/blog/introducing-video-screen-share-text-chat-support-for-stage-channels)
Zvýšili i limity pro počty lidí, takže limit na přednášky už nebudu mít 24 členů, ale třeba 100 nebo kolik.
Vlastně můžeme přestat streamovat na YouTube.
Nepřestaneme, protože to má i jiné výhody, ale prostě…
Chtělo se mi brečet dojetím 😀
Já tady rok něco řeším a pak otevřu blog a prostě je to konečně vyřešené, tím nejdokonalejším způsobem, přesně tak jak jsem si to přál!

![Discord blog]({static}/images/screenshot-2023-02-17-at-17-13-45-introducing-video-screen-share-and-text-chat-support-for-stage-channels.png){: .img-thumbnail }


## Úpravy v klubu

Trochu jsem přeskládal klub a přidal tam další kanály typu fórum.

-   Přidal jsem nového moderátora, „povýšil“ jsem do této role svého pomocníka na videa Tinukiho, protože byl proaktivní a zodpovědný a má klub rád a tak vůbec.
-   Vytvořil jsem „fórum“ na „volná témata“ a vcucnul do něj kanály o kávě, F1, Minecraftu a dětech.
-   Kanál o kurzech jsem předělal na „fórum“ a přidal spoustu emoji s logy kurzů (abych je mohl použít na tématické štítky).
-   Vytvořil jsem kanál s deníčky.
    Tento kanál se stal instantním úspěchem, po jednotkách dní si v něm svůj poloveřejný deníček o cestě k první práci v IT píše už 10 členů.
-   Vytvořil jsem „fórum“ na skupinky, který řeší více věcí najednou. Předně by snad mohl fungovat lépe než kanál na parťáky, kteří tímto zanikli.
-   Předělal jsem přednáškový kanál na _stage_.
-   A tak dále, a tak dále, mohl bych pokračovat ještě deseti body, ale nevím, koho by to zajímalo.
    Klikal jsem na věci, nastavoval hejblátka, utahoval šroubky a přemýšlel nad tím, jak má co fungovat tak, aby to fungovalo co nejlíp.

Díval jsem se, co si členové klubu v prosinci „přáli od ježíška“ a většina z toho je splněna.

![Deníčky]({static}/images/screenshot-2023-02-17-at-17-13-01.png)


## Problém s Memberful API

Jeden celý den jsem řešil, proč mi z ničeho nic, na Valentýna, jedno Memberful API vrací 403 a obskurní HTML chybu místo JSON odpovědi.

Token správný.
IP adresa to není - z mého počítače i z produkce stejná chyba.

Zkusil jsem to přes Postman, funguje.
Zkusil jsem to přes curl, funguje.
Tak jsem udělal minimální dva řádky v Pythonu s requests knihovnou a ty nefungovaly.

Zapnul jsem veškeré logování Python vnitřností, abych dostal přesně bajty, které to posílá.
Zapnul jsem veškeré logování curl, abych dostal přesně bajty, které to posílá.
Jedno posílalo HTTP 1.1, druhé HTTP 2, ale tím to nebylo.
Když jsem u obou použil HTTP 1.1, stále to z Pythonu nefungovalo.

Tak jsem šel HTTP hlavičku po hlavičce a zkoušel rozdíly.
A zjistil jsem, že je problém s `User-Agent`.
To je hlavička, kam jde napsat skoro cokoliv ve stylu „ahoj API, já jsem nástroj bla bla ve verzi 123“ a ani tam nemusí být.
Ve světe prohlížečů nebo při scrapování má větší význam, ale u API jsem nezažil, aby měla nějaký vliv.
Tady jsem zjistil, že hodnota `curl/7.85.0` projde, ale `python-requests/2.28.2` neprojde, Cloudflare to hodí přes palubu.
To druhé nastavuje Python knihovna requests standardně pro jakýkoliv request, který přes ni kdokoliv dělá.

Přijde mi to absurdní, prý to ale dělá i Wikipedia: [User-Agent policy](https://meta.wikimedia.org/wiki/User-Agent_policy), [Etiquette](https://www.mediawiki.org/wiki/API:Etiquette).
Tak jsem to nastavil na `JuniorGuruBot (+https://junior.guru)` a hotovo, funguje, to.

Na Memberful supportu mi trochu pomohli, ale spíš jsem si to musel vyřešit sám.
Napsal jsem jim druhý den čím to bylo a poděkovali mi s tím, že to asi není chtěné chování a že se poradí se svými provozáky.


## Hledání terapeutů a doktorů

Jako jeden z cílů na letošek jsem měl vyhledání psychoterapeuta.
O víkendu jsem si na to našel čas a nějaké terapeuty proklikal:

1.  Šel jsem na [seznam od VZP](https://dusevnizdravi.vzp.cz/seznam-terapeutu/).
2.  Vyřadil jsem ty, kteří nemají volno.
3.  Vyřadil jsem ty, kteří jsou moc daleko.
    Čím blíž bude, tím spíš tam budu schopen chodit.
    (Zatím zkouším najít prezenční terapii, tu online zkusím až kdyby to nevyšlo.)
4.  Vyřadil jsem ty, kteří nemají zadanou žádnou webovku a nelze o nich nic zjistit.
    Tedy asi by o nich něco zjistit šlo, kdybych třeba hledal jejich jméno, ale to bych asi letos nestihl.
5.  Pár jsem si jich prošel a pak mi došly síly pokračovat ve výběru.

Rozpracovaný seznam jsem si uložil a někdy se k němu zase vrátím.
Volně jsem místo toho přešel k výběru psychiatra, protože se to zdálo jednodušší.

![VZP]({static}/images/screenshot-2023-02-17-at-17-15-54-dusevni-zdravi-vzp-cr.png){: .img-thumbnail }

V uplynulém roce jsem díky osvětě v médiích dostal podezření, že mám AD(H)D.
Co jsem zatím zjistil, např. z [téhle příručky](http://nepozornidospeli.cz/images/ADHD_prowebFIN.pdf), mě utvrdilo v tom, že bych měl zjistit, jak to doopravdy je.
A to zjišťování se jmenuje diagnostika ADHD a dělá ji psychiatr, protože ADHD je vrozená nemoc a nemoci léčí doktor a doktor na duševní nemoci se jmenuje psychiatr.
Ideálně psychiatr, který něco o ADHD u dospělých ví.
A takových moc není, protože u dospělých se to začalo řešit až nedávno.

Tím se ale dost zjednodušuje hledání!
Pro ujasnění, slovo „zjednodušuje“ v tomto případě znamená jen to, že nevybírám ze čtyř set stejně vypadajících položek, o nichž nelze nic dalšího dohledat.
Neznamená to, že je to nějak jednoduché.

V náhodné [Facebookovou skupině](https://www.facebook.com/groups/ADHDdospeli/) jsem v hloubi jejích připnutých příspěvků našel odkaz na [mapu s doktory](https://adhdospeli.cz/seznam-odborniku/).
K tomu jsem ještě vyhledal lidi, kteří se o ADHD u dospělých vyjadřovali jako odborníci do různých médií.
Předpokládám, že pokud někdo dělá na ČRo osvětu o ADHD u dospělých, tak o tom nejspíš něco ví.

Našel jsem asi 10 zařízení, do kterých jsem napsal stejný e-mail:

> Dobrý den
>
> je mi 36 let a v uplynulém roce jsem díky osvětě v médiích dostal podezření, že mám AD(H)D. Co jsem zatím zjistil, např. z http://nepozornidospeli.cz/images/ADHD_prowebFIN.pdf, mě utvrdilo v tom, že bych měl zjistit, jak to doopravdy je.
>
> Chtěl bych se zeptat, zda se na diagnostiku ADHD u dospělých specializujete, zda berete nové klienty, a zda lze na vaše služby nějak uplatnit moje zdravotní pojištění u VZP. Případně jestli nemáte tip na jiného doktora v Praze, který by mi mohl v mém snažení pomoci.
>
> Díky,
> Honza Javorek

Většinou mi během týdne napsali, že mají beznadějně plno, ale dostával jsem i vtipnější odpovědi.
Každopádně mi z toho vyšli zhruba dva doktoři.
Jeden má čas v květnu a druhý v červnu.
O víkendu se chci rozhodnout a někam se objednat.

Pokud vás téma zajímá, doporučuji [Michala Kašpárka na Facebooku](https://www.facebook.com/kasparek/posts/pfbid0Nm9pWJUdAY52oR87xxeDbzshoq3uA6s9KfhtosHcj9J8zWWQSHuVtdckTVxKK4YDl), Annu Košlerovou na ČRo:
[1](https://www.irozhlas.cz/zivotni-styl/zdravi/psychiatr-adhd-psychika_2207170700_ank),
[2](https://www.irozhlas.cz/zivotni-styl/zdravi/rozhovor-o-adhd-v-dospelosti_2206180600_ank),
[3](https://www.irozhlas.cz/zivotni-styl/zdravi/adhd-psychiatr-nudz-dusevni-nemoc-psychiatrie-deti-detska_2211260700_ank),
[Filipa Titlbacha ve Studiu N](https://denikn.cz/1000209/studio-n-jak-se-zije-s-adhd/),
[Matěje Skalického ve Vinohradské 12](https://www.mujrozhlas.cz/vinohradska-12/dospeli-adhd-nemate-ho-taky-snaz-se-pozna-lide-jsou-ochotnejsi-problemy-resit).


## Další

-   Publikoval jsem [novou epizodu podcastu](https://junior.guru/podcast/) s Tomášem Ervínem Dombrovským z LMC a je to libový, poslechněte si to!
    Každou druhou větu bych mohl citovat v příručce.
    Posílám srdíčka!
-   Kamarádka má zaplacený ještě měsíc a půl v nedalekém coworkingu a nevyužije ho už.
    Nejde to zrušit.
    Tak mi to podarovala a budu tam teď asi chodit.
    Už jsem tam jedno odpoledne zkoušel pracovat a nebylo to vůbec špatné!
    Jsem zvědav, jaký si vymyslím režim.
    Je to pěkná příležitost si to vyzkoušet.
    Těším se na změnu a experimentování.
    Kamarádce tímto ještě jednou děkuji!
-   [Podpořil jsem PyCon NA na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7032007586929344513/) a dal jsem to i do klubu.
    Někteří opravdu přispěli, jóóóó!
-   Zjišťoval jsem, proč lidé nemohou vytvářet události v klubu, i když jsem na to dal práva všem členům.
    Nakonec se ukázalo, že Discord to považuje za funkci s širším oprávněním, u které vyžaduje, aby člověk měl přihlašování s 2FA.
    To je milé, ale mohli to napsat do té chybové hlášky.
    Nejsem sám, kdo z toho byl zmatený: [1](https://www.reddit.com/r/discordapp/comments/qvec5s/cant_schedule_events_in_a_server_i_admin/), [2](https://www.reddit.com/r/discordapp/comments/u7cavj/create_events_missing_permissions/)
-   Napsal jsem jednomu borcovi, který na YouTube učí lidi Swift, jestli by nechtěl do klubu.
    Napsal jsem jedné přednášející [odjinud](https://www.linkedin.com/posts/reactgirlsprague_meetup-activity-7029815878296698880-YOFC), zda by nechtěla přednášet i v klubu.
    Psal jsem si s [Nasťou](https://www.linkedin.com/in/anastazie-sedlakova/) a domlouval její přednášku v klubu.
    Přidal jsem nového mentora, [Martina](https://www.linkedin.com/in/martinkolareu/).
-   Udělal jsem review snad na pět CVček.
    V klubu se tohle teď fakt rozjelo.
    Vytvořil jsem dobrovolnou roli v klubu pro ty, kdo by s tímhle chtěli pomoci, ale zatím jsem tam jen já a Dan.
-   Ve [Tvůrcastu](https://podcasts.apple.com/cz/podcast/tv%C5%AFrcast/id1657971770) jsem slyšel o [Festivalu o psaní](http://www.festivalopsani.cz/) a hned jsem si koupil lístek.
    Psát dokážu, ale mohl bych to umět lépe.
    Už delší dobu cítím velké mezery v tom, jak úderně nebo stručně dokážu psát.
    Měl bych se v tom cíleně začít zlepšovat, pokud chci, aby psaní bylo můj primární způsob tvorby obsahu.
-   Uložil jsem si do osobního kalendáře termíny všech letošních závodů F1.
-   Nabídl jsem dvěma lidem, jestli nechtějí naprogramovat něco, co by se mohlo stát součástí junior.guru.
    Jsem zvědav, jak to dopadne.
-   Vytvořil jsem skript, který možná pomůže jednomu členovi klubu s psychikou a organizací sebe sama.
    Uvidíme.
-   Konečně jsem si našel čas pohrát si s ChatGPT.
    API mají, takže zvažuji, jak to využít v klubu.
    Mimochodem, [MacGPT](https://app.gumroad.com/d/0b51ea811553c333113e727b0f055efe) vypadalo jako užitečná appka, ale jak bývá teď ChatGPT dost přetížené, je asi lepší chodit rovnou přes web.
    Mají tam nějaké kontroly prohlížeče, aby se bránili proti robotům, a vypadá to, že MacGPT tím mnohdy neprojde.
    Přidal jsem se taky na OpenAI Discord.
    Ze zvědavosti.
-   Jedna firma mi napsala nedočkavý e-mail, že kdy už si bude moci zaplatit zvýraznění v katalogu vzdělávacích agentur a jestli už existuje.
-   Opravoval jsem odkaz, který má z junior.guru mířit na Red Hat.
    Překvapilo mě, že není jen v nabídkách práce, ale mám ho na mnohem víc místech, dokonce i přímo v příručce.
    Na to jsem však přicházel postupně, vždy když mi někde selhala kontrola odkazů, apod.
    Byl to tedy větší úkol, než jsem čekal.
-   Odsouhlasili jsme si prodloužení spolupráce s firmou, která má logo na příručce a platí si nejdražší tarif.
    Penízky, penízky!
-   Až před časem jsem zjistil, že v Pythonu mohu použít `%-d` pro formátování např. dne v týdnu, místo `%d`.
    S tím spojovníkem to nevypíše nulu před číslem, takže květen je 5 a ne 05.
    Nyní jsem změnil i starší kód tak, aby tuto věc využíval a je to krásné.
    Bohužel jsem při hledání a nahrazování udělal špatně odhalitelnou chybu.
    Na tu mě upozornil až kamarád, který si četl stránku s grafy a bylo mu divné, jak vypadá graf s počtem příspěvků v klubu.
-   Graf s počtem příspěvků v klubu jsem nakonec stejně změnil na [graf počtu napsaných písmenek](https://junior.guru/open/#aktivita-v-klubu).
    Přijde mi to adekvátnější číslo lépe reflektující úsilí vložené do psaní zpráv, než počet zpráv.
-   Opravil jsem malou chybu ve věci, která sdílí články z toho blogu na Telegram.
    Už to začínám mít fakt vyladěné.
    Myslím, že už mám [90 % hotovo](https://en.wikipedia.org/wiki/Ninety%E2%80%93ninety_rule).
-   Odpovídání v klubu, e-maily, [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), atd.
    Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
    Bylo toho nějak moc!
    Mám pocit, že za poslední týden se v klubu jen představovalo 15 nových lidí.
    Lidi dávali CVčka na review, diskutovali.
    Nestíhal jsem odpovídat na e-maily.
    Nestíhal jsem pracovat na jiných věcech.
    Uf.
-   Během 8 dní od 10. 2. do 17. 2. jsem naběhal 13 km, při procházkách nachodil 12 km. Celkem jsem se hýbal 7 hodin a zdolal při tom 25 kilometrů.
-   Finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).
    Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)


## Povedlo se

Udělal jsem něco z [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md)?

-   V podstatě jsou skoro hotové „firma musí vědět vše o svém předplatném, v jakém je stavu, kolik čeho zbývá“ a „já i firma musíme mít včas informaci, že se blíží konec“, i když bych si je představoval trochu lepší.
-   Zapracoval jsem na „najdu si terapeuta“.
-   Udělal jsem „pohraju si s AI“, i když jsem si to teda spíš představoval tak, že opravdu už naprogramuju něco, co to využívá.

<!-- Koukni sem https://www.icloud.com/notes/092v6QG3aoSmpVOGHnpg0uIXQ -->


<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví.**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>


## Plánuji

1.  Měl bych promovat přednášku v klubu, pohovory nanečisto, novou epizodu podcastu 😵‍💫
2.  Pošlu podklady pro daňové přiznání.
3.  Fakt už dokončím tu evidenci firem.


## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel toto:

- [Feri se rozhodl hájit za každou cenu a vyslal nebezpečný signál obětem sexuálního násilí](https://www.e15.cz/nazory/feri-se-rozhodl-hajit-za-kazdou-cenu-a-vyslal-nebezpecny-signal-obetem-sexualniho-nasili-1396624)<br>Pokud sledujete kauzu Feri, toto by nemělo zapadnout.
- [core-js/2023-02-14-so-whats-next.md at master · zloirock/core-js](https://github.com/zloirock/core-js/blob/master/docs/2023-02-14-so-whats-next.md)<br>Tohle je úplně šílená story. Zahrnuje polovinu internetu, open source, vězení, Rusko, celý JavaScriptový ekosystém, a mnoho dalšího… „Developers love to use free open-source software - it’s free and works great, they are not interested in that many and many thousands of hours of development, and real people with their own problems and needs are behind it. They consider any mention of this as an invasion of their personal space or even a personal affront. For them, these are just gears that should automatically change without any noise and their participation.“
- [Is Google’s 20-year dominance of search in peril?](https://www.economist.com/business/2023/02/08/is-googles-20-year-search-dominance-about-to-end?utm_medium=social-media.content.np&utm_source=facebook&utm_campaign=editorial-social&utm_content=discovery.content)<br>Má Microsoft šanci ukousnout si od Googlu část vyhledávání?
- [I hope I’m wrong!](https://www.garbageday.email/p/i-hope-im-wrong#%C2%A7where-will-traffic-come-f)<br>Jak bude vypadat budoucnost internetu? Pro ty z nás, kdo pamatujeme blogy a odkazy, nejspíš smutně. „If an A.I. arms race within social has turned every platform into a video platform and is turning our search engines into chatbots, how do you get people to look at your website? Not even just for little guys like me, but even for big publishers.“
- [How Might the Violence in Ukraine Come to an End?](https://www.spiegel.de/international/world/a-year-after-putin-s-invasion-how-might-the-violence-in-ukraine-come-to-an-end-a-e01a431e-cb92-44f6-aed8-8fe538e27640)<br>Půjde to vůbec nějak ukončit?
- [Javornicko: nejkrásnější český region trápí odliv obyvatel a nekonečné vzdálenosti](https://a2larm.cz/2023/02/javornicko-nejkrasnejsi-cesky-region-trapi-odliv-obyvatel-a-nekonecne-vzdalenosti/)<br>„Obce mohou opravit s pomocí dotací kde co, ale onu mytickou továrnu pro dvě stě lidí zařídit nedokážou. Nedokážou zlepšit dopravní infrastrukturu tak, aby cesta sem netrvala odevšad nekonečně dlouho.“ Vtipná a zároveň smutná reportáž z krásné, ale ekonomicky a sociálně vyloučené periferie republiky.
