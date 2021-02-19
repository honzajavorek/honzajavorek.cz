Title: Týdenní poznámky #38: Klub začíná vydělávat
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (15.2. — 19.2.) a tak [stejně jako minule]({filename}/2021-02-12_tydenni-poznamky-37-prvni-klubovy-sraz.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub podporovatelů](https://junior.guru/club/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Psaním poznámek jsem v poslední době trávil stále větší část pátku. Došlo to tak daleko, že musela zasáhnout investorka a jemně mi naznačit, že produkuji dlouhé texty, které nemůže nikdo zvládat číst, a že mi už psaní zabírá půl pracovního dne. Rád bych se tedy dneškem začal učit poznámky zestručňovat a zkracovat.

_Poznámka: Dnes nakonec trvalo napsání a vypublikování jen hodinu! Juch!_


## Klub začíná vydělávat

Členové [klubu](https://junior.guru/club/) mají přístup 14 dní zdarma, na vyzkoušení. Tento týden tato doba uplynula u prvních členů a tak se na účtě objevily první peníze. V tento okamžik jsem na téměř 3000 Kč MRR (_monthly recurring revenue_), ale v tomto číslu nejsou započítány žádné příjmy od firem, které jdou bokem přes faktury, je to pouze číslo z Memberful.

S Memberful jsem také řešil první problém. O víkendu jsem zjistil, že někteří lidé dostávají e-maily se zprávou, která nedává v kontextu jejich účtu smysl. Napsal jsem jim na support, ale jsou z USA, takže jsem věděl, že odpoví nejdříve v pondělí večer. Mezitím jsem každý den postižené členy osobně obepisoval a omlouval se jim. V pondělí večer jsem zjistil, co je za problém: Memberful počítá _free trial_ jako samostatné předplatné, takže pokud si někdo vypnul automatické prodlužování předplatného ještě předtím, než skončil jeho _trial_, tak by se nepřehouplo do plného předplatného vyžadujícího kartu, ale prostě by skončilo. Tomu odpovídaly i rozesílané e-maily. Já jsem navíc měl u ročního předplatného jako výchozí možnost nastaveno neprodlužování, takže to postihlo všechny, kdo měli roční předplatné.

Memberful má skvělý support a vše jsme si nějak vysvětlili. Stále si myslím, že je to bug nebo možná spíš nesmysl či neošetřený _corner case_ na jejich straně, ale shodli jsme se, že stačí pár změn na mé straně a není co řešit. Moje roční předplatné se bude odteď automaticky prodlužovat, ale před tím, než se to stane, se pošle e-mail, který na to upozorňuje. I kdyby přesto někdo protestoval, že se strhlo další předplatné, mohu mu vrátit peníze jedním tlačítkem. Co se týče prvních 14 dní, tam už vůbec nehrozí nikomu nic, protože karta se do systému zadává až ve chvíli, kdy _trial_ vyprší a člověk jde fakt platit.


## První ohlasy

Začínám sbírat i první ohlasy na klub. Zatím je nemám nikde na webu. tak jen takto:

- _Mně přijde, že je celkově dost problém najít komunitu, která je fakt o nějaký vzájemný pomoci a výměně informací, než o honění ega.. Dost často se právě setkávám s tím, že se někdo na něco zeptá a dostane akorát výsměch, nebo odpověď "Google", případně třeba odpověď k tématu, ale s takovou zvláštní příměsí nadřazenosti.. Nevím no. Proto mám třeba i radši víc ženský skupiny. Tam mi přijde, že to tolik nevídám. Ale tady je to třeba krásná výjimka. Jsem fakt ráda, že toho můžu být součástí._
- _Co mě vždy jako kluka z vesnice na programování nejvíce štvalo, bylo to, že jsem na to byl vždycky hrozně moc sám. Proto jsem opravdu vděčný za tuto komunitu, jednak Honzovi, ale i vám ostatním, co tu jste._
- _Dneska jsem si potvrdila, ze nacpat se sem do klubu je moc dobrej napad. Krome toho, ze podporim Honzu a celej tenhle projekt, coz jsem stejne mela v planu, je to pro me i pri soucasnem vicemene "pasivnim" pouzivani takova ta jemne popostrkujici a nejakou cinnost vyvolavajici a podnecujici sila, kterou jsem potrebovala._
- _Ahoj, tak jsem dostal ten job! Ty na tom máš obrovský podíl! Musím ti za to ohromně poděkovat!_


## Přepracovávání webu

Minulé poznámky byly z velké části o tom, jak uvažuji o přepracování webu. Přes víkend jsem se ale umoudřil, obrazně se profackoval a zakázal si cokoliv z toho dělat. Utopil bych v tom moře času a JG prostě ještě není v situaci, kdy si může nějaké velké přepisování dovolit. Šel bych proti všem poučkám SW inženýrství - nedělej radikálni _redesign_, nedělej _rewrite_, nerezignuj na _continuous delivery_… Navíc, jaká je odpověď na otázku "co teď potřebuju nejvíc"? Odpověď je "co nejvíc spokojených členů [klubu](https://junior.guru/club/)." Jaká k tomu vede nejkratší cesta? Rozhodně ne přes nějaké přepisování webu. Rozhodl jsem se preferovat chirurgické zásahy, které udělají 80 % parády s 20 % úsilí:

- Změnil jsem strukturu menu tak, aby odrážela budoucí strukturu webu. Nezměnil jsem při tom jediné URL, vše se odehrálo pouze v menu. Nyní jsou všechny obsahové stránky pohromadě pod odkazem "příručka", pak je odkaz "práce" s nabídkami a ceníkem pro firmy, pak je "klub". [Příručka o hledání první práce v IT](https://junior.guru/candidate-handbook/) je teď třetí krok, ten původně mířil na nabídky práce.
- Až po několika dnech jsem si všiml, že změna výše kompletně rozbila menu na mobilech. Opravil jsem dnes.
- Na homepage je nyní místo "průvodce programováním pro začátečníky" slogan "klub pro začátečníky v programování" a i na jiných místech jsem začal o JG mluvit jako o klubu místo o průvodci.
- Ze všech stránek kromě obsahových (příručkových) jsem odstranil [výzvu k dobrovolným příspěvkům](https://junior.guru/donate/). Až začně klub vydělávat víc, odstraním ji zcela, ale zatím na to nemám kuráž.
- Dnes jsem se pokusil upravit hlavní menu i graficky. Není to výkvět designu, ale cílem bylo, aby tlačítka vypadala spíše jako odkazy a klub vypadal jako tlačítko, které chytá za oči. To by mohlo dále zvýšit počty příchozích na stránku s klubem.

V pátek jsem si přece jenom ale zkusil ještě něco zjistit o MkDocs, četl jsem si [o pluginech](https://www.mkdocs.org/user-guide/plugins/) a procházel [jejich nekonečný seznam](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins). Vypadá to, že abych udělal to, co potřebuji, nebudu muset ani nic moc programovat. Stačilo by použít [mkdocs-jinja2](https://github.com/andyoakley/mkdocs-jinja2) nebo [mkdocs_macros_plugin](https://github.com/fralau/mkdocs_macros_plugin). U toho prvního si nejsem jistý, jak moc je to aktivní, tak jsem tam cvičně poslal Pull Request a založil issue :D Na JG jsem si udělal větev, ve které jsem experimentálně rozjel MkDocs a sloučil se zbytkem webu tak, abych případně mohl novou verzi příručky vytvářet jako _continuous deployment_ aspoň někde za lomítkem (třeba junior.guru/handbook/).


## Další poznámky

- Pročetl jsem si v klubu všechny příspěvky, kterými se nově příchozí představili. V souvislosti s tím mě napadla celá řada témat, které bych chtěl s lidmi v klubu probrat. Pár jsem jich už sem tam vytáhl.
- Připadal jsem si [takhle](https://twitter.com/dzello/status/1361422560617922560).
- Členka klubu [Martina Hytychová](https://martinahytychova.github.io/) napsala článek o tom, jak v [Česko.Digital](https://cesko.digital/) začala dobrovolničením sbírat praxi jako junior programátorka. Boží! Pracuji na tom, aby to mohlo vyjít na blogu Česko.Digital, případně jinde.
- Petr Viktorin [rozjíždí online kurz Pythonu pro začátečníky](https://www.youtube.com/watch?v=so10Ud-YlKE). Propagoval jsem kurz na několika místech.
- Na JG se objevilo pár nových nabídek práce, takže jsem se postaral o jejich uveřejnění na [stránce s inzeráty](https://junior.guru/jobs/) a fakturoval jsem.
- Koukal jsem se na [MyST](https://twitter.com/simonw/status/1272744281531285504?s=21), hybrid Markdownu a reStructuredText.
- Poslouchal jsem [jedno rádio na Islandu](http://radio.garden/visit/selfoss/Do0QYeu3) a [jedno v Zimbabwe](http://radio.garden/listen/nehanda-radio/4tvUaI27).
- Vedl jsem jednání s třemi firmami o jejich spolupráci s JG.
- Šel jsem na procházku s jedním velkým šéfem jednoho velkého českého startupu. Stále platí, že do června nehledám novou práci a počítám s tím, že se mi povede do té doby klub rozjet, ale je dobré nenechat si zrezavět zadní vrátka.
- Přeorganizoval jsem kanály v klubu na Discordu, aby (snad) lépe odrážely způsob, jakým lidé v klubu diskutují.
- Naprogramoval jsem integraci pracovních nabídek z portálu [Dobrý Šéf](https://dobrysef.cz/). Sami za mnou přišli a nabídli, že můžeme nabídky propojit.
- Snažil jsem se naprogramovat integraci [pracovních nabídek z Česko.Digital](https://wiki.cesko.digital/pages/viewpage.action?pageId=1573299#Kohote%C4%8Fhled%C3%A1me-%F0%9F%91%A9%F0%9F%8F%BB%E2%80%8D%F0%9F%92%BBV%C3%BDvoj), ale zatím se to nepovedlo dokončit. Je potřeba přeorganizovat data v Airtable (poprosil jsem) a pak [dokončit Pull Request](https://github.com/cesko-digital/cd-tools/pull/3). Byť jsem se u toho dost rozčiloval (kvůli Airtable) a vůbec neuměl TypeScript, všichni na mě byli moc milí a se vším mi pomáhali.
- Neuváženě jsem po dlouhé době upgradoval vše, co mám nainstalované přes Homebrew. Potom jsem hodinu nebo dvě řešil, proč mi přestalo vše na JG fungovat a dokola jsem přeinstalovával náhodné npm závislosti.
- Firmy, které mají logo na příručce, dostávají e-mailem pravidelné souhrny se statistikami. Doplnil jsem možnost zaznačit si, že firma souhrny dostávat nechce.


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. **[PANIC MONSTER](https://waitbutwhy.com/2013/10/why-procrastinators-procrastinate.html)** Napsat konečně článek pro [Kariérko.cz](https://karierko.cz/) **[PANIC MONSTER](https://waitbutwhy.com/2013/10/why-procrastinators-procrastinate.html)**
2. Přidat co nejzajímavější nový obsah do příručky a propagovat to, tím dostat přes nové menu další členy do klubu.
3. Komunikovat s firmami. Připomenout se těm, se kterými jsem si psal dřív a nemám odezvu.

Bonusy: Dále bych měl přemýšlet nad tím, [jak překopu homepage](https://twitter.com/honzajavorek/status/1362712162062524418) a jak překlopím příručku nebo celý web do MkDocs.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Je to druh sociální kritiky, říká Marie Heřmanová o konspiračních teoriích](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.novinky.cz%2Fkultura%2Fsalon%2Fclanek%2Fje-to-druh-socialni-kritiky-rika-marie-hermanova-o-konspiracnich-teoriich-40350134&h=931faac1550c9d305e455f4012797a91dbc14d2bcecfdb2332b5f6433bc45300)<br>“Dalo by se říct, že věříme konspiracím, protože jinak bychom museli uvěřit, že selhal kapitalismus – ale to by byla moc velká kognitivní disonance, to jde proti všemu, co se tady třicet let říkalo. Konspirace mohou lidem dávat paradoxně větší smysl.”
- [Vědci zkrotili jev umožňující teleportaci informací, pokládají základy kvantového internetu](https://getpocket.com/redirect?&url=https%3A%2F%2Fzahranicni.ihned.cz%2Fc7-66875080-r6hff-a9f9324f5d88fd6&h=ecd82f9a662cac27fbb6b4b79944b45770d4f32c69b3f6268e897290ef991aee)<br>Kvantové počítače se blíží. Na co se můžeme těšit?
- [Nelžete dětem, že budou potřebovat rozeznat druhy nerostů](https://getpocket.com/redirect?&url=https%3A%2F%2Fnicoleb.cz%2F2021%2F02%2Fnelzete-detem-ze-budou-potrebovat-rozeznat-druhy-nerostu%2F&h=38ddc7482dda8350c4496085ccde38ca5f2e60712aa3cabf8076f775f75203c0)<br>“Učení je poznávání chtěného i nechtěného, ale rozhodně ne nuceného – tomu se totiž říká otročení mysli.”
- [How Covid brought the future back](https://getpocket.com/redirect?&url=https%3A%2F%2Fworksinprogress.co%2Fissue%2Fhow-covid-brought-the-future-back%2F&h=5de124d5d8ad77cd3d8970389233ede8fdc20f5f2dcefd0d8aa9c9770e62b813)<br>Zajímavý článek o tom, jak bubliny předpovídají budoucnost, o Tesle, o SPAC, o dot-com a o tom, že nic nebude tak, jako bylo dřív a že to jde vyčíst z akciového trhu stejně, jako z nej šlo kdysi vyčíst, z čeho se vyrábí atomovka.
- [Co se děje u Babiše](https://getpocket.com/redirect?&url=https%3A%2F%2Freportermagazin.cz%2Fa%2FprrGV%2Fco-se-deje-ubabise&h=1330490fe1695b05eba488787c434ca8bc25969f7978a3a2ecd07cb0b4447d44)<br>Jak (ne)funguje náš premiér.
- [Na českých životech záleží. Politici odmítají nést odpovědnost za pandemii](https://getpocket.com/redirect?&url=https%3A%2F%2Fa2larm.cz%2F2021%2F02%2Fna-ceskych-zivotech-zalezi-politici-odmitaji-nest-odpovednost-za-pandemii%2F&h=85c5df9a6a179778d898976440f067b98af44a868c2d61c5c889d70b99863c5b)
- [Why did I leave Google or, why did I stay so long?](https://getpocket.com/redirect?&url=https%3A%2F%2Fpaygo.media%2Fp%2F25171&h=85b48e246dc5db7b3616c69ac2d9f5b5d703cb704498adcd191ba00fea0ad29a)<br>Až příliš podobné tomu, co jsme prožili po akvizici Apiary :)

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
