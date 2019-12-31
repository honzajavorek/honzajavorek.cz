Title: Více stylů pro IE? Na co?
Date: 2008-02-06 08:38:00
Lang: cs
Tags: css, explorer, názory, webdesign

O tom, jak vytvářet speciální styly jen pro IE a jak si tím pádem pročistit CSS kód, bylo [napsáno už dost](http://www.google.cz/search?q=podmíněné+komentáře+IE). Oddělené styly pro moderní prohlížeče pak nemusí být plné CSS hacků a dokonce nám projdou testem validity. Nevidím ale důvod, proč to s mánií podmíněných komentářů přehánět. Např. když se podíváte do kódu [Filosofa](http://www.filosof.biz/) (ale viděl jsem takových webů povíc), má jeden styl pro IE6, další pro IE7 a až naprogramují IE8, bude mít jeho web asi styly 4.

Přijde mi o dost lepší mít **jen jeden** speciální styl **pro IE7 a nižší**, v němž jednotlivé verze klidně rozliším hacky (vystačím si docela snadno pouze s [explorerovým sítem](http://www.pixy.cz/pixylophone/2004_06_archiv.html#1088438627)). Nehackované vlastnosti pak platí jen pro IE7. O „čistotu“ speciálního stylu mi vůbec nejde, takže mi toto řešení připadá jako opravdu o dost jednodušší a stejně výkonné, jako tvorba více stylů.

A jen tak na závěr… Osmička už se prý od půlky prosince [umí usmívat](http://blogs.msdn.com/ie/archive/2007/12/19/internet-explorer-8-and-acid2-a-milestone.aspx)
:) .
