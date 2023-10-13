Title: Týdenní poznámky: Famózní přednáška a evidence firem
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/111


Utekl zas nějaký ten týden (3. 2. až 10. 2.) a tak [stejně jako minule]({filename}2023-02-03_tydenni-poznamky-schuzky-a-evidence-firemnich-partnerstvi.md) sepisuji, co jsem dělal a co jsem se naučil.
Tvořím [junior.guru](https://junior.guru/) a nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/) a členy by mohlo zajímat, co dělám.
Psaní poznámek mi taky pomáhá nezbláznit se a nepropadat pocitu, že je konec týdne a já jsem nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


<!-- Honzo, piš jednu větu na řádek! https://sive.rs/1s -->


## Zuzana Pechová: Základy bezpečnosti pro vývojáře

V klubu proběhla přednáška od [Zuzany Pechové](https://www.linkedin.com/in/zuzanapechova/).
Mělo to nejživější diskuzi, jakou pamatuju.
Dostali jsme se poprvé v historii klubu na strop 25 lidí na video hovoru.
Byla tam spousta užitečných tipů a všem se to moc líbilo!
V klubu 20 reakcí na záznam přednášky a záznam má po dvou dnech skoro 90 _views_.

Podle mě to bylo jednoznačně poučné a zároveň podané formou, kterou junior pochopí.
Kombinace obojího se moc nevidí.
Spoustu zajímavých věcí jsem se dověděl i já.
Něco málo o bezpečnosti vím, ale moc se v tom nerochním, takže jsem byl rád za výlet do tématu.
A dověděl jsem se i dobré tipy, které by se daly dát časem na web.

![Plakát k přednášce]({static}/images/20230207-3f4025980ff02dba215a2a5c26de32b5dbc2f9e1a7bc3dcd44c45fc83495afc1.png){: .img-thumbnail }

Co se týče techniky, tak záznam zajišťoval Tinuki a opět vše skvěle klaplo.
Sice jsme dosáhli na strop účastníků, ale byl k dispozici online stream na YouTube, takže kdo by se chtěl ještě přidat, mohl přednášku aspoň sledovat.

Při velké účasti se však hned několikrát stalo, že se připojili lidi se zapnutým mikrofonem, aniž by si to uvědomili, a způsobili tak nepříjemný ruch.
Tohle s Tinukim zkusíme vyřešit zapnutím _push-to-talk_ v přednáškárně pro běžné smrtelníky, ale nejdříve to chceme vyzkoušet.
Také jsem dal Tinukimu oprávnění vypínat druhým lidem mikrofon, pokud by byl rychlejší než já.


## Evidence firem

Pokročil jsem v programování transparentní evidence partnerství s firmami.
Z výsledku mám radost, ale zároveň jsem tento týden věnoval možná až moc času různé administrativě a proto není evidence stále ještě hotová.
Máme půlku února a [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md) mě čeká ještě spousta.

-   Kód je nyní schopen zjistit, jestli byla firma uvítána v klubu a kdy.
-   Dokumentuji si do YAMLu, zda jsem firmu uvítal na sociálních sítích a kdy.
-   Dokumentuji si do YAMLu všechna další ujednání, která s firmami mám.
    Nejen abych byl transparentní, ale také abych si to sám pamatoval.
    Takhle budeme já i firma hned vědět, co jsme si domluvili nad rámec ceníku, co už je hotovo, a co chybí.
-   Doplnil jsem kód, který mi umožňuje vypsat benefity z tarifu, které jsou obohaceny o informaci, zda je daný benefit už splněn.
    Téměř vše se samo zjišťuje z databáze.
-   Opravil jsem propojení firem a podcastů, našel jsem v tom chybu.
-   Přidal jsem hromadu testů na různé části kódu.

![Partnerská stránka]({static}/images/screenshot-2023-02-10-at-11-55-14-partnerstvi-s-firmou-red-hat.png){: .img-thumbnail }
Zatím jsou informace jen tak ledabyle naházené do stránky. Ale jsou tam!


## E-maily na Memberful

Chtěl jsem v Memberful nastavit e-mail, který se lidem pošle, když zruší předplatné.
Cílem bylo především doručit k nim informaci, že mohou zažádat o stipendium, pokud jim klub přijde příliš drahý.

Posílání e-mailu jsem zapnul a sepsal jsem jeho obsah.
Prošel jsem ale i všechny zbylé e-maily a aktualizoval je.

![Nastavení e-mailů v Memberful]({static}/images/screenshot-2023-02-10-at-11-57-51-subscription-canceled.png)

Změnil jsem tón e-mailů a osobu, která je píše.
Původně to chodilo z `hello@`, teď to chodí z `kure@` a texty jakoby píše můj robot kuře.
V prvních e-mailech se lidem představí, v dalších už jen navazuje prostým „Ahoj, tady kuře.“

Přijde mi to lepší, než se tvářit, že e-maily píšu já osobně.
Stále je to vše přátelským tónem, ale už to jasně dává najevo, že jde o automaticky posílaný e-mail.
Lidé mohou na e-mail odpovědět a mají informaci, že taková odpověď přijde přímo mně a budu ji řešit.

Podobně můj „robot kuře“ komunikuje i v klubu, takže to lidi znají i odtamtud.
Lidé vědí, že mi pomáhá a je stejně „zábavné“ jako já, ale že je to jen robot.
Ideálně by veškerá má automatizovaná komunikace byla „od kuřete“, ať už jde o zprávy na Discordu nebo e-maily, zatímco živé odpovědi jsou „od Honzy“.

Jako kuře se identifikují i commity v Gitu, které automaticky posílám ze CI na GitHub (např. když CI nechám formátovat kód).

V souvislosti s tím vším jsem registroval pro e-mail `kure@` i [Gravatar](https://gravatar.com), aby si různé služby mohly k této adrese automaticky přiřadit obrázek.


## Další

-   Kontaktoval jsem daňaře, že bychom měli začít pracovat na přiznání.
    Vyžádal si podklady a teď je řada zase na mé straně.
    Až doděláme přiznání, vrhneme se na přechod na identifikovanou osobu, abych mohl i jako neplátce DPH volně nakupovat služby z EU.
-   Docházejí mi přednášející.
    Nějak jsem je zapomněl shánět.
    Kamarádka mi dala pár tipů na lidi, kteří se zabývají testováním.
    Komunikuji také s programátorkou, která by mohla mít přednášku o tom, jak v IT zvládat práci a děti.
    Chtělo by to ale přitlačit a domluvit zase nějakých třeba pět přednášek dopředu.
-   Psal jsem na Memberful support a posílal jim chyby v českém překladu.
    Překlady objednávají u externího dodavatele, takže jejich odpověď byla spíš vlažná.
    Nejspíš tedy budou místo dobropisu nadále posílat „dluhovou poznámku“.
-   Poprvé v historii junior.guru se mi stalo, že mi poptávku na partnerství s klubem poslala firma, kterou neznám, s lidmi, které neznám.
    Pracovní inzeráty chtěly vystavit různé firmy, ale partnerství za spoustu peněz, to byla vždy záležitost nějakých kontaktů, srazů, konferencí, kamarádů.
    Green Fox Academy se mi sice taky ozvali sami, ale tam jsme o sobě dlouhodobě tak nějak věděli, protože podnikáme v podobném segmentu.
    Firmu jsem rychle během týdne zprocesoval a brzy bude mít logo na webu.
-   Volal jsem si s ENGETO Academy, abychom se zase o kousek posunuli v přípravách ankety pro juniory.
    Šlo nám to hezky od ruky.
-   Dobrý kamarád plánuje poslat CVčko na _dream job_, který si někde vyhlédl.
    Nějaký čas jsem tedy strávil tím, abych se na to všechno podíval, okomentoval mu to a dal mu spoustu doporučení.
-   V 1Password doplňku do Firefoxu mi přestalo fungovat přihlášení přes TouchID.
    Našel jsem na internetu nějakou radu, že s verzí 8 to nefunguje.
    To mě rozčílilo a napsal jsem emotivní zprávu na jejich support.
    Než odpověděli, začalo to samo zase fungovat.
    Možná se něco aktualizovalo, nebo restartovalo.
    Byli milí a trpěliví.
    Upozornili mě, že rada z fóra je 2 roky stará a že by to fungovat mělo.
    Dali mi tipy a poslali dotazy, aby mi pomohli problém odladit.
    Omluvil jsem se jim a poděkoval za trpělivost s takovými panikařícími lidmi.
-   Zdá se, že jsem konečně opravil kapající vodovodní kohoutek v kuchyni.
    Dřívější výměna těsnění nepomohla, tak jsem na bráchovu radu vyměnil celé kartuše a to asi zabralo.
-   Objevil jsem fotobanku [stockai.com](https://www.stockai.com/) a uložil jsem si ji s tím, že do příštích poznámek dám úvodní obrázek z ní.
    Teď jsem to otevřel a už ten projekt neexistuje 😂
    Že je teď AI velký hype a probíhá v téhle oblasti překotný organický vývoj, to jsem tak nějak tušil, ale že něco zmizí z týdne na týden, to mě překvapilo.
-   Odpovídání v klubu, e-maily, [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), atd.
    Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
    I když toho nebylo v klubu tento týden nějak moc, několik dní po sobě jsem se tam na pár hodin zasekl.
-   Během 8 dní od 3. 2. do 10. 2. jsem při procházkách nachodil 13 km. Celkem jsem se hýbal 7 hodin a zdolal při tom 13 kilometrů.
-   Finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).
    Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/34fa3ec07892dd3ff64458e2ccbf12578e00860483427e9e7c4847bc/)


## Povedlo se

Udělal jsem něco z [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md)?

-   Daří se „Budu se podílet na anketě mezi juniory.“
-   Přiblížil jsem se ke splnění „Vyladím customer journey. Firma musí vědět vše o svém předplatném, v jakém je stavu, kolik čeho zbývá.“
-   Přiblížil jsem se ke splnění „Vyladím customer journey. Já i firma musíme mít včas informaci, že se blíží konec.“
-   Přiblížil jsem se ke splnění „Začneme označovat epizody podcastu, které jsou finančně podpořené spoluprací s firmami.“
-   Přiblížil jsem se ke splnění „Stanu se identifikovanou osobou.“


<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví.**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>


## Plánuji

1.  Pošlu podklady pro daňové přiznání.
2.  Udělám v klubu další fóra.
3.  Dokončit evidenci firem.

**Bonus:** Napíšu na sociální sítě o [PyCon NA](https://na.pycon.org/).
[Jsou úžasní]({filename}2021-06-17_jessica-upani-about-python-events-in-namibia-you-have-to-be-pure-in-terms-of-your-why.md) a chci je podpořit.
Podpořte je taky, lístek stojí zhruba pětistovku.
Ty lidi znám osobně a mohu se za ně stoprocentně zaručit.
Každá koruna jim udělá radost.


## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel toto:

- [Kočárkino a Baby Bio ve vašem kalendáři]({filename}2023-02-09_kocarkino-a-baby-bio-ve-vasem-kalendari.md)<br>Můj víkendový výtvor.
- [(něco na Twitteru)](https://twitter.com/karenxcheng/status/1623055316350029825)<br>Budoucnost vyhledávačů?
- [EU task force cracks down on cookie banners](https://www.simpleanalytics.com/blog/eu-task-force-cracks-down-on-cookie-banners)<br>„…any clever trick to get the user to accept cookies, is probably illegal. If you use web analytics or marketing cookies on your website, you should stick to the indications in the report and offer a transparent and compliant cookie banner. This means making your cookies easy to reject and will likely result in many users rejecting them. There is no way around that.“ 👏
- [Porostou daně? Státu chybí peníze, OSVČ by měli platit víc a důchodový věk se zvýšit, říká ekonom - Prostor X podcast — Prostor X](https://overcast.fm/+Wv2R5NDL0)<br>Dobrý, střízlivý rozhovor. Je příjemné si po slibech a prohlášeních politiků jednou poslechnout někoho, kdo se vládě snaží radit a reálně přemýšlí, jak by šlo problémy vyřešit, se všemi klady a zápory. Jediné, co mě tahalo za uši, bylo převedení peněz z daně z nemovitosti z obcí na stát, ale je možné, že to říkal v kontextu „aby tahle konkrétní daň pomohla řešit strukturální deficit, muselo by se stát tohle“ a ne, že by to navrhoval a myslel si, že je to dobrý nápad.
- [Menu du jour: Queen Mary vyplouvá](https://bigvilik.com/2023/01/29/menu-du-jour-queen-mary-vyplouv/)<br>Ano. Analogie s parníkem skvělá.
- [Chůze v přírodě je cesta do vlastní duše i k druhým lidem. Jak nás léčí procházky a výlety? — Balanc](https://www.mujrozhlas.cz/rapi/view/episode/0ba387f1-2f95-375e-9b60-24f5a10a5381)<br>Když jsem hodně během covidu chodil s kamarádem po parcích a povídali jsme si, nebo potom když jsem chodil s kočárkem, mělo to dobrý vliv. Asi by mi prospělo mít tohohle zase v životě trochu víc.
- [Leden 2023: Jan Romportl o umělé inteligenci](https://newslettery.substack.com/p/leden-2023-jan-romportl-o-umele-inteligenci)<br>Zatím nejpraktičtější věc, kterou jsem o novinkách v AI četl: „Jako byste najednou měli deset rukou místo dvou. Nenechte se přitom ošálit tím, že dosavadní AI nástroje mají svoje limity. Většina z nich časem zmizí.“
- [Neklamu.cz](https://neklamu.cz/)<br>Tohle je super
