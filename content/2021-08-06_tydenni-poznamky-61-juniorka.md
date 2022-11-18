Title: Týdenní poznámky #61: Juniorka
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl další týden (2.8. — 6.8.) a tak [stejně jako minule]({filename}2021-07-30_tydenni-poznamky-60-nova-stranka-pro-klub.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Rozšiřujeme tým

Tento týden jsme společně s investorkou do našeho doposud dvoučlenného týmu vzali malou juniorku. Když jsem ji poprvé viděl, byl to nejkrásnější moment v mém životě. Strávíme teď asi hodně času jejím zaučováním, takže minimálně na několik týdnů se moje práce na JG zastaví, nebo výrazně zpomalí. Zkusím ale odpovídat lidem v klubu, to bych stíhat mohl. Aspoň budu psát kratší poznámky.

![Ruka]({static}/images/mimi-ruka.png)

Většina toho, co popisuji níže, se událo z kraje týdne. Po příchodu juniorky jsem neudělal už prakticky nic, ačkoliv jsem doma zatím sám. Sjíždím akorát YouTube videa o tom, jak se takové malé juniorky správně zaučují.


## Styly pro obsahové stránky

Překlopil jsem do nového CSS stránky pro [Zásady osobních údajů](https://junior.guru/privacy/), [Pravidla chování](https://junior.guru/coc/) (ty jsem musel překlopit i z HTML do MkDocs), [Obchodní podmínky](https://junior.guru/tos/). Chvíli jsem vymýšlel nějaký vymazlený způsob, jak udělat nadpis stránky, ale pak jsem to smazal a udělal tam prostě akorát čáru. Tyto stránky jsou předvojem toho, jak by jednou mohla vypadat příručka. Mají užší sloupec s textem, aby se to lépe četlo, a dal jsem víc prostoru mezi nadpisy druhé úrovně. Víc jsem si s tím zatím nehrál, ale neměla by to být finální podoba.

Při stylování právnických textů jsem narazil na [číslování pomocí CSS](https://2ality.com/2012/01/numbering-headingshtml.html), což jsem ani nevěděl že existuje, ale nakonec jsem si s tím nehrál, asi jsou na JG důležitější stránky, než text obchodních podmínek :)


## Rychlost webu

Dával jsem [novou stránku pro klub](https://junior.guru/club/) do [Lighthousu](https://web.dev/measure/) a zkoumal chyby, abych je opravil dřív, než začnu podobné HTML a CSS používat i na zbytku webu. Hned zkraje jsem dostal velmi vysoké skóre a v podstatě nejpomalejší věcí na webu byly Google Analytics, lol.

Každopádně jsem se díval na to, [jak správně použít a preloadovat fonty](https://web.dev/preload-optional-fonts/), protože ikony z Bootstrapu mám na webu jako font. Preloadování mi nefungovalo, dokud jsem patřičný tag nedal až za tag s připojeným CSS stylem. Nevím proč a beru to za šamanskou věc, která prostě pomohla, a kterou jsem vyčetl [někde v 15. zoufalém komentáři na StackOverflow](https://stackoverflow.com/a/59664927/325365) ¯\\\_(ツ)\_/¯ Taky je blbé, že Bootstrap ten font načítá s nějakým URL parametrem zřejmě s hashem fontu, asi kvůli kešování, takže ten [jsem si do HTML musel nějak načíst](https://github.com/honzajavorek/junior.guru/blob/5de500ff3b46ec5dc69eff6f5897a61dc95479a3/juniorguru/mkdocs/context.py#L63), abych tam mohl mít správné, plné URL toho fontu. No ale zdá se, že teď to funguje.

Další věc, na kterou jsem se podíval, byla optimalizace obrázků. Přečetl jsem si o tom něco na [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset) a na [Vzhůru Dolů](https://www.vzhurudolu.cz/), ale znělo to všechno komplikovaně a jako něco, co se mi řešit moc nechce. Pamatoval jsem si, že o obrázcích mluvil Aleš Roubíček na jediných Frontendistech, na kterých jsem byl osobně naživo. Přednášku jsem [našel na jeho YouTubu](https://www.youtube.com/watch?v=Ue-VygGkn-A&list=PLssB0sQU6z8aKFpk8VEXWRAMd-OZ6rLVj&index=5), ale nejde tam moc vidět na slajdy, tak ty jsem si [otevřel bokem ze SpeakerDecku](https://speakerdeck.com/rarous/optimalizace-obrazku). Uvažoval jsem původně, jestli si responzivní obrázky nepořešit nějak sám, nevygenerovat si je, atd., ale ta přednáška mě přesvědčila, že to dělat nemám a že mám použít [Cloudinary](https://cloudinary.com/invites/lpov9zyyucivvxsnalc5/vxcgupnrez4e028suyyo).

Cloudinary vypadá jako dost složitá služba s milionem nastavení a zmateným webem i klientskou sekcí, takže jsem byl rád, že mi někdo ukázal, co mám hledat a jak to můžu použít jednoduše. Chtěl jsem se podívat, jak to používají přímo Topmonks, ale jejich web není udělaný k rozebírání, jejich HTML je v jednom řádku. Asi nic, co bych nepřekonal, jen jsem zavzpomínal na staré časy, kdy malému Honzovi stačilo zobrazit zdrojový kód stránky a Ctrl+C, Ctrl+V. Každopádně něco jsem pak vykoukal a pomohlo mi to. To, co používají a je to teda i v té přednášce, je [Remote image fetch URL](https://cloudinary.com/documentation/fetch_remote_images#remote_image_fetch_url), což má hezkou dokumentaci, když víte, jak se to jmenuje. Sám bych to nikdy v Cloudinary nenašel, nakonec jsem byl vůbec rád, že jsem našel nastavení, jak to omezit pouze na doménu junior.guru. Pak stačilo chvilku si s tím hrát a udělat nějaká rozhodnutí ohledně toho, co vlastně chci.

Jedna věc, kterou jsem chtěl podchytit, byla fallback na můj neoptimalizovaný obrázek, pokud by Cloudinary selhalo, nebo bych byl prostě ve vlaku na špatném připojení a chtěl vyvíjet web, nebo bych chtěl načíst obrázek, který ještě není deploynutý na webu a Cloudinary si jej nemá odkud stáhnout. TopMonks mají v kódu něco jako `onerror="this.onerror = null; this.src = ...`, což jsem zkoušel, akorát s obrázkem z vlastního serveru, ale nefungovalo mi to. Nakonec mi zafungovalo až `this.src = this.srcset = ` a možná by stačilo i `this.srcset = `.

Nakonec jsem si vytvořil [tohle makro v Jinja2](https://github.com/honzajavorek/junior.guru/blob/5de500ff3b46ec5dc69eff6f5897a61dc95479a3/juniorguru/mkdocs/macros/shared.html#L1), které za mě všechno tohle řeší. SVG vkládám starým způsobem, bitmapy novým a s použitím Cloudinary. Musel jsem kvůli tomu překopat trochu zase makra a Markdown, abych mohl jedno makro používat v MkDocs jak v šabloně, tak v samotné stránce, kde mám Jinja2 taky.

Teď mám v tom Lighthousu [fakt pěkný skóre](https://lighthouse-dot-webdotdevsite.appspot.com//lh/html?url=https%3A%2F%2Fjunior.guru%2Fclub%2F). Kazí mi to především ty Google Analytics :D Pokud chcete Cloudinary taky použít, jděte přes [tenhle odkaz](https://cloudinary.com/invites/lpov9zyyucivvxsnalc5/vxcgupnrez4e028suyyo), dostanu za vás nějaké dobro.


## Další poznámky

- Domluvili jsme se s [Credo Ventures](https://www.credoventures.com/). Poslal jsem fakturu a nahodil logo na web. Ceník už se tak nějak ustálil a [byť jej mám stále v Google Docs](https://docs.google.com/document/d/1keFyO5aavfaNfJkKlyYha4B-UbdnMja6AhprS_76E7c/edit?usp=sharing), položky z něj jsem si přepsal do [ceníku ve Fakturoidu](https://www.fakturoid.cz/podpora/automatizace/cenik), ať nemusím pokaždé vymýšlet popisky na fakturu a přepisovat ceny.
- Zapisoval jsem si feedback od lidí na novou stránku klubu, abych věděl, co musím ještě opravit a doladit.
- Počet klubu přesáhl 200, tak jsem tuto radostnou novinu sdílel na sociálních sítích. Protože jsem tušil, že přijde juniorka, pověnoval jsem se z kraje týdne sociálním sítím celkově a naházel do fronty nějaké další statusy, hlavně upoutávky na přednášky a další tipy.
- Zkoumal jsem, jak přesně funguje [navigace v MkDocs](https://www.mkdocs.org/user-guide/configuration/#documentation-layout) a jak ji mohu co nejvíc využít. Překopal jsem nějaké věci a teď mám v konfiguraci navigace prakticky všechny stránky, které v MkDocs mám. Do šablony je vypisuji trochu složitěji, vyzobávám si z toho navigačního stromu vždy jen něco, ale to nevadí. V Jinja2 se [dá udělat leccos](https://github.com/honzajavorek/junior.guru/blob/5de500ff3b46ec5dc69eff6f5897a61dc95479a3/juniorguru/mkdocs/theme/main.html#L191), hlavně díky filtru `selectattr()`. Asi by to šlo předfiltrovat v Pythonu, ale teď mi to asi vyhovuje takto, stejně se to do budoucna nebude moc měnit.
- Domluvil jsem se s [Danem Srbem](https://coreskill.tech/), že pokud nebudu moct, zaskočí u přednášek v klubu jako uvaděč a moderátor.
- Animované podtržení části textu v záhlaví nové stránky klubu poskakovalo sem a tam, ale [povedlo se mi to nakonec opravit](https://github.com/rough-stuff/rough-notation/issues/63#issuecomment-891895740). Bylo to chybějícím `width` a `height` v HTML u ilustračního obrázku.
- Poslal jsem červencový newsletter.
- Koukal jsem trochu do čísel a došla mi jedna věc. Původně jsem JG dělal tak, že příručka a rady pro juniory přitáhnou lidi, tito lidi půjdou na nabídky práce a inzerce nabídek práce mě bude živit. Teď je to tak, že lidi chodí z Googlu aj. vyhledávačů na nabídky práce, díky tomu objeví zbytek JG, příručku a rady, a díky tomu časem třeba skončí i v klubu, což mě živí. Takže úplně naopak. Vyplývá z toho ovšem, že inzeráty práce má rozhodně dál smysl rozvíjet a investovat do nich energii a čas, a to nejen proto, že je to samozřejmě velmi užitečná služba pro juniory. Je to i nečekaně silný SEO nástroj, který na web dostává spoustu lidí.
- V souvislosti s předchozím bodem mě napadlo, že má možná Google rád moje inzeráty, protože jsem před časem všude natlačil [sémantické značení](https://schema.org/JobPosting), které se Google botovi mocinky líbí, ale kdo ví.
- Během 7 dní od 31.7. do 6.8. jsem při procházkách nachodil 4 km. Celkem jsem se hýbal 2 hodiny a zdolal při tom 4 kilometry.


## Co plánuji

Dvě věci, které bych chtěl zvládnout udělat příště:

1. Zaučovat juniorku.
2. Zvládnout v klubu přednášku s Petrem Viktorinem a propagovat další přednášku, s Ivanou Hučkovou.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Proč má inspekce práce problémy zjišťovat porušování zákoníku práce](https://a2larm.cz/2021/07/proc-ma-inspekce-prace-problemy-zjistovat-porusovani-zakoniku-prace/)<br>Přesný popis toho, jak probíhá kontrola inspekce práce a proč tento systém v současné době příliš nefunguje.
- [Programátoři dobrovolníci slaví druhé narozeniny. Jsou jich čtyři tisíce, fandí jim i PPF a míří do Evropy](https://specialy.ihned.cz/c7-66954060-1-acbfe9863063def)
- [Když markeťáci textují xenofobní normalizaci](https://a2larm.cz/2021/07/kdyz-marketaci-textuji-xenofobni-normalizaci/)<br>„Babišův marketing se snaží přispět k vítězství oligarchy tím, že přetavil internetové hoaxy do plynulé řeči evokující zmateného uživatele Facebooku.“
- [My tiny side project has had more impact than my decade in the software industry – Mike's corner of the web](https://mike.zwobble.org/2021/08/side-projects-vs-industry/)<br>Michael Williamson píše o tom, jak jeho hobby projekt, který vytvořil za pár odpolední, přináší světu viditelně větší hodnotu, než pravděpodobně cokoliv, co dělal za poslední dekádu jako svou primární práci. Zároveň ale nevidí jasnou cestu co s tím.
- [Radek Holý: Python je moje srdcovka](https://medium.com/applifting-cz/radek-hol%C3%BD-python-je-moje-srdcovka-60d3a02f9768) — jsou tam super lidi. Můžu doporučit taky webovky junior.guru věnované začátečníkům nejen v pythonu, které je konkrétním jazykem krásně provedou, naučí je programovat i jak si najít práci.“
- [Apple's Plan to "Think Different" About Encryption Opens a Backdoor to Your Private Life](https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life)<br>Apple přidává velmi rozporuplnou fičuru do fotek a iMessage všech svých uživatelů v USA.
- [An Open Letter Against Apple's Privacy-Invasive Content Scanning Technology](https://appleprivacyletter.com/)<br>Otevřený dopis Applu, který můžete podepsat.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
