Title: Týdenní poznámky #59: Plakátky na přednášky
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (19.7. — 25.7.) a tak [stejně jako minule]({filename}/2021-07-16_tydenni-poznamky-58-po-tydnu-volna.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

V pátek se mi chtělo odpoledne spíš pracovat než psát poznámky a nechtěl jsem jejich psaní hrotit do noci, tak jsem to nechal na víkend. Jenže o víkendu jsem seděl hodně u počítače kvůli tomu, že jsem se rozhodl kompletně překopat způsob, jakým zálohuji data, takže jsem neměl vůbec chuť poznámky psát a píšu je nakonec až v pondělí.


## Design pro plakátky

Rozjíždí se zase přednášky v klubu a [první bude s Norou Kořánovou](https://junior.guru/events/#2021-07-27T18-00-00). Domluvili jsme si s Norou informace o přednášce. Zapsal jsem je do souboru `events.yml`, aby se mi vygeneroval plakátek, aby bot upozornil na přednášku a aby se objevila na webu.

To se nestalo, protože plakátek neměl žádné CSS, tento soubor nebyl propojený s webem a jediné, co jej aspoň trochu respektovalo, byl ten Discord bot. Takže hurá do práce, dodělat resty:

- Jeden celý den jsem designoval nový plakátek. Ten, který to tvoří teď, už je plně vytvořený automaticky, ne mnou ručně v Keynote (lol).
- Plakátek nejbližší přednášky se nastaví jako `og:image` pro [stránku s přednáškami](https://junior.guru/events/).
- Přednášky na [oné stránce](https://junior.guru/events/) se nyní vypisují z dat v souboru `events.yml`, doteď jsem je tam musel stále ještě psát ručně v HTML.
- Začal jsem generovat plakátky v různých velikostech, jak pro web do `og:image`, tak jako _thumbnail_ pro YouTube video se záznamem. Čtvercová verze pro Instagram už se mi generovala z dřívějška. Při ladění velikostí obrázků a poměrů stran se mi hodil [tento článek](https://iamturns.com/open-graph-image-size/) a tato skvělá [stránka s trojčlenkou](https://www.vypocitejto.cz/trojclenka/) :D Verzi pro YouTube mám podle rozměrů z jejich dokumentace, ale když to nahraju jako _thumbnail_ na video, vidím to oříznuté, tak nevím ¯\\\_(ツ)\_/¯ Všechna stará videa jsem opatřil novými obrázky.
- Přidal jsem k `events.yml` dokumentaci v podobě spousty komentářů, kdyby se tam náhodou chtěl nějaký speaker přidat sám přes PR. Například [Petr Viktorin](https://github.com/honzajavorek/junior.guru/pull/647), který to hned potom udělal.

Díky tomu všemu jsem ukrojil hned několik dalších úkolů ze [seznamu věcí, které musím kolem každé přednášky udělat](https://gist.github.com/honzajavorek/b1a77651e566cb6405a131bbf1fb0692). Automatizace pokračuje! Stránku s akcemi bych chtěl jednou celou předělat a udělat hezčí, teď je to spíš ostuda, ale teď to ještě musí bohužel počkat.

Zabýval jsem se dále domlouváním a připravováním dalších přednášek. Po delší pauze jsem se dostal do opačného problému, přednáška teď bude skoro co týden :) Už se těším!

![Nora Kořánová]({static}/images/talk-nora.png)

![Petr Viktorin]({static}/images/talk-petr.png)

![Ivana Hučková]({static}/images/talk-ivana.png)


## Nová klubová stránka

Práce na [nové stránce lákající na klub](https://junior.guru/club2/) a celkově na novém designu JG pokračují, byť tento týden nebyl ten posun velký. Dolaďoval jsem barvy, opravoval některé chyby, a tak.

Ke konci týdne jsem se rozhodl podívat se konečně na vršek stránky, který by měl být nejpromakanější a měl by upoutat. Zatím jsem to spíš odkládal. Prošel jsem si [tento článek](https://uxplanet.org/website-header-design-in-2020-best-practices-and-examples-1992f80ddd69), abych nabral inspiraci, a pak jsem udělal velkou věc: Dal jsem vršku žluté pozadí. A hned to trochu prokouklo! :D Byl už konec týdne, tak jsem si nadělil odměnu a místo efektivního postupu jsem si pohrál s nápadem, že spodní okraj vršku by mohl připomínat rozlámanou skořápku od vajíčka (maskotem JG je kuře klubající se z vajíčka).

Zkusil jsem to nejdřív přes [border-image](https://developer.mozilla.org/en-US/docs/Web/CSS/border-image), ale to mi akorát připomenulo, že `border-image` je pro mě nepochopitelná věc, pro kterou si neumím potřebný obrázek představit v hlavě, vytvořit na počítači, ani debugovat v prohlížeči. Byť jsem našel [téměř hotové řešení](https://atelierbram.github.io/frame-patterns/), nakonec jsem to stejně zahodil.

Moje řešení nakonec využívá starý dobrý [background-image](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image), s pár novějšími vychytávkami (novějšími v mém případě znamená, že už je 10 let podporují všechny prohlížeče). Našel jsem [toto řešení](https://stackoverflow.com/questions/53650302/container-with-zigzag-border-at-bottom-only-apply-to-the-border) a pak jsem si SVG obrázek upravoval v Inkscape tak dlouho, až se mi výsledek líbil a přišlo mi, že plus mínus připomíná skořápku. V Inkscape neumím skoro nic, takže i takovéto [velmi základní video](https://www.youtube.com/watch?v=QbjKrRhGXmU) mi pomohlo hned s několika triky.

Nebudu lhát, je úplně jedno, jestli je tam skořápka nebo ne, na úspěch stránky to nebude mít vliv a jen se s tím zdržuju. Ale člověk si to musí taky někdy udělat trochu hezký. Kdybych se fakt snažil a vymýšlel _business value_, která by za tím byla, asi by to byla jedině lepší rozpoznatelnost a zapamatovatelnost designu stránek. Což nakonec není úplně blbé, dneska všechny weby vypadají úplně stejně, takže laťka je i docela nízko :D Byť v rámci feedbacku se objevilo i to, že ten web teď „smrdí“ Bootstrapem (to nejsou slova dané osoby, ale já sám bych to řekl takhle), takže kdo ví. Třeba se mi ten Bootstrap povede ještě trochu další prací zamaskovat. A i kdyby ne, je to asi nakonec jedno, hlavně že se mi to dobře dělá, vydělává to (uvidíme!) a je to dobře použitelné pro návštěvníky webu.


## Markdown v Markdownu

Jako by mi nestačilo, že mám v nové verzi webu šablonování pomocí Jinja2, které je vlastně vnořené v původní Jinja2 od MkDocs, zjistil jsem, že budu potřebovat i Markdown v Markdownu.

Při tvorbě stránky pro klub jsem se totiž dostal do situace, kdy jsem potřeboval přidat ještě nějaké další HTML tagy přímo do Markdownu, třeba na oddělení jednotlivých sekcí stránky, jenže potom se mi už nerenderoval Markdown uvnitř. Částečně to lze řešit pomocí [markdown="1"](https://python-markdown.github.io/extensions/md_in_html/), jenže tenhle atribut se pak musí dát na všechny rodičovské obalovací elementy, takže když tam mám dva, musí tam být dvakrát, když tři, tak třikrát. A stejně to nefungovalo nejlíp.

Takže jsem začal chtít něco jako `{% call markdown %}**sem** píšu __markdown__{% endcall %}` (Jinja2 makro), nebo třeba `{{ variable|markdown }}` (Jinja2 filtr), aby se lépe psaly stránky, kde je nakonec víc HTML, než samotného Markdownu. Toto makro nebo filtr by vrátilo HTML markup, ten by se jako součást Jinja2 šablony vyrenderoval do HTML a to by MkDocs považovaly za Markdown, ale to je v pořádku, protože HTML může v Markdownu být, to vůbec nevadí, parser si ho nevšímá a nechá ho být tak, jak je. Ještě by se to dalo řešit tím, že pro tyhle stránky, kde je hodně HTML, bych použil úplně vlastní šablony přímo v _theme_ stránek, ale to mi přišlo jednak méně pružné, jednak bych měl různé stránky v různých složkách, prostě se mi to nelíbilo. A stejně bych tam občas ten Markdown použít chtěl ¯\\\_(ツ)\_/¯

Jenže to nebylo tak jednoduché jako importovat si Pythoní Markdown parser a udělat na dva řádky filtr do Jinja2. Protože by nefungovalo `{% call markdown %}odkazování [na další stránky](tos.md) stejně jako ve zbytku MkDocs{% endcall %}`. Ajaj! Takže jsem zkoumal, jak tohle makro a filtr napojit na to, jak Markdown renderuje přímo MkDocs. A bohužel to není v MkDocs příliš uděláno tak, aby to šlo použít i jinde, takže jsem se musel uchýlit ke [škaredé černé magii](https://github.com/honzajavorek/junior.guru/blob/92ffe220444bea7d520b78a70c67f5cb82505614/juniorguru/mkdocs/hooks.py#L65). Nicméně funguje to. A s výsledkem, tedy s tím, jak se to používá při psaní samotné stránky, jsem naprosto spokojen.


## Další poznámky

- O předešlém víkendu jsem si zkoušel hrát s alternativami Heroku, které by byly scale-to-zero a hodily by se např. na provozování příkladů pro [cojeapi.cz](https://cojeapi.cz/). Dostal jsem mimo jiné tipy na [Render](https://render.com/render-vs-heroku-comparison) a [Fly](https://fly.io/), z nichž zdarma je pouze Fly. Sice se musí zadat kreditka, ale dá se, na rozdíl např. od Google Cloudu, zadat i Revolut _prepaid_ karta, na které skoro nic nemám, takže pohoda. Když jsem chtěl zkusit spustit svůj první projekt, zaseklo se to na ověření účtu. Napsal jsem na support a odpověděli, že jsou obezřetní kvůli těžařům kryptoměn a že za to mrzení mi dají zdarma kredity navíc. Jenže jsem se k tomu pak už nějak nedostal, takže pokračování někdy příště.
- Zpracoval jsem jeden inzerát práce přidaný na JG (za 0 Kč).
- Zkoušel jsem o víkendu při svých zálohovacích dobrodružstvích [osxphotos](https://github.com/RhetTbull/osxphotos) pro čtení informací z Apple Photos a funguje to pěkně :) Škoda, že do Apple Photos nejde i programátorsky zapisovat a musí se do toho klikat.
- Zkusil jsem si do TweetDecku přidat sloupec, který bude sledovat určitá klíčová slova, včetně různých vzdělávacích agentur na českém trhu apod., prostě vše, co by mohlo souviset se segmentem trhu, na kterém se snaží prorazit JG. Od té doby jsem zatím ve TweetDecku nebyl :D
- Měli jsme v klubu rekord 42 pozitivních reakcí na zprávu (v souhrnech nejzajímavějších věcí za poslední týden je číslo). Zpráva byla o tom, jak se členovi povedlo sehnat první práci, čím prošel, co a jak udělal.
- Objevila se nějaká chyba v parseru inzerátů, který jsem kdysi dělal a jehož výsledky se teď ve skutečnosti nepoužívaly. Byl to pokus inteligentně rozsekat text inzerátu na sekce, u nichž bych znal jejich sémantický význam. Nefungovalo to špatně, ale nakonec se mi dařilo třídit inzeráty celkem efektivně i bez toho. Občas mi ty sekce pomáhaly při debugování jiných věcí, tak jsem je tam nechal, ale teď, když se objevila chyba, jsem ji odmítl řešit a prostě jsem akorát tuto část zcela vypnul.
- Přečetl jsem si [tento článek na iDNES](https://www.idnes.cz/finance/prace-a-podnikani/it-kariera-vzdelani.A210701_615448_podnikani_sov) a napsal na něj svou recenzi v podobě [tohoto komentáře na LI](https://www.linkedin.com/feed/update/urn:li:activity:6822108532133961728/?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A682210). Pak jsem zkusil napsat přímo do iDNES přes nějaký kontaktní formulář, že až budou chtít příště nějakou mluvící hlavu, můžou klidně napsat mně, místo pana Strejce :D
- Řešil jsem trochu vztahy a chování v klubu. Snad to bude OK. „Založil si komunitu a chodili mu tam lidi“ ;) S tímhle se holt musí počítat. Vztahy mezi lidmi a komunitní dynamika jsou velkými riziky mého podnikání. Ovlivním je jen o něco málo víc, než zemědělec ovlivní počasí. Mám [CoC](http://junior.guru/coc) a nesmím váhat při jeho dodržování, jinak se jedna z hlavních výhod klubu, tj. přátelské prostředí, rozplyne, ani nebudu vědět jak. To ode mne vyžaduje umět jít příkladem, nastavovat správná očekávání, vysílat správné signály na správná místa, umět občas udělat špinavou práci a vyřešit i méně příjemné věci, než se rozjedou k nezastavení.
- Rozmnožili se v klubu lidi, kteří se učí C#, tak jsem jim k tomu vytvořil dedikovanou místnost.
- Zjišťoval jsem, jak fungují kredity na [Italki](https://www.italki.com/), protože uvažujeme s Mews o tom, zda bychom je nemohli určitým lidem dávat na zlepšení angličtiny. Italki mi přijde lepší než kurz, protože kurzů je hodně a jsou i zdarma, ale málokdo se do toho dokope. Když si na Italki vybere lektorku nebo lektora a budou mít hodinu týdně, prostě se k tomu podle mě dokope a ještě to bude mít větší dopad (sebevědomí, mluvení…).
- Napsal jsem tady na blog reakci na jedno video: [Proč se neučit Python v roce 2021]({filename}/2021-07-21_proc-se-neucit-python-v-roce-2021.md)
- Czechitas chtějí analyzovat nabídky práce pro juniory, tak jsem se nabídl, že scraping mám _de facto_ hotový a data bych mohl poskytnout. Následně jsme si volali a nejspíš z toho bude spolupráce :)
- Všiml jsem si, že už je v klubu skoro 200 lidí a samotného mě to překvapilo :D
- Pomáhal jsem jednomu členovi klubu s motivačním dopisem a CV před tím, než se zkusí přihlásit na inzerát.
- Konečně jsem se podíval na [PR od Míly](https://github.com/honzajavorek/junior.guru/pull/579), který by měl posunout o krok dál přesun vyhodnocování nabídek práce od regulárních výrazů směrem k AI.
- Štvalo mě, že když mi napsal můj Discord bot, Kuře, tak se mi v levém seznamu na Discordu objevil se stejnou žlutou ikonou, jako má samotné JG. Takže nešlo poznat, co z toho je klub a co z toho zprávy od bota. Nakreslil jsem tedy alternativní ikonu, která má modré kolečko a bílé kuře, abych to nějak rozlišil. Trvalo mi sto let najít místo, kde se ta ikona mění. Proklikal jsem snad vše ostatní, než jsem našel [discord.com/developers](https://discord.com/developers/) a vzpomněl si, že něco takového vůbec existuje. Tam jsem změnil ikonu a nic se nestalo. Teď píšu poznámky a zase na to koukám a zjišťuji, že to byla ikona OAuth2 aplikace, ne bota. Ten má ještě jinou stránku. Takže se mi to reálně povedlo změnit až teď.
- Přejmenoval jsem hlavní větev tady na blogu z `master` na `main`. Na GitHubu je teď výchozí `main`, což mám tedy na nových projektech, ale potom se pletu, takže lepší, když bude `main` všude.
- Propagoval jsem dále své nedávné působení v .NET.CZ podcastu, [retweetem](https://twitter.com/dotnetcezet/status/1414499848250875904) a [přesdílením postu na LI](https://www.linkedin.com/feed/update/urn:li:activity:6820615880590807040/)
- Spoustu času tradičně sežralo procházení diskuzí v klubu, reakcí na sociálních sítích, e-mailů…
- Během 10 dní od 17.7. do 25.7. jsem při procházkách nachodil 3 km, ujel na kole 98 km. Celkem jsem se hýbal 12 hodin a zdolal při tom 101 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Zvládnout po dlouhé době přednášku v klubu, která bude v úterý.
2. Bušit dál CSS na té klubové stránce.
3. Propagovat [další dvě naplánované přednášky](https://junior.guru/events/#planned) a naházet nové věci do fronty na sociální sítě, kde teď nic nemám.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [ČSSD vsadila vše na jednu kartu. Vlažný start kampaně ji může přijít draho, v boji o voliče se navíc skrývá past](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.info.cz%2Fnazory%2Fcssd-vsadila-vse-na-jednu-kartu-vlazny-start-kampane-ji-muze-prijit-draho-v-boji-o-volice-se-navic-skryva-past%3Fodemknout%3DURRFXORSFF&h=17bae2b43ad8a2b18e46f7f448f0a6604edb124b4e0b9349662cba44bfcf665c)<br>Neexistence levice v příští sněmovně znamená, že polovina republiky v ní bude zastoupena skrze populisty, v horším případě nahnědlé. Můžete volit pravici, ale tohle je prostě realita. Je to jako byste neměli rádi hmyz a jeho vyhubení by vás těšilo, aniž byste si uvědomovali, že hraje v ekosystému nějakou roli a bez něj tady všichni umřeme.
- [Co trápí rodiče s dětmi v Praze? Na mnoha místech se cítí jako nezvaní hosté](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F06%2Fco-trapi-rodice-s-detmi-v-praze-na-mnoha-mistech-se-citi-jako-nezvani-hoste%2F&h=4e36390ae8c0fb7bad9b568c6b304c374d3052b231f8b714016897b1caf03f9d)<br>Zajímavý podcast o tom, jestli a jak je město vhodné pro život nebo pohyb s dětmi, jaká jsou oblíbená místa rodičů v Praze, na co se zapomíná, nebo co za překvapivé věci vyšlo ze souvisejícího dotazníkového průzkumu. Zajímavý a důležitý je i postřeh o tom, že v Česku existují dva segregované, paralelní světy: pro děti a pro dospělé. Přitom to vypadá, že lidem je úplně nejlépe na místech, kde se zabaví jak děti, tak dospělí, a kde jsou děti do dospěláckého světa bez velkých ofuků přizvány jako běžná součást života.
- [Vadí × nevadí: Jak se žije dětem a rodičům v Praze?](https://getpocket.com/redirect?&url=http%3A%2F%2Fwww.vipergallery.org%2Fvystava%2Fvadi-x-nevadi-jak-se-zije-detem-a-rodicum-v-praze&h=db289c0a270d8b4be500ab0ad9702ed2b29d77b1f9159f6bfd4ec2b3c9f2ec87)<br>Výstava souvisí s podcastem, který jsem taky sdílel. Byť byla za rohem od místa, kde bydlím, nevěděl jsem o ní a nestihl jsem ji. Tady jsem si aspoň mohl prohlédnout, jak to vypadalo a mohl jsem si proklikat související odkazy.
- [V jeskyni konspiračních teorií](https://getpocket.com/redirect?&url=https%3A%2F%2Fhoudekpetr.blogspot.com%2F2021%2F07%2Fv-jeskyni-konspiracnich-teorii.html&h=f02de1e191f8dbb630bf886b07bd528bbbfc9c36b83bb01a3042925a7cdd58d3)<br>„Tam, kde lidé ztrácí pocit moci něco ovlivnit, tím více obyvatelstvo věří konspiračním teoriím.“
- [Projeďte si novou linku D. Grafika ukazuje, kde vzniknou stanice metra bez řidiče](https://getpocket.com/redirect?&url=https%3A%2F%2Fzpravy.aktualne.cz%2Fekonomika%2Fdoprava%2Fgrafika-metro-d-mapa-plan%2Fr%7E627301965f4911e899570cc47ab5f122%2F&h=91569cc430a3bf1f3e8b775e73412d1d6b539ce9b033d2967d102827bef7fd74)<br>Fajn přehled. Zaujala mě dost mapa indexu změny zalidněnosti Prahy. Je vidět, že lidé jdou většinově „do polí“ kolem metropole a zlepšování městské infrastruktury půjde trochu mimo ně, protože budou do Prahy a zpět stejně jezdit autem. Metro tedy uleví především existující pozemní MHD, aut v Praze ale spíš neubyde. Řešení pro individuální přeshraniční dopravu do města a zpět z řídce osídlených a do krajiny rozházených satelitů zřejmě efektivně řešit ani nelze. Možná vlaky, ale ty taky nemohou jet do každé vesnice.
- [The forgotten history of how automakers invented the crime of "jaywalking"](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.vox.com%2F2015%2F1%2F15%2F7551873%2Fjaywalking-history&h=371350c0f306c15de11e352fb80850f2fd0d9926f2406f77de2c367c23756162)<br>Jak se automobilovému průmyslu podařilo přesvědčit lidi, že mají vyklidit veřejný prostor v ulicích a cesty přecházet pouze po přechodech. Nevzniklo to samo, šlo o lobby a PR.
- [Please, enough with the dead butterflies!](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.emilydamstra.com%2Fplease-enough-dead-butterflies%2F&h=f65106c797666de277ba5ae552492b3862de9ac77450e3fe562947adfe5cc1a1)<br>Když kreslíte motýla, kreslíte ho mrtvého, nebo živého? :)
- [Tenkrát na Žižkově. Unikátní staré fotografie pražské čtvrti, která slaví 140. výročí](https://getpocket.com/redirect?&url=https%3A%2F%2Fzpravy.aktualne.cz%2Fdomaci%2Ftenkrat-na-zizkove-unikatni-stare-fotografie-prazske-ctvrti%2Fr%7E75986ce4b3cd11ebb9860cc47ab5f122%2F&h=ed9e17b3bfdf63e698022e2e08699cd3038a15d7a68288b7f0c7368a6a389c1d)<br>Super foto série i s popisky

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
