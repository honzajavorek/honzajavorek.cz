Title: Týdenní poznámky: Katalog kurzů a úklid v Trellu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-05-08_tydenni-poznamky-propojeni-katalogu-s-partnery-stable-diffusion.md) už utekl nějaký ten týden (8. 5. až 12. 5.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Glance Media](https://junior.guru/jobs/b5bb05d439c71b800ca520b63c5ae9ab261d10d19681ff2bc2acce0c/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Katalog kurzů

Tento týden se mi na rozdíl od předchozího povedlo s katalogem docela pohnout vpřed 💪

-   Do katalogu jsem přidal [Programko.NET](https://junior.guru/courses/programkonet/), [CS50](https://junior.guru/courses/cs50/), [Lovely Data](https://junior.guru/courses/lovelydata/), [Škola kódu](https://junior.guru/courses/skolakodu/).
-   Partnerské firmy mají v seznamu kurzů odkaz, který nemá _nofollow_, takže jim to zlepší SEO.
-   Obarvil jsem partnerské firmy v seznamu kurzů i na podstránkách.
    Vysvětlil jsem tam, co to znamená, že firma je partnerská.
-   Propojil jsem seznam kurzů s podstránkami, takže když se teď v seznamu klikne na nějaký kurz, člověk je stále na junior.guru a až tam se dá prokliknout na samotnou webovku kurzů.
    Na podstránce zatím nic moc není, ale chci tam postupně doplňovat různé informace.
-   Předělal jsem, jak můj kód dělá screenshoty, nebo řekněme jak zjišťuje, jaký screenshot jaké URL má udělat.
    Potřeboval jsem to proto, že poprvé mám na webu kartu se screenshotem (web kurzu), která ale odkazem vede jinam (na podstránku).
    Předtím můj skript v podstatě scrapoval moje vlastní vygenerované HTML a hledal v něm karty s odkazy.
    Teď jsem to udělal explicitnější, přes `data-` atributy v HTML, kde mohu přesně specifikovat, co chci aby se dělo.
-   Vymyslel jsem ceník pro vzdělávací agentury.
    Ceník mám dlouhodobě v Google Docs, takže jsem jen šel do dokumentu a upravoval ho, dokud se mi to nelíbilo.
    Původně jsem se snažil [myslet na Levelse](https://twitter.com/levelsio/status/1430876859885969413), ale [nakonec je to mnohem jednodušší](https://junior.guru/pricing/).
-   Hned jsem to poslal všem vzdělávacím agenturám, se kterými jsem se v minulosti o katalogu bavil (5 firem).
    S jednou z nich mám zcela nedořešené vztahy a tarif, zůstalo to nějak na půl cesty, takže tam bych to rád dořešil a buď s nimi partnerství ukončil, nebo jej zařadil do jedné ze škatulek.
-   Katalog jsem poslal i Yablkovi, ať na to mkrne a napíše mi, co si o tom vůbec myslí.

![Katalog]({static}/images/screenshot-2023-05-12-at-19-13-08-kurzy-programovani.png){: .img-thumbnail }

## Hledání kanceláře

> Hledám malou kancelář na Žižkově s nájmem kolem 2.000 Kč měsíčně maximálně. Možná by se přidal kamarád, potom bychom se ve dvou složili a mohlo by to být za 4.000 Kč celkem.
>
> Mám minimální nároky, zásuvka, internet, záchod 🙂 Přístup tak, aby nebyl problém přijít v 7 ráno nebo odejít ve 21:00 večer. Stůl bych si asi zvládl sehnat, židli nepotřebuji. Teoreticky by to mohlo být s někým i sdílené, ale ideálně abych si tam mohl bezpečně nechat pár věcí a abych tam občas večer mohl mít nikým nerušený videohovor.
>
> Koukal jsem se po různých coworcích, ale ceny mají vyšší a většinu jejich služeb nevyužiji (hledám spíš klid než lidi).
>
> Nevíte někdo o něčem? Předem díky.

Takhle jsem to napsal [do sousedské skupiny](https://www.facebook.com/groups/praha3/posts/1452151182259027/), no někdo se mi ozval, někdo se mi vysmál.
Uvidím, co z toho bude.
Pokud o něčem víte, dejte vědět.

## Statistiky na prd

Když jsem zkoumal, proč některé grafy na [stránce s čísly](https://junior.guru/open/) vypadají divně, zjistil jsem, že jsem asi o nějaká historická čísla prostě přišel.
Au.

![Příchody]({static}/images/screenshot-2023-04-19-at-13-16-16.png){: .img-thumbnail }

![Odchody]({static}/images/screenshot-2023-04-19-at-13-16-20.png){: .img-thumbnail }

Po zdražení členství jsem si uklízel v administraci a smazal jsem staré tarify.
Tím se mi však povedlo omylem nenávratně smazat historická data, tedy všechny údaje o předplatných navázané na objekty těch tarifů.
Takže grafy přestaly dávat smysl.

Zatím jsem jen ořízl časové osy a věci související s členstvím začínají všechny až v březnu 2023.
Přes administraci Memberful jsem zjistil, že mají kromě evidence tarifů a předplatného i nějakou denormalizovanou časovou osu „aktivit“, která je i v API a asi by z ní nějaké údaje šly zpětně vyčíst.
Jenže to bych teď musel jít a všechny ty statistiky naprogramovat znova.
Takže třeba někdy.

![Příchody po ořezání]({static}/images/screenshot-2023-05-12-at-22-07-35.png){: .img-thumbnail }

## Realtime bot

Mrknul jsem po delší době na [realtime bota](https://github.com/juniorguru/juniorguru-chick/issues) a přidal do něj nové funkce:

-   Když někdo ručně přidá pracovní inzerát pro juniory, bot mu hned dá emoji "ďk".
    Jednak je fajn, když si někdo dá tu práci a do klubu inzerát vloží, jednak se mi to pak lépe rozlišuje od inzerátů, které tam sype samotný bot.
-   Když někdo vloží pracovní poptávku, tzn. popíše kdo je a co hledá, bot mu hned dá emoji s palcem nahoru.
-   Když se někdo představí v kanálu #ahoj, bot okamžitě vytvoří vlákno a přidá tři první emoji jako reakce.
    Ještě by tam časem měla být i nějaká uvítací zpráva, ale to je složitější, chci to celé předělat, takže to zatím dělá pomalý bot jen jednou denně.
    Krůček po krůčku.

## Firmy

Napsal jsem čtyřem firmám, kterým bude brzy končit partnerství s junior.guru.
Zatím odepsala jen jedna.

> Pokud jde o prodloužení partnerství, tak zde mám špatnou zprávu, prodlužovat ho nebudeme. Bohužel se mi z tvého kanálu nedostal do rukou žádný kandidát, kterého bychom připustili do alespoň druhého kola pohovorů a celkově ta kvalita byla spíše horší. To samozřejmě není tvá chyba, jen říkám, jak to je. Úroveň kandidátů, kteří k nám jdou od jinud, je jednoduše výrazně vyšší a stojí nám za investici víc.

Nečte se to dobře, ale je to realita.
Můžeme se bavit o tom, jaké měli nároky a zda jsme se pochopili v tom, jak vypadá úplný začátečník v oboru, nicméně to není jejich problém.
To je můj problém, abych prostě tu _experience_ zlepšil, abych to lépe vysvětlil, a hlavně abych dodal hodnotu.
Abych prodával něco, po čem si firma řekne: „Jo, to bylo dobrý, něco nám to vyřešilo“.
A já časem docházím k názoru, že pracovní inzeráty na juniory tenhle efekt nemají a mít nebudou, i kdybych se na hlavu postavil.

Myslím si, že vím, co mám firmám nabídnout (viz [bermudský trojúhelník]({filename}2022-12-26_strategie-na-2023.md#kurzy)), ale zatím to nabídnout neumím, takže se nedá nic dělat.
Letos mám v prioritách katalog kurzů, tohle holt musí počkat na 2024.
Možná už bude i lepší situace na trhu a bude dávat i větší smysl investovat do toho energii.

Očekávám, že z těch dalších třech firem prodlouží jen jedna, ale nechám se překvapit.
Každá firma do toho šla s jiným očekáváním a z jiných důvodů, takže záleží, jak si to vyhodnotí a kolik peněz mají.
V září jsem zdražoval a měnil ceník tak, abych měl méně firem za víc peněz.
Do toho je [zbrždění trhu, firmy šetří](https://archiv.hn.cz/c1-67168170-zchlazeni-na-trhu-prace-v-it-firmy-jez-pred-rokem-inzerovaly-pet-volnych-mist-nyni-nabizeji-jen-dve).

Tohle všechno se kombinuje dohromady a vychází z toho, že mi dost firem letos partnerství neprodlouží.
Částečně záměrně, takže se z toho nesypu.
Ale zbystřuji, protože už mi neprodloužily i firmy, které by prodloužit chtěly, jen na to prostě teď nemají peníze.
Pokud nebudou nové příjmy díky katalogu a stoupne mi zase režie (zvýšení cen, inflace, energie, teď zase změny v daních pro OSVČ…), tak je otázka, zda mě nečeká nějaký nouzový režim.

Znamenalo by to nechat všeho, co dělám, přitlačit na _sales_, a prostě hledat peníze, kde to půjde, místo abych se zabýval tvorbou hezkých věcí.
Junioři si mě v klubu platí, ale je to „jen“ 52 % mých příjmů.

## Stable Diffusion

Po večerech jsem se naučil nějaké nové věci kolem Stable Diffusion, ale vlastně jsem je na nic zajímavého zatím nepoužil.
Spíš se s tím učím a přemýšlím, co bych s tím mohl vyrobit, ale nějak mi došly vlastně nápady.
Taky hraje roli to, že ty pokročilé věci mi jedou fakt pomalu, takže jsem se zase vrtal v tom, zda to nejde nějak zrychlit.

-   Naučil jsem se základy používání Control Net a prozkoumal trochu víc img2img.
-   Koukal jsem na [How to improve performance on M1 / M2 Macs](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/7453).
    Autor dokonce udržuje nějaký [svůj vlastní fork automaticu](https://github.com/brkirch/stable-diffusion-webui/releases), kde má vylepšení pro Apple zařízení.
    To jsem zatím nezkoušel, ale pokukuju po tom.
-   Dřív se mi nepovedlo rozchodit [tomesd](https://github.com/dbolya/tomesd), možná by to teď šlo.
    Zatím jsem nezkoušel.
-   Ladil jsem výkon a [diskutoval v issues](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/9133#issuecomment-1544511246).

## Úklid v Trellu

Jako další úkol jsem si zadal napsat novou stránku do příručky, která by popisovala, jak si mají lidi vybírat kurzy.
Než začnu, chci si udělat pořádek v poznámkách, které si ukládám k příručce.

Doteď to bylo velké množství sloupců v Trellu podle jednotlivých kapitol.
Přemýšlel jsem, zda na to mít separátní Trello, nebo to dát do Notionu, nebo GitHub Issues.
Nakonec jsem si řekl, že stejně když jdu psát kapitolu, tak si vše nakopíruju do HTML komentáře pod Markdown a pak to postupně zpracovávám, takže to tak prostě rovnou udělám.

Vytvořil jsem si novou stránku pro každou kapitolu, kterou chci do příručky přidat.
Ty, na kterých nic není, nejsou zapojeny do navigace a běžný člověk se k nim neprokliká, ale soubory už tam jsou.
A v těch souborech jsou komentáře a v nich všechny moje poznámky.
U stránky o pohovorech jsem rovnou vyřízl kus z původní příručky a je z toho [tahle nová stránka](https://junior.guru/handbook/interview/).

Do tohoto zdánlivě chaotického a nestrukutovaného, ale mě nejspíš vyhovujícího formátu, jsem zatím přemístil asi deset sloupců z Trella.
Zbývá už jen jeden, kde je ale přes 500 karet.
Potom si chci projít ještě uložené zprávy z Discordu, těch je podle mě přes 100, možná i 200.
To vše si přepíšu do těch HTML komentářů a přetřídím.

Nové poznámky už si budu zapisovat nějak rovnou do těch souborů.
To ještě uvidím.

Abych měl trochu přehled, udělal jsem si nějaké statistiky a dal jsem si je na [stránku s čísly](https://junior.guru/open/#prirucka).
Upřímně si nejsem jistý, jak moc je tento „graf“ užitečný, ale pro začátek asi lepší než nic.

![Statistiky, příručka]({static}/images/screenshot-2023-05-11-at-13-00-13-jak-se-dari-provozovat-junior-guru.png){: .img-thumbnail }

## Další

-   Snažím se prodat lístek na [Festival o psaní](https://festivalopsani.cz/), kam jsem chtěl jít, ale pojedu v tom termínu nakonec na dovolenou.
    Moje cena 1.500 Kč.
-   Udělal jsem konečně [promo na náš poslední díl podcastu](https://www.linkedin.com/posts/honzajavorek_engineering-pohovory-interviews-activity-7061736620999221248-6_Rs?utm_source=share&utm_medium=member_desktop).
-   Dostal jsem pozvánku na [Hacker Camp](https://www.hackercamp.cz/), ale obávám se, že na to vlastně nemám peníze 😀
    No ještě to prozkoumám.
    Myslím, že budu rád, když letos zvládnu [Python sprint](https://blog.python.cz/Letni-sprinty-Python-komunity-v-Msenem).
-   Zdá se, že jsem našel někoho, kdo by mohl dělat rozhovory s juniory.
    Sice je nemám kde publikovat a kdo ví, kolik na to mám vůbec peněz, ale… krůček po krůčku, ono to nějak půjde.
    Tento týden jsem mu konečně předal dlouho slibované podklady.
-   Zjistil jsem, že existuje projekt WhiteNoise.
    Zajímavá je především sekce [Infrequently Asked Questions](https://whitenoise.readthedocs.io/en/stable/#infrequently-asked-questions).
-   Vyměnil jsem si nějaká eura, ať máme čím platit na dovolené.
    Pořídili jsme kočárek golfák, ať máme do čeho na dovolené dát dítě.
-   Účastnil jsem se akce Prague Professional Community o Salary Transparency.
    Je z toho [fotka](https://www.linkedin.com/posts/jeannetrojan_the-prague-professional-community-tackled-activity-7061650300201246720-XroW/).
    Byl jsem tam jediný, kdo narovinu řekl, kolik vydělává 😀
    Chystá se směrnice EU, která má do roku 2025 mimo jiné nařídit, aby všechny nabídky práce uváděly i mzdové rozpětí.
    Některým přítomným to přišlo jako úplné sci-fi.
    Na Slovensku to mají už dávno 😀
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
-   Během 5 dní jsem při procházkách nachodil 3 km. Celkem jsem se hýbal 2 h a zdolal při tom 3 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Dodělat úklid v Trellu.
2.  Psát novou stránku v příručce: Jak si vybrat kurz
3.  Shánět kancelář.

Pokud si budu chtít od psaní odpočinout, tak bych mohl vylepšit vítání členů v klubu a přeskupit v klubu zase trochu kanály.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Leaked Google document: “We Have No Moat, And Neither Does OpenAI”](https://simonwillison.net/2023/May/4/no-moat/?utm_source=tldrnewsletter&utm_medium=email)<br>„While our models still hold a slight edge in terms of quality, the gap is closing astonishingly quickly. Open-source models are faster, more customizable, more private, and pound-for-pound more capable. They are doing things with $100 and 13B params that we struggle with at $10M and 540B. And they are doing so in weeks, not months.“
- [The World Beyond Ukraine](https://www.foreignaffairs.com/ukraine/world-beyond-ukraine-russia-west)<br>Článek detailně popisuje, jak válka na Ukrajině sjednotila Západ, ale ne svět. Proč? Protože ostatni státy Ukrajina nebo rivalita s Čínou akorát zdržuje od důležitějších věcí. Je to pro ně stejně nedůležité, jako pro nás válka v Jemenu. Západ také ztrácí důvěru tím, jak hodně mluví, ale málo koná. Nebo nastavuje pravidla, ale sám je porušuje. „According to the Economist Intelligence Unit, two-thirds of the world’s population live in countries that are officially neutral or supportive of Russia. These countries do not form some kind of axis of autocracy; they include several notable democracies, such as Brazil, India, Indonesia, and South Africa.“ „The preferred Western framing of the war in Ukraine—as a contest between democracy and autocracy—has not resonated well outside Europe and North America.“
