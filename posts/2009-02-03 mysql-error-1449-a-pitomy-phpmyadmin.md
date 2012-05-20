Title: MySQL Error 1449 a pitomý phpMyAdmin
Date: 2009-02-03 14:56:00
Tags: fail, mysql, php

Tak se mi stalo, že jsem **nahrál dump databáze na localhost** a ona vyhodila asi takovýto error:

> There is no ‚root‘@‚%‘ registered

Jeho číselné označení si přečtěte v titulku. Pátral jsem pátral a nakonec jsem zjistil, že příčin může být více a zjistit o tom nejde skoro nic. Prima. Každopádně můj problém byl způsobený tím, že v databázi byly pohledy (`VIEW`) a ty mají **nastaveno určité oprávnění**. Je to kvůli bezpečnosti atd. – viz [manuál](http://dev.mysql.com/doc/refman/5.0/en/create-view.html), no každopádně když si to tam **nastavíte špatně**, tak máte smůlu. Při tvorbě `VIEW` máte možnost zadat `SQL SECURITY` jako `DEFINER` nebo `INVOKER`. Někdy se může hodit to první, tedy přesné nastavení uživatele na serveru, ale pro normální přenos kamkoliv jinam bez omezení je asi lepší `INVOKER`, což by měl být **ten, kdo pohled spouští**. Zajímavá diskuse k tématu je [zde](http://groups.google.com/group/comp.databases.mysql/browse_thread/thread/d8e6da7244a13788?pli=1).

Ale já přeci **nic nenastavoval** :| . Mám čistý dump z phpMyAdmina! No, to je sice hezké, ale phpMyAdmin s těmi `VIEW` moc neumí a přiřazuje každému nějaký defaultní `DEFINER`, který si vygeneruje (v mém případě `'root'@'%'`). Ten samozřejmě **na jiném PC vůbec neexistuje**. V phpMyAdminu mi to ani nešlo změnit, musel jsem to přepsat přímo v SQL a potom se to rozjelo. No asi mám nějaký starý phpMyAdmin, říkám si, takže stahuju a zkouším nový s myšlenkou, že to snad už dopilovali.

No, a světe div se, sice má více možností práce s `VIEW`, ale **kazí export úplně stejně jako ten starý**. Nikde nevidím nastavení tohoto omezení – ani v nabídkách pro pohledy, ani při exportu. Ach jo, takže **ruční práce** a dávat si pozor… Nic jiného nezbývá :( .