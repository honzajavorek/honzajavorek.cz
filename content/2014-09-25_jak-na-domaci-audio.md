Title: Jak na domácí audio?
Date: 2014-09-25 22:03:59
Lang: cs

Bydlím na novém bytě a vysnil jsem si, že v jednadvacátém století by nemuselo být těžké vymyslet nějaké sdílení domácích repráků tak, aby to nebyla pruda.

Tato hypotéza se úplně nepotvrzuje, ale neodrazuje mě to od myšlenek na nějaké řešení. Dalo by se říci, že s tím teď spamuju už dva dny Twitter a to je většinou okamžik, kdy by si měl dotyčný uvědomit, že to téma patří spíš někam jinak, třeba na blog. Už jen třeba proto, že odpověď na jeden tweet může vypadat třeba takto:

![konverzace]({static}/images/konverzace.png)

Samozřejmě mám mnohem lepší a důležitější věci na práci, samozřejmě že je to **[#firstworldproblems](https://twitter.com/hashtag/firstworldproblems)**, nebo snad dokonce **#tyhleproblémypražákůbychchtělmít**, ale já si prostě nemůžu pomoct.

## Moje situace

**Nejsem geek.** V tomto určitě ne. Chci něco koupit, chci abych to někam zapojil a aby to fungovalo. Nemám chuť si prgat po večerech skripty na spojování třech krabiček s třemi Linux distry specializovanými na hudbu a pak to devět měsíců rodit a ladit.

**Mám malý byt.** Má více místností a jedna má dokonce patro na spaní. V pokoji jsou klasické repráky s jackem a jsou slyšet z celého bytu. V bytě bydlíme dva, každý má notebook, časem by teoreticky mohl přibýt sdílený tablet nebo pracovní notebook, to je jedno. Nemáme a zatím neplánujeme smartphony. Používané OS jsou Linux, Windows, do budoucna možná jeden Mac, na tabletu potom iOS/Android. Rádi sdílíme do prostoru hranou hudbu pro osvěžení dne nebo navození atmosféry - sluchátka nepoužíváme.

**Mám spoustu hudby.** Chci ji uložit někam do cloudu nebo na jeden disk a pouštět si ji. Případně si chci občas pustit (internetové) rádio.

<small>(FM rádio nebudeme uvažovat, ať je situace jednodušší - dejme tomu, že si jej mohu vyjímečně pustit manuálně zastrčením jacku od repráků do své Nokie. Stejně se dá poslouchat jen bez reklam, což omezuje výběr na [COLOR](http://radiocolor.cz/) a různé noční [zóny lásky](http://www.radiocity.cz/#pageid=2000).)</small>

**Koukáme na seriály a filmy.** Chci, aby jejich zvuk mohl jet taky na těch reprácích.

### Případy použití

- přijdu domů, sáhnu po prvním zařízení a pustím na něm hudbu nebo rádio
- vařím a hraje mi u toho hudba, mohu ji přitom prvním zařízením po ruce ovládat (další písnička, hlasitost, ...)
- ležím v posteli na patře a bez scházení dolů můžu snížit hlasitost, vypnout hudbu, apod.
- ležím v posteli na patře a chci si pustit před spaním seriál - zvuk jde stále do repráků
- ideálně mám hudbu uloženou na jednom místě a dostupnou pro všechna svá zařízení, pro všechna zařízení přítelkyně a úplně ideálně i třeba v práci v kanceláři
- nechci, aby mi od tabletu nebo notebooku trčely nějaké dráty - chci, aby byly v rámci bytu normálně volně pohyblivé

## Moje situace na způsob Orbis pictus

![Domácí hudba]({static}/images/domacihudba.png)

### Možná řešení na repráky

- **Bluetooth**: V podstatě jsem si tím prošel a nejspíš to nechci. Kdysi jsem koupil něco jako handsfree, abych do toho píchl ten jack s tím, že se na něj budu připojovat přes BT z notebooku a vše bude super a bezdrátové. Jenže režie párování a připojování BT zařízení je velká, občas to blbne (zvlášť na Linuxu) a nakonec zjistíte, že A2DP je tak mizerné, že přehrávaný zvuk kolísá a co minutu slyšíte nějakou falešnou "vlnku", což vás, maje hudební sluch, přivádí k šílenosti. Za mě nejspíš *never more*. Dnes už jsou sofistikovanější věci, které asi budou hrát lépe a budou se integrovat lépe, třeba [tohle od Nokie](http://avmania.e15.cz/nokia-md-310-bezdratova-hudba-k-jakemukoliv-hi-fi-systemu) nebo [tyto srandy od Phillips](http://www.philips.cz/c-m-so/vyrobky-podporujici-aplikace/zvukovy-prijimac-bluetooth/latest#filters=BLUETOOTH_HIFI_ADAPTER_SU2&sliders=&price=&priceBoxes=&page=&layout=), ale stejně k tomu mám nedůvěru.
- **Chromecast:** Nezkoumal jsem to detailně, ale podle základního popisu to asi není úplně to co chci.
- **Sonos:** [Vypadá to](http://www.sonos.com/) úplně přesně jako to co chci, ale je to strašně drahé :)
- **AirPlay:** Mac věc, která taky vypadá jako něco co bych chtěl, ale myslím si, že bude kompatibilní jen s Mac světem a navíc je taky dost drahá.
- **RapsberryPi:** DIY řešení, které [vypadá celkem funkčně](https://twitter.com/starenka/status/515031269206675456). Nevýhodou RapsberryPi je třeba ale to, že na něj není Dropbox a nejspíš nikdy nebude (podpora pro specifickou ARM architekturu), nemluvě o dalších cloudových úložitích hudby, takže to lze kombinovat nejspíš jen s vlastním diskem.
- **ROCKI:** [Tohleto.](http://www.myrocki.com/) Velice zajímavé řešení, které vzešlo z Kickstarteru. Jestli jsem to dobře pochopil, je to v podstatě přesně to, co chci. Sice to má hnusný design, ale kdyby se to hodilo někam za polici, tak proč ne. Jenže jak to zkoumám víc a víc, tak se mi zdá, že to je pouze na telefon/tablet. Nelze to nejspíš ovládat z počítače (není appka pro Win/Lin/Mac).

### Možná řešení na sdílení hudby

- **Dropbox, Google Music, ...:** Dropbox je fajn z hlediska podpory různých zařízení a jednoduchosti. Prostě do něj hodím složku a je tam. Streamovat hudbu neumí, ale některé aplikace třetích stran to umí, takže asi to nějak jde. Těžko říct. Chtěl bych mít vše na jednom místě, ale nějaké Google Music bude nejspíš pro tento konkrétní účel vyladěnější. [I když...](http://content.fczbkk.com/preco-som-zrusil-predplatne-google-music/) Otázkou zůstává, jak toto úložiště propojit s nějakým řešním výše.
- **Vlastní disk, NAS:** To mám teď, ale je s tím práce navíc. Takový Dropbox by právě bez starostí vyřešil nejspíš všechny důvody, proč NAS mám, takže jsem uvažoval, že to na něj přesunu a NASu se spíš nakonec zbavím. Jasně, i NAS si můžu nasdílet někam do práce, ale budu já ho otevírat do světa, nastavovat zabezpečení, atd.? Nebudu. Budu já si pořád hrát s nějakým polofunkčním NFS nebo Sambou, abych to vůbec připojil k počítači? Nebudu. Dostanu se k datům, když zrovna nemám kontrolu nad routerem a není kam NAS síťově připojit? Nedostanu - připojit můj typ přímo přes USB nelze. Peču na to. To jsou přesně věci, co mě nebaví řešit. Spálil jsem se a chci od toho utéct, jak rychle to jen půjde.

## Nějaké rady? Zkušenosti?

Přijde mi zvláštní, že je toto stále v kategorii vesmírných vymožeností. Dnes, kdy má každý průměrný amík, jakožto zástupce nejsilnějšího trhu, všechno pěkně v cloudu a má k tomu doma deset zařízení. Nejspíš si nikdo nepouští hudbu jako já (nahlas a pro všechny, bez sluchátek), nebo nikoho (při dnešních možnostech!) neštve chodit/slézat někam, aby otočil hlasitost. Nebo si koupili roztrojku na audio kabel, jeho konce rozvedli do všech částí bytu a nevadí jim, že když si pouští Nirvánu a po tabletu při tom šmatlají Angry Birds, tak jim z toho čouhá šňůra. Nebo... nebo fakt nevidím nějaké zřejmé skutečnosti? Třeba je řešení strašně jednoduché a já to nesmyslně komplikuji. Pevně věřím že jo, protože to by vlastně byla skvělá zpráva :)
