Title: Týdenní poznámky: Další nemoci, angličtina a průzkum Apify
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-12-08_tydenni-poznamky-tatinek-na-plny-uvazek.md) už utekl nějaký ten týden (8. 12. až 22. 12.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [teď plánuji]({filename}2023-08-07_letni-pit-stop.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/3/).
</div>

Poznámky píšu po dvou týdnech, protože během toho prvního jsem opět prakticky nic neudělal.
Hned jak se začala žena trochu uzdravovat, lehli jsme všichni s covidem.
To bylo „výborné“, především na psychiku.

S dítětem je blbé to, že se o něj člověk musí starat, i když je sám nemocný.
Covid nekosí lidi v rodině postupně, ale všechny najednou, takže jsou všichni unavení, vyčerpaní, a protivní.

Přemýšlím, jaké to bývalo dřív. Člověk napsal do práce na Slack, že je nemocný, a zalezl si do postele. Pak byl zhruba týden největší životní problém to, že když se mi udělalo trochu líp, tak se mi noťas pořád přehříval o peřinu při hraní Europa Universalis 😀

Aby toho nebylo málo, v sobotu, kdy už jsem se cítil zdravý, jsem něco snědl a s život ohrožující alergickou reakcí mě odvezli sanitkou do nemocnice.
Tam mě zachránili a ještě ten den propustili.
Teď se cítím dobře.

Jsem zvědavý, kdy tahle má série zdravotních peripetií skončí a jestli vůbec.
Na stole mám teď tři žádanky k doktorům na příští rok a to mám ještě i v lednu stále ještě jednu pravidelnou léčbu.
Některé problémy, které jsem měl, spolu souvisí, ale některé vůbec.
Některé jsou ze stresu, který jsem se snažil v poslední době dost omezit, ale některé se dějí prostě jen tak.
Prostě mám asi jen to „štěstí“, že se to všechno sere najednou.
Každopádně mě to teda už psychicky dost ždíme.

Je zajímavé vyzkoušet si všechna mentální cvičení o tom, jak je dobré užívat si přítomného okamžiku, protože zítra můžu mít zase nějaký zdravotní problém, ale rád bych podotknul, že ta cvičení mám hotová a teď už bych si od nich dal i pauzu.
Tak snad už aby byl rok 2024 a přinesl nějaké nové zážitky, ideálně hezké.

## Angličtina

Rozjeli jsme v klubu lekce angličtiny s [Veronikou Rychlou z GeekPower](https://geekpower.cz/).
Lidi si to nějak domluvili a utvořili skupinky, na mně potom bylo vyřešit, jakým způsobem si za to budou připlácet a jak to celé bude fungovat.

To bylo složitější, než jsem čekal, ale nakonec jsem to nějak rozlousknul.
Na podpoře Memberful jsem se ujistil, že lidi se mohou přihlásit k více nezávislým předplatným, a potom jsem vytvořil nový tarif jen na angličtinu.
Nevýhoda je, že ten dědí veškeré nastavení pro předplatné klubu, takže např. formuláře při příchodu či odchodu člena, emailing, apod. jsou totožné a nelze to změnit.
Taky mi to dělá dost velký binec ve statistikách a zabralo mi celý jeden den přepsat všechny skripty tak, aby se tarif na angličtinu ignoroval.

Dost práce mi dalo i propočítat správně pricing, abych na tom neprodělával.
Cenu jsem chtěl paušální, měsíční, ale Veronika mi bude fakturovat jednotlivé lekce.
Taky jsem chtěl, aby to bylo pro členy klubu trochu dotované.

Nakonec to funguje takhle: [Klu­bo­vé lek­ce an­g­lič­ti­ny](https://junior.guru/membership-english/).
Spolu s vytvořením této nové stránky jsem do nového designu předělal i [starou stránku pro členy](https://junior.guru/membership/), kde se lidi objeví, když se zaregistrují do klubu.
Angličtinu zatím nikde veřejně nepropaguji, nechám to zatím plynout vlastním tempem a uvidím, jak se to vyvine.

Přemýšlel jsem nad tím, zda to mám celé vůbec dělat, když je s tím tolik problémů a nejspíš to přinese jen minimum plusů, ale dal jsem zatím na svůj pocit, že tohle do klubu patří, že bych to měl vyzkoušet, a že se u toho třeba naučím zase něco nového.

## PoC Apify

Pokračoval jsem v PoC (_proof of concept_) jestli by mi použití Apify náhodou nemohlo vyřešit spoustu problémů.
Setkal jsem se s fajn supportem přes jejich Discord i GitHub issues.
Některé věci ještě chybí, ale podle všeho se jim je povedlo vyřešit a doplnit dřív, než jsem dopsal tyhle poznámky.

Zkusil jsem pouštět více Scrapy spiderů v jednom actoru, ale [to mi moc nefungovalo](https://github.com/apify/actor-templates/issues/202#issuecomment-1856495473), tak jsem to [předělal spíš na monorepo](https://github.com/apify/actor-monorepo-example), kde každý spider je jeden actor.

Propojení actorů s Gitem mi přišlo jakési magické, nejasné a zmatené, ale nakonec jsem se s tím nějak naučil.
Asi to bylo tím, že jsem míchal více přístupů dohromady a ještě actory různě přejmenovával a přehazoval z místa na místo.

Zatím bych svůj dosavadní postup prohlásil za úspěch.
Musím [vyřešit použití proxy ve spideru](https://github.com/apify/actor-templates/issues/255#issuecomment-1858775525).
Potom zkusím data z Apify i konzumovat na straně existujícího robota.
Pokud to bude fungovat, můžu začít mazat kód a spoustu věcí začít přesouvat směrem do Apify.

Při pokusech jsem narazil na [scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), který aktuálně nevyužiju, ale možná bych jednou využít mohl, tak si to sem poznačím.

## Další

-   Pořizoval jsem vánoční dárky a balil je.
-   Propagoval jsem [Python Pizza](https://prague.python.pizza/), jednodenní konferenci v Praze, která proběhne v únoru.
    Ještě můžete poslat návrh na svou přednášku. Pokud byste tam chtěli mít přednášku. Tak šup.
-   Opravil jsem nějaké drobnosti v grafech příjmů a výdajů na webu.
-   Z textového kanálu „pozvánky a promo“ v klubu jsem udělal kanál typu forum, aby to tam bylo přehlednější.
    Protože do něj ale můj skript sype odkazy na srazy, vyústilo to v celý den programování.
    Musel jsem to skoro celé přepsat.
-   Poslal jsem přes Zásilkovnu knihu o šifrách, kterou vyhrál jeden člen klubu, účastník Mílovy přednášky.
    Poprvé jsem něco takhle posílal a překvapilo mě, jak to bylo jednoduché.
-   Napsal jsem advokátce, aby nám pomohla přepsat stanovy Pyvce.
    Nejsme usnášeníschopní, když je předsedkyně indisponovaná, a to by mohl být pro Pyvec do budoucna problém.
    Chce to nějaké pojistky, abychom mohli Pyvec ovládat i pokud předsedkyně zrovna nemůže.
-   Přidal jsem odkaz na [tento článek](https://www.irozhlas.cz/zpravy-domov/okd-rekvalifikace-horniku-programatori-ridici-data_2311030620_fil) na junior.guru do [sekce s Tomášem Hisemem](https://junior.guru/stories/#z-hornika-programatorem).
-   Nainstaloval jsem si [LM Studio](https://lmstudio.ai/) a o Vánocích zkusím, co umí lokální open source LLM modely.
-   Začal jsem občas sdílet obrázky vygenerované přes Stable Diffusion do komunity kolem Draw Things.
    Je fajn být součástí nějaké milé komunity a nemuset se tam o nic starat :)
    Dokonce mi nějací lidi soukromě napsali, zda bych jim neposlal jak to generuju, tak asi už nejsem úplná nula a mám nějaké _know-how_, to mě potěšilo.
-   Opravil jsem rozbitý skript, který mi pomáhá s ukládáním poznámek k jednotlivým stránkám příručky.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Naplánoval jsem nějaké statusy na LinkedIn.
    Pozval jsem jednu paní do podcastu.
    Domlouval jsem termín jednoho důležitého callu.
-   Za 15 dní jsem se nevěnoval žádné sportovní aktivitě.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Náš příběh je u konce](https://www.greenfoxacademy.cz/post/nas-pribeh-je-u-konce)<br>Ještě 27.11. startovali další vlnu kurzů, teď náhle v insolvenci. Velmi zvláštní. Green Fox Academy zavírají krám.
- [Unbundling AI — Benedict Evans](https://www.ben-evans.com/benedictevans/2023/10/5/unbundling-ai)<br>„But if you need a manual, it’s not ‘natural language’ anymore. Once you start talking about ‘prompt engineering’, you’re describing command lines - you’re describing what came before GUIs, not what comes after them.“
- [AI and Everything Else - Benedict Evans | Slush 2023](https://www.youtube.com/watch?v=xNBiPd2H9J0)<br>Benedict Evans se zamýšlí nad AI, pokládá otázky, zasazuje věci do kontextu, a mě to baví.
- [Všechno ohlídat a nesložit se z toho. Je to těžší, než jsem si myslel, říká táta na rodičovské — Houpačky](https://www.mujrozhlas.cz/rapi/view/episode/773bc04e-e473-308f-8c24-97581a845310)<br>Jaké to je být otcem na rodičovské?
- [Z Ukrajiny: „Přijdou pro tebe vojáci a za 3 dny jedeš na frontu. Dost lidí umírá“ — PULS](https://podcasters.spotify.com/pod/show/jolana-humplov/episodes/Z-Ukrajiny-Pijdou-pro-tebe-vojci-a-za-3-dny-jede-na-frontu--Dost-lid-umr-e2d7vfg)<br>Jak to teď vypadá na Ukrajině?
- [On Latex](https://www.scopeofwork.net/on-latex/)<br>„Just as speculators drove the value of untested, unprofitable dot com start-up companies to surreal levels during the 1990s, thousands of nineteenth-century New Englanders poured their savings into the miracle substance called rubber without knowing much of anything about it. In both cases, the education was hard-earned and painful.“
- [OpenCage - Easy, Open, Worldwide, Affordable Geocoding and Geosearch](https://opencagedata.com/)<br>Tohle se bude někdy hodit.
- [Real Play](https://www.theparisreview.org/blog/2023/10/19/real-play/)<br>Pamatujete hru Sims? Bavilo by vás to i dnes, jako dospěláky? Nejspíš ne, protože to žijete.
- [Kdo ty hlasy zvedne?](https://davidklimes.cz/newsletter/172)<br>„Tyto obrázky by měly být ukazovány politikům každý den a dokola by měly být tázáni, z čeho chtějí ty nové výdaje zaplatit, když už je neumí snížit.“
- [Vojtěch Pecka: Klimatické omyly Petra Pokorného](https://ekolist.cz/cz/publicistika/nazory-a-komentare/vojtech-pecka-klimaticke-omyly-petra-pokorneho)<br>„…víme, že lidská civilizace vznikla v době holocénní (poměrně nezvyklé) stability. Jak bude společnost reagovat na takto prudké změny je otázka, protože se s nimi nikdy nesetkala. Klimatické modely ukazují, že to je jenom klouzání po povrchu toho, co má přijít v následujících desetiletích, pokud nepřestaneme spalovat fosilní paliva.“ „V podstatě všechny modely již přes padesát let úspěšně popisují současný trend oteplení.“
- [Down to the wire: The ship fixing our internet](https://continent.substack.com/p/down-to-the-wire-the-ship-fixing)<br>„Ingenious engineering, sheer physical strength and careful coordination are required. Sometimes the cables carry live current, which heightens the danger.“ „It took the crew a month to sail around the Cape of Good Hope to make the repairs. Shortly after that, they restored another three cables in Angola which brought 750,000 people back online.“
- [Rukověť kybernetické odolnosti](https://blog.digitalnisvobody.cz/2023/12/07/rukovet-kyberneticke-odolnosti/)<br>Zajímavý výlet do hlubin osobní kybernetické bezpečnosti
- [The dawn of the omnistar](https://www.economist.com/leaders/2023/11/09/how-artificial-intelligence-will-transform-fame)<br>Co udělá AI se slávou?
