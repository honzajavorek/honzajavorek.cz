Title: Jak jsem si začal hrát s generováním obrázků pomocí AI
Image: images/screenshot-2023-04-14-at-21-39-47-diffusionbee-stable-diffusion-app-for-ai-art.png
Lang: cs
Telegram-Comments: https://t.me/honzajavorekcz/187

Během Velikonoc jsem si udělal volno a během něj jsem si začal hrát se Stable Diffusion.
Jaké jsou moje první dojmy?

![DiffusionBee]({static}/images/screenshot-2023-04-14-at-21-39-47-diffusionbee-stable-diffusion-app-for-ai-art.png){: .img-thumbnail }

Do této chvíle jsem nic o generování obrázků pomocí AI nevěděl, ani bych nedokázal říct, jaký je rozdíl mezi DALL-E, Stable Diffusion, nebo Midjourney.

Procházel jsem si během volna Fireship videa, což je můj nový oblíbený kanál na YouTube.
A [tohleto](https://www.youtube.com/watch?v=nYqeHIRKboM) mě namotivovalo zkusit si taky vygenerovat nějaké ty obrázky.
Šel jsem na Midjourney Discord, zaregistroval se, ale napsalo mi to, že servery jsou přetížené a musím zaplatit, jestli něco chci.

To mě naštvalo.
Otevřel jsem [DiffusionBee](https://diffusionbee.com/), což je appka na macOS, která zjednodušuje použití Stable Diffusion.
To je model, který je open source a když to člověk rozchodí na svém počítači, za nic neplatí.
Už před časem jsem si DiffusionBee ze zvědavosti nainstaloval, ale neměl jsem čas to vyzkoušet.

Nedařilo se mi však vygenerovat žádné dobré věci, tak jsem se do toho trochu zavrtal a snažil se pochopit, co dělám blbě.
No a dost mě to chytlo.
Přidal jsem se do různých Discordů, subredditů, postahoval nějaké upravené modely, pochopil rozdíly mezi různými AI.
V noci se mi o tom zdálo.

-   [Jak do DiffusionBee přidat vlastní modely](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/DOCUMENTATION.md#custom-models)
-   Podcast: [Stable Diffusion breaks the internet](https://changelog.com/podcast/506)
-   Reddity: [r/ChatGPT](https://www.reddit.com/r/ChatGPT/), [r/DiffusionBee](https://www.reddit.com/r/DiffusionBee/), [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/)
-   Discordy: [DiffusionBee](https://discord.gg/QCjYd4eQQD), [Craiyon](https://discord.gg/craiyon-1065723932109451284), [Midjourney](https://discord.gg/midjourney) (aktuálně největší Discord server na světě), [OpenAI](https://discord.gg/openai), [PromptHero](https://discord.gg/prompthero-1026222136790110259),
-   Různé další modely a galerie: [Crayon](https://www.craiyon.com/), [Lexica](https://lexica.art/), [ArtHub](https://arthub.ai/), [Civitai](https://civitai.com/)
-   Většina lidí nepoužívá DiffusionBee, ale [Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui), které je nejspíš promakanější.
    Nezkoušel jsem.
-   Modely jde najít na [HuggingFace](https://huggingface.co/).
    DiffusionBee podporuje zatím jen některé typy.
    Zajímavé modely: [openjourney](https://huggingface.co/prompthero/openjourney), [portraitplus](https://huggingface.co/wavymulder/portraitplus), [Nitro-Diffusion](https://huggingface.co/nitrosocke/Nitro-Diffusion), [dreamlike-photoreal-2.0](https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0), [modelshoot](https://huggingface.co/wavymulder/modelshoot), [vintedois-diffusion-v0-1](https://huggingface.co/22h/vintedois-diffusion-v0-1)

![Prompt okopírovaný z internetu]({static}/images/screenshot-2023-04-08-at-14-51-54.png)
Prompt okopírovaný z internetu, který náhodou dopadl dobře

Většina promptů, které jde najít na internetu, je nepoužitelných bez dalších informací.
Výsledek závisí na modelu a na jeho nastavení: kolik pixelů na kolik, počet kroků…
Různé modely se chovají různě.
Některé dávají lepší výsledky s pětislovnými zadáními, jiné je potřeba otesávat pomocí dvaceti a více slov a třeba i s nějakými číselnými váhami nebo závorkami.
Takže samotný prompt vám je většinou k ničemu, maximálně může posloužit jako inspirace.
K tomu ještě můžete využít i negativní prompt, který by měl nějaké věci vyloučit.

![Můj vlastní prompt]({static}/images/screenshot-2023-04-09-at-18-03-39.png)
Můj vlastní prompt

Nakonec jsem byl schopen generovat i celkem obstojné obrázky.
Kvalit toho, co jde najít na internetu, to však nedosahuje.
Stable Diffusion je sice zdarma, ale o to těžší je vymačkat z něj něco pořádného.
Když to srovnám v podstatě jakýmkoliv online placeným modelem, např. [Lexica](https://lexica.art/), kam napíšu tři slova, dostanu co chci a graficky je to pecka, tak nekonečné vyšívání nad Stable Diffusion je někdy k uzoufání.

O to větší respekt u mě mají všichni, kdo z toho dokážou ty dobré věci dostat.
Teď vidím, že v tom jsou hodiny a hodiny zkoušení.

A hlavně ten nedeterminismus!
Dám prompt, vygeneruje to osmkrát něco jiného.
Na stejný prompt.
Jako vývojář nejsem zvyklý pracovat s něčím, kde měním vstup a výstup se sice nějak upravuje podle toho, ale někdy taky ne, a někdy si dokonce dělá úplně co chce.
I magie v pohádkách a fantasy funguje tak, že pokud správně řeknu zaklínadlo, stane se něco, co mohu očekávat a předpovídat.
Tohle je z 50 % prostě náhoda!

Časem jde oko trochu vytrénovat, najít společné rysy vygenerovaných obrázků a odtušit, jakým směrem to ladit.
Výsledkem je však závislost, jakou si představuji, že mají lidi na automatech.
Tahám za páčku, tahám tahám a toužím po třech citróncích.
Ještě jeden pokus.
Ještě.
A ještě jeden, teď už to musí vyjít…

Taky jsem se přes Velikonoce hrabal ve starých fotkách a zkusil jsem upscalovat nějaké ze starých mobilů.
Některé ty fotky jsou menší než 640×480px a na mojí retině vypadají jako malý obdélníček uprostřed obrazovky.
Objevil jsem následující:

-   [jpgHD](https://jpghd.com/), který je online a nad rámec dema za peníze.
-   [upscayl](https://github.com/upscayl/upscayl), který je open source a jde nainstalovat a použít lokálně.

Ten druhý jsem zkusil a na to, co jsem do toho dával, to mělo celkem obstojné výsledky.
Možná by to ale šlo i líp.
Možná by k tomu šlo použít i to Stable Diffusion!
Jenže to jsem zatím nezkoumal.

Pokud jste ve zkoušení dál než já, dejte vědět nějaké tipy!
A jestli jste ještě Stable Diffusion nezkoušeli, třeba vám tenhle článek pomůže začít.
