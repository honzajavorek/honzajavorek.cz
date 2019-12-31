Title: Gmail jako plnohodnotný poštovní klient (+ case study: VUT mail)
Date: 2010-01-08 02:47:00
Lang: cs
Tags: gmail, net, software, škola, vut fit

Asi se shodneme na tom, že obyčejný poštovní klient jako Outlook nebo Thunderbird by měl splňovat tyto vlastnosti: Umět stahovat poštu odjinud přes **POP3**, být přístupný **offline** i se všemi daty, odesílat poštu přes jakýkoliv **SMTP** server. Tak **Gmail tohle všechno už nějakou dobu splňuje**. Navíc má rychlé a přehledné webové rozhraní. Zkusím popsat jak na to a jako case study si vezmu náš **školní mail**. Omlouvám se, ale pojmy z Gmailu budou v angličtině – nemám ponětí jak jsou přeloženy do češtiny a nehodlám to zjišťovat.

Zadáním je využívat Gmail pro příjem, uskladnění a odesílání [této školní pošty](http://www.fit.vutbr.cz/CVT/net/email.html.cs). Je potřeba, aby chodila na Gmail ze školního serveru, aby byla přístupná offline a aby odesílala zprávy přes školní SMTP, protože pokud tak činit nebude, kvůli tvrdé fakultní antispamové politice pravděpodobně každý náš e-mail žadonící o bodík z předmětu navíc skončí ve věčných lovištích a nikdo si jej nikdy nepřečte (to je fakt potvrzený zaměstnanci fakulty).

## Accounts

Základním stavebním kamenem pro náš úkol budou Accounts. Gmail dovoluje zakládat nové Accounts, tedy hloupě přeloženo účty. Každý takový účet představuje jednu e-mailovou adresu. Můžeme si vytvořit účet pro náš e-mail na Seznamu, na Centru, Hotmailu apod. To ještě není nic moc zvláštního – nastavíme si účet pro mail na Seznamu, třeba *[usni.lalok@seznam.cz](mailto:usni.lalok@seznam.cz)*, ověříme jej a Gmail nám dovolí odesílat e-maily, jež se tváří, jako by byly odeslané z *[usni.lalok@seznam.cz](mailto:usni.lalok@seznam.cz)*. Zpravidla si pak ještě na tom Seznamu nastavíme automatické přeposílání na
Gmail. **Takto můžeme spoustu e-mailových schránek sdružit pod jednu v Gmailu**.

## POP3

**Gmail ale dovoluje maily z takových účtů automaticky stahovat přes POP3** jako jiný běžný klient. Tak můžeme napojit i účty, kde není vytvoření přeposílacího pravidla možné, jednoduché, nebo úplně žádoucí. V nastavení dokonce vidíme, kdy naposledy mail kontroloval, kolik zpráv přijal a jestli se mu to vůbec povedlo. Kliknutím na tlačítko můžeme zprávy přijmout i hned, pokud chceme proces z nějakého důvodu urychlit. Přidání POP3 účtu je intuitivní. Pro případ školního mailu nám ale POP3 moc nepomůže, protože přístup je jen přes IMAP a ten Gmail neumí.

## Přeposílání

Ve většině e-mailů je možnost **přeposílat všechnu poštu někam jinam**, nebo se dá alespoň nastavit takový filtr, který ovlivní všechny příchozí e-maily (ať už je to třeba podmínkou „předmět neobsahuje slovo *b\~v\~d\~ď\~g\~h\~z\~ž*“, kterou projdou všechny) a pošle je jinam. Školní mail ale nic takového nenabízí, ani ve svém [webovém rozhraní](https://email.fit.vutbr.cz/). Co s tím? No existuje trochu hackerské řešení: Přihlašte se na libovolný školní server a do svého *home* dejte soubor `.procmailrc` s následujícím
obsahem:

    :0 * !^FROM_MAILER ! lalok@gmail.com

Tento kód zajistí, že všechna vaše pošta bude automaticky přeposílána na váš Gmailový účet *[lalok@gmail.com](mailto:lalok@gmail.com)*.

## Reply-To

Ke každému Accountu si můžeme nastavit tzv. **reply-to**, tedy e-mail, na který má dojít odpověd k mailům odeslaným z adresy tohoto Accountu. Bude většinou stejný, ale můžeme chtít takovým způsobem naznačit přátelům, že starý e-mail už nepoužíváme. Odešleme jim mail z *[usni.lalok@seznam.cz](mailto:usni.lalok@seznam.cz)*, ale když dají odpovědět, jejich mail půjde automaticky na *[lalok@gmail.com](mailto:lalok@gmail.com)*, pokud si to nastavíme. Takové srandy jde nastavit i globálně pro celý mail (*When receiving a message: Reply from the same address the message was sent to / Always reply from default address*), přičemž odchozí adresu si můžeme stejně kdykoliv explicitně vybrat při psaní mailu.

## SMTP

Velmi důležitou možností je **nastavení vlastního SMTP**. Bez něj nám sice vše bude fungovat po teoretické stránce – maily ze školy přijdou na náš Gmail, tam budeme mít nastavené, aby se tvářil jako *[xlalok00@stud.fit.vutbr.cz](mailto:xlalok00@stud.fit.vutbr.cz)* a on bude vesele pod touto adresou e-maily odesílat. Jenže problém je v tom, že školní servery v praxi stejně **rozeznají, že zpráva není odeslána z VUT** a mohou ji nekompromisně skartovat. Proto musíme e-maily posílat přes školní server k tomu určený – Evu. Potřebné nastavení je [zde](http://www.fit.vutbr.cz/CVT/net/email.html.cs), ale kam ho v Gmailu dát? Dříve to vůbec nešlo, nyní to ale Gmail už umí. Nejsem si jistý, ale mám dojem, že tu funkci spustil bez jakékoliv slávy. Prostě se tam jednoho dne objevila, já si jí za půl roku všiml a jásal jsem. Tak tedy SMTP lze nastavit pro každý Account zvlášť. Zeptá se vás *Send mail through your SMTP server?* a dá na výběr z posílání přes něj, nebo použití vlastního SMTP. Vyberte vlastní a napište tam údaje pro Evu.

## Offline přístup

Já osobně **offline přístup** nevyžaduji, ale Gmail jej podporuje a zkoušel jsem, jde to. Pokud nutně potřebujete poštu i někde na cestách, nainstalujte si [Google Gears](http://gears.google.com/) a v pravém horním rožku Gmailu si ikonkou nechte synchronizovat obsah e-mailu s diskem. Zabere vám to nějaké místo (pokud máte v Gmailu gigabajty pošty, tak gigabajty) a bude to chvíli trvat, ale inkrementální změny jsou potom už plynulé.

## Gmail jako klient

Tento článek neměl být ani tak o tom, že Gmail je lepší klient než Outlook nebo Thunderbird. Měl představit některé jeho **méně známé funkce** a vypíchnout, že z Gmailu jde udělat **terminál** se stejnou základní funkčností jako zmíněné programy a to včetně toho SMTP. Snažil jsem se to pojmout i jako **návod, jak integrovat školní poštu do Gmailu** a snad se to povedlo srozumitelně. Pokud někomu nevyhovuje Gmail nebo vůbec nějaká webová rozhraní, tak se tímhle vším samozřejmě vůbec nezabývejte. Mě vyhovuje Gmail, takže chci mít všechno v něm.

Nezapomeňte, že Gmail má nejvíce funkcí ve své **US English** jazykové verzi. Nové funkce se šíří do ostatních jazyků pomalu a to až tehdy, kdy jsou zcela přeloženy. Je tedy možné, že v českém Gmailu ani žádné SMTP není.
