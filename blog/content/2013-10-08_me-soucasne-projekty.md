Title: Mé současné projekty
Date: 2013-10-08 10:54:55

Od mého lednového [restartu]({filename}/2012-11-04_restart.md) jsem prošel vícero projekty a mnohdy jsem z týdne na týden odpovídal na otázku *na čem teď vlastně děláš?* pokaždé jinak. Teď se situace (snad!) na chvíli opět ustálila, takže jsem se rozhodl, že zde sepíšu takové menší shrnutí.

## Co mám za sebou

- Pracoval jsem ještě půl roku externě na **interním nástroji s REST API pro [Mergado](http://mergado.cz/)**. Mergado je projekt, na kterém jsem pracoval i mnoho let předtím. Máte-li e-shop, nasypete panu Mergadovi do krámku svůj XML feed se zbožím, jeho výstup pošlete do Heureky a pak už se jen koukáte, jak se vám zvyšují tržby.
- Programoval jsem **REST API backend k SPA [Vodafone Slevopark](http://slevopark.vodafone.cz/)**. Jednalo se o jednorázovou zakázku, kterou si cením především za získané zkušenosti v tvorbě backendu pro [SPA](https://en.wikipedia.org/wiki/Single-page_application). Taky jsem si vyzkoušel, jak... ehm, řekněme... zapeklitá je někdy spolupráce s korporacemi.
- Udělal jsem **pár nástrojů pro [SkyPicker](http://skypicker.com/)**. Na stránkách tohoto brněnského startupu najdete levné letenky přehledně podle mapy. Mojí nejoblíbenější funkcí je "radius", které nastavím tak, aby obsahovalo Prahu, Brno, Ostravu, Vídeň i Bratislavu a SkyPicker potom hledá lety ze všech těchto destinací.

## Synopsi.TV

**Od září pracuji pro [Synopsi.TV](http://synopsi.tv/)**, kam mě odlovil [Rasťo Turek](http://turek.co/). Kdo neznáte, jedná se o (víceméně) bratislavský startup se světovými ambicemi, jehož hlavním produktem je **doporučování filmů na míru uživateli**. To znamená, že si jednotlivá doporučení necucá z prstu, ani se neřídí vkusem vašich přátel, hodnocením kritiků (= [FFFilm](http://fffilm.name/)), nebo názorem masy (= hodnocení na ČSFD) - řídí se tím, co se v minulosti líbilo konkrétně vám. Jste-li tedy fanouškem béčkových hororů, Synopsi.TV by to mělo poznat a do budoucna vám je nabízet, ať už si o nich vaši přátelé, obyvatelé zeměkoule, či kritici myslí cokoliv.

![Synopsi.TV]({static}/images/stv.jpg)

Byznys model je zatím v tom, že se dá takový *reccomendation system* poskytovat partnerům - podobně jako kdysi [jyxo.cz](https://cs.wikipedia.org/wiki/Jyxo.cz) vyvíjelo a licencovalo vyhledávač.

Ještě se v nové práci stále rozkoukávám, ale na práci mám **vylepšování [API](https://developers.synopsi.tv/)**.

## API konzultant

Na volné noze se zabývám **navrhováním a konzultováním REST API**. V této souvislosti jsem např. navrhoval podobu **RESTové obálky kolem [RÚIAN](http://vdp.cuzk.cz/)** a například s API **pomáhám [Videoflotu](http://www.videoflot.com/)**, dalšímu perfektnímu brněnskému startupu.

Pokud si s API nevíte rady, potřebujete vyřešit zapeklité otázky ohledně návrhu, *best practices*, apod., rád vám pomohu - **kontaktujte mě**. Pokud jste nějaký neziskový projekt a já usoudím, že pracujete pro dobrou věc, nabídnu vám konzultace *pro bono*. API vám však nenaprogramuji, v tomto ohledu jsem plně vytížen.

### Videoflot

[Videoflot](http://www.videoflot.com/) je **tržiště pro videotvůrce**. Pokud potřebujete úvodní video pro svůj startup nebo jste kapela potřebujete klip, na Videoflotu si zdarma zadáte poptávku a pak už jen čekáte, kdy se vám ozvou ti praví lidé. Pro tvůrce je to zase platforma k sdružování v rámci komunity, třeba pro různé neziskové projekty. Zrovna s velkou slávou [spouští novou verzi](https://www.facebook.com/events/584749094919023/591573977569868/), tak se na tento pěkný počin mrkněte.

Mimochodem, tým za Videoflotem je **moc příjemná parta lidí**. Jejich kapitán David "Havran" Spáčil je navíc velice inspirativní osobou (viz [rozhovor](http://www.babelguide.com/case-studies/david-spacil-from-studying-camels-to-video-community-site-in-chile), který fakt stojí za přečtení), takže je vždycky radost s nimi strávit byť i jen chvilku času. Pokud se k nim chcete přidat a pomoci jim, neváhejte.

![Videoflot]({static}/images/videoflot.jpg)

## Hobby projekty

[Žít kino](http://zitkino.cz/) je můj malý *open source hobby startup experiment*. Jeho cílem je vytvořit **co nejúplnější a nejpřehlednější program brněnských kin**. Chcete jej podpořit? [Vylepšete jej](https://github.com/honzajavorek/zitkino/), [olajkukte jej](https://www.facebook.com/zitkino), [sledujte jej](https://twitter.com/zitkino). Na jeho vylepšení dokonce v Brně proběhl [první Python sprint](https://www.facebook.com/events/316558888489555/).

![Žít kino]({static}/images/zitkino.png)

No a potom pár knihovniček na [GitHubu](https://github.com/honzajavorek/):

- **[Redis Collections](https://github.com/honzajavorek/redis-collections)** - umožní vám používat datové typy v [Redisu](http://redis.io/), jako by to byly nativní Python typy. Pokud umíte dobře Python 3, [pomozte nám prosím s portováním](https://github.com/honzajavorek/redis-collections/pull/22)!
- **[fiobank](https://github.com/honzajavorek/fiobank)** - Python knihovna na přístup k [API od Fio Banky](http://www.fio.cz/bank-services/internetbanking-api). Zatím jen pro čtení, i když Fio už má API i pro zápis.
- **[czech-holidays](https://github.com/honzajavorek/czech-holidays)** - 100 řádků Python kódu, které vám usnadní práci s českými státními svátky.

## Co bude dál?

Moje plány do budoucna jsou:

- Vylepšovat své znalosti a zkušenosti v oboru **REST API**.
- **Psát pro [Zdroják](http://zdrojak.cz/)** zajímavé články, aby na něm [nebyla nuda](http://www.misantrop.info/jak-necist-zdrojak/).
- Dopomoci **Synopsi.TV** k ovládnutí světa.
- Ovládnout Brno pomocí **[Žít kino](http://zitkino.cz/)**.
- Věnovat se i nadále **[Pyvu](http://python.cz/#pyvo) a Pythonu u nás**.
- Spravit kolena a **jezdit víc někam do hor** ;-)
