Title: Týdenní poznámky: Dovolenkování, přípravy příručky
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158350562002707
Twitter-Comments: https://twitter.com/honzajavorek/status/1290276368475799554


Utekl zase nějaký čas (17.7. — 7.8.) a tak [stejně jako minule]({filename}/2020-07-17_tydenni-poznamky-po-usi-ve-frontendu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Dovolená a "sprint"

17.7. až 26.7. jsem byl na dovolené v Bílých Karpatech a v Beskydech. Od 30.7. do 2.8. jsem zase byl na "sprintu" české Python komunity, což je několikadenní akce na chalupě, kam se sjedou aktivní lidi ze všech koutů republiky a pracují na komunitních projektech. Zápis ze sprintu se v blízké době určitě objeví na [Python blogu](https://blog.python.cz/). Já jsem pracoval na různých věcech okolo [dokumentace české Python komunity](https://docs.pyvec.org/) a taky jsem vytvořil [Slack bota](https://github.com/pyvec/jechova/), který bude připomínat, že ještě nebylo oznámeno téma na [Pražské Pyvo](https://pyvo.cz/praha-pyvo/). Překvapilo mě, že to bylo na 45 řádků :)


## Další poznámky

-   Všiml jsem si, že na JG začala chodit spousta lidí z forum.root.cz, a to díky [příspěvku zde](https://forum.root.cz/index.php?topic=23241.0).

    > Osobně se mi líbí projekt https://junior.guru/ . Doporučuji ho každému, kdo se jen trochu zmíní, že by se rád naučil programovat.

    Potěší :)

-   Vypršela většina inzerátů na [stránce s pracovními nabídkami](https://junior.guru/jobs/). Před měsícem jsem doprogramoval expiraci. Nové inzeráty se moc nehrnou, jednak asi kvůli prázdninám, jednak má spousta firem, které by juniory nabíraly, hiring freeze kvůli koronaviru. Inzeráty jsou můj hlavní byznys model, takže toto budu muset nějak vyřešit.
-   Taky mě napadlo, že e-maily ohledně vypršení inzerátu mohou zapadnout. Doprogramoval jsem tedy, aby se u pravidelného e-mailu v případě, že má inzerát brzy vypršet, změnil předmět z "Jak se daří vašemu inzerátu?" na "Váš inzerát brzy vypřší"
-   Po dovolené jsem celý jeden den řešil maily, které se nasbíraly, ale taky jsem dost prokrastinoval jakoukoliv činnost, protože v Beskydech bylo fakt krásně a mojí hlavě se chtělo ještě chodit po horách. To abyste si nemysleli, že člověk, který dělá na svém, nemá nikdy [KOPR](https://cestina20.cz/slovnik/kopr/).
-   Vyplňoval jsem formuláře, díky kterým se stanu dodavatelem pro jednu korporaci.
-   Dostal jsem odpověď od Romea (viz nějaké předchozí poznámky) a dověděl se nějaký kontext a nějaké možnosti co by šlo dělat. Taky mi poslali [tento příběh](http://www.romea.cz/cz/zpravodajstvi/student-marcel-horvath-chtel-bych-pracovat-pro-velkou-it-firmu-napriklad-microsoft). Aspoň něco! Příběh jsem přidal na úvodní stránku JG. O chlapci existuje i [reportáž na ČT](https://www.facebook.com/watch/?v=328706637919134).
-   Když jsem příběh přidal, všiml jsem si, jak se to zobrazuje ošklivě, zalamování slov, nezarovnané sloupce a řádky… Takže jsem se neudržel, přepsal tuto část frontendu do BEMu a předělal ze [sloupců](https://developer.mozilla.org/en-US/docs/Web/CSS/columns) do [flexu](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). Teď to snad vypadá líp.
-   Oprava zase několika bugů souvisejících s hlavičkou, kterých jsem si všiml.
-   Vytvořil jsem [Strava Club pro fanoušky Pythonu v Česku](https://www.strava.com/clubs/715659).
-   S koncem měsíce jsem opět poslal [newsletter](https://us3.campaign-archive.com/?u=7d3f89ef9b2ed953ddf4ff5f6&id=a602dba821). Odběratelé stále stoupají, newsletter už má 190 odběratelů!
-   Prošel jsem něčí inzerát, jestli je hezky napsaný a dostatečně juniorní. Dělám to v rámci nějaké spolupráce nebo zadarmo ze známosti, ale začíná se mi to už stávat docela často - a to nejen co se týče juniorních inzerátů. Možná na to navěsím cenovku a poskytnu jako službu :) Sice to neškáluje, ale jako doplňková činnost dobrý, a kdyby mě to už nebavilo, cenovkou se dá počet poptávek regulovat.
-   Výpočty od kdy do kdy je inzerát aktivní a kolik dní zbývá jsem vytáhl ze skriptu, který posílá inzerentům pravidelné e-maily s analytikou a dal je přímo do Peewee modelu pracovní nabídky jako vlastnosti a metody. Díky tomu se to i hezky (unit-)testuje.
-   Pokračoval jsem v práci na osnově obsahové stránky. Třeba na [stránce o získávání praxe](https://junior.guru/practice/). Vpravo nahoře je tlačítko na zobrazení osnovy (obsah - pojmenování stále ladím), kde se dá mrknout na to, kde zrovna jsem, a kliknout na jinou sekci. Zatím je to takový prototyp, ale je tam. Ještě to budu muset doladit barevně, pro mobil, z hlediska přístupnosti… Nakonec se to otvírá pomocí JavaScriptu, ale hlavní ovládací prvek je normální HTML checkbox input, takže by to mělo mít základní přístupnost, např. by to mělo jít ovládat klávesnicí.
-   Žlutě podbarvené nadpisy už se mi přestaly líbit před nějakou dobou, ale neměl jsem dobrý nápad co s nimi. Až když jsem teď koukal, jak je udělaná osnova na Wikipedii, a všiml si, že pod nadpisy druhé úrovně mají čáru a vypadá to celkem dobře, jsem zkusil udělat něco podobného - ale žlutě. Nevím, jestli je to designový skvost, ale je to lepší než to původní, takže za mě zatím dobrý.
-   Rozhodl jsem se, že **příručku vydám 1.9.** Odběratelé [newsletteru](http://eepurl.com/gyG8Bb) by se k ní měli dostat ale dřív, protože jim to celou dobu slibuju. Ještě nevím, jak to udělám a kdy přesně pro ně bude připravená, ale nějak to snad vymyslím :D
-   [Lenka Erbenová](https://www.linkedin.com/in/lenkaerbenova/) dostala k přečtení připravovanou příručku a napsala, že je BOŽÍ. Hned jsem to [odcitoval na stránku pro firmy](https://junior.guru/hire-juniors/#handbook) a využil i na sociálních sítích. Budu rád, když mi retweetnete [tohle](https://twitter.com/honzajavorek/status/1290169787364990977). Podle provozu na silnicích vidím, že se lidi vrátili z dovolené a celý srpen bych měl na sociálních sítích strávit propagací toho, že 1.9. to vyjde, aby to vyústilo v pořádný _big bang_.
-   Uvažuju, jestli k vydání příručky nepřipravit i tiskovou zprávu, ale neumím to a moje předchozí pokusy pro PyCon CZ nebo když jsem zkoušel kontaktovat média během koronaviru neměly moc velký úspěch. Třeba se mi to povede udělat napotřetí dobře. Zkusím následovat všechny poučky pro psaní TZ, které najdu na internetu, víc pro to asi udělat už nemůžu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## PyCon Africa

Reklama: Zítra začíná [PyCon Africa](https://africa.pycon.org/), celoafrická konference o Pythonu. Je to zadarmo a letos kvůli (nebo možná v tomto případě díky?) koronaviru se koná online, takže se můžete účastnit na jeden klik. Přednáší tam i můj kámoš [Vuy Ndlovu](https://twitter.com/TerraMeijar) nebo [Miro Šedivý](https://twitter.com/eumiro), kterého znáte z českých PyConů, omrkněte to!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Komentář: Internet nemůže být tabu. Škola se po krizi musí změnit](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Fkomentar-internet-nemuze-byt-tabu-skola-se-po-krizi-musi-zmenit-112615&h=8ce8ed02958ad879c8993a20aca7092ae37ed2fa5e033fb9f93042dcc1b41c19)<br>“Škola se snaží připravovat děti na situaci, v níž nebudou mít internet na dosah. Přitom jedinou takovou situací je dnes v jejich životě jejich škola. Reálný svět už nikoli.”
- [Romové nemají šanci si pronajmout byt. Romská rodina nabízí pět nájmů dopředu, realitky se vymlouvají na majitele bytů](https://getpocket.com/redirect?&url=http%3A%2F%2Fwww.romea.cz%2Fcz%2Fzpravodajstvi%2Fdomaci%2Fromove-nemaji-sanci-si-pronajmout-byt.romska-rodina-nabizi-pet-najmu-dopredu-realitky-se-vymlouvaji-na-majitele-bytu&h=75cc256ab5631e10a16332f11aa1ea67df4f15d82c13d28f47909531c5168cb5)<br>“Každý svého štěstí strůjcem,” že? No, jenom když máte tu správnou barvu kůže.
- [Rok 2020 bude nejteplejší v dějinách. A ani poté to nebude lepší](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Frok-2020-bude-nejteplejsi-v-dejinach-a-ani-pote-to-nebude-lepsi-111707&h=08a9663ee7a6abd8e9834a623f106e2eef4afa764fca12b4e669cdc0c1f562ca)<br>Jo, prší, ale to neznamená, že oteplování nepokračuje a nebudou zase velká sucha.
- [Building a self-updating profile README for GitHub](https://getpocket.com/redirect?&url=https%3A%2F%2Fsimonwillison.net%2F2020%2FJul%2F10%2Fself-updating-profile-readme%2F&h=84258ec9f12ef1aa72c33db9592e23ffc089d8b4fcccc362c561ec7f4edef2e5)<br>GitHub nově umožňuje udělat si “osobní README” na profilu. Dá se s tím vyhrát a lidi už s tím všelijak blbnou. Návod jak začít tady u Simona.
- [When your coworker does great work, tell their manager](https://getpocket.com/redirect?&url=https%3A%2F%2Fjvns.ca%2Fblog%2F2020%2F07%2F14%2Fwhen-your-coworker-does-great-work-tell-their-manager%2F&h=4318a7a789853394f32eeedec6a8d53ee245917d485e57d66398cf9184eabebe)<br>Skvělý návod jak na to
- [Miloše Jakeše uhnětla první republika](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.seznamzpravy.cz%2Fclanek%2Fmilose-jakese-uhnetla-prvni-republika-112713%3Ffbclid%3DIwAR0K1Mgg0ELPdxWz-ahxcCHgNSZQPpDpdcQldjkEpNk8AkV5Bypy9lti8WI&h=92a843aece10c7185876042b7bcaeb6a96100a7b1a9bc77380f34e09a3ce09db)<br>“V extrémní chudobě pohraničí tkví zásadní důvody, proč sudetští Němci volili masově henleinovce. Kvůli bídě a neřešení sociálních problémů měly levicové strany soustavně skoro 1/4 všech hlasů ve volbách. Proto by nás neměl překvapovat razantní nástup komunistů po válce.”
- [Důchodci nemůžou za naše zpackané životy. Ať volí kohokoli](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fkaleidoskop%2F417918-duchodci-nemuzou-za-nase-zpackane-zivoty-at-voli-kohokoli&h=05adf0e20b7034cce1f1f15a56bac0f6be7543f5dbf6845b37ab34f04fcd8296)<br>Zajímavý rozbor, zda a proč důchodci volí jinak
- [Maximalism sucks!](https://getpocket.com/redirect?&url=https%3A%2F%2Fmedium.com%2F%40adent%2Fmaximalism-sucks-12dfec7e90d%3Fsource%3Drss-2d88645b5738------2&h=1ee7a777925cff5196f53aaa6541433bb5fabc90747aa59a0ecd852c30b8db24)<br>S tímhle mívám taky problém, ale na JG se snad trochu léčím
- [Praha – město, které se seniory nepočítá](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2020%2F07%2Fpraha-mesto-ktere-se-seniory-nepocita%2F&h=7646a012538daddbbbb5c108dab467effa1a7badfbc0cd930f78ff2b0fc7712e)<br>Jak se se stoupajícími nájmy zhoršila situace seniorů v Praze — nejen příběhy, ale i podrobný rozbor situace
- [Alkoholismus se dá léčit i mírněji než abstinencí, říká psycholožka Marie Funke](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.flowee.cz%2Fclovek%2F7536-alkoholismus-se-da-lecit-i-mirneji-nez-abstinenci-rika-psycholozka-marie-funke&h=8a22a1f7e19828677678c971e1d6dd197c15d58a4692f235e909fc9a8f5e5855)<br>“Nejčastější pacient je člověk, který je schopen týdny fungovat úplně v pořádku, pije kontrolovaně a jednou za čas přijde průšvih.”
- [Think lazy.](https://getpocket.com/redirect?&url=https%3A%2F%2Ft.co%2F4tnV2rY4X3%3Fssr%3Dtrue&h=1cce071e77271493c6bb06c9c305022ecbb70fb87ca89a9e0510c2783e18de53)<br>Čtení o tom, jak si Safari tým líně vybírá, co bude implementovat a co ne. Zaštiťují se soukromím uživatelů, ale spíš jde o zájmy Apple. Když na to někdo upozorní, dostane se mu šikany.
- [Chytrá karanténa: Velký státní podvod](https://getpocket.com/redirect?&url=https%3A%2F%2Fneovlivni.cz%2Fchytra-karantena-velky-statni-podvod%2F&h=732d4075d43bf16e75adabcc71231c110e2dc93cb7b02e4d99d4c02af526b582)<br>IT versus stát a podfinancovaná hygiena
- [Všude doma, dobře nejlíp. Kašpárkův průvodce českými městy](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fkaleidoskop%2F419087-vsude-doma-dobre-nejlip-kasparkuv-pruvodce-ceskymi-mesty&h=38944a5601cc0041d8760e09c29a6d4d1346632d11aa7b0af2b27e47db43258e)<br>Fajn tipy!
- [Trápí vás uhlíková stopa vašeho talíře? Neřešte, odkud je vaše jídlo, ale co jíte](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fekonomika%2F419314-trapi-vas-uhlikova-stopa-vaseho-talire-nereste-odkud-je-vase-jidlo-ale-co-jite&h=4a9a93a4ee7f2b88eb8ce9542b799df2baf6536173a30d867ff3bc23b6b1a687)<br>Rozbor dopadu potravin na oteplování Země — ač je to neintuitivní, lokální vs. z dálky nehraje roli, význam mají konkrétní potraviny (hovězí)

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
