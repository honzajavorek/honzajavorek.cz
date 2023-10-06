Title: Týdenní poznámky: Tipy pro nováčky v klubu, v2
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-09-29_tydenni-poznamky-nova-homepage-pycon-cz-dovolena-a-unava.md) už utekl nějaký ten týden (29. 9. až 6. 10.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [teď plánuji]({filename}2023-08-07_letni-pit-stop.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/3/).
</div>

Tento týden jsem se pustil do překopávání tipů pro nováčky v klubu.
MVP je v podobě dvou kanálů.

Jeden bude typu „fórum“ a budou v něm samotné tipy.
Toto fórum bude přístupné všem v klubu.
Budou do něj moci přidávat i svoje tipy, ale některé tipy bude spravovat bot na základě Markdownových souborů u mě v repozitáři a budou zvýrazněné a propagované jako „oficiální“ tipy.

Pak bude privátní kanál pro všechny nováčky, kam bude bot tipy postupně sdílet.
Zda mít takový jednotný kanál nebo dělat „kohorty“ („běhy“) nováčků podle toho, kdy přišli, je otázka, kterou si odpovím až v budoucnu - viz [diskuze na Mastodonu](https://mastodonczech.cz/@honzajavorek/111175595060968806).
Jednotný kanál je jednodušší na výrobu, tak s ním začnu.

## Tvorba „fóra“ s tipy

Zkoumal jsem, zda lze přes Discord bota vytvořit nové téma na „fóru“ a dát mu obrázek.
To jde.
Na čem jsem se pak ale zasekl bylo zjišťování, zda lze ten obrázek v budoucnu změnit.
To mi nešlo.
Pak jsem ze [zeptal](https://github.com/Pycord-Development/pycord/discussions/2236).
Pak jsem to ještě všelijak zkoušel.
A nakonec se mi to povedlo, tak jsem si zase [sám odpověděl](https://github.com/Pycord-Development/pycord/discussions/2236#discussioncomment-7175997).
A řešení jsem [zdokumentoval i do míst](https://github.com/discord/discord-api-docs/issues/936#issuecomment-1745017848), která jsem předtím náhodou vygooglil.

Nakonec jsem si ale uvědomil, že než bych ke každému tipu vyrobil nějaký pěkný obrázek, tak budou Vánoce, takže bude jednodušší začít ty tipy dělat bez obrázků 😀 Takže jsem

- vytvořil fórum,
- přepsal staré tipy do Markdownu,
- vyrobil skript, který je speciálním způsobem načte a připraví,
- napsal kód, který je do fóra přidá, pokud tam ještě nejsou, a upraví, pokud tam už jsou.

## Další

-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Tento týden toho bylo zase nějak hodně, především v klubu.
    Pátek ale uzavírám s tím, že mám skoro _inbox zero_ v e-mailu a v klubu mám všechno přečtené a vyřešené, včetně docela pracných odpovědí a kariérních rad, které jsem dlouho odsouval.
-   Spadl mi bot, protože název vlákna na Discordu může být jen do 100 znaků, ale Pyvo, které bude zanedlouho v Praze, se jmenuje „Pražské Pyvo #149 Engineering Of Structured, Semi-Structured And Unstructured Data & Language Models and the Non-English Languages“.
    Když jsem to opravoval, smazal jsem omylem další srazy z Discordu, takže peklíčko!
    Ale snad už opraveno.
-   Naprogramoval jsem si věc, která mi pošle report, pokud bot někomu [nabídne slevu]({filename}2023-09-01_tydenni-poznamky-python-sprint-mastodon-a-restart-newsletteru.md).
-   Přišly mi dva maily od dvou různých PR agentur s nabídkou hostů do [podcastu](https://junior.guru/podcast/).
    Poslal jsem je na ceník:
    > Hezký den, díky za tip, ale aktuálně máme na delší dobu naplněnou frontu hostů. Pokud by FIRMA do podcastu moc chtěli, mohou podpořit juniory v Česku a za pozvání si zaplatit https://junior.guru/pricing/ Díky, Honza Javorek
-   Rozjel jsem v klubu soutěž o tři lístky na [Frontkon](https://frontendisti.cz/konference).
    Konference se mezitím vyprodala, takže mají cenu zlata!
-   [Daria hledá práci!](https://www.linkedin.com/posts/honzajavorek_devtooling-monitoring-climate-activity-7116055394468155392-EdD4?utm_source=share&utm_medium=member_desktop)
-   Lidem, kteří jsou už rok v klubu, jsem přidal trochu víc oprávnění.
-   Zrušil jsem skupinu na FB, kde jsem byl admin: Učíme Python.
    Všechno jsem k tomu napsal do [vysvětlujícího příspěvku](https://www.facebook.com/groups/ucimepython/posts/6271091266329112/).
    Skupinu jsem vlastně nezrušil, ale jen pozastavil, protože jsem zjistil, že na FB skupinu zrušit prakticky nejde 🤯
-   Propagoval jsem přednášku, kterou jsme nedávno udělali s Nelou a pak uveřejnili.
    Dal jsem to [na Mastodon](https://mastodonczech.cz/@honzajavorek/111188534773357122) a na LinkedIn (tam je to myslím naplánované na nějaký další den), ale taky jsem prošel všechny příspěvky na FB skupinách, kam v minulosti dával související dotazník, a přidával jsem tam komentář, že na základě toho dotazníku vznikla ta přednáška.
-   Vyšel nový Flask a Werkzeug, což [rozbilo Frozen-Flask](https://github.com/Frozen-Flask/Frozen-Flask/issues/129) a [další věci](https://github.com/pyvec/elsa/issues/90).
    Udělal jsem [aspoň narychlo Pull Request](https://github.com/Frozen-Flask/Frozen-Flask/pull/130).
    Přišel tam pak týpek a dožadoval se okamžité opravy, tak jsem se neudržel a šel jsem mu [vysvětlovat open source](https://github.com/Frozen-Flask/Frozen-Flask/pull/130#issuecomment-1748247285).
    Na pyvec.org jsem [musel připnout verze](https://github.com/pyvec/pyvec.org/pull/364), a uvidíme, co do budoucna.
-   Přidal jsem Mastodon do svého [grafu počtu sledujících](https://junior.guru/open/#socialni-site-a-newsletter).
-   Odkaz na poznámky se minule na můj Telegramový kanál poslal třikrát.
    Snad jsem to opravil.
    Uvidíme dnes.
-   Měli jsme schůzi výboru Pyvce, zápis [zde](https://docs.google.com/document/d/1DN-HNK8rtwjEHViK1iYNKZ1UQ1Dzik5Rz5wNBtZuFdA/edit).
-   Udělal jsem [review Pull Requestu](https://github.com/juniorguru/juniorguru-chick/pull/32#pullrequestreview-1657192271) a doplnil něco do zadání.
-   Díky [Janu Cibulkovi na Mastodonu](https://mastodon.rozhlas.cz/@jancibulka/111170906678847503) jsem zjistil, že nitter.cz umožňuje odebírat různé Twitter účty přes RSS.
    Hurá!
    Mohu zase sledovat zásadní účty, jako jsou [levels](https://nitter.cz/levelsio), [středověký historik Borovský](https://nitter.cz/TomBorovsk1), nebo [Štěvo](https://nitter.cz/stevoeisele).
    Svět je zase v pořádku.
-   Dokončil jsem a poslal PDF s prezentací pro mou přednášku na [Frontkon](https://frontendisti.cz/konference).
-   Dokončil jsem dohodu s Red Hatem na další rok.
    Vypadá to dobře!
-   Švagrová objevila [můj e-shop](https://juniorguru.t-shock.eu/).
    Kdysi dávno jsem ho vytvořil, abych vyzkoušel, jak obtížné je udělat _merch_ pro junior.guru.
    Obtížné to nebylo, ale já tehdy hledal zdroj příjmů a na to to moc není, pokud neprodáte hromady produktů, protože t-shock má velkou provizi (oprávněně, když všechno řeší).
    Takže jsem to nikdy nespustil.
    Aspoň jsem si to teda myslel 😀
    Zjevně se produkty normálně zobrazují ve vyhledávání.
    Tak snad abych to prošel a naklikal tam aspoň něco hezkého a aktuálního.
-   Hrál jsem si ve [Draw Things](https://drawthings.ai/) s SDXL.
    Je fascinující, že to na počítači s 8 GB RAM vůbec rozjedu.
    Házelo to zajímavé obrázky, ale nakonec jsem se stejně vrátil k SD 1.5, protože SDXL bylo prostě pomalé a nebavilo mě čekat.
-   Během 8 dní jsem při procházkách nachodil 8 km, ujel na kole 15 km. Celkem jsem se hýbal 7 h a zdolal při tom 23 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Připravit se na Frontkon a přežít ho.
2.  Publikovat success story s Romanem V. Dvořákem.

Víc toho, myslím, nestihnu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to na [svém Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Odstranění Facebook skupiny, kterou spravujete | Centrum nápovědy pro Facebook](https://www.facebook.com/help/174988392554409/)<br>Věděli jste, že skupinu na Facebooku nelze žádným normálním způsobem úplně zrušit a smazat?
- [Bun hype. How we learned nothing from Yarn](https://dev.to/thejaredwilcurt/bun-hype-how-we-learned-nothing-from-yarn-2n3j)<br>Bun. TypeScript. Yarn. CoffeeScript. Stále stejná pohádka? Hype vynese novou technologii do oblak, aby pak všechny její funkce implementoval původní ekosystém a udělal z ní pouze kapitolu dějin. Autor naznačuje, že tyhle věci způsobují jen zmatek a ukrajují zdroje původnímu ekosystému. Otázka je, zda by se bez nich původní ekosystém inovoval, nebo zda by se ty vyhypované funkce nikdy nestaly prioritou vývoje 🤔
- [Intentional connection in the digital office](https://seths.blog/2021/09/intentional-connection-in-the-digital-office/)<br>„We can share a screen when we get stuck, and we can share it not with the closest person, but with the best person.“ „…connections at the office… didn’t work for everyone in the same way. They often reinforced status roles and privilege. They were unevenly distributed and didn’t usually appear when we needed them. All of which added up to a new layer of stress for many people.“
- [The future of Offpunk: UNIX command-line heaven and packaging hell](https://ploum.net/2023-10-01-future-of-offpunk-packaging-hell.html)<br>„4500 lines of organic python… The number of people able to understand its code entanglement was varying between 0 and 1, depending on the quality of my morning Earl Grey.“
- [Rethinking the Luddites in the Age of A.I.](https://www.newyorker.com/books/page-turner/rethinking-the-luddites-in-the-age-of-ai)<br>„At the time of the Luddites, many hoped the subpar products would prove unacceptable to consumers or to the government. Instead, social norms adjusted. Both the mass-manufactured products and the regimented jobs that produced them quickly became entrenched.“
- [Ozempic's Economic Empire — The Dial](https://www.thedial.world/issue-8/ozempic-novo-nordisk-denmark-economy)<br>Novo Nordisk je Dánská firma, která přišla s přípravkem proti cukrovce a obezitě. Je po něm obrovská poptávka a Novo je už hodnotnější než Coca-Cola. Jenže Dánsko je malá země pro takovou firmu a ekonomika státu se stává na úspěchu Novo Nordisk úplně závislá.
- [Is AI a Platform Shift?](https://matt-rickard.com/is-ai-a-platform-shift)<br>„AI turns the marginal cost of content to zero. Whenever the marginal cost of something in the value chain is set to zero, this usually has a downstream effect on where distribution aggregates (e.g., the Internet turned the marginal cost of software distribution to zero).“
- [(bez titulku)](https://nitter.cz/TomBorovsk1/status/1694042879780335751#m)<br>Mailová schránka po návratu z dovolené. Přesně takhle jsem to teď měl!
- [Audit domácnosti](https://ferovadomacnost.cz/audit)<br>Udělejte si audit domácnosti a posviťte si na to, kdo kolik čeho dělá a jestli by to nešlo změnit tak, aby to bylo vyrovnanější.
- [Typed Visions - SDXL - September 2023](https://docs.google.com/presentation/d/1HEcE3qOAGVujcDaNQbiLXyx7zwKHQkXEILsYBhsot7A/edit?usp=embed_facebook)<br>Chcete si doma hrát se Stable Diffusion? Začněte tady. https://docs.google.com/presentation/d/1HEcE3qOAGVujcDaNQbiLXyx7zwKHQkXEILsYBhsot7A/edit
