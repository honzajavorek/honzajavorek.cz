Title: Touchpad v Ubuntu
Date: 2009-12-06 18:25:00
Tags: hračičkování, linux, software

Moji kamarádi [mají radost, že jsem přešel na Linux](http://twitter.com/markoph/status/6380776939), tak jim přidám vodu na mlýn článkem s na první pohled masochistickým tématem. [Rád používám touchpad](http://honzajavorek.cz/blog/nemam-rad-mysi) a v Ubuntu mě vždy štvalo, že nastavení jeho ovládání nebylo nikdy moc snadné. Zapíšu si tu tedy pár poznámek, jak dotáhnout jeho ovládání k dokonalosti, protože dohledat tyhle věci je trochu problém. Pokud člověk napíše do Google slova Ubuntu a touchpad, většinou se lidé ptají na jeho vypnutí (barbaři!). Abych se vyvaroval některých komentářů, hned na úvod dodám návod pro
Windows: Nainstalujte si ovladače pro Synaptics Touchpad, tam si to naklikejte a nepište o tom články ;) .

Nastavení touchpadu je normálně v *System → Preferences → Mouse* na záložce *Touchpad*. Pokud toužíte po rozšířeném nastavení, tak pomůže instalace *gsynaptics* (pro GNOME). Ten je potom k nalezení pod *System → Preferences → Touchpad*. Jenže… Ačkoliv si můžete dopřát applovské triky a používat zoom nebo scrolling více prsty, pořád vám to nikde nedovolí nastavit ťapací oblasti. Já nutně potřebuji „prostřední tlačítko“ v pravém horním rohu.

No a k tomu pomůže [tato stránka](http://ubuntuforums.org/showthread.php?p=8403017), kde je nejprve [řešení dočasné](http://ubuntuforums.org/showpost.php?p=8261605&postcount=3) (do prvního restartu, což moc ani nepovažuji za řešení) a pak [řešení permanentní](http://ubuntuforums.org/showpost.php?p=8399228&postcount=8). Tedy přidat do `/etc/hal/fdi/policy` soubor `synaptics.fdi` a do něj hodit

    ::xml
    <?xml version="1.0" encoding="UTF-8"?>
    <deviceinfo version="0.2">
        <device>
            <match key="input.x11_driver" string="synaptics">
                <merge key="input.x11_options.RTCornerButton" type="string">2</merge>
            </match>
        </device>
    </deviceinfo>

No a to je vše. Pomocí změn v HALu (viz odkaz na permanentní řešení) byste měli uspokojit veškerá svá tajná přání, která vás v souvislosti s touchpadem kdy napadla. Ještě dodám, že tohle nastavení prostředního tlačítka do pravého horního rohu bylo v Ubuntu výchozí, ale podle lidu stěžujícího si na fórech pro Karmic teď zmizelo. Netuším proč. Přeji hezké ťapání.