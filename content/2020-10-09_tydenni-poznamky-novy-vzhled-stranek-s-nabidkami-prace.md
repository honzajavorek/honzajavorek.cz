Title: Týdenní poznámky: Nový vzhled stránek s nabídkami práce
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (5.10. — 9.10.) a tak [stejně jako minule]({filename}2020-10-02_tydenni-poznamky-nabidky-prace-podle-regionu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

V pondělí jsem měl dovolenou.

## Nový vzhled stránek s nabídkami práce

- Vytvořil jsem stránku pro [juniorní nabídky práce na dálku](https://junior.guru/jobs/remote/). S tím, co jsem si všechno připravil minulý týden, to bylo hotové za půl hodiny.
- Tím jsem splnil dva nejžádanější body z [ankety mezi uživateli JG](https://www.facebook.com/groups/junior.guru/permalink/450085692581710/): Filtrování podle regionu a podle toho, jestli jde o práci na dálku.
- Menu, kde si člověk překlikává regiony, jsem nějak nadesignoval a dal do horní části stránek. Nejsem s tím ještě nějak extra spokojený, ale je to lepší, než to bylo, takže šup s tím na produkci. Uvažuju, že bych ho na desktopu dal možná doleva jako sloupec, podobně jako je _table of contents_ u příručky a dalších stránek.
- Snažil jsem se, aby byly v novém vzhledu [stránky s nabídkami práce](https://junior.guru/jobs/) jasně a pokud možno stručně vyzdvižené hodnoty tohoto pracovního portálu oproti jiným, a to tak, aby to zapůsobilo jak na juniory, tak na firmy. Přibyly loga firem, které už u mě inzerovaly, a také loga míst, odkud stahuji další nabídky práce.
- Aby byla každému jasná hodnota mého robota, jsou tam přímo čísla, kolik nabídek práce robot vyřadil a kolik nechal. Chtěl jsem k tomu původně nakreslit robotické kuře, jak přebírá zrníčka, ale nakonec jsem byl líný to kreslit, a taky tam úplně není místa nazbyt. Abych mohl čísla zobrazit, musel jsem si na to připravit metriky na backendu a taky to správně spočítat (kdo ví, jak to mám s matematikou, nepřekvapí, že správně spočítat se mi to povedlo až napodruhé).
- Myslel jsem, že tlačítko na přidání pracovní nabídky bude někde vpravo nahoře a bude se posunovat spolu se stránkou, ale jakýkoliv pokus o toto řešení, který jsem učinil, se mi nelíbil. Prozatím je tedy tlačítko součástí pruhu odkazů na různé další věci.
- Protože by ho tam ale každý přehlédl, vytasil jsem se s [touhle blbinkou](https://roughnotation.com/), kterou jsem chtěl už hrozně dlouho použít, a která myslím náramně sedí do designu JG. Dokonce jsem si potom i pohrál s tím, aby se kroužek kolem odkazu kreslil až ve chvíli, kdy člověk odkaz vidí. Použil jsem [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) a zdokumentoval to v [GitHub Issue na projektu knihovny](https://github.com/rough-stuff/rough-notation/issues/51#issuecomment-705472507). Je to taková blbost, ale než vymyslím to tlačítko líp, bude mi tam dělat radost.
- Ladil jsem SEO elementy (_title_, _description_) a různé texty na jednotlivých stránkách.
- Upravil jsem zmínku o nabídkách práce na [úvodní stránce](https://junior.guru/). Tlačítko, které mířilo na newsletter, nyní míří přímo na [příručku o hledání první práce v IT](https://junior.guru/candidate-handbook/).
- O nabídkách práce se zmiňovala i samotná příručka, takže jsem se na to podíval a trochu to předělal. Vlastně nakonec úplně, ne trochu. Překopal jsem celou kapitolu o pracovních portálech. Dal jsem ji jako první ve své sekci a rozšířil jsem ji o vysvětlení nevýhod pracovních portálů. To může znít jako blbost, když jeden provozuji, ale není, protože kapitola končí tím, že pracovní portál na JG některé tyto problémy řeší, a vlastně tak kapitola čtenářům vysvětluje hodnotu mého produktu. Jelikož všechno, co tam píšu, je pravda, tak nemyslím, že je to nějaká nestoudná reklama - [posuďte sami](https://junior.guru/candidate-handbook/#job-boards). Odcitoval jsem tam i [yablka](https://www.youtube.com/watch?v=Ictmhp2uJu8), který poslední dobou točí [hezká videa na toto téma](https://twitter.com/yablko/status/1301811097159245825).
- Už delší dobu jsem toužil po tom, abych mohl na nabídky práce upozorňovat _inline_ v textu nebo třeba na 404ce. Vytvořil jsem tedy design pro takový menší, osekanější výpis nabídek práce, který funguje spíš jako upoutávka, než cokoliv jiného. Tento výpis jsem dal do relevantních částí příručky, vždy tak, aby to bylo nenásilné a plynule to navazovalo na kontext. Třeba u stáží je výpis pár stáží, pokud na JG zrovna nějaké jsou. Totéž u práce na dálku nebo dobrovolnictví. Výpis nabídek jsem dal i na tu 404ku. 404ka je důležitá, protože pokud na JG vyprší nabídka práce, původní URL už nikam nemíří a uživateli se zobrazí právě 404ka. Je tedy dobré, pokud člověka nasměruje na další nabídky práce.
- Opravil jsem průběžně spoustu nějakých vizuálnách bugů ve vzhledu výpisu nabídek práce a i jinde.
- Ve čtvrtek večer jsem se u sledování [Souboje Titánů (2010)](https://www.csfd.cz/film/236434-souboj-titanu/prehled/) musel opít vínem, abych film dokončil, takže se mi v pátek už nechělo nic moc dělat. Místo něčeho důležitého jsem vytáhl z hlubin backlogu průzkum [schema.org](https://schema.org/), což je způsob, jak lze sémanticky označit kusy stránky tak, aby jim mohli lépe porozumět roboti. Proč to dělat? Třeba Google je pak schopen stránku ve výsledcích zobrazit s nějakou přidanou hodnotou. Viz článek [tady](https://moz.com/learn/seo/schema-structured-data) nebo [tady](https://www.semrush.com/blog/what-is-schema-beginner-s-guide-to-structured-data/). Jedna z věcí, které jde označovat, je [nabídka práce](https://schema.org/JobPosting), což je pro JG jasná volba. Návod [here](https://schema.org/docs/gs.html), debugger [here](https://search.google.com/test/rich-results), za chvilu bylo hotovo.


## Další poznámky

- Upravil jsem čísla na [stránce pro firmy](https://junior.guru/hire-juniors/) tak, aby se místo 11000 zobrazovalo 11tis a otestoval jsem to.
- Videohovor o melouchu, do kterého se brzo pustím. Něco ohledně správného nastavení packagingu Python balíčků.
- Koukal jsem na Scrapy [AUTOTHROTTLE](https://docs.scrapy.org/en/latest/topics/autothrottle.html) nastavení a zkusil jej nastavit. Podle všeho by mělo stačit napsat do nastavení `AUTOTHROTTLE_ENABLED = True` :D Nevím, jestli to bude méně zatěžovat stránky, ze kterých stahuju nabídky práce, ale třeba jo.
- Produkce u JG vypadá tak, že se v noci spustí [CircleCI](https://circleci.com/), stáhne informace z internetu, vybuildí statickou webovou stránku a následně deployne na [Vercel](https://vercel.com/). Problém je, že CircleCI mašinky jsou samozřejmě z venku nějaká sdílená IP adresa, kterou všichni používají na všechno, a tudíž ji některé weby přímo blokují. Udělal jsem si tedy základní rešerši ohledně toho, co se dá dělat, když chce člověk používat nějakou jinou IP adresu, než na které je. Vylezlo mi z toho zatím [tohle](https://www.scrapehero.com/make-anonymous-requests-using-tor-python/), případně [tohle](https://www.khalidalnajjar.com/stealthy-crawling-using-scrapy-tor-and-privoxy/). Zatím jsem ani jedno nezkoušel.
- V podobném duchu jsem se pustil do hledání alternativy [SendGridu](https://sendgrid.com/). Jeho free plan má sdílené IP adresy, které se snadno mohou dostat do blocklistů. Takže e-maily, které pošlu, nemusí dorazit, jelikož je někdo po cestě zablokuje. Psal jsem na support, ale nic s tím nehodlají dělat. IP lze zaplatit, ale stojí to $90, což je pro mě trochu overkill. Já potřebuji posílat jen pár e-mailů, nejde mi o množství, ale potřebuji je posílat fakt spolehlivě. Alternativ je nesčetně. Pokud vás zajímají, [projděte si odpovědi zde](https://twitter.com/honzajavorek/status/1313411971044257792).
- Moje poznatky ohledně e-mailů: To, co chci, se jmenuje _transactional emails_. Existuje na to spousta služeb, které poskytují velké objemy a platí se hlavně za kvalitu doručování. Čím levnější, tím horší doručitelnost. Pokud je to zdarma, používají to spammeři a nedoručím ani prd. Pokud posílám desítky e-mailů (jakože posílám), nejspíš mi bude stačit prozatím posílat to normálně přes Gmailové SMTP :D Vlastně nevím, proč mě to předtím vůbec nenapadlo. Člověk má plnou hlavu _best practices_, až přes ně potom nevidí dostačující řešení.
- Když jsem se koukal na nějaké vhodné knihovny, nejvíc se mi zatím zalíbilo [yagmail](https://github.com/kootenpv/yagmail), ale pokud znáte něco lepšího, dejte vědět.
- Zdálo se mi, že se 1. října neodeslaly maily ohledně sponzorských log. No a taky že ne! Takže jsem našel chyby, proč se tak stalo, a skripty opravil. Znovu to posílat nebudu, inzerenti počkají do 1. listopadu. Nikdo si nestěžoval a já stejně musím nejdřív vyřešit to doručování mailů.

Toť vše! Další poznámky budou za dva týdny.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Studio N: Krvavý konflikt o Karabach může eskalovat ve válku](https://denikn.cz/452462/studio-n-krvavy-konflikt-o-karabach-muze-eskalovat-ve-valku/?ref=list)<br>Vysvětlení situace
- [Bláha: Vládní politici celou dobu lžou. Data z nemocnic byla tajná i před zdravotníky](https://video.aktualne.cz/dvtv/blaha-vladni-politici-celou-dobu-lzou-data-z-nemocnic-byla-t/r~3f29d4f8042411ebb115ac1f6b220ee8/)<br>Super rozhovor, díky za update ohledně toho, jak kvalitně se teď na zvládnutí covidu-19 pracuje
- [How One Guy Ruined #Hacktoberfest2020 #Drama](https://joel.net/how-one-guy-ruined-hacktoberfest2020-drama)<br>Proč lidi letos nadávají na Hacktoberfest
- [Karanténa, den čtvrtý: volá hygiena!](https://www.irozhlas.cz/komentare/covid-koronavirus-karantena-hygienicka-stanice-erouska_2010012215_jab)<br>“Tím, kdo v posledních týdnech s covidem-19 bojuje, jsou – ostatně stejně jako na jaře – Češi. Ne Česko.”
- [Ženy vybojovaly v krajích rekordní vítězství. Stále jich tam je ale jen pětina](https://zpravy.aktualne.cz/domaci/zeny-vybojovaly-v-krajich-rekordni-vitezstvi-stale-je-jich-a/r~6a3b9122062211ebb408ac1f6b220ee8/)<br>Zlepšujeme se, to je dobrá zpráva
- [Nahnal lidi na Letnou, zařídil Křečka a odešel do politiky. Minář má před sebou těžký úkol](https://a2larm.cz/2020/10/nahnal-lidi-na-letnou-zaridil-krecka-a-odesel-do-politiky-minar-ma-pred-sebou-tezky-ukol/)
- [Sociální demokracii čeká už jen jedna porážka](https://denikreferendum.cz/clanek/31732-socialni-demokracii-ceka-uz-jen-jedna-porazka?fbclid=IwAR0SxRoLwfU32fBIsknoOywuNsBWTM6304AjdpT37Ez7fxQn1PKFw5LNYcs)
- [Černí sokoli: příběh neslavného sociálního experimentu s africkými dětmi](https://finmag.penize.cz/recenze/420789-cerni-sokoli-pribeh-neslavneho-socialniho-experimentu-s-africkymi-detmi)<br>Příběh Namibijských dětí v ČSSR, o kterém jsem vůbec nevěděl
- [Volby přinesly naději na konec Babišovy éry](https://denikreferendum.cz/clanek/31729-volby-prinesly-nadeji-na-konec-babisovy-ery?fbclid=IwAR1vBiipVFAqFGaZFWk12mpQoSVwgcJkzLdNpxmMUpFmLox6lsT_IhpYb7M)<br>Možná přehnaně optimistické, ale přesto myslím hezké shrnutí voleb
- [Zemanovo mauzoleum: kanál Dunaj–Odra–Beznaděj](https://a2larm.cz/2020/10/zemanovo-mauzoleum-kanal-dunaj-odra-beznadej/)<br>Je to tak beznadějný, že už opět zbývá se tomu pouze zasmát s klasicky nihilistickým, přesným a vtipným Bilerem.
- [Předhoďte lidu Zemanův kanál. Ať neruší při rozdělování 180 miliard z fondu obnovy](https://nazory.aktualne.cz/komentare/predhodte-lidu-zemanuv-kanal-at-nerusi-pri-rozdelovani-180-m/r~88271988073811eb9d470cc47ab5f122/)<br>Je kanál jen vrtění psem?

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
