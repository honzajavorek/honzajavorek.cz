Title: Když je na disku málo místa
Date: 2010-07-24 09:01:00
Tags: linux

Setkal jsem se teď se zajímavým problémem. Že nemám místo na home partition kvůli hudbě, to jsem věděl. Jenže teď mi systém začal hlásit, že jsem vypotřeboval veškerý prostor i na root partition, kde jsem měl ještě před pár dny sotva čtvrtinu využitou.

V Ubuntu existuje několik možností, jak se koukat na disky. Můžete si doinstalovat GParted a přímo si prohlížet partitions, ale pro základní informace stačí záložka File Systems v System Monitoru. Pak je tady Disk Usage Analyzer, což je takový chytrý program, který projede váš disk a v pěkném grafu vám přesně řekne, co a kde vám zabírá nejvíce místa. Zvláštní ovšem bylo, že jak GParted, tak System Monitor mi sdělovaly, že na root partition žádné místo nemám, ale tím Analyzerem nešlo ani za nic najít žádné velké soubory.

Nakonec jsem vygooglil toto: `find / -size +1000000000c`. Příkaz, který najde soubory větší než X. Vypsalo mi to spoustu zamítnutých pokusů o přístup, tak jsem před to dal `sudo` a *voilà*, najednou se mi tam vyloupl v rootově koši nějaký šílený temporary soubor přes 20 GB velký, který jsem tam nedávno asi nějak vytvořil.

**Ponaučení:**

-   Dávat si dobrý pozor, co jako root dělám a kde mi zůstávají velké soubory.
-   Dávat si pozor na to, že programy často opravdu nevidí všude a to co patří rootovi je pro ně tabu, i když třeba jen počítají místo na disku.
-   Zapamatovat si užitečný příkaz pro nalezení souborových obrů.

Chtěl jsem si tímto článkem hlavně poznamenat, na co jsem přišel, takže pokud jsem vás zdržel a vy zrovna netoužili po nějaké šílené geekovině, pak se omlouvám a [posílám vám krásnou písničku](http://www.youtube.com/watch?v=GrO5J7TdS7c) na uklidnění.