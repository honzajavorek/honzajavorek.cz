Title: Týdenní poznámky: Odpočívání a nové starty
Image: images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří pracovat na [junior.guru](https://junior.guru/) a dalších věcech?
Od [posledních poznámek]({filename}2026-08-11_tydenni-poznamky-dokoncovani-kurzu-o-vytvareni-scraperu-pomoci-ai.md) už utekl nějaký ten týden (11. 8. až 4. 9.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/jan-kahanek-fVUl6kzIvLg-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

Dodělal jsem ten prázdninový červencovo-srpnový dvoutýden v rámci externí spolupráce s Apify, jak jsem o něm psal minule. Pak jsem se rozhodl, že si dám prostě volno, abych si fakt odpočinul a zvolnil.

Rodinka byla u babičky a já jsem doma v klidu dodělával ty věci pro Apify a pak trochu pro junior.guru co bylo potřeba, ale potom jsem si prostě řekl, že zbytek srpna si užiju jako _staycation_, když mě brzy čeká tolik různých životních změn.

Hlídal jsem řemeslníky na bytě, začal zase trochu sportovat, zabýval jsem se zařizováním, chodil po obchodech, byl u kadeřníka, viděl jsem se s kamarádem…

Týden jsme nechali dceru u babičky a žena přijela za mnou zpátky do Prahy, tak jsme sice pracovali a řešili, co bylo na bytě potřeba, ale zároveň jsme si užívali i to, že máme trochu času takhle sami a šli třeba do kina.

Pak jsme jeli na Moravu k babičce a tam jsem se hodně věnoval dceři a užíval jsem si kontakt s přírodou. Bavilo mě hrát si s ní a vytáhnout ji třeba na kolo a tak. Ale taky se jen chvíli povalovat v houpací síti a koukat na mraky nebo na mravence.

Začal jsem zase víc sportovat a po těchto dvou týdnech jsem se celkově začal cítit o dost lépe a šťastněji, víc nabitý energií a tak. Byl to krásný pocit a chtěl bych se naučit nějak si jej uchovat i během normálních dní 😀

Po návratu do Prahy už se začaly trochu roztáčet kolečka různých věcí, které bylo potřeba zařídit, a měli jsme už plnou starost o dítě, takže pohodička se začala trochu rozplývat pod náporem běžných úkolů. Ale i tak jsem si ještě utrhl pár pěkných prázdninových dní.

Třeba jsem s dcerou odzkoušel, jestli by šlo dojet do školky na kole, a byl z toho krásný celodenní výlet 😀

## Nové starty

Domluvili jsme se s Apify na podmínkách, podepsali smlouvy, a zvýšil jsem úvazek z 25 % na 50 %.

Prvního září jsem nastoupil a začali mě onboardovat jako plnohodnotného part-timera, což bylo srandovní, protože už pro ně pracuju víc jak dva roky, akorát do teď to bylo externě.

Potkal jsem zajímavé nové lidi, pozdravil staré známé, a celkově to bylo moc milé a fajn, dostalo se mi tam krásného uvítání a byl jsem zavalen všemožnými benefity. Ale taky onboarding checklistem, kde jsem po dvou dnech sotva někde za půlkou.

Prvního září jsem zároveň začal s dcerou dojíždět do školky, protože teď už do ní nedojdeme pěšky (a na ten poslední rok jsme ji nechtěli vytrhávat z kolektivu). Na Žižkově jsou zrovna rozkopané tramvaje na několika místech, takže je to radost a každá cesta trvá věčnost, ale bereme to sportovně.

V rámci krize středního věku jsem si obešel pár obchodů a pořídil nějaké nové oblečení. Taky jsem si nechal udělat nové brýle a záměrně jsem šel do spíš ulítlejší než konzervativnější varianty, tak jsem zvědav na reakce 😎

Na začátku září jsem se pokusil shrnout svoje veselé pocity z toho, že v mém životě začíná hodně nových věcí, do [tohoto příspěvku na Mastodonu](https://mastodonczech.cz/@honzajavorek/117198093335159645):

> Po víc jak 2 letech příležitostné práce pro Apify jsem tam od září na poloviční úvazek a tím jsem se stal plnohodnotným členem týmu, s vlastním e-mailem a přístupem ke všemu, co se tam děje.
> 
> Uvítali mně hezky, potkal jsem samé fajn lidi, tak teď se ještě naučit všechny ty moje aktivity nějak užonglovat ve správných poměrech:
> 
> 50 % junior.guru<br>
> 50 % Apify<br>
> 50 % zařizování bytu<br>
> 50 % dcera<br>
> 50 % druhé dítě na cestě<br>
> 50 % odpočinek, abych se nezbláznil, žejo<br>
> 50 % Python komunita a všechny side projekty<br>

## Opravy na junior.guru

Nemám teď na JG tolik času, takže mě to nutí optimalizovat, co můžu. Pokud mi něco spadne a já se tomu nemusím věnovat, ale můžu dát tu práci Claude Code a během toho dělat něco jiného, je to ideální. I tak to ale není „zadarmo“, často abych došel k úplné nápravě, musím problém pochopit a rozhodnout se, co s ním, protože Claude sice ví, že je něco rozbité, ale neví, co je z mého pohledu ideální řešení. Často by věci jen zbytečně komplikoval.

-   Upravil jsem texty na [junior.guru/about/finances](https://junior.guru/about/finances/), aby odpovídaly nové realitě.
-   Zjistil jsem, že httpx je neudržované, ale existuje fork httpx2, tak jsem balíčky nahradil ve svých projektech: [crowing#6](https://github.com/juniorguru/crowing/pull/6), [eggtray#417](https://github.com/juniorguru/eggtray/pull/417), [hen#149](https://github.com/juniorguru/hen/pull/149), [junior.guru#1725](https://github.com/juniorguru/junior.guru/pull/1725). Práci za mně udělal cloudový Claude Code, jen jsem ho kontroloval. Pracoval napříč několika projekty a Pull Requesty si celé zmanagoval sám, jen jsem vše kontroloval před tím, než jsem věci mergnul. Na mém oblíbeném projektu githubkit jsem založil issue, jestli nechtějí udělat totéž: [yanyongyu/githubkit#321](https://github.com/yanyongyu/githubkit/issues/321)
-  Padalo mi často CI, kvůli různým problémům, takže jsem si udělal určitou rutinu, která mi pomáhá, když to nechám Claude Code analyzovat: [junior.guru#1722](https://github.com/juniorguru/junior.guru/pull/1722), [junior.guru#1723](https://github.com/juniorguru/junior.guru/pull/1723). Zatím jsem byl ale líný z toho dělat nějaký skill, protože se skilly zatím ještě neumím pracovat. Následně jsem postupně s Claude Code opravoval různé problémy, které se na JG vyskytly: [junior.guru#1724](https://github.com/juniorguru/junior.guru/pull/1724), [junior.guru#1729](https://github.com/juniorguru/junior.guru/pull/1729), [junior.guru#1731](https://github.com/juniorguru/junior.guru/pull/1731), [junior.guru#1732](https://github.com/juniorguru/junior.guru/pull/1732), [junior.guru#1733](https://github.com/juniorguru/junior.guru/pull/1733), [junior.guru#1734](https://github.com/juniorguru/junior.guru/pull/1734)
-  Když mi o repozitář vedle spadly scrapery, udělal jsem změny, které umožní, aby to Claude Code nějak analyzoval a taky mi s tím pomohl: [plucker#172](https://github.com/juniorguru/plucker/pull/172), [plucker#173](https://github.com/juniorguru/plucker/pull/173)
- Spolu s tím, jak jsem nastoupil do Apify, tak mi začaly padat i JG schedules na Apify, což bylo celkem vtipné 😀 Udělali zrovna nějaké omezení, že kdo je na free planu, tak může pouštět jen 5 scraperů paralelně, aby to lidi nezneužívali. Já jsem na free planu, ale jsem dotovaný kreditama zadarmo, takže de facto nemám omezení na to, co můžu s platformou dělat, ale tenhle limit se mě začal týkat, protože free plan je free plan. Takže jsem musel udělat víc schedules po pěti scraperech.

## Delegování práce na reelskách

Myslel jsem si, že přidám Patrika a Táňu na YouTube, Instagram, TikTok, atd. a že vytvořím reelska, Patrik vytvoří reelska, a pak to budeme publikovat a pojede to jako mašina.

Strávil jsem nekonečné hodiny tím, abych přidal Patrika a Táňu do zmíněných služeb. Administrace takových těch „business“ marketingových administrací sociálních sítí je totiž strašně zmatená a nepřehledná a totálně nasírací. Nakonec se mi to ale nějak povedlo. Snad.

Ale každý jsme měli nějakou jinou práci, byly prázdniny, a navíc nás všechny podezírám, že se nám do toho vůbec nechce. Pro nikoho z nás to asi není zrovna něco, do čeho bychom se hrnuli. Zkusil jsem to pak ještě nějak pošťouchnout, něco se udělalo, ale nakonec jsem si nějaká videa stejně musel vypublikovat a naplánovat dneska sám.

Odnáším si z toho, že tohle moc dobře nefunguje a než nás do něčeho nutit, asi bych měl vymyslet jiný přístup, nebo na to dát jinou cenovku, nebo to nějak rozhýbat jinak prostě. Má programátorská duše samozřejmě pokukuje především po automatizaci větší části toho procesu.

## Python komunita

- Letos jsem (myslím že poprvé v historii) nejel na tradiční [letní sprint Python komunity](https://blog.python.cz/Letni-sprinty-Python-komunity-v-Msenem), nebyla na to v mém životě aktuálně energie. Ti, kdo jeli, vytvořili spoustu PR, ale na ty jsem se zatím nestihl podívat, kromě jednoho: [pyvec.org#484](https://github.com/pyvec/pyvec.org/pull/484)
- Pod hlavičkou PyData se připravuje nějaká akce pro začátečníky, která se má konat za měsíc a pod záštitou velké známe SW firmy, ale já bohužel nemám kapacitu se toho teď účastnit nějak víc. Přislíbil jsem jen pomoc s propagací.
- Se zpožděním jsem předal administraci [PyLadies CZ](https://www.linkedin.com/company/30644381/) stránky na LinkedIn někomu, kdo by se o ni mohl aktivněji starat.
- Známe nový termín připravovaného restartu české Python konference [PyCon CZ](https://cz.pycon.org/2027/)! Bude to 16.-18.4., v Plzni, ale zatím to nikomu neříkejte, je to podpultová informace.

## Osobní projekty

[Programy do voleb](https://programydovoleb.cz/) mi daly [přes Mastodon vědět](https://cztwitter.cz/@programydovoleb/117167021528422405), že se rozbil můj projekt [honzajavorek/czech-political-parties](https://github.com/honzajavorek/czech-political-parties/) a jestli to plánuju nějak opravit. Zjistil jsem, že stát původní web úplně změnil a přesunul, takže přišel na řadu kompletní přepis. Našel jsem nově i nějakou oficiální datovou sadu, ale nebylo v ní všechno, takže stejně něco i nadále scrapuju: [czech-political-parties#17](https://github.com/honzajavorek/czech-political-parties/pull/17), [czech-political-parties#18](https://github.com/honzajavorek/czech-political-parties/pull/18), [czech-political-parties#19](https://github.com/honzajavorek/czech-political-parties/pull/19), [czech-political-parties#20](https://github.com/honzajavorek/czech-political-parties/pull/20), [czech-political-parties#21](https://github.com/honzajavorek/czech-political-parties/pull/21). 

Přestalo mi zase fungovat film2trello na evidenci toho, co jsem viděl, nebo chci vidět, takže jsem tam taky trochu uklízel: [film2trello#339](https://github.com/honzajavorek/film2trello/pull/339) [film2trello#340](https://github.com/honzajavorek/film2trello/pull/340), [film2trello#341](https://github.com/honzajavorek/film2trello/pull/341), [film2trello#342](https://github.com/honzajavorek/film2trello/pull/342), [film2trello#343](https://github.com/honzajavorek/film2trello/pull/343), [film2trello#344](https://github.com/honzajavorek/film2trello/pull/344), [film2trello#345](https://github.com/honzajavorek/film2trello/pull/345), [film2trello#346](https://github.com/honzajavorek/film2trello/pull/346), [film2trello#347](https://github.com/honzajavorek/film2trello/pull/347), [film2trello#348](https://github.com/honzajavorek/film2trello/pull/348). Spolu s přestěhováním na nové místo na Praze 3 jsem si ještě přeskupil i kalendáře s kiny: [kino#81](https://github.com/honzajavorek/kino/pull/81)

## Další

-   Oslavili jsme moje narozeniny. Dostal jsem nabitou kartu na chození do Kina Aero, která má platnost půl roku, což beru jako signál, že má milovaná rodina chce, abych i při svém nabitém zodpovědném životě pravidelně odpočíval a večery trávil v kině.
-   Propagoval jsem [nový rozhovor s Pavlou Beránkovou](https://junior.guru/stories/pavla-berankova/). Přes svoje crowing udělátko jsem dnes vytvořil k rozhovoru i videa a nasdílel na sociální sítě jako reelska.
-   Udělal jsem v klubu soutěž o dva lístky na [FrontKon 2026](https://www.frontkon.tech/) a udělal jsem o tom nějaké statusy na sociální sítě.
-   Psal jsem pro Táňu doporučení, v plném znění [tady na navolnenoze.cz](https://navolnenoze.cz/prezentace/tana-vachova/doporuceni/). Taky jsme oslovovali přednášející na další měsíce. Zeptal jsem se lidí v klubu na to, co by je zajímalo, a pak jsem zkusil oslovit lidi, o kterých jsem si myslel, že by o tom mohli mluvit. Zatím to jde dobře, ale nevím, jestli něco stihneme domluvit už na září. Táňa mě uháněla celé léto, ale bohužel jsem měl hlavu jinde a nechal jsem naši přednáškovou _pipeline_ vyschnout, ač tipy na speakery jsou jedna z mála věcí, které stojí na mně. No uvidíme, přinejhorším to prostě rozjedeme až v říjnu a pauza bude delší.
-   Z [DigiKoalice](https://digikoalice.cz/) chtěli nějaký profil junior.guru jakožto následováníhodného projektu, nebo tak něco. Leží mi to v mailu už hodně dlouho, tak to zkusím delegovat na Táňu, jestli mi s tím nepomůže.
-   Vytváření newsletteru se rozbilo, tak jsem ho musel nejdřív opravit, ale pak jsem teda dopsal vydání za srpen a poslal. Pak jsem ho ještě nasdílel na LinkedIn.
-   Dodělali jsme na bytě už skoro všechno: Elektriku, kuchyň, máme jídelní stůl… ale stále zařizujeme. A nemáme třeba radiátory ještě. V létě to nebyla priorita, ale v září už možná bude. Udělali jsme prvotní nákup v IKEA a stavěl jsem několik dní šatní skříně PAX, což zatím považuju za vrcholný výkon co se týče svých kutilských dovedností. Koupil jsem si kvůli tomu i vrtačku a různé další nářadí, které jsem doteď neměl.
-   Dostal jsem nápad na startup a dokonce jsem si k němu koupil doménu mapahluku.cz, ale pak jsem zjistil, že to jednak už existuje jako appka (v lepší podobě, než bych kdy vymyslel) a že to, co bych vytvořil, nejspíš nemá žádný dobrý byznys model, tak jsem to nechal být. Doménu prodám za 500 Kč! 😆
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn. Publikoval jsem v klubu nějaké inzeráty pro juniory, co přišly mailem atd. Udělil jsem jedno stipendium. 22 upgradů závislostí na všech projektech.

## Plánuji

1.  Oslavit o víkendu kamarádovy čtyřicetiny.
2.  Začít pro Apify dělat i nějakou práci, ne jenom onboarding checklist.
3.  Věnovat se reelskám a procesu jejich publikace.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [How accurate have Ed Zitron's AI skeptic predictions been?](https://danluu.com/zitron/)<br>V začátku jsem Eda Zitrona četl a párkrát i sdílel. Pak jsem ho přestal číst, protože byl na můj vkus příliš naštvaný. Kopal do všeho kolem sebe a přišlo mi, že se AI fakt zlepšuje a on to ignoruje. Raději jsem se šel podívat, jak to teda funguje, co se s tím dá dělat, a jak a v čem mi AI může pomoct. A teď Dan Luu (známý tím, že si všechno rád propočítá, než něčemu začne věřit) publikoval tohle, kde se podíval na různá Zitronova tvrzení…
- [Toaletní papír jako záminka. Proč ve skutečnosti skončil v čele drah Krapinec a proč je povede právě Hamplová - Zdopravy.cz](https://zdopravy.cz/toaletni-papir-jako-zaminka-proc-ve-skutecnosti-skoncil-v-cele-drah-krapinec-a-proc-je-povede-prave-hamplova-296150/)<br>Fakt radost.
- [Anger, Anxiety and Agency | Armin Ronacher's Thoughts and Writings](https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/)<br>„I engage with plenty of people who project confidence in public and are much less certain in private. Many of them are placing bets, but they are talking with confidence about those bets, trying to keep their business afloat while the ground moves under them. They experience that uncertainty from a position where they can act on it, and they are often standing somewhere with a megaphone to get others on their side to improve their odds.“
- ["Už nejsou za exoty." Pečující tátové konečně přišli do módy – Page Not Found](https://pagenotfound.cz/clanek/uz-nejsou-za-exoty-pecujici-tatove-konecne-prisli-do-mody)<br>Super článek o moderním otcovství, který se na věc nezapomíná dívat ze všech stran: „…potřeby otců často zůstávají až na posledním místě, za dítětem i partnerkou. Mnozí zároveň cítí vinu, že zatímco matka tráví s dítětem celý den, oni by měli zvládat práci i péči bez nároku na odpočinek. Kombinace vysokých nároků doma i v zaměstnání podle něj přispívá k partnerským krizím a někteří muži si od tlaku ulevují alkoholem nebo marihuanou.“
- [A Future Worth Entering | Dark Thoughts](https://dark.ronacher.eu/2026/7/16/a-future-worth-entering/)<br>„The idea that my parents could have decided that the Cold War and the possibility of nuclear annihilation were reasons not to have me saddens me greatly. One must not get moral credit for “saving” someone whose existence one prevented, particularly after simply presuming on their behalf that their life would not have been worth living.“
