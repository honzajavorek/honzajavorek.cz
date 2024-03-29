Title: Programátora, který nepracuje v Linuxu, bych nenajal
Date: 2014-03-25 22:53:05
Lang: cs

Pár tweetů a tolik povyku :) Abych nakonec nebyl za úplného debila, musím to nějak doplnit tady na blogu.

Už před nedávnem [jsem začal na vývoj používat Vagrant]({filename}2013-11-28_vagrant.md). Tedy udělátko do příkazové řádky, díky kterému snadno a rychle
vytvoříte malé virtuálky (přitom backendy mohou být různé, např. VirtualBox). K čemu se to hodí? Můžete si tak vytvořit sandbox, v němž vyvíjíte a nešpiníte si přitom vlastní systém. Virtuálky můžete kopírovat, mazat, upravovat, rozběhnout si v nich Redis, PostgreSQL, MongoDB a klidně dvacet dalších služeb a pak je jedním příkazem vypnout (či pozastavit), až skončíte svou práci na onom konkrétním projektu. Já mívám většinou rozjetých více různých projektů (i během práce pro jednu firmu - dělá se na více věcech zároveň), každý má jiné závislosti atd., takže se mi to dost hodí.

Jenomže Vagrant a virtuálky jsou, přiznejme si to, celkem těžkopádné (a hlavně často dost pomalé) řešení. Proto někdo přišel a vymyslel [Docker](https://www.docker.io/). To je něco jako *lightweight* virtuálka, ale je to implementované přímo v ekosystému Linuxového jádra využitím všelijakých zajímavých funkcí, jež tam byly už dávno, ale nikdo je moc nepoužíval, nevědělo se o nich moc, nebo prostě nikoho nenapadlo dát je dohromady a použít zrovna na tohle. Navíc je tam ještě nějaké "verzování" atd., ale tomu až zas tak nerozumím, tak si to vyčtěte jinde. Prostě je to teď úplně nejvíc nejcoolovější věc, co frčí mezi vývojáři a kdo nemá na deklu laptopu nalepenou velrybičku, jako by nebyl ;-)

Akorát že pro spoustu lidí je menším zklamáním, že pokud to chcete rozjet na Macu, tak si musíte udělat virtuálku s Linuxem a v ní si rozjet Docker, protože na Macu to prostě nefunguje, je potřeba fakt přímo to Linuxové jádro. Takže jsem napsal tenhle (uznávám, trochu tendenční) tweet:

<blockquote class="twitter-tweet" lang="cs"><p>Tož ten slavný <a href="https://twitter.com/docker">@docker</a> je prý jen pro Linuxové jádro. Že by zas o důvod víc, proč je Linux pro profi vývojáře prostě nejlepší volbou?</p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/statuses/448097739155730432">March 24, 2014</a></blockquote>

Já osobně používám na svém laptopu Linux, konkrétně [Xubuntu](http://xubuntu.org/). Je to můj pracovní i volnočasový laptop. Během práce fakt silně cítím, jak mi to usnadňuje život. Během čistě uživatelské činnosti si vždy vážím toho, jak je Xubuntu na linuxové poměry ještě poměrně funkční volbou, ale i tak se někdy chytám za hlavu nad tím, co mi dokáže tenhle systém připravit za překvapení. Nejsem žádný linuxový fanatik - jsem pragmatik. Mou hlavní misí na tomto světě je v současnosti především programování webových aplikací v Pythonu a Linux je akorát prostě z mého pohledu ten úplně nejlepší systém, na kterém se to dá dělat. Je to systém, na kterém to pak na serveru většinou i běží, takže během vývoje prostě nejsou žádné problémy ([přečtěte si u Rikiho](https://www.facebook.com/fczbkk/posts/10152380085217741), jaké problémy začíná mít s Windows, a to prosím neprogramuje backendy webových aplikací). V mém světě je prostě všechno vytvořeno pro Linux a až potom, kvůli vývojářům, portováno na ten zbytek.

Měl jsem teď doma půl roku Mac od kamaráda na osahání. Zapnul jsem ho jednou. Byl to fajn systém, nic mi tam nevadilo, ale od Xubuntu se to v ničem nelišilo na první pohled natolik, abych měl motivaci si v tom systému zkusit pracovat nebo ho dlouhodobě používal. Neměl jsem motivaci zahájit změnu. Kdyby mě Linux štval, tak jo, ale já s ním vážnější problémy nemám, takže proč přecházet? Asi je to vymakanější, ale stojí to za tu cenu - čas strávený switchováním, peníze, atd.? Kdybych neprogramoval, tak bych se asi přeučil na Mac a používal ho. Ale takhle je pro mě prostě jednodušší přežít horší uživatelský prožitek, nic neřešit a užívat si toho, že ekosystém je na Linuxu odpradávna vyladěný pro programátora.

Koneckonců, je to jen OS. Jedničky a nuly... Svět je venku, za oknem. Ještě nejsme v [Her](http://www.csfd.cz/film/312650-ona/), aby byl výběr OS fakt to nejdůležitější rozhodnutí v našem životě :) Už to, že tady o tom píšu článek, je pro mě vlastně ztráta času. V mé hlavě je problém výběru OS poměrně neemotivní věc a flamům na tohle téma se fakt směju. Mnohem raději se budu hádat o mezerách a tabulátorech, ale ještě radši si s váma budu povídat o výletu do Pobaltí a nejkratší délce sukní, které jsme kdo už toto jaro stihli vidět.

V kontextu toho všeho a mého předešlého tweetu jsem si vzpomněl na [rozhovor s Jakubem Krčmářem](http://www.30minut.cz/jakub-whitwa-krcmar-grafika-pracujiciho-ve-windows-bych-si-nenajal/), kde se objevil "slavný" výrok:

> Grafika pracujícího ve Windows bych si nenajal

Dokonce je přímo v nadpisu toho rozhovoru. Kdo to pamatujete, tehdy to vyvolalo strašné pozdvižení a Jakuba pak nějakou dobu pranýřovali na každém rohu českého internetu, takže toho asi zpětně litoval a myslím, že to pak snad i v nějakém ohlédnutí vzal později zpět (ale to už se mi dohledávat nechce). Samozřejmě mu byli předhazováni všichni grafici windowsáci, od [Jerryho Tvrdka](http://www.jerrytvrdek.com/) až po nevímkoho.

Napadl mě vtípek - ironický tweet, kde bych se na tuhle větu odkázal a udělal si z ní srandu tím, že ji přepíšu na vývojáře a Linux. Aby bylo jasnější, že jde o srandu, uvedl jsem to profláklým "Nejsem rasista, ale..." a pro jistotu přidal ještě mrkajícího smajlíka. Jenže pět let od rozhovoru je pět let, kauzu už asi nikdo nepamatuje a můj humor [skoro](https://twitter.com/milancermak/status/448111199864225792) nikdo nezachytil.

<blockquote class="twitter-tweet" lang="cs"><p>Nejsem rasista, ale... osobně bych programátora, který není na Linuxu, nenajal. (parafráze a vzpomínka na <a href="http://t.co/9TwFSQrL14">http://t.co/9TwFSQrL14</a> ;-) )</p>&mdash; Honza Javorek (@honzajavorek) <a href="https://twitter.com/honzajavorek/statuses/448104192037879808">March 24, 2014</a></blockquote>

Možná už mě zblbly metahumorné diskuse [Žít Brna](http://zitbrno.cz/), kde je ironické a sakrastické úplně všechno. Každopádně jakmile jsem si všiml, že se to nesetkalo s pochopením, byly už jen dvě možnosti - přilít olej do ohně, nebo polopatě vysvětlit, že jsem to nemyslel vážně. Neměl jsem náladu na to druhé, takže jsem přilil - dal jsem si ale záležet, aby už bylo nadevše jasné, že to celé myslím s nadsázkou. Ani notoricky vysmívaná věta "Já mám Linux a jsem v pohodě" ale nepomohla! Dostal jsem nabídku vyargumentovat své postoje v článku na [Zdrojáku](http://www.zdrojak.cz/)!!1 8-) (Ano, i tu jedničku za vykřičníky jsem tam napsal schválně.)

<blockquote class="twitter-tweet" lang="cs"><p><a href="https://twitter.com/honzajavorek">@honzajavorek</a> na twitteru to nelze odargumentovat. Troufl by sis do clanku? Radi vydame, kdyz to bude dobre!</p>&mdash; Zdroják.cz (@zdrojak) <a href="https://twitter.com/zdrojak/statuses/448132799636451328">March 24, 2014</a></blockquote>

Raději jsem nereagoval a netrolil dál - pochopil jsem, že se ode mne na Twitteru očekávají pouze seriózní příspěvky a nemám dostatek energie, abych tuhle kauzu živil až do 1. 4., kdy mají i seriózní média právo dělat si z lidí srandu a kdy bych mohl vše beztrestně zakončit hlasitým "Apríl!", aby to došlo opravdu všem.

Pln výčitek a zodpovědnosti za fabulace jsem večer v krátké zprávě natvrdo odhalil o co celou dobu šlo, ale mám dojem, že tohle už nikdo nečetl. Aspoň jsem dostal hezké fiktivní tričko:

<blockquote class="twitter-tweet" lang="cs"><p><a href="https://twitter.com/honzajavorek">@honzajavorek</a> A nasemu pozornemu divakovi do Brna posilame tricko <a href="https://twitter.com/search?q=%23trololobit&amp;src=hash">#trololobit</a> <a href="http://t.co/tiVACRykop">pic.twitter.com/tiVACRykop</a></p>&mdash; Ales Zoulek (@aleszoulek) <a href="https://twitter.com/aleszoulek/statuses/448212604452737025">March 24, 2014</a></blockquote>

Za tričko děkuju!
