Title: Týdenní poznámky: Přednáška s Evou Pavlíkovou a pokusy s AI
Image: images/img-6506.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/352
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/114676567026113879

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-05-30_tydenni-poznamky-nove-detaily-prednasek-na-webu-a-dalsi-veci.md) už utekl nějaký ten týden (30. 5. až 13. 6.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/img-6506.jpg)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Minulý pátek jsem jel s kamarády na cykloexpedici, tak píšu až dnes. Ujeli jsme za 3 dny skoro 300km. Udělali jsme kolečko z Olomouce, přes Lipník, Hranice, Ostravu, Opavu a Bruntál zase zpátky do Olomouce. Ani jsme moc nezmokli. Hlava si odpočinula, ale fyzicky mi to dalo zabrat a ještě pár dní mi trvalo, než jsem se z toho trochu oklepal.

![text]({static}/images/img-6594.jpg)

## Přednáška s Evou Pavlíkovou

Na přednášku jsem se moc těšil. Protože Evu považuju za velkou hvězdu, dal jsem si tentokrát práci s propagací a celé jedno dopoledne jsem všude po internetu sdílel info o tom, že přednáška bude. Na Facebooky, LinkedIny, Discordy… Ohlasy to mělo [dokonce i na Mastodonu](https://mastodonczech.cz/@honzajavorek/114658100036407434).

Jak to dopadlo? No, dnes je pátek 13. ale nebojím se ho, protože se mi všechno přihodilo už ve středu:

- Na plakátu, kterým jsem olepil celý internet, bylo omylem 20:00 místo 18:00. Kód, který mi generuje plakátky, měl od posledních změn chybku v časové zóně.
- Nebyl jsem připraven půl hodiny předem tak, jak je v návodu pro speakery, ale Eva byla. Sice to udělala skoro jako první speaker vůbec, že by si přečetla návod a opravdu dorazila půl hodiny předem, ale to není její problém 😅
- Patrik, který přednášky nahrává, nebyl vůbec připraven kvůli chybě ve svém kalendáři. Když měla přednáška začít, narychlo jsem sehnal jeho telefonní číslo, ale to už mi nepomohlo, nebyl zrovna ani u počítače.
- Sehnal jsem rychle náhradu, Dana, ale trvalo dalších 30 minut to nastavit, takže Eva byla na callu hodinu (!) než to vůbec začalo.
- Na přednášku dorazilo dle mého názoru málo lidí, nejvíc nás tam bylo asi k patnácti.
- Ve 20:00 do klubu dorazil Jakub Nešetřil a divil se, že přednáška už proběhla.
- Záznam se nakonec stejně nepovedl, protože jak s tím Dan nedělá běžně, někdy v polovině omylem zaříznul to nejdůležitější: zvuk. Velká část tedy záznam má, ale stejně velká část záznam nemá, včetně mnoha zajímavých postřehů, dotazů, promluv od srdíčka, apod.

![ajaj]({static}/images/screenshot-2025-06-12-at-8-29-20.png)

Samotná přednáška byla super a všichni, kdo se připojili, si to moc užili. Bylo to zábavné, podnětné, byla hromada dotazů, bylo to živé, bylo to od srdíčka. Měl jsem v plánu, že bych přidal do příručky novou kapitolu o státní správě a tuhle přednášku dodatečně zveřejnil a vložil ji tam. Jestli má smysl zveřejnit useknutou polovinu záznamu, to teda fakt nevím.

Chyby a nepříjemnosti se dějí, ale už dlouho se mi nestalo, aby se toho v jeden den stalo tolik najednou. Když se kupily fuckupy, tak jsem zůstával ještě docela v klidu, protože jsem přece jenom něco už během těch přednášek zažil, a snažím se ty věci za běhu spíš řešit, než se jimi nechat vydeptat. Dokud jsem si myslel, že mám záznam, tak jsem měl navíc pocit, že to má _happy end_. Ale když jsem ráno otevřel DaVinci a viděl, že půlka audio stopy je hluchá, tak to na mě dolehlo a byl jsem z toho fakt smutný.

Evě jsem se za to celé omluvil. Jak to pojistit pro příště, to moc nevím. Napadlo mě nechat bota, aby Patrikovi vždy před přednáškou napsal ještě DM, čímž se pojistí jeho kalendář. A zkusit vymyslet, jak lokálně od sebe nahrát aspoň zvuk z Discordu a mého mikrofonu (což může být na macOS trochu výzva), protože ten zvuk je nakonec většinou to nejdůležitější.

![přednáška]({static}/images/screenshot-2025-06-11-at-19-29-46.png)

## Experimenty s AI

Napadlo mě, že bych mohl zkusit pomocí AI vytvořit lidsky čitelné shrnutí toho, co se v poslední době probíralo v klubu. To by řešilo hned několik zásadních problémů, protože pro mnoho lidí je Discord nepřehledný a neradi tam chodí, nebo ho prostě nestíhají sledovat.

Nejdřív jsem se zkoušel [vzdělávat](https://www.youtube.com/watch?v=qaPMdcCqtWk) a koukal jsem na [různé věci](https://python.langchain.com/docs/integrations/chat_loaders/discord/) a četl [dokumentaci langchainu](https://python.langchain.com/docs/tutorials/summarization/). Pak jsem začal experimentovat přímo v kódu.

Zkoušel jsem všechno možné. Napadlo mě klasifikovat jednotlivé zprávy, nebo celé kanály, a postupně dělat shrnutí z těch shrnutí. Dívat se na to, kolik lidí se mezi sebou bavilo, jak moc napsali písmenek, jak moc bylo reakcí a zkoušet podle toho identifikovat rezonující témata. Zkoušel jsem to zpracovávat v angličtině, pak zase v češtině. Na kousky, pak zase najednou. Napsal jsem nepřeberné množství promptů a ladil je a koukal, co z toho vypadne.

Postupně doiteroval k tomu, že mám `gpt-4.1-mini` místo `gpt-4o-mini`, protože mu jde mnohem lépe generování češtiny. Porozumění je asi stejné, ale když měl udělat český text, tak to co lezlo z `4o-mini` bylo [dost nepoužitelné](https://mastodonczech.cz/@honzajavorek/114671634596001913). Protože má `4.1-mini` obrovské kontextové okno, nic nerozděluju a nasypu to tam v jediném promptu. Nakonec jsem došel k tomu, že nejdřív udělám shrnutí a potom mu to shrnutí pošlu s úplně jiným systémovým promptem a snažím se ho přepsat do určitého stylu vyjadřování. Zdá se, že to funguje lépe, než když jsem se to snažil udělat celé v jednom. Langchain nakonec ani nepoužívám, nebylo proč. Asi 5x už jsem ten kód celý přepsal, protože jsem změnil přístup.

No, jsem po těch necelých dvou týdnech někde u docela funkčního prototypu, ale pořád to ještě není tam, kde bych to chtěl mít a bude to vyžadovat ještě nějaké to sochání promptů.

## Další

-   Do neděle je termín na registraci akcí pro Týden pro digitální Česko a já nemám žádnou registrovanou. Potřeboval bych se domluvit s Mews, ale neodpovídali mi teď, tak to tam asi nějak naplácnu nanečisto a uvidím, co z toho bude.
-   Organizoval jsem přednášky s Táňou. Táňa navrhuje dotazník na sbírání zpětné vazby po přednáškách. Děláme další plán na přednášky, vybíráme témata, oslovujeme možné speakery. Probírál jsem s Táňou newsletter.
-   Doklepnul jsem poslední věci kolem předělávání přednášek na webu. Promazal jsem v kódu něco, co už nebylo potřeba. Předělal jsem, jak jsou Danova a Nelina přednáška vloženy do příručky. Teď už to není úplně ručně, ale berou se data z databáze přímo z tabulky s přednáškami, a používá se tam lepší náhledový obrázek. Přidal jsem do HTML [Event metadata](https://schema.org/Event) pro vyhledávače a další nástroje. Dokonce jsem zjistil, že [to jde i otestovat](https://search.google.com/test/rich-results), že na to má Google nějaký nástroj. Na seznam přednášek jsem přidal odkaz na návod pro speakery. Ten jsem drobně vylepšil, přidal tlačítka a _Table of Contents_.
-   Updatoval jsem svoje fakturační údaje na WEDOSu. Nebo VEDOSu. Nevím? A nabil jsem si tam peníze na domény.
-   Updatoval jsem screenshoty na webu.
-   Vyzkoušel jsem opravenou verzi Lychee a [podal dlouhý report do issue](https://github.com/lycheeverse/lychee/issues/1709#issuecomment-2934933326).
-   Vzdělával jsem se ohledně DaVinci. [Tohle](https://www.youtube.com/watch?v=CH6hedwy2xM) bylo dobré video o efektech. [Tady](https://www.youtube.com/watch?v=WmGkRjYSOPk) je dobrá pasáž o tom, jak udělat takové to kolečko s mluvící hlavou v rohu nebo split screen.
-   Setkal jsem se s Milkem z klubu. Ukázal mi hezkou novou kavárnu poblíž České Televize. Volal jsem si přes hodinu s Danem. Popovídali jsme si o životě a o klubu. Volal jsem si s Terkou z ContentParty. Probrali jsme její podnikání a popovídali jsme si o životě. Dostal jsem u toho vždy pár nových nápadů, co by šlo dělat.
-   Začalo mi blbnout něco kolem Discordu, tak jsem upgradoval py-cord v celém stacku junior.guru. Všiml jsem si, že nevydávají nové verze a poslední byla snad před rokem nebo kdy, ale že v repozitáři to frčí. Tak jsem přešel na verzi přímo z Gitu. Protože používá cosi, co se jmenuje „setuptools_scm”, potřeboval jsem v Dockeru na Fly.io buď nainstalovat Git, nebo použít nějaký hack přes env var. Vybral jsem si zatím [ten hack](https://github.com/juniorguru/chick/blob/bc976111c7e281e0484ac2426a9afb3361915726/Dockerfile#L5). Za junior.guru jsem taky začal přes GitHub Sponzors podporovat maintainerku, protože je to pro mě dost zásadní balíček.
-   Koukal jsem, co by mi mohlo zrychlit esbuild, ale [asi ho zdržuje Sass plugin](https://github.com/evanw/esbuild/issues/2228#issuecomment-1120249605), se kterým nic nenadělám. Neměřil jsem to ale a nic jsem nezkoušel.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Přečetl jsem celý Discord. Prošel jsem všechny e-maily související s junior.guru, i ty, které mi tam kvasily fakt dlouho!
-   Za 15 dní jsem naběhal 6 km, ujel na kole 296 km. Celkem jsem se hýbal 32 h a zdolal při tom 302 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Registrovat akci do Týdne pro digitální Česko.
2.  Daria mi něco poslala k [EuroPython Beginners’ Day Unconference](https://ep2025.europython.eu/beginners-day/), kterou organizujeme, tak bych na to měl mrknout.
3.  Pokračovat ve tvoření těch automatických shrnutí.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [The two types of open source](https://filiph.net/text/two-types-of-open-source.html)<br>Zajímavé zamyšlení nad tím, jak přistupovat k open source projektům a pokud nějaké máte, jak je prezentovat světu, abyste se z toho časem nezbláznili.
- [Watching o3 guess a photo’s location is surreal, dystopian and wildly entertaining](https://simonwillison.net/2025/Apr/26/o3-photo-locations/)<br>„Technology can identify locations from photographs now. It’s vitally important that people understand how easy this is—if you have any reason at all to be concerned about your safety, you need to know that any photo you share—even a photo as bland as my example above—could be used to identify your location.“
- [F1 at 75](https://www.bbc.com/sport/extra/v7yykmbyey/f1-at-75-by-bbc-sport-and-getty-images)<br>Krásný průlet historií F1. Trvalo mi to teda týdny, než jsem si to po kouskách všechno prošel a prohlédl, jak nějakou výstavu nebo knihu, ale stálo to za to.
- [Cestující rozdělujeme na dva typy. Autoři nového designu českých nádraží vysvětlují změny písma i piktogramů - Zdopravy.cz](https://zdopravy.cz/cestujici-rozdelujeme-na-dva-typy-autori-noveho-designu-ceskych-nadrazi-vysvetluji-zmeny-pisma-i-piktogramu-246660/)<br>Budou nové cedulky na nádražích!
