Title: Týdenní poznámky #88: Pyvec a nová stránka do příručky
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (23.4. — 29.4.) a tak [stejně jako minule]({filename}/2022-04-22_tydenni-poznamky-87-stipendium-clanek-prednasky.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Nová stránka na příručce

S [Nelou Slezákovou](https://www.nelaprovazi.cz/) připravujeme novou stránku do [příručky](https://junior.guru/handbook/), která bude o duševním zdraví. Měli jsme už připravený nějaký základní text, tento týden jsem jej vysázel do příručky už přímo do HTML, tedy spíš do Markdownu.

Tato nová stránka bude prototypem spolupráce JG s nějakým nezávislým profesionálem. Takovou spolupráci jsem měl už déle v hlavě a tady byla hezká příležitost to zkusit. Jsem (snad) schopen udržovat jádro příručky sám, ale byla by škoda se omezit jen na to, čemu rozumím já. Chtěl bych tam mít stránky psané a „garantované“ i jinými odborníky, které znám a kterým věřím, výměnou za to, že tam bude odkaz na něco, čím se zabývají. Není to bez práce, stále tam figuruji jako nějaký editor, ale aspoň nemusím dělat velkou rešerši nějakého tématu a mohu se opřít o expertízu někoho dalšího a už to společně „jen“ napsat.

Takže ve spolupráci s Nelou píšeme tuto novou stránku a ona tam bude mít odkaz na sebe. Juniorům to pomůže, jí to pomůže, mě to pomůže. Win win win. Teď je to ve fázi že nám tam pár drobností ještě chybí v obsahu i designu. Obsah doplní Nela, já bych měl v CSS vymyslet, jak bude vypadat ten zvýrazněný odkaz na ni, aby bylo zřejmé, že to je nějaká spolupráce.


## Generování obrázků pro podcasty

Obrázky pro propagaci jednotlivých dílů podcastů jsem doteď „kreslil ručně“, tedy vždy splácal dohromady z nějakých obdélníčků v programu Keynote a exportoval jako PNG. Teď jsem to chtěl už automatizovat, protože to vypadá, že podcast bude chvíli ještě existovat :)

Obrázky využiju při ruční propagaci. Mohu je použít i přímo v podcastovém feedu a budou se zobrazovat na jednotlivých platformách. Taky jsem chtěl naučit bota, aby díly oznamoval přímo v klubu a tam se opět bude obrázek hodit.

### Fotky účastníků podcastu

Potřeboval jsem vyřešit dvě věci. První byla přidávání fotek účastníků podcastu. Pavlína vždy do YAMLu jen poslala přes Pull Request detaily k novému dílu, zbytek jsem zajistil já. Teď tam bude nová položka, cesta k fotce hosta. Tu nebude muset vyplňovat, fotku zajistím já, ale bude potřeba ji mít v tom YAMLu, načíst, atd. Na podobné fotky jsem už měl složku k přednáškám, pro které se taky generují náhledy. Přišlo mi zbytečné mít složku pro každou takovou věc, zvlášť když se kryjí někteří speakeři s hosty v podcastu. Tedy jsem to trochu překopal. Taky jsem u přednášek změnil YAML tak, aby se musela cesta k fotce všude explicitně napsat a už to není vázáno na nějaké Discord ID jako předtím, bylo to zbytečné a omezující provázání.

Teď mám tedy jednu složku s fotkami všech takových lidí a odkazuje na ni jak YAML pro přednášky, tak YAML pro podcast. Napsal jsem si kontroly, jestli mají fotky očekávaný tvar a velikost, aby skripty spadly, pokud nemají. To je nedokonalá ochrana (asi by to měl být spíš nějaký git hook) hlavně proti tomu, abych si necommitnul do Gitu omylem několikamegabytovou fotku, protože to by pak zůstalo v historii navěky.

Přidal jsem i separátní skript, kterým mohu nové fotky doplňovat. Zeptá se mě na cestu k souboru a jméno člověka a postará se o zbytek. Nakopíruje fotku do příslušného adresáře, ověří že jde o čtverec, zmenší, správně pojmenuje.

### SCSS v šablonách pro obrázky

Další věcí bylo sjednocení CSS tak, abych v těchto obrázcích generovaných z HTML šablon mohl používat vše, co i na webu. Donutil mě k tomu barevný pás tlačítek na různé podcastové aplikace, který jsem měl na původním „ručním“ plakátku. Ten jsem tam původně vlepil jako screenshot z webu, ale teď jsem to chtěl mít hezky v HTML, s tím stejným CSS jako na webu. Abych mohl použít totéž CSS, musel bych mít v šablonách nějak přístupný Bootstrap a celé svoje SCSS a nějak by se muselo přegenerovávat na čisté CSS při tom, jak se obrázek renderuje. Tomu jsem se dlouho bránil, ale reálně jsem na to narážel už ve víc případech, jelikož pokud se snažím dodržovat nějaký podobný vizuální jazyk na plakátkách jako na webu, prostě pak musím sdílet minimálně nějaké SCSS proměnné a tak.

Přesunul jsem tedy SCSS o několik složek výš, aby nebylo jen pro web, ale pro libovolný kód v rámci JG, stejně jako jsem to už dřív udělal s obrázky. Pak jsem do kód, který generuje obrázky, přidal nějaké srandy, které jsou schopny si poradit i s tím SCSS. Bylo to celé jednodušší, než jsem čekal a navenek se ani nic moc nezměnilo, jen jsem pak přejmenoval .css soubory na .scss a vše stále fungovalo, ale s většími možnostmi. Staré plakáty jsem nijak nemigroval, nový už jsem napsal tak, že vychází z Bootstrapu a mého dalšího SCSS, takže jsem tam mohl snadno použít barvy, tlačítka apod. stejně jako když styluju web.

### Co dál?

V pondělí jsem nově generovaný plakát rovnou použil při propagaci. Dál by bylo dobré naučit bota propagovat nové díly v klubu za mě a taky bych mohl plakátky přidat do XML podcastu, aby se objevovaly v podcastových aplikacích k jednotlivým dílům. S Pavlínou jsme se ještě bavili o vzhledu toho plakátu a máme nějaké nápady jak ho vylepšit, ale to se dá zase ladit klidně až v budoucnu.

## Práce pro Pyvec

Po volbách do výboru Pyvce je nyní potřeba udělat spoustu věcí, tak jsem se tomu trochu věnoval. Dali jsme si společný call starý a nový výbor. Tam si nový výbor zvolil předsedkyni a pokladníka.

Taky jsem upgradoval knihovny v Pyvec repozitářích přes dependabot, ale tak to dělám každý týden, asi nemá smysl to tu ani pořád psát. Následně jsem dával lidem přístupy do různých míst a oznamoval změny na Pyvec Slacku na různých místech (GitHub, Slack…). Inicioval jsem, aby se výbor poprvé sešel na pravidelné měsíční schůzi a vybíráme teď termín. Přihlásil jsem se dobrovolně k tomu, že kontaktuji právničku, aby nám udělala papíry k volbám a zanesla změny do rejstříku.

Přišla nám hned nová žádost o členství ve spolku, tak až se sejdeme, můžeme se hned procvičit v hlasování.


## Další poznámky

- Začal se mi na CI dost projevovat [tento problém s poetry](https://github.com/python-poetry/poetry/issues/3336). Chvíli jsem to trpěl, ale teď už mě to přestalo bavit a obešel jsem to přes workaround zmíněný v tom issue, vypnul jsem něco, čemu říkají „new installer“.
- Volal jsem si s Engetem a vymýšleli jsme, jak můžeme spolupracovat na další rok. Byl z toho dlouhý call a je z toho spousta nápadů, které musím ještě promyslet.
- Poslaly se mi v pondělí dvakrát maily inzerentům. Zjistil jsem, že jsem měl celou dobu v CircleCI nastavenou špatnou cestu k souboru, který řídil cache, která zabraňovala opakovanému odeslání. Bohužel chybějící soubor, který by se měl kešovat, není důvodem k failnutí jobu, takže jsem to doteď nezjistil. Opravil jsem to a maily se poslaly potřetí. Protože byl stejný klíč pro cache, takže CircleCI novou cache neuložilo a nepřepsalo ono „nic“ z minula :D Počtvrté už se to povedlo správně a nic se už neposlalo, uf.
- Opravil jsem si Stylelint ve VS Code, aby fungoval.
- Domlouval jsem se s lidmi, jestli a kdy se někdy potkáme.
- Vymýšleli jsme se StartupJobs, jak můžeme nějak víc spolupracovat, hlavně na obsahu jejich vzdělávací sekce.
- Připomínal jsem se firmám, ať už s prodlužováním členství v klubu, nebo s dalšími kroky v naplňování závazků, které jsme si domluvili. S Pure Storage chceme rozjet nabídku mentoringu v klubu, ale stále ladíme detaily.
- Domluvil jsem dvě až tři další přednášky do klubu. Juchů! Hned jsem si je nahodil do svého YAMLu a tentokrát jsem ani nečekal, až budou všechny detaily a napsal tam u všeho prostě jen „bude upřesněno“ a [nechal to, ať se to zobrazí](https://junior.guru/events/). Což ale způsobilo, že se vytvořily už i eventy na Discordu a klikají se na ně lidi. Nepamatuju si už ale, zda bot umí u těch eventů i aktualizovat popis, když se v budoucnu změní, tak snad jo, jinak to budu muset pak nějak editovat ručně, nebo nechat jak to je, se vším tím „bude upřesněno“ :D
- Ověřil jsem, že se námi podporovaný kluk se stipendiem dostal do všech služeb a všechny přístupy mu fungují.
- Vyšel mi (zatím) poslední článek na Heroine: [Jak jsem se stal ambasadorem začátečníků v IT. Zakladatel junior.guru o výhodách komunity a sdílení](https://www.heroine.cz/zeny-it/8100-jak-jsem-se-stal-ambasadorem-zacatecniku-v-it-zakladatel-junior-guru-o-vyhodach-komunity-a-sdileni)
- Propagoval jsem [nový díl JG podcastu s Terezou z ReactGirls](https://junior.guru/podcast/). Propagoval jsem prodloužené partnerství s [Lynt](https://lynt.cz/).
- Opravil jsem zase několik „rozbitých“ odkazů na webu, které nejsou ve skutečnosti rozbité, a [zanadával jsem si o tom na Twitteru](https://twitter.com/honzajavorek/status/1518864988991102976).
- Tento týden se nakupila spousta mailů a další administrativy. Snažím se to omezovat na dva dny v týdnu, ale jde to těžko. Aktuálně mám například v inboxu 7 méně důležitých emailů, ke kterým se nejsem schopen dostat už několik měsíců a už tam vidím jeden další, kterému se to asi stane taky, protože obsahuje nekonečně mnoho textu a nelze z toho ani zjistit, co ten člověk vlastně chce.
- Prošel jsem několikrát klub a odpovídal lidem, ale popravdě jsem to tento týden trochu zanedbával, nestíhal jsem.
- Během 7 dní od 23.4. do 29.4. jsem při procházkách nachodil 15 km. Celkem jsem se hýbal 6 hodin a zdolal při tom 15 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Naučit bota v klubu díly podcastu oznamovat za mě a přidat obrázky dílů do XML,
2. zkusit streamování na YouTube,
3. nastylovat odkaz na Nelu na nové stránce do příručky.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Vlevo dole](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BahZjVt9Z0&h=29a6f90aac668a55d7e04855d2725f34a3411eb2fe2fd80b4b59acdb4afd4ab6)<br>Kam se poděli Piráti?
- [Web scraping is legal, US appeals court reaffirms](https://getpocket.com/redirect?&url=https%3A%2F%2Ftechcrunch.com%2F2022%2F04%2F18%2Fweb-scraping-legal-court%2F&h=5af35d1fe077ba8d6d4711c8c0bd4e3df4fb36a00baf2d3f873f190f1d2559b0)<br>Scrapování je prý legální.
- [Vladimir 518: Praha ještě zazáří. Je třeba stavět, ale také pečovat o ikonické stavby z minulosti](https://getpocket.com/redirect?&url=https%3A%2F%2Fovercast.fm%2F%2BVf9THCkSA&h=e264023b98432a491b2cc175d62511e0680ee063ac0a30883653f319cb58987d)<br>Rozhovor o architektuře a Praze, líbilo se mi to.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
