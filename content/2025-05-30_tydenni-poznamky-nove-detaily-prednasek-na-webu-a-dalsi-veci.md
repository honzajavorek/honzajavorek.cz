Title: Týdenní poznámky: Nové detaily přednášek na webu a další věci
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/351
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/114598557052312158

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-05-23_tydenni-poznamky-vylepsovani-prezentace-klubovych-akci-na-webu.md) už utekl nějaký ten týden (23. 5. až 30. 5.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

## Odstranění Flasku a profiling MkDocs

V pondělí jsem zapnul dev server junior.guru a vyblilo to na mě milion warningů a trvalo to asi 15 sekund. Nebylo to nic nového. Do tohoto stavu se to dostalo postupnými změnami, upgrady knihoven, a dalším technickým dluhem.

Tak jsem se neubránil a šel jsem to už řešit. Kdysi byla webovka junior.guru postavená na Frozen-Flask, pak jsem přešel na MkDocs. Jenže jsem přecházel postupně a stále tam zbývalo pár stránek, které jely na Flasku a ve starém designu. Tak jsem se rozhodl, že to už konečně vyřeším.

Nejvíc práce daly stránky s výpisem inzerátů pro jednotlivé lokace. Třeba [Brno](https://junior.guru/jobs/brno/) a tak. Nová verze výpisu inzerátů jede v JavaScriptu a vystačila by si bez takových stránek, ale je to důležité kvůli SEO. Tak jsem to nějak vymyslel, zrealizoval, pak jsem desetkrát rozbil ten JavaScript, pak jsem ladil design, a tak.

Dále jsem musel přesunout 404ku. Dále manuálně zadané nabídky práce. No bylo toho hodně. Moc jsem se s tím nemazal, hlavně aby to bylo na MkDocs, ne aby to bylo krásné. Pak jsem odstranil Flask ze závislostí, z build procesu, a vůbec ze všech koutů kódu. Taky jsem mohl odstranit staré generování og:image pro Flaskové stránky, což bylo asi 100 řádků kódu.

Pak jsem šel optimalizovat ty MkDocs, protože i ty trvaly dlouho. Zjistil jsem, že plugin na navigaci se přejmenoval na `mkdocs-awesome-nav` a má úplně novou verzi. Tak jsem to celé zmigroval a spousta warningů zmizela. Nakonec jsem to dotáhl tak daleko, že mám `strict: true` v `mkdocs.yml`, a to je co říct.

Pomocí ChatGPT jsem napsal profiling skript. Výstupu jsem nerozuměl, ale ChatGPT ano, takže se mi díky tomu povedlo optimalizovat pár věcí. A taky to odhalilo, že je v buildu někde schovaný HTTP požadavek, který to celé zdržuje. Detektivně jsem na to nakonec přišel, na vině bylo jedno API, které vystavuju pro jednu firmu, které jsem před časem narychlo spíchnul, a neuvědomil si, že se to bude spouštět při každém buildu a zdržovat ho. Tak jsem to přesunul do jiné fáze generování webovek a najednou jsem se z 10s dostal na 4s a bylo to. Sám bych to ale nedokázal, nebo by mi to trvalo týden.

No ještě pořád se to nějak loudá, vedle MkDocs tam mám ještě esbuild se statickými soubory a ten trvá taky nějak podezřele dlouho. Ale to jsem si nechal už na jindy.

## Stahování log firem pro inzeráty

Ani potom jsem se ale nedostal k webovkám pro přednášky. Týden v kuse mě totiž zlobilo stahování log firem pro pracovní inzeráty a už bylo fakt nutné to opravit. Debugováním, ani logováním jsem na nic nepřišel, ale stejně jsem to chtěl už dlouho celé přepsat a přehodit jako scraper na Apify, tak jsem se do toho pustil.

Teď se v mém buildu na CI akorát sesbírají odkazy na obrázky a případně na webovky firmy, pošle se to do scrapery na Apify, ten to postahuje a případně identifikuje favicony apod., a vrátí obrázky zpět. Potřeboval jsem nějak vrátit binární data obrázku, tak jsem se naučil s Apify Key-Value Store. Pořád musím obrázky stáhnout HTTP požadavkem, ale z API od Apify a ne přímo z cílových webů, což je mnohem robustnější. A vypadá to, že to funguje.

Musel jsem ale předělat dost i algoritmus na výběr vhodného obrázku a tak, no přehazoval jsem vidlema dost kódu z kupky na kupku. A nakonec generování „písmenkových“ náhradních obrázků pro inzeráty, kde logo chybí. Tam to zlobilo a nevěděl jsem proč. Ale při přepisování jsem si všiml, že se tam hodněkrát něco potenciálně složitého zbytečně znova a znova načítá, tak jsem to předělal, aby se to kešovalo, a od té doby problém nebyl 🤷‍♂️ Nevím, dál. Funguje to teď pěkně, a to je důležité.

## Nové detaily přednášek na webu

Až ve středu jsem se dostal k přednáškám, takže jsem si pustil techno a jel jak drak, abych měl tento týden uděláno i něco, co jsem původně udělat chtěl. Zaznamenával jsem to postupně [na Mastodonu](https://mastodonczech.cz/@honzajavorek/114590162775357792):

- Dal jsem na [výpis přednášek](https://junior.guru/events/) tlačítka na přidání do kalendáře.
- Na podstránce akce jsem vymyslel, jak odprezentovat záznamy a popral jsem se i s tím, když má akce záznamy dva (celý pro členy a sestřih pro veřejnost).
- Nadesignoval jsem všechny nejrůznější stavy podstránky s akcí, ať už to bylo to, že jde o budoucí akci, klubovou, veřejnou…
- Čas a datum jsem dal mnohem větším písmem, dal jsem tam jasné _call to action_ na záznam nebo na připojení se.
- Sepsal jsem tam krátký návod, jak se lze na přednášku vůbec dostat.
- Přidal jsem _call to action_ na klub.
- Dolů jsem dal „Mohlo by tě zajímat“, kde je kolotoč s jinými přednáškami. Algoritmus výběru je sofistikovaný, tzv. _random_. Ale vlastně je to trochu složitější, protože jsem chtěl, aby tam vždy byla příští přednáška, která teprve bude, pokud taková je, a taky se tam nesmí vypsat ta samá přednáška, na kterou se člověk zrovna dívá.
- Doladil jsem vzhled rámečku se speakerem a přidal tam „bio links“, které mají i ikonky podle platformy, na kterou míří, a vyparsuje se i username. Takže se místo `https://www.linkedin.com/in/m%C3%ADla-votradovec-2a659920/` zobrazí **in/míla-votradovec-2a659920** s ikonkou LinkedInu.
- Dal jsem tam tlačítko na stažení plakátku k přednášce. To potřebuju hlavně já nebo Táňa, ale proč by nemohl pomoci přednášku propagovat i někdo jiný, že?

Hodně jsem to ladil a postupně měnil. Jako vedlejší efekt jsem na webu udělal spoustu drobných vylepšení a designových úprav, které tady nemá ani smysl psát.

Taky mi lidi psali, že odkaz na přidání do Google Kalendáře nefunguje, takže to jsem taky dost řešil, jak to opravit. Každopádně to byl problém na straně Googlu, ne můj a nepřišel jsem na to, jestli je to jen jejich nekompetence, nebo enshittification Google Kalendáře. Každopádně obejít to šlo jen tak, že jsem svůj perfektně interoperabilní a funkční iCalendar feed musel obalit jako „veřejný Google Kalendář“ v jejich ekosystému a lidem dát odkaz na přidání toho. Pragmaticky jsem to udělal, ale v duchu jim posílám prostředníček.

![Seznam přednášek - hlavička]({static}/images/screenshot-2025-05-30-at-15-01-27-online-akce-pro-zacatecniky-v-programovani.png){: .img-thumbnail }
Seznam přednášek (hlavička)

![Seznam přednášek]({static}/images/screenshot-2025-05-30-at-15-01-38-online-akce-pro-zacatecniky-v-programovani.png){: .img-thumbnail }
Seznam přednášek

![Detail přednášky]({static}/images/screenshot-2025-05-30-at-15-02-24-daniel-srb-jak-na-cv-pri-zmene-kariery-do-it-online-akce-na-discordu-junior-guru.png){: .img-thumbnail }
Detail přednášky

![Připravovaná přednáška]({static}/images/screenshot-2025-05-30-at-21-37-14-eva-pavlikova-jak-rozjet-svou-it-karieru-ve-statni-sprave-online-akce-na-discordu-junior-guru.png){: .img-thumbnail }
Připravovaná přednáška

![Speaker]({static}/images/screenshot-2025-05-30-at-21-37-32-petr-glaser-jak-pouzivat-ai-asistenty-a-odnest-si-z-nich-maximum-online-akce-na-discordu-junior-guru.png){: .img-thumbnail }
Speaker

![Záznam]({static}/images/screenshot-2025-05-30-at-21-37-54-tomas-ervin-dombrovsky-situace-na-it-trhu-z-pohledu-dat-a-co-to-znamena-pro-juniory-online-akce-na-discordu-junior-guru.png){: .img-thumbnail }
Záznam

![Kolotoč]({static}/images/screenshot-2025-05-30-at-21-38-16-mila-votradovec-proc-maji-programatori-radi-sifrovaci-hry-a-proc-by-mohly-bavit-i-vas-online-akce-na-discordu-junior-guru.png){: .img-thumbnail }
Kolotoč

![Dva záznamy]({static}/images/screenshot-2025-05-30-at-21-38-32-nela-slezakova-jak-se-jako-ajtak-cka-zbavit-pochyb-a-pocitu-ze-nejsem-dost-online-akce-na-discordu-junior-guru.png){: .img-thumbnail }
Dva záznamy

## Další

-   O víkendu jsem se podíval na [pyvec/docs.pyvec.org#439](https://github.com/pyvec/docs.pyvec.org/pull/439) a [pyvec/docs.pyvec.org#439](https://github.com/pyvec/docs.pyvec.org/pull/439), ale ještě na tom bude nějaká práce.
-   Řešil jsem něco kolem výuky angličtiny v klubu, která na čas ustala, protože lektorka je teď v Japonsku.
-   Byl jsem s dcerou u kamarádů v Černošicích poslechnout si jazz na jezu a bylo to fajn.
-   Sháněl jsem účastníky na [Beginners' Day Unconference](https://mastodonczech.cz/@honzajavorek/114558198633271824), kterou organizujeme v rámci EuroPythonu.
-   Jedna firma mi napsala, že pokračovat ve sponzorství nebude. Druhá firma mi napsala, že pokračovat ve sponzorství bude. Poslal jsem fakturu.
-   Byl jsem na své první dětské narozeninové oslavě v životě. Postupně si přes školku děláme nové (dospělé) kamarády a je to fajn.
-   Na nedělní odpoledne jsem naplánoval chlubící status na LinkedIn o tom, jak jsem překopal ten web pro přednášky.
-   Kamarád mi poslal Saru Landry a je super. Třeba [tady](https://www.youtube.com/watch?v=VDgaKWRuhRU) nebo [tady](https://www.youtube.com/watch?v=LrJtjGPNHPE). Její track ADHD, kde předělala Rimskij-Korsakova, je slušnej nářez 😅
-   Dcera jela se školkou na výlet.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Zkouším novou taktiku. Administrativní úkony a e-maily celý týden prokrastinuju a pak je všechny udělám v pátek, s větou „díky za trpělivost“ hned za pozdravem. Zatím vidím jen výhody. Za ten týden se to nasbírá a je jasnější, co je důležité, nebo co spěchá, a co ne. Taky mi odpovědi nechodí hned, protože v pátek už nikdo nepracuje. Možná někdo odpoví „hned“ v pondělí, ale i to je až po 2-3 dnech, čímž se automaticky nastavuje roztáhlejší tempo.
-   Za 8 dní jsem naběhal 3 km. Celkem jsem se hýbal 1 h a zdolal při tom 3 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Ještě je potřeba dodělat pár drobností na těch přednáškách, ale neměl bych na tom už vyšívat moc dlouho.
2.  Napíšu návod pro seniory - jak mohou v klubu pomáhat, jak se mohou zapojit.
3.  Zkusím promyslet MVP junior.guru newsletteru. [Buttondown](https://buttondown.com/) mám vyhlídnutý jako platformu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Cestující rozdělujeme na dva typy. Autoři nového designu českých nádraží vysvětlují změny písma i piktogramů - Zdopravy.cz](https://zdopravy.cz/cestujici-rozdelujeme-na-dva-typy-autori-noveho-designu-ceskych-nadrazi-vysvetluji-zmeny-pisma-i-piktogramu-246660/)<br>Budou nové cedulky na nádražích!
- [(bez titulku)](https://pavlinaspeaks.substack.com/p/ahoj-vol86-cringe?/&r=2epvcf)<br>„Vždycky budeš zpětně trapná. Jen v jedné z těch variant jsi z toho měla radost.“
- [Coloro na Instagramu](https://www.instagram.com/p/DJEza47tgUL/)<br>Color of the Year 2027 bude Luminous Blue! Velmi blízko modré barvě, která se používá na junior.guru. Náhoda? Nemyslím si! 😀
- [Culted na Instagramu](https://www.instagram.com/p/DGDTc0UNXUt/)<br>Děcka znovuobjevujou focení na šířku, super 😀
- [Duševní zdraví a hraní. Počítačové hry vás mohou s dětmi sblížit i ublížit — Balanc](https://www.mujrozhlas.cz/rapi/view/episode/e1e9a8c1-9775-32fc-957d-d61efa8c174c)<br>Pěkný pokec o tom, jaký efekt mohou mít hry a jak s tím jako rodič pracovat
- [Pocket is saying goodbye - What you need to know | Pocket Help](https://support.mozilla.org/en-US/kb/future-of-pocket)<br>Byla jen otázka času, kdy se to stane. Už před lety to nemělo žádné nové fičury, neopravovalo žádné bugy, přišlo mi to v kómatu na přístrojích. Takže jsem přešel jinam. A teď Pocket končí.
- [Peter Hanecak (@phanecak@mastodon.social)](https://mastodon.social/@phanecak/114552785464573897)<br>„Slovenka porazila aj mužov, v Himalájach vyhrala jeden z najťažších triatlonov na svete. Dokázala to ako prvá žena v histórii. Trénuje v Bratislave popri práci a hovorí, že nie je vrcholová športovkyňa. V Nepále však dosiahla prelomový úspech.“
