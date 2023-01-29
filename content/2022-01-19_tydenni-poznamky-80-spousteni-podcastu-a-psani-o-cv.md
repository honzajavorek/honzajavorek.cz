Title: Týdenní poznámky #80: Spouštění podcastu a psaní o CV
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl zase nějaký ten týden (3.1. — 19.1.) a tak [stejně jako minule]({filename}2022-01-02_tydenni-poznamky-79-grafy-a-podcasty.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Nebojte, poznámky v novém roce neskončily. Jen jsem měl hodně psaní a navíc termín na článek, takže hodit do toho ještě psaní poznámek, asi bych se už zbláznil. A teď to píšu až ve středu, protože jsem se rozhodl, že to je ideální činnost do vlaku směr hory, kde si chci od všeho na chvíli odpočinout.


## Podcast: Proč?

První díl [našeho podcastu](https://junior.guru/podcast/) měl být o CV a já měl psát o CV článek pro Heroine. Zároveň to bylo už natočené a vlastně se čekalo jen na to, až já udělám svůj job co jsem slíbil a vydám to. Tak jsem se hecnul, že rychle podcast vydám, napíšu článek a do článku třeba propašuju i odkaz na podcast, čímž ho podpořím do startu. Tím se všechno propojilo a bylo potřeba všechno rychle udělat. Výsledkem bylo, že jsem se hodně zpozdil s článkem, uvalil jsem na sebe velkou dávku stresu, ale vytvořil jsem v krátkém čase ohromné množství super věcí :D

Proč vlastně podcast děláme? Nevím, jestli jsem to tu psal. Pája za mnou přišla, že podcast dělat chce a já jsem chtěl, aby takový existoval. Dohodli jsme si role, ona to celé produkuje a já dělám technické zázemí a marketing. Zatím to vypadá, že to funguje skvěle.

Co z toho má JG? Podcast nic nevydělává, je to pouze výdaj, i kdyby jen časový. Z hlediska byznysu je to asi hlavně (content) marketing. Podcast dostane povědomí o JG k lidem, ke kterým by se to jinak nedostalo. Taky už teď můžu říct, že to zaujalo některé zajímavé lidi a sami se ozvali, že do podcastu chtějí. S jedním z nich dokonce mluvíme o partnerství firmy s JG. Takže ještě to ani pořádně nenastartovalo a je možné, že to nepřímo přinese desítky tisíc.

Další věc je, že tvorbu dostupných materiálů pro juniory stále považuji jako hlavní misi JG a tím pádem i svou. Příručka je hromada textu a ne každý to zvládne pročíst. Někomu vyhovuje audio, někomu video. Podcast je způsob, jak juniorům dodat jinou formu obsahu, doplnit informace o pohled konkrétních lidí z oboru, atd. Prostě stejně jako bych mohl psát nové kapitoly do příručky, tak můžeme vydávat i podcast a plní to podobnou funkci. Co víc, může se do doplňovat. Podcast lze vložit přímo do příručky jako doplnění toho, co se tam píše.

Co z toho má Pája? Zatím hlavně zábavu s natáčením a stříháním. Chce, aby takový podcast existoval a chce si to vyzkoušet. Pokud bude podcast úspěšný, třeba časem vymyslíme i nějaké finanční toky od JG k ní, ale zatím jsme to nechali být.

Celé je to teď především experiment, čemuž odpovídá i náš přístup k věci, kdy spíš vtipkujeme, pokud se něco nepovede, než že bychom to velmi řešili, a odpovídá tomu i měsíční frekvence vydávání, abychom to měli na pohodu.

O to víc překvapí, že po týdnu existence je homepage podcastu 7. nejnavštěvovanější stránka na JG s tisícovkou návštěv.

## Podcast: Teaser a ladění audia

Na Discordu jsem rozdělil role pro jednak tým audiofilů, kteří nám dávali feedback na teaser podcastu, jednak speciální roli pro Páju samotnou, aby měla u jména emoji mikrofonu.

Někdejší tajný kanál k diskuzi o tom, zda by nemělo smysl nahrávat kousky příručky jako audio, jsem přejmenoval na #nahrávací-studio a pozval tam jak tým, tak Páju.

Tam jsme řešili feedbakck na teaser a zda by šlo nějak ještě vyladit audio. Já se o stříhání a audio nestarám, to je Páji job, takže jsem jen koukal, co tam lítá za písmenka, čísla a slova.

Podcasty poslouchám na 2x rychlost, takže za mě se snažit ladit každou sykavku nemusí, ale třeba má někdo spoustu času, podcasty si nijak nezrychluje a tyto krásy postprocessingu ocení. Pája se chtěla zdokonalovat v postprocessingu a stříhání, baví ji to, tak byla ráda, že se naučí něco nového.

## Podcast: Publikace

Já mezitím dokončil technické zázemí podcastu. Co vypadalo jednoduše nakonec zabralo 2 dny. Přistoupil jsem k tomu moc perfekcionisticky a když už jsem si generoval svoje vlastní RSS, chtěl jsem ho mít hezké a mít v něm všechno správně. Což ale vyústilo ve studium toho, co kde jaká platforma podporuje, jak mám co kde zařadit, atd.

Místo [podgen](https://podgen.readthedocs.io/) jsem nakonec použil fork [pod2gen](https://pod2gen.caproni.fm/), protože jsem myslel, že tam budu moci dát víc kategorií. To nakonec nebyla pravda a vytvořil jsem [issue](https://gitlab.com/caproni-podcast-publishing/pod2gen/-/issues/26), u pod2gen jsem ale zůstal, protože tam generuje něco navíc. Zpětným pohledem je „něco navíc“ k ničemu, prostě jsem měl vygenerovat nejjednodušší XML, jaké jde, ale už je to jedno, no. Moc jsem si s tím hrál. Mám teď nejkrásnější XML na světě. Juchů.

Chvíli jsem se babral s číslováním epizod, protože jsem chtěl, aby teaser začínal „programátorsky“ jako nula, ale platformy nulu jako číslo epizody nepodporují. Podporují ale název čísla epizody a tam jsem to už vrazit mohl. Taky jsem čísla vrazil do titulku, protože některé platformy čísla z XML vyčíst neumí. Líbí se mi, jak podcaster někdy řekne „o tom jsme mluvili v epizodě číslo 42“ a já to pak mohu ve své aplikaci hned najít a přidat si ji. Některé podcasty čísla nemají a najít pak starou epizodu je fakt potíž.

Na [podcast.junior.guru](https://github.com/honzajavorek/podcast.junior.guru#how-does-it-work) jsem zdokumentoval, jak náš podcast funguje, kdybychom to třeba zapomněli. Přece jen vydáváme pouze jednou za měsíc a já někdy nevím ani co jsem měl včera k obědu.

Na hlavní stránce podcastu, [junior.guru/podcast](https://junior.guru/podcast/), jsem vyrobil jen stránku s nadpisem a nic víc, kdyby náhodou v nějakých platformách kontrolovali funkčnost odkazů. Pak jsem dal své vymazlené XML do všech platforem. I když jsem nakonec nepoužil Anchor, tak jsem si odtamtud okopíroval všechny odkazy, kam to mám dát: [Spotify](https://podcasters.spotify.com/), [Apple](https://podcastsconnect.apple.com/), [Google](https://podcastsmanager.google.com/), [Castbox](https://castbox.fm/podcasters-tools/), [PocketCasts](https://www.pocketcasts.com/), [Stitcher](https://www.stitcher.com/), [PodcastIndex](https://podcastindex.org/add), [České Podcasty](https://ceskepodcasty.cz/), [Podcasty.cz](https://podcasty.seznam.cz/). Pak tam byly ještě nějaké [RadioPublic](https://radiopublic.com/), [Breaker](https://www.breaker.audio/) a někde jsem objevil [Lecton](https://lectonapp.com/), ale u těch jsem vůbec nepochopil, jak tam mám přidat podcast a jestli je to vůbec pro mě. Většinu z těch platforem tak jako tak neznám a nepoužívám. Sám teď používám Overcast.fm, který si scrapuje Apple Podcasts.

Na Spotify byl podcast skoro okamžitě, ale jinak trvá několik dní, než platformy podcast přijmou. Hlavní platformy jsem kontroloval ručně, některé byly dokonce i tak hodné, že mi poslaly mail, když to prošlo. Na dalších, třeba ten Stitcher a tak, jsem ale pak už nikdy nebyl a ani nevím, jak to dopadlo :D Od Podcasty.cz, které patří Seznamu, mi po týdnu přišel nějaký salesácký email s PDF prezentací a smlouvou k podpisu, což mě vyděsilo a email leží v mém inboxu dodnes. Nevím co chtějí a proč, ale jestli chtějí moje peníze nebo nějaká kdovíjaká práva na obsah, tak tam podcast asi nebude. Hlavně nemám na takové blbosti čas, musím programovat krásná XML.

## Podcast: YouTube

Někde jsem narazil na [Headliner](https://headliner.app), což je věc, která umožňuje podcast smotat do videa a přímo ho automaticky nahrávat na YouTube. Hodně podcasterů v podcastech o podcastech, které jsem slyšel, říkalo, že na YouTube mají překvapivě dost poslechů a tak. Říkal jsem si, že to budu od začátku sypat i tam.

Stejně mám [kanál](https://www.youtube.com/channel/UCp-dlEJLFPaNExzYX079gCA), kam dávám videa z přednášek (byť _unlisted_) a budu tam dávat vše, co by případně s JG souviselo, takže když tam bude i podcast, aspoň to tam objeví víc lidí a nějak se to namíchá.

Jenže než jsem se s Headlinerem seznámil a vše vyladil ke své spokojenosti, vyčerpal jsem 5 nebo kolik videí na měsíc, co mají zdarma :D Takže teaser sice vyšel, ale první díl podcastu tam vyjde až někdy v únoru, kdy budu mít zase 5 pokusů :D Pak už by se to mělo všechno dít automaticky samo.

Říkal jsem si, že na 1 měsíc bych to zaplatil, ať to odblokuju, stojí to něco přes stovku, ale ono se to dá platit jen ročně, tak holt počkám. Platit na rok Headliner fakt nepotřebujeme, když publikujeme jednou za měsíc.

## Podcast: Homepage

Koukal jsem, [co má na homepage Adina](https://enterpodcast.com/) a udělal jsem to podobně jednoduše. Nadpis, tlačítka na platformy, představení těch kdo to dělají, napsat kdo je Pája, napsat že jsem jen kulisák, epizody, hotovo.

Tlačítka na platformy se mi vůbec nechtělo dávat nějaké jejich, jednak jsou hnusné a jednak ten jejich kód určitě nastavuje nějaké cookies a kdovíco, musel bych to stáhnout jako obrázky, nevím. Nikomu nic už nevěřím, natož platformám jako Google, Spotify nebo Apple. Takže jsem vzal klasická tlačítka a jen jsem je obarvil firemníma barvama, případně fialová pro Apple Podcasts, atd. Výsledek se mi líbí, je to takové pěkně duhové.

Bylo jasný, že to chce mít tam ty epizody nějak ke spuštění, ale nechtěl jsem zase vkládat kód jedné z platforem. Jednak cookies atd., jednak bych ji tím upřednostnil, což mi přijde divný, podcasty jsou (zatím) decentralizovaná věc, každý ať si vybere. V klubu jsem se o tom poradil a připomenuli mi, že existuje `<audio>`. Nikdy jsem to nepotřeboval a jsem stará škola, když jsem se učil HTML, tak to ještě nebylo :) Nastudoval jsem [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) a bylo, super!

Když už jsem měl své krásné XML, dal jsem jej na odiv i krásným _alternate_ linkem v kódu homepage podcastu. Co kdyby někdo používal RSS čtečku, že? Takhle se to za starých časů na slušných webech dělalo.

Některé chyby jsem na stránce opravil až po týdnu, např. margin u tlačítek na mobilu, nebo jsem změnil nějaké texty.

## Restrukturalizace příručky

Abych mohl začít psát o CV, zahájil jsem restrukturalizaci příručky. Aktuálně se už nějakou dobu skládala ze čtyř stránek. Tří delších rozcestníků a jedné dlouhé nudle v podobě původní příručky o hledání první práce v IT.

Chci stránky rozsekávat a postupně přidávat stránky zaměřené na určitá témata. Více kratších stránek, než dlouhé nudle, na kterých je všechno. Čím víc se to bude dařit, tím víc bude chybět hlavní stránka příručky s rozcestníkem, ale to zas jindy.

Přidal jsem do příručky možnost vložit nějakou poznámku s ikonkou. Přidal jsem tři nové stránky: [CV](https://junior.guru/handbook/cv/), [Git](https://junior.guru/handbook/git/), [LinkedIn](https://junior.guru/handbook/linkedin/). Pak jsem na původních stránkách vzal odstavce, které tato témata řešily a dal tam poznámku s odkazem, že teď to je jinde.

Tyto nové stránky jsem začal zpracovávat. Naposlouchal jsem na témata různé podcasty, pustil jsem si videa, dočetl články, které jsem si někdy uložil. Prošel jsem Trello sloupeček s 500 kartičkami a vyzobal ty, které se těchto témat týkaly. Měl jsem spoustu poznatků, které jsem nabral přímo z diskuzí v JG klubu, od juniorů, z jejich praxe s hledáním práce. Taky jsem se konečně jal zapracovat některé připomínky, které padly v komentářích např. od recruiterů, když jsem příručku o hledání práce poprvé vydal. Když jsem byl se svou rešerší spokojený, začal jsem sepisovat stránku o CV.

Abych nové stránky do příručky udělal tím nejlepším možným způsobem, prošel jsem si ještě [přednášku o dokumentaci Djanga od Jacoba Kaplana-Mosse](https://www.heavybit.com/library/video/how-great-documentation-drives-developer-adoption/), na které jsem byl kdysi osobně, a [Diátaxis framework od Daniele Procidy](https://diataxis.fr/). Nakonec jsem si to stejně celé napsal jinak a po svém, ale aspoň jsem se naladil na tu správnou vlnu.

## Stránka o CV

Novou [stránku o CV](https://junior.guru/handbook/cv/) jsem psal asi týden v kuse. Byl jsem už hodně po termínu na článek pro Heroine, ale rozhodl jsem se, že tentokrát to udělám tímto způsobem.

Předtím jsem vždy zpracoval téma pro článek a říkal jsem si, že časem totéž dopracuju do příručky. Teď jsem se rozhodl udělat to nejdřív do příručky a pak z toho umotat článek. Nechodil jsem skoro ven a psal a psal a psal.

Celkem novinka bylo psaní za postupného publikování. Vždy, když jsem měl něco napsaného, commitnul jsem to a hned to bylo na webu. Nedopsané kapitoly jsem opatřil poznámkou, že je teprv píšu. Stránku celou jsem nahoře opatřil poznámkou, že ji teprv píšu. Takhle text vznikal jako _continuous delivery_, rovnou před očima náhodných návštěvníků. Doteď jsou třeba stránky o Gitu nebo LinkedIn podobným způsobem nedodělané. A nevadí to. Dokud stránky nezpropaguju na sítích, stejně si jich nikdo nevšimne, jen náhodní kolemjdoucí.

Jako obvykle, krátká úderná stránka se proměnila v dlouhou nudli :( Jenže mi přijde, že tam jsou fakt ty podstatné věci a zkracovat to moc nejde. Je to návod, jsou tam vtípky a příklady, aby člověk neusnul při čtení. Fakt jsem se snažil, ale holt je to prostě výživné téma.

A mám z toho teď radost. Téma CV bylo na JG dlouhodobě podceněné. Dřív jsem si říkal, že návodů na CV je na internetu dost a nemusím zabrušovat do všeho, ale časem jsem si víc a víc uvědomoval, že by přece jen mohl existovat návod, který je specifický pro IT juniory a sděluje něco, co v jiných návodech není.

Zároveň některé původní rady v příručce vycházely spíš jen z mé osobní zkušenosti a byly odtržené od reality, např. že CV není vůbec potřeba a stačí LinkedIn a to celé ještě pouze v angličtině. Myslím, že to se s novou stránkou povedlo konečně napravit.

Když vyšel první díl našeho podcastu, pouštěl jsem si ho znova celý a snažil se najít citace, které bych vypíchnul. Ty jsem potom ještě použil v textu a taky jsem do stránky přímo vložil i samotný podcast s tím, že je k tématu.

## Přednáška s Rozbitým Prasátkem

Týden před přednáškou jsem ji na sociálních sítích propagoval. V klubu ji bot propagoval 12x po sobě, ale o tom potom.

Přednáška o financích se povedla a byl o ni velký zájem. Pan Prasátko nešel moc do hloubky, ale zase proletěl více témat. Dávalo mi to smysl, protože do hloubky jsou ty jeho podcasty nebo články a ty si může kdokoliv pustit a přečíst.

Několikrát říkal, že nemá úplně fit hlas, což jsem já osobně moc nepoznal, ale asi na tom něco bylo, když mi pak zpětně psal, že už ví čím to bylo, že se mu rozjížděl covid :D

Horší ale bylo, že přednáška byla tak populární, až se na ni musela stát fronta. Narazili jsme na limit Discordu na 25 účastníků, pokud se volá s videem. Řešili jsme pak, jak to podchytit do budoucna a žádné dobré řešení to nemá. Discord má sice _stage_ místnosti, což je kopie Clubhousu, ale tam nelze sdílet obrazovku, je to fakt jen na mluvené slovo.

Když kdokoliv zapne video, call se zastropuje na 25 lidí až do svého skončení. Tedy pokud je nás málo a narazíme na limit až později, nelze jen vypnout video. Call by musel skončit a začít znova.

Samotný screen share se [nepočítá jako video](https://support.discord.com/hc/en-us/articles/360040816151-Share-your-screen-with-Go-Live-Screen-Share) a zastropuje call na 50 lidí, což mi potvrdili i na Discord supportu.

To by mohla být asi cesta. Obrazovku sdílí skoro každý speaker, video nebývá tak nutné. Hloupé je, že nelze mít jednoho člověka na video a zbytek bez, což by šlo přes oprávnění a role podchytit/zakázat/povolit. Stačí jedno video, aby se call omezil na 25.

Ještě nevím, jak přesně toto do příště vyřeším, ale už teď vím, že nic z toho nebude ideální. Zase třeba to nebude takový problém, dost lidí se na přednášku připojuje „jako na podcast“, tzn. že jen poslouchají a třeba u toho vaří večeři. Někdy je ale ta interakce a video oživující.

## Článek pro Heroine

Když jsem měl hotovou stránku o CV, jal jsem se psát rychle článek pro Heroine. Vlastně jsem bral co už jsem měl, jen jsem vyzobával to nejzajímavější a učesával to do podoby časopisového článku.

Povedlo se mi to intenzivně za minulý pátek, na který jsem odešel z domů pracovat do kavárny. Hned v pondělí článek vyšel, prý s ním bylo minimum editorské práce: [Jak si napsat dobré CV a být vidět při hledání první práce v IT](https://www.heroine.cz/zeny-it/7091-jak-si-napsat-dobre-cv-a-byt-videt-pri-hledani-prvni-prace-v-it) Retweetovat můžete [zde](https://twitter.com/Heroine_cz/status/1483120486372495369).

Nakonec jsem na JG nestihl připravit stránku o LinkedIn a další o Gitu a GitHubu. Musím je dodělat jindy. Rešerše a poznámky k tomu mám, ale už jsem to nezvládl dotáhnout a do článku se o tom stejně dostalo minimum, v podstatě pár vět. Na JG bych se tomu chtěl ale pověnovat víc. Tak snad to zvládnu dopsat někdy brzo a ne za půl roku.

## Propagace podcastu

Teaser a pak i první díl podcastu jsem propagoval na sociálních sítích. Jednak klasickou formou, jednak jsem to dal ještě do různých skupin na FB. Bylo příjemné propagovat opět něco, kde po nikom nechci žádné peníze, jen nabízím podcast k poslechu :D

Výsledkem je, že je homepage podcastu 7. nejnavštěvovanější stránka na JG s tisícovkou návštěv. Pája mi napsala, že viděla, jak to tlačím a že je ráda, že ten marketing tomu dělat nemusí. Já jsem zase rád, že nemusím nic natáčet a stříhat. Jsme dokonalý tým :D

## Realtime chat v klubu

Do klubu se poslední dobou přidává fakt hodně lidí, i když podle mě nakonec zůstane vždy zlomek. To asi nevadí, ale s tím, jak klub roste, je potřeba myslet na nějaké škálování.

Jedna věc je onboarding členů, protože teď je zdravím já personalizovanými zprávami, ale někdy už to je trochu nad moje síly. A to se ani nepředstavují všichni, kteří přicházejí. Zdravím jen ty, kteří se sami představí.

Další věc, která přišla s více členy, je realtime chat. Klub byl doteď převážně pro pomalejší třicátníky, kteří s rozvahou napsali příspěvek o 600 znacích a ten si všichni přečetli. Teď přišli lidi, kteří Discord používají víc jako Discord a míň jako „fórum“, tedy že třeba napíšou „dobré ráno“ a rozjíždějí úplně náhodné, realtime diskuze o čemkoliv.

Zprvu to bylo rušivé a lehce jsme se to snažili vracet do původních kolejí, ale jeden člen nám vysvětlil, že by stačil jeden realtime chat kanál, kde by tohle šlo a spokojení by byli všichni. Zatím se to usídililo v kanálu #offtopic a sledujeme, co z toho bude. Co já vidím, je taková ta „volná zábava“, která bývala na Pyvo srazech po přednáškách, taková ta co tmelí lidi. A uvědomil jsem si, že něco takového nám tam asi fakt chybělo.

Takže jen vymyslíme, jak se zařídíme, jestli nějaké místnosti přejmenujeme a tak, ale realtime chat určitě zůstane. A ne, nebudu to asi všechno číst, někdy tam je 80 nových zpráv za dopoledne, ale to je holt nevyhnutelné s růstem klubu. Pokud by bylo potřeba moderovat, snad mě někdo upozorní. Zbytek klubu poctivě čtu, odpovídám, moderuji.

Tím jsem také strávil spousty hodin za poslední dva týdny, zvlášť teď, když se to tam fakt rozjelo a každý den přibude spousta příspěvků. Jsem zvědavý, co udělám až se po pár dnech vrátím z hor, jestli to jen označím za přečtené a pojedu dál, nebo to fakt budu číst.

## Samolepky

V [PrintAll](https://www.printall.cz/) mi vyrobili samolepky. Týden jsem neměl čas si pro ně přijít, protože jsem psal o CV, ale tento týden v pondělí jsem si to konečně vyzvedl.

Jednak jsem chtěl novou várku samolepek, jednak jsem měl nápad, že něco pošlu firmám jako PFko. Samolepky jsem tentokrát udělal asi v 10 verzích. Některé verze budu rozdávat pouze osobně a verzi s podcastem, „naslouchám juniorům“, plánuji dát Páji, ať je rozdává exkluzivně pouze ona sama.

PFko na konci ledna nevím no, ale poslal jsem. Holt to dřív nešlo. Dělal jsem co jsem mohl, zadal jsem to v prosinci jak nejdřív jsem dokázal, vyzvedl jsem si to jak nejdřív jsem dokázal. Jsem taky jenom člověk.

Celé pondělí večer jsem samolepky stříhal z archů a namíchával na míru balíčky pro jednotlivé firmy. Chtěl jsem přidávat osobní vzkazy, ale tak mě to zničilo, že jsem nakonec vždy jen připsal krátkou zprávu na zadní stranu obálky.

Kdo to tady nečte, dostane samolepky jako překvapení :) Poslat PFko v prosinci, to umí každý! V lednu budu mít pozornost příjemce celou pro sebe :D

Poslal jsem to i některým firmám, se kterými se „kamarádím“, ale nesponzorují mě. Cílem je samozřejmě kamarádit se víc :D Nakonec jsem ručně popisoval a odesílal 32 obálek. To je stejný počet jako má člověk zubů nebo kolik je karet v Mariáši. Ano, potřebuji dovolenou.

Chtěl jsem posílat ještě komunitám, ale to jsem nakonec odložil. Nabalím a pošlu postupně podle toho, jak kde to bude spěchat nebo dávat smysl. Zvlášť teď, když se někde věci konají třeba i jen online.

## wITamy w IT

Dawid Zamkowski z Polska se mi ozval:

> Ahoy Honza! How is your community? I've got over 300 members now, in less than 1 month. Now, I'm looking for partnerships (sponsors). I needed to switch from global (English) to Polish and you know what? Engagement increased dramatically! It's strange because I thought that everyone in IT should have basic English skills but it shows that not everyone feels comfortable with using English chat. I think that your move to keep it Czech was great! The name is "wITamy w IT" which means "Welcome in IT" in Polish.

Tolik k tomu, zda jsem udělal správné rozhodnutí, když jsem JG udělal česky a ne anglicky.

## Další poznámky

- Účastnil jsem se díky Česko.Digital mezikomunitního sdílení, kde byly i Czechitas, GUG, nebo #holkyzmarketingu. Bylo to fajn, protože řešíme podobné problémy a můžeme se od sebe učit, i když u všech ta komunita funguje trochu jinak. Czechitas mluvily o onboardingu nových členů do komunity a přivedlo mě to na spoustu zajímavých myšlenek.
- Urodila se hromada emailů, které jsem řešil. Velká část byla ohledně spoluprací. Volal jsem si s Nelou Slezákovou, která rozjíždí psychologické poradenství (nevím, jestli se tomu tak oficiálně říká, spíš ne) a koučování pro juniory, aby se během svého učení, hledání práce a zaučování psychicky nesesypali. Připravujeme přednášku v klubu. Taky jsem si volal s firmou, s níž se už delší dobu „kamarádím“. Připravujeme partnerství. Na svoje „sales cally“ jsem už celkem pyšnej, zatím každý je z klubu vždy nadšený. Asi bych to měl pro ty firmy zdražit :D
- Juicymo na JG [zainzerovalo hned tři pozice](https://junior.guru/jobs/), takže jsem to zpracoval a poslal fakturu.
- Minimálně se třemi lidmi jsem řešil nějaké nesnáze s přístupem do klubu, kupónem, zabugovaným Discordem.
- Přidal jsem do klubu emoji s terminálem a s logy některých vzdělávacích agentur, jejichž jména tam často padají.
- Upravil jsem emaily, které se posílají firmám, když inzerují pozice na JG. Předtím tam byla čísla, která se brala přímo z Google Analytics přes jejich API. Teď jsem tam dal odkaz na [Simple Analytics](https://simpleanalytics.com/junior.guru), který je předfiltrovaný od data začátku inzerce a konkrétně na URL inzerátu. Myslím, že to bude firmám stačit. Ještě dodělat počítání kliků na stránce inzerátu (jakože „počet lidí, kteří na inzerát chtěli odpovědět“) a můžu Google Analytics úplně odstranit.
- Loga komunit na [stránce o klubu](https://junior.guru/club/) jsem udělal barevně. Byly černobíle.
- Odstrojili jsme v klubu stromeček, tedy roli na Advent of Code. Přejmenoval jsem ji na Advent of Code 2021, odebral stromeček jako ikonku a posunul roli v dolů, aby nepřebila žádnou jinou. Díky tomu ji budou účastníci mít na svých profilech aspoň jako vzpomínku.
- Povedlo se mi při programování špatně odsadit blok Python kódu. Neměl být uvnitř cyklu, ale byl uvnitř cyklu. Taková ta chyba, kterou udělá začátečník na třetí lekci. Tak jen chci napsat, že se to děje i lidem, kteří v Pythonu dělají 10 let. Jedno ráno jsem se prostě probudil a v klubu byla upoutávka na přednášku s [Rozbitým prasátkem](https://rozbiteprasatko.cz/) asi 12x místo jednou :D
- Konečně se mi povedlo opravit strašně ošklivé a dlouhé odkazy, které vyskakovaly z některých inzerátů kvůli nějaké ochraně proti scrapování. Už jsem to opravoval asi 3x a furt to nefungovalo. Protože v těch výsledných URL bylo vždy něco náhodného a robot páruje inzeráty podle URL, objevovaly se ke všemu v klubu stále dokola. Celé Vánoce jsem to zoufale ručně mazal. Teď se mi konečně povedlo najít chybu. To, co jsem potřeboval, aby se dělo, se nedělo, protože to bylo o pár řádků níž, než něco jiného, co to mu zamezilo. Jinými slovy, oprava na 3 minuty, když si toho člověk všimnul, úprava pár řádků.
- Zašel jsem na _booster_. Chtěl jsem v Nemocnici sv. Kříže, ale už neměli, tak jsem musel opustit Prahu 3 (!) a dojít pěšky až na Hlavní nádraží. Vedlejším účinkem očkování bylo vytržení chlupů na ruce spolu s náplastí, hojí se to doteď.
- Pokoušel jsem se optimalizovat skript, který stahuje zálohy a staví z nich historii nabídek práce v čase. Věnoval jsem tomu pár hodin, ale moje pokusy byly neúspěšné, tak jsem toho prozatím nechal. Časem se ale délka běhu tohoto skriptu vyřešila sama. Myslím si, že díky opravě těch škaredých URL, o kterých píšu v předchozím bodě.
- Trochu času jsem trávil i moderováním ve FB skupině [Pyonieri](https://www.facebook.com/groups/pyonieri), kde se zase vyrojili chytráci trolíci po tom, co si někdo někam dovolil napsat slovo gender.
- Generování MkDocs začalo trvat už nějak dlouho. Začalo to s tím, jak jsem přidal databázové dotazy pro [grafy](https://junior.guru/open/). Data se získávala z databáze vždy znova pro každou stránku. Vymýšlel jsem, jak to optimalizovat, když jsou různá data potřeba na různých místech a v různý čas sestavování stránky. Nechtěl jsem to úplně komplikovat. Nakonec jsem to rozdělil podle toho, že některé věci stačí připravit jednou a jiné jsou specifické pro každou stránku. Zatím OK, build se zkrátil z 6s na 2,5s a to zatím stačí.
- Zkusil jsem dát na sociální sítě projekt jednoho z juniorů v klubu, [CV jako konfigurátor RPG postavy](https://www.robertbelan.com/). Protože se tam hýbou věci, zkusil jsem to natočit jako krátké screencastové video a koukal jsem, jak se takové video pak chová na jednotlivých sociálních sítích a kolik dostane pozornosti.
- Svetlana udělala [nejúžasnější status na IG](https://www.instagram.com/p/CYe9jHuLg50/), kde popsala, jak miluje JG klub.
- Připojil jsem se přes Zoom [na schůzi Zelených z Prahy 3](https://twitter.com/zelenip3/status/1480626256978882560), abych se podíval, jak taková schůze vypadá a co tam je vlastně za lidi. Bylo to strašně pěkný, lidi to byli hrozně milí a trvalo to nekonečně dlouho, protože sestavovali (volili) kandidátku do voleb. [Formulář](https://pridejtese.zeleni.cz/) jsem zatím nevyplnil.
- Byla schůze výboru [Pyvce](https://pyvec.org/). Určili jsme termín voleb do výboru a o kousek zase posunuli jejich přípravy.
- Během 17 dní od 3.1. do 19.1. jsem při procházkách nachodil 39 km. Celkem jsem se hýbal 14 hodin a zdolal při tom 39 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Jedna věc, kterou bych chtěl zvládnout udělat tento týden:

1. Nemyslet na JG.

Potom nevím, asi budu řešit onboarding a větší viditelnost firem v klubu. Nebo dopíšu stránku o LinkedIn a Gitu a GitHubu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Vytáhnem tě: #20 IT s Le Anh Viet Linh](https://www.buzzsprout.com/1373539/8257030-20-it-s-le-anh-viet-linh).
- [Rasty Turek: Přemlouval jsem investory, ať nám nedávají miliardu, ale jen milion](https://overcast.fm/+Vf9TZqZLM) Zajímavý rozhovor.
- [Dita Formánková: Dostat ženy do IT je začátek. I v Avastu pracujeme na tom, aby rostly až do vedoucích pozic](https://overcast.fm/+Vf9QAOY-Y)<br>Ditu už jsem si dlouho nikde nečetl nebo nepouštěl, protože jí bylo „všude plno“ a nebavily mě výroky ve stylu „nejsme žádné feministky“. Tento rozhovor mě potěšil. Mluví o tom, co dělá na D&I pozici v Avastu, jak je to široké a důležité téma, co všechno zahrnuje. A co plánují nebo už dělají Czechitas. Držím palce!
- [The Europeans](https://anchor.fm/the-europeans/episodes/Eurafrica-eatudm)<br>Podcast o Evropě, epizoda o Africe a dekolonizaci a o tom, jestli už se odehrála nebo stále trvá a co to v dnešní době znamená.
- [Dependency Risk and Funding](http://lucumr.pocoo.org/2022/1/10/dependency-risk-and-funding)<br>„…we need to find a better way to assess impact of libraries than just how many people depend on this on npm or other package managers. Because that's by far not the whole picture.“
- [Americká témata nezakrývají jen Česko, ale celý svět](https://www.mediar.cz/americka-temata-nezakryvaji-jen-cesko-ale-cely-svet/)<br>Chybí globální médium, s opravdu globální perspektivou.
- [Proč místo vakcín nepoužívat léky?](https://www.nihilistanabalkonu.cz/l/proc-misto-vakcin-nepouzivat-leky/)<br>Průlet dezinformacemi o lécích, které mají fungovat na covid. Peruánci, Trump, ginové koktejly, Elon Musk, koně, Beran, močovina, Janeček, misionáři, Larry Ellison. Je tam všechno!
- [Jak si vybudovat portfolio a ukázat, co už v IT umíte](https://www.heroine.cz/zeny-it/7047-jak-si-vybudovat-portfolio-a-ukazat-co-uz-v-it-umite)<br>Good point, že na vlastním projektu člověk nemusí získat tolik relevantních soft skills, jako když se někde k něčemu přidá.
- [Jak si napsat dobré CV a být vidět při hledání první práce v IT](https://www.heroine.cz/zeny-it/7091-jak-si-napsat-dobre-cv-a-byt-videt-pri-hledani-prvni-prace-v-it)<br>Jako by mi autor mluvil z duše!
- [Kouzlo vyprchalo? Harry Potter stárne a jeho fanoušci s ním](https://www.seznamzpravy.cz/clanek/kultura-chlapec-ktery-prezil-slavi-vyroci-zaujme-harry-potter-i-dalsi-generaci-186033)<br>„…co když Harry Potter přestane diváky zajímat? Co když zevšední mladším generacím?“

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu jsem použil vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
