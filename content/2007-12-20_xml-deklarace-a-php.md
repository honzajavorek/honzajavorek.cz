Title: XML deklarace a PHP
Date: 2007-12-20 01:42:00
Lang: cs
Tags: php, projekty, xml

Zase trochu o webdesignu. Připravte se na vzrušující objevování Ameriky, kola a podobných užitečných věcí. Čtenářky, které se nezabývají tvorbou webu, zřejmě zklamu, ale tak už to v životě chodí. Bavte se zatím třeba [tímhle](http://gringo.profitux.cz/komixy/).

## XML deklarace

Pokud se člověk už definitivně nevzbouřil, neodklonil od XHTML a stále ho baví psát striktně nevalidní jakožeXML dokumenty (více o těchto kravinách čtěte u [Dera](http://dero.name/weblog/xhtml-mime/) nebo [Martina Hassmana](http://html456.blogspot.com/)), jistě do nich také rád vkládá XML deklaraci. Je to první řádek v kódu, jenž hřímá „já jsem XML!“ a pokud stránka používá UTF-8, není povinný. Zakládám si na používání UTF-8, ale stejně jako mne náramně vzrušuje používat **X**HTML, svědomí mi nedovolí XML deklaraci prostě vynechat. Holt zažité superstriktní pudy z dob evangelizace webu.

## PHP

Bo su mimo jiné i PHP programátor, musel jsem po čase pokojného deklarování XML řešit jistý nedostatek symbiózy mezi jazykem a právě oním prvním řádkem dokumentu.

Zápis

    :::xml
    <?xml version="1.0" encoding="utf-8" ?>

prostě není úplně ono, protože ty špičaté závorky a otazníčky PHP bere na sebe a server vám vrátí něco podivného, asi **parse error**.

## Řešení

Řešení je zřejmé…

    :::php
    <?php echo "<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n"; ?>

Nebo třeba

    :::php
    <?php echo '<?xml version="1.0" encoding="utf-8" ?>' . "\n"; ?>

Jak je ale vidět, zřejmá řešení problémů nejsou ani hezká, ani elegantní. Předkládám proto jedno ne zcela zřejmé, ale geniální řešení, které je hezké, elegantní a navíc rychlé – nepotřebuje prakticky žádný výkon PHP.

    :::php
    <<?php ?>?xml version="1.0" encoding="utf-8" ?>

A je to! Že se tu zabývám blbostmi? No jistě že ano! Ale proč netrávit čas psaním a čtením článků o roztomilých maličkostech ;) . A že to šlo napsat v jedné větě? Ale no tak… Jako byste mě neznali! :D
