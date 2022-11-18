Title: Týdenní poznámky #35: Obchodní podmínky a tak
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (25.1. — 29.1.) a tak [stejně jako minule]({filename}/2021-01-22_tydenni-poznamky-34-eureka-clenstvi-vyreseno.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Nastavování Memberful

Jak jsem psal minule, pro správu členství v klubu jsem vybral jsem hotové řešení, [Memberful](https://memberful.com/). Tento týden jsem strávil dost času propojováním a nastavováním.

- Lokalizoval jsem všechny e-mailové šablony v Memberful. Je jich 14 a každou jsem upravil tak, aby byla osobní a česky vysvětlovala, co se děje a co má příjemce udělat. Bohužel Memberful češtinu přímo nepodporuje, takže některé části, které nemohu přepsat, se budou posílat v angličtině a výsledek bude tedy česko-anglický.
- Nastavoval jsem branding Memberful tak, aby ladil s JG
- Nastavoval jsem tam vše ostatní - nabídku, kupóny, všechna zaškrtávátka, odkazy.
- Integroval jsem Memberful s webem a toto jsem si připravil do vedlejší větve. Jedna z mála situací, kde jsem narušil trunk-based development a odvětvil jsem, protože se mi nechtělo řešit nějaký feature switch. Větev by stejně měla existovat jen do chvíle, než se finalizují obchodní podmínky.
- Díky tomu jsem také využil per-branch deployments, které mi dělá Vercel. Už delší dobu jsem myslel, že bych mohl zmigrovat na GitHub Pages, protože z pokročilých funkcí Vercelu vlastně nic nepoužívám, ale protože to zatím funguje, tak bylo snazší nic nedělat a zůstat, než někam odcházet. Teď jsem využil něco, co GitHub Pages nemají, a to deployment/náhled pro git větev. Náhled jsem mohl poslat i právničce, aby si mohla zkusit založit testovací členství. Samozřejmě mi tam našla nedostatky.
- Na [stránku o klubu](https://junior.guru/club/) jsem si připravil tlačítka pro zakoupení předplatného a další odkazy. Hodně se mi líbí, [jak to mají na WIP.co](https://wip.co/join), ale to asi až v nějaké další verzi. Přidal jsem i nějaké informace, např. "Jsou údaje o mé platební kartě v bezpečí? Jasně! K údajům o tvé kartě nemá nikdo z junior.guru přístup, jsou bezpečně uchovány platební bránou Stripe. Je to světoznámá služba, která má hromadu zabezpečení a certifikátů." Za takto vágní větu mě asi [Michal Špaček](https://www.michalspacek.cz/) nepochválí, ale myslím, že normálním smrtelníkům by mohla stačit.
- Připravil jsem stránku pro [obchodní podmínky](https://junior.guru/tos/).
- Připravil jsem stránku pro [pravidla chování](https://junior.guru/coc/) a naházel do ní text, který jsem měl doteď jen v Google dokumentu. Odkazy na pravidla jsem aktualizoval všude na Discordu.
- Přeložil jsem formulář na zadávání pracovních nabídek do češtiny. Stejně to tam zadávali pouze česky mluvící lidé. Původně jsem myslel, že by se to mohlo dostat do ruky i cizincům pracujících ve větších firmách, ale reálně se to neděje a právnička bude mít klidnější spaní. Provozovat dvě verze mi přišlo zbytečné. Překlad políček se mi vůbec nelíbí, protože místo "website link" tam teď mám "odkaz na webové stránky firmy" nebo místo "pricing plan" tam mám "varianta z ceníku". Zní to hrozně. Překládal jsem to ale hladový ve vlaku, není to zas tak podstatné a už je pátek, tak to tak teď nechám. Horší spíš bylo, že kvůli přejmenování políček se mi rozbily věci na backendu, které data z Google Sheets stahují, takže jsem to musel ještě opravit v kódu i v testech. Do formuláře jsem přidal zaškrtávátka k souhlasům s obchodními podmínkami a zpracováním osobních údajů.
- Zkoušel jsem, jestli funguje placení testovací kartou a jak fungují různá přesměrování z Memberful zpět na mé stránky.
- Na radu právničky jsem dal do patičky webu přímý odkaz na kontakt. Dává mi to smysl, vlastně ani nevím, jak se mi povedlo tam takový odkaz nemít :D Nicméně zatím vede jen na stránku s ochranou osobních údajů, kde je na mě kontakt v prvním odstavci. Ještě nějaký kontakt je i na stránce pro média, takže je v tom binec a poznamenal jsem si, že teď do toho šťourat moc nebudu, ale v budoucnu v té patičce musím pouklízet.
- Poslal jsem právničce detailní soupis toho, jak skrze JG protékají osobní údaje, aby mohla vytvořit nový a lepší text ke [zpracování osobních údajů](https://junior.guru/privacy/). Ten, co mám teď, jsem si napsal laicky sám.


## Clubhouse

Dostal jsem pozvánku do Clubhouse, ale zatím jsem si nenašel moc čas se tam porozhlédnout a něco si pořádně poslechnout. První dojmy?

Než jsem se tam dostal, zjistil jsem si něco o této nové sociální síti. [Tento tweet je pojat jako mem](https://twitter.com/honzajavorek/status/1354116768671870979), ale asi moc nezafungoval, protože moc srdíček nedostal. Zároveň je však myšlen i výsledek mého bádání. Odkazované video perfektně ukazuje, k čemu se může Clubhouse hodit a vidím díky němu potenciál, který tato nová síť vytváří. Odkazovaný článek zase popisuje, jak český Clubhouse ve svých počátcích vypadá kvůli tomu, že se šíří přes pozvánky. Jestliže se Twitter šířil přes geeky a ajťáky, Facebook přes studenty na Erasmu a Instagram přes teenagery, tak Clubhouse je jako byste dali mikrofon svému [feedu na LinkedIn](https://twitter.com/yablko/status/1329013868149043201). Osazenstvo je silně nahnuto směrem k markeťákům a influencerům. Je na vás, zda vás baví představa, že posloucháte rozhovor Petra Máry s Petrem Ludwigem o tom, jak a komu ukápla zmrzlina na botu, nebo vás to spíš odpuzuje.

Nežiju se sluchátkama na hlavě, takže pustit si nějaké povídání do uší je pro mě velmi vědomá činnost na kterou si musím vyhradit čas, pro kterou potřebuji konkrétní situaci v bytě a před kterou musím udělat hned několik úkonů. Je to asi jako kdybych si měl jít pustit gramofon. Myslel jsem, že jsem dobu dohnal, když jsem po letech odmítání trochu pronikl do světa podcastů, ale teď přichází nový level, Clubhouse. No uvidíme.

Co mě zarazilo, byla touha, s jakou Clubhouse chtěl všelijaké moje osobní údaje. A rovněž to, že jsem o tom nikde nezaznamenal absolutně žádnou diskuzi. Pozvánku nedostanete jinak, než poskytnutím svého telefonního čísla. Aby vám ji vůbec mohl někdo poslat, musí aplikaci poskytnout přístup ke všem svým kontaktům v telefonu. Jméno musí být jméno a příjmení, ne přezdívka. Myslel jsem, že po všech průserech Facebooku a spol. se v roce 2021 už vracíme k ochraně soukromí a přezdívkám (Reddit, Discord), ale zjevně i dnes může vzniknout nová a oblíbená sociální síť, která prakticky nefunguje, dokud o vás neví úplně všechno.

Paradoxně díky tomu, že kontakty mám do mobilu jen načtené z Google Contacts, mohl jsem je snadno odpojit před tím, než jsem někomu poslal pozvánku. Po odpojení se můj seznam kontaktů vyprázdnil, já si tam ručně přidal jen danou osobu, pak aplikaci povolil přístup, poslal pozvánku, v nastavení přistup zase odebral a kontakty opět připojil.


## Další poznámky

- Přidal jsem do [seznamu podporovatelů](https://junior.guru/donate/#sponsors) Miu! Díky!
- Upgradoval jsem závislosti na svých a Pyvec webech.
- Otestoval jsem mezi prvními [2FA na Fakturoidu](https://www.fakturoid.cz/podpora/nastaveni/dvoufazove-overeni).
- Četl jsem pár článků o tom, jak budovat komunity. Sleduji po očku také [Indie Hackers]() apod. Napadlo mě ale, že jsou to všechno nějací amíci a ti řeší prostě jiné problémy, než řeším já. Rád bych sledoval nějaké místní solo tvůrce, nebo aspoň nějaké ze střední/východní Evropy. Na [můj dotaz](https://twitter.com/honzajavorek/status/1354735756892319745) ale zatím nikdo neodpověděl :D Ach jo.
- Poslechl jsem si nové fajn [video o pracovních pohovorech](https://twitter.com/yablko/status/1354079536078581765) od yablka. Chtěl bych časem nějaká jeho videa vložit i rovnou do příručky, ale teď to nestíhám.
- Vytvořil jsem [repozitář pro grafický manuál](https://github.com/honzajavorek/logo.junior.guru) a zprovoznil jsem [logo.junior.guru](https://logo.junior.guru/). O tom jsem ale už napsal [samostatný článek]({filename}/2021-01-28_graficky-manual.md). Když jsem se koukal na stránku pro média, zapsal jsem si, že v budoucnu tam musím změnit texty, protože už mi přijdou zastaralé (vytvářel jsem ji myslím napodzim, hehe).
- Začala mi padat performance na stránce o klubu ([kontroluju kontinuálně přes Lighthouse]({filename}/2020-05-11_monitoring-performance-with-lighthouse-and-circleci.md)), ale rozhodl jsem se, že to zatím nebudu řešit. Až mergnu úpravy, které mám teď ve větvi, tak to poladím.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Dokončit obchodní podmínky a spustit klub! Otestovat na prvních lidech.
2. Věnovat se závazkům, které mám k pár dalším firmám a lidem (napsat jedné velké firmě, vytvořit banner, napsat článek).
3. Propagovat otevření klubu na sociálních sítích.

A ještě bod-nebod: Neměnit hlavní stránku, neuklízet v patičce, nepřepisovat texty, nic nemigrovat, prostě na nic na webu nesahat, dokud neuvidím, že lidi se hlásí do klubu a má smysl do čehokoliv z toho investovat energii a čas.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [V případu otravy Bečvy policie vyšetřuje, kdo dal Deníku Referendum informace](https://denikreferendum.cz/clanek/32203-v-pripadu-otravy-becvy-policie-vysetruje-kdo-dal-deniku-referendum-informace)<br>Bečva houstne. Je PČR nezávislá? Deník Referendum spekuluje, že ne, a posílá věc na GIBS.
- [ARAGORN vs. Toxic Masculinity](https://www.youtube.com/watch?v=pv_KAnY5XNQ&feature=youtu.be)<br>Proč je Aragon tak skvělý hrdina? Netrpí toxickou maskulinitou. Skvělé video, na kterém by mohl toxickou maskulinitu pochopit každý. "You can decapitate orcs and write poetry. They're not mutually exclusive."
- [Who Invented the Alphabet?](https://www.smithsonianmag.com/history/inventing-alphabet-180976520/)<br>Abecedu nejspíš vynalezli horníci, kteří neuměli hieroglyfy.
- [WhatsApp loses millions of users after terms update](https://www.theguardian.com/technology/2021/jan/24/whatsapp-loses-millions-of-users-after-terms-update)<br>Exodus z WhatsApp
- [Clubhouse je nikdy nekončící konference v pekle](https://a2larm.cz/2021/01/clubhouse-je-nikdy-nekoncici-konference-v-pekle/)<br>Velmi pobavilo!
- [Replicating The In-Office Experience Remotely Doesn’t Work. Here’s Why.](https://www.inc.com/rebecca-hinds/simply-replicating-in-office-experience-remotely-doesnt-work.html)<br>Nepřenášejte 1:1 svou původní firemní kulturu do online světa. Budete mít akorát více zbytečných meetingů. Dokumentujte způsob, jakým komunikujete. Nepřekračujte s hovory 30min, delší z člověka totiž dělají zeleninu. Naplno se ukazuje, že firemní kultura není pingpongáč, ale hodnoty, naslouchání lidem, opravdovost. Propálený čas ≠ výkon.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
