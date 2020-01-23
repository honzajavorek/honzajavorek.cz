Title: How I deploy
Image: images/andy-li-CpsTAUPoScw-unsplash.jpg
Twitter-Comments: https://twitter.com/honzajavorek/status/1220484534514393089
HackerNews-Comments: https://news.ycombinator.com/item?id=22133377


I'm a dev with **no passion for ops**. Everyone around me is hyped up about Docker, Kubernetes, and whatnot. For me, these things are a waste of time. It's something which I think should be solved _for_ me, not _by_ me. I'm here to develop amazing things, not to mess with server configuration. Still, I need to publish my amazing things to the internet somehow, right? Let me present my go-to solutions to the problem.

![Ops]({static}/images/andy-li-CpsTAUPoScw-unsplash.jpg)
Photo by [Andy Li](https://unsplash.com/@andasta)

Before I start, a disclaimer. I'm not saying ops have no value. It's just **my preference**. I don't find any enjoyment in ops. I can do ops if I'm forced to, but usually, I do everything I can to avoid it. If you like ops, I admire you! Go on, spend hours playing with YAMLs (instead of me!) if that's your thing. You have my deepest respect and full support. I'll be writing the docs you hate to write and eventually, everyone will be happy.

Especially on my projects or those [Czech Python user group](https://python.cz/en/) projects where I'm the maintainer, I can't _afford_ ops. I couldn't be maintaining so many of them in a single person if I needed to care about ops. To keep them sustainable, I must follow certain requirements:

-   **Easy to use.** Static, serverless.
-   **Free or very affordable.** 99.99% of the projects are nonprofit.
-   **Easy to explain** to someone else, so I'm not the sole maintainer forever. Relevant for the community projects.
-   **Easy to maintain.** If something breaks, I can fix it a week or two later, and the website stays up meanwhile.

What I should probably also mention is that all of my projects are **Open Source repositories hosted on GitHub**. Even my most serious and partially commercial project, [junior.guru](https://junior.guru/), is [open to everyone](https://github.com/honzajavorek/junior.guru). It makes my life a lot easier as many services have a free offering for public projects. I have little to no experience with managing private personal projects, so I can't advise about that.

## Content-heavy websites

In case I need to deploy a website, which has mostly text and no dynamic features, I make sure it is a _static_ website. There's no reason why such a project shouldn't be a static website, and the fact it is one simplifies _everything_.

Currently, my favorite place where I put my static websites is [ZEIT Now](https://zeit.co/). Quickstart:

```bash
$ npm install now --global
$ mkdir hello
$ cd hello
$ echo "Hello!" > index.html
$ now  # done, you have the site deployed
```

That example above is pretty much how I made and deployed my wedding website. One thing I love about Now is their **focus on simplicity**. The service provides me with easy solutions to my complicated problems. It allows me to specify redirects. It gives me live previews of my GitHub branches. It automatically handles HTTPS for me. My wedding website had HTTPS! Why? Because why not! I got it for free. And if I ever need something dynamic, Now works also as a serverless functions provider - but about that later.

Before I discovered Now, I used to put my projects to [GitHub Pages](https://pages.github.com/). There are multiple ways how to use them. They offer built-in [Jekyll](https://jekyllrb.com/), so it's probably **the easiest way someone can make a website using GitHub, without messing with technology way too much**. I recommended it to my brother when he wanted a solution for his [small site with ideas on Arduino projects with children](https://github.com/javorekm/arduino-deti), and I still recommend it for similar use cases.

Another way to use GitHub Pages is to skip Jekyll and manage the files yourself. You push your static files to a branch in your GitHub repo and GitHub Pages put it to the internet as it is. This approach still survives in many projects I previously touched, but I find Now superior these days.

[Netlify](https://www.netlify.com/) is, from what I understand, ZEIT's main competitor. I've never found time to try it out, and with Now in my toolbelt, I never really had a reason. Go and explore it for yourself.

## Dynamic content-heavy websites

You may think that your website **can't be static** because it contains some dynamic elements. Well, some people find excuses, some people look for solutions. Let's say your website needs to download calendar data from multiple sources, and then display it aggregated. Something like our Czech Python user group [events page](https://python.cz/en/events/#events). That's pretty dynamic content, right?

The key here is to realize _how much_ dynamic you need the page to be. The events page? Do I need to serve every visitor of the website with freshly baked aggregated events? Every second? Nah! I'm okay if it gets **refreshed daily**.

So you can have many projects as a static website, no problem. You need a **static site generator**, and you need to set up a **scheduler** to re-generate the website for you on the desired interval.

I experiment with this approach since 2012 when I employed it as an affordable and minimalistic way to deploy my hobby project [Žít kino](https://github.com/zitkino/zitkino.cz). Today it's becoming a trendy new approach to design and deploy websites. Wow!

![Doge Meme]({static}/images/static-site-doge.png)

### Static site generators

There's a site full of static site generators, [staticgen.com](https://www.staticgen.com/). I already mentioned Jekyll, which you get with GitHub Pages out of the box. Go browse the list and choose something you like.

![StaticGen.com]({static}/images/staticgen.png)
The staticgen.com website is hosted and maintained by Netlify, so you may notice Netlify ads all over the content, but they're pretty noninvasive. Interestingly, [staticgen.org](https://staticgen.org) leads to a ZEIT Now landing page :D I sense a subtle war.

Both ZEIT Now and Netlify support many of the popular static site generators **out of the box** and have [tutorials](https://zeit.co/docs/v2/build-step) on how to set up your project. If that's not enough for you, you can always have a custom build step.

As you might have noticed, this is quite **hyped up and heavily JavaScript-oriented field** right now. It's because JavaScript folks are re-inventing the whole static websites concept with the [Jamstack](https://jamstack.wtf/) architecture. If you're into React, check it out. Keywords: [Gatsby](https://www.gatsbyjs.org/) vs [Next.js](https://nextjs.org/), [GraphQL](https://graphql.org/), [React](https://reactjs.org/).

If you're a boring old fart like me or if you don't want to spend the rest of your life regularly upgrading your 4200 npm dependencies on each of your hobby projects (remember the **Easy to maintain** requirement?), skip it. I'd say the JavaScript ecosystem is great and it drives interesting innovations, but it's a nightmare to maintain if you can't attend to your projects on a very regular basis.

What do I do instead? I create a **good old Python website** using [Flask](https://flask.palletsprojects.com/), and then I use [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) to turn the app into a static website. I can write **good old HTML** using [Jinja2](https://palletsprojects.com/p/jinja/), which is what old farts like me enjoy to do, and despite developing a dynamic Python app, in the end, I have a directory full of static HTML, CSS, and images, which I can easily deploy anywhere.

A lot of projects I started are using this approach, especially the ones I made for the Czech Python user group, such as [python.cz](https://github.com/pyvec/python.cz/) or [pyvec.org](https://github.com/pyvec/pyvec.org/). As I mentioned, before I discovered ZEIT Now, I used to deploy to GitHub Pages, so that's what these projects use. I found [ghp-import](https://github.com/davisp/ghp-import) to be a handy tool for getting your static files to GitHub. As the combination of Frozen-Flask and ghp-import started spreading across the Czech Python user group websites, my friends packaged the deployment process into a cute tool called [Elsa](https://github.com/pyvec/elsa/).

### Schedulers

You might have heard about [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration), often shortened to CI. I won't go deep into explaining what it is, because in this case, I don't necessarily follow the _practice_ of continuous integration. **I take the CI tooling and abuse it so it works as a scheduler for me.** You might have noticed the idea in my [previous article about learning Haskell]({filename}/2020-01-14_courting-haskell.md).

My favorite service providing CI tooling is [CircleCI](https://circleci.com/). It has a very good free offering for Open Source projects, which now includes [Windows builds](https://circleci.com/build-environments/windows/) (free for Open Source! OMG! I'm already [using it](https://github.com/honzajavorek/cojeapi/blob/d2ea2d9d928c46141e30fbd9fc5e1b4779f5f7ca/.circleci/config.yml#L24)!), workflows, and whatnot. Moreover, they have excellent docs on everything. Despite the fact it gets configured by not-exactly-short YAML files, I happily play with it like I used to play with LEGO bricks in my childhood. Look, look, I built a castle!

![CircleCI madness]({static}/images/circleci-madness.png)

Enough praise! Back to the scheduler. CircleCI [allows you to schedule a build](https://circleci.com/docs/2.0/workflows/#scheduling-a-workflow) with the [crontab syntax](https://crontab.guru/). Check out the docs, they have examples on how to do _nightly builds_, which is essentially what I'm doing with my websites to re-generate them at least once per day. You add a config file to your repository, connect CircleCI, and that's it. CircleCI runs whatever you told it to run, at the time you specified. You can run your dynamic stuff, generate static files, and [deploy them to Now](https://github.com/mvxt/zeit-now) or wherever else you prefer. Daily, or every hour.

<small>**Appeal:** Please run your stuff with the least frequency you need. Spinning up builds every 5 minutes for no good reason burns rainforests and kills kittens.</small>

Not long ago GitHub introduced [Actions](https://github.com/features/actions), which is a **built-in GitHub CI**. I [tried it out](https://github.com/honzajavorek/honzajavorek.cz/actions) with [honzajavorek.cz](https://honzajavorek.cz/) (this website you are reading). Conveniently, you don't need to employ an external service to get a scheduler or a simple CI build. It seems it can do a lot of stuff CircleCI can do, but I didn't play with it much, so I won't do a serious comparison. It's a viable option and I'll probably use it with my future projects if I don't need anything special.

In the past I used to roll with **Travis CI**, like everyone else in the Open Source world, but compared to CircleCI, it's now slow, unreliable, and the configuration is a pure hell of duct-taping random stuff together. Also, the [scheduler they provide](https://docs.travis-ci.com/user/cron-jobs/) is not as flexible. They got acquired in 2019 and then [terminated a lot of people](https://twitter.com/ReinH/status/1098663375985229825), so who knows in which state the business is. RIP, I guess. Thanks for teaching the Open Source world what CI is!

One brilliant thing about ZEIT Now or Netlify is that they offer a way to **trigger a re-build of your website if something happens**. This is usually called webhooks or [deploy hooks](https://zeit.co/docs/v2/more/deploy-hooks). So apart from having the site re-built at least once per day, you can integrate things so your project also gets re-built e.g. after someone tweets, submits a form, publishes an article, you name it.

A convenient side-effect of this architecture is that if there's a bug or outage of a 3rd party service, your website stays resilient. Yes, your deploy fails, your build is red, **the site won't get the latest update, but it's up!** You have days, possibly weeks to fix it, while your users can still access the last successfully deployed version of your project.

## Blog

I consider a blog to be a special case of a static site, you just need to drop comments. Many [static site generators](https://www.staticgen.com/) are in fact **static blog generators**, or at least they started as blog generators and then evolved (the same way WordPress did).

They all work the same way. You have a directory where you put text files, each of them representing an article on your blog. Then you run a CLI program that reads the files and produces HTML, CSS, etc. into an output directory. Then you deploy the output directory as a static site.

**I'm personally happy with [Pelican](https://docs.getpelican.com/).** [Since December]({filename}/2019-12-31_reviving-my-blog.md) I even use its [unique feature for having articles in multiple languages](https://docs.getpelican.com/en/stable/content.html#translations). While Pelican works well for my personal needs ([this whole website is Pelican!](https://github.com/honzajavorek/honzajavorek.cz)), I wonder if there's something more beginner-friendly, or let's say user-friendly, which could be used for our community blog at [blog.python.cz](https://blog.python.cz/). Currently, it sports Pelican too, but I feel that it's not so welcoming to less tech-savvy people or just people who want to write articles but don't want to `git clone` repositories, install dependencies, and so on. I've noticed the following tweet and I hope it could lead to a nice solution, but I didn't have time yet to properly check it out.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Did you know that you can write blog posts for <a href="https://twitter.com/github?ref_src=twsrc%5Etfw">@GitHub</a> Pages using MS Word or Google Docs, including pasting images straight into your doc, and have it all synced to GitHub and included in your blog?<br><br>Here's how it's done! <a href="https://www.fast.ai/2020/01/18/gitblog/">https://www.fast.ai/2020/01/18/gitblog/</a></p>&mdash; Jeremy Howard (@jeremyphoward) <a href="https://twitter.com/jeremyphoward/status/1218662038752202753?ref_src=twsrc%5Etfw">January 18, 2020</a></blockquote>

## Documentation

Another special case of a static site is documentation. I happen to like writing documentation and **I usually do it with [Sphinx](https://www.sphinx-doc.org/)** covering my back. [ReadTheDocs](https://readthedocs.org/) used to be my go-to solution for deployment, but lately, I feel ZEIT Now eats its lunch, at least from my point of view.

I migrated my [API materials for beginners](https://cojeapi.cz/) to Now and I have live previews of my GitHub branches and more control over the build process (e.g. I can stop it if my automated checks find something's wrong). The Czech Python user group documentation, [docs.pyvec.org](https://docs.pyvec.org/), still runs on ReadTheDocs, but already uses the ZEIT Now GitHub integration to get live previews under Pull Requests.

![ReadTheDocs & docs.pyvec.org]({static}/images/readthedocs-pyvec.png)

## Apps

If you can't get away without a true server, there are still some solutions for you where you don't need to touch any Dockerfiles nor Nginx configs. There are at least two options: **PaaS or FaaS** (aka serverless).

### Platform as a Service

Before I discovered things like ZEIT Now and fully embraced the simplicity of static websites, I used to put all my projects to [Heroku](https://www.heroku.com/). It used to have a sensible free tier, a free scheduler for background jobs, and it allowed me to `git push` my code to their infrastructure while they took care of the rest. Then something happened to their free plan and I abandoned it. I don't remember exactly what was it, but I don't use it anymore. I have two hobby projects still hosted on Heroku and I don't touch them as I'm afraid they'd stop working. If they ever need my attention, I'll turn one of them into a static site and the second into something which runs on FaaS.

### Functions as a Service

FaaS is also called _functions_ or _serverless_. It's been hype for a while, so you've probably heard about it. ~~It's PHP re-invented.~~ Every HTTP request to your application gets handled by an isolated piece of code, so-called _lambda_ or _function_. That code **starts its life with the request and ends its life with the response**. That's it. Why it's so cool? First, you delegate all the ops stuff, yay! Second, it scales indefinitely. Third, you pay only for what runs. Main cons? You delegate all the ops (bad debugging, vendor lock-in), and you need to [BYO](https://www.urbandictionary.com/define.php?term=BYO) databases, etc.

It started with AWS Lambda, years ago, but today every cloud offers something like this, even [Google](https://alexolivier.me/posts/deploy-container-stateless-cheap-google-cloud-run-serverless) or [Oracle](https://fnproject.io/). Of course, you can learn all the details for the provider of your choice and set up everything manually in your project, but… that sounds like ops work, right? Well, you can dodge it with a **framework like [Zappa](https://github.com/Miserlou/Zappa), which does it all for you**. Flask? Django? No problem.

To be honest, I never tried out Zappa. I was so late to serverless that when I got to play with it, I had an even easier solution at my hand. As I mentioned earlier **ZEIT Now also works as a FaaS provider**. That's pretty awesome because it allows you to conveniently combine a static website with dynamic serverless code. Deploying a Python app to Now is [quite simple](https://zeit.co/blog/python-wsgi). They support both WSGI (Flask, Django, and everything else) and ASGI (all the shiny new async frameworks), so go an try it out with your next hobby app.

I'm yet to explore this path fully myself, but I already use this option in my [API materials for beginners](https://cojeapi.cz/) (Czech). When people follow the materials, they create their little API from scratch, and in the end, they deploy it to Now. It's nice, because this way they don't need to know any ops stuff to upload their project to the internet and to get a working public URL immediately. From time to time we organize a [workshop](https://cojeapi.cz/workshop.html) based on these materials, and from what I've seen it works pretty well this way even with total beginners.

## Database

If you checked out Heroku or the serverless solutions, you might have noticed that if you need anything else apart from static files and code, you need to get it from somewhere else. Databases are a prominent example.

To be honest, **I avoid databases**. They can be kind of cool, but at the same time, they always felt like a pet that constantly needs attention. I think my projects are not large enough to _deserve_ such a complex piece of software.

If you work with databases daily, you might think - man, what's the deal? You probably don't see it anymore, but databases do require a lot of maintenance: They need to be backed up, thought through (should I put an index here? or there?), secured, accessible, installed on my dev machine, available to my prod app, upgraded, they need drivers, models, migrations, ORMs, blah blah blah… basically, **they eat an enormous amount of time**. On a small hobby project, that's a curse.

Alternatives? In some cases, you can **store the data on disk** in YAML files and `git commit` them as part of your project. This also allows for easy Open Source contributions to the data. This is [how we store data for the python.cz website](https://github.com/pyvec/python.cz/tree/c45d47b/pythoncz/static/data) or what [Pelican](https://docs.getpelican.com/) does (instead of a database, it uses files to store your articles).

And if you really must have something like a database, perhaps you can **fake it till you make it with a Google Spreadsheet**. No, I'm not kidding. Having your data in a sheet is a perfectly viable option for a small project. It gives you a reliable, kind of backed-up database with authorized access, which has a nice administration interface out of the box (where you can invite also non-developers to perform back-office tasks in an environment they are familiar with), and you can even accept new data using Google Forms.

![Google Spreadsheets DB]({static}/images/google-spreadsheets-db.png)

This is exactly how I power the job board at [junior.guru](https://junior.guru/). I get the data from Google using the [gspread](https://github.com/burnash/gspread) library and that's it. Well, as the project grows, I introduced an intermediary [SQLite](https://sqlite.org/), where I put the data so I could comfortably query them in my app with [Peewee](http://docs.peewee-orm.com/), a minimalistic ORM. But that came only as the app continued to grow, and it still allows me to avoid a lot of hassle proper databases bring.

I have to admit **SQLite**, a database working on top of a file or memory is a nice tool I've been overlooking and underestimating for a long time. It's dead simple, but [powerful](https://github.com/simonw/datasette). And [languages have it built in](https://docs.python.org/3/library/sqlite3.html)!

## E-mail

I use [ImprovMX](https://improvmx.com/) to **redirect my e-mails**. If you send something to `hello@junior.guru`, it gets redirected to my personal GMail address. I only automatically flag it with a yellow label. I'm new to ImprovMX, but so far it seems to work reliably. I just hope they don't read all the messages and sell the data to the Russia, or worse, to Facebook. Or to Google. Oh, wait…

ZEIT Now requires me to use their DNS if I want a custom domain or HTTPS out of the box, so I use the Now CLI to set up ImprovMX where I need:

```text
$ now dns add junior.guru '@' MX mx1.improvmx.com 10
$ now dns add junior.guru '@' MX mx2.improvmx.com 20
```

## Dependencies

One slightly unrelated, honorable mention I want to make: [@dependabot](https://dependabot.com/).

A few lines above I'm making fun of the sheer amount of dependencies one needs to have to create a decent JavaScript project, but even with Python you often end up with a total tree of tens of packages in your dependencies. Tens are not much, but still more than I want to deal with manually, especially if I have ten projects to maintain.

It's fairly easy to turn on [GitHub Alerts](https://help.github.com/en/github/managing-security-vulnerabilities/about-security-alerts-for-vulnerable-dependencies) or [Snyk](https://snyk.io/) to get notified when the dependencies have **security issues**, but how do you keep them up to date? Manually?

You may think it's not important to keep dependencies up to date, but trust me, it is. Not just because of security. It's because often you get to your project after a while and try to develop something, but then you figure out you need to upgrade dependencies to have it done, and then, fast forward a few hours, **your precious evening dedicated to your hobby project got wasted on upgrading random outdated packages** and resolving issues the upgrades bring.

Upgrading packages gradually over time allows you to do this in small, easy-to-digest chunks. [@dependabot](https://dependabot.com/) does this for you. It monitors your dependencies and automatically sends Pull Requests with upgrades. If you have tests and CI set up on your project, **it can even auto-merge the upgrades** if the CI check passes. How cool is that? I use it on most projects, both personal and community ones.

## Summary

This is what happens when I decide to write a short article about a few interesting things I use. I'm sorry! I hope you liked the overview and learned about options on **deploying your projects with the smallest or no effort in ops, the smallest maintenance footprint, and for no money**. I hope this allows people to realize how easy is to put something into the world today. Now go and create something awesome, the internet is waiting!
