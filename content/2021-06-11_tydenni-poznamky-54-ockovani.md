Title: Týdenní poznámky #54: Očkování
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: týdenní poznámky


Utekl další týden (7.6. — 11.6.) a tak [stejně jako minule]({filename}2021-06-04_tydenni-poznamky-53-jaro.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Finišování materiálů

Jak jsem psal, dělám spolu s Engetem na speciálních společných materiálech. V pondělí to má termín, takže jsem se tento týden snažil vše dokončovat a zabralo mi to většinu času.

Výsledek bude něco, co se bude nacházet jak na jejich webu, tak na mojem. Benefitovat z toho bude moci široká veřejnost, takže win win, dost se na to těším. A jsem zvědavý, jak to dopadne, jak to nakonec bude vypadat.


## Zpracování sponzorů

Už minulý týden jsem si udělal tabulku sponzorů a aktualizoval všechny dohody, které jsem uzavřel. Uprostřed tohoto týdne jsem si potřeboval odopočinout od veškeré administrativní práce a od psaní materiálů, tak jsem naprogramoval skript, který sponzorům přidělí v klubu sponzorskou roli. Taky se teď loga na stránce klubu vypisují z databáze, resp. z té Google Sheets tabulky, a nejsou natvrdo v HTML.


## Favicon: Přitom taková blbost!

U nabídek práce, kde chybí logo firmy, stahuji favicon aj. obrázky z webu firmy. Byl to před časem takový zběsilý nápad, ale ve výsledku to funguje až překvapivě dobře. Blbé je, že knihovna [favicon](https://github.com/scottwernervt/favicon) vrátí někdy spoustu ikonek a obrázků a [scrapy pipeline](https://docs.scrapy.org/en/latest/topics/media-pipeline.html), která loga pak zpracovává, je nebyla schopna nějak dobře seřadit a vybrat ten nejlepší, takže se občas na webu objevil jako logo firmy úplně nesmyslný obrázek. Třeba [tenhle](https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/red-hat-social-share.jpg) místo [tohoto](https://www.redhat.com/misc/favicon.ico).

Štvalo mě to už dlouho, ale byl to úkol, který byl zcela nepodstatný. Jenže tento týden jsem měl trochu deficit programování a zároveň se tato chyba projevila i u nově přidané nabídky práce, že už jsem se naštval a řekl jsem si, že to opravím.

Již dříve jsem se pokoušel to vyřešit, ale kvůli architektuře systému (splachovací databáze, separátní procesy scraperů, předpřipravená pipeline od Scrapy, do které nejde zas tak moc hrabat, kešování) všechna přímočará řešení selhala. Teď jsem si matně pamatoval, že jediné, co mě kdysi ještě napadlo, bylo uložit si původní rozměry obrázku do EXIFu po tom, co ho stáhnu a zmenším, a pak je číst později při vybírání vhodného obrázku. To mi nyní přišlo jako velký úlet, takže jsem strávil několik hodin tím, že jsem prošel všechna ta přimočará, ale nefunkční řešení, která jsem prošel už dřív, vždy skončil na hlasitém „aha, ale to takhle vlastně nepůjde!“ a nakonec se vrátil k tomu, že jsem to udělal opravdu přes ten EXIF :D

Celé je to [tady](https://github.com/honzajavorek/junior.guru/blob/master/juniorguru/scrapers/pipelines/company_logo.py). Použil jsem [Pillow](https://pypi.org/project/Pillow/) (ten už jsem tam měl) a [piexif](https://pypi.org/project/piexif/). Funkci na výběr nejvhodnějšího obrázku mám i hezky otestovanou. Dal jsem do kódu mohutný komentář, který vysvětluje, že EXIF je opravdu nejlepší volba a pokud si někdo v budoucnu bude myslet, že je to padlé na hlavu a existuje jednodušší řešení, tak ať si to nemyslí. Chvíli jsem zápasil s tím, do jakých metadat původní rozměry obrázku vložit, ale nakonec jsem vybral něco, co měl piexif rovnou v příkladech. Stejně je to fuk, ty obrázky se použijí jen na JG a tyto údaje slouží pouze pro tu scrapy pipelinu. V první řadě se vybírá takový obrázek, jehož původní rozměry byly co nejvíc čtveraté:

```python
similarity_to_square = abs(width - height)
```

Ale zároveň pokud je obrázek moc malý, tak to nehraje roli:

```python
if width < 100 or height < 100:
    similarity_to_square = 0
```

Z těchto obrázků se vybere ten, který má větší „rozlohu“.


## Smlouva nad rámec všeobecných obchodních podmínek

Komunikoval jsem s právničkou, abychom doladili ještě nějaké otázky ohledně mé dohody s jednou vzdělávací agenturou. Neodpovídala a nakonec jsem zjistil, že jí ani nefunguje web. Napsal jsem SMS a zjistili jsme, že jí vypršela doména, ale maily jí chodí, zapomněla mi odpověď akorát odeslat.

Mezitím jsem se snažil aspoň sám zjistit, co vlastně potřebuji. Přišel jsem na to, že asi něco jako „smlouvu s včleňovací doložkou“, ale nakonec je posudek právničky takový, že nemám dělat byrokrata, že úplně stačí nějaký obyč papír. To je poprvé, kdy mi právníci navrhují něco méně právnického, než navrhuji já sám :D Asi mě ten Oracle nakonec opravdu nějak poznamenal. No, teď mám už vše potřebné pro uzavření dohody, ale v pátek už jsem to nedokázal dotáhnout do konce.


## Smutný

_Jsem smutná_<br>
_Jsem veselá_<br>
_Většinou je to jedno_<br>

[Pusťte si!](https://www.youtube.com/watch?v=3MSXuX_p1v0)

Měl jsem trochu depku, že se nikam neposouvám a nic nestíhám. Přemýšlel jsem, jestli se moc neutápím v každodenní administrativě a komunikaci s lidma, uzavírání nových partnerství apod. Jestli toho není tak moc, že při tom nestíhám dělat už nic jiného. Nakonec jsem si vsugeroval, že dělám ty materiály pro Engeto a to mi bere hodně času (hlavně ta prokrastinace psaní, ta toho času žere fakt hodně!), i když to není zrovna teď nikde vidět, a že po pondělku bude už Engeto hotové. A že smlouvu s další agenturou nějak už doklepnu a uzavřu, a že pak bude čas konečně zas dělat na samotném webu JG a na příručce. Těším se na to.

Mám v hlavě dokonalou představu, jak by která část JG měla vypadat, jak chci přebudovat příručku, pracovní nabídky, jak bude vypadat nová úvodní stránka klubu, apod. Všechno to mám vymyšlené a myslím, že tak jak to chci, tak to dává perfektní smysl na dlouhé měsíce dopředu, nevěřím, že se to pak už bude nějak překotně měnit, spíš budu jen přidávat nový obsah. Teď už to jen celé teda překopat :D Bude to hodně práce, bude to chtít hodně času. Ale snad už s tím brzo teda začnu.

Budu muset začít stránkou klubu, aby ze zlepšila konverze lidí do klubu, protože teď ta stránka moc dobře neláká na vše, co člověk v klubu dostane. Je to úplně prapůvodní stránka z února, kdy bylo v klubu pět lidí a sám jsem netušil, kam se to vyvine. Teď vím, co mám a kde jsou největší benefity, které chci na té stránce vysvětlit a lidem „prodat“.

Potom nahodím nový ceník pro firmy, ale upřímně, už jsem dost uvažoval i nad tím, že bych ho tam napevno nalinkoval jako ten Google Dokument, který mám teď, protože ho budu moci doplňovat a ladit a nebude mě to stát žádné nervy s HTML a CSS.

No a potom asi přijde na řadu příručka, překopat, nový design, rozházet obsah do více stránek, přidat nový obsah, revidovat existující, atd.


## Další poznámky

- Zašel jsem si na očkování. Díky očkování jsem měl příležitost si uvědomit, že ačkoliv jsem oficiálně levák, všechno kromě psaní dělám pravou :D
- Zrovna minule jsem tu myslím psal, že jsem zkoumal knihovny, které umožňují extrahovat hlavní text na stránce. No a hned potom můj oblíbený Simon Willison [tweetuje dotaz v podobném smyslu](https://twitter.com/simonw/status/1401656327869394945). Ta [trafilatura](https://github.com/adbar/trafilatura) vypadá zajímavě.
- Spoustu času jsem strávil s lidmi v klubu, vítáním nových členů, tříděním pracovních nabídek, vyřizováním e-mailů a trochu i se sociálními sítěmi, ale ty jsem měl většinu týdne opět zablokované.
- Psal jsem si s jednou další firmou o tom, jak bychom mohli spolupracovat.
- Volal jsem si s [Nadání a dovednosti](https://www.nadaniadovednosti.cz/) a dohodli jsme se, že moje nabídka dává smysl a že to nějak doladíme a zkusíme uvést v praxi.
- Zmeškal jsem skrze kostrbatou komunikaci přes LinkedIn a e-maily o jeden den nějaké zasedání Federace dětských domovů, kde jsem teoreticky mohl prezentovat nabídku pro DD. Možná dobře, aspoň to lépe připravím do podzimu, kdy má být další. Prý lepší oslovit DD tam, osobně. Pokud nebude další vlna covidu.
- Volal jsem si s Mews a dohodli jsme se na dalším postupu. Ladíme podobu něčeho jako stipendia/fin aid balíčku, který bychom mohli dávat znevýhodněným lidem s potenciálem dostat se do IT. Bylo by v tom členství v klubu, ale třeba i nějaký kurz apod. Celkově mi to přijde jako strašně super nápad. To, že budu pomáhat znevýhodněným do IT, mám ve své vizi už dávno. Když jsem ale v začátcích JG psal na [donate stránku](https://junior.guru/donate/) „aby každý Luďan z Mostu měl po ruce návod, jak začít s programováním“, tak jsem sám tak úplně nevěřil tomu, že to dokážu dotáhnout až takhle daleko a oslovím s tím i někoho jiného, než lidi z Karlína s latéčkem v ruce. No a teď to vypadá, že asi fakt snad brzo budu reálně schopný pomoci i někomu třeba z dětského domova.
- Přišla nová nabídka práce na JG, tentokrát dokonce placená. Recruiter v jiné firmě byl zmatený z mé nabídky (což se mu vůbec nedivím), tak jsme si vyměnili telefony a teď si občas voláme. Mělo by z toho být hned několik placených nabídek práce.
- Investorka nevěřila, že vydělávám pořád jen 20 tisíc čistého. Tak jsem zkoušel v tabulkách hledat chybu, v jejímž důsledku by čísla byla špatně a mohl bych díky tomu zjistit, že ve skutečnosti vydělávám víc. Chybu jsem hledal hodinu, ale žádnou jsem nenašel :D
- Během 7 dní od 5.6. do 11.6. jsem při procházkách nachodil 6 km. Celkem jsem se hýbal 1 hodin a zdolal při tom 6 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Konečně uzavřít dohodu s jednou vzdělávací agenturou.
2. Začít dělat novou úvodní stránku pro klub.
3. Dokončit v pondělí to, co spolu podnikáme s Engetem.

**Bonusy:**

- Pověnovat se Python komunitě, uspořádat schůzi výboru, členskou schůzi, zajít na [první letošní Pyvo naživo](https://twitter.com/naPyvo/status/1403312699291938816).
- Pověnovat se [PyCon Namibia](https://na.pycon.org/), který je letos online, lístky [zde](https://na.pycon.org/tickets/).


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Komentář: Feri hlasy mladých nikdy nepřitáhl. Chtějí lepší život, ne baviče](https://www.seznamzpravy.cz/clanek/komentar-feri-hlasy-mladych-nikdy-nepritahl-chteji-lepsi-zivot-ne-bavice-156785?%24coQ1BIUW43NFBIUW43NEQzQUNCQ1NCY0NzQVBfQUFFUEFBSVRJRjh3TEFBQWdBS0FBZ0FCVUFDNEFHUUFPZ0FnQUJRQUNvQUZvQU1nQWFBQTVnQ0lBSW9BUndBa2dCTUFDZUFGVUFMY0FZUUJpQUQ5QUlBQWhBQkVBQ3hBR2FBT0lBZHdCQ0FDVEFFOUFLUUFYVUF3SUJwd0RXQUkxQVIwQWtFQk5vQzNBRjVnTDVBN3FBMEFCVUFDNEFHUUFRQUF5QUJvQURtQUlnQWlnQk1BQ2VBRlVBTVFBaEFCRUFDeEFHYUFPNEFoQUJGZ0M2Z0dCQU5ZQWtFQk5vQzh3SGRBQUFBQUEuWUFBQUFBQUFBQUFB=)<br>Kašpárek: „Nestačí přidat na billboardy ke zmateným vysloužilým strejcům dalšího excentrika s Instagramem. Kdo chce pozornost a hlasy mladých, musí je brát vážně.“
- [Blog: Proč jsem jí nevěřil zamčené dveře? Mozek skrývá realitu druhých](https://www.seznamzpravy.cz/clanek/blog-proc-jsem-ji-neveril-zamcene-dvere-mozek-skryva-realitu-druhych-156423)<br>O klamech, které máme zabudované přímo v mozku a kvůli kterým je těžší být k někomu empatický. „Realita ostatních je pro nás obtížně nahlédnutelná. Někdo má dveře zamčené a někdo odemčené. A ti, kteří odemčenými dveřmi prošli na první pokus, nevěří těm, kteří lomcovali zamčenými dveřmi. Vždyť stačilo vzít za kliku…“
- [Why workers are calling BS on leaders about returning to the office](https://www.fastcompany.com/90639348/why-workers-are-calling-bs-on-leaders-about-returning-to-the-office)<br>“Our leadership felt people weren’t as productive at home. While as a company we’ve hit most of our goals for the year. . . . Makes no sense.”
- [Employees Are Quitting Instead of Giving Up Working From Home](https://www.bloomberg.com/news/articles/2021-06-01/return-to-office-employees-are-quitting-instead-of-giving-up-work-from-home)<br>“If anything, the past year has proved that lots of work can be done from anywhere, sans lengthy commutes on crowded trains or highways. Some people have moved. Others have lingering worries about the virus and vaccine-hesitant colleagues.”
- [„Výpověď znásilněných není filmový scénář, logiku v ní nehledejme,“ píše Kamil Fila](https://www.heroine.cz/zena-a-svet/4944-vypoved-znasilnenych-neni-filmovy-scenar-logiku-v-ni-nehledejme-pise-kamil-fila)<br>„Největším objevem, který jsem musel vstřebat, abych pochopil jednání obětí sexuálně násilných činů, bylo to, že v naprosté většině případů nejen, že nejsou jasné, logické, systematické a konzistentní, ale že takové dokonce ani být nemohou.“
- [Why Russians do not smile](https://www.chicagomaroon.com/2002/04/12/why-russians-do-not-smile/)<br>Proč se Rusové neusmívají a proč Američani ano. Česko bych řadil spíš do té Ruské kategorie.
- [Pohnutý osud namibijských dětí: Vyrůstaly v ČSSR, milovaly Vánoce. A dodnes umí česky](https://zpravy.aktualne.cz/zahranici/pohnuty-osud-namibijskych-deti-miluji-pohadky-a-dodnes-umi-c/r~527886babed911ebb9860cc47ab5f122/)<br>Drsný příběh. V Namibii jsem byl vloni na PyCon NA, ale o tomto jsem vůbec nevěděl.
- [Pohnutý osud namibijských dětí: Vyrůstaly v ČSSR, milovaly Vánoce. A dodnes umí česky](https://zpravy.aktualne.cz/zahranici/pohnuty-osud-namibijskych-deti-miluji-pohadky-a-dodnes-umi-c/r~527886babed911ebb9860cc47ab5f122/?utm_term=Autofeed&utm_medium=Social&utm_source=Twitter#Echobox=1622430371)
- [Mourem zapadaný kraj i duše. Cestou do postuhelné éry čekají Karvinsko krušné časy](https://zpravy.aktualne.cz/ekonomika/chude-cesko-21-karvinsko-cekaji-krusne-casy/r~e5b298ecb70b11ebb98b0cc47ab5f122/)<br>Můj rodný region.
- [It’s time to ditch Chrome](https://www.wired.co.uk/article/google-chrome-browser-data)<br>Používáte Chrome? Já nikdy nezačal. “Chrome provides Google with enormous amounts of behavioural and demographic data, control over people’s browsing experience, a platform for shaping the web to Google’s own advantage, and brand capture.”
- [U všech pozic povinně i částečné úvazky. První velká firma sází na flexibilní práci](https://zpravy.aktualne.cz/ekonomika/vodafone-nabidne-u-vsech-pozic-castecny-uvazek-cesko-s-flexi/r~40c55cf6c47c11ebbc3f0cc47ab5f122/)<br>Hurá
- [Taková hezká holka, proč neukážete víc?](https://nazory.aktualne.cz/takova-hezka-holka-proc-neukazete-vic/r~fb246052c53e11eb966d0cc47ab5f122/)<br>Jak může vypadat váš každodenní život, pokud jste atraktivní žena v Česku. Tohle se fakt musí změnit.
- [‘Shrek’ at 20: How a Chaotic Project Became a Beloved Hit](https://www.nytimes.com/2021/05/18/movies/shrek-20th-anniversary.html?smtyp=cur)<br>Už 20 let, jo? Hustý.
- [Havlíčkův plán národního úpadku (Všichni tady umřeme #11)](https://www.youtube.com/watch?v=uVh1nWCJI7o)<br>Bilera rapujícího svá nihilistická videa sleduji pravidelně jako svou každotýdenní malou dávku sebepoškozování. Videa většinou nesdílím, ať to tady není samý Biler, nicméně tento díl je obzvláště „výživný“ a smutný.
- [Why mentoring matters — a Q&A with my own mentor, Ben 👨‍👧](https://tereza-machackova92.medium.com/why-mentoring-matters-a-q-a-with-my-own-mentor-ben-2fa30b1063d9)<br>Rozhovor o mentorování, s mentorem
- [Personal Notes on Being an Imposter](https://tereza-machackova92.medium.com/personal-notes-on-being-an-imposter-c424e8b7d884)<br>Skvělý článek na téma imposter syndromu s tipy, jak s tím bojovat. Taky tím trpím.
- [Tank Man](http://www.jeffwidener.com/stories/2016/09/tankman/)<br>Dramatický příběh toho, jak vznikla fotka „tank man“, přímo od fotografa, který ji pořídil. Krásně napsané, četl jsem se zatajeným dechem.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
