Title: Jaký si mám vybrat Linux?
Date: 2012-07-06 10:36:23

Upgradoval jsem po dlouhé době svoje Ubuntu a zjistil, že ani Unity, ani Gnome Shell nejsou zrovna něco, v čem by se z mého pohledu dalo pohodlně pracovat. Zkusil jsem přeinstalovat na Linux Mint s prostředím Cinnamon, existovat se v tom dá, ale je to plné chyb a to mě nebaví. Píšu tedy linuxácký štěk o tom, jak hledám nové distro. Koho to nezajímá, nechť přeskočí komentáře a jde si číst [básničky](http://honzajavorek.cz/blog/ztisnena).

## Co od svého distra očekávám?

- Jede na Debianu. Fungují na něm návody na Debian nebo pro Ubuntu, `.deb` balíky a všude je k dispozici `apt-get`. Jednak je to pohodlné a skvěle funkční (kdysi jsem zkoušel Fedoru a instalace každé kraviny mi furt končila na nějakých závislostech - možná jsem však jenom blbej), za druhé je internet plný návodů jak něco udělat pod Ubuntu. O dalších distribucích je toho řádově méně.
- Nemá pomalý vývoj. Když chci nainstalovat nejnovější Redis nebo PHP, tak na to nečekám rok. Ano, kompilace je taky způsob jak instalovat software, ale já mám rád balíčky a aktualizace...
- Má dodělané UI! Dodělané znamená, že v něm nejsou chyby a má minimální WTF faktor. Unity je celé WTF, Gnome Shell ještě víc, Cinnamon z Mintu mi ukazuje dva dialogy na připojení k Wi-Fi a baterku že prý mám pořád na 98 %, ačkoliv jsem v síti. Děkuji, nechci.
- Hardwarové nároky (grafické karty, tiskárny, apod.) nemám. Ubuntu i Mint mi na HP notebooku pohodlně jede, takže očekávám, že by s ničím být problém neměl ani jinde.
- Je možné jej pohodlně provozovat s nějakým Clearlooks skinem. Žádné vyblitě zelené patlaniny (Mint) nebo oranžovo-černé, humpolácké prostředí vhodné akorát tak pro fanoušky [Duny](https://cs.wikipedia.org/wiki/Duna_%28rom%C3%A1n%29). Clearlooks skin "nosím" už od ranných dob Windows XP a líbí se mi ze všech pořád nejvíc, ač je dost okoukaný a patrně nejnudnější na světě.

To Clearlooks vypadá takto:

![Clearlooks](images/clearlooks.png)

Pohodlně skinovat na Clearlooks neznamená, že horko těžko najdu nějaký [Clearlooks-Phoenix](http://gnome-look.org/content/show.php/Clearlooks-Phenix?content=145210) GTK3 skin a potom zjistím, že na půlku oken se neaplikuje (nejspíš jsou v GTK2? ale koho to zajímá? proč to není dohromady?).

Ubuntu se snaží jet na kvalitu a uhlazenost, ale pro mě špatným směrem :-/ Tam opravdu sleduji jakousi snahu dotahovat věci do konce a zalepovat zamaskované díry, do kterých se člověku občas propadl kurzor myši, ale všechnu energii Canonical teď směřuje na Unity a to je bohužel z mého pohledu monolitická divočina, na kterou si nechci zvykat.

U jiných distribucí mám však obavy o ještě větší náchylnost na chyby. Vždyť Mint je snad druhé nejinstalovanější distro na světě. Úplně to ale vidím na tom Cinnamonu - přijde mi, že někdo to nakódil po večerech ze zábavy a sám to snad ani nepoužívá.

Určitě mi navrhnete KDE, ale to fakt nechci. Je to strašně nablýskané, naleštěné, každý ovládací prvek má třicet tlačítek a dá se nakonfigurovat snad i velikost ponožek jeho vývojáře. To je přece opačný extrém. Celý ekosystém KDE má sto programů (snad i na vaření kávy) a ty jsou v základu hned nainstalovány na můj systém. Drtivou většinu z nich nikdy nevyužiju, takže je pak odinstalovávám a to přece není žádná zábava. Možná je to zase trochu jinak, ale já už to zkoušel tolikrát, že se mi nechce ztratit zase celý den zbytečnou instalací KDE a jeho následným odebíráním. Připadal bych si jako moucha narážející do skla.


## Linux?

Jistě lze zpochybnit, [zda je pro mě Linux ten pravý operační systém](http://honzajavorek.cz/blog/tyden-s-tucnaky). To já osobně netuším, ale zkusme to jednoduchou dedukcí. Potřebuji nějaký UNIX, protože mi to neskutečně usnadňuje mou práci. Nedovedu si představit pořád překonávat nějaké překážky s vývojem v Pythonu či v PHP na Windows - navíc pokud je finální železo mé aplikace UNIXový server.

- Windows? *Windows' Not Unix!* Navíc, nějaké lítající placičky ve Windows 8 mě nelákají už vůbec. Nechovám k tomuto OS žádnou zášť, [mnoho let jsem jej používal](http://honzajavorek.cz/blog/windows-xp-budou-moje-posledni-windows), Windows 7 jsou velice dobrý systém, ale chybí tam prostě ten UNIXový podklad. Ne, Cygwin není řešení.
- Mac OS je sice UNIX, ale to svoje UI má dost svérázné a já si netroufám nijak tvrdit, jestli by mi vyhovovalo nebo ne. Bohužel, systém je to dost drahý a nevím o tom, že bych měl možnost si zkusit pracovat na něm několik dní bez zakoupení. Mám obavy, že dost lidí si raději zvykne i na to, co jim úplně nevyhovuje, protože dali 20 litrů za Mac a přece se ho nebudou zbavovat na Aukru jen kvůli "pár nedokonalostem" :) Také je tam vazba na hardware a ten ve mě budil vždy dojem *karoserie od Pininfariny, motor z Fiat Panda*.

Navíc, oba zmíněné systémy (a řekl bych, že i to Ubuntu se v tomto snaží držet krok) inklinují k tomu, aby se staly *firmwarem* svého hardwaru - jestli víte, co tím myslím. Chápu, že 99 % populace to chce, ale já nemám rád, když nad svým OS nemám alespoň nějakou kontrolu. Vždy tam musí být nějaký `root`, který mi dovolí vše co chci, dát si *partitions* na disku jak chci, atd. Takže co zbývá? Linux. S uživatelským rozhraním, které mi je asi nejblíž (možná ten Mac?), ale zároveň je dost nedodělané. Achjo.

Pokukuji po [Xubuntu](http://xubuntu.org/), ale už mě to nebaví. Rozhodně nic přeinstalovávat teď nebudu, možná po létě. Slunečné dny jsou příliš drahá cena za nový Linux ;-)
