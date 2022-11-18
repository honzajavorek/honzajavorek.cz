Title: Týdenní poznámky: Nový ceník, menu, vizitky
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky
Twitter-Comments: https://twitter.com/honzajavorek/status/1281659042285457409
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158285679227707


Utekl další týden (6.7. — 10.7.) a tak [stejně jako minule]({filename}2020-07-03_tydenni-poznamky-rymicka-a-menu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Nový ceník

Věnoval jsem se opět uzavření obchodu s velkou firmou. Jak jsem psal minule, bylo potřeba doladit ještě způsob, jakým předplatné funguje. Nakonec to vyústilo v jeden celý den kompletního překopávání toho, jak mi funguje ceník, a jeden další den kompletního překopávání stránky s ceníkem :D Ach jo. Ale myslím, že je to teď celé [jednodušší a srozumitelnější](https://junior.guru/hire-juniors/). Změny jsou založeny na následujících postřezích:

- Pro robota, který bude ze stránek velkých firem stahovat jejich juniorní nabídky, není trh. Nikdo nebude inzerovat tolik juniorních nabídek, aby něco takového potřeboval.
- Firmy nechtějí inzerci a logo dohromady, jen ty největší. Většina firem má zájem buď o inzerci, nebo o logo.
- Pryč s cenami jako 290, 5990, apod. Bavme se narovinu, používejme hezká čísla, která si na nic nehrají a každý si je může hned hezky spočítat v hlavě. Efekt cen končících na devítky se možná přeceňuje, zkusím to teď bez nich.
- Jednoduché počty.
- Inzerce na JG musí být levná, abych posbíral opravdu všechny nabídky na trhu a nikdo neřešil, jestli se mu to vyplatí. To bude teď moje strategie. Nová cena je za pětikilo, to je [o polovinu méně, než nejlevnější inzerce na StartupJobs](https://www.startupjobs.cz/pro-firmy). Pětikilo bez větších problémů zaplatí i fyzická osoba.
- Nově je roční paušál pro větší firmy jako samostatný tarif, který není nutně dohromady s logem na příručce. Sice se vyplatí až od 10 inzerátů (včetně prodlužování), ale zase není tak drahý, aby si jej firmy nepořídily prostě jen proto, aby nemuseli řešit žádné další faktury na drobné.
- Logo na příručce na měsíc nikdo nechce a dává to smysl. Nejkratší doba je teď 3 měsíce.
- Cena za logo na 3 měsíce je pod psychologickou hranicí 10 000 Kč.
- Když už jsem se před nedávnem naučil dělat odkazy na Google Forms tak, aby byla nějaká políčka předvyplněná, udělal jsem teď tlačítka v ceníku tak, aby po kliknutí měl formulář už přímo předvyplněný odpovídající tarif.

Také jsem na stránku pro firmy přidal důraz na to, že JG je pro firmy i řešení pro diverzitu jejich týmu. Nechtěl jsem ovšem použít žádná slova, která dnes v lidech vzbuzují emoce, jako diverzita, inkluze, apod. Zároveň jsem chtěl, aby management velkých firem z textu hned pochopil, o co jde, a s D&I si to spojil. Bylo to velké hraní se slovíčky, no nakonec jsem vyplodil toto:

> Aktuálně je v Českém IT [pouze 9,9 % žen](https://www.ceskovdatech.cz/clanek/128-neni-ajtak-jako-ajtak/), což je méně než v Turecku. To znamená, že **pokud se omezíte jen na hledání zkušenějších programátorů, rozmanitost svého týmu neposílíte**. Díky tomu, jak je junior.guru tvořeno a s jakými komunitami od svého počátku spolupracuje, oslovuje pestrou škálu lidí, včetně mnoha žen programátorek.

Další drobné změny:

-   Loga na jsem předělal v CSS do BEM komponenty a vylepšil způsob, jakým se zobrazují na mobilu.
-   Čísla (počet návštěvníků atd.) jsem udělal větším fontem, protože si jich všímalo málo lidí :D Teď jsou obří. Jestli to pomůže, nevím.
-   Zkusil jsem skrýt delší pasáže pomocí tlačítka "Zobrazit víc". Je to takový experiment. Sice tím při úvodním načtení zmizela loga komunit, jsou schovaná, ale zase je stránka kompaktnější a rozšířené informace se zobrazí opravdu jen těm, kteří mají zájem něco takového číst. No uvidím, třeba je to úplná blbost.

Když už jsem byl u všech těch změn, přečetl jsem si znova i starší e-mail s postřehy od [Honzy Horny](https://web2-0.cz/), který mi radil jak vylepšit na stránce pro firmy UX a texty, a zkusil něco z toho zapracovat. Díky!


## isort a pyflakes

[isort](https://github.com/timothycrosley/isort/) vydal novou verzi, která je určitě strašně super (aspoň podle oznámení a changelogu), ale mě pár věcí rozbila, a já se rozhodl, že nemám náladu to řešit a nástroj jsem z projektu odebral. Řazení importů je teď prostě zcela zbytná věc, nemá smysl aby mi jakkoliv žrala čas, a neměl jsem ji v první řadě do projektu v tak brzké fázi vůbec přidávat.

Když už jsem u toho ale byl, rozhodl jsem se, že se mrknu na to, jestli by nemělo smysl přidat nějaký linter. Ze stejného důvodu, jako jsem neměl přidávat isort, jsem nechtěl přidávat nic, co mi v kódu hlídá styl jeho psaní, nebo nic, co kód formátuje a zdržuje mě od commitování. V Pythonu se však hodí mít něco, co ve statické analýze odchytá alespoň zjevné chyby. Po základní rešerši jsem zjistil, že [pyflakes](https://github.com/PyCQA/pyflakes) je přesně to, co hledám:

> Pyflakes analyzes programs and detects various errors. Pyflakes makes a simple promise: it will never complain about style, and it will try very, very hard to never emit false positives.

Bohužel jsem zjistil, že pyflakes [nemá přímou podporu ve VS Code](https://github.com/microsoft/vscode-python/issues/9315) (WTF? lintery jsou tam hardcoded?). Řešení bylo ale jednoduché - prostě jsem použil [flake8](https://gitlab.com/pycqa/flake8), který pyflakes obaluje, a [nastavil jej](https://github.com/microsoft/vscode-python/issues/9315#issuecomment-629831988) tak, aby nic jiného než pyflakes nereportoval.

Následně jsem opravil všechny chyby, které to zahlásilo. Většina byla _unused import_, ale našlo to i dvě poměrně závažné chyby. Jedna z nich dokonce něco, co by se velmi brzy projevilo a poslalo zákazníkům e-mailem, takže dost dobrý. Hlavní problém byl v tom, že jsem občas omylem rozkopíroval testy, ale nezměnil jejich název:

```python
def test_verify_a():
    a = 42
    assert a == 1

def test_verify_a():
    b = 2
    assert b == 2
```

Tenhle kód projde, protože druhá funkce se jmenuje stejně jako první a přepíše ji. První se nikdy nepustí a pytestu to nijak nevadí. Měl jsem tedy několik testů, které jsem myslel, že se pouští a procházejí, ale nebylo tomu tak a kód nefungoval správně.

**Poučení:** Na formátování kódu kašlat, zvlášť když na projektu nedělá nikdo jiný než já. Ať už jde o kontrolu stylu nebo jeho vynucení přes věci jako [isort](https://github.com/timothycrosley/isort/) nebo [black](https://github.com/psf/black), je to v začátku prostě zbytečná práce navíc. To ale neplatí pro věci, které hlídají opravdové chyby. [pyflakes](https://github.com/PyCQA/pyflakes) jsem měl mít v projektu od prvního dne!


## Menu a nový proužek pod ním

Pokračoval jsem ve vylepšování menu. Chci jej obohatit o osnovu/obsah aktuální stránky a nějakou vnitřní navigaci v rámci jedné stránky. Zatím to mám rozmyšlené jen v hrubých rysech a postupuji po malých krocích.

Už od minulého týdne vršek stránky na JG zůstává přilepený při scrollování. Teď jsem to upravil tak, aby byl na mobilu přilepený jen když se scrolluje nahoru, a zmizel, když se scrolluje dolů, aby měli lidi víc místa na displeji pro čtení.

Hned potom jsem se vrhnul na to, aby se pod menu na obsahových stránkách zobrazoval ještě jeden proužek, kde budu tvořit tu osnovu. Jako první úkol jsem si dal, že proužek bude taky přilepený při scrollování, a že bude zobrazovat nadpis aktuálního odstavce. Zabralo mi to většinu pátečního odpoledne a dost jsem se u toho zapotil. Nejhorší bylo nějak nakombinovat střídavé přilepování a mizení žluté hlavičky, zatímco pod ní je přilepený bílý proužek, který nemizí nikdy. No naučil jsem se zase v CSS hromadu věcí a nakonec jsem to vytvořil - prototyp můžete vidět živě třeba na [stránce se základy programování](https://junior.guru/learn/).

Příští týden chci proužek vylepšovat a rozšiřovat. Až budu mít lepší řešení pro interaktivní osnovu, budu zase o krok blíž vydání příručky.


## Další poznámky

-   Přidal jsem do [seznamu podporovatelů](https://junior.guru/donate/#sponsors) [Tomáše Votrubu](https://tomasvotruba.com/) s odkazem na jeho [Rector](https://github.com/rectorphp/rector). Juchů!
-   Celebrita, kterou jsem oslovil (viz minule), mě poslala k šípku, protože trpí tím samým, čím trpím i já - má už spoustu projektů rozjetých a chce nejdříve dokončit ty, než bude začínat další.
-   Minulý týden jsem odeslal newsletter, ale nezaznamenal jsem si u odeslaných nabídek práce do databáze, že byly odeslány. Napadlo mě, že bych si na to mohl napsat skript, ale zatím jsem si z toho udělal jen kartičku do Trella a dál to neřešil.
-   Už jsem se nemohl dívat na to, jak mi Google Sheets zobrazují data v americkém formátu, tedy M/D/YYYY. Bylo to strašně matoucí. Změnil jsem to na ISO, ale tím se změnily i hodnoty, které stahuje z Google Sheets [gspread](https://github.com/burnash/gspread) a tudíž jsem musel upravit i aplikaci, aby jiný formát zvládala.
-   Ladil jsem drobnosti ve vzhledu nového menu. Třeba jsem ho zarovnal doprava, tak jak jste mi poradili v komentářích pod minulými poznámkami.
-   Zákazník odepsal na automatický e-mail a požádal o upravení inzerátu. Je fajn, jak s těmi e-maily je to teď takové osobnější a komunikace je najednou obousměrná. Inzeráty nejsou jen řádky v databázi, ale jsou za nimi reální lidé v reálných firmách, se kterými si mohu psát.
-   Od jednoho zákazníka jsem dostal za úkol, abych na JG přivedl víc lidí z Brna. Momentálně je 40 % návštěvnosti z Prahy a 15 % z Brna, to je pro ně málo. Kdybyste měli nějaké tipy jak to udělat, dejte vědět :D Já něco v záloze mám, ale rád nasbírám další inspiraci.
-   Napsal jsem na [Romea](http://www.romea.cz/) a na [DigiKoalici](https://digikoalice.cz/), jestli by mi nedokázali radit s tím, jak mezi juniory dostat více Romů a jestli na to jsou vůbec nějaká čísla, jaká je vůbec situace, atd. Nemám zatím žádný konkrétní plán ani záměr, chci jen zjistit situaci.
-   Doteď jsem při každé změně při vývoji musel čekat vždy skoro deset dlouhých sekund, než se přes [Frozen-Flask](https://github.com/Frozen-Flask/Frozen-Flask/) vygenerovala celá statická stránka. Nechci totiž vyvíjet nad Flaskem, ale opravdu nad výsledkem, který to nakonec vytvoří na produkci. Bylo to celé strašně pomalé a i s nějakým livereloadem, který tam mám, byl takhle vývoj fakt strašný zážitek. Myslel jsem, že je to problém i toho livereloadu (proto jsem se [ptal na Twitteru](https://twitter.com/honzajavorek/status/1281518073678311424)), ale nakonec se mi rozsvítilo a svůj obří `Gulpfile.js` jsem upravil tak, že statické soubory se při vývoji neprotahují přes Flask, prostě se jen překopírují. Frozen-Flask se tedy dostane ke slovu jen při změně HTML nebo Python kódu. Neuvěříte - najednou se změny v CSS nebo JS projevují naprosto okamžitě. Já se asi zblázním. Půl roku jsem JG programoval tak, že jeden reload trval deset sekund a stačila tato malá změna, aby polovina změn byla okamžitá.
-   Zjistil jsem, že v CSS existuje [:target](https://developer.mozilla.org/en-US/docs/Web/CSS/:target).
-   Zůčastnil jsem se setkání Prague Professional Community organizované [Jeanne Trojan](https://twitter.com/jmtcz/) a rozdal tam své první, čerstvě vytištěné vizitky!

![Návrh na vizitky]({static}/images/vizitka-navrh.jpg)
Návrh vizitek, který jsem posílal do [PrintAll](http://www.printall.cz/)

![Vizitky]({static}/images/vizitka.jpg)
Výsledek


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [KOMENTÁŘ: Proč české děti nesnáší češtinu aneb na prahu druhého obrození](https://www.idnes.cz/zpravy/domaci/cesky-jazyk-cestina-vzdelavani-deti-zaci-ucitele.A200630_202921_domaci_aug)<br>Perfektní filipika proti klasické výuce češtiny
- [Tim O’Reilly makes a persuasive case for why venture capital is starting to do more harm than good](https://techcrunch.com/2020/06/26/tim-oreilly-makes-a-persuasive-case-for-why-venture-capital-is-starting-to-do-more-harm-than-good/)<br>Tim O’Reilly o investování
- [Koronalekce z Karviné: Nestíháme, tak promořujeme?](https://www.respekt.cz/rozhovor/koronalekce-z-karvine-nestihame-tak-promorujeme)<br>Česko se rozhodlo, že koronavirus už je prostě pryč — všechna opatření opadla a nemoc se šíří dál
- [How Western media would cover Minneapolis if it happened in another country](https://www.washingtonpost.com/opinions/2020/05/29/how-western-media-would-cover-minneapolis-if-it-happened-another-country/)<br>Jak by vypadaly současné zprávy o USA, kdyby nešlo o USA
- [Atlantropa](https://en.wikipedia.org/wiki/Atlantropa)<br>Věděli jste o plánech na přehrazení Giblartaru a vytvoření Atlantropy?
- [Principles and priorities](https://adactio.com/journal/16811)<br>“User experience, even over developer experience.”
- [The Wrong Abstraction — Sandi Metz](https://www.sandimetz.com/blog/2016/1/20/the-wrong-abstraction)<br>“Prefer duplication over the wrong abstraction” aneb vakcína na vir s názvem DRY

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
