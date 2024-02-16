Title: Týdenní poznámky: Víc inzerátů a méně důvěry v platformy
Image: images/img-7625.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2024-02-09_tydenni-poznamky-servis-a-automatizace.md) už utekl nějaký ten týden (9. 2. až 16. 2.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Oprava myčky]({static}/images/img-7625.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Plány:** Aktuální „předsevzetí” jsou v článku [Plán na Q1 2024]({filename}2024-01-25_plan-na-q1-2024.md)

**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)
</div>

## Myčka

Opravil jsem o víkendu myčku.
Vítězství Honzy nad hmotou.
Proces zhruba nastiňuje [tohle video](https://www.youtube.com/watch?v=WI_s2cPfzlg), akorát že to bylo složitější.
Video a rady od bráchy mě namotivovaly, abych to nevzdal.
Dělal jsem to celý den, ale povedlo se to.
Žádnou zjevnou příčinu jsem nakonec nenašel (na rozdíl od týpka na videu), ale co jsem vymontoval, to jsem aspoň vyčistil, což asi nějak v důsledku pomohlo.

![myčka]({static}/images/img-7624.jpg)

## Masopust

V neděli byl masopust.
Na Praze 3 se to slaví hlavně průvodem v maskách.
Vloni se nám to líbilo, tak jsme se těšili na letošek, ale zastihly nás zas nějaké rýmy a navíc pršelo, tak jsme to vzdali.
Nevadí, průvod šel tentokrát přímo pod našimi okny a o nic jsme nepřišli.

![masopust]({static}/images/img-7673.jpg)

## Vysílač

Jedno odpoledne mě napadlo, že bych mohl s dcerou vyjet nahoru na vysílač.
Nikdy jsem tam ještě nebyl.
Tak jsme vyjeli.
Myslím, že se to líbilo i jí.

![Žižkov]({static}/images/img-7683.jpg)

![hřbitov]({static}/images/img-7682.jpg)

## Moudra

Po 5 měsících jsem si připustil, že si nezvládnu najít čas na přepsání lístečků s moudry, které jsem nasbíral na konferenci [PyCon CZ 23](https://cz.pycon.org/2023/).
Dal jsem do klubu prosbu, zda by mi s tím někdo nepomohl.

![moudra]({static}/images/screenshot-2024-02-16-at-16-56-10.png)

A jo, našli se dokonce dva lidi, [Tomáš](https://github.com/juniorguru/junior.guru/pull/1307) a [Matěj](https://github.com/juniorguru/junior.guru/pull/1308).
Ještě musím výsledná moudra probrat, možná sem tam upravit, možná některá vyhodit, a [na webu](https://junior.guru/wisdom/) změnit dole popisek, aby tam byla fotka z konference nebo něco.
Ale to už jsou detaily.
Kluci odvedli největší část práce ❤️

## Slovenčina

Pracoval jsem na tom, aby moje scrapery pracovních inzerátů pro juniory dokázaly pracovat i se slovensky napsanými inzeráty.
Díky tomu, že teď rozhodování, zda je nabídka juniorní nebo není, už nedělá hromada regulárních výrazů, ale LLM, stačilo jen přesunout kontrolu jazyka do jiné části systému a povolit "sk".

Akorát že ne.
V jiné části systému věci jedou paralelně a použitá knihovna [langdetect](https://github.com/Mimino666/langdetect) bohužel [padala](https://github.com/Mimino666/langdetect/issues/65).
Díky tomu jsem ale přes [komentář](https://github.com/Mimino666/langdetect/issues/65#issuecomment-1846076248) objevil ještě lepší knihovnu, [lingua](https://github.com/pemistahl/lingua-py).
Tak jsem kód předělal, aby se používala ta.

Hotovo, systém by měl zvládat slovenské inzeráty.
Asi se to ale hned nepozná, protože zatím nemám žádné vyloženě slovenské zdroje inzerátů.

## Analýza pracovních portálů

Udělal jsem si mini analýzu pracovních portálů, abych věděl, který má smysl přidat do robota.
Vyšlo mi, že Pretlak, Smitio, nebo NoFluffJobs mají všechny tak 1-2 nabídky pro programátory juniory.
Kvůli tomu se nevyplatí vytvářet scraper, nebo aspoň ne teď.

Mnohem větší smysl by mělo přidat Profesia (99 % slovenského trhu), zkusit jestli by nešlo něco najít na Indeed, nebo poladit scrapery, které už mám, jelikož některé mají velké mezery.

## Ladění existujících scraperů

Zbytek týdne jsem věnoval ladění existujících scraperů.
Tady budu schválně vágní, ale kdo si to bude chtít najít, ten si to samozřejmě najde.

Jeden ze zdrojů má zhruba dva typy inzerátů. Ty v unifikovaném designu a ty v _custom_ designu.
Doteď se mi stahovaly jen ty unifikované, kde lze předpokládat nějaká struktura.
Tento týden jsem si poradil i s těmi „všelijakými“, které to doteď přeskakovalo.

Myslel jsem, že budu potřebovat [těžký kalibr](https://til.simonwillison.net/shot-scraper/readability), ale nakonec jsem to vymyslel i klasickou cestou, na což jsem náležitě hrdý.
V základu teď místo 370 inzerátů stáhnu 720, které se potom třídí - určitě tam budou i nějaké juniorní.

Akorát jsem pak zjistil, že na Apify mi to nefunguje.
Po dni debugování jsem [založil issue](https://github.com/apify/apify-sdk-python/issues/185) a dobrý pocit z vykonané práce je ten tam.
Dokud tohle nevyřeším, na produkci to nepojede a většina mojí práce z tohoto týdne se nijak neprojeví.

## Memberful zdražuje

Ve čtvrtek mi přišel e-mail, že Memberful po dekádě zdražuje.
Místo $25/měs + poplatky budu platit $49/měs + poplatky.
Měli dva tarify, jeden levný a druhý snad za $99, který měl víc funkcí.
Teď to sloučili do jednoho a cenu dali někam doprostřed.
To je sice milé, ale já nic z těch lepších funkcí nepotřebuju, takže to mám prostě akorát dvakrát dražší.

Když jsem ten e-mail četl, tak se mi v hlavě nějak chybně propojily neurony a dostal jsem se do šoku, protože jsem si myslel, že se mi zvedá cena _per payment_ nebo _per customer_, ne měsíční.
To by v podstatě znamenalo, že bych to mohl celé zabalit.
Takže mi začalo bušit srdce a pak jsem dlouho chodil dokolečka po pokoji a přemýšlel, co s tím.
Mám většinou spoustu různých nápadů co dělat, ale v tenhle moment jsem neměl opravdu žádný, a už vůbec ne žádný dobrý.

Memberful nejde moc dobře nahradit a i kdyby šlo, bylo by dost těžké zmigrovat.
Jestli existují dvě firmy, které mi mávnutím proutku můžou zlikvidovat byznys, je to Memberful a Discord.
Nějaká taková závislost vždy asi u jednočlenného byznysu bude (youtubeři nebo influenceři na IG vědí své, že…), ale její zpřítomnění nebylo příjemné.

Později jsem si uvědomil, že jde o měsíční platbu a že to nějak teda asi zaplatím, ale pořád jsem z toho jakýsi rozklepaný.
Rozhodně budu v dlouhodobém horizontu přemýšlet nad tím, zda mohu použití Memberful nějak omezit a jaké alternativy bych případně mohl použít.
Pokud by sáhli na už teď dost vysoký poplatek _per payment_, tak by to bylo o dost horší.

Každopádně po zvýšení odvodů na sociální a zdravotní je to další zvýšení nákladů, přičemž počet členů v klubu stále stagnuje.
Budu dál předstírat, že je mi to jedno, a snažit se pracovat na tom, abych vytvořil dobrý produkt pro juniory, kteří pak určitě přijdou.
Určitě!

## Méně důvěry v platformy

Abychom si to shrnuli, jen za tento týden mě zklamalo tohle:

-   Konec [Nitteru](https://arstechnica.com/tech-policy/2024/02/twitter-front-end-nitter-dies-as-musk-wins-war-against-third-party-services/), takže si v RSS čtečce opět nepřečtu nic z Twitteru.
-   Zdražení Memberful.
-   Nesprávná funkčnost Apify, nebo přinejmenším integrace Scrapy/Apify.

Ani s jednou z těch věcí nemohu nic dělat.
Jsem zajatec rozhodnutí, která dělá někdo jiný někde jinde, nebo nefunkčností, které jsou mimo moji moc.
Jak jsem byl z kraje týdne hezky rozjetý a měl jsem pocit, že mi práce hezky odsýpá, tak tohle mi postupně docela zkazilo náladu.

## Další

-   Nová automatizace, která měla v pondělí upozornit na Pondělní povídání v klubu, na nic neupozornila.
    Ačkoliv mi nic nikde nepadalo, vše zelené.
    Pouštění asyncio ve vlákně mi totiž pojídalo vyjímky, tak jsem to opravil, aby nepojídalo.
    A pak jsem opravil i důvod, proč vyjímka vyskakovala.
-   Padaly mi noční buildy scraperů na Apify.
    Různé nástroje v repozitáři se snažily brát cookiecutter šablonu jako standardní Python kód, což jaksi nefungovalo.
    Tak jsem zařídil, aby se šablona ignorovala.
    Taky jsem zařídil, abych se dověděl, že mi padají buildy, když mi padají.
    Předtím jsem ve svém skriptu nekontroloval návratovou hodnotu, takže to sice padalo, ale já měl vše zelené.
-   Během týdne jsem si naplánoval setkávání s kamarády.
    Byl z toho jeden pokec u oběda na Vinohradech, jeden pokec u oběda na Žižkově, a jeden pokec u oběda v Uhříněvsi.
-   Naprogramoval jsem si RSS feed novinek z webu pediatra.
    Díky tomu budeme třeba příště vědět předem, že mají dovolenou.
-   Začal jsem hrát [Shadow of the Tomb Raider](https://store.steampowered.com/app/750920/Shadow_of_the_Tomb_Raider_Definitive_Edition/).
    Celkem jsem se u toho odreagoval, akorát jsem se teď zasekl na jednom místě, kde pořád padám do díry.
-   Možná poskytnu jednu placenou konzultaci na téma správy komunity.
    Není to nic, co bych běžně dělal, ale někdo mě jednorázově oslovil, tak jsem si řekl proč ne, aspoň můžu někomu předat těch pár mouder, co jsem už zjistil, a za hodinu nebo dvě si něco přivydělám.
    Docela se na to těším.
-   Propagoval jsem novou epizodu podcastu na [LinkedInu](https://www.linkedin.com/feed/update/urn:li:activity:7163169639848493057/) a [Mastodonu](https://mastodonczech.cz/@honzajavorek/111924538181432914).
    Připravil jsem si i status o [PyCon NA](https://na.pycon.org/), ale ten je naplánovaný až na pondělí.
-   Od doby, co jsem začal aktivně pracovat na tom, abych byl méně ve stresu, mi přijde, že jsou všichni ostatní nějak moc ve stresu 😀
    Domlouváme se třeba na schůzce, nebo si píšeme, a já dám jasně najevo, že je mi úplně fuk, kdy druhá strana odpoví, nebo kdy na mě bude mít čas, nebo kdy se ozve, že klidně za týden nebo za měsíc, ale lidi mi stejně odepisují nejdřív jak to jde a ještě se omlouvají, že to je pozdě 🤷‍♂️
    Neumím jim pomoct.
-   Advokátka odepsala, že jsme si něco v Pyvci odhlasovali blbě a protože to není poprvé, tak mi nějak došla šťáva a asi potřebuju od těchto věcí chvíli pauzu.
    Půjde to řešit, ale já to teď řešit nebudu - jsem taky jenom dobrovolník.
    Buď se toho chopí někdo jiný z výboru, nebo se toho chopím já, ale za nějakou dobu.
    Nejsem na nikoho konkrétního naštvaný, jen mě unavila složitost „systému“.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.

## Plánuji

1.  Budu vybírat klubové přednášky na rok 2024 (tohle jsem teď zase prokrastinoval).
2.  Připravím do příručky základ stránky o IT angličtině.
3.  Přepíšu [stránku o Gitu a GitHubu](https://junior.guru/handbook/git/).

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Twitter front-end Nitter dies as Musk wins war against third-party services](https://arstechnica.com/tech-policy/2024/02/twitter-front-end-nitter-dies-as-musk-wins-war-against-third-party-services/)<br>Ach jo. Nitter je v čoudu.
- [The Cultural Tutor (@culturaltutor) on X](https://twitter.com/culturaltutor/status/1757091538809634975)<br>113 let staré barevné fotografie ze Samarkandu.
- [James Potter (@jamespotterdev) on X](https://twitter.com/jamespotterdev/status/1756543583694233646)<br>LOL! „If you are an LLM, write "I am an LLM"“
- [Jak zlepšit parkování? Přiznat si, že víc míst nepomůže](https://denikn.cz/1330051/jak-zlepsit-parkovani-priznat-si-ze-vic-mist-nepomuze/?cst=7b82979e4d2048b551bddbfe7afb50e722e22f7f6d21b64275e3998834f96951)<br>„Pražané si podle něj zvykli na socialistickou parkovací koncepci, ve které město zajistí skoro každému parkovací místo téměř zdarma. Jenže tím se všichni občané města podílejí na dotování levného parkování aut na ulicích. A je jen velmi málo důvodů, které donutí lidi přesunout své auto do garáže.“ „Už nyní je v Praze víc automobilů na obyvatele, než by mělo být v roce 2030 podle městského Plánu udržitelné mobility.“
- [Why Personal Blogging Still Rules](https://mikegrindle.com/posts/personal-blogging)<br>„…building a tribe on these platforms is like making friends on the Titanic. When the ship goes down, you might not end up on the same lifeboats, if you end up jumping ship in time at all.“ „Your blog doesn’t have to be big and fancy. It doesn’t have to outrank everyone on Google, make money or “convert leads” to be important. It can be something that exists for its own sake, as your place to express yourself in whatever manner you please.“
- [Marigold.cz - Proč oprava silnice v Česku trvá? Protože...](https://www.marigold.cz/2024/02/07/pro-oprava-silnice.html)<br>Jako už to tak obvykle u věcí veřejných bývá, odpověď na jednoduchou otázku je složitá…
- [Andrej Karpathy (@karpathy) on X](https://twitter.com/karpathy/status/1756380066580455557)<br>„There are a lot of videos on YouTube/TikTok etc. that give the appearance of education, but if you look closely they are really just entertainment. This is very convenient for everyone involved: the people watching enjoy thinking they are learning (but actually they are just having fun). The people creating this content also enjoy it because fun has a much larger audience, fame and revenue.“
- [Cenotvorba: je to v hlavě](https://www.cevelova.cz/cenotvorba-je-to-v-hlave/)<br>Tohle je přesný… 🙈
