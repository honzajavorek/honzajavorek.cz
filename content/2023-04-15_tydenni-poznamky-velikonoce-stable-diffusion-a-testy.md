Title: Týdenní poznámky: Velikonoce, Stable Diffusion a testy
Image: images/img-2845.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/189

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-03-31_tydenni-poznamky-rychlejsi-spendliky-a-ai.md) už utekl nějaký ten týden (31. 3. až 14. 4.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/img-2845.jpg)
Pohled z terasy Deloitte

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

## Volno

Na Velikonoce jsme odjeli k babičce.
Rozhodl jsem se, že nebudu pracovat a pojmu to jako volno.
Nevyšlo moc počasí, tak jsem přečetl hromady věcí na internetu, hrál jsem si se Stable Diffusion, plánovali jsme dovolenou, uspořádával jsem archiv rodinných fotek…

## Psaní

Velikonoční pauzu jsem využil k napsání hned několika článků na blog:

- [Notion as a replacement for Pocket]({filename}2023-04-01_notion-as-a-replacement-for-pocket.md)
- [Clutter be gone: Reclaiming reading on the internet with a single button]({filename}2023-04-07_clutter-be-gone-reclaiming-reading-on-the-internet-with-a-single-button.md)
- [Jak jsem si začal hrát s generováním obrázků pomocí AI]({filename}2023-04-14_jak-jsem-si-zacal-hrat-s-generovanim-obrazku-pomoci-ai.md)

Na další mám nápady, případně je mám i rozepsané.
Titulky anglických článků jsem začal konzultovat s ChatGPT.
Většinou je to delší konverzace, brainstorming, než že by mi to na první dobrou dalo něco, s čím bych byl spokojený.
Někdy jsem titulek vymyslel sám, ale díky podnětům, které mi poskytlo AI.

Že by mi to šetřilo čas se říct nedá, ale rozhodně mi to pomáhá vymyslet něco lepšího, než bych dokázal sám.
Na titulky jsem úplně marný a jejich vymýšlení mě ani nijak zvlášť nebaví.
ChatGPT tento blok odbourává.
Navíc, pokud jde o angličtinu, navrhuje mi úderná slova, která by mě samotného nenapadla.

## AI

Jak jsem už psal, [hrál jsem si hodně se Stable Diffusion]({filename}2023-04-14_jak-jsem-si-zacal-hrat-s-generovanim-obrazku-pomoci-ai.md).
Ale hrál jsem si i s ChatGPT a myslím, že jsem vymyslel způsob, jak jej využít na vítání nových členů v klubu, nebo na třídění nabídek práce.
Specifický způsob promptování mě napadl už dřív, ale až teď jsem to vyzkoušel a k mému velkému překvapení se zdá, že to funguje.

![ChatGPT]({static}/images/screenshot-2023-04-15-at-10-03-14-chatgpt.png){: .img-thumbnail }

## Newsletter

První z článků nějak záhadně přesvědčil MailChimp, že má poslat newsletter.

![Newsletter]({static}/images/screenshot-2023-04-01-at-13-16-21.png){: .img-thumbnail }

To mě dost překvapilo, protože jsem měl za to, že to prostě nefunguje.
V nastavení jsem vůbec nic neměnil.
Poslalo to pak i druhý a třetí článek.
Tak jsem zvědav, jestli to pošle i tyhle poznámky!

