Title: Reviving my blog
Date: 2019-12-31 14:36:00
Lang: en
Twitter-Comments: https://twitter.com/honzajavorek/status/1212446176903094273
LinkedIn-Comments: https://www.linkedin.com/posts/honzajavorek_reviving-my-blog-honza-javorek-activity-6618211942764949504-dq6D
Facebook-Comments: https://www.facebook.com/honzajavorek/posts/10157684811687707


This blog hasn't seen a new article for almost a year and half now. **It's not dead though** - at least not on purpose. I still think about article ideas, and about finding time to sit down and publish new texts here. It's just that lately I was quite busy (getting married, leaving my job…) and blogging wasn't my priority. I'd like to get back to it now, with a few things changed.

## So old that it's cool again

Sure, I know it's 2020 in a few hours. I know blogging is way past its original charm and in 2020 I should definitely go with a YouTube channel, SoundCloud podcast, or at least turn this into a Substack newsletter. Well, thanks but no. This blog has existed since 2007 and it's going to go on as it is - my personal, **independent** platform for sharing my thoughts in a written form. First, I like writing, and second, I like the fact that this site is just a boring text inside a boring HTML file, hosted on my own boring domain. Because that's how it survived 10+ years. It's a relict of the oldschool web, where sites were made for fun and not for profit.

## Purer

I wanted to embrace this with my latest changes. **I removed all share buttons, Twitter's scripts, Google's fonts. I removed Disqus comments.** If you wish to react to my articles, use social network of your choice - it is their job to fascilitate discussions. I'm keeping backup of the original comments made here under the old articles and maybe one day I'll parse the backup and display the comments statically under the texts, but it's not on my list right now. Also, I'm still keeping Google Analytics, but perhaps in the future that will go as well.

## Simpler

I got inspired by the [Manifesto for Preserving Content on the Web](https://jeffhuang.com/designed_to_last/). I made the design simpler. I removed a lot of complexity which got here over the years. Not so long ago I built a new homepage at [honzajavorek.cz](https://honzajavorek.cz), with a refreshed design and updated info, but I made it using a separate app written in [Flask](http://flask.pocoo.org/) and deployed using [Flask-Frozen](https://pythonhosted.org/Frozen-Flask/), while the rest of the site was still using [Pelican](https://docs.getpelican.com/). Because I wanted to be cool, I made the homepage app very "automagic" and modern, which manifested mainly in using [SCSS](https://sass-lang.com/) for the design or Gravatar for my photo instead of a simple JPEG file.

Also, the blog wasn't using just Pelican. In the past I thought it's smart to create a package called [danube-delta](https://github.com/honzajavorek/danube-delta/) with shared configuration, theme, and plugins. This has been used on my site as well as on two other blogs, including the [blog.python.cz](http://blog.python.cz/), effectively turning them all into a distributed maintenance nightmare. Also the deployment was a duct-taped piece of crap, which included custom scripts, [CircleCI](https://circleci.com/) night builds, [GitHub Pages](https://pages.github.com/), and many more pieces making the whole thing complex in the first place. The package was also trying to "automagically" create thumbnails, or make many other implicit guesses.

> Beautiful is better than ugly.<br>
> Explicit is better than implicit.<br>
> Simple is better than complex.<br>
>
> &mdash; [Zen of Python](https://www.python.org/dev/peps/pep-0020/)

I migrated the site to use Pelican exclusively. I replaced `pipenv` with good old `pip`. I rewritten everything into plain HTML, plain CSS, and plain ES5 JavaScript. I created an updated design for the blog matching the new homepage. It is even simpler than the previous one which I thought is the simplest possible. I'm not using any CSS frameworks or even CSS resets! The basic browser styling works pretty well so far, I only adapted it. I'm using default fonts and static JPEG images, now manually optimized with [imagemin](https://github.com/imagemin/imagemin-cli). I'm not doing any "automagic" transformations. I still have a few Pelican plugins, but they only fix a few things in the markup. Instead of "automagically" guessing what should be an article's image for previews on social media, I'm setting it explicitly in the article's metadata. Instead of generating thumbnails for large photos, I check size of the linked photos and if they're too large, I simply fail the build to deal with it manually.

**The danube-delta package needs to go.** In a way, it was an attempt to make Pelican more user-friendly for non-developers, but I think if that's a requirement, Pelican shouldn't be used. We should use something else for [blog.python.cz](http://blog.python.cz/), something focused on users in the first place, and then perhaps just automatically backup the site as static HTML or as Markdown files.

## Using GitHub Actions and ZEIT Now

I removed CircleCI in favor of built-in [GitHub Actions](https://github.com/features/actions), but I replaced GitHub Pages with [ZEIT Now](https://zeit.co/), my current favorite place for hosting static pages. It gives me CDN, HTTPS, automatic deploys of my GitHub branches for live previews, and many more, including dynamic lambdas if I ever need them. Pelican isn't supported directly, so I needed to write custom `now.json` and `now.sh` files (see [the code here](https://github.com/honzajavorek/honzajavorek.cz)), but it still feels somewhat more straightforward than deploying to GitHub Pages with the `gh-pages` branch and the `gh-import` utility, which was the previous setup here. Since ZEIT Now requires me to use their DNS, I'm using [ImprovMX](https://improvmx.com/) for e-mail forwarding now instead of WEDOS, my domain name registrar.

## Polyglot

One completely new thing here is an **explicit support for translations**, which is available in Pelican [out of the box](https://docs.getpelican.com/en/stable/content.html#translations). I had to tweak it a bit so it was able to keep my old URLs, but otherwise it seems to work like a charm - see [Testing in JavaScript and in Python]({filename}/2017-01-18_testing-in-javascript-and-in-python.md) for example. Any article can now clearly declare in which language it is written and translations are nicely interlinked. This also brings me to the fact that from now on, this blog won't continue with the name "Javorové lístky" anymore as I want my new articles to be primarily in English.

## HJ's blog

Yeah, dropping the original name makes me sentimental too, but that's life. I can't really translate the name literally (misguided [Maple Leafs](https://www.nhl.com/mapleleafs/) fans would start hitting my articles) and I was lazy to come up with a new cool name. There's no need for a separate brand name. From now on, this is just "my blog". **HJ's blog.** One era ends, another begins.
