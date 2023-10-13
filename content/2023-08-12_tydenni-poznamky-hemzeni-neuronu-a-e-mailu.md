Title: Týdenní poznámky: Hemžení neuronů a e-mailů
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/268

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-08-04_tydenni-poznamky-cisla-a-premysleni.md) už utekl nějaký ten týden (4. 8. až 12. 8.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [teď plánuji]({filename}2023-08-07_letni-pit-stop.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/3/).
</div>

Vůbec jsem nevěděl, jak tento týden nazvat, protože jsem jeho první polovinu přemýšlel a psal [Letní pit stop]({filename}2023-08-07_letni-pit-stop.md), druhou jsem posílal různé e-maily.
Jen zlomek času jsem nakonec stihl věnovat kódění.

## Šifrovačka

Byl jsem s kamarádem na [šifrovačce](https://sifrovacky.cz/) v Brně a bylo to super!
A to přesto, že docela pršelo.

![Šifrovačka]({static}/images/img-4749.jpg)

## Hledání pisatele rozhovorů

Jak jsem psal už v tom letním pit stopu, rozhodl jsem se, že rozhovory s juniorama budou jednou z aktuálních priorit.
Už dříve jsem naťukl pár lidí, že by to pro mě mohli psát, ale zatím z toho nikdy nic nebylo.

Zkusil jsem tedy oslovit lidi v klubu.
Tam to sklidilo velký ohlas, že chci něco takového dělat, ale nikdo se nepřihlásil, že by to psal.
Možná jsem to ale i špatně formuloval, protože se přihlásili lidi, kteří by chtěli být v rozhovoru.
Až potom mi došlo, že to šlo pochopit i tak, že hledám respondenty.

Nicméně vzpomněl jsem si na jednu autorku rozhovorů, kterou znám díky spolupráci s [Heroine](https://www.heroine.cz/).
Té jsem napsal a vypadá to, že se domluvíme.
Ladíme podobu spolupráce, ale myslím, že to klapne a už se těším, až se to rozjede 💪

## Cindy

Ve volném čase jsem dokončil [cindy](https://github.com/honzajavorek/cindy), jednoduchý prográmek, který mi pomůže třídit fotky.
Vezme složku s fotkami a rozřadí je do adresářů podle data, kdy byly fotky pořízeny.
Ne že bych měl vždy album 1:1 ke každému dni, ale se salátem náhodných fotek ve složce to pomůže.

Když jsem na cindy pracoval, narazil jsem na [tento bug](https://github.com/ianare/exif-py/issues/184) v knihovně exif-py.
Nakonec jsem ale veškeré knihovny na meta data fotek vzdal a volám prostě v subprocesu starý dobrý exiftool.
Aby to však bylo rychlé, naučil jsem se dělat [subproces pomocí asyncio](https://docs.python.org/3/library/asyncio-subprocess.html).
Frčí to jak namydlené.

## Anketa a focus

Prokrastinoval jsem zapracování zpětné vazby na anketu mezi juniory.
Jak se to celé táhne, tak už mě to moc nebaví.
Těším se, až to bude venku a budeme sbírat nějaké odpovědi.

Zamyslel jsem se i nad samotným důvodem, proč dělám anketu, a zda bych měl něco jako anketu vlastně dělat.
Z ankety nakonec bude třeba jeden článek na blogu, přitom to zabere hromadu práce.
Neztrácím těmito vedlejšími aktivitami focus?
Nemůžu přece dělat všechno.

Do budoucna se mi rýsuje trochu jiný systém.
Moje práce je budovat rozcestník, klub a příručku.
Řešit juniorům problémy, pomáhat jim sehnat práci.
Na to bych se měl soustředit.
Co se týče dalšího obsahu, myslím si, že bych jej **neměl tvořit**.

-   Mohu jej **nakoupit**.
    Vydělám peníze, někomu je dám, a ten někdo to pro junior.guru vyrobí: Podcast, článek, anketa…
-   Mohu jej **agregovat**.
    Najít existující obsah a udělat na junior.guru feed nebo katalog: Srazy, pracovní inzeráty, kurzy…
-   Mohu být **kurátorem**.
    Najít existující obsah a vybrat jen to nejlepší: Příručka

Všechny uvedené strategie do nějaké míry **škálují**.
Ale tvoření původního obsahu a osobní angažmá neškáluje.
Příručku tvořit chci, to ano, ale nic bokem už ne.
Nechci psát články pro jiná média, připravovat si složité přednášky pro konference, natáčet podcasty, vyrábět ankety.
Buď to udělají jiní a já jim dám prostor na svém webu a v klubu, nebo to neudělají a já hodím peníze na to, aby to vzniklo.
Ale svůj čas a svůj focus si musím chránit.

## Počátky blogu na junior.guru

Začal jsem pracovat na tom, aby bylo kam na junior.guru publikovat články.
V menu jsem položku Podcast přejmenoval na Novinky.
Přidal jsem boční navigaci a kromě podcastu jsem dal do stejné sekce i akce v klubu.

![Novinky]({static}/images/screenshot-2023-08-12-at-22-42-00-podcast-pro-juniory-v-it.png){: .img-thumbnail }

Akce jsem musel předělat ještě ze starého designu a staré infrastruktury.
Je to jedna z nejvíc zanedbaných stránek na webu.
Výhodou je, že cokoliv je lepší než co tam bylo, takže ani teď jsem se s tím moc nemazal.

![Původní akce]({static}/images/stare-akce.jpg){: .img-thumbnail }
Jak vypadaly akce původně

Dal jsem tomu CSSko z výpisu podcastových epizod a hotovo, _good enough_.
Pohraju si s tím později.

Uvažoval jsem, že sekci pojmenuju Log, Feed, Rozhled, Aktuality, Novinky, Aktuálně, Inspirace.
Nic z toho mi nepřišlo dost dobré a nakonec jsem zůstal u nudného „Novinky“, což je navíc prachsprostá kopie portálu [Na volné noze](https://navolnenoze.cz/novinky/), kde přesně takovou sdruženou sekci taky mají.
Jenže u jiných názvů, byť vzletnějších, mi nepřišlo, že by člověk věděl, co za takovým odkazem v menu čekat.
Název jsem řešil několik dní v hlavě a pak zhruba hodinu velmi inzenzivně.
Volal jsem si s kamarády a konzultoval ChatGPT.
Po hodině jsem mávl rukou a dal tam „Novinky“ s tím, že se nechci na něčem takovém zaseknout, ani to víc pitvat.
Zpětně se mi slovo „Novinky“ vlastně líbí, protože navádí do budoucna i na to, že to půjde odebírat newsletterem.

Rozepsal jsem si úkoly na příští týden a už se těším, jak mi to bude růst pod rukama.

## Další

-   Vyšel podcast, kde jsem s [Lucií Tvrdíkovou](https://www.linkedin.com/in/lucietvrdikova/) u Jury.
    Jurův status [tady](https://www.linkedin.com/posts/activity-7094597661684547584-d8sK/).
    Psal mi „máme za sebou 3 dny a před sebou víkend, máme 412 poslechů a hodně pozitivního feedbacku do soukromých zpráv“.
    Ke mě se na ten rozhovor zatím taky dostalo dost pozitivních ohlasů.
    Tohle vypadá, že vyšlo pěkně 💪
-   Do [grafu s anketou odkud chodí lidi](https://junior.guru/open/#vykonnost-kanalu-podle-ankety) jsem přidal odpověď „internet“.
    Hodně lidí to tam totiž píše.
    Původně to bylo v kategorii „ostatní“, ale nakonec jsem se rozhodl, že i takto vágní odpověď je pořád méně vágní, než „ostatní“.
    Například lze předpokládat, že tím většina myslí vyhledávání apod.
-   Kamarádka poslala nějaké PR na [real time bota](https://github.com/juniorguru/juniorguru-chick/), tak jsem dělal review atd.
-   Jedno celé dopoledne jsem zabil chozením po doktorech.
    Zatím spíš bez výsledku.
    Příští týden zas.
-   Udělal jsem v klubu Discord událost pro [PyCon CZ](https://cz.pycon.org/2023/) a pro [FrontKon](https://frontendisti.cz/konference), aby tam šli junioři.
-   Dal jsem na web měření [automated events](https://docs.simpleanalytics.com/automated-events), ale asi tam dám ještě i nějaké svoje ruční eventy.
    Tohle je sice hned hotové, ale já bych chtěl přesnější rozlišení např. prokliků přes loga firem apod.
-   Byl jsem na kamarádově oslavě narozenin.
    Děkoval mi, že jsem mu nedal alkohol, ale med a sirup.
    Asi už jsme staří.
    Všichni byli ve víru latinskoamerických tanců.
    Já tancuju leda tak na Michaela Jacksona, takže jsem odchytával ostatní netančící a konverzoval s nimi.
    Užil jsem si několik zajímavých konverzací - od padání z koňů, přes apartheid, království v Beninu, až po houby, LSD a šamany.
-   Měl jsem call s jednou vzdělávací agenturou, která si možná zaplatí partnerství, aby šla víc vidět v [katalogu](https://junior.guru/courses/).
    Byla to velká lekce prodeje.
    Pán byl sympatický, ale drsný.
    Čísla čísla čísla, chceme banner, chceme pixel na retargeting, chceme do vašeho newsletteru, ROI…
    „400 lidí? To je maličko…“
    Ozvali se mi sami! Já prodával. Já mám něco, co chtějí.
    Přesto jsem se celý call cítil zahnaný do kouta a vymezoval jsem si prostor.
    Stále jsem musel dohledávat tvrdá čísla.
    Na spoustu otázek jsem musel odpovídat, že to nedělám a dělat nechci, např. z etických důvodů.
    Každopádně zajímavá strategie, jak nakoupit, nacpat se všude, dostat hodně za levno.
    Snad jsem to nějak ustál.
    Přišlo to zrovna v den, kdy jsem dopisoval ten [letní pit stop]({filename}2023-08-07_letni-pit-stop.md), takže psychika nahoru dolů.
    Říkal jsem si potom, že přesně takového týpka bych potřeboval jako mentora, aby mě naučil dělat byznys 😀
-   Štvalo mě, že Dependabot vždy jde a otevře na junior.guru několik PR najednou.
    Jednak to spustí paralelně několik buildů a ty pak zbytečně zatěžují nějrůznější služby (takže to občas zbytečně spadne), jednak si to stejně šlape po prstech v lockfilech a musím ty PR rebasovat a čekat, atd.
    Takže jsem Dependabot [omezil](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#open-pull-requests-limit) na maximálně 1 otevřený PR a jednotlivé package managery jsem dal na různé dny v týdnu.
    Jsem zvědav, zda to pomůže.
    Upgrady balíčků budou pomalejší, ale přímočařejší a budou mě méně štvát.
-   Tady na blogu mi po upgradu Bootstrapu nefungovalo obarvení odkazů na zeleno.
    Opravil jsem to.
    Bylo to tím, že Bootstrap přidal nějaké `-rgb` barvičky a ty já jsem neměl definované.
    Trochu teda opruz, definovat dvakrát totéž, jednou jako hex a podruhé jako čísla.
-   Apple Silicon jsem [měl úplně mezi prvními]({filename}2020-12-18_i-bought-apple-silicon.md).
    Homebrew s M1 tehdy ještě nefungovalo moc dobře a musel jsem mít i záložní intelácký Homebrew přes Rosetta 2.
    Protože jsem se bál, že se něco rozbije, a protože jsem měl lepší věci na práci, měl jsem to tak doteď.
    Až teď jsem šel a ten intelácký Homebrew jsem [odinstaloval](https://github.com/homebrew/install#uninstall-homebrew).
    Překvapilo mě, jak jednoduše jde Homebrew odinstalovat.
    Zatím vše funguje.
    Sbohem, `arch -x86_64`!
-   Kamarád Vuy hledá práci.
    DevOps, Python, PowerShell, Linux, AWS, Azure, technical writing.
    Víc [tady](https://www.linkedin.com/posts/honzajavorek_hi-friends-i-am-looking-for-work-and-am-activity-7095427342566576129-xrWe?utm_source=share&utm_medium=member_desktop) a [tady](https://vuyisile.com/).
-   Sešel jsem se s Miou a Kubíkem z Python komunity.
    S Miou jsem řešil panel na PyCon CZ, s Kubíkem jsme šli za advokátkou a vysvětlovali jí, co je [Helios](https://vote.heliosvoting.org/) a jak funguje, abychom jej mohli přidat do stanov jako možný prostředek volby výboru.
    Samotného mě překvapilo, že Helios má i [heslo na Wikipedii](https://en.wikipedia.org/wiki/Helios_Voting).
-   Koukal jsem kamarádovi na jeho [nový projekt, který tiše spouští](https://richbull.co/).
    Psal jsem mu na to nějakou zpětnou vazbu.
-   Zjistil jsem, že Jinja [má nějaký byte code](https://jinja.palletsprojects.com/en/3.0.x/api/?highlight=cache#jinja2.BytecodeCache) a když se kešuje, dá se tím o dost urychlit build webovky.
-   Udělil jsem tři stipendia.
    Jedno z nich jsem potřeboval dát do budoucnosti a tím jsem si zkomplikoval čtení dat o předplatném ve svých skriptech, takže jsem to pak upravoval.
-   V souvislosti s [pit stopem]({filename}2023-08-07_letni-pit-stop.md) mi několik lidí nezávisle na sobě popisovalo svou zkušenost s hledáním juniorů přes junior.guru.
    Ve zkratce: Není to jednoduché a někdy to ani vůbec nevyjde.
    V klubu je to o náhodě.
    Na inzeráty na webu chodí kdokoliv z internetu, takže kvalita kandidátů pokulhává.
    No nebylo příjemné si to číst, ale aspoň mě to utvrdilo v tom, že inzeráty jsou prostě blbost a mým úkolem je najít jiný a lepší způsob, jak tuto věc řešit.
    Nápady mám.
    Otázka je, zda budou fungovat! 😀
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
    Psal jsem si s několika vzdělávacími agenturami a domlouval schůzky.
    Napsal jsem do Red Hatu, kterému bude končit partnerství.
-   Během 9 dní jsem ujel na kole 20 km. Celkem jsem se hýbal 6 h a zdolal při tom 20 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Vyhodnotit zpětnou vazbu od pokusných králíků, kteří viděli anketu pro juniory.
2.  Mít v Novinkách podstránky, přesunout tam existující příběhy juniorů a přidat tam meetupy.
3.  Rozjet „přáníčka“ od juniorů pro juniory, což musím stihnout do PyConu.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Pod čarou: Je lepší být turista než cestovatel. Výletník si na nic nehraje.](https://seznam-zpravy.u.mailkit.eu/mc/VUQMVLWE/ROTKZGIIFLKKNCEDKE/CLQEIELVLIL)<br>„Z cestování se stala obecně uznávaná kladná věc, která prý přispívá ke zlepšování rozhledu a vzdělání, i když realita často ukazuje pravý opak – na cestách si především chceme potvrdit vlastní představu o světě, a jakýkoliv rozpor našich názorů se skutečným stavem věcí snadno překryjeme různými mentálními kličkami (rasistického strýčka z jeho názorů dovolená v Tunisu většinou nevyléčí).“
- [AI is killing the old web, and the new web struggles to be born](https://www.theverge.com/2023/6/26/23773914/ai-large-language-models-data-scraping-generation-remaking-web)<br>„In recent months, discussions and experiments at some of the web’s most popular and useful destinations — sites like Reddit, Wikipedia, Stack Overflow, and Google itself — have revealed the strain created by the appearance of AI systems.“
- [RIP Metaverse, we hardly knew ye](https://www.businessinsider.com/metaverse-dead-obituary-facebook-mark-zuckerberg-tech-fad-ai-chatgpt-2023-5)<br>Tohle je skvělý. Facebook změnil název na Meta a Zuck oznámil Metaverse. Od té chvíle do toho tato a další firmy nalily hromady peněz, všichni papouškovali Zuckova tvrzení, plácali se po zádech, utužoval se hype, bullshit za bullshitem. Až to ze dne na den bez jediného úspěchu umřelo. „Decentraland, the most well-funded, decentralized, crypto-based Metaverse product (effectively a wonky online world you can "walk" around), only had around 38 daily active users in its "$1.3 billion ecosystem." Despite the might of a then-trillion-dollar company, Meta could not convince people to use the product it had staked its future on.“
- [Cyklistika je nejen sport, ale i transport. Má být brána stejně jako auta, shodují se města — Město](https://www.buzzsprout.com/2007031)<br>Jak je na tom cyklodoprava v Ostravě, Brně a Praze?
