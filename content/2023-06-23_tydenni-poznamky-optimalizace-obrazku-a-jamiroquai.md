Title: Týdenní poznámky: Optimalizace obrázků a Jamiroquai
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-06-16_tydenni-poznamky-strakovka-podcast-inboxy.md) už utekl nějaký ten týden (16. 6. až 23. 6.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Red Hat](https://junior.guru/jobs/aac817ee027512f150caf872e149e12ef9246815b1ecf880501b877d/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

O víkendu jsem byl s kamarády na chatě a vším, co jsem tam dělal, ať už to bylo požívání, běh, či tanec, jsem se zničil natolik, že jsem se z toho dostával až do úterního večera.
Sešlo se to navíc s tím, že dceři rostly zuby, takže jsem nemohl nic v noci dospat a byla to úplná krize.

Do toho různí doktoři a jiné pochůzky.
V pondělí jsem šel na první návštěvu k psychiatrovi kvůli diagnostice ADHD.
Byl to fajn pokec, ale ještě budeme mít několik sezení, než vydá verdikt.

Ve čtvrtek jsme šli se ženou na Metronome festival.
Cílem bylo sejít se s kamarády z Brna a vidět Jamiroquai, ale stihli jsme i Auroru a trochu Aiko.
PSH jsme vzdali, protože budova, kde hráli, měla příšernou akustiku.
Zvuk bolel v uších a ze slov nebylo rozumět nic, což zrovna u rapu celkem vadí.

Bylo to poprvé od narození dcery, co jsme se s manželkou takhle pozdě večer někam vypravili.
Babička přijela z Moravy a statečně se pokusila o uspání dítěte, které bez nás ještě nikdy neusnulo.
A povedlo se to!
Nám se zase pro změnu povedlo vyhnout se nějaké té příšerné bouřce, která se řítila na Prahu z Německa.

![Jamiroquai]({static}/images/img-4309.jpg)

Tím se uzavírá můj divoký červen, do něhož se mi z důvodů koordinace všelijakých termínů vložily prakticky veškeré aktivity, které jsem chtěl letos v létě dělat.
Jsem z toho poměrně vyčerpaný a těším se, že budu mít konečně nějaký týden, kdy budu jen v práci nebo doma.
Myslím, že junior.guru se těší taky, protože teď bylo celkem zanedbáváno 😞

## Přednáška s Nelou

V úterý večer byla v klubu po dlouhé době opět přednáška.
Poprvé jsem si ji chtěl vzít z nové kanceláře.

Minuty před začátkem jsem však zjistil, že byť mi jede Discord na chat, nejede mi na zvuk a video.
Nepřipojí se.
Naštěstí byl v kanceláři zrovna kamarád [Míla](https://milavotradovec.cz/) s neomezeným internetem v mobilu a připojil mě přes LTE.
Z toho jsem vzal nakonec celou přednášku.
Co bych bez něj v tu chvíli dělal, to upřímně nevím.
Takže Mílo, ještě jednou fakt díky!

Další den jsme to pak vyřešili.
Discord potřebuje na volání nějaké porty, které byly blokované na místním routeru.

Nela měla pomalejší tempo vyprávění, ale jinak proběhlo všechno v pohodě.
Přednáška to byla hezká, diskuze výživná.
Záznam bude veřejný a dáme ho pak zase na stránku [Psychika na cestě do IT](https://junior.guru/handbook/mental-health), ale nejdřív musí Tinuki dokončit jeho stříhání ✂️

![Nela]({static}/images/20230620-8831c9f9d7408f8d23462a58fa6d6c0278db3046d79cbabb3f069d0cfdadf644-yt.png){: .img-thumbnail }

## Optimalizace obrázků

Během týdne jsem se nepříjemně zamotal do optimalizace obrázků na junior.guru.
Přemýšlím, že bych generované obrázky commitoval zpět do repozitáře, aby se tím kešovaly a nevytvářely pokaždé znova.
Jednak se příliš nemění, občas akorát nějaký přibude, jednak jejich generování trvá dost dlouho.

Jenže aby nezabíraly v Gitu moc místa, chtěl jsem je mít co nejmenší.
A to lze docílit jen optimalizacemi.
Jde o celkem dost obrázků a bude jich jen přibývat, takže rozdíly jsou v MB, možná desítkách MB, a to už se po čase při `git pull` pozná.

Napadlo mě, zda bych se nemohl na všechny optimalizace vyprdnout a prostě použít třeba WebP, který má určitě vše už vyřešené.
U screenshotů měl oproti JPEG celkem dobré výsledky, tak jsem to předělal.
U generovaných PNG to ale nevycházelo líp a hlavně nejde WebP přetáhnout např. jako obrázek ke statusu na LinkedIn, což je pro mě problém.

[Pillow má option](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png) `optimize`, což jsem nevěděl, napověděl mi to při psaní GitHub Copilot. Moc velkou parádu to však neudělalo.

Hodně se mi líbil [pngquant](https://pngquant.org/) v kombinaci s [oxipng](https://github.com/shssoichiro/oxipng).
Prakticky nerozeznatelné PNG mělo místo 300 kB třeba jen 70 kB.
Jenže se mi nějak nepovedlo to jednoduše dostat na CI.
Vyžadovalo to instalaci přes `apt-get`, což je vždy opruz a čas buildu navíc, a taky se mi nepovedlo najít adekvátní balíček pro oxipng.
Hledal jsem, zda by to nešlo udělat nějak nativně v Pythonu a našel toto:

- [pyoxipng](https://github.com/nfrasser/pyoxipng)
- [Pillow quantize()](https://github.com/python-pillow/Pillow/pull/1889): `image.quantize(method=Image.Quantize.LIBIMAGEQUANT)`
- Omezení palety pomocí Pillow: `image = image.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)` Jenže jak je to jen 256 barev, tak to bylo dost hnusné.

Několik dní jsem se v tom motal a zkoušel různá řešní.
Ten `pyoxipng` mi třeba fungoval krásně lokálně, ale na CI se záhadně zasekával.

Nakonec jsem to vzdal a obrázky se generují neoptimalizované.
Budu jejich velikost muset řešit jinak.
Buďto je zmenším před commitem lokálně, nebo je nebudu commitovat, ale využiju třeba [CircleCI cache](https://circleci.com/docs/caching/), nevím.
Každopádně mám pocit, že na to, jaká je to blbost, jsem v tom utopil strašně moc času.

Aspoň se mi povedlo na několika místech výrazně zrychlit generování obrázků i jinak:

-   Místo dočasného adresáře pro každý generovaný obrázek se používá jeden jako sdílená keš.
-   Místo toho, aby se pokaždé kompilovaly SCSS soubory a kopírovaly se fonty, děje se to jen jednou.
-   Místo toho, aby se SCSS kompilovalo ručně, pak se ručně kopírovaly fonty a přepisovaly jejich cesty, dělá to teď speciálně nastavený `esbuild`.

Ten poslední bod mě potrápil, protože `esbuild` se rozbije o relativní cesty k fontům v balíčku [@fontsource/inter](https://www.npmjs.com/package/@fontsource/inter).
Procházel jsem nějaké pluginy, ale nakonec je řešením `precompile` přímo v rámci [SCSS pluginu](https://github.com/glromeo/esbuild-sass-plugin):

```js
await esbuild.build({
  ...
  plugins: [
    sassPlugin({
      precompile(source, pathname) {
        if (pathname.endsWith('@fontsource/inter/index.css')) {
          return source.replaceAll('./files/', '../../node_modules/@fontsource/inter/files/')
        }
        return source
      },
    }),
  ],
})
```

Taky jsem při ladění nejrůznějších problémů dost překopal jak mi funguje logging.
Objevil jsem třeba [record_factory](https://stackoverflow.com/a/57820456/325365), pomocí níž si loguji z jakého procesu je záznam, ale pouze pokud není v tom hlavním.
Zrušil jsem logování do souboru, protože ho nepoužívám, a přidal jsem si `--debug` do CLI, které zapne detailnější logování.

## Další

-   Pomáhal jsem [PyCon CZ](https://cz.pycon.org/2023/) týmu propagovat [možnost přihlásit si na letošní konferenci přednášku nebo workshop](https://cz.pycon.org/2023/cfp/).
    Výzvu jsem dal do asi desítky Facebookových skupin, ale zdá se mi, že nakonec ze všeho nejvíc frčí [můj status na LinkedIn](https://www.linkedin.com/posts/honzajavorek_python-cfp-pyconcz-activity-7077574515693645824-WkJA).
    Vyhodnocuji si z toho pro osobní účely, že Facebook je už asi opravdu mrtvý.
-   Sdílel jsem [status Kateřiny Lesch](https://www.linkedin.com/posts/kveselovska_16-kate%C5%99ina-lesch-deloitte-o-um%C4%9Bl%C3%A9-inteligenci-activity-7071741104039047168-IxR-/) o tom, že byla u nás v podcastu.
-   Přihlásil jsem se na podzimní půlmaraton v Blansku a nejspíš na jednu letní šifrovačku v Brně.
-   Opravil jsem nějaké malé chybky na junior.guru.
    Rozbité cesty k souborům, špatně generované adresy, atd.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
    Od dovolené jsem ještě stále ve skluzu co se týče čtení klubu.
-   Během 8 dní jsem naběhal 19 km. Celkem jsem se hýbal 3 h a zdolal při tom 19 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1.  Věnovat se v klidu rodině a práci a nic dalšího 🙏
2.  Dohnat všechny možné resty z posledních týdnů.
3.  Nějak uzavřít překopávání toho, jak se buildí frontend junior.guru.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
Od posledních poznámek jsem sdílel:

- [Call for Proposals: Přihlaš si přednášku, workshop nebo sprint na PyCon CZ 23](https://www.youtube.com/watch?v=xNvvK-gPXUo)<br>A už jsem tady psal, že právě můžete poslat návrh na přednášku nebo workshop pro letošní PyCon CZ, českou Python konferenci? Letos tam bude i celá sekce pro začátečníky. Pusťte si Dana na videu, vysvětlí vám, jak to funguje 🙂 V popisku je pak odkaz přímo na formulář. A neváhejte, ten formulář nebude už otevřený moc dlouho.
- [Gaming On Mac Just Got WAY Better - A Developer's Perspective](https://www.youtube.com/watch?v=Cg1g27MUd_0)<br>Áčkové hry na macOS? Wow.
- [O Pyvci s Bárou Drbohlavovou (Rohlík.cz) — ProgramHRování - váš HR průvodce světem IT](https://overcast.fm/+1O3lj1Evs)<br>Konečně jsem si pustil tohle a super. Díky Báro za super promo pro Pyvec a Python komunitu ❤️ (jsem taky ve výboru)
- [Digital Culture Is Literally Reshaping Women's Faces](https://www.wired.com/story/flawless-korea-beauty-elise-hu/)<br>„While fixing individuals reduces prejudice directed toward particular individuals, it increases prejudice in general.“ Nebo: „We assume that desire is objective or subjective, but in reality it rests on a third party who gives value to objects. This third party is usually the one who is closest, the neighbor. When the entire internet population is your neighbor, this is a recipe for conflict.”
