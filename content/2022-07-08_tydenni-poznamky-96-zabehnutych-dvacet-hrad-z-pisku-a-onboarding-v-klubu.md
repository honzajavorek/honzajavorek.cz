Title: Týdenní poznámky #96: Zaběhnutých dvacet, hrad z písku a onboarding v klubu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl zase nějaký ten týden (2.7. — 8.7.) a tak [stejně jako minule]({filename}/2022-07-01_tydenni-poznamky-95-opravy-cisel-a-premysleni.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Na tento týden jsme odjeli ke Zlínu k babičce, což nazývám dovolenou, protože tím vzniká nepoměr 3 dospělí na 1 batole v místě, kde je bazének, houpačka, zvířátka, pískoviště, apod. Tím ale velmi erodovala moje pracovní morálka. Prioritizoval jsem zážitky s rodinou a k práci jsem si sedl, jen když nebyl jiný program. Za jedny z největších úspěchů tedy považuji třeba postavení hradu z písku nebo zaběhnutí 20 km přes kus Zlínského kraje. Hrad si můžete ještě chvilku prohlédnout [ve storíčku](https://www.instagram.com/honza.javorek/), jsem líný si fotku posílat na počítač a dávat do článku.


## Robotický onboarding

Během těch pár hodin, které jsem si vyhradil na programování, jsem vytvořil základní funkčnost robotického onboardingu nových členů do klubu. Můj Discord bot nyní dokáže projít všechny členy a vytvořit jim soukromý kanál, do něhož má přístup jen tento člen, robot a moderátoři. Do tohoto kanálu poté bot dokáže postupně posílat nějaké přednastavené zprávy.

Chtěl jsem, aby robot uměl kanál smazat, pokud už člověk v klubu není. Kanál je k osobě vždy přiřazen skrze ID, které si ukládám do topicu kanálu. Bot topic parsuje a podle ID zjistí, čí kanál to je. Přišlo mi to lepší, než kdyby musel zkoumat oprávnění v kanálu a dovozovat si z toho, který člen je tam navíc kromě moderátorů a robota. Také mi to přišlo spolehlivější, než to dělat vyloženě jen podle názvu kanálu (může být víc členů se zhruba stejným jménem). Ještě mě napadlo, že by bot neměl kanál mazat hned, ale až třeba po měsíci, protože lidem třeba vyprší karta a tak, takže aby neztratili hned historii a nerestartoval se onboarding.

Zprávy v kanálu se řídí tím, že začínají nějakým emoji. Bot najde poslední svou zprávu v kanálu, která začíná na určité emoji a podle toho ví, která to je. Žádné dvě onboarding zprávy s tipy nesmí tím pádem mít stejné emoji. Když časem upravím text pro určitou zprávu, umí bot původní zprávu editovat. Ještě jsem uvažoval, že by mohl pak dodat ještě reply do kanálu, že ji upravil, pokud je to už delší doba, ale to je bonus. Taky by se zprávy měly posílat s nějakým časovým odstupem, třeba každý den jedna. Teď se tam zatím nasolí všechny najednou.

To celé vyvíjím jako continuous delivery, takže je to už na produkci. Mám to ale zatím omezeno pouze na jednoho testovacího uživatele, takže členové to nevidí. Teď bych měl jednak dodělat to postupné posílání, jednak bych měl hlavně vymyslet obsah těch tipů, tak aby dával největší smysl. Už teď vím, že se s tím budu moc patlat. Musím si opakovat, že lepší mít něco trochu blbého hned a iterovat a vylepšovat to už se zpětnou vazbou od lidí, než abych to ladil k dokonalosti někde bokem. Ideálně kdyby se to celé spustilo, klidně i jen s třemi úvodními zprávami, třeba už příští týden.


## Další poznámky

- Vymýšlel jsem rodinnou dovolenou na září. Zjistil jsem, že neumím vymýšlet rodinné dovolené. Ještě tomu dám pár pokusů a pak jdu pro katalog Čedoku.
- Vypadá to, že opravili [problémy](https://github.com/instantpage/instant.page/issues/72) v instant.page, tak jsem to na JG upgradoval na nejnovější verzi.
- Strašně jsem si užil Silverstone ([sestřih](https://www.youtube.com/watch?v=bM6ren2tPU8)), což byl snad nejlepší závod, jaký jsem kdy v F1 viděl. Nutno podotknout, že jsem F1 posledních 10 nebo 15 let nesledoval a to předtím si pamatuju jen dost matně :D
- Sociální sítě jsem prokrastinoval, protože jsem na ně neměl náladu.
- Klub, maily, zprávy na LinkedIn, a tak dále. Klub i maily jsem prošel několikrát a bylo hodně co řešit. Ve skutečnosti mi to zabralo velký díl času, který jsem během uplynulého týdne věnoval práci. V klubu jsem si například dal tu práci napsat feedback hned na tři CVčka.
- Pokročil jsem v domluvení konzultace s [Janou Dolejšovou](https://www.janadolejsova.cz/).
- V klubu jsem doplnil popisek kanálu pro mentoring a upravil návod, jak se zakládají vlákna v poradně, protože byl špatně a nikomu kromě mě nefungoval.
- Domluvil jsem prodloužení partnerství s [Inuits](https://www.inuits.eu/) a poslal fakturu.
- Odebral jsem kód na slevu na lístky na WebExpo, který jsem před konferencí schoval do různých částí kódu JG webovek.
- Během 7 dní od 2.7. do 8.7. jsem naběhal 34 km, při procházkách nachodil 18 km, ujel na kole 9 km. Celkem jsem se hýbal 16 hodin a zdolal při tom 61 kilometrů.
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/).


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1. Navrhnout náplň onboardingu.
2. Vymyslet nový ceník.
3. Seznam co zrušit, delegovat, nebo automatizovat přeměnit na konkrétní úkoly.

**Bonus:** Doplánovat si pořádnou dovolenou.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [Pod čarou : Každý příběh je lež. Nepřehánějme to s jejich vyprávěním.](https://seznam-zpravy.u.mailkit.eu/mc/VVQIVPEI/IFFILXQQDLFARYLJIY/CQMCWMIUIPV) si záměrně zamlčujeme řadu důležitých věcí. A možná ještě horším důsledkem je, že se kvůli důrazu na příběhy navzájem velmi podceňujeme a hovoříme spolu jako s malými dětmi.“
- [Na záda batoh a jde se. Matka čtyř dětí radí, jak cestovat s dětmi bez auta. Hlavní je trpělivost a nelpět na plánech](https://www.heroine.cz/zena-a-svet/8966-na-zada-batoh-a-jde-se-matka-ctyr-deti-radi-jak-cestovat-s-detmi-bez-auta-hlavni-je-trpelivost-a-nelpet-na-planech)<br>Drsné.

<small>Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. K vygenerování tohoto seznamu používám vlastní knihovnu <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>. Věci, které jsem sdílel v den psaní minulých poznámek, se opakují i v těch dalších a je to záměr, ne chyba.</small>