Pokud chcete, aby vám do mailu náhodně chodily nebo nechodily mé články, tak se [přihlašte zde](http://eepurl.com/ifI06H).

## Opravy na junior.guru a testy

I přesto, že jsem měl volno, neubránil jsem se několika rychlým opravám:

-   Jedna [nabídka práce](https://www.linkedin.com/jobs/view/junior-v%C3%BDvoj%C3%A1%C5%99-simula%C4%8Dn%C3%ADch-model%C5%AF-a-n%C3%A1stroj%C5%AF-pro-testov%C3%A1n%C3%AD-%C5%99%C3%ADdic%C3%ADho-sw-trak%C4%8Dn%C3%ADch-pohon%C5%AF-vhodn%C3%A9-pro-studenty-at-siemens-3541984424/?originalSubdomain=cz) měla nekonečně dlouhý titulek: „Junior vývojář simulačních modelů a nástrojů pro testování řídicího SW trakčních pohonů (vhodné pro studenty)“
    Na Discordu to spadlo, protože ten má zjevně limit na počet znaků pro název vlákna.
    Ořízl jsem to v Pythonu na menší počet znaků.
-   Spadlo mi CI, protože jsem nedomyslel něco kolem souborů.
    Opravil jsem to a dopsal jsem k tomu testy.
-   Uvítalo to v klubu automaticky firmu, kterou to uvítat nemělo.
    Změnil jsem tedy algoritmus, kterým bot vybírá, jakou firmu uvítat.

V tomto týdnu jsem hlavně doháněl e-maily a klub.
Ženu a dítě přemohla rýma, tak jsem si nedělal velké ambice a pracoval jen tak napůl.
Doplnil jsem aspoň testy pro velké množství kódu, který jsem napsal v předešlých týdnech.

Dnes Pavlína poslala [Pull Request na další díl podcastu](https://github.com/honzajavorek/junior.guru/pull/1106), tak jsem ho připravil k vydání.
Venku to bude zítra.

## Q&A živě v klubu i na YouTube

Hned po příjezdu od babičky, pár hodin po tom, co jsme přijeli vlakem, jsem měl na večer plánovanou tu svou první Q&A.
Měl jsem trochu nervy, ale nakonec v pohodě.

Záznam je [tady na YouTube](https://www.youtube.com/watch?v=vN235cq8xP4).
Je tam i replay chatu, takže jdou vidět dotazy.
Zvláštní je, že chat se nezobrazil hned po nahrání streamu, ale [muselo se na něj počkat](https://www.reddit.com/r/youtube/comments/uvygbn/comment/i9q3v9t/?utm_source=share&utm_medium=web2x&context=3).
To mě dost zmátlo.

Co se týče failů, tak Tinuki ze začátku trochu přepálil zvuk a mě se vybily sluchátka, protože jsem je po cestě vlakem zapomněl nabít.
Takže konec už je bez sluchátek.
Za mě dobrý, na to, že to bylo poprvé!
Odškrtávám si jeden další velký milník a na podzim naplánuju další.
Pouhým okem mi přišlo, že počet nově příchozích do klubu se těsně před a po Q&A mírně zvýšil, ale nehodlám to nijak exaktně měřit.

Jako fail by se jinak dalo počítat i to, že můj brácha v klubu šířil inzeráty na nějaké pozice u nich ve firmě a už měl i zájemce, ale ten z toho po mé Q&A vycouval, protože jsem tam juniorům nedoporučil do začátku práci „na IČO“.
Ups!

![Marc Rebillet]({static}/images/screenshot-2023-03-13-at-10-43-01-rainy-sunday-youtube.png){: .img-thumbnail }
Přesně takhle vypadala moje Q&A s chatem na YouTube

## Zneužívání 14 dní zdarma

Moderátoři a jeden další člen klubu mi nezávisle na sobě dali tip, že někdo nejspíš zneužívá 14 dní zdarma v klubu.
Týpek s nápadně podobnými přezdívkami a nápadně podobnými dotazy.
Vždy, když potřebuje něco vyřešit, nejspíš dokonce do práce, udělá si nový účet, jde zdarma do klubu a využívá jej.

Nechtěl jsem si kazit Velikonoce, tak jsem se na to pořádně podíval až v tomto týdnu.
A fakt že jo.
Nakonec jsem zjistil, že si takhle vytvořil dokonce osm, možná až devět účtů.

Nemyslím, ze má smysl to kvůli jednomu kazit pro ostatní, tedy zavádět nějaké nové systémové pravidlo, ale zase musím ty, kdo pomáhají, trochu chránit aby věděli, ze se tady nebudou vysilovat na někoho, kdo jen bere ale nemá chuť dat něco zpátky.
Zatím jsem mu jen napsal.
Přemýšlím, co se dá s takovými lidmi dělat, aniž bych uvalil nějaké nové restrikce i na ostatní.

![Zneužívání]({static}/images/screenshot-2023-04-14-at-20-57-53.png)

## Další

-   [Propagoval jsem](https://www.linkedin.com/posts/honzajavorek_kfc-bootcamp-kurzy-activity-7048655097991450624-OIjK) poslední díl našeho podcastu.
-   Udělal jsem si pořádek v jednom Trello sloupci z osmdesáti.
-   Komentoval jsem [pod LinkedIn příspěvkem o juniorech](https://www.linkedin.com/posts/lucietvrdikova_junior-startvit-pohovor-activity-7046356549253922816-pO5N).
    Trochu jsem si povolil vodítko a pojal jsem to jako za starých facebookových časů.
-   Šel jsem na [příjemnou vývojářskou akci do Deloitte](https://www.deloitte-digital.cz/event-page).
    Pěkná terasa!
    Potkal jsem tam lidi z klubu, seznámil se s nějakými novými lidmi a v baráku plném auditorů jsem se zakecal o tom, zda by šlo nějak spolupracovat a kontrolovat marketingová prohlášení vzdělávacích agentur.
-   Michal Kašpárek vytvořil [svoje vlastní udělátko nad ChatGPT](https://github.com/michalkasparek/gusta), tak se na to plánuji někdy brzo mrknout.
-   Přihlásil jsem se do bizarního „obrazového“ newsletteru [readjpeg.com](https://www.readjpeg.com/).
    Jsem zvědav, co mi bude chodit.
-   Losoval jsem výherce slevy na lístky na WebExpo a pak i jednoho lístku úplně zdarma, který věnovala [Adina](https://www.linkedin.com/in/adina-foxova/).
-   Před časem jsem dával na Discord [Mimo Agendu](https://mimo-agendu.ghost.io/) inzerát na někoho, kdo by dělal pro junior.guru rozhovory s juniory.
    A teď se mi na to někdo ozval!
    Tak jsem zvědavý, co z toho bude.
-   Četl jsem si [články o tom, jak mám mít vytuněný LinkedIn](https://www.linkedakademie.cz/blog/).
-   Zjistil jsem, že RSS pro playlisty na YouTube obsahuje jen prvních pár videí od začátku, ne od konce.
    Takže pak nepřibývají nové.
    Zjišťoval jsem, zda to jde nějak řešit, ideálně bez programování, ale muselo by se jít přes API.
    Tak místo toho sleduji celé ty kanály, tam naštěstí RSS funguje tak, jak bych očekával.
-   Koukal jsem na [ObčanGPT](https://obcan.petrbrzek.cz/) a přemýšlel, jak udělat totéž pro příručku na junior.guru.
-   Koukal jsem na [PicoCSS](https://picocss.com/), jestli bych na to nemohl přehodit blog.
    Štve mě, že tu nemám _dark mode_, ale nechce se mi to vůbec řešit.
-   Koukal jsem na [cron.com](https://cron.com/) a na [retool.com](https://retool.com/), aby mi neujel vlak, ale přijde mi, že ani jedno z toho nevyužiju.
-   Radil jsem kamarádovi s rozjížděním [RichBull](https://richbull.co/).
-   Všiml jsem si, že na irozhlas.cz [je i počasí](https://www.irozhlas.cz/pocasi/585068) a že je (subjektivně, pro moje potřeby) mnohem přehlednější, než pocasi.cz.
-   Zapnul jsem si na iCloudu [Advanced Data Protection](https://support.apple.com/en-us/HT212520).
-   Zapomněl jsem na call výboru Pyvce a připojil se až na posledních 10 minut.
    Domlouvám sraz s naší advokátkou, abychom probrali něco ohledně voleb do výboru.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
    Vyřídil jsem jedno stipendium.
-   Během 15 dní jsem naběhal 27 km, ujel na kole 29 km. Celkem jsem se hýbal 8 h a zdolal při tom 56 km.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

Půjdu na [sraz komuniťáků](https://talkbase.io/event/breakfast-for-community-builders/czech-community) a na [WebExpo](https://www.webexpo.net/).
V pátek přijede rodina a budu se jí věnovat.
Ve zbylém čase asi stihnu jen klub, nějakou režii, možná opravy chyb v kódu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Programmer’s Guide to the Big Tech Companies 💻 | Zero To Mastery](https://zerotomastery.io/blog/programmers-guide-to-the-big-tech-companies/)<br>Jaké jsou motivace velkých firem jako Google nebo Apple?
- [Jako Slovák mám po návštěvě Izraele vzkaz pro Čechy: Přestaňte už konečně s tím „malým národem“](https://cc.cz/jako-slovak-mam-po-navsteve-izraele-vzkaz-pro-cechy-prestante-uz-konecne-s-tim-malym-narodem/)<br>„…průměrný Čech je bohatší než průměrný Izraelec. K tomu ještě malá zajímavost. Česko má HDP na obyvatele vyšší i než Japonsko.“
- [LLMs break the internet — The Changelog: Software Development, Open Source](https://changelog.com/podcast/534)<br>Rozhovor se Simonem Willisonem o LLMs (AI jako je GPT) a o tom co všechno to může do budoucna způsobit, co to už způsobuje, jak to využít, použít, jak s tím začít.
- [The User is King (And Not)](https://nemil.com/2020/01/29/the-user-is-king-and-not/)<br>„You think the user is just like you. In some contexts—developer tools, open source software—you’re actually a pretty good proxy for the actual user. But especially today where tech is used by billions of people from all walks of life, you’re only one small group—and probably not the most important one.“ … „If you haven’t interacted with some of your users, you’re doing software wrong.“ A podle mě nejlepší způsob jak toho v běžné firmě dosáhnout je sednout si občas k user supportu a odpovídat.
- [SQLitePCLRaw and open source sustainability](https://ericsink.com/entries/sqlitepclraw_sustainability.html)<br>Je pěkné si jednou za čas přečíst i „success story“ od open source maintainera, jestli se tomu tak dá říct. Není to úplně duhy a jednorožci, je to o hranicích a vyváženém vztahu.
- [M&M23 206: Krása představ o budoucnosti](https://bigvilik.com/2023/04/06/mm23-206-krsa-predstav-o-budoucnosti/)<br>„Poslední měsíce „vizionáři“ předvídají, co nás čeká s umělou inteligencí. Stává se z toho otravná záležitost, protože asi nás všechny už unavují hahapokusy ve volně dostupných aplikacích, kterými se na sociálních médiích prsí kdekterý hejhula z obecní čítárny. To, že skutečně profesionální modely AI změní svět, to je jisté. Jenom si to pořád představujeme jako kreslíři z pařížského magazínu LP 1900, co ukazovali, jak podle nich bude vypadat rok 2000.“
- [Kuřecí svíčková](https://houdekpetr.blogspot.com/2023/04/kureci-svickova.html)<br>Bageta. Tiramisu. Fish and Chips. Tequila. Sushi. Losos. Poké. Guláš. Nic z toho není doopravdy „tradiční“ a existuje to jen pár desítek let.
- [#6 Smějí se mému českému přízvuku. Vietnamci druhé generace v Česku — Vysílač](https://overcast.fm/+lh3JfSp_M)<br>Malá sonda do toho, jak se žije druhé generaci Vietnamců v Česku, jak vyrůstali, jaký vztah mají k Vietnamské kultuře, apod.
- [Think of language models like ChatGPT as a “calculator for words”](https://simonwillison.net/2023/Apr/2/calculator-for-words/)<br>LLM jako ChatGPT je kalkulačka na slova. Není to vyhledávač a není moc dobrý na sdělování faktů. Užitečná analogie. „So many of the challenges involving language models come down to this: they look much, much easier to use than they actually are.“ http://simonwillison.net/2023/Apr/2/calculator-for-words/#
- [the machine's work is good enough](https://bnet.substack.com/p/the-machines-text-is-good-enough)<br>„Writing, for most people, is not a job; it's just a thing you have to do in the course of a different, actual job. Boilerplates exist for a reason. Sure, I wince a little when I see a reply-all in the vein of, "Thanks for sharing these learnings! It's so important to amplify our impact when connecting with our partners and stakeholders" — but I also understand that coming up with unique text is almost always wasted effort. Exponentially more of this type of writing is done manually by people all over the world on a daily basis than is, say, a longform narrative investigation or a funny blog post.“
- [The weird future of music](https://www.youtube.com/watch?v=1LV1K69885E)<br>Budoucnost hudby?
- [Unreal Engine 5.2 is getting too real](https://www.youtube.com/watch?v=qLGmj86-j4k)<br>Tohle je paráda. Nový level toho, co dokáže počítačová grafika ve hrách.
- [Stávky a demonstrace se v Česku moc nenosí. Poučíme se z francouzských a britských protestů? - VOXPOT](https://www.voxpot.cz/stavky-a-demonstrace-se-v-cesku-moc-nenosi-poucime-se-z-francouzskych-a-britskych-protestu/)<br>„V Česku to naopak občas vypadá, jako by důstojnost byla jakousi nadstavbou, když už je práce hotová, nebo když na ni zbydou peníze. Pracovat je potřebné, i když mzda není adekvátní. Pracuji, tedy jsem. Kdo nepracuje, ať nejí. Jako by lidská důstojnost byla až odměnou za odvedenou práci.“
- [Množící se Escobarovi hroši poputují pryč z Kolumbie, cesta bude stát 3,5 milionu dolarů - VOXPOT](https://www.voxpot.cz/flash-news/mnozici-se-escobarovi-hrosi-poputuji-pryc-z-kolumbie-cesta-bude-stat-35-milionu-dolaru/)<br>Kdo taky viděl Narcos?
- [The world according to Xi | The Economist](https://www.economist.com/leaders/2023/03/23/the-world-according-to-xi)<br>„China’s “Global Civilisation” argues that Western advocacy of universal human rights, in Xinjiang and elsewhere, is a new kind of colonialism… To many, the invasion of Iraq in 2003 exposed the West’s double standards on international law and human rights…“
