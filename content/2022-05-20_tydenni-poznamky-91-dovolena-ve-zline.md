Title: Týdenní poznámky #91: Dovolená ve Zlíně
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl zase nějaký ten týden (14.5. — 20.5.) a tak [stejně jako minule]({filename}2022-05-13_tydenni-poznamky-90-zmeny-v-mentoringu-a-stream-na-youtube.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Něco jako dovolená

Tento týden jsme strávili ve Zlíně u babičky. Na dítě jsme tedy byli tři, když započítám kočku tak čtyři. Hned to byla mnohem větší pohoda, dovolím si tvrdit že pro všechny. Díky tomu jsem měl i čas chodit dost běhat, prakticky jsem se šel téměř denně provětrat na 10 km. Natáhli jsme internet na terasu a už teď se těším, až se tam vypravíme zase. Teď už jedeme vlakem zpátky do Prahy.

Sice to nebyla dovolená v pravém slova smyslu, přes týden jsem vlastně normálně pracoval. Tempo života bylo ale takové pomalejší a hlavně člověk neměl na očích starosti z místa, kde žije. Nemusel do detailů řešit naplňování ledničky, nemusel přemýšlet nad úklidem, nad odklízením krabic z parapetu, které tam jsou už věčnost, apod. Prostě mentální dovolená na baba hotelu. Jak jsem teď někde četl, [dovolená je hlavně stav mysli](https://a2larm.cz/2021/09/dovolena-je-zmena-stavu-mysli-nezalezi-kde-jste-rika-fotografka-ktera-se-rekreovala-na-sidlisti-dablice/).


## Vylepšování mentoringu

Jal jsem se vylepšovat, jak funguje mentoring v klubu. Seznam mentorů v jedné zprávě se mi nakonec moc nelíbil, tak jsem založil kanál jen pro čtení, kde bot vytváří zvlášť zprávu pro každého mentora. Díky tomu mohou mít i obrázek. Taky jsem se naučil jak přidat ke zprávě tlačítka, na která jde klikat. Ty jsem použil pro odkazy k rezervaci termínu konzultace v kalendáři mentora.

![Mentoring kanál]({static}/images/mentoring-kanal.png)

Bot je schopný přidávat mentory, pokud se objeví v YAMLu, nebo mazat, pokud z YAMLu zmizí. Nakonec vždy dává zprávu, která vysvětluje, jak mentoring funguje. Pokud někdo nový přijde do klubu a rozklikne si tento kanál, uvidí tuto zprávu, protože je v kanálu jako poslední. Na mentory si potom doscrolluje nahoru do historie. Bot se stará o to, aby návod na fungování mentoringu byl vždy poslední zpráva, i kdyby přidával nové mentory.

![Mentoring info zpráva]({static}/images/mentoring-info.png)

K tomu jsem přidal novou pravidelnou zprávu do kanálu #parťáci a do #poradna. Jednou za měsíc se v parťácích připomene, že si tam lidi mohou hledat kámoše na společný projekt nebo společné učení a že mi mají napsat, pokud vytvoří skupinu a chtějí k tomu třeba privátní kanál na domlouvání. A je tam „reklama“ na to, že existuje #mentoring.

![Zpráva v kanálu #parťáci]({static}/images/partaci-info.png)

Do #poradna se zase jednou týdně napíše info o tom, jak to tam zhruba funguje a jak na Discordu najít tlačítko pro založení nového vlákna s otázkou. Zakládání vláken jsem následně vynutil oprávněními.

![Zpráva v kanálu #poradna]({static}/images/poradna-info.png)

Formulace budu časem ještě ladit. Taky bych chtěl přidat na web stránku o mentoringu a o tom, jak se správně ptát, kde se bude možné více rozepsat. Tyto pak chci odkazovat z oněch pravidelných zpráv.


## Zálohovací prográmek na iCloud

Chtěl bych si zálohovat fotky a další věci na iCloud. Jenže ne pomocí Apple Photos, ale jako soubory. To zní jednoduše, prostě je dám na počítači do iCloud složky, že? Jenže toho mám nějaký ten terabajt. Chtěl jsem něco, co by soubory na iCloud prostě jednorázově nahrálo a ony tam byly jakoby z jiného zařízení. Můj macOS by se pak mohl rozhodnout, jestli tyto soubory chce, nebo nechce stahovat na disk.

Myslel jsem si, že něco takového není možné vyrobit, ale nedávno jsem narazil na knihovnu [pyicloud](https://github.com/picklepete/pyicloud), která to překvapivě umožňuje. Když jsem tedy měl o víkendu nějakou tu chvilku, mrknul jsem na to. Už dřív jsem si na 10 řádků napsal prototyp, který nahrál jeden soubor na iCloud, abych ověřil, zda to fakt funguje. Teď jsem začal vytvářet „seriózní“ prográmek, který vezme složku na mém disku, cestu na iCloudu a z jednoho místa soubory nahraje do druhého.

Narazil jsem při tom na chyby v té knihovně, což mě dost zdrželo, jelikož jsem nikdy nevěděl, zda nedělám něco špatně já a snažil se věc debugovat. Ale byla to chyba v kódu. Knihovna nevypadá moc udržovaná, takže řešení je vždy v issues nebo v Pull Requestu, který nikdy nikdo nezamergoval. Nejdřív [tohle](https://github.com/picklepete/pyicloud/issues/326#issuecomment-1126925582=), pak [toto](https://github.com/picklepete/pyicloud/issues/337). Opravy šlo naštěstí udělat pomocí _monkey patchingu_ a nemusel jsem knihovnu třeba forknout.

Dostal jsem se do fáze, že prográmek umí nahrát pár souborů na iCloud. Kdo ví, kdy se k tomu zase někdy dostanu a dodělám to. Zatím to nemám ani na GitHubu, je to jen kus kódu na disku.


## Další poznámky

- Udělil jsem jedno stipendium na roční členství v klubu.
- Odložili jsme na neurčito klubovou přednášku o frontendu, která měla být příští týden. Převážně kvůli covidu, který skolil speakera.
- Poslouchal jsem [nový díl našeho podcastu](https://junior.guru/podcast/), který vyšel s Tatankou. Byla to sranda, je to dobrý vypravěč.
- Předělal jsem týdenní souhrn v klubu tak, aby nepoužíval v Discord embedu označování lidí, což se pak nezobrazuje úplně dobře v Discord klientech. Vypisuju tam teď proste jen _display name_. Tady to vůbec nevadí, protože z embedu lidem stejně nechodí notifikace a klikatelné to tam být nemusí.
- Šárka z [ProgramHRování](https://www.programhrovani.cz/) mě poprosila, zda bych ji nepropojil s pár lidmi, většinou v souvislosti s organizací PyCon CZ. Propojil jsem.
- Nová česká komunita pro dokumentaristy a _tech writers_, [TWguild.cz](https://www.twguild.cz/), měla organizační online call, ale nezvládl jsem tam dorazit. Spolupráci jsme ale o krůček posunuli, dal jsem jim přístup do klubu a na [klubovou stránku](https://junior.guru/club/) jsem přidal jejich logo.
- S [Aj ty v IT](https://ajtyvit.sk/) jsme se bavili o tom, že bych mohl mít na webu i slovenské nabídky práce. K tomu ale potřebuju scrapnout profesia.sk (to mi měly dohodnout) a umět třídit slovensky psané inzeráty. S tím by mělo pomoci ML, které chceme s kamarádem Mílou do bota zavést už dlouho. Udělal jsem tedy [hrubý plán](https://github.com/honzajavorek/junior.guru/issues/862) toho, jak by to mohlo probíhat.
- StartupJobs přidali vyjímku pro JG do své ochrany proti robotům. Díky tomu zase funguje stahování log firem pro jejich inzeráty, takže na [inzerátech](https://junior.guru/jobs/) je teď o dost méně prázdných rámečků.
- Domlouval jsem se s [robime.it](https://robime.it/) a [WebExpo](https://www.webexpo.net/), zda si můžeme nějak pomoci.
- Domyslel jsem spolupráci s Engetem a napsal jsem jim.
- Zjistil jsem, že role v klubu „Mám #ahoj a profilovku“ (která má členy motivovat k představování a k tomu, aby si nahráli nějaký obrázek a šli od sebe odlišit) nefunguje správně. Jak jsem před časem optimalizoval stahování avatarů, tak se teď dávala jen lidem, pro které byly avatary stažené, takže asi jen 30 lidem z klubu. Všiml jsem si toho a opravil jsem to.
- Dva lidi z Pure Storage neměli správnou firemní roli. Jeden jsem zjistil, že má vstup už od dřív díky tomu, že mě podporuje na GitHubu. Debugováním druhého jsem přišel na nějaký prapodivný bug v tom, jak zpracovávám data z Memberful. Zabralo mi dost času vymyslet, co mám vlastně dělat v případě, že má jeden uživatel víc _subscriptions_. Vymýšlel jsem různé složitosti, ale nakonec jsem to smazal a udělal opravu na jeden řádek.
- Sociální sítě jsem zanedbával a nic jsem na ně nedal.
- Klub, maily, a tak dále.
- Během 7 dní od 14.5. do 20.5. jsem naběhal 47 km, při procházkách nachodil 9 km, ujel na kole 9 km. Celkem jsem se hýbal 9 hodin a zdolal při tom 65 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Vylepšovat mentoring,
2. zamyslet se nad novým ceníkem s tou 15% inflací a drahým plynem,
3. zvládnout pár byznysových schůzek v kavárně.

**Bonus č. 1:** Užít si [Žižkovské mezidvorky](https://www.facebook.com/events/756977309009547/).

**Bonus č. 2:** Všem říct, aby pro [náš podcast](https://junior.guru/podcast/) hlasovali v [téhle anketě](https://www.podcastroku.cz/#hlasov%C3%A1n%C3%AD).


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [The 2022 Market Crash - Why is Everything Down?](https://www.youtube.com/watch?v=ddWr9dPGqDA)<br>Co se děje s trhy?
- [Bořiči dezinformací. Dáváme lidem argumenty proti nesmyslům, vysvětlují autoři projektu Ověřovna](https://www.mujrozhlas.cz/rapi/view/episode/0e1bf90d-12bb-3df9-95c8-3c738d170960)<br>Super.
- [The Premium Mediocre Life of Maya Millennial](https://www.ribbonfarm.com/2017/08/17/the-premium-mediocre-life-of-maya-millennial/)<br>Tohle je nejlepší analýza městských mileniálů, kterou jsem kdy četl. Hodně meta, ale těch myšlenek, co tam řežou do živýho!
- [Vážil jsem se čtyřikrát za noc. Moderátor Čestmír Strakatý přiznává souboj se svým tělem](https://www.mujrozhlas.cz/rapi/view/episode/b78d8bac-074c-3ce4-b97e-aebcd6841ddd)<br>Zaposlouchal jsem se do této podcastové série a rozjezd hodně dobrý.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
