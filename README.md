# Blog Javorové lístky


This is source code of my blog _Javorové lístky_. You can read it
comfortably at [honzajavorek.cz][blog] if you know Czech. It is
proudly powered by [Python][python] using [Pelican][pelican], [Markdown][markdown],
and [Jinja2][jinja].

GitHub [pull requests][pull_requests] fixing typos in my articles are very welcome! :-)


### License

(cc) 2007–2012 Jan Javorek.

This work is licensed under a Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported License.

https://creativecommons.org/licenses/by-nc-sa/3.0/


--------------------------------------


Toto je zdrojový kód mého blogu _Javorové lístky_. Můžeš si jej pohodlně
přečíst na [honzajavorek.cz][blog]. Velice hrdě se hlásím k tomu, že celá
tahle sranda běží na [Pythonu][python] a to díky nástrojům [Pelican][pelican],
[Markdown][markdown] a [Jinja2][jinja].

Vítám opravy překlepů a hrubek v článcích přes GitHub [pull requests][pull_requests]! :-)


### Licence

(cc) 2007–2012 Jan Javorek.

Toto dílo podléhá licenci Creative Commons
Uveďte autora-Nevyužívejte dílo komerčně-Zachovejte licenci 3.0 Česko.

https://creativecommons.org/licenses/by-nc-sa/3.0/cz/


[python]: http://www.python.org
[blog]: http://www.honzajavorek.cz
[pelican]: https://github.com/ametaireau/pelican
[markdown]: http://daringfireball.net/projects/markdown/
[jinja]: http://jinja.pocoo.org/
[pull_requests]: http://help.github.com/send-pull-requests/


## Installation

This installation guide is for Ubuntu Linux in 7 simple steps. It's remainder for me in case I would forget how to run the blog on my computer.

1. Clone the code. `git clone git@github.com:honzajavorek/blog.git`
2. `cd blog`
3. Create a new Python virtual environment. `virtualenv env --distribute`
4. Activate the environment. `. env/bin/activate`
5. In virtual environment, install all Pythonic requirements. `pip install -r requirements.txt`
6. Install SASS. `apt-get install ruby rubygems && gem install sass`
7. Run it. `start.sh`

