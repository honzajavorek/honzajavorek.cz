Title: Týdenní poznámky #97: Debugování a onboarding
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (9.7. — 15.7.) a tak [stejně jako minule]({filename}2022-07-08_tydenni-poznamky-96-zabehnutych-dvacet-hrad-z-pisku-a-onboarding-v-klubu.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Debugování pycordu

Pycord, tedy Python knihovna na interakci s Discordem, vydala novou verzi. Po mnoha _release candidates_ vydali konečně v2. Chtěl jsem hned upgradovat, ale zjistil jsem, že nová verze konzistentně selhává ve stahování a analýze obsahu klubu.

Založil jsem [issue](https://github.com/Pycord-Development/pycord/issues/1491) a několik následujících dní jsem postupně zkoušel debugovat, proč to padá. Zabralo mi to ohromné množství času, ale měl jsem zrovna na takovou detektivku celkem náladu a říkal jsem si, že discord.py a pycord mi ušetřily svou existencí už tak milion hodin, takže proč nějakou lásku nevrátit zpět.

Nicméně zatím se mi nepovedlo problém rozřešit a vypadá to, že jde o nějaký hodně specifický problém, takže ani nenaskakuje moc dalších lidí na to, aby se jím zabývalo. Zbývá ještě několik věcí, které bych mohl udělat, abych zjistil, co se přesně děje, ale nějak bych už rád dělal zase něco jiného, takže jsem upgrade zatím odložil.


## Onboarding

Nejdřív jsem opravil zjevný bug v prototypu onboardingu z minulého týdne. Bot posílal zprávy všechny najednou a ne každý den jednu.

Potom jsem se podíval do Trella a snažil se udělat si pořádek v kartičkách, které se onboardingem nějak zabývají. Bylo toho hodně a dalo mi dost mentální práce vytvořit si z toho v hlavě nějakou mapu a uspořádat si myšlenky. Je to celé mnohem větší:

- Plynulá cesta člověka na [stránce /club/](https://junior.guru/club/) až do Discordu.
- [FAQ](https://junior.guru/faq/)
- Tipy ohledně Discordu samotného, ohledně klubu, ohledně JG webu a všech funkcí JG
- Uspořádání klubu, kanál s pravidly, okýnko s pravidly, uvítací texty a popisky na Discordu
- Stránka o tom, jak se správně ptát a jak správně debugovat

A mnohé další. Trello jsem si přesypal několikrát na různé hromádky, než se mi z toho začalo něco rýsovat. Rozhodl jsem se, že půjdu zevnitř ven - nejdříve vylepším klub jako takový a uživatelskou experience v něm. Poté vylepším jak se lidé dostávají do klubu. Potom vylepším stránku o klubu. Potom hlavní stránku JG a SEO a _inbound_ marketing atd.

Myslím si, že je nutné to udělat v tomto pořadí, protože naopak by to vedlo k tomu, že víc lidí dokážu dostat do klubu, ale oni odpadnou, protože tam bude hrozná uživatelská zkušenost. Zlepšením zkušenosti si zachovám co nejvíc lidí z těch, kteří už teď jsou schopni do klubu přicházet a když to bude vyřešené, mohu uvolňovat _funnel_ ve vyšších polohách a lít do něj víc a víc lidí.

Udělal jsem postupně tyto věci:

- Prošel jsem si jak vypadá onboarding do [Scrimba](https://scrimba.com/), pro inspiraci.
- Prošel jsem si s úplně novým fake uživatelem onboarding do klubu od objednávky po psaní do kanálů a dělal jsem si poznámky. Bylo to příšerné. Vůbec nechápu, že je někdo schopen se do klubu probojovat, já bych to asi pětkrát vzdal. Většinu z těchto věcí ale budu, jak jsem psal už výše, opravovat spíš později.
- Podíval jsem se, [jak ještě mohu upravovat vzhled](https://vimeo.com/715325990) objednávkové stránky atd.
- Všiml jsem si, že kanál na oznámení ve Scrimba nemají jako typický Discordí _news channel_. Pokud nevyužívám možnost že by někdo ten můj _news channel_ odebíral, je to možná lepší jako normální kanál, protože zpráva „odebírej tento kanál na svém serveru“ nemate nové uživatele. Tato zpráva se mi jako adminovi nezobrazuje, takže bez toho, že bych si vyzkoušel klub jako cizí člověk, bych na to vůbec nepřišel. Hned jsem to změnil.
- Překopal jsem neskutečné množství věcí v klubu tak, abych jej zjednodušil. Sloučil jsem některé kanály, některé archivoval, přejmenoval. Prošel jsem _topic_ zprávy a _pinned_ příspěvky ve všech kanálech a buď je přepsal, nebo změnil, atd. Zkoušel jsem, jestli by kanály nebyly přehlednější s emojis na začátku, jak jsem to viděl na jiných Discordech (nebyly). Zjednodušil jsem kategorie, do kterých se kanály dělí. To vše jsem udělal proto, abych měl méně práce s onboardingem. Pokud bude klub sám o sobě jednodušší, bude méně věcí na vysvětlování. Opět mě v tom trochu inspirovala Scrimba, kde jsou tisíce lidí a přesto je tam jen pár kanálů. Zas nemohu kopírovat 1:1, protože oni jsou víc orientovaní na kurzy, kdežto já provozuju víc diskuzní Discord a proto je přece jen adekvátní, že mám víc kanálů.

Pak jsem i trochu programoval. Uvědomil jsem si, že je sice milé, jak jsem prototyp onboardingu naprasil nejrychlejším možným způsobem, ale že už teď se v tom nevyznám a přitom to ještě nic pořádně neumí. Samý if/else a spousta možností, co se může stát, v tom zaprasené async/await se změnami na Discordu jako mazání nebo vytváření kanálů. To si říkalo o velký špatný.

Takže jsem to rozdělil. Vždy jsem udělal funkci, která vezme data a na základě nich vrátí datové struktury v podstatě s instrukcemi o tom, co se má provést. Tyto funkce lze skvěle testovat a také jsem je co nejvíc otestoval. Na vstupu různé situace, které se mohou v kanálu se zprávami objevit, na výstupu co by měl můj skript udělat. Když objevím bug nebo situaci, se kterou jsem původně nepočítal, nebo budu chtít přidat funkčnost, prostě si přidám _test cases_ a bude. Kód, který pak sahá přímo na Discord je už relativně primitivní a testovat ho nemusím, nebo spíš prostě nebudu. Bere instrukce a provádí je, kontrola že funguje správně jde celkem dobře dělat i jen okem. Sice mi to zabralo den a půl, ale hodně mi to pomohlo kód připravit na to, abych do něj něco dalšího přidával a jsem rád, že jsem to udělal.


## Další poznámky

- Z grafů o příchodech a odchodech na [stránce s čísly](https://junior.guru/open/) jsem odmazal poslední měsíc, protože v něm stejně byly nesmysly a jen mi to ustřelovalo měřítko osy Y a kazilo čitelnost předchozích měsíců.
- Zabýval jsem se odpovídáním na různé věci na Pyvec Slacku, kde se mi toho za zhruba týden, co jsem tam nebyl, trochu nahromadilo.
- Zavolal jsem si s mentorem z Mews, který se už přes rok nabízí v klubu na 1:1 konzultace. Byl z toho dvouhodinový hovor, ze kterého si odnáším spoustu poznámek a poznatků.
- Sociální sítě:
- V klubu se toho moc neděje, asi léto. Mailů jsem měl přes 30, většinu jsem vyřešil.
- Během 7 dní od 9.7. do 15.7. jsem naběhal 8 km, při procházkách nachodil 11 km. Celkem jsem se hýbal 6 hodin a zdolal při tom 19 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Ceník jsem opět nevymyslel a ještě je na to snad čas, tak to nechám zatím být. Seznam co zrušit, delegovat, nebo automatizovat jsem taky nepřeměnil na konkrétní úkoly, udělám někdy později. Stres ze zátěže režií ustal s tím, jak všichni odjeli na dovolenou.

Budu se teď soutředit na onboarding, když už jsem ho rozdělal. Takže tři věci, které bych chtěl zvládnout udělat příště:

1. Doprogramovat základní funkčnost onboardingu.
2. Připravit první verzi zpráv pro onboarding a pustit je do první testovací skupiny lidí.
3. Zpracovat poznámky z hovoru s mentorem a prodiskutovat je s ostatními mentory.

**Bonus:** Doplánovat si pořádnou dovolenou.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}2020-06-04_neni-to-zavod.md). Není zač!
