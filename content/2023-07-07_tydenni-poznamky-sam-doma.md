Title: Týdenní poznámky: Sám doma
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/238

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-06-30_tydenni-poznamky-smrst-v-klubu-a-programovani-lepsiho-tydenniho-shrnuti.md) už utekl nějaký ten týden (30. 6. až 7. 7.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

Dohodli jsme se, že rodina pojede k babičce a já budu týden kralovat sám doma v Praze.
Jednak se mi nechtělo zase někam jezdit, jednak jsme si takhle všichni od všeho odpočinuli a mohli si nadělit nevšední zážitky, nebo fungovat bez toho, abychom se museli na něčem domlouvat.

Vůbec jsem si nevšiml, že mají být zrovna nějaké svátky, takže mě překvapilo, jak málo lidí bylo v Praze a kolik toho bylo zavřeného.
Nemohl jsem tedy skoro nic zařídit z věcí doma, na které jsem měl zrovna čas.
Nakonec jsem si namíchal nějaký snad rozumný mix povinností, zábavy a práce.
Co jsem dělal ve volném čase?

- Uklizení celého bytu (s podcasty v uších je zábava i mytí záchodu),
- pivo s kamarádem, kterého jsem neviděl tak dekádu,
- návštěva [nejlepšího kina](https://kinoaero.cz/): [Asteroid City](https://www.csfd.cz/film/1069519-asteroid-city/),
- cyklovýlet s kamarádem z Ústí do Mělníka (Středohoří ani Kokořínsko prakticky neznám, takže poprvé),
- druhá návštěva [nejlepšího kina](https://kinoaero.cz/): [„slepá ulička Holywoodských blockbusterů“ naslepo](https://www.csfd.cz/film/18204-kralovstvi-ohne/prehled/),
- cyklovýlet s kamarádem, oklikou k bráchovi na zahradu, následně sběr úrody
- sledování filmu: [Pleasure](https://www.csfd.cz/film/811314-rozkos/prehled/),
- hraní si se Stable Diffusion,
- oběd s kamarádkou s miminem,
- sledování F1 v Rakousku.

Včera jsem nasedl na vlak a už jsme zase celá rodinka pohromadě.

![Aero]({static}/images/img-4418.jpg)
Aero

![Úštěk]({static}/images/img-4380.jpg)
Úštěk

![Kokořín]({static}/images/img-4395.jpg)
Kokořín

## IRL srazy v klubu

Povedlo se mi nakonec hacknout meetup.com.
Kód, který se tam přihlašoval a stahoval iCalendar, jsem musel smazat, protože nefungoval na CI.
Meetup.com zdetekoval, že se přihlašuji z nějaké podezřelé IP adresy a poslal mi na mail 2FA kód, který jsem měl zadat, což znemožnilo jednoduchou automatizaci.

Napadlo mě však, že i _walled garden_ potřebuje být na Googlu a že možná na webu používají mikroformáty ze [schema.org](https://schema.org/).
A taky že jo.
Pustil jsem na jejich HTML [extruct](https://github.com/scrapinghub/extruct/) a bylo to, měl jsem veškerá data o plánovaných událostech.
Stačilo to jen nějak sloučit s iCalendar exportem z [pyvo.cz](https://pyvo.cz/) a zpracovat.

Během pár hodin už jsem pro každý budoucí sraz zakládal událost na Discordu.
Nakreslil jsem k nim i obrázky.
Bot by je mohl přímo generovat, ale řekl jsem si, že rychlejší bude, když ručně udělám tři obrázky pro tři typy srazů.
Namastil jsem to v [Canva](http://canva.com/).

Při programování jsem narazil na nějaké nesrovnalosti v pycordu, tak jsem založil [#2160](https://github.com/Pycord-Development/pycord/issues/2160) a [#2161](https://github.com/Pycord-Development/pycord/issues/2161).
Dokonce se mi po několika dnech ozvali i ze supportu meetup.com, že mi rádi pomohou, ale vůbec netuší, která bije, tak jestli jim můžu nahrát video.
K tomu jsem se ještě nedostal, ale udělám to.
Pokud je to bug a oni vůbec nevědí, že jim několik měsíců nefungují iCalendar exporty, tak to by mě dost pobavilo.

![Události na Discordu]({static}/images/screenshot-2023-07-07-at-12-39-43.png)
Dovedu si představit, že by se to dalo dál vylepšovat, ale pro začátek to bude takhle stačit

## Optimalizace buildu webu

Jedna z nejpomalejších věcí při buildu webu bylo generování [stránky s grafy](https://junior.guru/open/), protože se tam dělá spousta dotazů do databáze a spousta výpočtů.
Napadlo mě, že bych to mohl přesunout do synchronizační fáze, tzn. že by se to jednou předpočítalo, uložilo do databáze a při buildu webu už by se to jen vypsalo.
To urychlí především lokální vývoj, kdy každou chvilku reloaduji web.

No tak jsem to takhle udělal.
Chvíli mi trvalo to správně navrhnout, ale myslím, že výsledek je i flexibilnější a přehlednější, než jak to bylo předtím.

Přidal jsem i nový graf, [podíl žen mezi hosty podcastu](https://junior.guru/open/#podil-zen-mezi-hosty-podcastu) (45-55 %, hezký!).

## Obnova ztracených statistik

Nedávno jsem si omylem na Memberful smazal nějaká stará data a připravil jsem se tím o historii spousty produktových grafů, které se týkají členství.
To je dost průšvih.
V Memberful API je ještě něco, co se jmenuje _activity log_, tak jsem si myslel, že bych některá čísla mohl obnovit z toho.

Jenže v API je toho méně, než co jde vidět v _activity logu_ na webu v Memberful.
Zjistím asi jen příchody a odchody lidí, ale už ne co měli za tarif nebo za kupón, bohužel.

Takže je otázka, jestli se mi bude chtít programovat nějakou netriviální záležitost jen kvůli polovině grafů.
A ještě bych musel vymyslet, jak ta čísla spojit dohromady s tím, co mám za poslední měsíce.
Udělal jsem _proof of concept_, ale nejsem si jistý, co dál, jestli to vlastně dotáhnu.

Stažení dat do databáze bylo celkem jednoduché, ale pak jsem je potřeboval nějak normalizovat, aby tam nebyly duplicity.
Vůbec jsem nevěděl jak na to, ale ChatGPT mi to celé vymyslelo!
Můj dotaz zněl takhle:

> I have a database table with column "user_id" typed as number, "happening_on" typed as date, and column "activity_type", which can have only two values: begin, end.
>
> The data represents activity log. It can happen that some actions in the system result in multiple activities of the same type happening one after another. Example:
>
> user_id: 1, happening_on: 01-07-2022, activity_type: begin
> user_id: 1, happening_on: 04-07-2022, activity_type: end
> user_id: 1, happening_on: 10-07-2022, activity_type: end
> user_id: 1, happening_on: 11-07-2022, activity_type: end
> user_id: 1, happening_on: 12-07-2022, activity_type: begin
> user_id: 1, happening_on: 12-07-2022, activity_type: begin
> user_id: 1, happening_on: 13-07-2022, activity_type: begin
>
> What would you suggest me to do with the data so that I normalize the records and get rid of duplicate activites? Let's say I'd want to keep always only the first one of the same type happening for each user:
>
> user_id: 1, happening_on: 01-07-2022, activity_type: begin
> user_id: 1, happening_on: 04-07-2022, activity_type: end
> user_id: 1, happening_on: 12-07-2022, activity_type: begin

Vyplivlo to SQL, které používalo nějaké poddotazy a věci, které ani neumím používat.
Tak jsem se rovnou zeptal, jestli mi to nemůže napsat v syntaxi Peewee.
A chtěl jsem to bez nějaké další tabulky, tak mi to zase přepsal.
A nakonec jsme se dobrali ke kódu, který po překopírování prakticky hned fungoval.

```python
subquery = (
    ActivityLog
    .select(
        ActivityLog.id,
        fn.ROW_NUMBER().over(
            partition_by=[ActivityLog.user_id, ActivityLog.activity_type],
            order_by=[ActivityLog.happening_on]
        ).alias('row_num')
    )
    .from_(ActivityLog)
    .cte('subquery')
)

duplicate_ids = (
    ActivityLog
    .select(subquery.c.id)
    .from_(subquery)
    .where(subquery.c.row_num > 1)
)

ActivityLog.delete().where(ActivityLog.id.in_(duplicate_ids)).execute()
```

Když si to čtu, tak tuším, co se tam děje a proč to funguje, ale v životě bych takovou šílenost sám nenapsal, ani v SQL, natož v Peewee.
Ušetřilo mi to hromadu práce.
Pokud to teda funguje!
Musím si na to ještě napsat testy.

## Optimalizace obrázků

Noční CI workflow, které formátuje kód a pushuje zpátky na GitHub, jsem přejmenoval z `format` na `tidyup` a doplnil jej o další věci.
Teď to umí zmenšit avatary na 500x500 px, pokud jsou větší, a optimalizovat trochu jejich JPG kompresi.
A taky to umí optimalizovat SVG.
Tyto věci se tedy dějí jednou za den a změny se commitnou zpět do gitu, takže na to sám nemusím nijak zvlášť myslet.

Generované obrázky (plakátky k podcastu, přednáškám…) se nově přenášejí z buildu na build přes CircleCI cache.
To znamená, že stejný obrázek se nebude generovat znova a znova a šetří se čas.
Ale taky to znamená, že starý, nepotřebný obrázek, by tam zůstal navěky.
Tak jsem doplnil věc, která sleduje, které generované obrázky jsou opravdu potřeba a staré nepotřebné smaže.

Tímto jsem prozatím ukončil svoje přebudovávání toho, jak na junior.guru funguje build frontendu.
Zabralo to víc času, než jsem myslel, ale s výsledkem jsem celkem spokojen.
Vyřešil jsem spoustu malých otravných problémů a celé jsem to dost zrychlil, což by mělo i podpořit mou chuť na frontendu něco dělat.

## Další

-   Vyšly se mnou [Newslettery.cz](https://www.newslettery.cz/p/cerven-2023)!
-   Doladil jsem slučování dat na CI, které se dělá po paralelizaci skriptů.
    Došlo mi, že nechci slučovat soubory se staženými nabídkami práce, protože pokud už se ten den stáhly, tak se vůbec nemají stahovat znova.
    Velmi to zjednodušilo kód, spoustu věcí jsem smazal.
-   Dal jsem si záležet, abych byl tentokrát ve správný čas na správném místě, ale stejně se nám nepovedlo jako výbor Pyvce sejít.
    Začínám to vnímat jako větší a větší problém, tohle musíme nějak vyřešit.
-   Udělal jsem upgrade na [nový Bootstrap](https://blog.getbootstrap.com/2023/05/30/bootstrap-5-3-0/), který umí _dark mode_.
    Akorát na junior.guru teda ještě _dark mode_ nebude, to budu muset celé ještě prozkoumat, přečíst si [Michálka](https://www.vzhurudolu.cz/prirucka/dark-mode), atd.
-   Pročistil jsem si jeden sloupec v Trellu a vyházel kartičky, které jsou už nerelevantní, nebo hotové.
-   Předělal jsem na Discordu kanál na hádanky a šifry z textového na forum.
    [Míla](https://milavotradovec.cz/) ho chce propojit s [Šifrovačkami](https://sifrovacky.cz/).
-   Call s ENGETO Academy. Kecali jsme nějak dlouho, tak jsme si dali ještě druhý na příští týden.
    Odpadla nám kamarádka na dotazník a my asi vzdáme to, aby to viděl nějaký odborník.
    Už teď na tom děláme někdy od listopadu a furt to není venku, přitom jak já, tak ENGETO preferujeme spíš způsob „zkusit, poučit se, zkusit znova“ a ne něco rok ladit.
-   ENGETO bude hledat seniorního vývojáře, tak jsem jim mrknul na inzerát.
    Měl jsem k tomu spoustu připomínek a komentářů, tak snad jsem to moc nerozcupoval na kousky.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
-   Během 8 dní jsem ujel na kole 143 km. Celkem jsem se hýbal 18 h a zdolal při tom 143 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Pod každou stránkou příručky bude „komentářová sekce“, ve skutečnosti reklama na klub.
2.  Dělat promo věcem, kterým mám dělat promo.
3.  Rozhodnout se co s těmi ztracenými metrikami na [/open/](https://junior.guru/open/).

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Your People](https://randsinrepose.com/archives/your-people/)<br>Proč se vyplatí mít „svoje lidi“? Zajímavý postřeh od Randse.
- [edu.digital - 7 důvodů, proč státní IT nefunguje (záznam)](https://www.youtube.com/watch?v=PhS2qoEOjJk)<br>Super vhled od Jakuba Onderky do toho, proč nefunguje IT ve státní správě. Je to delší, ale pustil jsem si to k vaření oběda a šlo to. Akorát to trochu zkazilo chuť 😅
- [Červen 2023: Honza Javorek o placené komunitě](https://www.newslettery.cz/p/cerven-2023)<br>:)
