Title: Týdenní poznámky: Moribundus
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/82


Utekl zas nějaký ten týden (16. 12. až 13. 1.) a tak [stejně jako minule]({filename}2022-12-16_tydenni-poznamky-vymysleni-strategii.md) sepisuji, co jsem dělal a co jsem se naučil.
Tvořím [junior.guru](https://junior.guru/) a nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/) a členy by mohlo zajímat, co dělám.
Psaní poznámek mi taky pomáhá nezbláznit se a nepropadat pocitu, že je konec týdne a já jsem nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


Nejdřív onemocněl zbytek rodiny, pak došlo i na mě.
Poznamenalo to celé moje Vánoce a až tento týden jsem dobral antibiotika.
Začalo to jako viróza, pak se to chovalo jako zánět dutin a skončilo to jako zánět průdušek.
Některé dny jsem celé nehybně proležel, takže na konci poznámek najdete nezvykle hodně přečtených článků.


## Strategie

V první části nemoci, která nebyla tak hrozná, jsem sepsal [strategii na rok 2023]({filename}2022-12-26_strategie-na-2023.md).
Mělo to být pár odrážek, ale dopadlo to jako vždycky.

V souvislosti s tím jsem si dělal povrchní úklid v Trellu.
Měl bych to však ještě dotáhnout a Trello vyvětrat pořádně.


## Úpravy na blogu

Ve volných chvílích jsem se mazlil tady s blogem.
Netušil jsem, kolik práce dá [udělat nový favicon](https://dev.to/masakudamatsu/favicon-nightmare-how-to-maintain-sanity-3al7), ale budiž.

![Nový favicon]({static}/images/screenshot-2023-01-14-at-13-47-00.png)
Rozdíl v kvalitě faviconu junior.guru a mé webovky je teď propastný!

GitHub mi odmítá spouštět actions u commitů poslaných z actions.
Takže když se přidá odkaz na Telegram a commitne zpátky do repa, nedeployne se blog.
To by měl řešit [PAT](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic), ale nefunguje mi to.

Taky se mi nezobrazuje náhled článků, které dám do [své Telegramové skupiny](https://t.me/honzajavorekcz) přes bota.
Nezjistil jsem, jak to řešit.
Mohu to ručně poslat na [@WebpageBot](https://t.me/WebpageBot), ale to není to, co si představuji pod slovem _automatizace_.
Bot nemůže psát jinému botovi, takže ten to neudělá.
Zkouším trik, že by to bot nejdřív poslal do soukromé zprávy mě a až za několik sekund do skupiny.
Zda to funguje, zjistím, až vydám tento článek.

Povedlo se mi díky supportu MailChimpu [vytvořit RSS kampaň](https://us14.admin.mailchimp.com/customer-journey/#/create-campaign/explore/emailCampaign:custom).
S pomocí [merge tags](https://mailchimp.com/help/rss-merge-tags/) a [různých návodů](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) se mi povedlo něco nastavit.
Formulář jsem chtěl mít v češtině, ale MailChimp tam má jen nějaký hrozný automatický překlad, tak jsem si to [přeložil ručně](https://mailchimp.com/help/translate-signup-forms-and-emails/).
Přihlásit k odběru se můžete tlačítkem nahoře na [úvodní stránce blogu](https://honzajavorek.cz/blog/).
Udělalo to už 15 lidí.
Je to zatím pouze pokus, tak jsem to moc nepropagoval.
Zda a jak to funguje, zjistím, až vydám tento článek.
Celé mi to taky pomůže do budoucna vymyslet newsletter pro junior.guru.


## Zdražení

Chtěl jsem do konce roku zdražit klub členům, aby lednový nápor už proběhl za nové ceny.
Nakonec jsem to dělal na poslední chvíli, když mi zrovna bylo chvíli líp.

Vybral jsem cenu **199 Kč měsíčně**.
K tomu, abych šel s novou cenou na vrchní hranici zvažovaného rozsahu, mě motivovali sami členové.
Udělal jsem si aspoň základní propočty.
Protože zdražuji v podstatě na dvojnásobek, musela by odejít polovina členů, aby se mi to nevyplatilo.

Někdo mi chtěl v minulosti platit víc než kolik stálo členství, protože mě chtěl podpořit.
Experimentuji tedy s tím, že lidi s měsíční platbou [mohou zadat i vyšší číslo](https://memberful.com/help/plans-and-products/enable-choose-what-to-pay/).

Vše jsem diskutoval v klubu a také jsem všem členům poslal e-mail, kde jsem se snažil změnu vysvětlit.
Stávající členové mají možnost koupit si roční členství za původní cenu.
Starou cenu mají i na měsíčním členství, a to do února, kdy je převedu na nové tarify.

Na Silvestra jsem na webu změnil ceny, některé texty, odkazy.
Přečetl jsem si pro jistotu obchodní podmínky apod. stránky na webu.

![Nové ceny]({static}/images/screenshot-2023-01-14-at-13-48-18-klub-pro-zacatecniky-v-programovani.png){: .img-thumbnail }

Hodně jsem studoval dokumentaci Memberful, třeba [změnu ceny](https://memberful.com/help/plans-and-products/change-plan-price/), [upgrady](https://memberful.com/help/plans-and-products/configure-upgrade-settings/), [přístup zdarma](https://memberful.com/help/manage-your-members/give-free-access/), [hromadné přesunování lidí mezi tarify](https://memberful.com/help/manage-your-members/move-all-members-of-a-plan/).
Doteď si nejsem jistý, zda při přesunu lidi nepřijdou o kupóny.
To by byl pro mě dost problém.

Napadlo mě, jestli by nešlo stipendium kompletně převést z Google formuláře pod Memberful.
Bohužel [custom fields](https://memberful.com/help/customize/create-custom-fields/) jsou pro všechny tarify totožné, nelze udělat jinou sadu otázek pro speciální tarif.

Chvíli jsem se snažil stipendium do toho formuláře na Memberful nacpat, než jsem zjistil, že je to hloupost.
Díky tomu jsem aspoň všechny texty a otázky ve stipendiu zkrátil a zjednodušil.

Také jsem aspoň přidal ke všem tarifům dotaz na to, kde lidi přišli na junior.guru.
Skvělé je, že se to lidem objeví k vyplnění hned po registraci, takže si to nejspíš budou ještě pamatovat.
Je to otevřená otázka, což znesnadní zpracování, ale umožní to lidem napsat věci svými slovy.

![Otázka po registraci]({static}/images/screenshot-2023-01-14-at-13-49-35-customize-custom-fields.png){: .img-thumbnail }

Udělal jsem úklid v kupónech a pročistil lidi, kteří měli vstup zdarma díky podpoře přes GitHub nebo Patreon, ale kteří mě tam již nepodporují.
Zrušil jsem kupóny firem, které neprodloužily partnerství.


## Jak lidi nacházejí junior.guru

Než jsem přidal otázku po registraci, která u nových lidí zjišťuje, kde našli junior.guru, zkusil jsem v klubu udělat jednoduchou anketu.
Výsledky mě překvapily, jelikož úplně nekopírují moje dojmy, na kterých jsem založil svou novou [strategii na marketing]({filename}2022-12-15_moje-nova-strategie-na-socialni-site.md) 😀

![Anketa]({static}/images/screenshot-2023-01-14-at-13-58-16.png)

Výsledky ankety ale nelze číst přímočaře.
Jednak odpovídali lidi, kteří v klubu už jsou, a to třeba i déle než rok.
Někdy si ani nepamatují, jak to přesně bylo.
Moje strategie tehdy a dnes se dost liší.

Také mi nikdo neřekne, že junior.guru objevil přes newsletter nebo Q&A, když newsletter nemám a Q&A nedělám.
Dokud to nevyzkouším, tak nezjistím, zda to nahradí nebo překoná Twitter či Instagram.
LinkedIn tam vychází slabší než ostatní sítě, ale zase nehlasovalo tolik lidí, abych mohl něco vyvozovat z rozdílu dvou hlasů.
Na své strategii tedy měnit zatím nic nebudu a nechám se překvapit.

Že mě nejvíc lidí našlo přes příručku, potvrzuje, že bych se měl soustředit na SEO a Google.
Čekal jsem však, že bude v klubu mnohem víc těch, kdo mě našli přes hledání kurzů nebo inzerátů práce.
Stránky kurzů mají dlouhodobě velkou hledanost i návštěvnost a pamatuji si nové členy, kteří přes ně jednoznačně přišli.
Je možné, že sice přišli, ale nezůstali?
Mohlo by to znamenat, že na kurzy sice chodí hodně lidí, ale není to pro klub kvalitní návštěvnost ke konverzi.
Ovlivní to nějak můj nový produkt, katalog kurzů?

Zajímavé také je, že lidé chodí hodně přes podcasty, ale ne ty naše 😀
Pamatoval jsem si, že hodně lidí zmínilo, že přišlo „přes podcast“ a já automaticky předpokládal, že přes náš.
Z ankety to spíš vypadá, že dobře funguje, když se nechám pozvat do jiných podcastů, ale nejspíš není mnoho lidí, kteří junior.guru našli přes junior.guru podcast.
Mám tedy v roce 2023 do našeho podcastu investovat tolik energie, kolik jsem si naplánoval?

A překvapilo mě, kolik lidí mě objevilo díky [yablkovi](https://robweb.sk)!


## Grafy

Mojí již tradiční vánoční kratochvílí je vylepšování [stránky s čísly a grafy](https://junior.guru/open/).
Když mi zrovna bylo lépe, hrál jsem si s barvičkami, upravoval texty, vylepšoval zobrazení.

-   V souvislosti s novými finančními cíli jsem změnil _progress bar_ na tabulku se smajlíky.
-   Udělal jsem grafy [responzivnější](https://www.chartjs.org/docs/latest/configuration/responsive.html), aby se daly číst i na mobilu.
-   Našel jsem zajímavou knihovnu [chartjs-plugin-datalabels](https://chartjs-plugin-datalabels.netlify.app/samples/charts/line.html), ale nakonec jsem ji nepoužil.
-   Použil jsem [chartjs-plugin-annotation](https://www.chartjs.org/chartjs-plugin-annotation/latest/guide/types/box.html).
    Umožnilo mi to na grafy přidat svislé čáry pro různé milníky v historii junior.guru.
    A přidal jsem i čárkované označující přelomy let.
    Dalo to nečekaně dost práce, hlavně umístění popisků a volba barev, aby to nebyl úplný chaos.
-   Do grafu **Členství v klubu** jsem přidal počet ročních individuálně placených předplatných.
-   Přidal jsem sekci **Aktivita v klubu**, kde je graf počtu příspěvků v klubu a počet online akcí v klubu.
    První mi pomůže sledovat, zda klub žije méně nebo více.
    Druhý mi umožní hlídat, zda plním svůj cíl zajistit v průměru dvě oficiální akce měsíčně.
-   Předělal jsem, jak se odhaduje počet žen v klubu.
    Místo pevného seznamu křestních jmen si nyní bot stahuje [tabulku z Wikipedie](https://github.com/5j9/wikitextparser a https://cs.wikipedia.org/wiki/Seznam_nej%C4%8Dast%C4%9Bj%C5%A1%C3%ADch_%C5%BEensk%C3%BDch_jmen_v_%C4%8Cesku).
    Graf podílu žen v klubu jsem už měl, ale přidal jsem graf podílu žen mezi přednášejícími na oficiálních akcích.
    Umožní mi to hlídat, zda mám za posledních 12 měsíců 50% podíl žen mezi přednášejícími, nebo je to jinak.
-   S novou verzí chart.js jsem objevil chybu v annotation pluginu a [založil jsem issue](https://github.com/chartjs/chartjs-plugin-annotation/issues/831).
-   Přidal jsem do grafů barvičky pro výdaje spojené s produkcí video záznamů.
    Také jsem do samostatné barvy vyčlenil lidi, kteří mají vstup do klubu zdarma díky tomu, že mi pomáhají.
    Například [Pavlína](https://junior.guru/podcast/), moderátoři, atd.
    Nazval jsem to „tým junior.guru“.

![Náklady]({static}/images/screenshot-2023-01-14-at-15-45-16.png){: .img-thumbnail }


## Discord a Memberful

-   Discord už dlouho umožňuje propojit svůj účet s účty na jiných službách, ale nyní to vylepšují a [lákají na to platformy](https://discord.com/build/linked-roles).
    Většinou jde o hry, hudbu, apod.
    Mohu např. nastavit, že kdo má nějaké úspěchy při hraní Diabla, bude mít na mém serveru automaticky nějakou roli.
    Dovedu si představit, že pro hry je to hodně dobré, ale zatím nevím, jak bych to využil.
    Připojit jde GitHub, tak jsem na zkoušku udělal roli pro ty, kdo si profil propojili, ale nedá se tam využít žádná další data, např. dát speciální roli někomu, kdo má aspoň 3 repozitáře.
    LinkedIn propojit nejde.
-   Našel jsem další a další nedokonalosti v tom, jak fungují tipy pro nové členy v klubu.
    Ať už technického rázu, nebo co se týče uživatelské použitelnosti.
    Přemýšlel jsem jak to napsat, ale napíšu to stručně:
    Ty tipy už mě serou.
    Musím vymyslet, co s nimi, rychle to udělat a posunout se na další věci.
-   Do budoucna jsem uvažoval o tom, že kdo by do klubu doporučil nového člena, dostal by nějakou výhodu.
    Jedna možnost je sleva, jiná možnost je dárek.
    Slevy jednak dávat nechci, jednak by se to bilo s mojím systémem kupónů, takže i když [to má přímo Memberful](https://memberful.com/help/analytics-and-tracking/track-member-referrals/), nemohu to snadno použít.
    Napadlo mě, že jako dárek by se dalo tomu člověku zaplatit [Discord Nitro](https://discord.com/nitro).
    Je to ale dost drahé, takže maximálně tak na měsíc 😬
-   Memberful přidal a hned všem zapnul tzv. [cancellation surveys](https://memberful.com/product-updates/cancellation-survey/).
    Když někdo ruší předplatné, hned se jich ptá, proč to dělají.
    Možnosti odpovědí nemohu měnit, ale lepší bych stejně nevymyslel.
    V administraci mám pak statistiku.
    Díky tomu jsem už zahlédl hned dva lidi, kteří zrušili členství kvůli tomu, že je drahé, a mohl jsem je kontaktovat a doptat se jich na další informace.
    Dovedu si představit, že časem napíšu automatizaci, která mi ty zajímavější odcházející klienty pošle na Discord do privátního kanálu, kde se o tom hned dovím.


## Hry

Když mi bylo líp, dostal jsem chuť zahrát si hru.
Zkusil jsem přes PlayOnMac nainstalovat na tisící pokus svou starou oblíbenou hru [Original War](https://www.youtube.com/watch?v=tH4U0EEczFg), ale opět se mi nepovedlo to dotáhnout.
Pak jsem zkoušel přes `brew install widelands --cask` nainstalovat Widelands, ale několikrát se to nepovedlo.
Nainstaloval jsem to ručně a jelo to, ale už během tutoriálu mi to několikrát náhodně spadlo, tak jsem to vzdal.

Dostal jsem chuť na novou hru.
Nejlépe něco, co má příběh a bude to víc jako film a míň jako sto let stará RTS, kde něco buduju.
Půl dne jsem koukal na upoutávky ke hrám.
Prošel jsem si pár seznamů nejlepších her, které jedou na macOS a pár věcí mě zaujalo:
Life is Strange, Knights of the Old Republic, Company of Heroes, Hitman, Cities: Skylines, Cuphead, The Elder Scrolls, Hollow Knight, Her Story, Rise of the Tomb Raider, Kingdoms and Castles, Old World, Shadow of the Tomb Raider, Timberborn, Hades, Crusader Kings.

![Life is Strange]({static}/images/capsule_616x353.jpg)

Nakonec jsem si na hodinu zahrál Life is Strange a strašně mě to bavilo.
Dokonce jsem kvůli tomu i vyhrabal a zapojil myš!
Ale druhý den už jsem začal pracovat a od té doby jsem si to neotevřel.


## Objevy

-   Prošel jsem si služby, které při podnikání využívám (např. Memberful, Fakturoid…).
    Pro každou jsem našel jejich produktový blog s novinkami a ten jsem si přidal do RSS čtečky.
    Už jsem díky tomu objevil hromadu zajímavých funkcí.
-   Poslouchal jsem [Změny a strategie Czechitas 2023](https://www.youtube.com/watch?v=YcI7HDqErtQ).
-   Hledal jsem, zda existuje doplněk do MkDocs, který by z emoji udělal obrázky, které se všude zobrazí stejně.
    Nakonec jsem se [zeptal](https://github.com/mkdocs/mkdocs/discussions/3082).
    Díky tomu jsem objevil [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/), což je sada doplňků pro Markdown, která vypadá fakt nabušeně!
-   Kamarádi z Afriky sepisovali články o tom, jak se jim líbilo v Praze:
    [Ngazetungue Muheue](https://ngazetungue.hashnode.dev/my-time-in-prague-for-the-ubuntu-summit-2022),
    [Abigail Mesrenyame Dogbe](https://mesrenyamedogbe.hashnode.dev/my-experience-at-the-ubuntu-summit-2022).
    Co mě zaujalo?
    Slovo _hashnode_ v adrese obou těch blogů.
    Možná jsem poslední člověk na světě, který to objevil, ale vůbec jsem nevěděl, že něco jako [Hashnode](https://hashnode.com/) existuje!
    Hned jsem to prozkoumal a vypadá to jako zajímavá platforma na technicky zaměřené blogísky a nejen to.
    Znali jste to?
    Používá to někdo v Česku?
-   Několikrát mi lidi doporučovali knihu [Company of One](https://www.goodreads.com/book/show/37570605-company-of-one).
    O Vánocích jsem ji už málem koupil, ale pak jsem si přečetl recenze a pochopil jsem, že mě osobně by nejspíš vůbec nic nedala.
-   Abych dokázal dobře rozjet newsletter, začal jsem to trochu studovat.
    Přidal jsem si do RSS čtečky [newslettery.cz](https://newslettery.cz/) a celé jsem to sjel i s podcastem.
    Pak jsem objevil Tvůrcast a až po pár dílech mi došlo, že [to má stejného autora](https://navolnenoze.cz/novinky/tvurcast/) 😀


## Bráchova přednáška v klubu

Před časem se mi brácha, analytik v bance, nabídl, že juniorům v klubu odpřednáší o této své profesi.
Přišlo mi to jako super nápad a 10.1. přednáška v klubu proběhla.

Opět mi záznam zajišťoval pomocník Tinuki a bylo to úžasné.
Opravdu si užívám, že mohu jen moderovat a nemusím řešit streamování a záznam.
Na jednotlivé přednášky jsem se začal zase těšit, stres úplně zmizel.

Bráchu jsem před přednáškou trochu víc než obvykle promoval v klubu i [na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7018240804745789440/).
Myslím, že to lidi trochu vyhajpovalo a došli v hojném počtu.
Nebo se jenom chtěli podívat, jak vypadají dva Javorci vedle sebe.
Přednáška se protáhla na dvě hodiny, ale měla úspěch a já z ní mám velkou radost.

![brácha]({static}/images/1673278998985.png){: .img-thumbnail }

Po přednášce mi spadl CircleCI build, protože seznam záznamů klubových akcí přesáhl limity Discord zpráv na počet písmenek.
To jsem nečekal, i když zpětně je logické, že jednou to přijít muselo.
Jako hotfix jsem [zakomentoval pár starých, méně významných akcí](https://github.com/honzajavorek/junior.guru/commit/12e5f192c536ad6d3b556dda28fab24a1794a894).
Musím ale vymyslet úplně nový způsob, jak budu lidem v klubu záznamy zpřístupňovat.


## Moderátoři

Ve své strategii jsem měl úkol, že v roce 2023 seženu dalšího moderátora.
Zavedl jsem na to řeč v klubu a někdo se mi dokonce i sám přihlásil!
Někoho jsem ještě ukecal a bylo to.
Ani jsem nevěděl jak, najednou je nás moderátorů šest, včetně mně.

Se dvěma z nich, které jsem neznal osobně, jsem si dal krátký seznamovací call.
Musel jsem čistit kanály nebo měnit role v klubu.
Předtím totiž role moderátorů znamenala „jsem jedním ze dvou bohů”, zatímco teď má znamenat „mám oprávnění dělat v klubu o pár věcí víc než ostatní“.
Dva dny jsem opravoval bota, aby se změnami vypořádal a nepředpokládal, že každý moderátor chce například vidět všech 300 kanálů s tipy pro nové členy v klubu, nebo touží aktivně vítat každého nováčka.

Tuto roli jsem zcela oddělil a umožnil lidem, aby si sami zaklikli, že budou „Vítací typ“.
Bot je pak bude automaticky přidávat do vláken, kde vítáme nové členy.
Roli může mít kdokoliv a je samoobslužná, takže koho to už nebude bavit, odklikne se z toho.

Všem moderátorům jsem změnil předplatné tak, aby měli klub zdarma.
To vyústilo v nějaké proplácení peněz zpět na jejich kartu (nevyužité měsíce), nebo v to, že jsem je změnami omylem vyhodil z klubu, či vytvořil kombinaci předplatných, se kterou bot vůbec nepočítal.

Díky [jednomu náhodnému postu na Redditu](https://www.reddit.com/r/discordapp/comments/108xe9e/had_a_moderator_invite_a_bot_to_the_server_which/) jsem si uvědomil, že s vyšším počtem moderátorů vzniká větší prostor pro _attack vector_ nebo lidskou chybu.
V komentářích doporučovali zálohovat klub pomocí [server templates](https://support.discord.com/hc/en-us/articles/360041033511-Server-Templates), což jsem doteď neznal a nikdy nepoužil.
Měl bych bota naučit, aby začal dělat aspoň takovéhle snapshoty klubu.
Snad to [nějak půjde](https://docs.pycord.dev/en/stable/api/models.html#discord.Template).


## Další

-   S jednou firmou plánujeme udělat anketu mezi juniory.
    Ptal jsem se lidí v klubu na co se máme ptát a měl jsem k tomu už dva celkem produktivní meetingy.
-   Sdílel jsem svou strategii na rok 2023 [na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7014987059060690944/) a pak tam vedl diskuze o tom, jestli je to vůbec strategie.
-   Založil jsem skupinu na Telegramu, kde se o podnikání radím s dalšími dvěma kamarády podnikajícími v podstatě nebo úplně sólo.
    Čekám od toho, že se budeme motivovat, radit si, a tak.
    Pokud už něco podobného v Česku existuje, dejte mi vědět, ale já našel jen zahraniční, nebo pro jiný typ lidí.
-   Na [stránce klubu](https://junior.guru/club/) je vždy náhodně pár upoutávek na přednášky.
    Všiml jsem si, že se zobrazují přednášky z budoucnosti, nebo akce, které byly spíš vedlejšími akcemi než přednáškami, na něž bych chtěl někoho lákat.
    Upravil jsem výpis tak, aby promoval jen to, co dává trochu smysl.
-   Obíhal jsem obchody, chodil pro balíky, odesílal dopisy.
    Slavil jsem Vánoce.
    Dostal jsem [dárek od STRV](https://www.linkedin.com/feed/update/urn:li:activity:7012387898507296768/).
    Viděl jsem nějaké pohádky.
    Byli jsme se ženou v divadle na [Válka Roseových nebude!](https://divadlozlin.cz/predstaveni/valka-roseovych-nebude/), zatímco babička hlídala dítě.
    Nový rok jsem spíš promarodil.
-   Prosincové [Pyvo](https://pyvo.cz/praha-pyvo/) bylo v době, kdy už byla rodina nemocná.
    Rozhodl jsem se tam nejít, ač mě to mrzelo.
    Bylo to dobré rozhodnutí, akorát bych to roznesl.
-   Přemýšlel jsem, koho volit, ale zároveň jsem se snažil co nejvíc vyhýbat veškerému cirkusu spojenému s prezidentskou volbou.
    Rozhodování bylo těžké a nakonec jsem si tak trochu hodil korunou.
    Druhé kolo bude snad jednodušší.
-   Napadlo mě, že ač jsem se vždy bránil provozovat v souvislosti s junior.guru cokoliv kontinuálně běžícího, na některé věci by to bylo bez rizika.
    Mohl bych mít někde jednoduchou appku, která by fungovala jako „bezstavový“ bot bez databáze.
    Kdyby spadnul, nic by se velmi nestalo, ale kdyby zrovna jel, zrychloval by u některých věcí odezvu bota v klubu, která je standardně „do 24 hodin“.
    Například vlákna pro nově příchozí by mohl zakládat hned, k tomu žádnou perzistenci nad rámec samotného Discordu nepotřebuje.
-   Četl jsem [Four Thousand Weeks](https://www.oliverburkeman.com/books), ale stále jsem to ještě nedočetl.
-   Propagoval jsem [junior.guru podcast s Lukášem Konarovským z Fakturoidu](https://junior.guru/podcast/).
    Hlavně [na LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7011717833013231616/).
    Pomohl jsem Pavlíně kontaktovat budoucí hosty.
    Bavili jsme se i o budoucnosti podcastu.
-   Stát nám automaticky vytvořil datovou schránku pro Pyvec, z.s.
    Tak dík, no.
-   Na Facebooku se objevila [kritika klubu](https://www.facebook.com/groups/917615511634078/posts/5943298875732358/?comment_id=5943385505723695&reply_comment_id=5945008632228049).
    Členové mě na to upozornili, tak jsem tam šel a vyjádřil jsem se k tomu.
-   Založil jsem support ticket na [Benevity](https://benevity.com/), aby opravili starý název Pyvec, o.s. na Pyvec, z.s.
-   Doporučil jsem [Janu Dolejšovou](https://www.linkedin.com/in/dolejsovajana/) na LinkedIn.
-   Odpovídání v klubu, e-maily, [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), atd.
    Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
    Po nemoci jsem doháněl, co jsem zmeškal a stále mám zhruba 20 nevyřešených záležitostí v e-mailu.
    Celkem hodně lidí mi v poslední době psalo ohledně toho, že se jim nedařilo dostat do klubu nebo kvůli jinému chaosu v účtech, tarifech, placení, apod.
-   Klukům ze svého „běžeckého klubu“ jsem napsal své cíle na letošek:

    1. Běhat pravidelně,
    2. zaběhnout aspoň 2x do roka 20 km,
    3. zaběhnout lepší výsledek v Kozojedech (10 km) a účastnit se aspoň zase Blanska (20 km).

    První cíl bude obtížný dost, takže nemá smysl mířit výš.
    Kdybych se napodzim moc šťoural v nose, lákalo by mě [5BV](https://www.5bv.cz/).

-   Během 29 dní od 16. 12. do 13. 1. jsem při procházkách nachodil 3 km.
    Celkem jsem se hýbal 1 hodin a zdolal při tom 3 kilometry.
-   Finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).
    Aktuální nabídky práce pro juniory: [FYZIOklinika](https://junior.guru/jobs/b264ff2a02a50256a3f79075aa5392af08439d165e138ee99ef2df47/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/215426887eaaad9105ecf647d0ff24cf94de7c9eb47cc6f2c55e6921/)


## Povedlo se

Udělal jsem něco z [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md)? **ANO!**

- Zrealizoval jsem nejjednodušší možný způsob, jak zjišťovat, odkud do klubu přišli lidi.
- Rozjel jsem newsletter, díky kterému lze odebírat tento blog e-mailem.
- Našel jsem další moderátory.
- Zdražil jsem členům klubu.


<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví.**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>


## Plánuji

1. Dořešit vše, co mám v mailu nebo na Discordu.
2. Odjet na hory.
3. Naučit bota vytvářet [zálohy](https://support.discord.com/hc/en-us/articles/360041033511-Server-Templates) klubu.


## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel toto:

- [Lessons Learned from Building Products: The Power of Outcomes over Outputs](https://jukben.codes/lessons-learned-from-building-products-the-power-of-outcomes-over-outputs)<br>O produktovém vývoji z pohledu vývojáře: „I'm a missionary, not a mercenary“
- [Community engagement is so 2022. Here are 10 things you should obsess over instead.](https://rosie.land/posts/dont-obsess-over-community-engagement/)<br>Super souhrn 10 věcí, kterými by se měl zabývat člověk starající se o komunitu (místo měření engagementu)
- [(něco na Twitteru)](https://twitter.com/urbanismu/status/1610924394703982596)<br>ledabylost x kultivovanost (vlákno)
- [The Dark Side of Open Source](https://redd.one/blog/the-dark-side-of-open-source/)<br>Artem, můj bývalý kolega, popisuje, jaké to je stát se správcem úspěšného open source projektu. Co to obnáší? Líbí se mi jeho analogie, nebo důležitý a pro někoho ne úplně zřejmý postřeh, že open source projekt je produkt. A rady kolem toho, aby si člověk nastavil jasné hranice a nenechal se semlít nekonečným seznamem issues: „Everybody wins when the creator is healthy“
- [Students who grew up with search engines might change STEM education forever](https://www.theverge.com/22684730/students-file-folder-directory-structure-education-gen-z)<br>Mladí nechápou koncept složek na počítači. I když je jim to vysvětlováno. Řešení nejspíš není, budoucnost tento technický detail zanedbá. Sestimsmiř! Kdo se adaptuje, přežije.
- [Africa rising](https://www.economist.com/leaders/2011/12/03/africa-rising)<br>„Africa's enthusiasm for technology is boosting growth. It has more than 600m mobile-phone users—more than America or Europe. Since roads are generally dreadful, advances in communications, with mobile banking and telephonic agro-info, have been a huge boon. Around a tenth of Africa's land mass is covered by mobile-internet services—a higher proportion than in India.“
- [Ministerstvo dopravy zpřísní sankce za zablokování MHD špatným parkováním - Zdopravy.cz](https://zdopravy.cz/ministerstvo-dopravy-zprisni-sankce-za-zablokovani-mhd-spatnym-parkovanim-138575/)<br>Tak ještě by to chtělo postihovat zablokování provozu pro chodce na chodníku, pokud nejste stěhováci nebo jeřáb… Pokud se nevyhnou dva kočárky vedle sebe, odtáhnout, pokutovat, zabotičkovat, ale hlavně prostě nějak řešit. Toho se asi nikdy nedočkáme, chodci jsou ten poslední plankton.
- [Africa’s rising cities: How Africa will become the center of the world’s urban future - Washington Post](https://www.washingtonpost.com/world/interactive/2021/africa-cities/)<br>Úžasný longread s mapami a video záběry. Hned několik afrických měst se do roku 2100 stane, pravděpodobně zcela nevyhnutelně, jedněmi z nejlidnatějších měst na světě, nebo přímo nejlidnatější. Znáte je vůbec? Co se v nich děje? Proč tam žije tolik lidí? O uprchlících, migraci v rámci Afriky, válkách, odkazech kolonialismu, vlivu Číny, velkých rozdílech v bohatství, ale i o obyčejných lidech, kteří v těchto městech žijí.
- [Je ostuda, že nás předběhlo Chorvatsko. Hlavní argumenty proti přijetí eura už padly, říká Špicar](https://cc.cz/je-ostuda-ze-nas-predbehlo-chorvatsko-hlavni-argumenty-proti-prijeti-eura-uz-padly-rika-spicar/)<br>„…jestli Česko někdy vstoupí do eurozóny, tak to bude ze zoufalství.“
- [„Nebudu dětem přece lhát.“ Roste počet rodin, které si odmítají hrát na Ježíška - VOXPOT](https://www.voxpot.cz/nebudu-detem-prece-lhat-roste-pocet-rodin-ktere-si-odmitaji-hrat-na-jeziska/)<br>Zajímavé rozšíření obzorů. Naše dítě to zatím neřeší, tak to nemusíme řešit ani my, ale brzy to přijde. Jak to je u vás?
- [ODRAZ 89 - Epizoda 3: „Někteří rodiče pořád chtějí pro děti školu, do jaké chodili oni.“ — Stopáž](https://www.seznamzpravy.cz/sekce/audio-podcast-odraz-89-463)<br>Stav a vývoj českého školství od revoluce. Pěkný rozhovor, ale obávám se, že možná až příliš optimistický…
- [Newey in-depth: Aborted Ferrari switch, Verstappen and retirement - The Race](https://the-race.com/formula-1/newey-in-depth-aborted-ferrari-switch-verstappen-and-retirement/)<br>Rozhovor s nej technologickým borcem ve Formuli 1. Pokud F1 nesledujete, asi vám to nic nedá. Mít v týmu Neweyho je jako kdyby vám s kódem radil Daniel Stenberg, Dave Cutler, nebo Guido van Rossum, akorát že by to asi o polovinu zvýšilo vaše šance na úspěch a porážku všech konkurentů.
- [Prokrastinace jako protijed   — PAVLINA_SPEAKS](https://www.pavlinaspeaks.com/blog/protijed)<br>„Jedna z nejtěžších věcí je být sám a bez úkolů. Čelit vlastním myšlenkám, zabavit se. Telefon si nosíš na záchod, knížku kamkoliv jdeš a partnerské životy zachraňuje Netflix. I chvíle přemýšlecího nicnedělání si zaslouží vlastní strukturu: vyplňuješ Year Compass, bullet journal, gratitude notes.“ ... „Vysněných Keynesových patnáct hodin týdně v práci znamená, že bys sis musel vyplnit těch zbývajících 153 sám.“
- [The moral roots of liberals and conservatives - Jonathan Haidt](https://www.youtube.com/watch?v=8SOQduoLgRw)<br>Zajímavá krátká sonda do toho, jak vnímají svět liberálové a konzervativci a proč to tak je.
- [Povstane nová ekologická třída? Pavel Barša nad posledním textem sociologa Bruna Latoura - Novinky](https://www.novinky.cz/clanek/kultura-salon-povstane-nova-ekologicka-trida-pavel-barsa-nad-poslednim-textem-sociologa-bruna-latoura-40418326)<br>Hutné čtení. „V tomto pojetí zůstává příroda a konkrétně Země stále něčím vnějším člověku a jeho nejdůležitějším aspiracím. Člověk se bez ní neobejde, netvoří však poslední horizont jeho sebeuskutečnění. Když ho donutí ekologické hrozby, může se snažit respektovat hranice, které příroda klade jeho záměrům. Stojí však mimo ni: nežije v ní, ale z ní.“ Nebo „Ekologie již nemůže být pouhým vnějším korektivem ekonomiky, ale celkovou osnovou, v jejímž rámci bude ekonomice přiděleno důležité, ale odvozené a omezené místo.“
- [Pod čarou: Sedmidenní týden není povinnost. Čas může plynout jinak.](https://seznam-zpravy.u.mailkit.eu/mc/VVCVVPVM/CWVPKJHSDADFYPOYCI/CVIILWICEPV)<br>„Standardizace času kvůli průmyslové výrobě nás ovlivnila natolik, že jeho měření už automaticky spojujeme s prací. Dny mohou být jen sváteční nebo pracovní (snad s výjimkou onoho záhadného povánočního týdne), a logika diářů nás nutí dodávat každé hodině nějaký program či výplň – i když spíme, sportujeme nebo se zkrátka jen povalujeme, pořád daný časový úsek „něčím“ vyplňujeme, a nedokážeme si představit čas vnímaný nezávisle na tom, čím dané měřené úseky strávíme.“
- [Annus mirabilis 2023](https://davidklimes.cz/newsletter/132)<br>„Nadchází superdůležitý rok pro Česko a Evropu, ale veškeré výhledy jako by nyní končily u 28. ledna, kdy bude jasný nový prezident republiky. Při vší symbolice a vyšokované pozornosti, kterou nyní na volbu hlavy státu upíráme, rozhodně nejde o to nejpodstatnější, co v roce 2023 budeme řešit. Tak se pojďme podívat, co je skutečně důležité.“
- [My time in Prague for the Ubuntu Summit 2022](https://ngazetungue.hashnode.dev/my-time-in-prague-for-the-ubuntu-summit-2022)<br>Kamarád Ngazetungue Muheue napsal na blog, jak si užil Ubuntu Summit v Praze a čas, který jsme jemu a jeho skupině v Praze věnovali ❤️
- [Definitive edition of "How to Favicon in 2021"](https://dev.to/masakudamatsu/favicon-nightmare-how-to-maintain-sanity-3al7)<br>„I thought adding a favicon to my website was a simple thing. I was wrong.“
- [Vysokorychlostní vlaky dorazily do dalšího španělského regionu - Zdopravy.cz](https://zdopravy.cz/vysokorychlostni-vlaky-dorazily-do-dalsiho-spanelskeho-regionu-137292/)<br>„Dokončením nového úseku přesáhla délka vysokorychlostních tratích ve Španělsku 4000 kilometrů. Více takových tratí má na světě jen Čína.“
- [Strategie na 2023 — Javorové lístky](https://honzajavorek.cz/blog/strategie-na-2023/)<br>Strategie na 2023
- [10 Most(ly dead) Influential Programming Languages](https://www.hillelwayne.com/post/influential-dead-languages/)<br>Krásný výlet do historie
- [Gestalt princip blízkosti v UI designu: Jak ho používá Airbnb nebo Netflix? - Designui.cz](https://www.designui.cz/lekce/gestalt-princip-blizkosti-v-ui-designu-jak-ho-pouziva-airbnb-nebo-netflix)<br>Pěkně vysvětleno, jak pracovat s white space při navrhování. Taková věda za tím, a přitom taková blbost!
- [The Winners and Losers of Energy Transition - The Green Line - Ep 5 — The Red Line](https://theredline.libsyn.com/the-winners-and-losers-of-energy-transition-the-green-line-ep-5)<br>Strašně zajímavý podcast o tom, jak se změní svět spolu s energetickou transformací, které země na to doplatí nejvíc a první, které vydrží. Celá pasáž o tom, jak Ukrajina zásobuje Evropu elektřinou ze svých elektráren a proto na ně Rusko útočí.
- [Autonomous Region of Bougainville](https://en.wikipedia.org/wiki/Autonomous_Region_of_Bougainville)<br>Věděli jste, že v roce 2027 možná vznikne nový stát? Bougainville má na základě referenda přislíbenou nezávislost od Papui Nové Guinei. https://en.wikipedia.org/wiki/Autonomous_Region_of_Bougainville#2019_independenc
- [Cesty Zdopravy - Martin Kupka — Zdopravy Podcast](https://omny.fm/shows/zdopravy/cesty-zdopravy-martin-kupka-1)<br>Zajímavý přehled toho, co se chystá…
- [Těžká výzva pro Slovensko: Proč mladí schopní lidé odcházejí do ciziny a jak tomu zabránit? - VOXPOT](https://www.voxpot.cz/tezka-vyzva-pro-slovensko-proc-mladi-schopni-lide-odchazeji-do-ciziny-a-jak-tomu-zabranit/)<br>Na Slovensku se žije tak „dobře“, že mladí odchází dlouhé roky pryč ze země. Zůstávají staré generace, které však podmínky a stav země nezlepší. Konzervatismus, nepotismus a xenofobie se tím jen zhoršují. Spirála dolů.
- [Navzdory státu jsme rok 2022 zvládli dobře](https://davidklimes.cz/newsletter/131)<br>Denní zpravodajství si otevřu málokdy a pokud, tak hlavně abych zjistil, co se děje na Ukrajině. Povrchní povědomí o tom, co hýbe Českem, získávám každý všední den z podcastu Vinohradská 12. O věcech hluboko pod povrchem a o tom, co se chystá a co je trochu mimo radary, se dovídám čtením newsletteru Davida Klimeše. Odebírejte taky!
- [Nespokojené duše](https://houdekpetr.blogspot.com/2022/12/nespokojene-duse.html)<br>„Čemukoli věnujeme pozornost, najdeme, jak by to mohlo být lepší. Postoj, který bezpochyby stojí za vzestupem lidské civilizace. Zároveň však omezení bránící nám, abychom byli vděčni za to, jaké věci už jsou. A to by vždycky mohly být i mnohem, mnohem horší.“
- [Is web3 bullshit? (Transcript)](https://blog.mollywhite.net/is-web3-bullshit/)<br>Dobře naložila 😀
- [Technologičtí giganti už nechtějí zachraňovat svět. Vítejte ve virtuální poušti - VOXPOT](https://www.voxpot.cz/technologicti-giganti-uz-nechteji-zachranovat-svet-vitejte-ve-virtualni-pousti/)<br>Zajímavé zamyšlení. Ruší mě v něm hlavně to, že vše ilustruje na Facebooku a jeho metaverse, resp. virtuální realitě, a vztahuje to na celou technologickou scénu. Kde je komentář k poblázněné kryptogeneraci kolem web3? Kde jsou v tom zahrnuty pokroky s AI, které už každý týden vstupují do našeho běžného života skrze uměle generované obrázky, text, nebo zvuk? Kde je naděje v solarpunk? Podmořské kabely mají určitě uhlíkovou stopu, ale řešení klimatické krize si bez nich představit neumím. Zmínka o tom, že eskapismus si nemůžeme dovolit mi taky ruší vlny. Polovina popkultury v čele se Star Wars a Tolkienem je do velké míry eskapismus. Člověk prostě musí chvíli vypustit, aby mohl nabít baterky a měl sílu řešit reálné problémy v reálném světě. Možná je to myšleno tak, že bychom na to nemuseli vydávat tolik energie. Ale otázka je, kolik energie za rok vydá třeba jiná továrna na eskapismus, Hollywood (nebo Bollywood!). Možná je to myšleno tak, že by šlo o plošný eskapismus, kde se všichni před globálním oteplováním schováme do Mety. Ale to odporuje chování Minecraftové generace, která ve virtuální realitě žije od mala a přitom protestuje za klima.
- [The Age of Social Media Is Ending](https://www.theatlantic.com/technology/archive/2022/11/twitter-facebook-social-media-decline/672074/)<br>Nevím, jestli souhlasím se vším, ale bylo zajímavé si to přečíst a přemýšlet o tom. Přechod od social networking k social media je ale rozhodně užitečná mentální pomůcka k pochopení toho, co se na sítích za ty roky změnilo, k čemu byly dřív a k čemu směřují dnes.
