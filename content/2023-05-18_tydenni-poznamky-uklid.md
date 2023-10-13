Title: Týdenní poznámky: Úklid
Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
Lang: cs
Tags: týdenní poznámky, junior.guru
Telegram-Comments: https://t.me/honzajavorekcz/210

Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
Od [posledních poznámek]({filename}2023-05-12_tydenni-poznamky-katalog-kurzu-a-uklid-v-trellu.md) už utekl nějaký ten týden (12. 5. až 18. 5.), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

<div class="alert alert-warning" role="alert" markdown="1">
**Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
Aktuální nabídky práce pro juniory: [Glance Media](https://junior.guru/jobs/b5bb05d439c71b800ca520b63c5ae9ab261d10d19681ff2bc2acce0c/), [Processand](https://junior.guru/jobs/dbbb7bf406b3c33aeba36cae817919d44bfb368a08fb1b4899dba130/), [Red Hat](https://junior.guru/jobs/ade40e530211c36a309fa370d270da7650ad18462c03c95b0b38de57/)

**Plány:** Četli jste, co [letos plánuji]({filename}2022-12-26_strategie-na-2023.md)?
Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
</div>

Poznámky píšu už ve čtvrtek, protože v pátek si beru volno a jedu na prodloužený víkend na kolo s kamarády.

## Shánění kanceláře

Hned na pondělí jsem si sjednal dvě schůzky ohledně kanceláře na Žižkově.
Na obchůzky jsem se vydal s dvouletou dcerou a kvůli vlastní prokrastinaci asi o hodinu později, než jsem potřeboval, takže _what could possibly go wrong_.
Jednu schůzku jsem zvládl a stihl, i když z ní dcera nebyla zrovna nadšená a musel jsem jí to pak vynahradit hraním na písku.
Jednu schůzku jsem vůbec nezvládl a nestihl, třikrát jsem se za to omluvil a doteď se stydím, ale tak snad už dobrý.

Ta první schůzka naštěstí vedla k nějakému výsledku.
Vypadá to, že jsem kancelář našel.
Ještě se tam v pondělí znova podíváme i s kamarádem a pak to snad už definitivně potvrdíme.
Doma se pracovat fakt už moc nedá.


## Úklid kolem příručky

Pokračoval jsem v úklidu Trella, jak jsem ho už popisoval v předchozích poznámkách.
Dodělal jsem poslední sloupec, kde bylo přes 500 kartiček.

Pak jsem si šel odpočinout a předělal jsem [tohle](https://junior.guru/open/#prirucka) z tabulky na graf.
O dost přehlednější!

![Graf]({static}/images/screenshot-2023-05-18-at-17-11-20.png){: .img-thumbnail }

Na řadu přišel úklid v uložených zprávách na Discordu.
Napadlo mě, že tohle už by šlo nějak zautomatizovat.

Přiřadil jsem ke každé stránce v příručce unikátní emoji.
Pak mám skript, který projede všechny zprávy z klubu, které jsem si nechal botem uložit do soukromé konverzace.
Pokud má zpráva reakci s určitou emoji, uloží se obsah zprávy a odkaz na zprávu do poznámek v souboru pro danou stránku příručky.
Asi to zní zmateně, tak třeba to půjde pochopit aspoň z obrázků:

![Uložené zprávy]({static}/images/screenshot-2023-05-18-at-13-14-50.png){: .img-thumbnail }
Takhle vypadají uložené zprávy, kterým přiřazuji emoji.

![Skript]({static}/images/screenshot-2023-05-18-at-13-16-58.png){: .img-thumbnail }
Projedu skriptem a ten mi zprávy roztřídí a uloží do komentářů ve zdrojových souborech příručky.

![Příručka]({static}/images/screenshot-2023-05-18-at-13-18-08.png){: .img-thumbnail }
Modifikované soubory, kam přibyly nové poznámky.

![Hotovo]({static}/images/screenshot-2023-05-18-at-13-17-40.png){: .img-thumbnail }
Zpracované zprávy skript označí, aby je pak už neřešil.

Nejsložitější bylo vymyslet, jak to má fungovat.
[Výsledný skript](https://github.com/honzajavorek/junior.guru/blob/a1044b12c619b22af7079a3361750f470e051e2f/juniorguru/cli/notes.py) je už celkem jednoduchý a napsal jsem ho rychle.

Prošel jsem pak na Discordu přes 200 uložených zpráv a přiřadil jim emoji podle kapitol příručky, ke kterým si je chci přidat do poznámek.
Skript mi je uložil a tím je to celé hotovo.

Když si budu v budoucnu ukládat nějaké zprávy na Discordu, stačí je pak v soukromé konverzaci roztřídit pomocí emoji a spustit zase skript.
Jen je škoda, že Discord má omezený počet emoji, takže je tam nemůže bot předchystat, v příručce už je příliš mnoho stránek.
Musím je vždy hledat a dávat ručně.

I tak to ale bude velký posun k organizovanějším poznámkám kolem příručky a věřím, že mi tohle pomůže psát nové kapitoly rychleji a efektivněji.


## Stable Diffusion

Ve volném čase si pořád ještě hraju se Stable Diffusion a stále studuju nové techniky a zahazuju staré. Akorát pro pracovní věci je mi to k ničemu, je to jen relax.

I když jsem objevil i LoRA, které dokázaly generovat docela konzistentní ilustrace v určitém stylu a to jsem si už říkal - aha, tohle by se dalo využít na webu. Ten si ilustruju sám, ale je to vždycky strašná práce. Mohl bych ty ilustrace generovat a byly by kvalitní a po celém webu konzistentní. Příklady:

- [Pen and ink](https://civitai.com/models/51458/pen-and-ink)
- [Watercolor](https://civitai.com/models/56082/watercolor-painting-vizsumit-or-lora)
- [Wood](https://civitai.com/models/45058)
- [Fashion watercolor](https://civitai.com/models/65466/fashion-watercolor)

![Fashion watercolor LoRA]({static}/images/screenshot-2023-05-18-at-18-48-51.png){: .img-thumbnail }

Ten poslední styl si úplně umím představit jako generátor ilustrací k článkům Heroine.cz třeba.
Škoda, že [se chystá legislativa](https://technomancers.ai/eu-ai-act-to-target-us-open-source-software/), která má open source modely a podomácku vyrobené LoRA naprosto zničit a rozprášit.
Asi je to [jediný způsob](https://simonwillison.net/2023/May/4/no-moat/), jak zajistit, že AI bude pěkně zregulované, v rukou monopolů, které na to mají dost peněz, a ne že si s tím bude hrát každý doma na noťasu.

V příští verzi AUTOMATIC1111 UI bude už [tomesd](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/9256), nový způsob jak zrychlit generování větších a náročnějších obrázků.
Díval jsem se na nějaký [neoficiální build UI vyladěný přímo pro macOS](https://github.com/brkirch/stable-diffusion-webui/releases), ale nepozoroval jsem žádné zrychlení, tak jsem to zase smazal.
Kdo máte intelovský MacBook, kde AUTOMATIC1111 UI vůbec nefunguje, tak to ale zkuste, možná to díky tomu rozjedete.

Celkově mi ale trochu docházejí nápady a prvotní nadšení opadlo.
Nemám na to ani už tolik času.
Možná to nechám chvíli ležet a počkám, až přijde zas nějaká inspirace.


## Další

-   Prošel jsem připravovanou anketu, kterou chystá [Nela](https://www.nelaprovazi.cz/), a dal jí na to feedback.
-   Byl jsem na Pyvu, srazu Pythonistů.
    Jedna z věcí, které mě tam zaujaly, je, že [Apify mají nově podporu pro Python](https://docs.apify.com/sdk/python/).
    Pecka!
    Nutnost psát scrapery v JavaScriptu mi bránila to na cokoliv použít.
    Pamatuju si, že jsem to kdysi zkoušel a fakt jsem se snažil, ale vzdal jsem to a napsal jsem si scrapery sám v Pythonu.
-   Další firma mi napsala, že neprodlouží o rok partnerství.
    Šetří.
    Chápu.
    Nebylo to moc peněz, tak to není velká tragédie, ale trend je asi jasný.
-   Dal jsem na web proužek, že mají lidi hlasovat pro Junior Guru podcast v anketě [podcastroku.cz](https://www.podcastroku.cz/).
-   Kamarád mě upozornil na [kill-the-newsletter](https://github.com/leafac/kill-the-newsletter), věc, která umožňuje odebírat newslettery pomocí RSS.
    Ani bych si to [nemusel hostovat sám](https://kill-the-newsletter.com/).
    Ale neměl jsem ještě čas se na to vlastně podívat.
-   Naučil jsem se používat [tagy ve Finderu na macOS](https://support.apple.com/guide/mac-help/tag-files-and-folders-mchlp15236/mac).
    Zajímavá fičurka!
    Kolem Stable Diffusion je asi pět různých složek, kam se potřebuji pravidelně přepínat.
    Otagoval jsem si je a mám je všechny rychle přístupné.
    Cool.
-   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
-   Během 7 dní jsem při procházkách nachodil 5 km, ujel na kole 15 km. Celkem jsem se hýbal 7 h a zdolal při tom 20 km.
    Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

<div class="alert alert-warning" role="alert" markdown="1">
**Okénko duševního zdraví:**
Máte dojem, že na rozdíl ode mně nic nestíháte?
Buďte v klidu, [není to závod]({filename}2020-06-04_neni-to-zavod.md)!
</div>

## Plánuji

1. Psát novou stránku v příručce: Jak si vybrat kurz
2. Napsat různým lidem a firmám různé maily.
3. Vylepšit vítání členů v klubu a přeskupit v klubu zase trochu kanály.

## Zaujalo mě

Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
Od posledních poznámek jsem sdílel:

- [Your job is (probably) safe from artificial intelligence](https://www.economist.com/finance-and-economics/2023/05/07/your-job-is-probably-safe-from-artificial-intelligence)<br>Fakt hodně dobrých postřehů (vycházejících z různých studií). Ochutnávka: „The biggest corporate winner so far from the new ai age is not even an ai company. At Nvidia, a computing firm which powers AI models, revenue from data centres is soaring.“ „Smartphones have been in widespread use for a decade, billions of people have access to superfast internet and many workers now shift between the office and home as it suits them. Official surveys show that well over a tenth of American employees already work at firms using ai of some kind, while unofficial surveys point to even higher numbers. Still, though, global productivity growth remains weak.“ „Blue-collar work, such as construction and farming, which accounts for about 20% of rich-world gdp, is one example. An llm is of little use to someone picking asparagus.“ „It is even possible that the ai economy could become less productive. Look at some recent technologies. Smartphones allow instant communication, but they can also be a distraction. With email you are connected 24/7, which can make it hard to focus.“
- [Is Chinese power about to peak?](https://www.economist.com/leaders/2023/05/11/is-chinese-power-about-to-peak?utm_medium=social-media.content.np&utm_source=twitter&utm_campaign=editorial-social&utm_content=discovery.content)<br>„Beijing’s economic power may be peaking, but no other country is so capable of challenging America globally“
- [Strejček: Beru velké prachy za debilní ilustrace, umělé inteligence se nebojím, i když většina lidí půjde od válu - Prostor X podcast — Prostor X](https://overcast.fm/+Wv2QlvpYA)<br>Fajn rozhovor s výtvarníkem. Sebere mu Stable Diffusion práci?
- [Právo samosprávy na sebedestrukci. Obce nestíhají plánovat rozvoj a krotit developery, škody jsou trvalé - VOXPOT](https://www.voxpot.cz/pravo-samospravy-na-sebedestrukci-obce-nestihaji-planovat-rozvoj-a-krotit-developery-skody-jsou-trvale/)<br>„Praha přímo sousedí s katastry zhruba 40 obcí. Téměř 500 jich pak leží v prstenci označovaném jako Pražská metropolitní oblast. V České republice je celkem 6254 obcí, nejvíce na obyvatele v celé Evropské unii. Každá z nich si schvaluje územní plán sama. Prostor pro korupci či i legální ovlivňování postojů veřejnosti a zastupitelů – například skrze sponzorské dary chudým obcím či místním spolkům – je tak obrovský.“
- [Poland will be wealthier than Britain by 2030 – it’s time we took notice](https://www.telegraph.co.uk/business/2023/05/07/poland-europe-superpower-communism-putin-military/)<br>„What this means is that Poland may well soon possess the largest and best land fighting capabilities of all the European members of Nato. Even France, with only some 200,000 front-line troops, may soon find itself outnumbered by Poland.“ „Adjusted for purchasing parity, GDP per head in Poland is now £28,200 compared with £35,000 in the UK, £34,200 in France and £39,800 in Germany. At its current trajectory rate, Poland will overtake the UK by 2030.“
