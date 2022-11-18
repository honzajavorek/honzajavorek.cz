Title: Týdenní poznámky #37: První klubový sraz
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (8.2. — 12.2.) a tak [stejně jako minule]({filename}/2021-02-05_tydenni-poznamky-36-prvni-tyden-klubu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Klub

V průběhu tohoto týdne jsem se dále věnoval [klubu](https://junior.guru/club/). Každý den sleduji, co se tam děje a dělám si poznámky z toho, co se tam řeší, abych měl inspiraci na nové kapitoly do příručky. Zároveň na vše odepisuji, když tedy mám co odepsat. V klubu už je zhruba 100 lidí, žije to tam diskuzemi o materiálech, kurzech, motivaci, projektech, pohovorech. Radíme si o všem možném.


### Vylepšení avatarů na stránce klubu

Avatary členů na [stránce klubu](https://junior.guru/club/) jsem měl hotové už minulý týden, ale měl jsem tam chybu v číslu, což poškozovalo marketingové sdělení. Tu jsem opravil, použil jsem [fetch_members](https://discordpy.readthedocs.io/en/latest/api.html#discord.Guild.fetch_members). Avatarům jsem přidal `width` a `height`. Načítaly se přímo ze serverů Discordu, což jsem nechtěl, takže jsem trochu přebudoval backend a obrázky postahoval přes možnosti objektu [Asset](https://discordpy.readthedocs.io/en/latest/api.html#discord.Asset.save). Byly ve formátu WebP, což tedy má prý už dnes každý používat místo PNG, ale já jsem pozadu a konzerva, takže jsem zatím WebP neřešil (i když [gulp-webp](https://github.com/sindresorhus/gulp-webp) jsem teda našel a asi by nebylo to těžké přidat a všechny obrázky co mám převést). Stažené avatary jsem naládoval přímo do [Pillow, které WebP umí](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp), konvertoval do PNG, zmenšil, uložil. Paráda.


### Rozcestník pro členy

Zjistil jsem podle zpětné vazby, že registrace do klubu není pro mnoho lidí zrovna bezproblémová. Vytvořil jsem tedy novou stránku, [rozcestník pro členy](https://junior.guru/membership/), kde jsou všechny důležité odkazy a i nějaké praktické tipy. Na tuto novou stránku jsou lidi přesměrováni hned po registraci, ale mohou se na ni prokliknout i ze [stránky klubu](https://junior.guru/club/) přes odkaz.

Adresa je `/membership/`, ale po registraci přesměrovávám na `/membership/?state=success`. JG jsou statické stránky, ale toto mi umožňuje, abych se v JavaScriptu podíval do parametrů v URL a když tam najdu `state=success`, odkryju přes `display: block;` ještě jedno jinak skryté upozornění navíc. Klidně si to [zkuste](https://junior.guru/membership/?state=success).

Vyjel jsem si z Memberful seznam lidí, kteří mají členství, ale neprošli až do Discordu. Poslal jsem jim jednorázově ručně e-mail, kde jsem je na nový rozcestník upozornil a poprosil je, aby mě kontaktovali, pokud se nemohou do chatu dostat. Samozřejmě je možné, že mě chce někdo jen podpořit a do chatu vůbec nechce. To se uvidí, až vyprší těch prvních 14 dní zdarma :)


### První sraz

Chtěl jsem uspořádat nějaký první živý online sraz, abychom se trochu lépe poznali. V pondělí jsem vytvořil [Google dokument s informacemi](https://docs.google.com/document/d/171BZ-JcoRMdZxaL4F7VSUOMIdC3q4iCzp61zgnQ_vB8/edit?usp=sharing) a dal v klubu hlasovat o tom, který den to chceme udělat. Z hlasování vyšel čtvrtek, takže se to odehrálo včera. Měl jsem _lightning talk_ o tom, jak chápat a používat GitHub profil. Myslím, že to bylo fajn a vypadá to, že si to myslí i účastníci.

Řešili jsme nějaké technické potíže s Fedorou (nebo možná spíš Firefoxem) a s otravnými zvuky, ale vše jsme během dneška vyřešili, takže se to příště už nebude opakovat. _Lightning talky_ jsme z různých důvodů nestihli do pěti minut a volnou debatu se nám nedařilo úplně moderovat tak, aby nemluvili stále stejní lidé. Prošli jsme si tedy stejným problémem, jaký bývá i na jiných online srazech, když se pokouší o volnou debatu. Podle všeho ale tento problém vadí hlavně mě a dvěma dalším lidem, ostatní si to zřejmě užili i přesto.

Chtěl bych, abychom aspirovali na nějaké řešení toho problému. Jeden člověk tvrdí, že moderování nepomůže a řešit by to snad mohlo jít jen jinou technologií pro sraz (např. [gather.town](https://gather.town/)). Druhý člověk tvrdí, že bychom moderování měli dát ještě šanci, ale opravdu se tomu věnovat a aktivně zkoušet všechny moderovací techniky. Nevím, kdy bude další sraz, takže mám čas si to nechat projít hlavou, ale pokud máte nějakou zkušenost s nějakou z následujících technologií, budu rád, pokud se podělíte o dojmy:

- [gather.town](https://gather.town/)
- [reslash.co](https://reslash.co/)
- něco ze seznamu [tady na HN](https://news.ycombinator.com/item?id=25041946)
- něco ze seznamu [tady na Google docs](https://docs.google.com/spreadsheets/d/1R5DXWtz4H7eIT5VbGYJEdY0fHasekDxL_x-FN84ItvE/edit#gid=0)

Sraz probíhal od 18:30 zhruba do 22:30, za mě dobrý :) Uvažuji, že příště dotáhnu nějaké speakery s přednáškami, ale uvidím. Vlastně ještě nevím, jaký formát tomu chci dávat. Osobně by mi vyhovovalo, kdyby to nebyly nějaké velké pravidelné srazy, ale spíše častější setkání pro ty, kteří půjdou zrovna kolem, tu pokec, tu přednáška. Nechci konkurovat srazům jako Frontendisti nebo Pyvo, chtěl bych ty akce mít spíš nahodilejší, odlehčenější, pro utužení komunity uvnitř klubu. Vůbec by mi nevadilo, kdyby si nějaké srazíky časem uspořádali i samotní členové, klidně i bez mé účasti.


## Přebudování webu JG

Chystám se přebudovávat web JG tak, aby nově odrážel to, že klub je hlavní aktivita. Také chci, aby byla příručka snadno spravovatelná, lehce se do ní přidávalo, případně aby se do ní lidi nebáli poslat Pull Request. Jistě bych to mohl nějak splácat v tom, co mám, ale na to nějak nemám chuť. S _pivotem_ na klub mám vnitřní pocit, že stavět nad tím, co mám, by vyústilo v hrozný nepořádek a také by mě to nebavilo. Nevím, co z toho je horší. Takže uvažuji, jestli neudělat zásadní změny v architektuře webu, designu, atd.

Mou hlavní úlohou je teď věnovat se klubu a propagovat ho, získat pro něj aspoň 300 platících lidí. Zároveň ale nemám jinou naléhavou činnost, u které bych mohl "odpočívat" od komunikace a něco vyrábět. Myslím, že i kdyby se nepovedlo klub rozjet, bylo by dobré JG přebudovat tak, aby nebylo tolik závislé na mně a dalo se třeba do budoucna udržovat např. na dobrovolnické bázi. Tento týden jsem se tedy dost věnoval přemýšlení a vzdělávání:

- Koukal jsem na [Frontendisty o TypeScriptu](https://www.youtube.com/watch?v=9MaHeNOUv2Q). Vlastně ani nevím proč, TS mě nezajímá. Asi jsem chtěl jen vidět Aleše, jak všechny vyhejtí :D a co doporučí místo TS.
- Vyplnil jsem Frontendistům [dotazník](https://frontendisti.cz/dotaznik) a pak jsem si trochu prošel různé technologie, které zmiňoval, jako Snowpack, esbuild, PostCSS, PureCSS, Semantic UI. Nejvíce mě pro mé využití zaujal esbuild. U toho PostCSS jsem si nějak nebyl jistý, jestli to není něco, co mělo dřív význam, ale dnes už by mohlo být za zenitem, protože prefixů netřeba. Nicméně nedokážu asi fundovaně posoudit.
- Pustil jsem si pár videí na [YT kanálu CD, který jsem si nedávno oblíbil](https://www.youtube.com/channel/UCCfqyGl3nq_V0bo64CjZh8g). Nadšeně jsem o nich vyprávěl pár přátelům a ti se zakoukali do dalších videí a pak mi je posílali a vedli jsme o nich kratší nebo i dlouhé debaty.
- [Zeptal jsem se](https://www.facebook.com/groups/frontendisti/permalink/2750538771824296/), kde by se dal sehnat podklad pro CSS, který by byl trochu jako Tailwind, ale vlastně neměl s Tailwindem nic společného.
- Na základě odpovědí na dotaz jsem [pročítal velkou část dokumentace nejnovějšího Bootstrapu](https://getbootstrap.com/docs/5.0/) a zkusil vytvořit malinký prototyp, který by podklad z Bootstrapu používal. Zajímavá cesta.

Zamyslel jsem se zase nad tím, že příručka je ve své podstatě dokumentace a nebylo by od věci na ni použít nějaký dokumentační _engine_, jako třeba Sphinx. Jenže to už jsem trochu zkoušel a nikam to nevedlo. Taky mě štve, že teď JG používá Flask a Frozen-Flask, ale je to vlastně _overkill_ a už jen přegenerovat HTML vždy hrozně trvá. JG je ve své podstatě SQLite databáze, ze které se generují statické HTML stránky přes Jinja2. Flask mi pomáhá s pár detaily (třeba generování stránek s dynamickým URL, jako jsou nabídky práce, nebo provázání stránek přes `url_for()` apod.), ale jinak je tam vlastně zbytečně. Říkal jsem si, jestli v dnešní době není něco lepšího, co by mi řešilo většinu věcí a zbytek bych jen přiohnul. Mrkl jsem na [staticgen.com](https://jamstack.org/generators/), vyfiltroval na Python a Jinja2, procházel co najdu.

Jsem velkým fanouškem Sphinxu, ale jeho síla i velká nevýhoda je to, že stojí nad docutils. Ty jsou totiž abstraktní "DOM" dokumentu, jenž Sphinxu umožňuje pracovat s různými formáty a generovat různé výstupy (HTML, PDF...). Jenže tato abstrakce strašně zesložiťuje psaní nějakých rozšíření. Navíc docutils mají naprosto mizernou dokumentaci. Na tomto se prostě vždy zaseknu. Třeba v sekci [Jak začít](https://junior.guru/learn/#learn) mám obrázkový seznam a takových mám na JG hodně. V reStructuredText ani Markdownu je neudělám. Mohl bych si na to napsat rozšíření, ale ve Sphinxu to prostě nedám, je to strašné. A tak jsem začal koukat po [MkDocs](https://www.mkdocs.org/). Asi netušíte, jak se při tom cítím, prostě úplná hereze, ale dávám tomu šanci. Ještě větší hereze by byla klesnout k MDX a nějakým těm Gatsby/Next.js věcem, ale to mi asi fakt nehrozí, to bych se musel zbláznit.

- Chvíli jsem uvažoval, jestli mít Markdown v HTML (případně v Jinja2), jako to dělá třeba tady [nějaké rozšíření pro Flask](https://flask-markdown.readthedocs.io/) pomocí `{% filter markdown %}...{% endfilter %}`, nebo jestli mám mít občasné HTML v Markdownu.
- Pročetl jsem velkou část dokumentace MkDocs. MkDocs dnes vypadají kupodivu docela rozšiřitelně. Mám pocit, že když jsem se díval posledně, pluginy tam ještě nebyly.
- Koukal jsem, [jak lze v MkDocs použít třeba SCSS](https://github.com/mkdocs/mkdocs/issues/2276).
- Pročetl jsem velkou část dokumentace [Markdown knihovny pro Python](https://python-markdown.github.io/). Zkoumal jsem, jak se v Pythonu píšou rozšíření pro Markdown.
- Díval jsem se na [attr_list](https://python-markdown.github.io/extensions/attr_list/), který umožňuje vkládat CSS třídy přímo do markupu.
- Procházel jsem si [seznam rozšíření](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions), abych si je proklikal a podíval se, jak jsou vyrobené. Překvapilo mě, že jedno z nich mířilo na [můj repozitář](https://github.com/honzajavorek/markdown-del-ins). Pak jsem si vzpomněl, že vlastně jedno rozšíření opravdu spravuji. Jsem jeho maintainer, spravuji jeho balíček na PyPi. Dokonce jsem o tom myslím dřív psal tady v poznámkách. No, stane se, člověk zapomene :D
- Přemýšlel jsem i o něčem jako [MDX](https://mdxjs.com/) a koukal jsem se, v jakém stavu jsou [Web Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components) a jestli existuje něco, co pracuje s nimi. A našel jsem [MDJS](https://twitter.com/honzajavorek/status/1360225550644740096)!

Zatím se mi rýsuje něco jako:

- Zkusit udělat většinu webu nad MkDocs. Pokud mi nebude dostačovat běžný Markdown, zkusit si jej rozšířit. Uvažuji o něčem jako o možnosti napsat si v Jinja2 "komponentu" a tu potom moci "použít" v Markdownu, zavolat ji akorát s nějakými daty.
- CSS založit na podkladu z Bootstrapu, ale psát si nad tím komponenty v SCSS sám ručně pomocí BEMu jako doteď.
- Pokud JavaScript, tak vanilla ES2017 a pokud by ho bylo potřeba více, tak [Hotwire](https://hotwire.dev/).

Zatím jsem ale moc nepřišel na to, jak takové přebudování udělat jako _continuous delivery_ a nezbláznit se z toho. Jinak to ovšem dělat nechci, takže není cesta začít to šudlat někde bokem, jediná cesta je nějak to prostě vymyslet.


## Další poznámky

- O víkendu jsem napsal [článek o tom, jak napsat neinteraktivního Discord bota]({filename}/2021-02-06_how-to-create-non-interactive-discord-bot.md).
- Hned z kraje týdne se [rozbilo](https://twitter.com/honzajavorek/status/1358749770886619140) napojení na API [remoteok.io](https://remoteok.io/). Opravil jsem to tak, aby se má strana s chybou vyrovnala a prostě v takovém případě vyhodila nula nabídek. Teď koukám, že už to opravili.
- Odstranil jsem Stripe z dependencies JG, protože jej nakonec nevyuživám napřímo, ale přes Memberful.
- Vymysleli jsme v klubu jiný název pro hlavní hlasový kanál, aby se nepřekrýval s hlavním textovým a lidé se omylem nepřeklikávali.
- Koukal jsem na kousek [debaty o NNŽ](https://www.campuj.online/).
- Připomenul jsem se jednomu vydavatelství s tím, že bychom mohli domluvit slevu na knihy pro klub. Zatím bez odpovědi.
- Připomenul jsem se někomu, kdo mi má poslat fakturu. Poslední dobou mi nějak neodepisují lidé ani firmy, až mám skoro obavu, jestli mi funguje e-mail. Ale asi mi prostě akorát neodepisují :-/ Že mi ale člověk nepošle fakturu když mu mám zaplatit peníze? :)
- Domluvil jsem se na příští týden na venkovní kafe s jedním velkým šéfem.
- Naceňoval jsem nabídku pro jednu firmu. Dělal jsem to vždy večer a nasekal jsem v tom postupně různé chyby a pak jsem se omlouval. Poučení: Když už mi nejde ta matika, tak bych ji aspoň měl dělat ráno, nebo nevím. Dopadlo to dobře, faktura odeslána, roční členství v klubu a logo na příručce bude!
- Koukal jsem na [piano](https://andrewsvk.github.io/piano/), které vytvořil jeden člen klubu.
- Koupil jsem si běhací ledvinku na mobil, ale ještě jsem v ní nebyl. Při posledním běhu jsem uklouzl na bahně a spadl do šípkového keře, takže tento týden jsem nechával odpočinout kotník.
- Zjistil jsem, že na světě existují dvě ikony pro sdílení a podle toho, jestli používáte Google nebo Apple jste velmi pravděpodobně zvyklí jen na jednu z nich a automaticky jí rozumíte, ale té druhé ne. Anketa [zde](https://twitter.com/honzajavorek/status/1360223114714611713). Někdo mi řekl "dej tam ikonu na sdílení, takové ty tři tečky spojené čárama, tomu rozumí každý". Vůbec jsem netušil, o čem je řeč!


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. **[PANIC MONSTER](https://waitbutwhy.com/2013/10/why-procrastinators-procrastinate.html)** Napsat konečně článek pro [Kariérko.cz](https://karierko.cz/) **[PANIC MONSTER](https://waitbutwhy.com/2013/10/why-procrastinators-procrastinate.html)**
2. Začít předělávat web junior.guru tak, aby klub byl v centru dění.
3. Napojit nabídky práce z [Dobrého šéfa](https://dobrysef.cz/).


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Varování: Plus size modelka na obálce časopisu škodí zdraví?](https://www.heroine.cz/styl/3968-varovani-plus-size-modelka-na-obalce-casopisu-skodi-zdravi)<br>“Pokud je na obálce příliš hubená modelka, nikdo v takové míře naštvané statusy nepíše a její zdraví se neřeší.”
- [Redneck #41: Kdo je Kamala Harris?](https://soundcloud.com/rdnck/redneck-41-kdo-je-kamala-harris)
- [Redneck #42: Od segregacionistů až po Irák. Jakou kariéru má za sebou nastupující prezident Biden](https://soundcloud.com/rdnck/redneck-42-od-segregacionistu-az-po-irak-jakou-karieru-ma-za-sebou-nastupujici-prezident-biden)<br>Kdo je Joe Biden?
- [Trendsetter: Bernie Sanders](http://markething.cz/trendsetter-bernie-sanders)<br>Virální palčáky a jak to Bernie hned podchytil. Možná Amerika, možná by to šlo i u nás. V březnu 2020 mohl Hamáček prodávat červené svetry a dávat výtěžek na charitu. Možná měl jiné starosti než marketing.
- [Žijeme ve státě, který nám umírá před očima. Tentokrát bohužel doslovně](https://nazory.aktualne.cz/komentare/zijeme-v-absurdni-republice-predstirani-kdyz-neni-ockovani-m/r~453cb266608b11eb8972ac1f6b220ee8/)<br>“Nepotřebujeme, aby se v zemi rozmohla kultura kolektivního předstírání, jakého jsme si v 70. a 80. letech minulého století užili víc než dost.”
- [My product is my garden](https://herman.bearblog.dev/my-product-is-my-garden/)
- [Homebrew Python Is Not For You](https://justinmayer.com/posts/homebrew-python-is-not-for-you/)<br>Python v Homebrew není vhodný pro vývoj. Používejte pyenv nebo asdf. Sám s tím už bojuju delší dobu. I na macOS je zjevně správné nastavení Python prostředí chaos.
- [Rozhovor s Pavlou Říhovou: Ředitel Geuss Inspekci životního prostředí rozložil](https://denikreferendum.cz/clanek/32285-rozhovor-s-pavlou-rihovou-reditel-geuss-inspekci-zivotniho-prostredi-rozlozil)<br>“Po nástupu inženýra Geusse klesl celkový počet pokut uložených inspekcí a jejich výška o třetinu až čtvrtinu.”
- [Why the EU lost the vaccine war](https://unherd.com/2021/02/why-the-eu-lost-the-vaccine-war/?=frlh) než jako efektivní startup, jenž se nebojí technologií, inovací a umí se soustředit na řešení té aktuálně jediné nejdůležitější věci.
- [When Test Driven Development Goes Wrong](https://www.youtube.com/watch?v=UWtEVKVPBQ0)<br>Vypadají vaše testy tak jako tady v tomto videu? Pak asi děláte něco špatně. Musím uznat, že v minulé práci jsme přesně takhle špatně udělali podle mě skoro všechny testy :D
- [Tereza Soušková: Navalnyj není lidskoprávní hrdina. Ruská veřejnost řeší jiné problémy](https://a2larm.cz/2021/02/tereza-souskova-navalnyj-neni-lidskopravni-hrdina-ruska-verejnost-resi-jine-problemy/)<br>Super vysvělení situace v Rusku
- [Šárka Homfray: Výrazná část politické elity je vyčpělá a nedokáže se zamyslet nad budoucností. Vize už se ani nepředstírají](https://a2larm.cz/2021/02/sarka-homfray-vyrazna-cast-politicke-elity-je-vycpela-a-nedokaze-se-zamyslet-nad-budoucnosti-vize-uz-se-ani-nepredstiraji/)<br>Zajímavý rozhovor o práci, odborech, práci a ženách a tom, jaká je budoucnost práce v Česku
- [Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
- [Citizenship Is A Myth](https://www.noemamag.com/citizenship-is-a-myth/)<br>Ideje, na kterých stojí dnešní občanství, jsou dávno rozpadlé a neplatné. Občanství si můžete koupit, nebo můžete být rodilý občan, který nemá právo ani volit. “The membership model is increasingly blind to political, civil and social reality.”
- [Je to druh sociální kritiky, říká Marie Heřmanová o konspiračních teoriích](https://www.novinky.cz/kultura/salon/clanek/je-to-druh-socialni-kritiky-rika-marie-hermanova-o-konspiracnich-teoriich-40350134)<br>“Dalo by se říct, že věříme konspiracím, protože jinak bychom museli uvěřit, že selhal kapitalismus – ale to by byla moc velká kognitivní disonance, to jde proti všemu, co se tady třicet let říkalo. Konspirace mohou lidem dávat paradoxně větší smysl.”

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
