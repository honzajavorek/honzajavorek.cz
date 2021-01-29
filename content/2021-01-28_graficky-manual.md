Title: Grafický manuál
Image: images/visualbook.png
Lang: cs


Nevím, jak se to správně dělá, jsem influencer začátečník. Prý se má někam napsat **#spolupráce**, tak to sem píšu raději hned v prvním odstavci. Už nějakou dobu mám na junior.guru [stránku pro média](https://junior.guru/press/) se sekcí o logu, barvách, fontech, správném psaní názvu projektu. Kamarád [Jirka Chlebus](https://www.jirichlebus.cz/) si toho všiml, vyrobil přes Vánoce pro junior.guru profesionální grafický manuál a ten mi dal jako dárek. V krátkém článku napíšu, co se mi na tom líbí.

<iframe width="839" height="472" src="https://www.youtube.com/embed/aXA_DUFQbko" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Grafický manuál se všemi potřebnými informacemi Jirka vytváří v podobě tzv. [Visualbooku](https://visualbook.pro/). Místo abych měl odkazy na logo a údaje o barvách nějak nepřehledně na webu, nebo aby to bylo v nějakém [několikamegovém PDF](http://www.oracle.com/us/technologies/java/java-licensing-logo-guidelines-1908204.pdf), naskládá to všechno přehledně do webové stránky. Ta pak žije třeba na [juniorguru.visualbook.pro](https://juniorguru.visualbook.pro/), ale je to jen statické HTML, CSS a trocha JS, takže to můžu vzít, upravovat, hostovat kde chci. Hodil jsem to tedy na [GitHub Pages](https://pages.github.com/) a mám to na [logo.junior.guru](https://logo.junior.guru/), což se dá komukoliv snadno i nadiktovat.

![Visualbook]({static}/images/visualbook.png)

Díky tomu, že mám teď na vizuální styl separátní webovku, mohl jsem [udělat změny](https://github.com/honzajavorek/junior.guru/commit/c8591cb25f1ab9f0eb9819429735bee149c0fce2), ve kterých jsem ze stránky pro média odebral hodně nepřehledných odkazů a díky kterým z gitu zmizela spousta velkých souborů s fotkami. Ty teď můžu mít na Google Drive, což je upřímně pro takové věci o dost praktičtější. Předtím, kdybych chtěl přidat fotku, musel bych jít do gitu a měnit vše přímo v projektu. Teď mi stačí soubory přetáhnout sem a tam ze složky nebo do složky a hned se to projeví v grafickém manuálu.

![Google Drive]({static}/images/visualbook-gdrive.png)

Jak moc je Visualbook ve skutečnosti praktický nebo ne, jsem měl šanci si vyzkoušet překvapivě brzy. Během ledna dělám co můžu, abych mohl v rámci junior.guru [otevřít zájmový placený klub]({filename}/2021-01-11_spoustim-klub.md). To zahrnovalo například nastavení platební brány [Stripe](https://stripe.com/) nebo hotového řešení pro správu členství [Memberful](https://memberful.com/). Obě tyto služby mají možnost přizpůsobit branding tak, aby jejich uživatelské rozhraní zapadalo do mého webu a působilo na lidi povědomě, důvěryhodně. Ostatně, stejnou věc jsem už dřív nastavoval pro [newsletter](https://eepurl.com/gyG8Bb), který zase řeším přes [MailChimp](https://mailchimp.com/).

![Stripe]({static}/images/visualbook-stripe.png)
Nastavování vzhledu ve službě Stripe

No a nastavování brandingu bylo s tímhle novým grafickým manuálem fakt radost. Hex kódy barev se kopírují na jeden klik, šup šup, logo, ikona a je to. Nemusím nic složitě hledat, všechno na jednom místě.

Další super věc je, že teď mám i stránku, kde je na příkladech vysvětleno [jak se má junior.guru správně psát](https://logo.junior.guru/naming.html). Já to všude píšu stylizovaně junior.guru, ale třeba novináři s tím celkem zápasili. Ono ani junior.guru nevypadá zrovna hezky, když s tím chcete začít větu, nebo dokonce nadpis. Časem jsem tedy vytvořil alternativu, která mě štvala nejmíň: Junior Guru. No a grafický manuál teď všem pěkně ukazuje, jak název správně psát a jak ho rozhodně nepsat. Nevím, jestli to někdo bude číst sám od sebe, ale stačí mi teď případné hříšníky upozornit, že v manuálu to mají vysvětlené.

Do budoucna jsme s Jirkou domluvení, že případné aktualizace provede ručně on. Jde o obyčejné HTML a CSS, tak bych jednoduché věci zvládnul sám, ale je vygenerované, tak do toho nechci moc šťourat, aby se naše verze příliš nerozjely. Hlavně neočekávám, že vůbec nějaké změny budou. To, co by se měnit mohlo, můžu ovládat sám přes Google Drive a výrazné změny ve značce nechystám, dokud si na to junior.guru nevydělá. Vím, že to, co teď mám, je amatérismus splácaný na koleně, ale dokud se junior.guru pořádně nerozjede jako byznys, nemá smysl do něčeho takového zatím investovat. Nějaké ruční aktualizace Visualbooku mě tedy myslím omezovat nebudou. Těším se, že jednou za Jirkou přijdu, dám mu balík peněz na stůl a objednám celý nový vizuální styl :)

No a to je vše, chtěl jsem se jen podělit o radost z vánočního dárku a o tip, jak lze taky pojmout grafický manuál, pokud zrovna něco takového řešíte. Myslel bych si, že pro junior.guru bude něco takového overkill, ale uběhlo jen pár týdnů a hned jsem to několikrát sám využil. Za využití Visualbooku jsem já osobně nic neplatil ani nedostal, spadám do Jirkovy charitativní činnosti (dělal třeba brand i pro [CoroVent](https://cs.wikipedia.org/wiki/CoroVent), nadšenci sestavený covidový ventilátor). O to, abych napsal takovýto článek na blog, se neprosil, udělal jsem to z vlastní vůle :)
