Title: Týdenní poznámky #58: Po týdnu volna
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (12.7. — 16.7.) a tak [stejně jako minule]({filename}/2021-07-02_tydenni-poznamky-57-ponoren-v-css.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Relax

Vzal jsem si týden volna. Bylo to v týdnu s dvěma státními svátky, kdy si vzal volno každý, takže po mě mezitím ani nikdo nic moc nechtěl. Z rodinných důvodů jsem nemohl nikam odjet, tak jsem si užil týden ve vylidněné Praze, což taky mělo svoje kouzlo. Lituju ty, kdo jeli do lesa a potkali tam všechny ostatní. My jsme si s kamarádem vzali [BeRidery](https://www.be-rider.com/) a zkoušeli na tom jezdit po ulicích bez provozu, bylo to fajn. Taky jsem se pak projel na kole, šli jsme se rozplácnout do parku, nebo jsme objevili hru [0 A.D.](https://play0ad.com/) a zkoušeli ji trochu pařit.

Ze začátku týdne jsem ještě četl každou zprávu v klubu, ale od poloviny jsem už na práci nemyslel a hezky se mi vyčistila hlava. Na konci dovolené jsem si šel zaběhat a během 10 km jsem na práci nepomyslel ani jednou, což je běžně zcela nemožné.

Narazil jsem na články Petera Debnára a hned jsem jich několik sjel. Moje nejoblíbenější jsou zatím o parkování a ten o sídelní kaši (_urban sprawl_) s názvem Hybaj do polí. Odkazy jsou tradičně na konci poznámek. Má i podcast, zatím jsem slyšel jen [jeden díl o tom parkování](https://open.spotify.com/episode/7N04bNOeZGYve0Q5lax5v7?dl_branch=1) a rozhodně je to zajímavé, ale forma je „rapuju svoje názory do ticha“, což může být zábavné u [Standy s Marunou](https://www.youtube.com/watch?v=vl_Gptbo904&list=PLOBZS7cBuNIl5P4l7KEyHG6WHa_d0ZWBr), ale tady to po mě vyžadovalo dlouhou soustředěnost a přijde mi, že text na taková témata prostě funguje líp.


## Po týdnu volna

- Prošel jsem 50 mailů (= zhruba půlka jednoho pracovního dne).
- Prošel jsem všechny zprávy v klubu za poslední týden a odpověděl tam, kde to dávalo smysl (= zhruba jeden celý pracovní den).
- Poslal jsem maily firmám, se kterými komunikuji, že můžeme komunikovat dál.
- Poslal jsem volňásky na WebExpo lidem, kteří je vyhráli (někdo se mi neozýval v klubu, ale na mail už jo).
- Prošel jsem všechny upgrady dependencies z Dependabota na několika repozitářích a vše pomergoval.
- Prošel jsem notifikace z [Frozen-Flask](https://github.com/Frozen-Flask/Frozen-Flask/).

Hned v pondělí byl taky termín na dokončení připomínek k materiálům, které vytváříme s Engetem, takže jsem to hned takhle po dovolené celé prošel a do večera se to snažil dokončit, ať je to připraveno včas. Na výsledek se dost těším :)


## Úklid

Když jsem dodělal úvodní úklid po dovolené, nechtělo se mi hned ponořit do CSS a pokračovat ve tvorbě nové stránky klubu, což je teď priorita. Navíc jsem měl kvůli návštěvám a jiným věcem v životě půlden sem, půlden tam, tak jsem to nakonec využil na drobný úklid v kódu:

### Dlouhý build

Zjistil jsem, že build JG se vším všudy zabere už víc jak 20 minut a zdálo se mi, že v některých případech mi ho CircleCI i zabije, protože překročí jejich časový limit. Dopsal jsem si tedy [dekorátor na měření délky](https://github.com/honzajavorek/junior.guru/blob/a53af0388f33fba8f07027e671b3f180b86f4327/juniorguru/lib/timer.py#L32) a dal ho k jednotlivým skriptům, které se spouští během synchronizace a stahování dat, abych věděl, které trvají dlouho a má smysl je optimalizovat. Akutní problém to není, takže pokračovat v optimalizacích budu zase někdy jindy, ale aspoň budu mít v logu data.

```
[timer] INFO: proxies() took 0.4min
[timer] INFO: club_content() took 1.9min
[timer] INFO: pins() took 0.6min
[timer] INFO: avatars() took 0.7min
[timer] INFO: returning_members() took 0.5min
[timer] INFO: jobs() took 1.0min
[timer] INFO: sync() took 6.2min
```

Smazal jsem položky, kde bylo 0.1 nebo 0.0 minut. Očekávatelně, nejvíc času zabere stahování a zpracovávání pracovních nabídek. Položka `sync()` je za celou synchronizaci a má jen 6 minut, ne 20, takže to je taky zajímavé a budu to do budoucna sledovat.

### Dependabot

Dependabot začal na JG repozitáři blbnout a začal mi v nekonečné smyčce na repu zakládat [issue o tom, že nedokáže nainstalovat moje závislosti](https://github.com/honzajavorek/junior.guru/issues?q=Dependabot+can%27t+resolve) (což jsem nedokázal reprodukovat u sebe ani na CircleCI). Napsal jsem na support GitHubu a řekli mi, ať upgraduju na novou verzi. Tento upgrade jsem prokrastinoval, protože jsem chtěl řešení pro auto-merge, který nový Dependabot už nemá. Tato věc se mezitím posunula a [řešení existuje](https://github.com/dependabot/dependabot-core/issues/2268#issuecomment-877272539), ale není triviální a mě se s tím nechtělo teď hrát, takže jsem se na to vykašlal a prostě jsem upgradoval bez auto-merge a budu na ty PR muset holt dokola klikat jak blbeček, dokud si nezařídím vlastní automatizaci. PR, který Dependabot vygeneroval pro migraci na novou verzi, obsahoval část, která ignoruje určité knihovny. To bylo matoucí, tak jsem zjišťoval, proč to tam je. Důvod jsem [našel](https://github.com/dependabot/dependabot-core/issues/3589#issuecomment-829081718) a napsal jsem jej i [pod Pyvec repo](https://github.com/pyvec/docs.pyvec.org/pull/211#issuecomment-879969912), kde jsme se už dřív nad stejnou věcí podivovali. Migrace na nový Dependabot byla nakonec jednoduchá a chyby s instalacemi závislostí tím ustaly.

### main místo master

Když už jsem se hrabal v repozitáři, přejmenoval jsem hlavní větev z `master` na `main`. Na GitHubu je teď výchozí `main`, což mám tedy na nových projektech, ale potom se pletu, takže lepší, když bude `main` všude. Tím jsem pár věcí rozbil, například deployment na Vercel, ale nakonec OK.

### Poetry místo Pipenv

Dále jsem se rozhodl přejít z pipenv na poetry, které je mi už nějaký ten čas sympatičtější. Už před časem jsem zmigroval `[scripts]` z `Pipfile` do `Makefile`, takže teď už nic nebránilo přechodu - kromě toho, že je to samozřejmě nejzbytečnější věc, kterou bych se měl v této fázi projektu zabývat, ale tak když už jsem měl takové odpoledne na přehazování kódu a konfiguráků vidlema z hromádky na hromádku, řekl jsem si proč ne. Zahlédl jsem nástroj [pipenv-poetry-migrate](https://pypi.org/project/pipenv-poetry-migrate/), tak jsem ho zkusil použít. Některé věci to zmigrovalo, některé ne, např. `allow-prereleases = true`. Učil jsem se, jak říct Poetry, který Python má použít. Blbnulo mi [gql](https://pypi.org/project/gql/), asi právě kvůli nastavení prereleases, které se z Pipfile nepřeneslo úplně dobře. Nakonec jsem po delším debugování zjistil, že původní nastavení, že má pipenv brát prereleases, pipenv zjevně nerespektoval a instaloval `gql==2`, ne `gql==3.0.0a6`. Takže když jsem v poetry nastavil prereleases a ono to začalo respektovat a instalovat `gql==3.0.0a6`, nefungovalo mi to :) Takže nakonec stačilo všechno kolem prereleases odebrat.

### GitHub Pages místo Vercel

Rozhodl jsem se pomaličku začít pracovat na tom, že vyhodím [Vercel](https://vercel.com/). Na ten nasazuji stránky JG přes strašlivý hack od dob, co změnili svoje CLI a přestali umožňovat integraci s CI tím způsobem, že deploy se provede nad složkou se soubory přímo z CI mašiny. Teď preferují, aby se vše buildilo u nich, jenže zatímco CI mašinu si nastavím celou sám (instalace fontů, browserů…), nad Vercel mašinou nemám kontrolu a musel jsem vše hackovat do nějakého Bash skriptu a ladit pokus omyl. Takže jsem to pak vzdal a funguje mi to teď tak, že na Vercelu mašina jen čeká, až skončí CircleCI, a poté si stáhne zazipovaný artefakt se soubory a ten rozbalí a prohlásí to za vysledek buildu :D No a vzhledem k tomu, že žádné další výhody Vercelu už ani neocením, už ani ty feature branches prakticky nedělám, že bych potřeboval náhledy na rozpracovaný PR, tak jsem se rozhodl Vercel vyhodit a přejít na GitHub Pages, stejně jako jsem to už dřív udělal tady s tím blogem.

Protože mám na Vercel navázaná i DNS a spoustu dalších věcí, rozhodl jsem se začít jemně a nejdřív vyřešit deployment z CircleCI na GitHub Pages a až potom dělat migraci. Už tento samotný duplicitní deployment na GHP byl plný spousty zjišťování a ladění:

- Zjistil jsem, že existuje [CircleCI Orb přímo na GitHub Pages](https://circleci.com/developer/orbs/orb/sugarshin/gh-pages). Super :)
- Ten ale potřebuje nějaký certifikát, kterým se provádí push na GitHub. Certifikát, který už jsem na CircleCI měl, byl jen pro čtení.
- Trvalo mi to, ale nakonec jsem našel dokumentaci k těmto věcem:
    - [Creating a GitHub deploy key](https://circleci.com/docs/2.0/gh-bb-integration/#creating-a-github-deploy-key)
    - [Adding an SSH Key to CircleCI](https://circleci.com/docs/2.0/add-ssh-key/)
- Pak už to skoro fungovalo, akorát že to zkyslo na tom, že mašina neznala github.com a interaktivně se ptala, jestli této doméně má věřit nebo ne. To jsem taky musel hledat jak se řeší a [nakonec teda řešení našel](https://github.com/cypress-io/circleci-orb/issues/101#issuecomment-861911201).
- Až po tomhle všem jsem našel [oficiální návod](https://circleci.com/blog/deploying-documentation-to-github-pages-with-continuous-integration/) :D
- Pak jsem zjistil, že když to pushne do větve `gh-pages`, tak CircleCI řve, že tam není konfigurák na CI a neví, co má spustit. Prý se to řeší přes `[skip ci]` v commit message, ale to mi přišlo, že tam ten CircleCI Orb přímo dává, tak o co jde? No trvalo mi to pěknou chvíli, než jsem si všiml, že tam dává `[ci skip]`, ale já asi potřebuju `[skip ci]`. Ehm.
- Chtěl jsem tedy nastavit vlastní commit message, ale nedařilo se mi to, házelo to nějaké Bash chyby. Nevymyslel jsem způsob, jak vlastní commit message zadat, tak jsem šel [číst kód toho Orbu](https://github.com/sugarshin/circleci-orbs/blob/3e28970d428fdead80ee3648ab8554f2b42b6e15/src/gh-pages/commands/deploy.yml#L99) a z toho jsem to nakonec vydedukoval.

Nakonec úspěch, stránky se mi kromě Vercelu [hážou i na GitHub Pages](https://honzajavorek.github.io/junior.guru/club2/), pokračovat v tomto úsilí budu zas jindy. Už se těším, až potom smažu z repozitáře hromadu kódu s těmi hacky kolem Vercelu.

## Tvorba nové stránky pro klub

Závěr týdne jsem bušil CSS na novou stránku pro klub. Pracoval jsem na komponentách pro ceník, důvody proč platit, citace toxických komentářů z jiných, veřejných skupin, tabulku porovnání výhod, ikonky benefitů klubu, loga firem a komunit, obrázky členů klubu…

Taky mi přišlo, že mám strašný binec ve whitespace kolem různých věcí, tak jsem vše předělal tak, aby komponenty neměly žádný margin okolo, kromě maličkého marginu dole, který kdyžtak později zvětším přes nějakou přídavnou třídu. Toto by mělo navazovat na to, jak je to i přímo v Bootstrapu.

Pak jsem se chvíli [díval na svůj výtvor](https://junior.guru/club2/) a byl smutný z toho, že se s tím tak mažu a pořád to vypadá, jako bych ty věci k sobě stloukl kamenem, přitom normální podnikatel vezme první WordPress šablonu a má za 5 minut něco, co vypadá 700x lépe. Ale řekl jsem si, že aspoň ten web nevypadá jako všechny ostatní weby a bude trochu osobitý. Navíc budu schopen jej sám udržovat, doplňovat věci a nové komponenty, a tak. Věřím, že to k nějaké rozumné kráse a funkčnosti dotáhnu, i když to nebude ta největší trendy bomba. Aspoň to bude uvěřitelné a autentické!

![Wish]({static}/images/wish.png)

## Další poznámky

- Vyšel se mnou [rozhovor na .NET.CZ Podcastu!](https://twitter.com/dotnetcezet/status/1414499848250875904)
- Volal jsem si s Mews, abychom posunuli naši iniciativu v tom, abychom podpořili znevýhodněné lidí v jejich vstupu do IT. [Jan Meissner](https://www.linkedin.com/in/jan-meissner/), s nímž to řeším, dostal fajn nápad sepsat si všechno do jednoho dokumentu, což nám dalo celkový přehled toho, co máme, co je potřeba ještě udělat a co jsou konkrétní další kroky. Call byl díky tomu velmi produktivní a měl jsem z něj velkou radost.
- Pokusil jsem se naplánovat schůzi Pyvce, kterou jsme minule nějak zapomněli naplánovat.
- Opravil jsem odkaz v poznámkách ke stanovám Pyvce.
- Autor „Automate the Boring Stuff with Python“ [vydal knížku](https://twitter.com/AlSweigart/status/1415030015129919491), „The Big Book of Small Python Projects“.
- Zaujal mně [seznam zajímavých lidí z oboru](https://twitter.com/danluu/status/724570756831567872), které se vyplatí sledovat a číst, od Dana Luu.
- Během 15 dní od 3.7. do 17.7. jsem naběhal 10 km, při procházkách nachodil 5 km, ujel na kole 102 km. Celkem jsem se hýbal 15 hodin a zdolal při tom 117 kilometrů.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Bušit dál CSS na té klubové stránce.
2. Dodělat CSS pro plakátky na přednášky v klubu.
3. Oznámit příští přednášku v klubu, která by měla být 27.7.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [K násilí na ženách v politice dochází i v Česku. Jeho cílem je političky zastrašit a vytlačit](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F06%2Fk-nasili-na-zenach-v-politice-dochazi-i-v-cesku-jeho-cilem-je-politicky-zastrasit-a-vytlacit%2F&h=73b3f9be57c752b1bea26359d8edc8444af7f04febff143d5ad72c421ca928ca)<br>Tolik k tomu, zda mají ženy v politice stejné podmínky, jako muži.
- [Esej Kateřiny Smejkalové: Různé světy české společnosti](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.novinky.cz%2Fkultura%2Fsalon%2Fclanek%2Fesej-kateriny-smejkalove-ruzne-svety-ceske-spolecnosti-40364443&h=172ac3603c472ddc6af4c7df5700265e4d7eb38e9ce3179ed1029dd38131822e)<br>Klenot! Studie Jedna společnost – různé světy. Přečtěte si, proč lidé volí SPD, na čem se dva hlavní názorové tábory neshodnou a na čem se naopak shodnou, proč může být kritické myšlení elitářským chucpe, proč tu nejsme jako v Německu. Děsivé zrcadlo, ale asi nám nezbývá, než do něj pohlédnout a říct si sestimsmiř. Toto se jen tak nezmění a proto tady ještě dlouho nebudeme moci mít hezké věci.
- [YAGNI exceptions](https://getpocket.com/redirect?&url=https%3A%2F%2Flukeplant.me.uk%2Fblog%2Fposts%2Fyagni-exceptions%2F&h=80e71f42ecbc4e979d82e35214ac9d250b6e5477f10f3be78760b429f6162cae)<br>YAGNI se stále učím, ale myslím, že za poslední rok už jsem se vycvičil celkem slušně a tenhle přístup zbožňuju. Je fajn vědět, kdy je dobré přece jenom plánovat trochu dopředu. Některé z bodů jsem zažil i v praxi.
- [Začínáte v IT? Zkuste open source!](https://getpocket.com/redirect?&url=https%3A%2F%2Fblog.cesko.digital%2F2021%2F06%2Fzkuste-open-source&h=7f1c3dacc25491ef654c933e2994d11bf01437733b170c3df9ef1781fca95396)<br>Praktický návod a inspirace jak začít s open source i jako junior.
- [Weimar Republic](https://getpocket.com/redirect?&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWeimar_Republic%3Fwprov%3Dsfti1&h=9345d2145b10ef99378a9d0cade1983da17c6577d2ba9fcbae13f93a0698d4c9)<br>Trochu slepá skvrna v mém historickém vzdělání, tak jsem to celé přečetl. Dynamický příběh o polarizované společnosti (místy děsivě aktuální, ale jakoukoliv historickou analogii si rozhodně nedovolím) a zákonu akce a reakce, který smetl všechny zúčastněné. Dějiny v Německu mezi první a druhou světovou válkou jakoby jely po tobogánu.
- [Vítejte v Developerově. Vzor levného bydlení leží hnedka za zatáčkou](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fspolecnost%2F425095-vitejte-v-developerove-vzor-levneho-bydleni-lezi-hnedka-za-zatackou&h=58b94d0ed12ccb6ea3b3d949d78b3b7c2975124a17d972ef1fac044d844ee908)<br>Zajímavý pohled na to, kde máme ve stavební politice mezery a co všechno dělají ve Vídni jinak. Přijde mi, že z A2larmu jsem měl jen polovinu toho příběhu, ale abych byl spravedlivý, rozhodně jsem nečetl a neslyšel vše, co tam v poslední době k bydlení vyšlo. Škoda, že na rozdíl od Vídně Praha své zajímavé pozemky už nemá v majetku a tudíž ani pod kontrolou.
- [Mužský a ženský mozek neexistuje, tvrdí vědci. Rozdíly v chování jsou výsledkem kulturního vývoje](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.lidovky.cz%2Forientace%2Fveda%2Fmuzsky-a-zensky-mozek-neexistuje-tvrdi-neurovedci-rozdily-v-chovani-jsou-vysledkem-kulturnich-stereo.A210514_140805_ln_veda_livs&h=abc489f14ff5c65050dda29513cfe44188ab5b1e9116427109354ba7e728e274)<br>Rozdíly v chování mužů a žen jsou naučené. Mozek mají stejný, liší se jen to, co do něj společnost „napíše“.
- [npm audit: Broken by Design](https://getpocket.com/redirect?&url=https%3A%2F%2Foverreacted.io%2Fnpm-audit-broken-by-design%2F&h=2f104284a74b73de59167a057d95eb64d1ed0c9aa95aff335b224dbe79dcf321)<br>Dan Abramov poukazuje na nedostatky v npm audit. Že bychom se opět dostali o kousek blíž k tomu, aby bezpečnost závislostí byla o něco méně padlá na hlavu?
- [„Zbavme se těch štěnic.“ Návrhu ODS na kriminalizaci chudých nejvíc tleskají komunisté](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F01%2Fzbavme-se-tech-stenic-navrhu-ods-na-kriminalizaci-chudych-nejvic-tleskaji-komuniste%2F&h=ca07d9fa2e3528b24c1bb76ac65b1ad3f663dad7bd68b954416abd2f70f64f3a)<br>Tohle je maso. Zákon, který chce z chudáků udělat ještě větší chudáky, se líbí všem od komunistů a nácků až po ANO a ODS. Proč to teď má být vůbec priorita? Zneužití nejnižších pudů, asociální politika hrozeb a zákazů, předzvěst toho, jak bude vypadat politika příští vlády. Pirátům se to nelíbí, ale jak říkal Biler, ať budou hrát v příští vládě jakoukoliv roli, se svými snahami budou sami a prosadí prd.
- [Stavební normy. Silnice do horoucího pekla asfaltované dobrými úmysly](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fveda-a-technika%2F420143-stavebni-normy-silnice-do-horouciho-pekla-asfaltovane-dobrymi-umysly&h=d12843e485899112b7c74486b4f1e46e93f8d1e60fec86c82843bfbfc5fc0ca9)<br>„Developeři ovšem nemají konkrétní ideologii, pragmaticky staví přesně to, co s minimálním odporem vyhoví legislativě. Forma všeho je předepsaná množstvím regulací, které jsou dobře míněné, ale z architektů dělají pouhé administrátory skládání technologických komponentů do formy, která je předem daná. Vytvořila ji jedna z nejpřísnějších norem na počet parkovacích stání v Evropě, tlak na nejmenší počet výtahů pro co největší počet bytů a ohled, jestli na třetinu plochy svítí 1. března 90 minut přímé slunce.“
- [Mnohem lepší parkování](https://getpocket.com/redirect?&url=https%3A%2F%2Fopen.spotify.com%2Fepisode%2F7N04bNOeZGYve0Q5lax5v7%3Fsi%3DS_4nhMOEQySoOxX7mSFK4g%26dl_branch%3D1&h=9bc6555524600dbde90b431cefb9d09d547f44953bf3be5c6d750190b72211a4)<br>Nový podcast Lepší města, první díl o parkování. Boží. Peter Bednár nakládá.
- [Hybaj do polí](https://getpocket.com/redirect?&url=https%3A%2F%2Ffinmag.penize.cz%2Fpenize%2F419465-hybaj-do-poli&h=d13e6e28e02d4af784d09724dab995508cf7d854a94637522e9d6187b5538fcc)<br>Debnár o fenoménu sídelní kaše. Takové to, co podvědomně možná vnímáte, ale nevíte, co je na tom vlastně špatně a jak to vzniklo. „Zajímavé je dnes už nepostavitelné umístění v krajině, většinou s domy těsně u sebe. Vesnickou malebnost vytváří koncentrace budov a lidí, kteří následně uživí třeba místní hospodu.“ „Velké vzdálenosti vynucují pro důstojný život rodin alespoň dvě auta.“ „Rodinný dům bývá na pozemku nejčastěji zhruba uprostřed, kde spolehlivě znehodnotí všechny potenciální kvality domu i zahrady.“ „Skokové, ale představitelné zdražení benzinu třeba na dvojnásobek by bylo likvidační i pro život těch, kteří se teď v okolí velkých měst právem považují za střední třídu.“
- [Život v satelitu po letech](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.novinky.cz%2Fzena%2Fstyl%2Fclanek%2Fzivot-v-satelitu-po-letech-40364977&h=c75ee6b5d3dfaf95e5d9af0a810ee64794a16948178e1a2874eb712f4818561a)<br>A hned potom, co sdílím Debnárovu sídelní kaši, sdílím konkrétní příklad, který mi někdo poslal.
- [Proč je noční vlak v roce 2021 pro mnohé nejlepší volbou?](https://getpocket.com/redirect?&url=https%3A%2F%2Fcestavlakem.cz%2Fnocni-vlak-2021%2F&h=cb80d9f1127b8e6ff198f859a3291be4912d34880562236a3b4f1eca53b7988a)<br>Na příští dovolenou vlakem?
- [Finland Had a Patent-Free COVID-19 Vaccine Nine Months Ago — But Still Went With Big Pharma](https://getpocket.com/redirect?&url=https%3A%2F%2Fjacobinmag.com%2F2021%2F02%2Ffinland-vaccine-covid-patent-ip%2F&h=ea98988c63869f1da68d6fc82c382949badd2ffbed4e9f77bc5526be23ad8eec)<br>Článek z Jacobinu, takže plný Big Pharma a zlého kapitalismu, ale sdílím, protože mě zaujala realita toho, že i když chce někdo udělat vakcínu jako „open source“, na rozdíl od SW to nemůže jen hodit na GitHub, potřebuje financování na testy. A tam to drhne, protože stát je nedá (byť Big Pharma vesele dotuje) a ostatní chtějí profit. Přidejte k tomu „jerk move“ západních zemí s tím, že na patenty se ani v pandemii sahat nebude a je to - ostatní země se trpí bez vakcín, vir mutuje, lidi umírají…
- [Scaling Normcore way down](https://getpocket.com/redirect?&url=https%3A%2F%2Fvicki.substack.com%2Fp%2Fscaling-normcore-way-down&h=79235fcf24d68aebb8b32468e49a69e4a1c97b9502bb2b2b09b086eb3a6c4d5a)<br>Vicki Boykis si dává do odvolání pauzu od psaní. Příležitost upozornit na její newsletter/blog a doporučit ke čtení všem, kteří by snad na její „normcore tech“ články zatím nenarazili (několik odkazů je i přímo v tomto rozloučení).
- [Corgi v cargu](https://getpocket.com/redirect?&url=http%3A%2F%2Ftkalci.cz%2F2021%2Fzapisy%2Fcorgi-v-cargu.html&h=11f335ad57c7f49b1ead2b682baa8c74429002e16097cb7f792b6c6c812bcc48)<br>Nejvtipnější recenze na nákladní kolo, jakou jsem kdy četl :)

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
