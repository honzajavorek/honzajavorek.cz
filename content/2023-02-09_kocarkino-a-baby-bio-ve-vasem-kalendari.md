Title: Kočárkino a Baby Bio ve vašem kalendáři
Image: images/329913737-513213380935038-6597939849996854149-n.png
Lang: cs
Telegram-Comments: https://t.me/honzajavorekcz/110


O víkendu jsem zhruba za hoďku vytvořil automatizovaný kalendář promítání pro rodiče s malými dětmi, která se konají v kinech blízko pražského Žižkova.

Původně tam bylo jen Kočárkino z KC Vozovna, tak se to jmenuje [https://honzajavorek.cz/kocarkino.ics](https://honzajavorek.cz/kocarkino.ics), ale přidal jsem tam pak i Baby Bio.

![Kočárkino a Bio Oko v kalendáři]({static}/images/329913737-513213380935038-6597939849996854149-n.png){: .img-thumbnail }

## Použití

Jestliže to chcete použít, nestahujte to jako soubor, ale nahrajte si to do kalendáře jako „živou URL“.
Pouze tak se to bude v čase aktualizovat.
U každého filmu jsou odkazy na web kina i na vyhledávání na ČSFD.

## Jak to funguje?

Kód v Pythonu je [tady na GitHubu](https://github.com/honzajavorek/honzajavorek.cz/blob/798faaa9dd3db9c4de956326ab9a10ec12932849/blog/kocarkino.py). Pokud kalendář aktivně používáte a něco vám v něm chybí, napište mi o tom do [GitHub Issues](https://github.com/honzajavorek/honzajavorek.cz/issues).

Pokud vás napadá, co by kalendář mohl umět, ale nehodláte jej aktivně sami používat, tak svůj nápad napište na kompostovatelný papírek, udělejte z něj vlaštovku a pošlete jej z okna.

## Souboj knihoven: ics nebo icalendar?

Dříve už jsem takových kalendářů vytvořil hromady, ale s knihovnou [ics](https://pypi.org/project/ics/).
Její vývoj je však nějaký divoký a pomalý, dlouho jsem musel používat nějakou verzi z Gitu, takže jsem tentokrát vyzkoušel knihovnu [icalendar](https://pypi.org/project/icalendar/).
Tu jsem objevil díky tomu, že ji použila Mia Bajić, když vytvářela [pyvo-bot](https://github.com/pyvec/pyvo-bot/).

Moje hodnocení?
Na čtení staženého kalendáře je možná jednoduchá, ale na vytváření je to o dost víc práce, než s ics.
Přijde mi, že icalendar mi dává pár vychytávek navíc oproti tomu, kdybych se ten textový soubor snažil vytvořit ručně, ale abych něco doopravdy vytvořil, musím ten formát docela detailně znát a trávit čas čtením specifikace.

Abych mohl věc vůbec dokončit, pomohl mi dost [online iCalendar validátor](https://icalendar.org/validator.html) a stejně jsem se ještě půl hodiny motal v časových pásmech, než se to začalo v mém Google Kalendáři zobrazovat správně.
Oproti tomu, když jsem dřív používal ics, většinou stačilo nasypat do něj data podle dokumentace a i když jsem o iCalendar formátu nic moc nevěděl, vygenerovalo mi to přesně to, co jsem chtěl.
