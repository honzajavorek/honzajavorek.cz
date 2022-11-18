Title: Týdenní poznámky: Po uši ve frontendu
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False
Twitter-Comments: https://twitter.com/honzajavorek/status/1283827499298938881
Facebook-Comments: https://www.facebook.com/10156592446432707/posts/10158301883642707


Utekl další týden (13.7. — 17.7.) a tak [stejně jako minule]({filename}/2020-07-10_tydenni-poznamky-novy-cenik-menu-vizitky.md) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({static}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


Tento týden jsem hlavně ladil všechno možné na frontendu JG:

- Přidal jsem [Michala Špačka](https://www.michalspacek.cz/) do [seznamu podporovatelů](https://junior.guru/donate/#sponsors), juchů!
- Dvě mentorovací sessions.
- V pondělí se zákazníkům nerozeslaly e-maily se statistikami. Příčinou bylo, že se prostě vůbec nespustil nightly build. Nevím proč, asi chyba v ~~Matrixu~~ CircleCI. Pustil jsem to ručně a bylo vyřešeno.
- Upravil jsem dobu, od které začnou maily varovat, že inzerát vyprší. Bylo tam 7 dní, ale maily se posílají vždy v pondělí. Kdyby inzerát vypršel za 8 dní hned v úterý potom, přišel by recruiterovi mail s varováním jen den předem. To mi přišlo málo. Zase když budou dostávat ta varování opakovaně, tak se bojím, že budou mít _notification fatigue_. Uvidím, no.
- [Dan Srb](https://coreskill.tech/) důsledně prošel celou [stránku pro firmy](https://junior.guru/hire-juniors/) a poslal mi hromadu připomínek. Některé jsem jedno celé dopoledne opravoval, k některým jsem se ještě nedostal, každopádně díky!
- [Michal Wiglasz](https://twitter.com/kacer/status/1281662611352887302) i Dan mi pomohli odladit poskakování skrývacího menu. Zase jsem ho trochu předělal a teď už snad žádné problémy nemá. Předešlá věta moc dobře neilustruje, jak moc jsem se s tím nadřel, takže: NADŘEL.
- Celkově jsem laděním hlavičky a frontendu strávil vlastně několik dní. Vždy jsem něco opravil a tím jsem vytvořil 5 bugů a ty jsem pak opravil a vytvořil 5 nových :D
- Spadl mi CircleCI build, který [hlídá frontend JG pomocí Lighthouse]({filename}/2020-05-11_monitoring-performance-with-lighthouse-and-circleci.md). Opravil jsem tedy na pár věcí. Přečetl jsem si, [jak se dělají neblokující skripty](https://www.vzhurudolu.cz/prirucka/html-script) a poladil jsem to. Doplnil jsem `alt="text"` k některým obrázkům.
- Přidal jsem do proužku v menu odkaz na obsah stránky. Mám s ním další plány, ale zatím jen kotvou vede na obsah tak jak už na JG v minulosti byl. Do budoucna mám vymyšleno, že na širším displeji bude napravo od textu permanentní ToC (_table of contents_) a na mobilech že by se to dalo nějak rozkliknout právě přes ten Obsah odkaz.
- Abych mohl pokračovat a vrtat do layoutu stránky kvůli ToC, zjistil jsem, že nejlepší bude, když převedu co nejvíce věcí ze starých špaget do [BEMu](https://www.vzhurudolu.cz/prirucka/bem). A tak jsem převáděl. A protože jsem měl dny rozkouskované schůzkami, cvičením, mentorováním a pitím piva na [Pyvu](https://pyvo.cz/praha-pyvo/), tohle už jsem dělal v mezičasech celý zbytek týdne.
- V proužku v menu se objevuje vždy aktuální nadpis podle scrollování. Odladil jsem ho tak, aby se vyrovnal i s tím, pokud je fakt dlouhý a nevleze se do proužku (třeba na malém mobilu). Klíčové CSS: [text-overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow), [white-space](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space)
- Už teď se při najetí myší na odkaz v rámci jedné stránky na JG objevil _tooltip_, který upozornil, že se jedná jen o skok v rámci téže stránky (selektor `a[href^="#"]`). Rozšířil jsem tuto navigační pomoc a přidal podobný _tooltip_ i k odkazům, které míří jinam na JG a nejsou externí (selektor `a[href^="/"]`). Oba tyto typy odkazů jsem navíc zkusil ještě jemně odlišit od externích odkazů vlastností [text-decoration-style](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration-style). To by mohlo pomoci odkazy rozlišit a lépe se v textu orientovat lidem, kteří jsou na mobilu, protože ti žádný _tooltip_ nemají. Je hodně nová, ale o nic nejde - ve starších prohlížečích to bude prostě vypadat stejně jako jakýkoliv jiný odkaz.
- Heroku mi napsalo, že vypne moje dva projekty na staré infrastruktuře. Jeden už jsem dříve přesunul na [Vercel](https://vercel.com/), druhý byl táborový web. Tábor už web nepotřebuje a [kód je archivován na GitHubu](https://github.com/taborprekvapeni/taborprekvapeni.cz). Řekl jsem si ale, že než to definitivně shodím, zaarchivuju i statické HTML tak, jak v tento okamžik je. To jsem udělal přes [HTTrack](https://www.httrack.com/) a vytvořil druhý repozitář, [kam jsem zaarchivoval HTML](https://github.com/taborprekvapeni/taborprekvapeni.cz-static). Udělal jsem i screenshot (vestavěná funkce Firefoxu) a dal jej do README, kdybych se chtěl někdy oddávat nostalgii. Pak jsem smazal vše co mám na Heroku a doménu přesměroval na FB stránku tábora.
- Ve čtvrtek před koncem šichty mi zbyla půlhoďka a nechtělo se mi už začínat nic velkého, tak jsem vytáhl nějakou blbost ze dna backlogu. Nelíbil se mi font v náhledech pro sociální sítě. Ty se generují jako obrázky na CircleCI a tam je samozřejmě nějaký spartánský Linux, takže text byl nějakým škaredým (ale jistě zcela svobodně licencovaným!) fontem. Na netu výsledky hledání nic moc, ale pak jsem našel jednoho (jediného) dalšího zoufalce, který řešil (a vyřešil) podobný problém a v jeho CircleCI konfiguraci byla instalace fontů. Takže jsem to nemusel vymýšlet, jen jsem [obšlehl ty tři magické řádky](https://github.com/honzajavorek/junior.guru/commit/1d024b969a3f7cc1b059973c111b055153a721a1) a bylo to, balík `ttf-mscorefonts-installer` nainstalován, font o dost hezčí. Asi je to teda nějaký Arial nebo co, a ne Helvetica, ale na Linux dobrý.
- Účastnil jsem se schůzky [PyLadies](https://pyladies.cz/) s jednou korporací, která by chtěla pomoct s otevřením třetího běhu začátečnického kurzu v Praze.
- Konečně jsem v [KB5](https://www.kb5.cz/) zvedl 32 kg na [TGU](https://duckduckgo.com/?t=ffab&q=turkish+get+up&iax=images&ia=images).
- Vzhledem k mému tempu i okurkové sezóně se pomalu ale jistě přikláním k tomu, že příručku uveřejním 1.9.

Další poznámky budou až za dva týdny.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({filename}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

- [The Wrong Abstraction — Sandi Metz](https://www.sandimetz.com/blog/2016/1/20/the-wrong-abstraction)<br>“Prefer duplication over the wrong abstraction” aneb vakcína na vir s názvem DRY
- [The Walkman, Forty Years On](https://www.newyorker.com/culture/cultural-comment/the-walkman-forty-years-on)<br>Jak Walkman změnil způsob, jakým lidé vnímají hudbu — a jak se Applu podařilo stát se Sony
- [Apolena Rychlíková: Bydlení není komodita, ale potřeba. Bez narovnání trhu se jeho dostupnost nezlepší](https://t.co/CTkvLndfY3?ssr=true)<br>Bydlení jako investice likviduje bydlení jako lidskou potřebu
- [Etcd, or, why modern software makes me sad](https://www.roguelazer.com/2020/07/etcd-or-why-modern-software-makes-me-sad/) Nedokážu posoudit, nakolik je pravdivý, ale dokážu si představit, že feature-creep do OSS projektů na základě specifických požadavků korporací je běžná věc. Na VŠ jsem HTTP server v C++ napsal, HTTP2 bych už nedal.
- [Nejhnusnější nádraží v zemi i developerský gulag. Místa v Brně, která musíte vidět](https://magazin.aktualne.cz/cestovani/jsou-mesta-ktera-jsou-zajimava-vsim-a-pak-je-brno-novy-pruvo/r~4621042ac4e611ea8972ac1f6b220ee8/?utm_term=Autofeed&utm_medium=Social&utm_source=Twitter#Echobox=1594786106)”
- [Komentář: Internet nemůže být tabu. Škola se po krizi musí změnit](https://www.seznamzpravy.cz/clanek/komentar-internet-nemuze-byt-tabu-skola-se-po-krizi-musi-zmenit-112615)<br>“Škola se snaží připravovat děti na situaci, v níž nebudou mít internet na dosah. Přitom jedinou takovou situací je dnes v jejich životě jejich škola. Reálný svět už nikoli.”
- [Romové nemají šanci si pronajmout byt. Romská rodina nabízí pět nájmů dopředu, realitky se vymlouvají na majitele bytů](http://www.romea.cz/cz/zpravodajstvi/domaci/romove-nemaji-sanci-si-pronajmout-byt.romska-rodina-nabizi-pet-najmu-dopredu-realitky-se-vymlouvaji-na-majitele-bytu)<br>“Každý svého štěstí strůjcem,” že? No, jenom když máte tu správnou barvu kůže.
- [Rok 2020 bude nejteplejší v dějinách. A ani poté to nebude lepší](https://www.seznamzpravy.cz/clanek/rok-2020-bude-nejteplejsi-v-dejinach-a-ani-pote-to-nebude-lepsi-111707)<br>Jo, prší, ale to neznamená, že oteplování nepokračuje a nebudou zase velká sucha.
- [Building a self-updating profile README for GitHub](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/)<br>GitHub nově umožňuje udělat si “osobní README” na profilu. Dá se s tím vyhrát a lidi už s tím všelijak blbnou. Návod jak začít tady u Simona.

<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
