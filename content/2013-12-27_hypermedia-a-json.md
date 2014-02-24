Title: Hypermedia a JSON
Date: 2013-12-27 19:36:20

Více lidí mě poprosilo, abych rozvedl tento tweet:

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p>Čím víc toho vím o hypermedia APIs, tím víc mám pocit, že JSON je na to fakt špatná volba. Kacířská myšlenka?! <a href="https://twitter.com/jirkakosek">@jirkakosek</a> by měl radost :)</p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/statuses/416598629965504512">December 27, 2013</a></blockquote>

Nepovedlo se mi to napsat do 160 znaků, tak to zkusím stručně tady na blogu.

Přijde mi, že **síla formátu JSON je v tom, že je jednoduchý a přehledný**. Myslím si, že je to hlavní důvod, proč jej spousta lidí začalo používat místo XML a oblíbilo si jej. Jakmile chceme ovšem JSON použít jako formát pro hypermedia API, zjistíme, že nám v něm chybí spousta věcí.

Řešení? Přilepíme do něj co potřebujeme a vydáme jako speciální MIME type! Jenže ať koukám jak koukám, ani [HAL](http://stateless.co/hal_specification.html), ani [Collection+JSON](http://amundsen.com/media-types/collection/), ani [Siren](https://github.com/kevinswiber/siren) už **nejsou jednoduché a přehledné** - stává se z toho stejně špatně čitelná "próza", jakou je ono zatracované XML.

<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p><a href="https://twitter.com/honzajavorek">@honzajavorek</a> <a href="https://twitter.com/jirkakosek">@jirkakosek</a> Proč? Holt už pak JSON odpověď není tak stručná, přehledná na první pohled :)</p>&mdash; Jan Žák (@zakjan) <a href="https://twitter.com/zakjan/statuses/416602887116959745">December 27, 2013</a></blockquote>

Jenže proč se potom vůbec trápit s JSONem? **XML má přece všechny ty věci, kvůli kterým rozšiřujeme JSON.** Nejen to - má mnohem víc, např. jmenné prostory nebo dotazovací jazyk. A má to všechno už dlouho, funguje kolem něj ekosystém vyladěných nástrojů, existují [připravené a rychlé parsery](http://lxml.de/), lze jej [snadno streamovat](http://lucumr.pocoo.org/2013/2/13/moar-classes/), atd.

Nechápejte mě špatně - třeba tu nějaké skvělé důvody jsou, ale **na první pohled** mi to prostě smysl nedává. Pokud se mi líbí jízda na kole, protože s ním na rozdíl od auta můžu po chodníku, prokličkuji kolem kdejaké zácpy a zaparkuji ho u každé lampy, tak z něj přeci nezačnu stavět cykločtyřkolku při prvním zjištění, že na něm domů nepřevezu matraci z IKEA. Prostě si na to vezmu to auto, protože je k tomu dělané - existuje pro tento účel několik desítek let a pokud mě v něm třeba někdo srazí, mám velkou šanci přežít.

Možná je má analogie nepovedená a myšlenka nedotažená - to je v pořádku. Myšlenka je to dost čerstvá a klidně je možné, že mě dobrým komentářem vyvedete z omylu. Snažím se jen pragmaticky uvažovat nad nástroji, jež máme k tvorbě API k dispozici a pokládat si záludné otázky :-) Nechtěl jsem o tom hned psát na blog, ale Twitter, což je to nejlepší místo pro podobně nezralá zamyšlení, mi na to byl už moc těsný.

