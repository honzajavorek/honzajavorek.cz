Title: Týdenní poznámky #75: Vylepšování robota
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (22.11. — 29.11.) a tak [stejně jako minule]({filename}/2021-11-21_tydenni-poznamky-74-studium-marketingu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

O víkendu se mi poznámky nechtělo napsat, tak mi to zas přeteklo do pondělí. Ach jo.

## Polský kolega

Odebírám [Rosieland](https://rosie.land/). Nečtu to moc, ale tentokrát jsem to otevřel a bylo tam něco o Rosieland Discordu a pozvánka do něj. Tak tam jdu a v kanálu, kde se lidi představují, vidím hned jako posledního týpka z Polska, nějaký Dawid Zamkowski, který jako Indie Hacker provozuje [Junior Jobs Only](https://www.juniorjobsonly.com/) :D Konečně někdo z východní Evropy a navíc [řeší úplně totéž](https://twitter.com/dawidzamkowski/status/1427888791784759296), jako já!

Tak jsem mu napsal [na Twitteru](https://twitter.com/dawidzamkowski) a půlku pondělí jsme si psali o tom, co děláme a jak nám to jde. Když jsem si původně prošel jeho web, přišlo mi, že to má všechno zmáknuté a je mnohem dál než já. Jenže z konverzace vyplynulo, že dokonce uvažuje nad prodejem projektu, protože na něm nedokáže vytvořit stabilní příjem. Má skupinu na FB, kde má 25 000+ členů, ale nedokáže to monetizovat, podobně jako se o to teď [pokouší](https://cc.cz/holky-z-marketingu-se-meni-na-firmu-z-facebookove-skupiny-je-projekt-ktery-na-pracovnim-trhu-pomaha-tisicum-zen/) například #holkyzmarketingu ([podcast](https://www.youtube.com/watch?v=pXn-WY-zXQY) o tom).

Rozdíl je taky v tom, že není tvůrce obsahu (já píšu texty a dělám to rád) a snaží se stavět věci jen pomocí no-code, nechce programovat, chce ty věci kdyžtak radši koupit. A nevypadalo to, že by se mu chtělo tvořit content, ať už texty nebo videa. Bez programování taky určitě ušetří na prodebugovaných dnech a zbytečných fičurách. Jenže jak potom dát lidem něco unikátního, za co bude mít smysl platit? To upřímně nevím. Udělat pouze placenou komunitu, to mi nepřijde úplně samonosné.

Já píšu příručku a programuju bota, který mé placené komunitě přidává spoustu fajn drobností - nabídky práce se posílají do Discordu, bot oznamuje přednášky, uděluje role, posílá týdenní souhrny, ukládá lidem do soukromých zpráv věci, které si zašpendlíkují, atd. Všechno jsou to custom-made věci, které bych pomocí no-code dělal těžko. Jasně, existuje hromada existujících Discord botů, ale ten můj je prostě na míru a mám plně pod kontrolou, co vše bude dělat a co ne. Nedělám to jen za účelem zisku, dělám to, protože mi na tom záleží, chci aby to bylo dobré a sloužilo to.

A to jsem teda pominul, že lidi mi prostě platí i jen za to, že existuje ta příručka, že jsem ji napsal a dal veřejně na web. Prostě na tom celém vidím, jak kvantita není kvalita a že z no-code a FB skupiny nebo Discordu se nedá jen tak lusknutím prstu vyvařit totéž, co mám já. A to i když opomenu svůj sociální kapitál, který jsem do toho všeho vložil a díky kterému třeba snadno sháním přednášející.

Nasdíleli jsme si nějaké tipy, psal jsem mu o [svém pivotu]({filename}/2021-01-11_spoustim-klub.md). Byznys pro juniory, pokud neděláte kurzy, je minové pole. V Česku zmizelo levio.cz, v zahraničí zase s velkou pompou spouštěli entrylevel.io, ale teď tam vidím akorát rok staré nabídky. Newsletter juniorsintech.com taky skončil. Někomu se ale daří. [Ladybug](https://www.ladybug.dev/) běží, [Emma](https://twitter.com/emmabostian/) prodává [knížky](https://technicalinterviews.dev/). Ale prodávat knížku svému existujícímu obřímu publiku z celého světa, to je trochu specifické.

Myslím, že budeme s Dawidem kamarádi. Blbé je, že si asi nepřečte poznámky, které píšu česky, a překládat mu všechno do angličtiny, do soukromých zpráv, asi nebudu. Spíš si prostě občas napíšeme, jak se komu daří a co je nového. Zatím výsledek [tu](https://twitter.com/dawidzamkowski/status/1463057905985503233).

## Robot na pracovní nabídky a ML

Kamarád [Míla](https://milavotradovec.cz/) se mi připomenul s ML na rozpoznávání juniorních nabídek, že prý kdy to bude dokončené. Napsal jsem mu, je to v zítřejším plánu, bod 34 hned po „naučit se portugalsky“.

Domluvili jsme se, že bych mohl sepsat nějakou roadmapu věcí, které je potřeba udělat, aby ML bylo. A že mi s tím možná Míla pomůže. Že mu budu prostě zadávat práci a on to bude dělat. Tak jsem zvědavý, jak se nám to povede, samozřejmě od toho nic nečekám, ale budu se snažit, aby to bylo aspoň teoreticky možné.

Založil jsem [issue na GitHubu](https://github.com/honzajavorek/junior.guru/issues/737) pro koordinaci práce a rozpracoval tam postup. Pak jsem ho ještě několikrát rozpracoval do podrobnějších bodů. Při tom, když už jsem se zamyslel nad optimalizací načítání starých nabídek práce ze záloh, tak jsem to rovnou udělal.

Po krátkém boji jsem zkrátil načítání z půl hodiny na minutu. Možná jsem to mohl udělat už dřív :D Ale až teď mi červenalo CircleCI častěji a zároveň se to sešlo s tím GitHub issue… no a prostě jakmile je něco promyšlené, někdy je už jednoduché to pak naprogramovat. Myšlení na celý den, programování na 4 řádky.

Problém byl v tom, že aby vznikala kumulující se tabulka s pracovními nabídkami za celou historii JG, musí se stáhnout zálohy databáze z předchozích dní a z nich se nabídky práce přenést do aktuální databáze a napárovat. To je OK, ale záloh je mnoho a jsou velké. Doteď se to stahovalo všechno a trvalo to nekonečně dlouho. Teď jsem přidal podmínku, že když se to bere od nejnovějších po nejstarší, tak pokud už nové pracovní nabídky pocházející ze záloh nepřibývají, přestanou se stahovat další zálohy.

## Robot na Discord

Přeuspořádání místností v Discordu stále prokrastinuji, ale aspoň jsem kouknul na bota. Knihovna discord.py před časem umřela, tak jsem hledal žijící fork. [Tento článek](https://zech.codes/moving-on-from-discordpy) mě nasměroval, nakonec jsem vybral pycord, ale vlastně upřímně ani moc nevím proč. Přišlo mi, že oba hlavní forky jsou na tom stejně, akorát pycord má možná větší following. Ještě jsem objevil [hikari](https://www.hikari-py.dev/), které existuje už dlouho a je dobře udržované, ale to by bylo na přepis všeho co mám.

Přidal jsem se na pycord Discord a začal to sledovat i na Twitteru, ať jsem v obraze. Přece jenom je to teď dost blízko mému core businessu. Přeinstaloval jsem knihovnu a zjistil jsem, že abych měl nejnovější verzi, musím instalovat tzv. „alpha“ přímo z Gitu. Nějaký neoficiální návod jsem díky jejich Discordu našel [tady](https://namantech.me/pycord/). Tož dobrá, co se dá dělat, instaluju z Gitu.

První fičura, kterou měl upgrade umožnit, bylo analyzování Discord threadů. Ty Discord přidal nedávno a můj bot, který běžel ještě na starém discord.py, je přeskakoval, takže v nich nenašel děkovačky ani špendlíky, což jsou zásadní funkce v klubu. Na threadech jsem pak ale spálil hodně času prostě proto, že mi nešlo vymyslet, jak se na ně mám vůbec dostat, hlavně i na archivované thready atd. SDK nebylo úplně přímočaré v tom, jak ze startovací zprávy získat thread, a to ani nemluvím o tom, že jsem si musel domyslet, že thread je pak vlastně totéž, jako kanál.

Když se mi to povedlo zlomit, nakonec jsem musel vyřešit, jak efektivně zpracovávat kanály a potom stejným způsobem i thready. Skript byl poměrně sekvenční, chtěl jsem jej zrychlit. Naučil jsem se trochu víc asyncio, hlavně `asyncio.gather()` a `asyncio.Queue()`. Super bylo, že mi stačilo najít tu frontu a v Python dokumentaci byl přímo příklad, jak to mám celé udělat. Zase jsem mohl využít svůj VŠ titul, a zase nic, je z toho zase copy-paste z dokumentace. Vytvořil jsem frontu, workery, prošel kanály a když jsem narazil na thread, ten jsem za běhu přihodil do té fronty. Celé to teď místo 4 minut trvá 1 minutu, a to ten skript prochází mnohem víc zpráv než předtím.

Poslední věcí byl přechod na timezone-aware datetimes, které teď pycord používá. Převedl jsem je zpět na naivní datetimes, protože se s nimi jednodušeji pracuje a dají se uložit do SQLite. Stejně je to všechno v UTC. Pycord (zatím?) nemá migrační návod, tak jsem musel čerpat i z [návodu nextcordu](https://nextcord.readthedocs.io/en/latest/migrating_2.html), kde mají stejné změny.

Když už jsem byl u optimalizací, zrychlil jsem i načítání avatarů (tam byla zase u pycord změna a dokonce i nějaké zjednodušení kódu, nemusím už ručně rozpoznávat, zda jde o výchozí Discord avatar, nebo nastavený). Naopak zpracovávání špendlíků se mi zrychlit nepovedlo, muselo by se to celé přepsat a na to jsem se teď vykašlal, jde jen o dvouminutový skript.

Nakonec jsem si po všech těch změnách všiml, že bot uživateli Jarda odebral roli, kterou získá, když má představení a avatar. Přitom Jarda avatar i představení má. Toto jsem řešil půl hodiny, než jsem si všiml, že Jardové jsou v klubu dva. No nic.

Během změn v botovi jsem upravil i způsob logování informací. Na CI jsem vypnul _debug_ výpisy. Ty mám zase zapnuté na lokálu, když vyvíjím. Do _debug_ si dovolím házet i nějaké specifické informace, například IDčka, názvy threadů a kanálů, atd., ale do _info_, které se zobrazuje na CI, už dávám pouze vágní nebo agregované info o tom, co se zhruba děje. Nechci, aby mi do CI logů zbytečně ucházela data z klubu.

## Dokončování článku pro Heroine

Místo prvního odstavce jsem měl u odevzdaného článku napsáno „bla bla bla, stejně redakce napíše lepší úvod“, ale to mi neprošlo, tak jsem to ještě v průběhu týdne dopisoval. Článek, který jsem se snažil [podpořit anketou na Twitteru](https://twitter.com/honzajavorek/status/1463589379390193664), vyšel v pátek: [Chcete začít programovat a nevíte kudy do toho?](https://www.heroine.cz/zeny-it/6682-chcete-zacit-programovat-a-nevite-kudy-do-toho) Potěšilo mě, že tentokrát se nemuselo seškrtat skoro nic a dokonce se do postranních boxíků vlezlo i to, co jsem myslel, že se nikam nevleze.

Taky jsem psal další článek. Psal jsem ho pozdě, měl termín v neděli, odevzdal jsem ho v úterý. Ale dovolil jsem si to, protože i vydávání článků mělo skluz. Nikdo neprotestoval. Kdy vyjde, to zatím nevím.

## Změna brandingu na sociálních sítích

O víkendu jsem se rozhodl „relaxovat“ tím, že uvedu v realitu něco, co mi šťouralo už delší dobu v hlavě v návaznosti na mé předchozí studium marketingu. Řekl jsem si, že informace o JG přesunu víc na svoje osobní profily. JG je tak či tak pevně spjato s mou osobou a od začátku se nijak nebráním tomu, abych brand propojoval. Rozhodl jsem se to tedy propojit důrazněji.

Nahrál jsem si na většinu sociálních sítí nový profilový obrázek. Použil jsem svou starou fotku z jedné ze svých přednášek, kterou jsem už stejně používal v záhlavích, tuším na Twitteru a LinkedIn. Ve [Photopea](https://www.photopea.com/) jsem se vyřízl a udělal tam bílý okraj, na pozadí jsem dal žlutou barvu z JG. Výsledkem je moje fotka, neutrální, ale barvou brandovaná do JG. Podvědomě budu svou přítomností na sociálních sítích dělat JG reklamu, případně někoho bude zajímat, co je to za žlutého blázna, a můj profil si spíš rozklikne. Taková výrazná žlutá se totiž na profilovkách moc nevyskytuje, takže je to vidět a je to jasně rozpoznatelné.

Taky jsem zapracoval na „cover“ obrázcích. Vytvořil jsem je všechny v Keynote jako slajdy a exportoval jako obrázky. U některých profilů si to vzalo dost ladění. Části cover obrázku jsou na různých místech totiž zakryté, někdy je to i v různých kontextech na různých místech. FB zase k obrázkům zdola přidává jakýsi hnusný přechod, který funguje možná dobře na fotky, ale ne na jednobarevné věci s ilustracemi. Nejtěžší to bylo asi na LinkedIn, kde je velmi úzký pruh a na mém profilu je překrytý mou fotkou vlevo, ale jinde je fotka uprostřed. Takže jsem dal doprostřed kuře tak, aby se přesně na pixel zakrylo mou fotkou v tom druhém případě. Prostě piplačka.

Proč to má smysl? Jednak se na sítích dost vyskytuji a je škoda to nevyužít k propagaci JG. Každý z nás si někdy dal rámeček, že volí Zelené, nebo že je „open to work“ na LinkedIn, tak tohle je jen jiná varianta téhož. Vaši profilovku nebo profil samotný vidí spousta lidí a je škoda jim neříct, co mě živí, když už tam jsou, třeba to využijí, nebo o tom někomu řeknou.

Sociální sítě mají zároveň tzv. organický dosah a placený dosah. Když jsou nové, mají velký organický dosah (ukazují příspěvky hodně lidem a ty se snadno šíří), ale časem se to vždy utuží a za šíření se musí platit. Pokud jste stránka na FB, dnes už se prakticky žádný váš status nedostane k víc jak pár lidem, pokud za to nezaplatíte. Dá se to ale hacknout tím, že používáte věci, které sociální síť chce, abyste používali. Například Instagram teď preferuje videa a ukáže je více lidem. Facebook preferuje osobní profily a skupiny. Takže budu víc psát na osobní profil a méně na specializované JG profily. Ostatně, na Twitteru to tak mám od začátku.

O FB skupinu se nechci starat a moderovat ji, nebo tam budovat jakoukoliv komunitu. Na to mám klub. Zároveň ji nemůžu smazat. Je tam 800+ lidí, FB preferuje skupiny, interakce s novinkami o JG tam celkem je. A lidi tu skupinu hlavně nacházejí přes klíčová slova a sami se do ní přidávají. Je to vlastně takový SEO lapač, ale na FB. Tak jsem ji přepnul do „módu pro čtení“. Všechny příspěvky musím nejdřív schválit. Obrázek a popisek jsem změnil tak, aby jasně vedly na JG. Ještě bych mohl přidat nějaké oznámení jako uvítání nebo nějaká pravidla pro vstup, ale s tím si pohraju jindy. V podstatě bude skupina fungovat jako by měla fungovat FB stránka, ale na rozdíl od FB stránky moje posty FB dokonce aspoň pošle pár lidem.

Svůj osobní profil na FB jsem pročistil a ve své hlavě jej mentálně přepnul spíš do něčeho, jako je můj Twitter. FB kdysi bylo místo, kde jsem se bavil se svými kamarády a dovídal se o tom, co dělají, ale už dlouho tím místem není. Využil jsem funkce archivace příspěvků a všechno před rokem 2019 jsem archivoval, tedy nesmazal, ale nejde to už vidět. Bylo to nekonečné klikání v administraci a objevil jsem při tom mnoho vzpomínek. Je škoda, že se z FB stalo co se z něj stalo, ale to už nejde vrátit. Část mých kamarádů už si jej smazala úplně. Já už delší dobu měním svůj přístup k tomu, co tam píšu. Tento víkend byl jen završením této změny. Nebude z toho „reklamní prostor“, normálně jsem tam pořád jako Honza Javorek, i když teď teda budu víc psát o JG i přímo na osobním profilu. Budou pokračovat ilustrované statusy o tom, jak něco sháním, stále budu diskutovat a normálně tu síť používat. Jen budu profil brát víc jako místo, kde mohu něco propagovat, než kde mám fotky z vysokoškolských párty. Jiné než veřejné příspěvky psát už nebudu. Jak jsem už psal, prostě jako Twitter.

Ještě musím lidi přesměrovat z firemních profilů na moje osobní. To bude nejhorší na IG, kde mám 700 followerů, zatímco Honza Javorek má 150. Myslím ale, že je to dobrý tah a měl bych to udělat raději dříve než později. Např. i Heroine když propaguje články, propaguje tam můj profil, ne JG. Dává prostě smysl spojit to se mnou a informovat o JG na svém vlastním profilu jako o něčem, co dělám a případně přidat i něco ze zákulisí.

## Jakub a memy

Minule jsem psal, jak se navzájem dobíráme s [Jakubem Mrozkem](https://jakubmrozek.cz/). To dobírání si s sebou nese spoustu kontextu. Lidem, kteří nečtou naši soukromou Messenger konverzaci (ahoj Zucku), to může vyznít všelijak, tak bych tady chtěl jen zmínit, že já Jakubovi závidím, že může číst knihy jak na běžícím páse, nesměju se mu za to. Četl bych taky.

Taky rozumím tomu, proč věci dělá tak jak je dělá, má k tomu své dobré důvody. Můžu se smát memům, ale mega mu držím palce. Kdyby existovala jedna cesta k úspěchu, tak JG neexistuje, protože po ní rozhodně od začátku nešlo, nedrželo se všech pouček. Vždy je potřeba dělat věci v kontextu, ne slepě opakovat poučky, i když na memu vypadají dobře. Já sám jsem se provinil hned několika věcmi, ze kterých si Dagobert dělá v memech srandu, přitom JG existuje a roste.

## Komunikace s firmami

- Volal jsem si s CDN77 a vymýšleli jsme, jak budeme dál spolupracovat.
- Byla schůze výboru [Pyvce](https://pyvec.org/).
- Psal jsem si s Engetem kvůli videím a dalším věcem. Budeme si volat.
- Psal jsem jedné firmě, zda chce prodloužit logo na příručce.
- S Mews jsme řešili přikoupení dalšího vstupu pro dalšího člověka do klubu.

## Další poznámky

- Řešil jsem s Czechitas nesrovnalost v API, kterým jim dávám data z pracovních nabídek. Druhá strana je v práci zaneprázdněna probíhajícím Black Friday, takže výsledek debugování se dovím později.
- Se Soňou jsme si domluvili [detaily příští přednášky](https://junior.guru/events/#planned).
- Domlouvali jsme prvního hosta do podcastu pod hlavičkou JG.
- Zkoušel jsem dvě různé aplikace na podcasty s tím, že snad bude aspoň jedna méně blbá než Spotify: [Overcast](https://overcast.fm/) a [Pocket Casts](https://www.pocketcasts.com/). Vítěze zatím nemám, ale méně blbé než Spotify jsou obě.
- Během 8 dní od 22.11. do 29.11. jsem při procházkách nachodil 11 km, na túrách nachodil 8 km. Celkem jsem se hýbal 7 hodin a zdolal při tom 19 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Pověnovat se uspořádání klubu, kde už se delší dobu hromadí nápady na změny. Nadělit klubu vánoční dárek.
2. Doladit způsob, jakým budu propagovat věci na sociálních sítích a zpropagovat přednášku Soni.
3. Napsat čtvrtý [článek pro Heroine](https://www.heroine.cz/zeny-it/).


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Tento týden jsem nepřečetl nic, co bych [sdílel na Pocketu](https://getpocket.com/@honzajavorek). Toto se stalo poprvé! Snad se to nebude opakovat.

Poslouchám teď dost podcasty, ale ty nikde nesdílím, i když se mi líbí. Zkusím ručně sepsat pár náhodných doporučení bez dalšího komentáře: Hlas Heroine, Prostor X, Moderná firma, Lepší města, Přepište dějiny, Bourání, Fall of Civilizations.
