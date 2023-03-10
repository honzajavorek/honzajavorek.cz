Title: Týdenní poznámky: Nabídky práce, realtime bot, Brno a mnoho dalšího
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/136


Utekl zas nějaký ten týden (24. 2. až 10. 3.) a tak [stejně jako minule]({filename}2023-02-24_tydenni-poznamky-tyden-zdravi-a-dokonceni-evidence-firem.md) sepisuji, co jsem dělal a co jsem se naučil.
Tvořím [junior.guru](https://junior.guru/) a nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/) a členy by mohlo zajímat, co dělám.
Psaní poznámek mi taky pomáhá nezbláznit se a nepropadat pocitu, že je konec týdne a já jsem nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Před týdnem jsem poznámky nestihl, protože jsme odjeli do Brna na prodloužený víkend a ve vlaku se mi chtělo spíš programovat.
Takže píšu zpětně za dva týdny.
Může se to zdát dlouhé, ale standardně jsou poznámky na 10 minut čtení a tohle je na 20, takže to vychází 😀


## Vítání firem

Po dokončení evidence firem jsem se vrhnul na úpravy vítání firem v klubu.
Vždy, když uzavřu partnerství s novou firmou, uvítá ji bot viditelně v klubu a popíše, co jsme si domluvili.
Původní verze byla vzhledem k nové evidenci firem už zastaralá, takže jsem to celé přepisoval.
Nejvíc práce dalo vymyslet nové uvítání tak, aby bylo co nejpřehlednější.

![Vítačka]({static}/images/screenshot-2023-03-10-at-14-43-40.png)


## Vylepšování nabídek práce

V bodech jsem si sepsal záměr, jaký mám s nabídkami práce do budoucna:

-   Inzeráty jsou jednak inzeráty, jednak data, která mohu podarovat (Czechitas, Aj Ty v IT) nebo prodat dál.
-   Propisují se do klubu v podobě fóra, do kterého přispívá bot, ale může tam přispět i někdo jiný.
-   Kariérní věci se probírají v #kariéra nebo #pohovory.
-   Existuje #práce-inzeráty (kam padají inzeráty), #práce-hledám (kam píšou lidi).
-   Náhled na inzeráty je na webu, ale víc informací k nabídkám práce se lidi doví v klubu.
-   Informace k nabídkám lze donekonečna vylepšovat zlepšováním dat, což přináší hodnotu klubu i datům.
-   Data zatím nebudu sbírat do historie a nebudu se tím trápit…
    Na GitHubu nebo na CDN bych možná mohl mít data warehouse, ale pokud by odběratelům stačila průtoková data, je to pro mě jednodušší.
    Zase bez historie nejsem schopen sám data nějak analyzovat a dělat k firmám např. graf jak často hledají juniory apod.
-   Algoritmus třídění nabídek zjednoduším.
    Najít 20 % práce, která vyřeší 80 % věcí.
    Analyzovat složitě texty inzerátů je asi overkill, nejspíš by šlo dosáhnout podobného výsledku s pár klíčovými slovy a dobře mířenými reguláry.
    Netrápit se tolik tím, pokud proklouzne seniornější nabídka nebo občas něco nerelevantního, ale spíš tím, že nespravědlivě vyhážu 30 juniorních.
-   Implementace AI je bonus a pokud by se mi povedlo udělat nový algoritmus dostatečně dobrý, možná to dělat vůbec nebudu.
    Pokud AI bude, tak v klubu bude ještě forum #práce-inzeráty-koš (výchozí emoji bude 👍) a dobrovolná role, kterou si mohou vzít lidi, kteří chtějí s nabídkami práce pomáhat.
    Mohou se probírat košem a učit AI, že něco neměla vyhodit.
-   Bylo by dobré zefektivnit stahování inzerátů, aby to odsýpalo.
-   Bylo by dobré si ke scraperům vytvořit monitoring a dát třeba na [/open/](https://junior.guru/open/) nějaké statistiky, ať vím, co se ve skutečnosti děje.
    Při posledním předělávání inzerátů jsem monitoring smazal a doteď jej ničím nenahradil.

Nový vzhled pracovních inzerátů v klubu jsem tedy udělal pomocí Discord kanálu typu fórum.
Krátkým skriptem jsem ověřil, že lze do vláken ve fórech přidávat embedy, tlačítka, apod.
Náhledový obrázek mi ale přidat nešlo.
[Zeptal jsem se](https://github.com/Pycord-Development/pycord/discussions/1948) a pak jsem si sám odpověděl, protože jsem našel _workaround_.
Nicméně jde o bug a autoři pycordu jej už opravují.

Následně jsem překopal kanály, které řeší pracovní inzeráty.
Měl jsem v klubu #práce a #práce-bot.
Nyní je tam #práce-inzeráty, kam přispívá jak bot, tak lidi, a #práce-hledám, kde mohou lidé práci poptávat.
Bota jsem naučil zakládat v #práce-inzeráty vlákno pro každou nabídku zvlášť, s logem a tlačítky, a hned jsem to pustil na produkci.
První reakce od členů v klubu nebyly jednoznačné, ale budu doufat, že je to lepší, než co tam bylo předtím.
Těžko členům teď vysvětlovat, že jde o úplně prvotní verzi a výhody nového uspořádání vyniknou až s dalšími změnami a vylepšeními.

![Inzeráty]({static}/images/screenshot-2023-03-10-at-17-10-28.png)

Například mohu ke každému inzerátu přidat do vlákna zprávu s dalšími informacemi o firmě.
Mohu každou nabídku obohatit dalšími odkazy, daty, grafy.
Lidé mohou pod inzeráty diskutovat.
Je to na Discordu, takže tam mohu mít i věci, které bych veřejně na web raději nedával.
Zároveň je to přidaná hodnota pro členy klubu a další důvod platit za klub, což mi pomáhá tuhle práci financovat.

Následně jsem skoro celý jeden pracovní den strávil s tím, že jsem procházel svoje historické poznámky a úkoly k pracovním inzerátům na JG.
Byl to jeden dlouhý sloupec v Trellu, který jsem roztřídil na tři jiné:

-   Vylepšování [webové verze inzerátů](https://junior.guru/jobs/),
-   vylepšování dat kolem inzerátů (např. normalizace názvu firmy, deduplikace…),
-   nové zdroje inzerátů, ze kterých by je šlo stahovat (asi 30 nápadů).

Několika kartičkám jsem se samozřejmě pouze zasmál a smazal je.
Některé staré nápady byly fakt naivní.

Pak jsem udělal _proof of concept_ na scraper Jobs.cz.
Ten jsem postupně vylepšoval a vylepšoval.
Zatím to neumí inzeráty, které jsou na samostatných klientských portálech, ale základní inzeráty to zvládne.
Poslední vylepšení jsem dělal během dneška, tak uvidím, jak to bude fungovat a co bude potřeba opravit.
Až to chvíli pojede, napíšu do Czechitas, že už si Jobs.cz nemusí stahovat samy.

![XPath]({static}/images/screenshot-2023-03-07-at-18-41-19.png)
Překvapilo mě, jak pěkně umí ChatGPT napovídat se složitými XPath dotazy. Odpověď na toto bych na Google hledal hodinu, tady jsem vložil konkrétní HTML a přirozeným jazykem AI nasměroval k tomu, co potřebuji vyřešit.

Nějvětší paráda je, jak se mi to celé daří dělat v rámci _continuous deployment_.
V podstatě každý commit šel hned na produkci a mohl jsem se tak průběžně vždy radovat z hotové práce.


## Realtime bot!

OpenAI [vydalo API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) a to mě zase nakoplo, abych si pospíšil s realtime botem.

Jde o to, že můj standardní bot se spouští jen zhruba jednou denně.
Už delší dobu jsem měl nápad, že by mohl existoval ještě realtime bot, který by pomáhal s nenáročnými drobnostmi, jmenovitě:

- Okamžité zakládání vláken v některých kanálech,
- okamžité vítání nových členů,
- okamžité ukládání špendlíků do soukromých zpráv,
- a další.

Bot by vycházel pouze ze stavu Discordu, neměl by žádnou databázi nebo napojení na zbytek JG.
Kdyby spadnul, nic zásadního by se nestalo, asynchronní pomalý bot by to pak někdy udělal za něj.

No a já si brousím zuby na to, že by tihle moji boti mohli lidi vítat s pomocí ChatGPT.
Je to příležitost, jak být mezi prvními, kdo se naučí využívat ChatGPT v praxi, ve svém produktu, a získat tak v téhle zásadní oblasti náskok.

Nemám na to ale vlastně moc čas.
Naštěstí jsem objevil pomocníka jménem [Mandlemankiller](https://github.com/Mandlemankiller), který se do tvorby realtime bota s nadšením pustil.
Pro něj je to pěkný projekt, na kterém se může učit, a mě to řeší reálné potřeby a reálné _R&D_.
Organizaci na GitHubu jsem vytvořil už minule, teď jsem přidal [repo](https://github.com/juniorguru/juniorguru-chick/).

Nejvíc času nám zabralo vymyslet název.
Nakonec jsem vymýšlení vzdal a nazval to `juniorguru-chick` (bot se jmenuje kuře), ačkoliv to z různých důvodů není úplně ideální, ale chtěl jsem se po hodině vymýšlení posunout už někam dál.

![Nové repo]({static}/images/screenshot-2023-03-10-at-17-11-55-issues-juniorguru-juniorguru-chick.png){: .img-thumbnail }

Zatím bot umí okamžité zakládání vláken ve dvou kanálech, kde se to v klubu hodí.
Vítání uděláme v první verzi bez AI, ale i tam nám to ještě zabere nějaký čas, protože tam to bude chtít promyslet a bude to víc práce.

Mandlemankillerovo nadšení do práce mě strhlo a snažil jsem se, aby se na věci co nejvíc učil, aby měl nové výzvy, a abych jej nezadusil tím, že nebudu po ruce.
Bylo vlastně osvěžující po letech práce v jednom člověku zase jednou sepisovat README a dělat věci jako Issues, reviews, nebo Pull Requesty.

Chtěl jsem, aby to celé bylo _continuous deployment_ a aby hned viděl výsledky své práce.
Jako runtime jsem zvolil [Fly.io](https://fly.io/), kde už jednu soukromou appku mám a zdá se mi to tam v pohodě.
Inspiroval jsem se [tady](https://jonahlawrence.hashnode.dev/hosting-a-python-discord-bot-for-free-with-flyio), ale nakonec jsem řešil hned několik zádrhelů.

Fly neumí v Python buildpacku instalovat pomocí [Poetry](https://python-poetry.org/) a řešení je vlastní `Dockerfile`.
Jenže ten zas neumím já.
Nefungoval mi deploy a než jsem přišel na to, čím to je, myslel jsem, že mám chybu v `Dockerfile` a skoro jsem už i nainstaloval Docker a smiřoval se s tím, že se jej budu muset konečně naučit.
Bylo to ale tím, že se mi `flyctl` lokálně zneschopnilo kvůli nějakému problému se sítí (_wireguard_, který [mám resetovat](https://community.fly.io/t/deployments-not-working-error-connecting-to-docker/3992/40), ehm, vůbec netuším o co jde).
Řešil jsem to snad hodinu nebo dvě.

Další problém byl, že bot nemá žádný interface, na kterém by mohlo Fly kontrolovat, jestli žije.
Trvalo dost dlouho, než mi došlo, že deploy neprojde, protože se Fly snaží zjistit, zda bot jede, ale nemá jak.
Smazal jsem tedy kontroly, které mi Fly vygenerovalo do konfiguráku a už to jelo.

Později jsem se naučil, jak k realtime Discord botovi [přidat i nějakou HTTP stránku přes aiohttp](https://github.com/juniorguru/juniorguru-chick/issues/1).
Tohle jsem nikdy nedělal, takže pomohlo [StackOverflow](https://stackoverflow.com/a/54462411/325365) a dokumentace.
Nakonec se mi [podařilo](https://github.com/juniorguru/juniorguru-chick/pull/9/) vystavit jednoduchou JSON odpověď, přes kterou mohu kontrolovat, že bot žije.
Dělám to jak přes Fly, kam jsem vrátil kontroly, tak přes [nový skript](https://github.com/honzajavorek/junior.guru/blob/e570f9bcf1b7fdf2216ce113d1337b1168ca2f4c/juniorguru/cli/check_bot.py) na hlavním repu.
Ten se podívá, jestli bot žije a pokud ne, tak build selže.
Neshodí to ale celý build.
Podobně jako kontrola rozbitých odkazů v příručce mi tohle jen zahlásí do e-mailu, že se něco nepovedlo, ale nezávisí na tom vše ostatní.

Vypisuje se tam i _uptime_ a hned při prvním pokusu mi přišlo, že je nějaký malý.
V logu na Fly jsem pak zjistil, že se bot nemohl připojit v jednu chvíli na Discord, tak spadl, ale Fly jej nahodilo zpět.
Takže paráda!
Máme realtime bota, který už s něčím pomáhá v klubu a máme na něj i primitivní monitoring, který jednou denně zkontroluje, jestli bot žije.


## Mentoring

Sešel jsem se s Mews a s Pure Storage.
V Mews mají super střechu s výhledem a v Pure Storage spoustu balkónů, kde mohou lidi pracovat, jíst, nebo prostě chillovat a dýchat u toho čerstvý vzduch.

Obě schůzky byly v podstatě debriefingem k aktuální podobě firemního partnerství.
V mnohém to bylo podobné, protože obě firmy se mnou spolupracují na 1:1 mentoringu v klubu.

Na základě zpětné vazby mi dává smysl do budoucna změnit, jak mentoring funguje.
Nyní se junioři s mentory domlouvají napřímo a nemám nad tím prakticky žádnou kontrolu, žádný vhled.
Nemohu se tím pádem starat o kvalitu a životní štěstí ani jedné ze stran.
Nejsou jasná očekávání a i pokud jsou někde napsaná, lidé je ne vždy respektují, nebo si je uvědomují.
Individuální mentoring poskytovaný dobrovolníky je možná až příliš dobrá nabídka na to, že to je dostupné všem v základní sazbě za klub a u juniorů to přispívá k tomu, že si této nabídky někdy dostatečně neváží.
Junioři přicházejí s jednorázovými problémy či úkoly, jsou na schůzky nepřipravení, nebo vůbec netuší, co od toho celého chtít.
Mentoři netuší, zda mohou někoho odmítnout a jak, někdo nemá dostatečně silné osobní hranice a souhlasí pak se vším, ale je mu z toho následně smutno.

Řešení, které mě zatím napadá, je zavést přihlašovací formulář, podobně jako u stipendia.
Junior do několika políček popíše, jaké jsou její nebo jeho cíle, co potřebuje řešit, atd.
Fakt, že bude potřeba vyplnit formulář, odradí lidi, kteří do toho nechtějí vložit žádnou energii.
Formulář také přinutí člověka zodpovědět si položené otázky i sám pro sebe, ujasnit si myšlenky, cíle, motivaci.
Celé to bude působit víc dojmem „jdu se tady přihlásit k něčemu dlouhodobějšímu a vím, co od toho chci“, než jako jednorázová konzultace.

Další věc je, že odpovědi na formulář by padaly do privátního kanálu #mentoři.
Tam by se sami mentoři mohli rozhodnout, zda mají danému juniorovi co nabídnout a v případě zájmu by se ozvali.
Tím by se zajistilo alespoň základní párování.
Junioři nebudou muset psát neznámým lidem podle několika klíčovým slovům a mentoři nebudou muset řešit, že se jim ozval někdo, komu vlastně neumějí pomoci.
Veřejný seznam mentorů v současné podobě by nejspíš úplně zmizel.


## Anketa

Pokračoval jsem ve tvorbě ankety pro juniory, na které pracuji spolu s ENGETO Academy.
Nakonec jsme ale schůzku posunuli na příští týden.

Zmínil jsem se na několika místech, že uvítáme někoho, kdo by nám s tím pomohl.
Dostal jsem díky tomu hned několik kontaktů, koho oslovit.
Tohle je text mého „inzerátu“:

> **Sháním někoho, kdo rozumí anketám, dotazníkům, statistice.** Připravuji za junior.guru a spolu s ENGETO Academy anketu mezi juniory/začátečníky v programování a ocenili bychom před vypuštěním do světa review od odborníka (sociolog, statistik, prostě někdo, kdo nedělá anketu poprvé). Hledám tedy někoho, kdo by rozebral naše naivní představy na kousky a pomohl nám to zase složit dohromady. Jsme schopni za to zaplatit. Pokud máte tip, nebo se hlásíte, napište mi prosím.


## Q&A

Chtěl jsem vyplnit mezeru mezi přednáškami svou vlastní večerní Q&A.
Nestihl jsem to však nijak propagovat a nakonec jsem si z víkendu v Brně přivezl strašnou rýmu, tak jsem to posunul.
Mám připravený [stream na YouTube](https://www.youtube.com/watch?v=vN235cq8xP4) a měl bych teda nějak určit finální datum a začít to propagovat.


## Tipy pro nováčky v klubu (onboarding)

Napadlo mě, jak řešit do budoucna tipy pro nováčky, které jsem programoval velkou část loňského roku a nakonec s nimi narazil na spoustu technických obtíží i na svou vlastní nechuť dál tuhle funkci rozvíjet.
Říkejme tomu třeba verze 1.
Toto je zpráva, kterou jsem napsal moderátorům v rámci přemýšlení nad verzí 2:

> Co kdyby byl jeden kanál typu fórum, kde by byly všechny tipy?
> Buď by je tam spravovalo kuře (má větší schopnosti, např. embedy a tak), nebo bych je tam psal já ručně (jednodušší a rychlejší na psaní a editaci).
> Zakládat nové tipy bych mohl jen já/kuře, lidi by mohli jen číst a komentovat ve vláknech.
> 
> Když by přišel nováček, udělal bych z něj akorát pomyslnou figurku, která by chodila po těch tipech.
> Pořadí tipů bych měl tímhle pod kontrolou bez ohledu na to, kdy byly napsány. Implementace „chození“ mě napadly dvě:
> 
> 1.  Kuře by mu udělalo v ten den mention do vlákna pod konkrétní tip, tím by mu přišla notifikace.
      Pak by tu zprávu hned smazalo, ale notifikace by přišla.
> 2.  Kuře by posílalo člověku do soukromé zprávy odkaz na tip, podobně jako teď posílá špendlíky.
      Díky embedu atd. lze vytvořit docela pěkný náhled a odkaz, i když nejsou DM součástí klubu.
> 
> Kdo by si tip přečetl, dal by na něj nějakou reakci.
> Kuře by udělovalo roli „přečetl jsem všechny tipy“ (samozřejmě by ji snadno někdo mohl nafejkovat, prostě by vše poklikal, ale to je jedno).
> 
> **Co by to řešilo?**
> Mnohem méně kódu, mohl bych se komplet zbavit managementu tisíce kanálů pro nováčky na Discordu.
> Existoval by veřejný registr tipů.
> Viděli bychom, zda to lidi čtou a které tipy.
> Lidi by si tipy mohli číst i volně bez ohledu na pořadí, klidně pět najednou, pokud mají chuť. Tipy by šlo ilustrovat obrázky nebo gify.
> Tipy by šlo kategorizovat tagy (Discord, placení, psaní do klubu...).
> 
> **Co by to neřešilo?**
> Zpětnou vazbu od lidí bych sbíral jinak.
> Kanály na tipy na tohle stejně nefungují.
> Už teď jsem jednu z těch otázek dal přímo do checkoutu na Memberful, lidi to vyplňují, když jdou do klubu.
> 
> Nemám úplně vymyšlené, jak by to člověk vypnul, ale možná by prostě jen kuřeti napsal nějakou zprávu (to by vedlo spíš k variantě 2 ).

Líbí se mi, jak některé nápady postupně zrají, když se jim dá čas.
Najednou to někam zacvakne a hned je jasné, jak to má být.
Vidím to teď po několika letech provozu JG na všech frontách.


## Různá vylepšení

Během těch dvou týdnů se mi několikrát stalo, že jsem měl menší chvilku času a chuť programovat.
Využil jsem to tedy k vyřešení několika drobných úkolů, které měly nízkou prioritu:

-   Bot v klubu nyní kontroluje, zda je životnost Discord vláken nastavena na nejdelší možnou dobu.
    Výchozí doba je myslím tři dny, toto způsobuje, že vlákna se sama archivují až po týdnu.
    Při vytváření nových kanálů jsem to vždy zapomínal ručně nastavit.
-   Upravil jsem bota, abych dokázal lépe pracovat s konceptem rodičovského kanálu.
    Od dob, co jsou na Discordu vlákna a teď navíc fóra, mohou být kanály jakoby uvnitř jiných kanálů.
    Bot tohle zatím moc nevnímal.
    Nyní může vypsat do týdenního souhrnu v rámci jakého rodičovského kanálu se téma řešilo, nebo mu mohu říct, že některé kanály nemá vůbec číst, a to na základě ID rodičovského kanálu.
-   Udělal jsem nějaké upgrady závislostí.
-   Začal jsem scrapovat počty svých _followers_ na YouTube a LinkedIn, abych je mohl případně sledovat v čase.
    Musím říct, že ani jedna z těch stránek není moc vlídná k tomu, aby z ní šlo něco programem zjistit, takže se mi tento malý úkol rozložil hned do několika dní.
    Nakonec se mi to ale [povedlo](https://github.com/honzajavorek/junior.guru/blob/e570f9bcf1b7fdf2216ce113d1337b1168ca2f4c/juniorguru/sync/followers.py).
    Čísla si ukládám perzistentně tak, že je [commituji zpátky do repozitáře](https://github.com/honzajavorek/junior.guru/blob/e570f9bcf1b7fdf2216ce113d1337b1168ca2f4c/juniorguru/data/followers.jsonl).
    Jde o JSONL soubor, kam se vždy přidá nový záznam pro nový měsíc.
    Až toho bude víc, dám to na [/open/](https://junior.guru/open/).
-   Používám Fakturoid a mám ho napojený na bankovní účet, aby pároval faktury s transakcemi a automaticky je uměl označit jako zaplacené.
    Problém je, že od začátku JG mi na účet chodí i spousta věcí, které fakturu nemají.
    Dobrovolné příspěvky.
    Členství v klubu.
    A tak dále.
    Upozornění o nespárované platbě jsou jen upozornění a mohl bych je snadno všechny označit jako přečtené a neřešit je.
    Chtěl jsem nad tím však mít větší kontrolu a zachytit případné podezřelé platby.
    Na JG mám už dávno skript, který mi stahuje transakce z účtu na Fio a kategorizuje je.
    Stačilo tedy přidat něco, co se podívá i na Fakturoid a upozornění související se známými transakcemi by označilo jako přečtené.
    Tento úkol jsem rovněž očekával jednodušší a roztáhlo se mi to na několik dní.
    Zjistil jsem, že API Fio banky nejspíš vrací částky v JSONu jako float, místo aby je poslalo jako string a šlo z toho udělat [decimal](https://docs.python.org/3/library/decimal.html) a následně deterministicky porovnat částky.
    Chtěl jsem kvůli tomu [předělat celou svou knihovnu](https://github.com/honzajavorek/fiobank), ale nakonec jsem si v tom zabránil, nechal změny ležet na disku a vymyslel jiný způsob, jak to celé řešit.
    Nakonec jsem vyřešil ještě pět jiných zádrhelů, kvůli kterým se transakce nepárovaly s upozorněními ve Fakturoidu.
    Už to nicméně funguje.
    Objevil jsem díky dvě nebo tři podivné transakce, ale všechny měly nějaký dobrý důvod (např. vrácené daně z FÚ).
    Účel to tedy plní.
    Mimochodem, API Fakturoidu je [zdokumentováno v Apiary](https://fakturoid.docs.apiary.io/), kde jsem dřív pracoval.
    Zamáčkl jsem slzu.


## Další

-   Předplatil jsem si svého oblíbeného tvůrce podcastů.
    Uvědomil jsem si, že od něj poslouchám (nebo jsem poslouchal) snad už deset různých podcastů.
    A že chodím na jeho web, když chci vědět, co je ve světě nového.
    Nemá Patreon ani HeroHero, ale nějaký [svůj formulář](https://poplatek.rozhlas.cz/).
    Naklikané to však bylo rychle a vygenerovalo to QR kód, který jsem hned zaplatil mobilní appkou své banky.
    Jde to zaplatit na rok dopředu, vychází to na pár stokorun.
    To mi přijde jako směšná cena za to všechno, co využívám.
-   Poladil jsem barvy rolí v klubu, aby se nepletli lidi, kteří hodně pomáhají a moderátoři.
    Zdokumentoval jsem v klubu na nástěnku nějaké nové dobrovolné role, které jsem nedávno přidal.
-   Poslal jsem konečně daňařovi podklady pro přiznání.
-   Green Fox Academy se zeptali, zda by mohli do klubu posílat studenty.
    Napsal jsem jim, jak to funguje.
    Doteď jsem měl tohle jen se Software Development Academy a stále nevím, zda je to funkce, kterou bude chtít víc firem, nebo mám ten kód smazat.
    Jsem zvědav, zda se jim to bude líbit a půjdou do toho.
-   Dělal jsem promo nové epizodě našeho [podcastu](https://junior.guru/podcast/).
    Mě se epizoda s Tomášem Ervínem Dombrovským moc líbila a zřejmě jsem nebyl sám.
    Na LinkedIn to [mělo celkem dost sdílení a interakcí](https://www.linkedin.com/posts/honzajavorek_deeptalks-data-trh-activity-7035958087731544064-DQze).
-   Snažil jsem se po kouskách dělat pořádak v rodinných a osobních financích.
    Počítal jsem si zpětně složený úrok p.a. z několika bizarních podílových fondů, jež jsem si kdysi dávno zřídil.
    Ani s kalkulačkou na [WolframAlpha](https://www.wolframalpha.com/), která umí komplexní čísla a všemožné rovnice, se mi to ale nepovedlo.
    Nicméně jsem mnohem lépe pochopil, jak to celé funguje, a co bych měl s fondy do budoucna udělat.
    Zrušil jsem účet na Revolut a vše přesunul k Wise.
    Nakoupil jsem nějaká Eura na dovolenou, protože jsou teď levná.
-   Byli jsme v Brně na prodloužený víkend.
    Klasicky [vlakem]({filename}2021-08-28_bez-auta.md), tentokrát jsme vzali i kočár.
    Měli jsme strašně nabitý program jak jsme se snažili vidět co nejvíc kamarádů a rodiny a stihnout co nejvíc akcí (běh, [Sendivč](https://www.hrasendvic.cz/), [koncert](https://www.artbar.club/events/mutanti-hledaj-vychodisko-don-juan-disco)).
    Myslím, že jsme to trochu přehnali a měli jsme si to dát víc lážo plážo.
    Místy utrpělo naše zdraví i psychika.
-   Účastnil jsem se uživatelského testování appky [RichBull](https://richbull.co/), nového nástroje pro trackování investic.
    Dělá na tom kámoš a držím mu s tím palce.
-   Propagoval jsem v klubu kurz pro začátečníky, který v Praze organizuje Pure Storage.
-   Zase jsem někde [prosil o RSS](https://twitter.com/honzajavorek/status/1632675967859605506).
    Pokud vám stačí e-mail, odebírejte, vypadá to fajn.
-   Udělal jsem po delší době zálohu fotek a systému.
    Dokončil jsem [program](https://github.com/honzajavorek/isublime), který mi umožňuje nahrávat soubory na iCloud tak, že to vypadá, jako by je tam dalo jiné zařízení.
    To mi dovoluje nahrát tam spoustu archivních souborů, které si můj počítač stahuje až podle potřeby.
    Program je strašně pomalý a knihovna [pyicloud](https://github.com/picklepete/pyicloud/), nad kterou je postavený, má spoustu chyb, ale nějak to funguje a pár souborů jsem si takhle už „zazálohoval“.
-   Udělil jsem hned několik stipendií a další na mě čekají v e-mailu.
-   Užil jsem si první závod letošní sezóny F1.
    Alonso je borec!
-   Odpovídání v klubu, e-maily, [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), atd.
    Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
-   Během 15 dní od 24. 2. do 10. 3. jsem naběhal 25 km, při procházkách nachodil 14 km. Celkem jsem se hýbal 12 hodin a zdolal při tom 39 kilometrů.
    Část z těch naběhaných kilometrů byl [závod](https://gici.behaj.cz/bbp-9-2023-beh-kolem-myslivny/).
-   Finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).
    Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)


## Povedlo se

Udělal jsem něco z [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md)?

-   „Vylepším zobrazení inzerátů na Discordu“ v podstatě hotovo!
-   „Přidám Jobs.cz“ v podstatě hotovo!
-   Dělám na „Budu se podílet na anketě mezi juniory“
-   Dělám na „vymýšlení MVP s tipy pro nové členy v klubu“
-   Blížím se k „Rozjedu pravidelné Q&A pro komunity“
-   Blížím se k „Pohraju si s AI“


<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví.**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>


## Plánuji

1.  Rozplánovat přednášky a Q&A, promovat svoje Q&A.
2.  Kontaktovat 5 firem, kterým má brzo končit členství a dořešit prodlužování nebo loučení.
3.  Vytvořit nové plakáty na podcast a implementovat označení epizod, pokud jde o „spolupráci“.


## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel toto:

- [Řež u Bachmutu. „Rusové můžou na každého z nás vystřelit stokrát. My musíme trefit vždycky“ - VOXPOT](https://www.voxpot.cz/rez-u-bachmutu-rusove-muzou-na-kazdeho-z-nas-vystrelit-stokrat-my-musime-trefit-vzdycky/)<br>„Západ posílá hlavně vyřazené stroje. Tankům přestane fungovat motor třeba i uprostřed boje. Jeden z velitelů nám ostatně už v dubnu vyprávěl, že protitankové střely NLAW doručené z Británie měly často vadné spouštěcí baterie. Když s nimi voják vyběhl do boje, někdy teprve tváří v tvář tanku zjistil, že systém nefunguje – a s tankem v zádech musel rychle utíkat pryč. „Všechny vaše armády se na Ukrajině zbavují toho, co by už stejně musely vyřadit…“
- [How long does Twitter have left?](https://davekarpf.substack.com/p/how-long-does-twitter-have-left)<br>Otázka není, jestli se Twitter zhroutí, ale kdy.
- [Sú ženy súčasťou našej technologickej budúcnosti? | Petra Kotuliaková | TEDxBratislava](https://www.youtube.com/watch?app=desktop&v=WZ8Qpn7E2EQ)<br>Na Slovensku je 15 % žen v IT. Co bychom za to v ČR dali 😓
- [OnlyFans star Aella on the ethics of pornography](https://www.youtube.com/watch?v=HlW2QdzZuZ8)<br>Zajímavé interview s jednou z nejvíc vydělávajících žen na OnlyFans, o její minulosti, morálce, etice pornografie, směřování pornografie, atd. V nejednom momentě mě překvapilo, jak dobře byl ten rozhovor vedený a jak byly otázky skvěle podány a zacíleny.
- [Artificial Intelligence: Last Week Tonight with John Oliver (HBO)](https://www.youtube.com/watch?app=desktop&v=Sqa8Zo2XWc4)<br>Dobře vysvětleno. A ten Clippy!
- [Text is All You Need](https://studio.ribbonfarm.com/p/text-is-all-you-need)<br>Venkatesh Rao o AI. „This isn’t the world’s elite chess or Go players. This is us in our billions, in a remarkably unflattering mirror, but it is us. The real us.“ Stačí text, abyste druhou stranu vnímali jako osobu. „Either piles of mechanically digested text are spiritually special, or you are not.“  „The fact that we routinely use an apparently impoverished vocabulary of emoji instead of sending authentic facial expression selfies to each other reveals just how textualized personhood is.“
- [Zničené ukrajinské domy či mosty, ale i ruské zákopy. Válečnou zkázu ukazuje srovnání satelitních snímků](https://www.irozhlas.cz/zpravy-svet/ukrajina-satelitni-snimky-valka-krym-lyman-vuledar-severodoneck_2302230650_cib)<br>Srovnání satelitních snímků před válkou a rok poté.
- [Jaký byl sex za komunismu? Kniha otevírá dveře do československých ložnic](https://www.seznamzpravy.cz/clanek/kultura-jaky-byl-sex-za-komunismu-kniha-otevira-dvere-do-ceskoslovenskych-loznic-226655)<br>„Někteří sexuologové a sexuoložky na konci 50. let tvrdili, že se muži mají více zapojovat do výchovy dětí a domácích prací, což mělo být jedinou cestou k ženskému orgasmu. Zároveň ale explicitně varovali před myšlenkou, že se dá kvalitnějšího sexu dosáhnout rozvíjením sexuálních technik. Tvrdili, že sexuální neduhy, a především ty ženské, může vyléčit jedině nové uspořádání rodiny, ve kterém si muž a žena budou rovni, budou si vědomi vzájemných závazků a budou se skutečně milovat… V šedesátých letech však přišel obrat. Pozornost se přesouvá z matky na dítě, jeho psychickou pohodu. Čím dál častěji je vyzdvihována role matky a obecně nastává návrat k tradičnímu pojetí rodiny a genderu.“
- [Noční ulicí kolem popraviště. Nová sezona F1 je rekordní ve sportovních i politických ohledech](https://www.irozhlas.cz/sport/nocni-ulici-kolem-popraviste-nova-sezona-f1-je-rekordni-ve-sportovnich-i_2303030630_ksp)<br>F1 už dnes!
- [In defense of prompt engineering](https://simonwillison.net/2023/Feb/21/in-defense-of-prompt-engineering/)<br>Bude nebo nebude prompt engineering reálná pozice a kariéra?
- [Jak Ukrajina vyhrává informační válku](https://markething.cz/jak-ukrajina-vyhrava-informacni-vojnu)<br>Ukrajinská propaganda.
- [Obrazem: Prostranství před brněnským nádražím se promění, práce začnou v březnu - Zdopravy.cz](https://zdopravy.cz/obrazem-prostranstvi-pred-brnenskym-nadrazim-se-promeni-prace-zacnou-v-breznu-146396/)<br>Konečně. Proč to trvalo nekonečně dlouho?
- [Pod čarou: Města jsou velká a plná lidí. Prostě se s tím smiřte.](https://seznam-zpravy.u.mailkit.eu/mc/VUQVVPIW/DEQZYFBVAWUQDSLBJP/CUULVWECWMM)<br>„Iracionální láska k automobilismu je ale jen jedním z mnoha projevů myšlení, které zhoršuje život ve velkých městech a brání jejich rozvoji. Řada lidí totiž města a s nimi spojený životní styl ve skrytu duše nesnáší, a i když v nich musí dobrovolně či z donucení pracovat a pobývat, odmítají se podvolit jejich vnitřní mechanice a všude si s sebou nosí jakousi mentální vesnici.“
