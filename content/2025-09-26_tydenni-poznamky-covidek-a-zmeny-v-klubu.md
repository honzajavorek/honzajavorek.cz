Title: Týdenní poznámky: Covídek a změny v klubu
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/360
Mastodon-Comments: https://mastodonczech.cz/@honzajavorek/115272345037190486

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2025-09-19_tydenni-poznamky-tyden-pro-digitalni-cesko-tatovsky-vikend-a-nemoc.md) už utekl nějaký ten týden (19. 9. až 26. 9.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
</div>

V pátek jsem se cítil líp, ale pak přes víkend to bylo zase na prd. A takhle to bylo nějak pořád dokola. V pondělí to bylo lepší, ale v úterý jsem zase zalezl do postele.

Udělal jsem si test na covid, ale vyšlo to negativně. Ve středu jsem šel k doktorce a ta mi řekla, že to stejně asi covid byl. Že když se to testuje moc brzo, nebo moc pozdě, tak ten test už nefunguje. A že mi nemá jak pomoct, že mám chodit na procházky a dýchat vzduch a že se moje chrchlání a smrkání musí zlepšit samo.

Potom se to už začalo zlepšovat tak nějak konzistentně. Sice pořád chrchlám a smrkám, ale aspoň už nemám návaly slabosti a hlavu jak balon. Účast na nedělním [půlmaratonu v Blansku](http://blanenskypulmaraton.cz/) jsem zrušil, protože se jednak ani dnes necítím zcela fit, jednak si prostě nemůžu takhle brzo po nemoci dát závod. Budu rád, když si půjdu zaběhat tak za týden, a určitě ne 20 km.

![doge meme]({static}/images/a77wla.jpg)

## Zálohy

Po delší době jsem si udělal pořádek ve fotkách a poté vždycky následuje záloha. Nejen že si přes `rsync` kopíruju soubory na externí disk, ale taky tam mám partition na [Time Machine](https://support.apple.com/cs-cz/104984). Nikdy jsem TM sice nepoužil na obnovení nebo cestování v čase, ale zálohy čas od času dělám, nebo si aspoň myslím, že je dělám 😀

Akorát už mě štvalo, že to trvá 20 hodin, tak jsem začal s ChatGPT řešit, proč to tak je. Radilo mi to nejrůznější příkazy, díky kterým jsme společně zjistili, že se tam (na mechanický disk) kopírují tisícovky miniaturních souborů, a proto to trvá tak dlouho. A co to bylo za soubory?

No všechny ty .venv, node_modules, .git, a podobně z mých vývojářských projektů. Jenže TM umožňuje ignorovat jen konkrétní složky, nejde tam dát _wildcard_. Naštěstí nejsem první, kdo tohle řeší, takže jsem nainstaloval starý, ale stále funkční [asimov](https://github.com/stevegrunwell/asimov). Akorát že jsem ho musel trochu patchnout, aby ignoroval víc složek, protože to neumělo správně detekovat Pythoní věci, nebo tam z dobrých důvodů nebyla .git složka, ale já ji ignorovat chci. Tak snad to bude nějak fungovat.

Té aktuální záloze to rozhodně pomohlo a do desítek minut byla hotová.

## Úklid v klubu

Sice jsem plánoval dělat na newsletteru, ale jak si pro mě na střídačku pořád chodila nemoc, nějak se mi nechtělo se zabrat do takové velké věci a rozhodl jsem se, že by nemuselo být špatné dát po dlouhé době nějakou lásku přímo klubu. Tak jsem vzal koště a začal vymetat pavučiny:

- Oslovil jsem dva lidi, zda by chtěli dělat moderátory a předjednal s dvěma starými, že bych je vyměnil. Oba oslovení lidi souhlasili, takže jsem si je zřejmě vytipoval dobře 😀 A i staří moderátoři souhlasili s výměnou. Vše jsem zprocesoval, starým poděkoval soukromě i veřejně, nové uvítal. Obměna v mod týmu by mohla do klubu přivést zase trochu svěží vítr a narušit _status quo_.
- Hledám v klubu mezi členy dobrovolníka, který by dělal každý měsíc nějakou programovací výzvu. Vybral by téma, třeba „v říjnu tvoříme piškvorky“ a na konci měsíce by se vidělo, co by kdo vytvořil. A další měsíc jiné téma. Koncept ještě ladíme. Zatím se mi hlásí 1,5 dobrovolnice.
- Přidal jsem tři nové role, díky kterým si lidi můžou zakliknout, v jakém ze tří největších českých měst se chtějí potkávat. Zatím to nic nedělá, je to jen experiment. Chtěl bych to pak propojit s místními skupinkami.
- Zrušil jsem privátní kanál #práce-data, který jsem kdysi používal na spolupráci s Czechitas a jiné věci.
- Zrušil jsem roli @Mentoruju a kanál #mentoři, protože se to už nepoužívalo. Teď je #mentoring jako tržiště nabídky a poptávky a funguje to už dlouho jinak.
- Zrušil jsem roli @Mám GitHub, protože byla k ničemu. Dřív jsem myslel, že pak díky ní přes API vytáhnu propojení mezi Discord uživatelem a GitHub profilem, ale v API to bohužel dostupné není.
- Zrušil jsem kanál #projekťáci, kde kdysi dva aktivní lidi vymýšleli, jak by mohli v klubu juniorům vést projekty. Vyšumělo to a oba dnes už mají jiné starosti.
- Zrušil jsem roli „@WebExpo 2022”, protože takové věci se dnes už v klubu řeší skupinkovými vlákny.
- Zrušil jsem zájmovou roli „@Zajímá mě: Softwarová analýza”, protože i když ji mělo hodně lidí, na nic užitečného se nepoužívala a přišlo mi lepší ji nahradit jinými zájmy, viz níže.
- Sloučil jsem kanály #zdraví-mysli a #zdraví-těla do jednoho: #zdraví
- Přeskupil jsem kanály v kategoriích tak, aby to dávalo větší smysl.
- Napsal jsem Veronice z GeekPower, jestli ještě chceme pokračovat s výukou angličtiny v klubu, nebo jak to je.
- Napsal jsem Danovi z CoreSkillu, jestli ještě chtějí využívat Discord pro svoje studenty, nebo jak to je.
- Zvažoval jsem zrušení kanálu #hádanky-šifry, ale nakonec jsem jej vzal na milost.

Pak jsem ještě do #oznámení zhruba napsal, co jsem všechno změnil 😀

## Nový systém pro zájmy v klubu

Už delší dobu se v klubu řešilo, jak pracovat se zájmy - že někoho zajímá Python, jiného bezpečnost, dalšího zase datová analýza… Měli jsme na to asi deset kanálů, ale těch témat začalo přibývat a bylo jasné, že „přidáme další roli a další kanál“ nebude fungovat donekonečna.

Řešením, které se nabízelo, bylo udělat to jako vlákna v kanálu typu forum, kde každé vlákno by bylo nějaké téma. Nabízel by se kanál #skupinky, kde si už teď mohl kdokoliv udělat např. studijní nebo projektovou skupinku na libovolné téma. Jenže toto mělo také své nevýhody. Ve vláknech už nelze dělat podvlákna. A nelze to automaticky propojit s rolemi v rámci Discordího onboardingu tak, jako to jde u kanálů.

Nicméně prodiskutovalo se to dostatečně a cítil jsem, že nic lepšího prostě nevymyslíme a že to musím už nějak rozseknout. Že o tom buď můžeme pořád jen mluvit a já nad tím donekonečna přemýšlet, nebo do toho prostě říznu a něco s tím udělám, i kdyby výsledek nebyl ideální.

Tak jsem šel a přeskupil zájmové role, kanály, a celý onboarding. Mělo to několik fází a musel jsem do bota doprogramovat, aby podle zájmů lidem skupinky nabízel, protože jinak by je neobjevili. Přidal jsem „Matematika a algoritmy“, „C nebo Rust“ a rozdělil „JavaScript a frontend“ na dva samostatné zájmy. Na to jsem musel napsat jednorázový skript, který roli zduplikoval tak, aby ti samí lidi měli místo jedné role dvě.

Bota jsem naučil, aby si všímal, kdo má jaké zájmy a podle toho je přidával do skupinek. Pokud se z nich pak sami odeberou, už jim jen napíše zprávu, jestli to není omyl, ale dál už je nepřidává. Měla by se tím vyřešit _discoverability_, ale zároveň by to nemělo být otravné.

Když bot někoho přidá do vlákna, tak to tam dá systémovou zprávu, a ta způsobí, že se vlákno zobrazuje jako nepřečtené. To jsem tak sice nechtěl, ale po hodinách zkoušení různých způsobů, jak přidávat lidi do vlákna, jsem zjistil, že úplně všechny nějakým způsobem ostatním označí to vlákno jako nepřečtené.

Tak jsem se s tím smířil a beru to teď jako _feature_, protože aspoň ty zájmové „gangy“ uvidí, že mezi ně přibyl někdo nový, a mohou tyto lidi vítat a tak. Nejdřív jsem posílal pro každé přidání jednu zprávu do DM, ale na sobě jsem si vyzkoušel, že to bylo velmi rychle otravné, tak jsem pro lepší UX věnoval jedno celé dopoledne ještě tomu, aby se to sloučilo a když bot člověka přidává do víc míst, tak mu to napíše jen v jedné zprávě.

Pak jsem si ještě napsal skript, který umí podle původního kanálu vytvořit vlákno se „zájmovou skupinkou“, do té nakopírovat pár posledních zpráv z kanálu, přidat tam lidi podle role, a ten původní kanál pak archivovat. Říkal jsem si, jestli je vůbec potřeba to automatizovat, protože těch kanálů bylo asi jenom deset, a možná by to bylo rychlejší ručně, ale nakonec automatizace nelituju, protože těch kanálů i úkonů bylo prostě dost a z těch přesunů bych se jinak asi zbláznil. Během dneška jsem tímhle skriptem všechny zájmové kanály předělal na „skupinková“ vlákna 💪

Tak jsem zvědav, jak to bude fungovat! Je to větší změna ve fungování klubu po docela dlouhé době. Bude to zase trochu jiná dynamika, ale moc se mi líbí, že si teď může kdokoliv založit skupinku na libovolné téma, které lidi v klubu zajímá, a já to pak už jen mohu podpořit rolí v onboardingu, aby to lidi našli.

![Nový onboarding]({static}/images/screenshot-2025-09-26-at-21-10-55.png)

## Videa z akce „AI a junioři: pomocník, nebo riziko?“

SlidesLive nám poslali videa z akce, takže jsme to zkontrolovali, mě se jedna věc nelíbila, tak jim to Kája vrátila, a oni to opravili a máme to už ve skvělé podobě. Poslali to jako soubory, tak jsem si je stáhl (omg, gigabajty!) a nahrál na YouTube a jsou tam!

- [Panelová diskuze](https://www.youtube.com/watch?v=SEktMHmRl98)
- [Praktická přednáška](https://youtu.be/MWcTtMn4COY)

Pak jsem to dal do klubu do #oznámení a [na Mastodon](https://mastodonczech.cz/@honzajavorek/115263713102442945) a Kája napsala e-mail všem účastníkům, kde jim to poslala taky. V dohledné době to ještě protočíme přes LinkedIn. Koukejte, sdílejte!

![Panelovka intro]({static}/images/panel-intro.png)

## Další

-   Mám [nového sponzora na GitHubu](https://github.com/sponsors/honzajavorek/)! Díky Honzo!
-   Přidal jsem do [junior.guru/jobs](https://junior.guru/jobs/) podporu pro [pracovní portál státní správy](https://portal.isoss.gov.cz/irj/portal/anonymous/anonym-base-page#/home). Bohužel tam toho moc není, protože i když asi je nějaká snaha to centralizovat, používá to jen málo úřadů. Ale co kdyby? Po nemoci to byla dobrá rozcvička v programování. Už mi to teda jednou shodilo systém, protože ČOI v Ústeckém se neobtěžovala ani vyplnit popis práce, dali tam jen titulek „informatik“ 🤦‍♂️
-   Předělal jsem junior.guru z Poetry na uv! Díky vibekódění [cluck](https://github.com/juniorguru/cluck) jsem totiž před časem zjistil, že konečně umí namespace balíčky, které na junior.guru mám. Nejobtížnější nakonec bylo dostat tuhle novou verzi na CircleCI, protože tam mají nějakou o něco málo starší, která to ještě neumí.
-   Upgradoval jsem na junior.guru verzi Pythonu a Node.js
-   Řešil jsem těžko rozlousknutelnou chybu `[mkdocs.config] ERROR Config value 'theme': Invalid type <enum 'Sentinel'>. Expected a string or key/value pairs.`, no nakonec jsem přišel na to, že jsem upgradoval `click` a kvůli tomu se nějak rozbilo provolání MkDocs commandů z mého commandu a kvůli tomu nemohly MkDocs najít konfigurační soubor a kvůli tomu mi vyhodily chybu, že je ve špatném formátu 🤪
-   Protože naše akce byla díky Mews na [Luma.com](https://luma.com/eckxgfwc?tk=s7ko8T), a protože je na Lumě čím dál víc akcí, přemýšlel jsem, jak se o takových akcích dovědět, i když mě někdo nepozve. Jinými slovy, jak by mohl bot z junior.guru ty akce sledovat a dávat o nich vědět juniorům. Zatím nejlepší, co jsem našel, je stránka [luma.com/prague](https://luma.com/prague), ale nic zas tak zajímavého jsem tam neviděl, tak jsem to prozatím nechal být a nescrapuju to. Nechám to uzrát.
-   Napsal jsem do ENGETO, proč by měli další rok sponzorovat junior.guru. Napsal jsem do Red Hatu, jak že to s nimi je.
-   Dali jsme si se ženou po dlouhé době [Kosmo](https://www.csfd.cz/film/435776-kosmo/prehled/) a furt je to dobrý. Akorát je trochu děsivé, že i po dekádě je to všechno pořád aktuální.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
-   Za 8 dní jsem při procházkách nachodil 3 km. Celkem jsem se hýbal 1 h a zdolal při tom 3 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

## Plánuji

1.  Dotáhnu ten newsletter, aspoň do nějakého prototypu.
2.  Vymyslím přednášku na říjen, ať ji může Táňa zařídit.
3.  Nepoběžím půlmaraton a nepojedu na FrontKon.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Facebook CEO Demos New Meta AI And It Couldn't Have Gone Worse](https://kotaku.com/meta-ai-mark-zuckerberg-korean-steak-sauce-facebook-2000626808)<br>Tohle je fakt zábavný popis toho, jak se Zuckovi nepovedlo živé demo jeho AI.
- [Anti-*: The Things We Do But Not All The Way - Jim Nielsen’s Blog](https://blog.jim-nielsen.com/2025/my-antis/)<br>Tak co, kolik máte antitabů?
