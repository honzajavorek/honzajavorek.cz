Title: Týdenní poznámky: Média a metriky z příručky
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden (7.9. — 11.9.) a tak [stejně jako minule]({filename}/2020-09-04_tydenni-poznamky-uverejneni-prirucky.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Média

Minulý týden jsem zakončil bláznivým pátkem, kdy spousta lidí našla příručku po [retweetu](https://twitter.com/spazef0rze/status/1301773489041371136) Michala Špačka a po publikaci zpráviček na Lupě, Rootu a Zdrojáku. Zároveň jsem finalizoval tiskovku.

V pondělí jsem udělal poslední úpravy na tiskovce. Přečetl jsem si všechno možné na [PR tipech](https://prtipy.cz/) a zjistil jednu zásadní věc: Nepotřebuji tiskovou zprávu :D Tisková zpráva je hromadný spam do schránek redakcí, kterým firma dává najevo, že existuje, a udržuje nějaký _heartbeat_ informací o sobě, kdyby je náhodou někdo potřeboval. Není to ale způsob, jak novinářům říct, aby o vás něco napsali. Cituji [PR tip](https://prtipy.cz/2018/06/30/posilame-tiskove-zpravy-a-nemame-z-nich-vystupy-jak-je-to-mozne-a-co-s-tim-075/):

> S novináři musíte komunikovat přímo, připravit pro ně unikátní témata, dát jim to, co zrovna potřebují. Hovořit s nimi o věcech, které jsou podstatné, nové, zajímavé a mají smysl pro jejich čtenáře. K tomu tiskové zprávy neslouží.

To dává perfektní smysl, že? Čím spíš novinářům naservíruji nějaké unikátní, zajímavé téma, tím spíš z toho udělají článek. A TZ je z definice unifikovaná zpráva, která se rozesílá na tunu adres, takže jde úplně proti tomu. Tak jsem se zase něco nového naučil! Aspoň nemusím být smutný, že [moje TZ](https://junior.guru/press/handbook/) podle některých není dost profesionální. (Ale že je podle některých na první TZ prý docela dobrá, to si samozřejmě někam zarámuju.)

No, když už jsem tu TZ měl, tak jsem tedy v pondělí ještě zapracoval všechny připomínky a večer rozeslal na všechny možné adresy. Moc jsem od toho nakonec nečekal, takže jsem použil prakticky stejný "media list" co minule.

Abych ale nezůstal jen u toho, že TZ je na nic, jal jsem se řídit radou z PR tipů a napsal osobně pár novinářům, jestli by neměli zájem o exkluzivní obsah, který jsem schopný nějak dodat nebo konzultovat. To nějakou odezvu mělo, jestli se to promění i ve hmatatelné výsledky, to se ještě uvidí. TZ se mi v tomto případě hodila jako poznámka pod čarou - mimoděk jsem mohl zmínit, že jsem něco vydal a do závorky napsat, že detaily jsou tady v tiskovce. Takže třeba úplně k ničemu nakonec nebyla.

I přes to všechno díky všem, kteří mi s TZ pomohli. I když si příště rozmyslím, zda něco jako TZ potřebuji, bylo to velmi poučné cvičení a rozhodně užitečná lekce jak vůbec psát něco, co by mohl chtít číst někdo, kdo to číst nechce. Já jsem totiž zvyklý psát jen věci, kde předpokládám dobrovolné zaujetí čtenáře už díky vybranému tématu :)

## Metriky z příručky

Během čtvrtka jsem neměl žádné pochůzky ani telefonáty, takže jsem ráno radostně usedl k počítači a odlepil se od něj až večer. Tento nepřerušovaný čas jsem věnoval velkému nápřahu co nejrychleji zhotovit posílání statistik zobrazování sponzorských log na příručce a klikání na ně.

Věděl jsem, že se mi to moc dělat vlastně nechce a že bych to prokrastinoval, tak jsem se rozhodl, že to tedy udělám co nejdřív, ať to mám prostě z krku, i když na to mám ještě skoro měsíc. No a za jeden den bylo vymalováno. Byl to kód dost podobný tomu, co už mám pro pracovní inzeráty, takže nic velice náročného.

Informace o sponzorech mám teď v Google Spreadsheets, kde je mohu snadno upravovat a mám tam i informace, jako kolik kdo platí apod. Odtud se hezky stáhnou do SQLite a přidají se k nim data o proklicích a návštěvnosti z Google Analytics. Loga se nově vypisují na příručku z SQLite (kdo má delší tarif, zobrazí se dřív, potom se to řadí podle data začátku sponzoringu), předtím tam byly prostě natvrdo ručně vepsané do HTML. Posílání mailů jsem vyčlenil do samostatného workflow v CI, aby nehrozilo, že mi spadne nightly, já udělám retry a pošle se klientům duplicitní várka mailů. Teď to bude hezky padat každé zvlášť :) No a mám hotovo, už stačí jen počkat do 1.10. na první várku, protože statistiky ze sponzoringu se budou posílat měsíčně. Všechno mám samozřejmě hezky otestované.

Počítání návštěvnosti pro loga bylo zajímavé, protože mám samozřejmě jen data o tom, kolik lidí si zobrazilo příručku. To je totožné se zobrazením loga, ale každé logo je na příručce jen v určitém časovém období, a v tom je ten rozdíl. Takže stahuji informace o návštěvnosti pro každé jednotlivé datum a potom dělám pro každé logo sumu čísel za interval, kdy bylo zobrazeno na příručce.

Práci na statistikách o tom, kdo chodí z jakého regionu, jsem zatím pozastavil. Chce to jen jeden klient a bylo by to hodně kódu. Nejdřív počkám a uvidím, jestli je to opravdu tak strašně potřeba.

## Další poznámky

- [Scrapy](https://scrapy.org/) udělalo nějaké změny, které způsobovaly "deprecation warnings" v kódu robota na nabídky práce. Opravil jsem to.
- Odstranil jsem PayPal ze [stránky, kde prosím o příspěvek](https://junior.guru/donate/). Za celou dobu jej použil jeden člověk. Většina lidí, kteří mi chtějí něco poslat jednorázově, zvolí přímou platbu na účet. Kdo mě chce podporovat dlouhodobě, má možnost v podobě GitHub Sponsors nebo Patreonu.
- 2x mentoring session.
- Schůze výboru [Pyvce](https://pyvec.org/). Konečně jsme obnovili schůzování po koroně, v létě jsme na to trochu kašlali. Probrali jsme pár drobností a shodli jsme se, že bychom se možná časem mohli odvážit i naučit se konečně svolávat členskou schůzi, [když už teď máme i ty členy](https://docs.pyvec.org/operations/runbooks.html#jak-clenstvi).
- PyLadies kurzy v Praze budou mít na podzim i běh v nějaké online podobě a k tomu si zakládají dedikovanou FB skupinu (každý běh má svoji jen pro lidi z daného běhu). Poprosili mě, abych doplnil obrázek pro záhlaví skupiny, takže [tady je](https://github.com/pyvec/resources/blob/master/Design/Facebook%20Group%20Headers/pyladies-praha-online.png).
- Řešíme, proč jednomu inzerentovi nechodí maily se statistikami. Vypadá to, že nějaká náhodná IP adresa SendGridu se dostala na náhodný spam list a jejich firma ty maily nepustí dovnitř. Zatím ping pong s jejich technickou podporou.
- Poněkolikáté se mi stalo, že jsem zapomněl zaznamenat datum, kdy jsem určité inzeráty rozeslal v newsletteru. Přišel jsem na to až když jsem kontroloval maily se statistikama pro inzerenty, ve kterých tato informace je. A byla tam špatně. Takže jsem se už naštval a naprogramoval skript, který z MailChimp API stáhne informace o obsahu newsletterů, najde v nich odkazy na inzeráty, a do databáze uloží údaje o tom, která nabídka práce byla ve kterém newsletteru odeslána. Pryč s manuální prací! Teď už se bude vše dít automaticky a nemusím na to myslet.
- Zmizelo video Cala Newporta z Vimeo.com a rozbilo mi to odkaz. Po dlouhé době byl můj skript na kontrolu odkazů opravdu užitečný a ne jen otravný. Našel jsem naštěstí [podobné video na YouTube](https://www.youtube.com/watch?v=LUQjAAwsKR8). U této příležitosti jsem si jej i pustil a [přepsal závěr příručky](https://github.com/honzajavorek/junior.guru/commit/c4eee432dae8f8098e7e086706329b1813a6e25b), aby nebyl tak moc ezo.
- Na [stránku pro firmy](https://junior.guru/hire-juniors/) jsem přidal logo Root.cz do místa, kde jsou média, která někde zmínila JG. Můj skill s Inkscape je každým dnem mnohem lepší!
- V pátek jsem měl hovor s Lukášem z [Fakturoidu](https://www.fakturoid.cz/) o tom, že bychom společně něco mohli připravit. Potom jsem strávil nějakou tu hodinu tím, že jsem připravoval tu svou část. Víc prozrazovat zatím nebudu.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Programování je bolest](https://getpocket.com/redirect?&url=http%3A%2F%2Fborisovo.cz%2Fprogramming-sucks-cz.html&h=1f77c3e49a00598020adb476a1109d39fc7c13d9fc9c254ca6850fd447c0e87d)<br>Když se živíte programováním, máte místo fyzické zátěže psychickou. Zbude vám jen vykouřit krabičku cigaret denně nebo meditovat. Tohle bych měl asi na JG taky nějak zmínit :)
- [Příručka hledání první práce v IT](https://getpocket.com/redirect?&url=https%3A%2F%2Fjunior.guru%2Fcandidate-handbook%2F&h=c3271c25a00beb18d5bab00a4b909e32d644923d8c6ad904128dbe897d53d583)<br>Nejlepší příručka, jakou jsem kdy četl! 😀
- [Transcript of Reboot 11 speech by Bruce Sterling, 25-6-2009](https://getpocket.com/redirect?&url=https%3A%2F%2Fwww.wired.com%2F2011%2F02%2Ftranscript-of-reboot-11-speech-by-bruce-sterling-25-6-2009%2F&h=e8d4e39e7e40399ab5af76194557a2abf2816cc98ce315249b224301b5f99029)<br>Skoro deset let starý projev o tom, jak budeme žít dnes. Technologie, způsob života, rozmělněný pokrok, ekologie a nakonec rady ala Marie Kondo. Hodně zvláštní text, který si budu muset asi přečíst víckrát, než ho plně vstřebám.
- [Budoucnost je v no-code aneb Proč květinářství nepotřebuje web na míru](https://getpocket.com/redirect?&url=https%3A%2F%2Ffrontend.garden%2Fbudoucnost-je-v-no-code-aneb-proc-kvetinarstvi-nepotrebuje-web-na-miru%2F&h=4121649606538c5c3885a973ec28e92b4a6ceed1aafe39e8a70f248cf2c9000b)<br>Že je overkill dělat web květinářství na míru, to asi tušíme. Že je dnes už overkill i ten WordPress, toho si ještě mnozí nevšimli.
- [Stát zkrachoval. Každý Čech se stává superministrem svého vlastního osudu](https://getpocket.com/redirect?&url=https%3A%2F%2Fnazory.aktualne.cz%2Fstat-zkrachoval-kazdy-cech-se-stava-superministrem-sveho-vla%2Fr%7E02071908f38711ea80e60cc47ab5f122%2F&h=f027a715b399246007409c1bb21eb261cdc88e27d0b3354613cb173d01602bed)<br>Stát DIY

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
