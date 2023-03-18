Title: Týdenní poznámky: Průzkumy, přípravy a podcast
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru


Utekl zas nějaký ten týden (10. 3. až 17. 3.) a tak [stejně jako minule]({filename}2023-03-10_tydenni-poznamky-nabidky-prace-realtime-bot-brno-a-mnoho-dalsiho.md) sepisuji, co jsem dělal a co jsem se naučil.
Tvořím [junior.guru](https://junior.guru/) a nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/) a členy by mohlo zajímat, co dělám.
Psaní poznámek mi taky pomáhá nezbláznit se a nepropadat pocitu, že je konec týdne a já jsem nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Záměr s newslettery

Sepsal jsem si svůj záměr s newslettery, které chystám.
Toto mám k osobnímu newsletteru, který by měl fungovat tady v rámci mého blogu:

-   Můj osobní newsletter bude lidem posílat seznam odkazů, které teď dávám na Telegram a seznam článků, které jsem vydal na blogu.
    Na konci by byla upoutávka, že mám ještě jeden newsletter, který se týká JG, s ukázkou toho, co dostanou, např. s odkazem na poslední vydání toho JG newsletteru.
-   Ještě nevím, jak vyřeším archiv newsletteru.
    Vydat to jako další článek na blogu mi přijde divné.
-   Na blog přidám štítky, aby přes ně šlo filtrovat a aby je šlo přes RSS separátně odebírat.
    Ono to teda už vlastně jde a štítky tu jsou, ale nikde se nezobrazují.
-   Předělám blog tak, aby tady všude byly upoutávky na to, že mám newsletter.
    Líbí se mi, jak to dělá Substack nebo jak to má [Pavlína Louženská](https://www.pavlinaspeaks.com/).
-   Můj osobní newsletter by se mohl [propisovat jako články na můj LinkedIn](https://www.linkedin.com/help/linkedin/answer/a522525), pokud API dovolí.
    Lidi by mě mohli pak odebírat i tam.

Toto mám k newsletteru/blogu na JG:

-   Na JG vytvořím novou sekci, která bude sdružovat veškerý _time-sensitive content_.
    Tedy věci, které nejsou statická příručka, ale vycházejí v čase.
    Moje statusy na LinkedIn, podcasty, články na budoucím blogu JG, newslettery, přednášky.
-   Mohlo by se to jmenovat „Log“.
    Líbí se mi, že to vychází z blogu (což vychází z _web log_, ehm) a zároveň je slovo _log_ obecnější a v programátorské hantýrce používané pro protokol o běhu programu.
    Tohle bude protokol o běhu JG 😀
-   Časem by se tam daly přidávat další a další události.
    Vítání firem, inzerce práce, založení vlákna v #práce-hledám, upozornění na IRL srazy, svátky aj. akce.
-   Každá taková věc se bude kategorizovat štítkama, podle kterých to půjde filtrovat.
-   Na LinkedIn bych mohl psát mnohem častěji a dávat tam „rychlé“ statusy jako dřív na Twitter, které budou upozorňovat na zajímavosti z oboru.
    Mohl bych je třídit pomocí hashtagů.
    Byl by to nějaký flexibilní systém, který by mi umožňoval vymýšlet nové štítky za pochodu.
    Tipy, drby, přednášky, kritika článků v médiích, atd.
-   Log by si ty statusy stáhl k sobě, archivoval by jejich text a publikoval i na webu, hezky roztřízené.
    LinkedIn bych tedy využil jako platformu, kam bych ručně psal novinky, ale zároveň bych měl zálohu a až ta síť shoří v pekle, mohu se přesunout klidně jinam.
-   Jednou za čas se pošle newsletter, který bude inteligentním souhrnem událostí z „Logu“ od posledního newsletteru.
    Vygeneruji to automaticky, ale díky ručně psaným statusům z LinkedInu apod. tam bude prostor pro lidský element.
    V něčem mi také může pomoci ChatGPT API.
-   Newsletter má archiv v rámci „Logu“.
-   Web JG bych pak chtěl prošpikovat (nenásilně) upoutávkami na to, aby se lidi přidali do newsletteru.
-   Newsletter by se mohl také [propisovat jako články na můj LinkedIn](https://www.linkedin.com/help/linkedin/answer/a522525), pokud API dovolí.
-   Cílem newsletteru by bylo poskytnout zajímavé informace z oboru, ne dělat vyloženě reklamu na JG.
    Nejspíš tam bude informační koutek o tom, co se děje na JG, ale chci, aby jádrem těch e-mailů byl užitečný obsah, který nikde jinde moc není.
-   Do ceníku přidám, že pracovní nabídky se posílají i do newsletteru.
    Nebude to nejspíš stát nic navíc.


## Průzkum OpenAI

Napadlo mě, že bych mohl použít OpenAI tady na blogu.
Nějaká drobnost, díky které bych si ale vyzkoušel jejich API a zjistil, jak to funguje a naučil se s tím.
Tož API je fajn a povedlo se mi z Pythonu posílat na ChatGPT dotazy a dostávat odpovědi.

Akorát jsem chtěl udělat třeba to, že by ChatGPT vymyslelo shrnutí článku do pár vět pro ty, komu se to nechce celé číst.
A to moc dobře nejde, protože mu mohu poslat jen omezený počet znaků 😀
Zkoušel jsem i nějaký [trik z Redditu](https://www.reddit.com/r/ChatGPT/comments/11aoci0/how_to_get_around_the_chatgpt_prompt_size_limit/), ale bez úspěchu.

Budu se tedy ve svých nápadech soustředit zatím jen na věci, které mají zhruba do 2.000 znaků.


## Průzkum Ecomailu

Už před časem jsem si všiml, že existuje [Ecomail](https://www.ecomail.cz/), česká služba na mailing, [konkurence MailChimpu](https://blog.ecomail.cz/ecomail-vs-mailchimp/).
Šel jsem to konečně prozkoumat a jsem silně nakloněn tomu, že svoje newslettery, které plánuju, rozjedu tam.
Vychází to lépe finančně, budu mít českou podporu a kvalitní doručování do českých schránek a tak dále.
A když jsem zabloudil až k nim na YouTube, našel jsem tam dokonce [video s novinkami](https://www.youtube.com/watch?v=ExKnvsENu-U), které zrovna popisuje, jak přidali podporu pro mailing na základě RSS!
V neposlední řadě, API dokumentaci [mají v Apiary](https://ecomailczv2.docs.apiary.io/), kde jsem pracoval, takže po [Fakturoidu](https://fakturoid.docs.apiary.io/) opět moment nostalgie.

Jediná nevýhoda je, že kontakty z Memberful bych si musel do Ecomailu načíst sám, kdežto s MailChimpem to má integraci.
Memberful má ale API, které jsem už několikrát použil, takže to asi není nic zásadního.


## Průzkum LinkedIn

LinkedIn má API a už dřív jsem si tam v nastavení připravil OAuth aplikace, přes které jej mohu použít.
Tak jsem si řekl, že zkusím napsat program, který přes API stáhne odkazy na všechny moje příspěvky na profilu, které jsem na LinkedIn napsal.
Mám totiž pár nápadů, jak by to šlo využít a zároveň bych zjistil, jak se s tím API pracuje.
Možná by to šlo i scrapnout, ale naivně jsem si myslel, že by to přes API mohlo být jednodušší.

![LinkedIn API]({static}/images/screenshot-2023-03-12-at-16-49-09-linkedin-api-documentation-linkedin.png){: .img-thumbnail }

Dokumentace API je ale složitá a je to spousta klikání a čtení, tak jsem to vzdal a zkusil ChatGPT.
Zeptal jsem se nejdřív toto:

> I have a profile at LinkedIn and I add posts there so that others can read them. They are public. How do I use the LinkedIn API to list my own posts using Python 3?

Hned mi vyhodil kód, který šel prakticky _copy-paste_ použít.
Jenže to bylo mnou nenáviděné OAuth 2.0, které nejde použít bez interakce s uživatelem (se mnou), tzn. pro účely nějaké automatizace na JG je to nepoužitelné.
Zkusil jsem tedy doplňující dotaz:

> Is there a way to do this without user interaction? This requires me to open a browser and do something as a human. I'd like to have a Python 3 script, which runs on a server, without human interaction.

A šup, měl jsem krásný příklad, jak to udělat jinak.
Ten bohužel nefunguje, ale za to ChatGPT nemůže:

```python
{
    'error': 'access_denied',
    'error_description': 'This application is not allowed to create application tokens',
}
```

Tak jsem zkoušel a hledal, kde bych to nějak vyřešil, ale bez šance.
[Dokumentace praví](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow?context=linkedin%2Fcontext), že mám „Reach out to the LinkedIn Relationship Manager or Business Development team to get the necessary access“, což netuším co znamená.
Napsal jsem jim na support ([zhruba 4.000 znaků textu](https://gist.github.com/honzajavorek/9f9db686888715ee09ce877cccb70feb), ehm) a k mému překvapení do několika hodin odpověděli.
Akorát že tohle:

> In terms of your questions, we have dedicated resources for APIs that you can find here:
>
> https://developer.linkedin.com/<br>
> https://learn.microsoft.com/en-us/linkedin/<br>
> https://www.linkedin.com/help/linkedin/answer/a526157<br>
>
> Additionally any specific questions you have regarding your app can be directed to our API helpdesk: https://linkedin.zendesk.com/hc/en-us/requests/new

Pokračování někdy příště.
Koukal jsem ještě na GitHub, jestli už někdo něco s LinkedIn API neřešil, ale je tam hlavně hromada pokusů o scrapování LinkedIn.
Nejhustější je projekt [linkedin-api](https://github.com/tomquirk/linkedin-api), který zřejmě používá hodně lidí a má i sponzory, ale přímo v README má tohle:

> This project violates Linkedin's User Agreement Section 8.2, and because of this, Linkedin may (and will) temporarily or permanently ban your account. We are not responsible for your account being banned.

Jako nevím, no.
Ještě to oficiální API nebudu vzdávat.


## Příprava Q&A

Dotáhl jsem tento týden výběr termínu Q&A.
Bude 11.4. v šest večer, [tady na YouTube](https://youtube.com/live/vN235cq8xP4).
Posouval jsem to několikrát.
Snažil jsem se domluvit s PyLadies, aby to bylo i pro ně a nebylo to v den, kdy mají večer kurz.

Bude to fungovat tak, že se připojím na Discord, tam mě Tinuki nahraje a odstreamuje to na YouTube.
Na Discordu i na YouTube je chat.
Členové se mohou ptát na Discordu, ostatní na YouTube na chatu.
Budu se to snažit sledovat a na vše postupně odpovídat.
V záznamu budou oba chaty, protože jeden bude přímo ve snímaném obrazu, druhý uchovává YouTube spolu s videem a při přehrávání záznamu se budou komentáře postupně objevovat, jako by to bylo v reálném čase.

Jsem zvědav, jaké to bude a jak to zvládneme technicky.
Zatím to budu šířit jen v klubu a mezi PyLadies.
Napodzim udělám další Q&A a o té už dám vědět třeba i do dalších komunit.

Spolu s tímhle jsem doladil i termín jedné z budoucích přednášek v klubu.


## Mentoring

Udělal jsem si pořádek v mentorech z Mews, kde mi nějak neseděly počty a měl jsem pocit, že mi někdo chybí v seznamu, a přitom se nabízel na mentoring.

Svůj záměr s mentoringem, který jsem popsal v minulých poznámkách, jsem poslal mentorům v klubu a požádal je o zpětnou vazbu.
Zároveň jsem se konečně po třičtvrtě roce dokopal k tomu, abych zpracoval poznámky z někdejšího callu s Linhem, nejaktivnějším mentorem v klubu, a nasdílel je s ostatními mentory, aby se mohli vyjádřit.
Linh pojmenovával mnoho různých bolestí současného fungování mentoringu a mě zajímá, jestli to vidí stejně, nebo zda vidí třeba i nějaké další věci, které by bylo dobré řešit.

V mentoringovém programu v klubu je 23 lidí, ale vyjádřili se k tomu zhruba 3, takže zatím jsem moc zpětné vazby neposbíral.
Vypadá to ale, že případné změny by snad mohly jít dobrým směrem.
Minimálně by nejspíš řešily většinu problémů, které identifikoval Linh.


## Anketa

Opět jsme si volali s ENGETO Academy ohledně ankety.
Jsme v podstatě ve finále.
Máme posledních pár drobností, co chceme doladit.

Sehnal jsem ještě kamarádku [Báru](https://www.linkedin.com/in/baradrb/), která rozumí anketám a podívá se na to, než to pustíme do světa.
Taky to pak chceme ještě na zkoušku projít třeba s třemi lidmi a pozorovat je, jak to vyplní.


## Pyvo

Ve středu bylo v Praze [Pyvo, sraz programátorů v Pythonu](https://pyvo.cz/praha-pyvo/).
Už strašně dlouho jsem tam nebyl, tak jsem vyrazil.

Před srazem jsem se ještě na pivu sešel s Tatankou, členem klubu, a pár kamarády.
Pak jsme šli na Pyvo a tam jsem si povídal s mnoha lidmi o všem možném, od komunity a konferencí až po ADHD a autismus.
Potkal jsem se tam i s již zmíněnou Bárou a řešili jsme i tu anketu.
Rozdal jsem pár JG samolepek.


## Podcast

Green Fox Academy si na JG zaplatili nejvyšší tarif a v rámci něj je epizoda podcastu.
Domluvili jsme kdo bude hostem a Pája to natočila.
Povedlo se nám najít hosta, který má dokonce vztah i k JG klubu, takže super.

Výrobu podcastu ale provázela určitá nejistota, protože to byl první takový placený díl a navíc jde o vzdělávací agenturu.
Já si přitom hodně [hlídám střet zájmů](https://junior.guru/faq/#vzdelavaci-agentury).
Pavlína mi před vydáním poslala sestříhaný draft a ten jsem si poslechl.
Líbilo se mi to a nepřišlo mi, že by to po obsahové stránce vyžadovalo nějaké změny nebo opatrnější našlapování.
Lukáš je v podcastu skvělý a vysvětluje jak věci kolem GFA, tak poskytuje i obecnější rady pro ty, kdo se chystají změnit kariéru.

Chci však, aby takové díly byly transparentně označeny.
Tento týden jsem na tom pracoval, právě proto, že měla vyjít tato epizoda.
Myslel jsem, že při tom předělám i obrázky pro epizody a upoutávky, ale na to nakonec nedošlo, protože jsem se zamotal v refactoringu všeho možného.
Epizody vytvořené ve spolupráci s firmou jsem označil na webu, na Discordu, v popisku v XML feedu podcastu.

![Označený podcast]({static}/images/screenshot-2023-03-17-at-23-52-08.png){: .img-thumbnail }

Na webu jsem přemístil tlačítko vedoucí na YouTube, aby bylo první.
Uvědomil jsem si, že pokud si lidi vybírají, tak preferuji, aby lidi sledovali můj YouTube účet, než aby šli na Spotify, protože na YouTube toho dávám a budu dávat víc.

![Preference YouTube]({static}/images/screenshot-2023-03-17-at-23-54-31.png){: .img-thumbnail }

Když už jsem upravoval oznamovačku podcastu v klubu, tak jsem ji změnil celou a vylepšil.
Jsou tam teď taky tlačítka.

![Podcast na Discordu]({static}/images/screenshot-2023-03-17-at-23-55-30.png)

Jeden kamarád, kterého nebudu jmenovat, si opakovaně stěžuje na zvukovou kvalitu podcastu.
Vedl jsem o tom s ním debaty a potom i s Pájou.
Stojím si za tím, že priority jsou takové, jaké jsme si s Pavlínou nastavili na začátku:

1.  Podcast existuje a Páju baví.
2.  Kvalita obsahu.
3.  Kvalita zpracování.

Podcast jsme založili jako _low-effort_ projekt, který musí být možné stíhat rodičovské.
Máme svoje limity.
Když budeme tlačit na kvalitu zvuku, bude to větší závazek a Pavlínu to bude méně bavit.
Navíc ani já, ani Pavlína nejsme audiofilové a současná kvalita nám stačí.
Jasně, občas se stane nějaká chyba, která nás mrzí, ale jinak si myslíme, že to není potřeba moc řešit.
Za nás je to _good enough_.

Poslal jsem e-mail do GFA, že podcast je hotov.
Reakce byla:

> Skvělé! Moc děkuju, mám z toho radost!


## Další

-   V klubu jsem obnovil kanály #python, #csharp a #php.
    Přidal jsem kanál #java.
    K tomu jsem překopal _onboarding_ na Discordu, kde si lidi vybírají oblasti zájmu.
    Nově jsou tam i přímo takhle jazyky a lidé dostanou i role, např. „Zajímá mě: Python“.
    Tyto role jdou rovnou v chatu označit a poslat tím notifikaci.
    „Tajnou“ skupinku Django Coders jsem potom přesvědčil, že už existuje dost vhodnějších míst, kde mohou realizovat totéž, a po domluvě jsme kanál archivovali.
    Měl jsem spoustu nápadů, jak bude bot na Discordu hlídat, že každý kanál pro daný jazyk má svou roli a že popisky jsou všude stejné apod., ale nakonec jsem si zabránil to hned začít programovat a udělal jsem vše jen ručně.
-   Na [Discordu Jakuba Zelenky](https://discord.gg/Ee8sV6MrPN) „Mimo Agendu“ jsem napsal [něco jako inzerát na novináře](https://discord.com/channels/809699708557721610/812644125953359882/1085303527993245736), kterého bych najmul, ale zatím spíš bez odezvy.
-   Koupili jsme letenky na dovolenou.
    Zjistil jsem, že na [Festival o psaní](http://festivalopsani.cz/) nebudu v Praze a přemýšlím, co s lístkem.
    Napsal jsem jim e-mail, ale zatím bez odpovědi.
-   Přepsal jsem kód, který mi vyrábí obrázky pomocí screenshotů, aby pokaždé nespouštěl prohlížeč.
    Hypotéza byla, že se to tím hrozně zdržuje.
    Vytáhl jsem to tedy do separátního procesu, který běží na pozadí a když dostane úkol něco screenshotovat, tak to udělá a pošle výsledek.
    Zabralo mi to jedno celé dopoledne a bohužel to nic zásadně nezrychlilo 😂
    Zrušil jsem aspoň vytváření upoutávky na přednášku pro Instagram a pro web.
    Vytváří se jen pro YouTube a pro Discord.
-   Vyřídil jsem dvě stipendia.
-   Opravil jsem Jobs.cz scraper, aby správně stahoval loga firem.
-   Povedlo se mi upravit [iSublime](https://github.com/honzajavorek/isublime) tak, že si umí načíst heslo k iCloudu z mého 1Passwordu.
    Nechtěl jsem ho mít jen tak hozené do _environment variable_.
    Teď když to spustím, vyskočí na mě akorát že mám přiložit palec ke čtečce otisků prstů na mém Macbooku a když ho přiložím, program se přihlásí a synchronizuje soubory.
-   Prokrastinoval jsem maily firmám, které mají končit v březnu, a bylo mi trapné, abych se jim ozýval dva týdny před koncem partnerství.
    Jednu firmu jsem rovnou vyřídil a poslal fakturu na další období, protože jsme byli domluvení z osobní schůzky.
    Povedlo se mi při tom udělat chybu a způsobil jsem, že firma zmizela na pár dní z webu.
    Trochu _faux pas_, ale snad nic hrozného.
    Chyba to nebyla vyloženě lidská, spíš to byla nedostatečně otestovaná situace v kódu, takže jsem doplnil testy a opravil to.
    Spolu s tím jsem opravil i pár dalších drobností v evidenci firem.
    Ostatním jsem prodloužil partnerství do dubna a pokusím se jim co nejdřív ozvat.
-   Chtěl jsem dnes předělat vítání nových členů v klubu, ale když jsem se podíval do kódu, nějak jsem se neubránil a začal přepisovat pár věcí.
    Soubor `club.py` jsem rozdělil asi na pět menších.
    Na různé konstanty jsem použil [Enum](https://docs.python.org/3/library/enum.html).
    Pak jsem ještě přepracoval způsob, jakým vypínám a zapínám, zda může bot zapisovat do různých služeb.
    Chci totiž, aby se muselo explicitně zapnout, že může zapisovat změny do Discordu nebo do Memberful API.
    Na produkci je to vše zapnuté, ale při vývoji mi to brání udělat nevratné chyby ledabylým spouštěním příkazů.
    Nebudu to tady rozepisovat, bylo by to dost technické, ale s výsledkem jsem dost spokojen.
-   Řešil jsem nějaké problémy s účty u členů klubu, změny v předplatných, vracení peněz.
-   Doklepli jsme s daňařem přiznání, akorát ty věci musím ještě nahrát na příslušné portály.
    Pokročili jsme v tom, abych se stal idenfitikovanou osobou.
-   Přišla mi pozvánka na vyzkoušení Bingu s AI, ale pak to po mě chtělo, abych si stáhl Edge nebo co, tak jsem to zavřel a neřešil.
-   Jordi Bruin vydal [novou verzi MacGPT a další aplikace](https://goodsnooze.gumroad.com/?recommended_by=library), která už umí i to jejich nové API, ale nakonec stejně chodím spíš k nim na web.
-   Na realtime botovi jsem do [Issues](https://github.com/juniorguru/juniorguru-chick/issues) nasypal nápady na půl roku dopředu.
-   Prošel jsem svá trička a vyházel stará.
    Koupil jsem si pak nová trička.
    Různě na internetu a v infocentru Prahy 3.
-   Byl jsem pro něco do Alzy a když jsem šel na zastávku tramvaje, uviděl jsem, že zrovna jedna jede.
    Rozběhl jsem se a pak si jen pamatuju, že jsem hodně zblízka viděl chodník.
    Tramvaj jsem stihl.
    Na přestupu mě trochu ošetřil pán v kebabu.
    Je to týden, tak se už díry v rukou hojí, ale první dny byly celkem blbé.
    Zničil jsem si gatě, ale jinak žádné větší škody.
-   Byli jsme s děckem v kavárně v [DOX](https://www.dox.cz/)u a je tam super herna pro děti.
-   Teploty se dnes vyšplhaly na 15°C, takže jsem vzal děcko podruhé na kolo a objel s ním celkem slušný kus Prahy kolem Rokytky.
-   Odpovídání v klubu, e-maily, [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), atd.
    Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
-   Během 8 dní od 10. 3. do 17. 3. jsem při procházkách nachodil 10 km, ujel na kole 18 km. Celkem jsem se hýbal 8 hodin a zdolal při tom 28 kilometrů.
-   Finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).
    Aktuální nabídky práce pro juniory: [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)


## Povedlo se

Udělal jsem něco z [plánů na rok 2023]({filename}2022-12-26_strategie-na-2023.md)?

-   „Začneme označovat epizody, které jsou finančně podpořené spoluprací s firmami“ je hotovo!
-   „Rozjedu pravidelné Q&A pro komunity“ skoro hotovo!
-   „Pohraju si s AI“ je hotovo!
    Jako lepší by bylo, kdybych s tím něco i vytvořil, ale asi si to odškrtnu už teď.
-   Přemýšlím nad „umožním lidem odebírat tento blog a novinky na junior.guru skrze newsletter“.
-   Makám na „stanu se identifikovanou osobou“.
-   Makám na „budu se podílet na anketě mezi juniory“.
-   Makám na „dvakrát do roka si dám dovolenou, která bude aspoň týden v kuse“.


<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví.**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>


## Plánuji

1.  Vylepším automatické vítání lidí v klubu.
2.  Rozmyslím MVP katalogu vzdělávacích agentur.
3.  Administrativa:
    -   Zpracuji poslední kousek ankety.
    -   Odešlu daňové přiznání.
    -   Kontaktuji firmy, kterým brzo končí partnerství.
    -   Promo přednášky, Q&A, podcastu.
    -   Úterní přednáška.


## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel toto:

- [Omezení aut v centru Prahy? Místní by to přivítali, ukázal průzkum - Zdopravy.cz](https://zdopravy.cz/omezeni-aut-v-centru-prahy-mistni-by-to-privitali-ukazal-pruzkum-149407/)<br>Tak třeba se něco pohne.
- [Češi jako Prchalův byznys. Vůči emocím nemá šanci nikdo, říká někdejší Babišův guru marketingu](https://www.e15.cz/rozhovory/cesi-jako-prchaluv-byznys-vuci-emocim-nema-sanci-nikdo-rika-nekdejsi-babisuv-guru-marketingu-1397114)<br>Rozhovor s Prchalem
- [GPT-4](https://openai.com/research/gpt-4)<br>„We’ve created GPT-4, the latest milestone in OpenAI’s effort in scaling up deep learning. GPT-4 is a large multimodal model (accepting image and text inputs, emitting text outputs) that, while less capable than humans in many real-world scenarios, exhibits human-level performance on various professional and academic benchmarks.“
- [Francouzské státní dráhy chtějí zkoumat levitující vlaky i pro provoz na lokálkách - Zdopravy.cz](https://zdopravy.cz/francouzske-statni-drahy-chteji-zkoumat-levitujici-vlaky-i-pro-provoz-na-lokalkach-148952/)<br>Levitující vlaky na konvenční trati? Hustý. To by mohl být celkem game-changer.
- [How do I control where links open on iOS?](https://apple.stackexchange.com/questions/430158/how-do-i-control-where-links-open-on-ios)<br>Nevím, jak je to na Androidu, ale od začátku, co používám iOS, mi přijde všechno kolem in-app browseru naprosto chaotické. Nenávidím ho. Každý odkaz se otevře jinak, každý musím zpracovat jinak, pokud jej chci dostat do standardního Safari, nemluvě např. o Firefoxu. Každá aplikace to má jinak a neexistuje globální nastavení, které by in-app browser třeba zakázalo a vše by se muselo otevřít přímo v Safari (nebo v příslušné appce, pokud to umí).
- [Matt Yglesias and the secret of blogging](https://maxread.substack.com/p/matt-yglesias-and-the-secret-of-blogging)<br>„…there is currently no real economic punishment for content overproduction. You will almost never lose money, followers, attention, or reach simply from posting too much… No one wants to pick “quantity” over “quality” when it comes to their own work, and most readers, given the explicit choice, would say they prefer one great newsletter a week over five “coherent” ones. But the fact is that as much as people might complain that a given newsletter appears too frequently for them to read it, or that a person's byline is ubiquitous, in practice, the vast majority will not unsubscribe or mute or ignore.“
- [Únor 2023: O přínosu nicnedělání](https://newslettery.substack.com/p/unor-2023)<br>„Však si zkuste v práci pár hodin jen tak přemýšlet. Rychle na vás někdo nastoupí a pokusí se vás „zaměstnat“. Paradoxní je, že kdybyste místo přemýšlení bezmyšlenkovitě vyřizovali desítky nebo stovky e-mailů, svět kolem vás bude spokojený… zaneprázdněnost je intelektuálním ekvivalentem fast foodu a pro kreativní práci má zhruba stejnou výživovou hodnotu.“
- [Valtteri Bottas: The Untold Story of Mental Health in F1](https://www.youtube.com/watch?v=wzA2zNeVLmY)<br>Bottas se podělil o své zážitky s mlýnkem na maso jménem F1. Psychické zdraví, váha, poruchy příjmu potravy. Vůbec jsem nevěděl, že F1 nedávno zaváděla nová pravidla, která určují minimální váhu pilotů, aby ti nemuseli řešit nějaké šílené hubnutí 🙈
- [Large language models are having their Stable Diffusion moment](https://simonwillison.net/2023/Mar/11/llama/?utm_source=tldrnewsletter)<br>Jak mít celé to slavné AI na vlastním počítači 😱
- [I promise you ChatGPT can’t access the internet, even though it really looks like it can](https://simonwillison.net/2023/Mar/10/chatgpt-internet-access/)<br>Zajímavé. ChatGPT neumí pracovat s odkazy, ale bude vás přesvědčovat o tom, že umí.
- [The Identity of Tits](https://aella.substack.com/p/the-identity-of-tits)<br>Opět Aella. Zajímavá úvaha nad tím, jak atraktivita nebo to, že je někdo „sexy“ a chová se „sexy“ sice zvyšuje pozornost ostatních, ale zároveň způsobuje to, že ostatní danou osobu přestanou respektovat a neberou ji vážně. Proč to tak je? „Often when people ask why I’m popular, others respond, “tits.” And maybe this is partially true, but it immediately kicks the legs out from under the serious stuff I’ve done, frames me as someone who people only are pretending to respect… I probably would have way fewer followers if not tits. But maybe I would have more respect if not tits? It also threatens the reputations of those who do respect me, because now they’re vulnerable to being accused as manipulated by or secretly just into tits… I like the idea of seeing if I can get people to take me seriously while presenting as someone people should not take seriously.“
- [(něco na Twitteru)](https://twitter.com/levelsio/status/1634457854957723648)<br>Zajímavý postřeh o „prompts“. Možná budou běžným uživatelům skryté a nikoho zajímat nebudou, kromě „inženýrů“.
