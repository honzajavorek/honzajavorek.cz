Title: Týdenní poznámky: Rýmička a menu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False
Twitter-Comments: https://twitter.com/honzajavorek/status/1279105167753973764
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158264382662707


Utekl další týden (29.6. — 3.7.) a tak [stejně jako minule]({filename}/2020-06-26_tydenni-poznamky-ladeni-robota-priprava-na-prirucku.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

Tento týden jsem byl poměrně nefunkční. V pondělí večer jsem zjistil, že minulý víkend cestou ze svatby jsem se asi nachladil jízdou v klimatizovaném autobuse. Úterý a středu jsem prosmrkal a proležel. Ve čtvrtek jsem už skoro i něco dělal, v pátek jsem už skoro i normálně pracoval.


## Nové menu

Menu je asi jediná opravdu podstatná věc, které jsem se tento týden zvládl věnovat. Abych mohl do JG zařadit [příručku](https://junior.guru/hire-juniors/#handbook), potřebuji flexibilnější navigaci. Už minulý týden jsem na ní začal trochu pracovat. Rozmyslel jsem si, jak by mělo nové menu vypadat, a předělal to stávající v CSS do BEMu.

Další krok byl udělat "sticky" menu, tedy takové, které by jezdilo se stránkou při scrollování. Po velké rešerši jsem zjistil, že existuje `position: sticky;` (viz [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/position)) a je to :D

Jenže když hlavička jezdí, přestanou fungovat odkazy na odstavce v rámci stránky - nadpisy skončí pod hlavičkou. Našel jsem nějaké návody jak to řešit, pěkný je třeba článek na [CSS Tricks](https://css-tricks.com/hash-tag-links-padding/). Řešení mi chvíli zabralo, protože kvůli rozklikávacím odstavcům (např. [zde](https://junior.guru/learn/#python)) mi to nefungovalo hned. Nicméně vyřešil jsem, funguje.

No a další krok byl přidat podmenu na [stránku s hledáním práce](https://junior.guru/jobs/). Měl jsem nějaký nápad, ale když jsem ho přenesl do CSS, vylezla mi z toho tahle příšernost:

![Nepovedená hlavička]({static}/images/nepovedena-hlavicka.jpg)
Takhle fakt ne!

Nuže, jal jsem se to zase celé překopat a zkoušel a experimentoval, odkoukával jak to mají třeba ve [Fakturoidu](https://www.fakturoid.cz/), a nakonec jsem došel tedy k něčemu, co se mi celkem líbilo a celkem fungovalo na počítači i na mobilu. S tím, jak teď hlavička jezdí, už nemělo moc smysl, aby horní menu bylo v podobě záložek, takže jsem jejich vizuál opustil a zkusil něco jiného. Nevím, jestli je to finální fáze, mám toho už plný oči a nechám to uležet, ale uzavírám pátek s dobrým pocitem.

![Povedená hlavička]({static}/images/povedena-hlavicka.png)
Tohle by snad šlo


## Další poznámky

-   V úterý, poslední den v červnu, jsem poslal [červnový newsletter](https://us3.campaign-archive.com/?u=7d3f89ef9b2ed953ddf4ff5f6&id=ceb91d9dd9). Od posledně se do newsletteru přidala spousta lidí. Jenže já jsem pracoval minulý měsíc hlavně na tom, aby inzerenti měli analytiku, takže nic moc nového viditelného pro juniory není a příručka ještě taky není venku. Bál jsem se, jestli od toho lidi nebudou čekat něco víc a hned se všichni zase neodhlásí. Na mé nejistotě se jistě podepsalo i to, že jsem newsletter tvořil během největšího náporu rýmičky. Nikdo se ale neodhlásil a ještě se přihlásili další :) Vysvětluju si to tak, že v novém textu při přihlašování [lidem narovinu odkazem na archiv ukazuju, co v e-mailech je](http://eepurl.com/gyG8Bb).
-   Během týdne jsem řešil hlavně e-maily. Jednak jsem měl předchozí pátek volno, takže se mi nasbíraly i z minulého týdne, jednak jsem pak dva dny proležel, takže se nasbíraly zase. K tomu jsem i rušil různé věci, kam jsem se měl dostavit.
-   Za [Pyvec](https://pyvec.org/) jsem prodloužil doménu [pyworking.cz](https://pyworking.cz/). Všechny naše domény [jsou v dokumentaci zde](https://docs.pyvec.org/operations/domains.html).
-   Na [python.cz](https://github.com/pyvec/python.cz/) se nám rozbil build. Protože je to staticky generovaná stránka, tak stále fungovala, ale neaktualizovala se. Tři měsíce si toho nikdo nevšiml, jelikož hlavní věc, která se tam aktualizuje, je kalendář akcí, a akce žádné nebyly :D [Petr Viktorin](http://encukou.cz/) si našel čas to opravit, za což mu děkuji, a já jsem na jeho PR udělal aspoň review.
-   V souvislosti se spraveným buildem na python.cz jsem tam s pomocí [@dependabot](https://dependabot.com/) upgradoval závislosti.
-   Finalizoval jsem s [PrintAll](http://www.printall.cz/) podobu JG vizitek a schválil je k tisku.
-   Zvažoval jsem, jestli se přidám jako [mentor](http://bit.ly/fpmentors) do [Femme Palette](https://www.femmepalette.com/). Dost se mi to líbilo, ale nakonec jsem to odmítl, protože teď nemám kapacitu dělat moc _pro bono_ věcí. Možná až se JG trochu víc rozjede. Pokud kapacitu máte, napište jim!
-   Zkritizoval jsem někomu inzerát na seniora, který jeho tým vypsal a nedaří se jim na něj nikoho ulovit. Za odměnu jsem z něj vytáhl kontakty na recruitment v jejich firmě, které mohu použít k pokusu nabídnout JG :)
-   Můj skript na kontrolu nefunkčních odkazů opět vyžadoval nějakou pozornost. Zjistil jsem, že LinkedIn a Twitter nyní asi nově detekují HTTP požadavky z CI a hromadně je blokují. Od určité chvíle vždy všechny odkazy na tyto služby skončily buď s HTTP kódem 999 (způsob jakým dává prostředníček LinkedIn) nebo [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (prostředníček od Twitteru). Je škoda, že stále více webů blokuje kdejaký obyčejný HTTP požadavek a člověk si pak ani nemůže zkontrolovat, jestli má platné odkazy. To je furt něco, už mě to moc nebaví. Každopádně jsem tedy musel dát oboje do vyjímek.
-   S velkou firmou, se kterou pracuji na _dealu_ jsem měl jeden neoficiální videohovor a předběžně je to na dobré cestě. Bude potřeba ale doladit ještě způsob, jakým předplatné funguje. Chtěl jsem to dořešit do konce týdne, ale nějak jsem na velké kalkulace neměl energii. Když jsem nabyl nových sil, utopil jsem je raději v CSS a toto nechal na příští týden, až budu zcela čerstvý.
-   Přečetl jsem si, že podle [Digital Economy and Society Index Report 2020](https://ec.europa.eu/digital-single-market/en/human-capital) vydaného Evropskou Komisí byla v roce 2018 situace v ČR ohledně trhu s IT odborníky následující:

    > The problem is even more widespread in Romania and Czechia, where at least 80% of enterprises that either recruited or tried to recruit ICT specialists reported such difficulties.

    Uf! Ještě že už existuje [řešení](https://junior.guru/) tohoto zapeklitého problému!

-   Zjistil jsem, že existuje [český překlad slavného návodu jak se ptát](https://www.root.cz/texty/jak-se-spravne-ptat/)! Všude jsem doteď odkazoval originál a byl z toho trochu smutný. Šel jsem tedy na všechna místa na JG a třeba i do pravidel na [Pyonýrech](https://www.facebook.com/groups/pyonieri/), a všude dal odkaz na tuto českou verzi, která bude přece jen pro začátečníky o něco stravitelnější.
-   Odstranil jsem z JG sekci s koronavirovými slevami. Myslím, že je čas se v tomto ohledu posunout dál. Sekci [Co způsobí koronavirus?](https://junior.guru/learn/#covid19) jsem ale zatím zachoval. Myslím, že co doopravdy způsobí, se dovíme pořádně až napodzim, a trochu se bojím, že můžem doufat v co chcem, ale bude to celkem vítr.
-   Opravil jsem vzhled tlačítek na úvodní stránce JG. Tlačítka byla na mobilu splácnutá k sobě a celkově nehezká. Původně to tak nebylo, rozbilo se to ale už před nějakou dobou, když jsem přepisoval tlačítka do BEM a tohle nějak neodchytil.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [On Four Types of Development Companies](https://almad.blog/notes/2020/on-four-types-of-dev-companies/) Prostě — kvalitní materiál, čtěte!
- [V Čestlicích hořel vůz s elektrickým pohonem. Hasiči vložili auto na několik dní do kontejneru s vodou](https://www.irozhlas.cz/zivotni-styl/auto/pozar-elektromobilu-praha-skoda-dva-miliony-korun_2006250738_vin)<br>Jak se hasí elektromobil
- [Práce v IT na volné noze](https://navolnenoze.cz/blog/it/)<br>Vše o práci v IT na volné noze — super článek! Typy firem, projektů, jak a co, ceny, práce na dálku, korporace…
- [Tak se zrodila brněnská chobotnice](https://reportermagazin.cz/a/pLThe/tak-se-zrodilabrnenska-chobotnice)<br>Detailní popis toho, co se řeší s brněnským ANO
- [Martin Koníř (Nemocnice Na Bulovce): Chtěli jsme naši eNeschopenku uvolnit zdarma. Prý bychom ale okradli stát](https://www.lupa.cz/clanky/martin-konir-nemocnice-na-bulovce-chteli-jsme-nasi-eneschopenku-uvolnit-zdarma-pry-bychom-ale-okradli-stat/)<br>IT v nemocnici
- [Minitel: Francie znala online porno i nákupy už v 80. letech](https://finmag.penize.cz/ekonomika/417602-minitel-francie-znala-online-porno-i-nakupy-uz-v-80-letech)<br>O francouzském předchůdci internetu - vůbec jsem neznal!
- [Demagog slouží jako PR alibistického Facebooku](https://www.mediar.cz/demagog-slouzi-jako-pr-alibistickeho-facebooku/)<br>Jak Facebook ve skutečnosti s desinformacemi nebojuje
- [KOMENTÁŘ: Proč české děti nesnáší češtinu aneb na prahu druhého obrození](https://www.idnes.cz/zpravy/domaci/cesky-jazyk-cestina-vzdelavani-deti-zaci-ucitele.A200630_202921_domaci_aug)<br>Perfektní filipika proti klasické výuce češtiny

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
