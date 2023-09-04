Title: Týdenní poznámky: Python sprint, Mastodon a restart newsletteru
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/280
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/111006913133888025

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-08-18_tydenni-poznamky-sekce-s-novinkami-a-jinja.md) už utekl nějaký ten týden (18. 8. až 1. 9.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [teď plánuji]({filename}2023-08-07_letni-pit-stop.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/3/).
</div>

Píšu po dvou týdnech, tak je to dnes trochu hutnější!
A mimochodem, minule jsem si ani nevšiml, že jsem napsal 550. článek na tento blog.
Tenhle je 551.

## Sleva pro dlouhodobé členy klubu

Rozhodl jsem se, že nebudu řešit tzv. _referrals_, tedy institucionalizované doporučování nových lidí do klubu stávajícími členy.
Původní nápad byl, že by bot každému rozeslal nějaký odkaz, kterým mají posílat nové lidi do klubu.
Tento odkaz by sledoval, kolik kdo poslal lidí do klubu, a dával by jim nějakou slevu.

Jednak by to bylo implementačně obtížné, jednak si vlastně nemyslím, že by to mělo velký efekt.

Memberful [to sice umí](https://memberful.com/help/analytics-and-tracking/track-member-referrals/), takže by se použilo to, ale nejsem si jistý, zda by šlo např. nastavit, aby se započítal jen člověk, který zůstal po _trialu_.

Lidi klub doporučují sami od sebe a rádi.
A já si myslím, že je takové sledování a počítání nakonec spíš otrava.
Když Alice řekne Pepovi, aby přišel do klubu, a on to za půl roku udělá, asi se nebude registrovat přes její odkaz.
Nebo když mu víc lidí klub doporučí, má si mezi nimi vybírat?
Co když někdo klub doporučí ústně?
Prostě je to zanášení nějakého technicistního přístupu do mezilidských vztahů a pestrého, chaotického vzájemného doporučování.

Co mi nakonec i po konzultaci s investorkou (manželkou) dávalo větší smysl, byla paušální sleva všem, kdo jsou v klubu už nějakou delší dobu.
Klub má pro lidi omezenou využitelnost.
Málokdo si nenajde práci např. do roka, mnoho lidí si ji najde i dřív.
V tu chvíli jejich sociální potřeby začne saturovat kolektiv ve firmě a klub pro ně už přestává být tak důležitý, jako dřív.
Pokud se do něj rádi vracejí, je to aby jej podpořili, nebo aby poradili.

Dostávají tedy od klubu menší hodnotu a naopak nějakou přinášejí.
Toto chci reflektovat a to přinášení hodnoty a budování nějakého stálejšího jádra v komunitě chci podporovat.
Spravil jsem tedy jak se počítá „rok v klubu“, protože to byl doteď jen primitivní výpočet:

```
(datum dnešní - datum registrace) / 365
```

Lidem, kteří byli v klubu měsíc před rokem a měsíc teď, to započítalo, že jsou v klubu celý rok.
Teď to sleduje opravdovou dobu, po kterou člověk klub využíval.

Pak jsem si udělal nějaké propočty.
Rozhodl jsem se slevu nabídnout lidem, kteří jsou v klubu déle jak rok.
9 lidí z klubu mělo za členství utraceno v součtu 4.587 Kč (nejvíc).
45 lidí mělo za členství utraceno víc jak 3.000 Kč.
184 lidí bylo v klubu déle než rok, 74 déle než dva, z toho 44 nemělo žádný kupón (stipendium, placeno firmou, apod.).
V moment, kdy jsem slevu spouštěl, by na ni dosáhlo 115 lidí, ale sleva se nabídne těsně před končícím aktuálním členstvím a ti lidé mají různé datum, kdy jim členství vypřší.
Je to tedy dost lidí, ale rozloženo postupně v čase.

Nakonec jsem přidal ještě podmínku, že slevu dostanou jen ti, kdo za poslední půlrok něco málo napsali do klubu.
A stačí fakt málo.
Přijde mi to fér.
Pokud chci podpořit zdravé jádro a to, aby zkušenější lidi pomáhali méně zkušeným, tak tohle nevybuduju na lidech, kteří si klub pouze čtou.
Nemám nic proti pasivnímu využívání klubu a ve všech ostatních případech si vážím pasivních uživatelů klubu stejně jako těch aktivnějších, ale toto je cílená sleva s nějakým záměrem a pasivní čtenář holt k tomu záměru nepřispívá.
Také to odfiltruje lidi, kteří si zaplatili roční členství, ale nakonec jej přestali využívat a jen jim doběhlo.

Co se týče slevy, původně jsem uvažoval až o 50 %, ale to pak vycházelo až nesmyslně levně, takže jsem dal slevu menší, byť stále dost výraznou.
Chtěl jsem, aby to bylo jasné gesto.

Dvěma lidem jsem přes administraci posunul obnovení členství o pár dní, aby stihli nově zavedenou slevu chytit.
Pak jsem naprogramoval mechanismus, který lidem s nárokem na slevu pošle do soukromé zprávy nabídku na slevu dva týdny před prodloužením předplatného.

Memberful umožňuje [hromadně vytvářet unikátní kupóny](https://memberful.com/help/custom-development-and-api/create-coupons-in-bulk-via-api/), ale s tím jsem se nepáral a prostě mají všichni stejný kupón.
Budu to řešit až pokud to bude problém.

K dnešnímu dni ten kupón nikdo nevyužil.
Takže buď mi to nefunguje a lidem se nic neposílá, nebo všichni chtějí junior.guru podpořit a není pro ně taková sleva podstatná.
Pokud tohle čte někdo z členů, kdo dostal soukromou zprávu jako na obrázku níže, napište mi prosím aspoň, že to funguje 😀

![Soukromá zpráva od kuřete]({static}/images/screenshot-2023-09-01-at-16-14-00.png)
Soukromá zpráva od kuřete

## Novinky!

Na webu byla už z předchozích týdnů sekce Novinky, no teď konečně dostala [svou úvodní stránku](https://junior.guru/news/).
Zadání znělo:

> Mít úvodní stránku pro Novinky, kde bude poslední díl podcastu, poslední přednáška, plánovaná přednáška, poslední příběhy juniora a aktuální info, o čem se nejvíc diskutuje v klubu (kanály jako v týdenním souhrnu?)… Tahle úvodní stránka by měla potenciál stát se pravidelným obsahem newsletteru, takže nedělat žádný složitý design.

A tak se i stalo.
Díky vzniku úvodní stránky jsem taky mohl odstranit boční panel, který se sice hodí na příručce, ale tady nedával smysl a nelíbil se mi.
Místo toho jsou tam různé [drobečky](https://en.wikipedia.org/wiki/Breadcrumb_navigation#Websites) a tlačítka.

![Úvodní stránka novinek]({static}/images/screenshot-2023-09-01-at-18-29-44-novinky-pro-zacatecniky-v-programovani.png){: .img-thumbnail }

Nakonec jsem obsah upravil tak, aby tam byla vždy jedna věc nejnovější a jedna je náhodný „tip z archivu“.
To by mohlo pomoci lidem objevovat i klenoty z minulosti.
Algoritmus výběru toho tipu je zatím opravdu náhodný, což má své mouchy, ale to mohu vylepšit později.

Hodně jsem se mazlil s designem a všechno na té stránce jsem tak třikrát změnil, než se mi to začalo aspoň trochu líbit.

Každopádně to plánuji udělat tak, že jednou za dva týdny nebo za týden se jakoby vezme to, co je na téhle úvodní stránce, a pošle se to lidem e-mailem.
A to bude newsletter junior.guru.
Budu se snažit, aby tenhle rozcestník novinek, potažmo newsletter, měl jasnou odpověď na tyto otázky:

-   „Proč by to měl někdo číst nebo odebírat?“
-   „Kde je přidaná hodnota?“

Zatím to neumím úplně dobře zformulovat, ale to je taky tím, že tam ještě nemám vše, co tam chci mít.
Plánuji to vylepšovat postupně a je možné, že to prostě začne na nízké hodnotě „nové věci od junior.guru“ a až časem se to bude zlepšovat třeba k „unikátní výběr toho nejlepšího pro juniory, ze všech různých zdrojů“.

Pro teď mám v zásadě hotovo, co se týče vyšívání na novinkách.
Teď musím počkat, až moje spolupracovnice pošle první hotový rozhovor a ten pak mohu v rámci téhle nové sekce na webu publikovat.

## Python sprint

O víkendu byl letošní [letní sprint Python komunity](https://blog.python.cz/Letni-sprinty-Python-komunity-v-Msenem).
Poslední roky jsem vynechal, protože jsme měli mimino, letos jsem poprvé přijel už ve čtvrtek.
Bylo fajn vidět zase všechny lidi, které znám a mám rád.
Bylo fajn potkat nové lidi.
Na sprintu jsem:

-   Trochu počistil nastavení [@pyvec](https://github.com/pyvec) na GitHubu
-   Dal jsem na [pyvec.org](https://pyvec.org/) odkazy na Mastodon jednotlivých lidí
-   Udělal jsem pořádek ve starých [zápisech ze schůzí výboru](https://docs.pyvec.org/operations/meeting-notes.html)
-   Upgradoval jsem Sphinx na [docs.pyvec.org](https://docs.pyvec.org/)
-   Měli jsme schůzi výboru
-   S Anežkou jsme pročistili [dokumentaci ohledně Twitter účtů](https://docs.pyvec.org/operations/twitter.html)
-   Trochu jsem klukům radil s oživením [blog.python.cz](https://blog.python.cz/) a jeho případným přesunem na [Hashnode](https://hashnode.com/).
-   Chtěl jsem rozbitý [python.cz](https://python.cz/) dostat do stavu, kdy bude fungovat a bude do něj bude schopen přispět i někdo další, ale pak jsem zjistil, že to udělal už tři dny přes sprintem [Petr Viktorin](http://encukou.cz/).
    Jenže jak už nesleduju ten repozitář, tak jsem si toho vůbec nevšiml.
    Nemohli jsme se ale pohnout, protože Hashnode celý víkend nefungovalo tlačítko na upgrade z _free_ tarifu na placený.
-   Předchozí bod mě neodrazil od [robinzonády](https://cs.wikipedia.org/wiki/Robinzon%C3%A1da), které jsem se věnoval celý zbytek sprintu, a to [předělávání python.cz na MkDocs](https://github.com/pyvec/python.cz/pull/559).

Co se týče posledního bodu, překvapilo mě, jak rychle šlo něco tak dobrého vykutit na [MkDocs](https://www.mkdocs.org/).
Když se totiž použil vzhled [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), tak ten si s sebou nese asi tisíc dalších nastavení a udělátek, které stačí nakonfigurovat a ono to PROSTĚ FUNGUJE.
I na mobilu! 😀
Rozpracovaný nový python.cz si lze prohlédnout [zde](https://honzajavorek.github.io/mkdocs-python.cz/).
Bohužel jsem to nestihl do konce sprintu dodělat, takže to teď bude asi čekat, kdy budu mít zase trochu času.

![Rozpracovaný nový python.cz]({static}/images/screenshot-2023-09-01-at-17-38-42-python-v-cr.png){: .img-thumbnail }

Cíle a důvody atd. jsem [popsal v Pull Requestu](https://github.com/pyvec/python.cz/pull/559).
Jde hlavně o to, aby vznikla webovka, kde není _custom_ design, protože Pythonisti nejsou webaři, a kam je schopen přispět úplně kdokoliv, protože obsah je obyčejný Markdown.
Kdyby se to osvědčilo, dovedu si představit stejný princip implementovaný jednou i na [pyvec.org](https://pyvec.org/) nebo [pyladies.cz](https://pyladies.cz/).

## Mastodon

Už jsem neodolal a ze zvědavosti jsem si založil Mastodon.
Moc jsem neřešil provozovatele.
Mám to na [@honzajavorek@mastodonczech.cz](https://mastodonczech.cz/@honzajavorek).

![můj Mastodon]({static}/images/screenshot-2023-09-01-at-18-37-10-mastodonczech.png)

Můj kanál na Telegramu sledovalo 36 lidí.
Řekl jsem si, že když bude můj Mastodon bez jediného příspěvku sledovat taky aspoň 36 sledujících, tak tam začnu něco psát.

Nejpřímočařejší využití by bylo stejné, jako je u toho Telegramového kanálu.
Dával bych tam zajímavé odkazy a články z blogu.
Jestli bych tam dával i něco dalšího, to by se ještě vidělo.

Byť má Telegram svoje API a to API je celkem použitelné (přičemž ani jedno není u dnešních sociálních sítí standardem), přece jen je Mastodon otevřenější platforma a to je mi sympatické.
Taky by [šlo odpovědi integrovat jako komentáře na blog](https://github.com/honzajavorek/honzajavorek.cz/issues/286).
To mi přijde lákavé.

Na Python sprintu jsme založili Mastodon i pro [PyCon CZ](https://floss.social/@pyconcz) a uvidíme, jestli to bude mít nějaký dosah.
Twitter brzy shoří v plamenech a bylo by fajn mít i nějaké jiné místo, kde mohou lidi konferenci sledovat.
Pokud se to osvědčí, možná založíme i něco na další aktivity z české Python komunity, jako alternativu k [našim Twitter účtům](https://docs.pyvec.org/operations/twitter.html).

Taky jsem oslovil členy Pyvce, jestli Mastodon používají.
Do seznamu na [pyvec.org](https://pyvec.org/#members) jsem pak přidal ikonku Mastodonu u těch, kdo účet mají.

Mezitím má můj Telegram 43 sledujících a Mastodon 28, takže je z toho závod 😀

## Meetup zlobí

Hned po tom, co jsem si liboval, jak mám hezky na junior.guru vyřešené to stahování událostí z Meetup.com, a jak to budu moci použít i pro nový python.cz (protože [se to tam rozbilo](https://github.com/pyvec/python.cz/issues/557)), tak to zase přestalo fungovat. To už jsem se fakt naštval!

Bylo zjevné, že o toto se bude potřeba pečlivě starat, jinak se to bude stále rozbíjet.
Aby tedy mohl jednou python.cz využít toho, že díky junior.guru budu mít vždy funkční a opravené řešení, vytáhl jsem toto řešení do samostatné knihovny v rámci juniorguru organizace na GitHubu.

![konverzace s ChatGPT]({static}/images/screenshot-2023-08-30-at-15-13-38.png){: .img-thumbnail }
ChatGPT sice schválilo můj postup, což mě zahřálo na srdíčku, ale moc mi nakonec nepomohlo

Při vymýšlení názvu jsem sice poprosil ChatGPT, ale nakonec jsem si ho vymyslel sám: [teemup](https://github.com/juniorguru/teemup).
Díky [Poetry](https://python-poetry.org/) jsem měl za chvíli funkční balíček.
Využil jsem [doctests](https://docs.pytest.org/how-to/doctest.html), tak jsem zvědav, jak praktické to do budoucna bude.

![teemup]({static}/images/screenshot-2023-09-01-at-17-53-23-juniorguru-teemup-if-meetup-didn-t-become-a-walled-garden-the-world-wouldn-t-need-teemup.png){: .img-thumbnail }

Do README nové knihovny jsem popsal, proč existuje a zaznamenal jsem historii toho, jak se integrace s Meetup.com postupně rozbíjí.

Druhý den se to rozbilo znova, ale jen kvůli tomu, že jsem jeden případ nedomyslel, takže bylo snadné to opravit.
O to horší to bylo ale co se týče publikace nového balíčku.

Já jsem si totiž na [PyPI](https://pypi.org/) nově zapnul 2FA a pak jsem zjistil, že bez nějaké super bezpečné šílenosti zvané _Trusted Publisher Management_ teď nemůžu vůbec publikovat nové balíčky.
Vypnout 2FA už nešlo.
Asi hodinu jsem četl návody, psal YAMLy, vyplňoval formuláře a nadával jsem si, že jsem si to 2FA zapnul.
Nakonec jsem to [nějak rozchodil](https://github.com/juniorguru/teemup/blob/ef27c6b11d964a42357af535c852409bf7b407fc/.github/workflows/release.yml) a balíčky se publikují.
Já jako chápu, že jméno a heslo mělo jistě spoustu bezpečnostních slabin, ale jako _tyvole_!
Kvůli jedné… musíš rozebrat celý traktor.
Verzi 1.0.1 se mi nicméně nakonec povedlo vydat.

## Newsletter

Po sprintu jsem se rozhodl, že by bylo fajn na úvodní stránku Novinek přidat přihlašování k newsletteru.
Že ještě neexistuje?
Nevadí 😀
Za jeden den jsem měl hotové tohle:

![Newsletter]({static}/images/screenshot-2023-08-31-at-13-43-14-novinky-pro-zacatecniky-v-programovani.png){: .img-thumbnail }

Mail se zaznamená v [Ecomailu](https://ecomail.cz/) a to je všechno 😀

-   Budu mít méně stresu, že už bude [PyCon CZ](https://cz.pycon.org/2023/) a já stále ještě nemám newsletter a nesbírám kontakty
-   Že zatím nic nechodí si podle mě stejně nikdo nevšimne
-   Číslo 378 jsem tam napsal natvrdo. Je jich opravdu 378, přenáším starou databázi z MailChimpu, z dob kdy jsem ještě měl původní newsletter. Aby se číslo zjistilo z API Ecomailu dodělám později.
-   Bylo potřeba dodělat _double opt-in_.
-   Bylo potřeba dodělat poděkování, když se někdo přihlásí, protože se nic nezobrazilo a člověk nevěděl, která bije.
-   Ecomail má zdarma tarif na míň kontaktů, než mám já, takže ani žádný newsletter teď poslat nemůžu - to až začnu platit. Ale taky to znamená, že sbírat kontakty můžu hned, i bez toho, abych už platil.

Spousta nedostatků a žádný newsletter vlastně ještě ani není, ale – je to venku! 💪

![Ecomail]({static}/images/screenshot-2023-09-01-at-18-40-36-prehled-ecomail.png){: .img-thumbnail }

Registrace a nastavení Ecomailu bylo jednoduché.
Chvíli jsem hledal, jak přesunout kontakty z MailChimpu, ale nakonec [našel](https://support.ecomail.cz/cs/articles/6419768-prechod-z-platformy-mailchimp).

Ecomail je strašně osvěžující po tom přeplácaném a nepřehledném prostředí v MailChimpu.
Jen jsem se tam přihlásil, abych exportoval kontakty, a měl jsem pocit, že mi jeb…
Když jsem se odhlašoval, připadal jsem si jako že utíkám z nějaké hořící stavby, která se hned po mém odchodu sesune k zemi.
Podobný pocit, jako když jsem opouštěl přeplácané Google Analytics a odcházel k [Simple Analytics](https://www.simpleanalytics.com/?referral=honza-javorek). Nebo z Twitteru na ten Mastodon. Vypadá to, že Ecomail:

-   Je přehlednější a svižnější
-   Má na všechno pěkné návody, i video návody
-   Má jednoduché API, které jsem schopen použít
-   Je česky (stejně jako moje cílovka)
-   Je údajně vyladěný pro české e-mailové schránky (např. Seznam, kde je hodně mojí cílovky)
-   Nesnaží se ze mě vytřískat za každou cenu peníze, naplácat si do e-mailu loga, apod., a má rozumnou cenu
-   Má všechny možné fičury

Ecomail má nějaké svoje vyladěné JavaScriptové formuláře, ale já jsem fanoušek HTML, takže jsem si našel, [jak to udělat čistě přes to](https://support.ecomail.cz/cs/articles/66568-pouziti-a-nastaveni-vlastniho-formulare#h_0877a464c5).
Pak už stačilo jen nastavit, aby po uložení kontaktu uživatele přesměrovali na `junior.guru/news/#email-subscribed` a po ověření kontaktu na `junior.guru/news/#email-confirmed`.

Následně jsem si napsal [svých pár řádků JavaScriptu](https://github.com/honzajavorek/junior.guru/blob/7f0e08ec39df4f45cd1b9a20febb9de642f5b1d9/juniorguru/js/email.js), které pouze zobrazují nebo schovávají kousky formuláře podle toho, co je v adrese stránky.

![Potvrzený e-mail]({static}/images/screenshot-2023-09-01-at-17-20-13-novinky-pro-zacatecniky-v-programovani.png){: .img-thumbnail }

Z API Ecomailu jsem si vytáhl počet odběratelů a přidal k počtům sledujících na různých sítích.
Takže [mám newsletter už i v grafu](https://junior.guru/open/#socialni-site-a-newsletter) a číslo na stránce s odběrem se propisuje podle reálného počtu odběratelů.

Dodělal jsem to dnes, tak budu rád, když to otestujete a dáte mi vědět, jestli to vlastně funguje 😀

## Doktoři

Objížděl jsem opět doktory.
Jedno pondělí jsem v čekárně strávil 3 hodiny.
V ordinaci jsem byl 5 minut, ani ne.
Když připočítám cestu, z domova jsem vyrazil 9:20 a zpět jsem byl 14:50.
Bohužel jsem to nečekal, takže jsem neměl ani pití, ani svačinu, ani počítač, a po dvou hodinách se mi vybil mobil.

Druhá podobná návštěva naštěstí vyšla lépe a v čekárně jsem strávil asi jen půl hodiny.
Měl jsem z toho smíšené pocity, protože jsem to sice vyřešil rychle, ale taky jsem s sebou měl tentokrát pro jistotu úplně všechno, snad kromě stanu a křesadla.
Takže jsem se s tím vším tahal úplně zbytečně.

Celkově se řešení mých problémů táhne a zatím se nikam moc neposouvá.
Dovolené doktorů nebo naše to samozřejmě prodlužují.
Příští týden snad bude další posun.

Nikde jsem záměrně nepsal, co přesně řeším, takže nemusíte prohledávat předchozí poznámky.
Nikde to zmíněno není.
Mám to celý život, teď se to akorát zhoršilo a nikdo si s tím neví tak úplně rady.
S každým dalším týdnem se mi dost zhoršuje kvalita života, ale programovat můžu 😎
Nebudu však zastírat, že je čím dál obtížnější se soustředit i na běžnou agendu.

## Záložník za Tinukiho

Tinuki nahrává přednášky v klubu a ozval se mi, že neví, jestli bude mít od října tolik času.
Začal jsem tedy hledat záložníka, případně náhradníka.
Inzerát zní nějak takto a dával jsem ho zatím jen do klubu:

> Nahrává se přes OBS, ideálně pokud máš nějakou zkušenost s podobným streamováním, ale zase netřeba to hrotit, děláme to spíš punkově. Tinuki by tě zaučil. Časová vytíženost je zhruba 2x2h měsíčně (většinou úterky mezi 17:30 a 19:30). Je to placené jako brigáda. Součástí je samozřejmě zdarma členství v klubu.

Nakonec se mi ozval borec, který dělá streamy pro [Nauč mě IT](https://naucme.it/), a na první pokec to vypadalo dobře.
Záložníka tedy asi máme.
Hned jsem zase o něco klidnější.

## DDoS útok na české banky

Někdo dělá DDoS útok na české banky.
Takže mi samozřejmě padají všechny skripty, které se snaží číst můj bankovní účet (Fio API) nebo třeba kurzy dolaru a eura (ČNB API).
Aspoň jsem to teda předělal, aby to nepadalo na takových věcech (které nejsou na junior.guru zrovna to nejpodstatnější), ale představoval jsem si pátek jinak.
I když…
NÚKIB si asi taky představoval pátek jinak 😀

Díky předchozím změnám se skript, který chodí na Fio, s výpadkem vyrovná celkem snadno.
Historii transakcí si uchávám, takže si akorát nenačte nové.
U směnných kurzů jsem založil [nový YAML v repozitáři](https://github.com/honzajavorek/junior.guru/blob/7f0e08ec39df4f45cd1b9a20febb9de642f5b1d9/juniorguru/data/exhange_rates.yml), kde budou natvrdo a když nebude mít ČNB výpadek, tak se akorát budou automaticky aktualizovat.
Bylo zajímavé cvičení zajistit, aby [strictyaml](https://hitchdev.com/strictyaml/) při zapisování YAMLu dal desetinné číslo (ve skutečnosti [Decimal](https://docs.python.org/3/library/decimal.html)) do uvozovek jako _string_.
I když jsem to možná neměl vůbec řešit a je to jen profesní deformace, protože pro moje účely je úplně jedno, jestli tam bude [_floating point_ chyba](https://en.wikipedia.org/wiki/Floating-point_arithmetic#Accuracy_problems) nebo ne…

## Další

-   Začal jsem v klubu sbírat vzkazy od juniorů pro juniory.
    Chci z toho udělat nástěnku na [PyCon CZ](https://cz.pycon.org/2023/).
    Čas se mi ale nějak krátí!
-   S autorem [JinjaX](https://jinjax.scaletti.dev/) jsem diskutoval o různých věcech a zjistil jsem, že by to asi šlo použít i pro můj _use case_.
    Navíc to vypadá, že [mám v jednom případě nápad](https://github.com/jpsca/jinjax/discussions/18#discussioncomment-6805986), který nedostal ani samotný autor knihovny.
    Třeba mu s tím pomůžu!
-   Logo junior.guru je i s popisem v [seznamu partnerů PyCon CZ](https://cz.pycon.org/2023/sponsors/).
    Juch!
    Dík [Danovi](https://coreskill.tech/), že ho upravil tak, aby mělo i žluté pozadí.
-   Opravil jsem spoustu různých malých chyb, které mi zabraly od pěti minut po celé hodiny času, ale jejichž popisu vás ušetřím.
    Např. [tohle](https://github.com/honzajavorek/czech-political-parties/issues/3).
-   Sháněl jsem dárky pro manželku.
-   DigiKoalice, jejímž jsem členem, spustila „konkurenční“ [seznam kurzů](https://digikoalice.cz/kurzy/) 😀
    Má to trochu jiný záměr atd. a jsem zvědav, jak se jim bude dařit to držet aktuální.
    Napsal jsem jim a pokud by byl způsob, jak jim můžu pomoci, tak jim pomůžu.
-   Investorka (manželka) si koupila lístek na [PyCon CZ](https://cz.pycon.org/2023/) a půjdeme tam spolu.
    Máme tam společné kamarády (angažovala se dřív v [PyLadies](https://pyladies.cz/)) a na konferenci by měl být i nějaký dětský koutek, tak snad se u dcerky zvládneme prostřídat a oba si to užijeme.
-   Objevil jsem [Draw Things](https://drawthings.ai/)!
    Už jsem na to narazil dřív, ale myslel jsem, že je to jen pro telefony.
    Můj iPhone X to přitom nespustí.
    Jenže mi nedošlo, že to můžu nainstalovat i do macOS, když mám Apple Silicon.
    Uživatelské rozhraní je trochu divoké, ale je to asi nejvyladěnější a nejrychlejší způsob, jak generovat obrázky přes Stable Diffusion na macOS.
    Jsem už hodně zvyklý na [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui), je to už takový _industry standard_ všech nadšenců do SD, ale je rozdíl na něco čekat minuty, nebo sekundy.
    Appka má i Discord, kde se toho děje „tak akorát“, což je taky příjemné.
-   [Tvůrcast](http://tvurcast.cz/) měl díl o tom, jak máme podporovat tvůrce, které máme rádi.
    Jak jim máme psát zpětnou vazbu a platit za to, co dělají.
    Tak jsem si Tvůrcast zaplatil, no.
    Nedělám to úplně na denním pořádku, ale 99 Kč za měsíc si rozpočet junior.guru může dovolit a dostanu za to nějaké nové impulzy a komunitu lidí, kteří řeší podobné problémy, jako já.
    Tu jejich komunitu, která je taky na Discordu, jsem začal samozřejmě hned plevelit svými hlubokými myšlenkami 😅
-   Pomáhal jsem kamarádce s přípravou její přednášky na [PyCon CZ](https://cz.pycon.org/2023/program/talks/92/).
    Pak nás napadlo, že bychom udělali i webovku, kde by o ní bylo základní info, a která by jí mohla na konferenci při networkingu pomoci objevit nové příležitosti.
    Ještě ten večer jsem si řekl, že to zkusím vykutit za 15 minut a fakt, [povedlo se](https://github.com/honzajavorek/domicanhelp.cz/).
    To mě dost překvapilo, protože většinou, když si myslím, že něco bude trvat 15 minut, tak mi to zabere dva dny.
    Tohle vyšlo i s registrací domény, změnami DNS a certifikátem na https.
    Taky mě překvapilo, že GitHub Pages umí zobrazit README soubor rovnou jako HTML.
    Už jsem si brousil zuby na [Simple.css](https://simplecss.org/) nebo tak něco, ale pro MVP to nebylo ani potřeba.
    Samozřejmě to není ještě obsahově hotové, tak to zatím nikomu neposílejte.
-   Zarezervovali jsme si dovolenou na druhou polovinu září.
    Tahle bude v ČR.
    Tím se mi snad povede splnit cíl, že budu mít aspoň dvě aspoň týdenní dovolené za rok.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Mailů se mi nahromadilo nějak strašně moc a během sprintu jsem nestíhal číst klub, takže to jsem pak všechno doháněl snad dva dny v kuse.
    Zpracoval jsem jedno stipendium.
-   Koupili jsme konečně dceři postel.
-   Během uplynulých 15 dní jsem se nevěnoval žádné sportovní aktivitě.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Spustit anketu pro juniory.
2.  Dodat PyCon CZ téma diskuze, kterou tam povedu.
    Zpracovat nějak vzkazy od juniorů pro juniory.
    Promovat svůj panel a diskuzi na PyCon CZ.
3.  Aktualizovat stránku pro speakery.
    Sehnat přednášející do klubu na podzim.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Trying To Find Fitness Advice Online](https://www.youtube.com/watch?v=MtQZKyDGXaM)<br>Jak vypadá pokus o to cokoliv zjistit nebo se naučit na dnešním internetu
- [Ekonomický blok BRICS nabídl členství šesti novým zemím. Je to historický krok, řekl čínský prezident - VOXPOT](https://www.voxpot.cz/rychle-zpravy/ekonomicky-blok-brics-nabidl-clenstvi-sesti-novym-zemim-je-to-historicky-krok-rekl-cinsky-prezident/)<br>Tohle bude ještě zajímavé.
- [The World China Is Building](https://www.noemamag.com/the-world-china-is-building/?utm_source=noematwitter&utm_medium=noemasocial)<br>„The capitalist system pursues frontier technologies and profits, but companies like Huawei pursue scalability to the forgotten people of the world. For better or worse, it’s San Francisco or Shenzhen. For many countries in the Global South, the model of development exemplified by Shenzhen seems more plausible and attainable. Nobody thinks they can replicate Silicon Valley, but many seem to think they can replicate Chinese infrastructure-driven middle-class consumerism.“ „If every apartment decorated with IKEA furniture looks the same, prepare for every city in booming Asia to start looking like Shenzhen. If you like clean streets, bullet trains, public safety and fast Wi-Fi, this may not be a bad thing.“
- [Honza Javorek (@honzajavorek@mastodonczech.cz)](https://mastodonczech.cz/@honzajavorek/)<br>Kanál na Telegramu aktuálně sleduje 36 lidí. Na zkoušku jsem si založil Mastodon. Až tam budu mít taky aspoň 36 sledujících, tak tam třeba něco začnu psát 😄
- ["Catching up on the weird world of LLMs" - Simon Willison (North Bay Python 2023)](https://www.youtube.com/watch?v=h8Jth_ijZyY)<br>Super shrnutí všeho kolem AI ve čtyřiceti minutách od Simona Willisona (a když píšu AI, myslím tím konkrétně LLM, jako je ChatGPT apod.)
- [Why we stopped trying to engage passive community members — the 3 circles model.](https://medium.com/together-institute/why-i-stopped-trying-to-engage-passive-community-members-the-3-circles-model-a5144ec8be5b)<br>„It takes a lot of energy to convince a passive person to be active and the results are often short-lived. Force doesn’t work. It doesn’t work in most parts of life, but especially not in non-hierarchical and volunteer-driven environments like communities.“
- [The strange, sad side effect of side hustles](https://www.businessinsider.com/hobbies-death-side-hustles-remote-work-job-market-economic-precarity-2023-7)<br>„A hobby, by definition, is an activity done regularly in one's leisure time for pleasure. But in recent years, expectations have shifted: The fun activities we used to do to fill our spare time should be productive, even profitable.“ Tohle se mi přesně stalo: „One con is that you just don't have hobbies anymore because you've monetized them.“
