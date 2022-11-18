Title: Týdenní poznámky: Dohánění CSS a korporátní balíčky
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky
Twitter-Comments: https://twitter.com/honzajavorek/status/1268968394050715649
Facebook-Comments: https://www.facebook.com/honzajavorek/posts/10158178601917707


Utekl další týden (1.6. — 5.6.) a tak [stejně jako minule]({filename}2020-05-29_tydenni-poznamky-horst-fuchs.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Dohánění CSS

Během toho, co jsem minulý týden tvořil [stránku s nabídkou pro firmy](https://junior.guru/hire-juniors/) mi začínalo být už definitivně jasné, že způsob, jakým píšu CSS, je naprostá [špageta](https://cs.wikipedia.org/wiki/%C5%A0pagetov%C3%BD_k%C3%B3d), v níž se přestanu orientovat za 3… 2… 1… BUM. Tweetnul jsem tedy dotaz.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How should I organize my CSS? I&#39;m not a big fan of class-based frameworks like <a href="https://twitter.com/hashtag/Bootstrap?src=hash&amp;ref_src=twsrc%5Etfw">#Bootstrap</a> or <a href="https://twitter.com/hashtag/Tailwind?src=hash&amp;ref_src=twsrc%5Etfw">#Tailwind</a> - it&#39;s another language to learn &amp; pollutes my HTML. I know CSS, so abstractions on top of it obstruct my ability to deliver. However, I always end up having &quot;CSS spaghetti&quot; 🍝</p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/status/1267843448809435136?ref_src=twsrc%5Etfw">June 2, 2020</a></blockquote>

A lidé se hned přihnali s [odkazem na Vzhůru dolů](https://www.vzhurudolu.cz/prirucka/bem), jako bych ten web už dávno neznal. Ostatně minule s tím dotazem na papírování kolem DPH to bylo podobné, odpověď byla „použij [Fakturoid](https://www.fakturoid.cz/)“, který dávno používám.

Jenže jak jsem dělal zhruba šest let backend jako zaměstnanec, tak mi mezitím všechny novinky ve Fakturoidu utekly, a podobné je to i s frontendem. Ten jsem [pověsil na hřebík v roce 2012](http://javorek.net/). Proklikával jsem tedy různé články na Vzhůru dolů a četl si o [BEM](https://www.vzhurudolu.cz/prirucka/bem), [OOCSS](https://www.vzhurudolu.cz/prirucka/oocss), [respektujícím CSS](https://www.vzhurudolu.cz/prirucka/rcss-zasady) apod. Nevěřil jsem vlastním očím, jaké že to skvělé konvence existují! Pod jakým kamenem jsem to spal? Tohle jsou nejspíš věci, které dnes zná každý kodér.

Nejhorší je, že ten BEM jsme používali i v mé minulé práci, ale jak jsem nedělal frontend, tak jsem tomu nevěnoval moc pozornost a úplně to zazdil. Nebo vlastně ne. Nejhorší je, že mi přišel velmi poučný [tento článek, který shrnuje novinky v roce 2014 oproti roku 2009](https://www.vzhurudolu.cz/blog/29-organizace-css-2014). Nebo je možná úplně nejhorší má naivita, když jsem si myslel, že jsem svůj desetiletý skluz dohnal studiem [flexu](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

BEM a OOCSS jsem při prvních úpravách začal hned aplikovat. Hezké je, že se to dá celkem kombinovat i se starším prasokódem. Ten jsem vykázal do samostatné složky. Chtěl jsem ji pojmenovat `legacy`, ale přišlo mi blbé, abych měl na méně než rok starém projektu něco s takovým názvem, takže nakonec je to ve složce `spaghetti`. Když už na tom dělám sám, ať je to aspoň zábava 🍝


## Korporátní balíčky

Začal jsem oslovovat první firmy s nabídkou [sponzorování příručky](https://junior.guru/hire-juniors/#handbook). Schválně jsem nenapsal hned všem firmám, ale zkusil tak pět, abych viděl jak reagují a mohl případně nabídku upravit. Z oslovených firem se mi jich zatím moc neozvalo, ale nic si z toho nedělám, protože i pokud to někoho zaujalo, než to lidi vůbec proberou na poradách, může uplynout nejeden týden.

Mezitím se mi ale ozvaly dvě firmy prakticky samy! Takže jsem to ve středu oslavil - večer jsem šel na pivo. Moje první pořádné pivo po karanténě. Ani u toho jsem ovšem nezahálel a věnoval se poctivě marketingu…

![Pisoárový marketing]({static}/images/pisoarovy-marketing.jpg)
Pisoárový marketing na Žižkově

Začal jsem jednat i s jednou velkou firmou, která s JG v minulosti už experimentovala. V podstatě jsem si jejich připomínky vyložil následovně:

- Velké firmy nebudou nic platit měsíčně. Buď ročně, nebo navždy.<br><small>(Nemohu nevzpomenout na staré moudro, které praví, že v metalových písních se používají jen tři časové jednotky: _forever_, _never_, _ten thousand years_. Korporace to asi mají podobně.)</small>
- Bylo by fajn si moci prohlédnout nějaké výňatky z příručky, osnova nestačí.
- Měřit, měřit, měřit! Když máme platit, chceme vědět, jakou to má výkonnost.

Třeba hned ten první bod by mi byl ještě před rokem úplně jasný - sám jsem přece v korporaci pracoval. Jenže bohužel zapomínám rychle.

Poslední bod zatím promýšlím. Podle mě ho nemám jak udělat. Měřit interakce s tlačítkem na JG prý nestačí. Ideálně bych na každého člověka, který chodí po JG, fyzicky nalepil čárový kód, a jejich recruitment by jej potom načetl a zvolal: „Ha! Tak tento kandidát přišel z JG!“ Jenže já nechci sledovat lidi, podle GDPR snad ani nemůžu, a hlavně - kandidát se může ozvat úplně po vlastní ose a pokud se ho nezeptají, kde ten inzerát viděl poprvé, tak neexistuje způsob, jak zjistit, že přišel z JG.

Ty první dvě věci jsem ale do konce týdne zkusil nějak vyřešit. Vymyslel jsem korporátní balíčky - a to jak [pro nabídky práce](https://junior.guru/hire-juniors/#pricing), tak [pro sponzorování příručky](https://junior.guru/hire-juniors/#handbook-pricing). Nejsem zrovna nějaký machr na cenotvorbu, ale prostě jsem to nějak vypotil u Excelu a kalkulačky, zatím to takhle musí stačit. Jsem zvědavý, jestli bude moje nabídka po těchto změnách pro velké firmy zajímavější.

Taky jsem na stránku přidal [výňatky z příručky](https://junior.guru/hire-juniors/#handbook-preview). Je jich 12 a i tak je to jen zlomek z celého textu. Stejně jsem si už dřív chtěl něco takového připravit, abych mohl ukázkama postupně tapetovat sociální sítě a zajistit tím, že lidi budou o příručce vědět, a že se na ni budou těšit. Požadavek velké firmy tedy akorát uspíšil přípravu obrázků a když už jsem je měl na disku, naplánoval jsem přes [Buffer](https://publish.buffer.com/) statusy na všechny sítě. Protože si myslím, že na Twitteru a LinkedIn mám spíš „fanoušky myšlenky“ a na Facebooku spíš juniory, je text statusů mírně jiný. Na Twitteru a LinkedIn vybízím ke sponzorování, na Facebooku k tomu, aby se junioři přihlásili k [odběru e-mailů](http://eepurl.com/gyG8Bb) a díky tomu se o vydání příručky dověděli mezi prvními.

Díky tomu, že jsem přihlašování do newsletteru minulý týden dost vylepšil a taky jej promuji na sociálních sítích i na samotném webu, každý den teď stoupá počet přihlášených. Zrovna teď jich je 122.


## Ostravské firmy

Jednomu juniorovi, který si právě hledá práci v Ostravě, jsem pomohl s průvodním dopisem. Na oplátku mi sestavil seznam firem, které v okolí Ostravy najímají programátory. Už se těším, až jim budu psát. Mám vždy velkou radost, když se na JG objeví nabídka práce z regionů - Ostravy, Pardubic, Plzně, apod. Je to totiž jinak celkem přeplněné Prahou a do toho sem tam nějaké Brno. Takže snad se mi povede nějaké ty firmy z Ostravy na JG nalákat.


## Týdenní poznámky

Dostal jsem na týdenní poznámky již několik ohlasů. Mnoho se točilo kolem toho, že to lidé rádi čtou, ale pak se cítí blbě. Sepsal jsem tedy kvůli tomu [separátní článek]({filename}2020-06-04_neni-to-zavod.md). Poté jsem ještě přidal do svého [skriptu](https://github.com/honzajavorek/honzajavorek.cz/blob/master/weeknotes.py) na připravu poznámek odstavec, kde na ten článek budu z každých dalších poznámek odkazovat. Je zajímavé, že tento článek rezonoval spoustě lidí, jejichž komentáře nebo lajky pod svými články zas tak moc nevídám. Zřejmě se mi podařilo oslovit nějakou část lidí, kteří jsou většinou jen „tiší čtenáři“ 🙂

Další ohlas byl tento:

> Čtu si už tvoje čtvrté poznámky a koukám, že už jsi úplnej entrepreneur. Já teda nevim přesně, co to znamená, ale určitě to jsi! Používáš slova jako monetizovat a sdílíš, co jsi četl o Lady Gaga 😀

Potěší. Také jsem se minule ptal, jak se vám líbí přidaná sekce s články z [Pocketu](https://getpocket.com/@honzajavorek). Na to jsem dostal jediný ohlas, a to tento:

> Co mě zaujalo by mělo o 90 % vyšší přidanou hodnotu, kdyby k tomu linku bylo vždy tak 5 slov proč tě to zaujalo 😊

Jeden ohlas z jednoho je 100 %, takže jsem si řekl, že bych s tím měl něco dělat. Pocket naštěstí umožňuje při sdílení napsat komentář, takže to nebyl velký problém. Nechtěl jsem to celé ale už dál prasit ve `weeknotes.py` a rozhodl jsem se, že na to vytvořím separátní knihovnu. Tak se i stalo, vytvořil jsem [honzajavorek/pocket-recommendations](https://github.com/honzajavorek/pocket-recommendations):

- Poprvé jsem si vyzkoušel Python balíček vytvořit pomocí [Poetry](https://python-poetry.org/) a bylo to skvělé! Všechno srozumitelné a jednoduché. Určitě doporučuji.
- Byl jsem líný psát dokumentaci a ještě testy, tak jsem vše sepsal do README a to testuji pomocí [doctest](https://docs.python.org/3.7/library/doctest.html). Ani jsem nevěděl, že [pytest](https://docs.pytest.org/) má toto [přímo integrované](https://docs.pytest.org/en/stable/doctest.html). Funguje to parádně, na takovou malou knihovnu mi to přišlo jako výborný způsob, jak rychle sfouknout dvě věci najednou.

Počínaje těmito poznámkami si tedy můžete u sdílených článků i přečíst, proč mě zaujaly.


## Další poznámky

- Přidal jsem [Tomáše](https://tomasehrlich.cz/) [do seznamu podporovatelů](https://junior.guru/donate/#sponsors). Juchů!
- [Připomněl jsem lidem na Twitteru, že v Česku je rasismus taky.](https://twitter.com/honzajavorek/status/1267491717395161088?s=20) Získalo to k dnešnímu dni pěkných 57 srdíček a kupodivu tweet nevyvolal hnojomety, ale jen pár poměrně kultivovaných diskusí. Nejsem zastáncem toho, že s lidmi s jiným názorem se nemluví, snažím se vždy slušně odpovídat. Sám jsem kdysi rasista byl, a kdyby se mnou nikdo nemluvil a jen mi říkal, že jsem rasista, tak jsem jím dodnes. Diskusi na FB profilu SPD bych asi nepřežil, ale nedělal jsem si iluze, že na Twitteru by to mohlo být lepší. Reakce na můj tweet mě však příjemně překvapily. Do podobných věcí se běžně nepouštím, takže možná je to jen štěstí začátečníka? 😀
- Vymýšlel jsem, jak by šlo udělat automatické zalamování dlouhých slov, abych do nich nemusel ručně psát `&shy;` mezi slabiky. Objevil jsem [tohle](http://shy.nothrem.cz/) a [mnater/Hyphenopoly](https://github.com/mnater/Hyphenopoly), ale zatím jsem s tím nic nedělal.
- O víkendu jsem vytvořil a poslal [květnový newsletter](https://us3.campaign-archive.com/?u=7d3f89ef9b2ed953ddf4ff5f6&id=bd0fb23645). Běžně na JG o víkendu nepracuji, ale byl už konec května a květnový newsletter by asi neměl lidem chodit v červnu.
- Už nějakou chvíli funguje [robot na stahování nabídek práce odjinud](https://junior.guru/jobs/#jobs-bot). [StartupJobs](https://www.startupjobs.cz/) mi napsali, že za prvních několik dnů měli 113 prokliků a dva zájemce na konci. Jejich marketing dostal zelenou promovat naši spolupráci, takže se zmínka o JG objevila hned na několika jejich profilech, které mají na sociálních sítích.
- Ještě v souvislosti s monetizací příručky jsem si četl o tom, jak týpek monetizuje svou knihu o typografii: [proč nemá ebook](https://practicaltypography.com/why-theres-no-e-book-or-pdf.html), [jak mu lidi platí za veřejně dostupnou knihu](https://practicaltypography.com/to-pay-or-not-to-pay.html), [jak se snaží o kvalitu čtenářů a ne kvantitu](https://practicaltypography.com/graylist.html). Velmi zajímavé čtení, ale z mnoha důvodů má poměrně speciální situaci a nevím, kolik z toho bych já osobně mohl reálně aplikovat.
- Přes [IFTTT](https://ifttt.com/) jsem týdenní poznámky automaticky posílal na Twitter a LinkedIn. Na Facebook to bohužel nejde, tam to musím dávat vždy ručně. Tento týden jsem se ale rozhodl, že poznámky jsou takový můj osobní deníček, a že mi to k LinkedIn vlastně moc nesedí. Vím, že to je veřejné a přečíst si to tu může kdokoliv, ale tak nějak si romanticky představuju, že jsem tady se skupinkou nadšenců, kterým můžu věřit. Lidem na LinkedIn bych raději posílal ty ceníky než hovorový popis toho, jak jsem je vymýšlel. Navíc to na LinkedIn nikdo ani jednou nelajknul, ani neokomentoval, takže to tam asi ani nikoho nezajímalo. Automatické publikování jsem tedy zrušil a zůstane jen FB a Twitter.
- Byl jsem se za kamarádem podívat do pražského WeWorku. [Mají to tam hezký!](https://www.televizeseznam.cz/video/gebrianvs/novostavba-na-narodni-skryva-prekvapivy-vnitrek-207332)
- Kontaktovala mě firma, jestli na JG nepřidám odkaz na jejich kurzy. Vedl jsem o tom dlouhou debatu na pomezí sales a produktu s nimi i s investorkou (manželkou) a došel jsem k tomu, že to zatím řešit nebudu. Priorita jsou nabídky práce a příručka. Pod všechny seznamy na JG jsem do poznámky přidal zmínku o tom, že pokud chce někdo promovat své kurzy nebo firmu, nechť si zaplatí logo na příručce. Doporučované materiály na JG jsou pečlivě vybrané, není to seznam všeho, co je k nalezení na internetu. Jediný takový seznam je [tady](https://junior.guru/practice/#skills), ale to je jen dočasná z nouze ctnost - s tou sekcí mám časem velké plány.
- Začal jsem pomalu připravovat backend na podporu pro automatickou expiraci nabídek práce. Zatím šlo jen o drobné zemní práce.
- Když nabídka práce umožňuje „plný úvazek“ i „částečný úvazek“, zobrazuje se nyní „plný i částečný úvazek“, místo aby se to jen oddělilo čárkami. Taková blbost, ale šetří to dost místa a lépe se to čte.
- Někteří chytráci při zadávání nabídek práce vyplní všechny možné úvazky, takže je tam jak „plný úvazek“, tak „dobrovolnictví“. Udělal jsem inteligentní filtr, který vyháže nesmysly a nechá jen to, co pro juniory dává největší smysl. Pokud firma je ochotná za práci platit, nemá tam „dobrovolnictví“ co dělat. To je pro neziskovky. Stejně se stážemi. Pokud někdo zadá „placená stáž“ i „neplacená stáž“, zobrazí se na JG jen ta placená.


## A co vy?

Máte dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli? Mám pro vás skvělou zprávu!
V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Za šťastné dnešky! Vyšla působivá studie života v korporátu](https://finmag.penize.cz/recenze/416865-za-stastne-dnesky!-vysla-pusobiva-studie-zivota-v-korporatu)
- [Skandál na Dole Darkov. Nákaza se šíří, ale horníci chodí dál do práce](https://a2larm.cz/2020/05/skandal-na-dole-darkov-nakaza-se-siri-ale-hornici-chodi-dal-do-prace/)
- [Butterick’s Practical Typography](https://practicaltypography.com/typography-in-ten-minutes.html)<br>Základních pět typografických pravidel na webu
- [Uvolněte se, ale s rozumem. Jak se teď nenakazit koronavirem](https://finmag.penize.cz/kaleidoskop/416839-uvolnete-se-ale-s-rozumem-jak-se-ted-nenakazit-koronavirem)<br>Čím se zřejmě budu ještě chvíli řídit - 20 % pravidel, které vychytají 80 % možností se nakazit
- [Vote with your wallet, not your ad blocker](https://practicaltypography.com/vote-with-your-wallet.html)<br>Používejte Ad-Blocker, ale nezapomínejte při tom autorům obsahu platit napřímo, jinak přestane existovat obsah, který je pro vás
- [Mýty o čokoládě díl 1: Čím tmavší, tím lepší](https://www.chocolatehill.cz/alkalizace-kakaa-cokolady)<br>Pravá čokoláda nemá mít černé tóny, má být tmavě hnědá - doteď jsem zjevně věřil hned několika mýtům o čokoládě!
- [Reklama na cigarety. Čím vás dostane?](http://markething.cz/reklama-na-cigarety-cim-vas-dostane)<br>Kam “pivotuje” tabákový průmysl spolu se svým manipulativním marketingem
- [It's time to maintain](https://vicki.substack.com/p/its-time-to-maintain)<br>O neviditelné práci žen, která se neobjevuje v HDP, není oslavována, ale drží všechno pohromadě
- [The Office Is Dead](https://marker.medium.com/the-office-is-dead-16be89f25d01)<br>Covid-19 pomohl firmám v USA uvědomit si, že možná nepotřebují kanceláře - odstěhují se lidi mimo město, skončí mrakodrapy?
- [Why we at $FAMOUS_COMPANY Switched to $HYPED_TECHNOLOGY](https://saagarjha.com/blog/2020/05/10/why-we-at-famous-company-switched-to-hyped-technology/)<br>Šablona na váš úspěšný HackerNews post
- [Z pěší zóny je ‚dálnice‘. Z historického centra Brna se stal průjezd i parkoviště pro auta](https://t.co/uFVWG2Yyf6?ssr=true)

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
