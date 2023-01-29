Title: Týdenní poznámky #89: Podcasty v klubu a mentoring
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl zase nějaký ten týden (30.4. — 6.5.) a tak [stejně jako minule]({filename}2022-04-29_tydenni-poznamky-88-pyvec-a-nova-stranka-do-prirucky.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tentokrát píšu ve vlaku. Musím říct, že vnímám značný rozdíl mezi tichým oddílem, na který jsem býval zvyklý, a dětským oddílem. Hraje mi tu třeba Sandokan.


## Fonty v obrázcích

Na JG používám obyčejný bezpatkový font. Když generuju různé obrázky u sebe na počítači, je to s Helveticou a texty jsou krásné. Když se ale generují na CI, použilo to nějaký linuxový font a texty byly hnusné. Takže jsem se snažil na ten Linux nainstalovat aspoň Arial z nějakého balíku MS fontů, ale to:

- Trvalo dlouho a častokrát se to nedařilo napoprvé (selhalo stahování), takže jsem tam měl 3x retry v Bashi.
- Pořád nevypadalo nejlíp a hlavně to pořád vypadalo jinak, než plakátky vygenerované u mě na počítači.

Dřív jsem hledal, jak dostat na CI tu Helveticu, ale teď mě napadlo něco jiného. Zadal jsem do vyhledávače „most helvetica like free font“ a našlo to [tento článek](https://learnui.design/blog/helvetica-similar-fonts.html), kde jsem se dověděl o fontu Inter. Ten vypadá docela dobře.

Zatímco na webu je mi přednější rychlost načítání než hraní si s fonty, u těch obrázků generovaných z HTML mi dává smysl natvrdo font určit a sjednotit jej mezi CI a mým počítačem. Nainstaloval jsem tedy ten Inter [jako balíček z npm](https://www.npmjs.com/package/@fontsource/inter) a bylo to!

No samozřejmě, že ne. Aby mi při generování obrázků fungovalo kompilování SCSS apod., dějou se tam čachry s temporary adresářem a kopírování věcí sem a tam. Přidat do toho fonty byl hrozný guláš a zabralo mi celé jedno dopoledne odladit to tak, aby se v těch náhledech dal použít jak font z Bootstrap Icons, tak tenhle Inter. CSS v těch fontových balíčcích používají relativní cesty k .woff souborům. Ty cesty se ale při importu do SCSS přenesou do výsledného CSS souboru tak jak jsou, takže pak by font musel být „na produkci“ ve stejně pojmenovaném adresáři a ve stejné struktuře, což by způsobilo strašný nepořádek. Nakonec jsem prostě nakopíroval soubory a to CSS regulárem přepsal, nic lepšího mě nenapadlo.


## Oznámení epizod podcastu v klubu

K těm fontům jsem se dostal tak, že jsem pracoval na plakátcích k jednotlivým epizodám podcastu. Chtěl jsem je dát do XML podcastu, ale nelíbilo se mi, jak vypadají. Když jsem měl fonty vyřešené, zase jsem si uvědomil, že se tam ty plakátky moc nehodí a nakonec jsem do XML k epizodám dal zatím jen obrázky jednotlivých hostů :) Ty jsem přidal i na [stránku podcastu](https://junior.guru/podcast/), ať se v jednotlivých dílech lépe vizuálně orientuje.

Pak stačilo udělat skript, který oznamuje nové podcasty do klubu. To už bylo jednoduché, takových skriptů tam mám už víc. Při té příležitosti jsem ale upravil YAML s daty o podcastu tak, že se do něj dá zapsat délka zvukových souborů a další data potřebná pro XML s podcastem. Tato data jsem předtím zjišťoval stahováním jednotlivých dílů a jejich analýzou, ale trvá to dlouho a jak je dílů stále víc, je to otravné. Teď se to stáhne jen pokud to skript nenajde v YAMLu a potom mi to do logu vypíše přesně řádky, které mám do YAMLu přidat, aby se to stahovat nemuselo. To mi umožňuje ručně optimalizovat tempem, jaké je mi příjemné. Když nebudu mít moc času si s tím hrát, můžu díl publikovat i bez toho. Když budu mít vše v YAMLu, skript proběhne super rychle.

Pak jsem si všiml, že se mi plakátky vždy přegenerují, ačkoliv by se měly cachovat. Klíč ke cachování obsahuje data, která posílám do HTML šablony pro obrázek s plakátkem. Ta data obsahují databázový objekt s epizodou podcastu. Ten obsahuje atribut `._dirty`, kde si Peewee udržuje informace o tom, jaké atributy byly změněny. Je to množina. A když se množina prožene přes pickle a pak se to ukládá jako string, mohou prvky v té množině být v náhodném pořadí, pokaždé jinak. A to způsobovalo, že byl klíč ke kešování vždy jiný :D Rozebral jsem traktor a udělal jednořádkovou změnu, která to opravila.


## Scheduled Events na Discordu

Upravil jsem skript na akce v klubu, aby uměl z dat v YAMLu eventy na Discordu nejen zakládat, ale i aktualizovat. U toho jsem si všiml, že mohu k eventu přidat i obrázek. Říkám si, že když už do toho vrtám, tak to udělám, ale nepřišel jsem na to jak. Je to zas nějaký úplně jiný způsob, než co mi fungovalo kdekoliv jinde v discord.py/py-cord knihovně. Ptal jsem se na py-cord Discordu, ale nic, takže jsem založil [dotaz na Stack Overflow](https://stackoverflow.com/q/72134026/325365).


## Mentoring

Byl jsem v Karlíně u Pure Storage a probírali jsme, jak bude vypadat středeční event v klubu, kde chci členům připomenout, jak v klubu funguje mentoring, co to obnáší, co to je a co to není, a představit nové mentorky a mentory z Pure Storage. Posezení to bylo moc fajn a vše důležité jsme probrali, dostal jsem i dost nepřímých podnětů, co by šlo vylepšit.

Sepsal jsem anotaci k eventu a publikoval, ať už je v klubu k dispozici informace s plakátkem pro členy, že akce bude a o čem to bude. Také jsem sepsal status na sociální sítě o našem partnerství a o mentoringu v klubu.

Následně jsem se shodou okolností viděl na kafi i s Janem Meissnerem z Mews, s nímž jsme původně celý 1:1 mentoring v klubu vymysleli a rozjeli. Získal jsem od něj další feedback na to, jak to funguje nebo jak by to fungovat mohlo a domluvili jsme se, co dál a že udělám podobné intro ještě jedno i s jejich mentory (to jsem sám nabídl, protože mi to dává velký smysl). Zpětná vazba z Mews je super v tom, že už je skoro po roce provozu a dá se u toho poučit z reálného chování lidí.

Zároveň jsem nedávno byl na mezikomunitním setkání, kde se téma mentoringu řešilo a mám z toho spoustu poznámek. No a tohle všechno teď dávám dohromady do jednoho kastrólu ve své hlavě a míchám a do středy bych chtěl vymyslet nějaký mentoring 2.0, který bych na tom večerním eventu oznámil.

Udělal jsem o tom i vlákno přímo v klubu, v kanálu #nápady-klub, kde se ptám na zpětnou vazbu i členů. Myslím, že bude důležité hlavně pojmenovávat věci správnými slovy a dát mentoringu nějaký rámec a nastavit společná očekávání co to jakože vlastně vůbec je, na co to slouží a na co ne.

Jestli to celé dám dohromady do středy? Bude to celkem výzva, ale když se to celé tak sešlo, asi v blízké době nebude lepší moment, kdy to zkusit posunout na jiný level.


## Streamování na YouTube

Discord má limit 25 lidí na callu, pokud se používá video. Vymyslel jsem [zrcadlo](https://junior.guru/speaker/), které to řeší, ale pro speakery je to divné a neintuitivní, navíc přenáším limitace své platformy na ně.

Alternativní řešení by mohlo být streamovat přednášku na YouTube a kdo se nevleze, odsleduje aspoň tam. [Nastudoval jsem si](https://www.youtube.com/watch?v=AtipBVW4vxA), jak se to s OBS dělá a když jsem to chtěl konečně vyzkoušet, napsalo mi YouTube, že fičura streamování se zapíná 24 hodin a mám den počkat. Takže jsem to nevyzkoušel, zapne se to (snad) až během dnešního odpoledne ¯\\\_(ツ)\_/¯

Během čtení věcí o streamování jsem ale narazil na [info o tom, že na macOS se v OBS hodně seká obraz při nahrávání konkrétního okna](https://www.reddit.com/r/obs/comments/kobcy6/window_capture_on_osx_is_laggy/), což je přesně to, co dělám a u čeho se mi obraz fakt seká. Myslel jsem, že to je tím „zrcadlem“, ale když jsem koukal na starší záznamy, tam se to seká taky. Takže jsme si tam toho jenom všimli, ale je to něčím jiným. Důvody sekání jsou nejasné, na macOS prostě OBS v tomto případě nevymáčkne lepší kvalitu.

Lidi to obcházejí různě. Buď mají Windows, nebo externí displej a nahrávají ho celý, protože v takovém případě OBS z macOS vymáčkne víc. Má to ale zase jiné nevýhody. Taky jsem objevil něco, co se jmenuje OBS Ninja, teda dnes už [VDO Ninja](https://vdo.ninja/). Trochu jsem si to proklikával, ale najít adekvátní řešení je asi na dlouhé lokty a mnoho zkoušení různých kombinací. Navíc se všechno postupně mění s vydáváním nových macOS i nových OBS, takže třeba [toto video](https://www.youtube.com/watch?v=z3uDpGMzHCg) už je jakože zastaralé a nedá se v tom vyznat.

Teď je ale priorita streamování, tak to vyzkouším co nejdřív. Nejbližší akce v klubu je ve středu. To sekání je nepříjemné, ale jestli je na 10 předchozích záznamech, tak se asi svět nezboří, když bude i na jedenáctém. Aspoň jsem poladil vzhled YouTube kanálu a některé popisky tam. Moc jsem to ale nepřeháněl, spíš update, než revoluce.


## Aj ty v IT

Poslouchal jsem v parku podcast [Steet of Code](https://wp.streetofcode.sk/podcast/dievcata-a-zeny-v-it/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=dievcata-a-zeny-v-it) a byla tam nějaká Veronika Pizano z [Aj ty v IT](https://ajtyvit.sk/). Strašně se mi líbilo, co tam říkala a byl jsem nadšený snad z každé věty. Přidal jsem si ji hned na LinkedIn a ve zprávě podcast chválil. Nezávisle na tom jsem se přidával na Aj ty v IT Discord (přidával jsem se hned na několik podobných Discordů). Tam mě uvítala nějaká Veronika. Chvíli mi to trvalo, ale nakonec jsem si spojil, že jde o stejnou osobu :D Každopádně jsme se začali bavit o tom, zda můžeme nějak spolupracovat. V pondělí si budeme volat.

Opět nezávisle na tom jsem na LinkedIn narazil na CEO Aj ty v IT Petru Kotuliakovou a přidal jsem si ji, protože jsem chtěl číst její statusy a dovědět se víc o lidech, kteří jsou v čele Aj ty v IT, resp. srovnat si to třeba s Ditou z Czechitas. Petra mi hned napsala a je dost možné, že se uvidíme v Praze.

Nevím, co se děje, ale mávnutím motýlích křídel jsem se z člověka, který sice Aj ty v IT fandí, ale vlastně o nich nic dalšího moc neví a nemá tam žádné kontakty, stal člověkem, který si s nimi má zavolat a sejít se s nimi :) Tak jsem zvědavý, co vymyslíme. Bylo by dobré, kdybych měl třeba [na webu](https://junior.guru/jobs/) slovenské nabídky práce, ale to je bohužel zatím z hlediska mého vytížení spíš hudba daleké budoucnosti.


## Další poznámky

- Dan Srb měl mít přednášku v klubu, ale nestíhal to připravit. Posunuli jsme to na pozdější datum. Díky naplánovanému eventu s Pure Storage mi to vlastně ani nevadí, aspoň budou věci v klidnějším tempu.
- Janis Ozolins [jedním jediným obrázkem vysvětlil](https://twitter.com/OzolinsJanis/status/1519628239253106690), proč tyto poznámky bývají nesnesitelně dlouhé (píšu je rychle) a proč jsou kapitoly v příručce údernější (jeden odstavec tam edituji i několik dní).
- Napsal jsem si s kluky ze Street of Code a třeba spolu něco vymyslíme.
- Domlouvám se s Inuits a Mews, že budou prodlužovat členství v klubu na další rok.
- Řešil jsem s právničkou všechny detaily formalizace voleb do výboru spolku a zapsání změn do rejstříku.
- Přidal jsem se na Discord Street of Code, robime.it, Aj ty v IT, Informatika s Mišom. Kromě klubu jiné Discordy číst vůbec nestíhám, ale musím mít přehled a chci být k dispozici, kdyby mě někdo chtěl označit. Přehled znamená, že koukám, jak dělají jiné Discordy třeba _onboarding_ nových členů, nebo které věci jsou produktově spíš „komodita“ a které jsou u mě unikátní.
- Tweetnul jsem si [vlákno o tom, jakou mapu bych na Mapy.cz chtěl](https://twitter.com/honzajavorek/status/1520684708031516672). Bylo to celkem populární, nasbíralo to přes 230 lajků. Asi nejsem sám.
- Dostal jsem nabídku kandidovat na Praze 3 v letošních komunálních volbách.
- Prošel jsem všechno v klubu. Zkusil jsem odpovědět na co nejvíc mailů.
- Šéfredaktorka Anna Urbanová [si dává pauzu od Heroine](https://www.facebook.com/anna.urbanova.904/posts/10217352432801804).
- Volali jsme si s Nelou Slezákovou a probírali novou kapitolu v příručce pro juniory, která by měla být o duševním zdraví. Nela teď bude ladit text a zavoláme si zase za pár týdnů. Já jsem před callem ještě novou kapitolu ladil, hlavně po vizuální stránce.
- Meetup asi změnil URL kalendářových exportů, takže to rozbilo python.cz. Zjistil jsem, jaká jsou nová URL a [opravil jsem to](https://github.com/pyvec/python.cz/commit/3330d1e024d510e6d01c2d6ab8a94dd6f4344e8b). Snad to teď funguje :D
- Během 7 dní od 30.4. do 6.5. jsem naběhal 10 km, při procházkách nachodil 35 km. Celkem jsem se hýbal 16 hodin a zdolal při tom 45 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Vymyslet změny v mentoringu, uskutečnit je
2. a úspěšně zorganizovat středeční večerní event v klubu :)
3. Zkusit streamování na YouTube a když budu odvážný, hned to ve středu použít.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Dev Stories (#3): Pavel Polcr - Z rekvalifikačního kurzu do IT](https://www.programhrovani.cz/1843229/10467773-dev-stories-3-pavel-polcr-z-rekvalifikacniho-kurzu-do-it)<br>Super rozhovor s Pavlem, členem junior.guru klubu. Pavlova cesta byla dost zajímavá a pěkně popisuje i detaily kurzu na VŠB a i samotného hledání práce.
- [Insider #109 - Marek Hanč](https://overcast.fm/+RsY6qtV_s)<br>Spousta věcí pohledem marketéra z Babišova týmu.
- [Patrick Zandl: Jak řešit krizi bydlení? O technologiích, úpadku médií a lokální politice](https://protiproudu.libsyn.com/patrick-zandl-jak-eit-krizi-bydlen-o-technologich-padku-mdi-a-lokln-politice)<br>Nejen o bydlení, ale o všem možném. Pěkný rozhovor k procházce s kočárkem.
- [A decade and a half of instability: The history of Google messaging apps](https://arstechnica.com/gadgets/2021/08/a-decade-and-a-half-of-instability-the-history-of-google-messaging-apps/)<br>Velmi dlouhý článek, který jsem ale celý přečetl a užil si jej. Mnoho zajímavých popisů nezdařených produktů a produktových strategií. Kromě nostalgie a osvěžení paměti také soupis všech absurdit, o kterých jsem ani nevěděl, že existovaly. Ze všeho nejvíc to pro mě osobně má „Oracle vibes“, kde jsem podobné změny zaměření a priorit z roku na rok viděl taky.
- [Ep. 82 – Dievčatá a ženy v IT – Aj Ty v IT](https://wp.streetofcode.sk/podcast/dievcata-a-zeny-v-it/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=dievcata-a-zeny-v-it)<br>Pecka rozhovor, s každou větou jsem chtěl říct: „ANO! THIS!“ Některé obraty dokonce sám používám, když někde o juniorech mluvím. Už delší dobu mám dojem, že se můj přístup dost shoduje s tím, jaký razí Aj ty v IT a toto je jen potvrzení.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu jsem použil vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
