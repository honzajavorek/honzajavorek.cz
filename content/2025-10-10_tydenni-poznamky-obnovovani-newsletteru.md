Title: Týdenní poznámky: Obnovování newsletteru
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/361
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115351106633375952
LinkedIn-Comments: https://www.linkedin.com/pulse/t%C3%BDdenn%C3%AD-pozn%C3%A1mky-obnovov%C3%A1n%C3%AD-newsletteru-honza-javorek-gt4oe/
Description: Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru? Tentokrát je to na 15 min čtení 😅

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-09-26_tydenni-poznamky-covidek-a-zmeny-v-klubu.md) už utekl nějaký ten týden (26. 9. až 10. 10.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Minulý týden v pátek jsem doma zůstal na dceru sám, protože žena jela volit na Moravu, a tak jsem napsat týdenní poznámky nestihl. Dneska to možná taky nestihnu, ale dám tomu šanci.

Toto vydání nově nejenom že vyjde na mém blogu a zprostředkovaně potom na Telegramu, Mastodonu, v klubovém Discordu a ještě přijde těm, kdo to tady odebírají e-mailem, ale taky se objeví na LinkedInu! Čtěte dál a dozvíte se, jak je to možné. Jsem zvědavý, zda to přinese nějaké nové čtenáře a případně jaké 😀 Každopádně kdo tohle čtete na LinkedInu, vítám vás!

## Skupinky v klubu

Na klubovém Discordu jsem ještě dodělal věci kolem skupinek. Propojil jsem skupinky na C/C++/Rust/Zig a na JavaScript s odpovídajícími zájmovými rolemi a všechno, co ještě chybělo, jsem dokonfiguroval.

Na [prodejní stránce klubu](https://junior.guru/club/) jsem omezil počet vypsaných zájmů členů na 12, které mají nejvíc členů, aby tam toho nebylo příliš. A když už jsem byl u toho, tak jsem tam přidal i ikony jednotlivých programovacích jazyků a technologií.

Bylo to trochu složitější, protože v [Bootstrap ikonách](https://icons.getbootstrap.com/) nejsou programovací jazyky. Kombinuju to s [DevIcon](https://devicon.dev/). Ty jsou zase barevné, ale to není nic, s čím by si neporadilo `filter: brightness(0) saturate(100%);` v CSS. Takhle to teď vypadá:

![Nové ikony]({static}/images/7a6e13848b837b15.png){: .img-thumbnail }

Napsal jsem pak o tom ještě statusy [na LinkedIn](https://www.linkedin.com/posts/honzajavorek_tak-jsem-kone%C4%8Dn%C4%9B-p%C5%99idal-i-ikonky-programovac%C3%ADch-activity-7379406044210413569-fRrg) a [na Mastodon](https://mastodonczech.cz/@honzajavorek/115292263035221535).

## Vibe coding

Už jste si někdy něco [navibekódili](https://cs.wikipedia.org/wiki/Vibe_coding)? Zkusil jsem to s Pythonem, ale nedokázal jsem do toho nekoukat a nehrabat. Teď mě napadlo, že by se mi hodil _custom_ doplněk do Firefoxu. Nikdy jsem nic takového nepsal a do JavaScriptu nemám vůbec problém se ani trochu nedívat 😆, takže ideální příležitost zkusit to navibovat. Bez AI bych se do něčeho takového ani nepouštěl.

Copilot měl první verzi hotovou za pár minut. Pak jsem jen promptoval a zkoušel, jestli to funguje tak, jak chci. Když ne, dal jsem mu nějaké debug info a promptoval jsem dál. Neviděl jsem do dnešního dne ani řádek kódu.

No a mám hotovo! Povedlo se to. Díky vibekódění můžu konečně překonat zdi uzavřených sociálních sítí a provozovat POSSE, tzn. [Publish on your Own Site, Syndicate Elsewhere](https://indieweb.org/POSSE), i na tak těžkém kalibru, jakým je LinkedIn! Tady je video, jak to funguje:

[![Video jak funguje doplněk do Firefoxu]({static}/images/screenshot-2025-10-10-at-13-59-09.png)](https://www.youtube.com/watch?v=1xqSONbMlZI)

Discord tam je jen jako bonus. Mohl bych to do něj dát přes API, ale chci, aby vlákno s mým klubovým deníčkem bylo osobnější, tak si to tam jen připravím k odeslání.

Takže díky tomuhle teď můžu publikovat tyhle články i na LinkedIn, jako ten jejich slavný „pseudo-newsletter“. Třeba díky tomu víc lidí objeví tento blog a třeba i junior.guru. A když se jim to bude líbit, začnou to odebírat nějakým normálním způsobem, třeba e-mailem, a staromilci klidně i přes RSS 😉

Kód jsem nikam nedával, zatím to mám jen lokálně. Třeba jednou hodím na GitHub, s velkým varováním, že to je jen na vlastní nebezpečí.

## Newsletter na junior.guru

Hlavním cílem uplynulých dvou týdnů bylo oživit newsletter na junior.guru. Spoustu věcí už se mi povedlo připravit v minulých dvou měsících, ale stále to nebylo dotaženo. Protože byl přelom září a října, dělal jsem si naděje, že bych mohl zrovna poslat první vydání, které by bylo shrnutím novinek za září.

Začal jsem postupně skládat e-mail, který se bude posílat. Buttondown má API a e-maily jdou vytvořit jako Markdown, tak jsem si napsal skript, který to tvoří. Postupně jsem do toho dal shrnutí toho, co se událo v klubu, pak čísla ohledně pracovních nabídek, informace o aktuálně populárních kurzech, kolik jsme dělali review CVček, kolik bylo v klubu výtvorů, klubové akce a jejich záznamy, nejaktivnější skupinky a deníčky, nejbližší programátorské srazy, konference…

No dalo to hromadu práce. Už jenom sehnat vždycky ta data, mít je v databázi, vytáhnout tak jak potřebuju, a asi nejvíc práce nakonec vždycky zabralo vymyslet, jakým způsobem je budu lidem prezentovat v obyčejném e-mailu v Markdownu. U toho jsem samozřejmě našel hromadu chyb v existujícím kódu, nebo jsem nějaké chyby omylem přidal a pak je opravoval.

Mezitím Buttondown [implementoval češtinu](https://buttondown.com/changelog/2025-10-01), kterou jsem jim už dříve dodal.

Začalo mě stresovat, že vytvořit newsletter v prvním týdnu nestíhám, tak jsem se rozhodl, že svůj týden práce pro Apify posunu a že tomu dám ještě jeden týden.

Protože jsem ještě nepřesunul formulář na registraci do newsletteru, noví odběratelé mi stále padají do Ecomailu. A do Ecomailu jsem kdysi přesunul i svoje někdejší odběratele z MailChimpu 😅 Do toho mám ještě Memberful s lidmi, kteří jsou členy klubu.

Napsal jsem si tedy skript, který mi lidi z Ecomailu přes [Buttondown API](https://docs.buttondown.com/api-subscribers-create) přidá do seznamu odběratelů rovnou, ale který vezme i lidi z Memberful a přidá je taky, akorát přes opt-in, tzn. že budou muset ještě potvrdit, že to fakt chtějí odebírat.

Členům klubu jsem nejdřív napsal zprávu (třetí hromadný emailing v historii existence klubu), kde jsem jim vysvětlil, že obnovuju newsletter, a že mohou očekávat tu opt-in zprávu, kde to buď potvrdí, nebo to budou ignorovat a nic jim už chodit nebude. Tento postup mi přišel jako dobrý kompromis všeho a podle ChatGPT je to i legálně a eticky správně 😅

![Mail členům]({static}/images/screenshot-2025-10-10-at-19-22-23-edit-post.png){: .img-thumbnail }

No takže jsem si napsal skript, který to celé pěkně řeší. Vyzkoušel jsem, že funguje, pak jsem smazal všechny odběratele a pustil ho znovu. Ale systém Buttondownu mi napsal, že ty kontakty, co jsem smazal, nemůžu přidat znova, že se odhlásily 🙈 Asi to nerozlišuje, když si s tím hraju ručně v adminovi, a když se lidi fakt odhlásí sami. Nu dobrá, přes support vyřešeno, tenhle skrytý stav těch e-mailů mi resetovali.

Tak jsem skript spustil znova. A Buttondown mi zablokoval účet, aby zjistili, jestli nejsem spammer. Navíc jsem narazil na limit počtu lidí, které mohu za jeden den přidat. A druhý den se stalo totéž. Přes support mi poradili, že mám zkusit nahrát lidi přes CSV, kde není limit, tak jsem si jiným skriptem vygeneroval CSV, ale když jsem ho nahrál, tak se mi všechny e-maily sice přidaly, ale všechny rovnou 🙈

A to jsem ještě pár zádrhelů vynechal, protože to bych tady mohl popisovat asi ještě dlouho. No prostě teď jsem ve stavu, že je pátek odpoledne a já newsletter stále odeslat nemůžu. Sice už se mi povedlo přesypat ty e-maily, ale mám zase zablokovaný účet a nějaká ta stovka e-mailů je přidaná bez opt-inu, což tak nemůže zůstat, potřebuju je přeřadit na opt-in.

Takže si dopisuju se supportem a kdo ví, kdy ten „zářiový“ junior.guru newsletter vůbec pošlu… No až ten první newsletter pošlu, tak to bude velká sláva teda! Naštěstí všechny tyhle fuckupy souvisí jen s úvodním přesypáním odběratelů a tím, jak to mám z historických a všelijakých důvodů já složité. Až bude přesypáno, tak tohle nebudu už muset (snad nikdy) řešit.

![Náhled e-mailu]({static}/images/screenshot-2025-10-10-at-13-53-07-zari-2025-ve-svete-it-junioru-emails-buttondown.png){: .img-thumbnail }
Takhle nějak to bude vypadat…

## Plánování klubových akcí

Nemáme naplánovanou [klubovou akci](https://junior.guru/events/) na říjen. Všimla si toho Táňa, všiml jsem si toho já, ale to nic nezměnilo na tom, že přednáška naplánovaná není 😅

Táňa mi nepomůže s výběrem speakerů, dramaturgií a úvodním kontaktováním, takže míček byl na mojí straně. Vyhrnul jsem tedy rukávy a udělal konečně tabulku s nápady na témata a speakery. Pak mi Táňa vybrala tři, které mám oslovit, a to jsem nakonec i udělal. Všichni souhlasili, tak teď bych měl ještě navázat a odstartovat společné konverzace, kde bude i Táňa a ta pak už může všechno zařídit a domluvit.

V plánu je udělat si _pipeline_ na několik měsíců dopředu, tak jak by se slušelo a patřilo, abychom to vždy nehonili na poslední chvíli. S frekvencí jedna přednáška měsíčně by to nemusel být zas takový problém.

## Video pro PodVocasem

Natočil jsem upoutávku na živé natáčení podcastu PodVocasem, kde budu jako host. Dal jsem to na [YouTube](https://youtube.com/shorts/fwknNIBq-tY), [LinkedIn](https://www.linkedin.com/posts/honzajavorek_zaj%C3%ADm%C3%A1-t%C4%9B-osud-it-junior%C5%AF-v-dob%C4%9B-ai-p%C5%99ij%C4%8F-activity-7381991032697208832-1n4h), [Mastodon](https://mastodonczech.cz/@honzajavorek/115343620794294772), [Instagram](https://www.instagram.com/p/DPmk8RvjAUaXhtAsdo1We-oe6rfHLlrKCcRSfw0/).

Původně se mi do toho moc nechtělo, ale kluci mě poprosili a já věděl, že to dokážu, jen se mi nechtělo… nakonec jsem se do toho ale dokopal. Šel jsem do parku a natočil tam pár záběrů, pak jsem to sestříhal a bylo.

Bohužel zvuk z parku byl příšerný a obraz taky, takže jsem asi dvě hodiny strávil opravováním, aby mi šlo aspoň trochu rozumět a nevypadalo to hrozně. Asi fakt budu muset koupit ten mikrofon. A s tím obrazem nevím co, myslel jsem, že iPhone to nějak pořeší sám od sebe, ale houbelec. Asi se ze mě bude muset stát _colorist_, ale zas jako že bych měl čas a energii přebarvovat každý záběr, který natočím, to asi taky neškáluje.

Každopádně kromě toho opravování to byla nakonec celkem zábava. Ale pravidelně bych to dělat nechtěl. Jednak je takové natáčení sama sebe pro mně pořád ještě za komfortní zónou, jednak jsem s tím prostě zabil celé jedno dopoledne, přitom je to video na pár sekund.

![Video na LinkedInu]({static}/images/screenshot-2025-10-10-at-18-56-08-2-post-feed-linkedin.png)

## Pračka

Shořela nám pračka. Tedy ne nám, protože není naše, byla součástí vybavení bytu, kde jsme v nájmu, ale protože jsme v ní prali, tak udělám zkratku a napíšu, že naše. Byla už dost stará, takže nás její shoření nepřekvapilo.

Naštěstí máme v pohodě majitele, takže jsme jim napsali, domluvili že koupíme novou a jakou, a oni že jo, že to proplatí. Takže jsme něco koupili, Datart to dovezl, ale řekli nám, že jsme tu starou měli vypojit a že to oni teda dělat nebudou, nechali nám doma novou i starou a odjeli pryč.

Někde malým písmem jsme pak našli v podmínkách, že to tak opravdu je, měli jsme ji vypojit a připravit. Je to odšroubování dvou koleček, ale podle mě se borci zalekli především toho, že pračka je v nepřístupném koutě malé koupelny a bylo by dost logisticky obtížné ji vytáhnout.

Tak jsme si včera odpoledne udělali se ženou brigádu a tu logistiku jsme vymysleli a dopravili přes různé polštářové tlumiče a posuny po karimatce starou pračku ven a novou dovnitř. Tu jsem rovnou i zapojil a pere. Ze srandy jsem to natočil na video a to jsem si ještě pro radost hned večer sestříhal do dvouminutového dramatického heroického opusu, ale nikam veřejně to dávat nebudu.

## Změna „ceníku“ na prodejní stránce

Moje komunita na Discordu funguje už od svého vzniku před 4 lety tak, že je tam 14 dní zdarma, bez zadávání karty. Ale stále ladím způsob, jak to odprezentovat na prodejní stránce, aby se toho lidi nebáli a opravdu to vyzkoušeli.

Chápu, když mi někdo z nejrůznějších důvodů nedůvěřuje, ale všechny moje verze textů, tlačítek a příslibů vždy spíš trpěly tím, že si lidi ani nevšimli, že to je na 14 dní úplně zdarma. Že se ani nezadává karta, a pokud člověku klub nesedne, prostě akorát po dvou týdnech nedoplní platební údaje a systém jej automaticky vyhodí.

Teď se mi stalo, že i člověk, který vyloženě věděl, že na té stránce někde existuje tlačítko na vyzkoušení klubu, to tlačítko prostě nenašel. A to už jsem si řekl, že to už není možné, že tam mám fakt něco zásadního špatně.

Čerstvýma očima jsem se podíval, jak ta moje landing page vlastně vypadá, a pak jsem to celé překopal. Následovala i obligátní kontrola přes ChatGPT - jestli by mi ještě něco doporučilo a co by vylepšilo.

Měl jsem to hotové za půl dne a podle mě je to o dost lepší. Podle lidí na [LinkedInu](https://www.linkedin.com/posts/honzajavorek_zdarma-na-14-dn%C3%AD-bez-zad%C3%A1v%C3%A1n%C3%AD-karty-fakt-activity-7378817344657211392-rvUM?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACB93ABHHj4UI2winetGMZHboHlZIZojJA) nebo [Mastodonu](https://mastodonczech.cz/@honzajavorek/115288653905946374) taky. Tak jsem zvědav, jestli se teď do klubu dostane víc lidí?

![Před]({static}/images/screenshot-2025-09-29-at-11-09-00-klub-pro-zacatecniky-v-programovani.png){: .img-thumbnail }
Před změnami

![Po]({static}/images/screenshot-2025-09-29-at-18-39-36-klub-pro-zacatecniky-v-programovani.png){: .img-thumbnail }
Po změnách

## Další

- Prvního října v klubu na junior.guru odstartovala první projektová výzva 💪 Jsem zvědavý, jak se to chytne. Zadání na říjen bude naprogramovat hru oběšence. Jakýkoliv jazyk, jakékoliv řešení, musí to akorát splňovat několik bodů jak se to má chovat. Těším se, že by to mohlo rozproudit aktivitu a motivovat lidi velmi volnou formou k projektům, tak nějak každý za sebe, ale vlastně tak nějak všichni společně. Tyhle výzvy si vzala pod křídla členka Jana Z. a výkop té výzvy udělala fakt skvěle.
- Byl jsem na obědě s [Nelou S.](https://junior.guru/handbook/mental-health/), která se náhodou ocitla v Praze a náhodou i kousek od místa, kde pracuju. Bylo to fajn.
- V kanceláři, kde pracuju, se to začalo zahušťovat! Dlouho jsem byl sám v místnosti, ale kamarád, který tady má firmu, začíná úkolovat nějaké nové lidi a ti sem začínají chodit. Konec hardcore poustevničení a introvertství 😀 Oba nové lidi znám z Python komunity a je to fajn osvěžení. Je to druhý den, co jsou tady, a už jsem zažil docela dost srandy a hned i dva společné obědy.
- Zašel jsem si do sauny.
- Posunul jsem o kousek dál jednání o sponzorství s Red Hatem na další rok. Chtěli, ať pošlu _service offer_. Sice nevím, co to je, ale poslal jsem to. Stejně jako vloni 😀
- Vyšel nový Python 3.14, takže jsem opravoval asi pět věcí, které mi kvůli tomu přestaly fungovat. Především _nightly_ buildy na hobby projektech, kde se zničeho nic nedařilo nainstalovat nějakou závislost. Zapinoval jsem prozatím verzi Pythonu. CircleCI taky upgradovalo Node.js a já neměl zapinovanou přesnou verzi Docker image, takže tam mi taky něco vybouchlo.
- Spadlo mi [p3news](https://mastodonczech.cz/@p3news), protože na oficiálním webu Prahy 3 použili v jednom článku jako obrázek SVG a s tím Mastodon nepočítá na vstupu. Opravil jsem.
- Plánujeme spolu s Terezou P. zase nějaké pravidelné cally, kde si budeme povídat o mojem marketingu a její komunitě pro copywritery. Shodli jsme se, že nám to bude teď stačit jednou za měsíc.
- Hodil jsem konečně na sítě videa z akce, kterou jsem nedávno konal spolu s Mews. Dal jsem je na obvyklá místa jako [na LinkedIn](https://www.linkedin.com/posts/honzajavorek_ai-a-junio%C5%99i-pomocn%C3%ADk-nebo-riziko-probrali-activity-7381232150760595456-tS4o), ale taky na nejrůznější Discordy a do Facebookových skupin.
- Během volebního víkendu jsem zažil velký stres při shánění nového bydlení. Vyhnuli jsme se něčemu, co by paní Jolanda nazvala velký špatný. Takže výsledky voleb mě oproti tomu už pak vůbec nijak netrápily 😀
- Od organizátorů konference [DevFest](https://devfest.cz/) jsme jako komunita dostali tři volňásky, tak jsem na ně zase udělal soutěž. Na začátku týdne jsem to na Discordu spustil, dneska jsem to losoval, a už máme tři výherce.
- Viděl jsem se na chvíli s tátou v Praze na nádraží, když sem měl cestu.
- Členka klubu Sandra H., která se pustila do studia IT na univerzitě v Pardubicích, se mi přihlásila, že by tam mohla rozdat nějaké junior.guru samolepky. Tak jsem hned nějaké nacpal do obálky a přes Zásilkovnu jsem jí to poslal.
- Vzpomněl jsem si, že jsem kdysi dávno zadal Adamovi K. psaní rozhovorů s členy klubu, které by mohly vycházet na [stránce s příběhy](https://junior.guru/stories/). Měl maturitu, tak jsem mu dal období hájení, ale teď už mi přišlo, že bych nerad, aby to vyhnilo. Poslal mi draft prvního rozhovoru a líbilo se mi to, takže budem pokračovat a těším se, až to vydáme.
- Měl jsem dnes schůzku se svým novým „šéfem“ v Apify, a večer jdu na párty, oslavu 10 let existence Apify.
- Přišlo mi pár Pull Requestů na projekt [Danube Delta](https://github.com/honzajavorek/danube-delta/), který má pohnutou historii a normálně bych jej už archivoval, ale bohužel na něm závisí blog Python komunity. Řešil jsem pak na Slacku Pyvce, co s tím, a jestli to nepřesunout pod Pyvec.
- Domluvili jsme se s ENGETO na prodloužení jejich sponzorství. Zanesl jsem změny do systému a poslal fakturu.
- YouTube mi [nabídl vstup do Partner Programu](https://mastodonczech.cz/@honzajavorek/115275289782362791), ale vůbec nevím co to znamená, jestli je to dobře nebo špatně, a neměl jsem čas s tím cokoliv dělat 😀 Dokud mi nepřijde plaketa za milion odběratelů, tak je to pod mou úroveň 😆
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Nasbíralo se toho dost, ale všechno jsem prošel, vyřešil, přečetl, na vše odpověděl, a teď to mám celkem čisté. Tak ahoj za týden práce pro Apify – to zas bude nasbíráno jak po dovolené 🙈
-   Za 15 dní jsem se nevěnoval žádné sportovní aktivitě.

## Plánuji

1. Budu týden pracovat pro Apify.
2. Pokud to půjde a pokud mi pomůžou na podpoře Buttondownu, pošlu ve volné chvíli ten první newsletter.
3. Vymyslím přednášku na říjen, ať ji může Táňa zařídit.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Deloitte Australia to partially refund $290,000 report filled with suspected AI-generated errors | AP News](https://apnews.com/article/australia-ai-errors-deloitte-ab54858680ffc4ae6555b31c8fb987f3)<br>Další díl příběhu „všechno teď bude dělat AI“, popřípadě „AI umí v kancelářském zaměstnání skvěle ušetřit čas a práci“ apod.
- [The RubyGems takeover from the perspective of an open source developer](https://joel.drapper.me/p/ruby-central/)<br>Tož dobrý fuckup mají v Ruby komunitě. Už jsem o tom četl asi čtyři články, ale kdo se neorientuje ve specifických jménech a názvech, nebo se v nich nechce začít orientovat jako já, ocení nejvíc asi tenhle – stručné zhodnocení toho, co se stalo na úrovni open source principů.
- [Graph – Portfolio Portešová](https://sarkaportesova.com/vizpraktikum/)<br>Tohle je úplně skvělé. Úplně všechno o českých coverech zahraničních písniček.
- [Whisky War - Wikipedia](https://en.wikipedia.org/wiki/Whisky_War#Conflict)<br>Jak vypadá drsný konflikt mezi Kanadou a Dánskem: „In 1984, Canadian soldiers visited the island and planted a Canadian flag, also leaving a bottle of Canadian whisky. The Danish Minister of Greenland Affairs came to the island himself later the same year with the Danish flag, a bottle of snaps, and a letter stating "Welcome to the Danish Island". The two countries proceeded to take turns planting their flags on the island and exchanging alcoholic beverages.“
