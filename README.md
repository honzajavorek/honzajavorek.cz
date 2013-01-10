# honzajavorek.cz

This is source code of my site, including my blog _Javorové lístky_. You can read it
comfortably at [honzajavorek.cz][site] if you know Czech. It is
proudly powered by [Python][python] and [GitHub][github] using [Pelican][pelican], [Markdown][markdown],
and [Jinja2][jinja].

## Status: ACTIVE

Under active development and maintenance. GitHub [pull requests][pull_requests] fixing typos in my articles are very welcome! :-)

## Installation

This installation guide is for Xubuntu Linux in a few simple steps. It's a remainder for me in case I would forget how to run the site generator on my computer.

1. Clone the code. `git clone git@github.com:honzajavorek/honzajavorek.cz.git`
2. `cd honzajavorek.cz`
3. Create a new Python virtual environment. `virtualenv env --distribute`
4. Activate the environment. `. env/bin/activate`
5. In virtual environment, install all Pythonic requirements. `pip install -r requirements.txt`
6. Install Sass. `apt-get install ruby rubygems && gem install sass`
7. Put your API key into plain text file `google_static_maps_api_key`.
8. Run it: `start.sh`

## License: CC BY-NC-SA

(cc) 2007–2013 Jan Javorek &lt;<a
href="mailto:jan.javorek&#64;gmail.com">jan.javorek&#64;gmail.com</a>&gt;

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

&nbsp;
----
&nbsp;

# honzajavorek.cz (in Czech)

Toto je zdrojový kód mého webu včetně blogu _Javorové lístky_. Můžeš si jej pohodlně
přečíst na [honzajavorek.cz][site]. Velice hrdě se hlásím k tomu, že celá
tahle sranda běží na [Pythonu][python] a [GitHubu][github] díky nástrojům [Pelican][pelican],
[Markdown][markdown] a [Jinja2][jinja].

## Status: AKTIVNÍ

Aktivně vyvíjeno a udržováno. Vítám opravy překlepů a hrubek v článcích přes GitHub [pull requests][pull_requests]! :-)

## Licence: CC BY-NC-SA

(cc) 2007–2013 Jan Javorek &lt;<a
href="mailto:jan.javorek&#64;gmail.com">jan.javorek&#64;gmail.com</a>&gt;

Toto dílo podléhá licenci [Creative Commons Uveďte autora-Nevyužívejte dílo komerčně-Zachovejte licenci 3.0 Česko](https://creativecommons.org/licenses/by-nc-sa/3.0/cz/).


[python]: http://www.python.org
[github]: http://pages.github.com/
[site]: http://www.honzajavorek.cz
[pelican]: https://github.com/ametaireau/pelican
[markdown]: http://daringfireball.net/projects/markdown/
[jinja]: http://jinja.pocoo.org/
[pull_requests]: http://help.github.com/send-pull-requests/
