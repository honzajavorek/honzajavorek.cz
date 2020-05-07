# honzajavorek.cz

[Honza Javorek](https://github.com/honzajavorek)'s personal site and blog. Powered by [Pelican](https://docs.getpelican.com/), a static site generator written in Python.

## 👩‍💻 Installation & Usage

For installation, see the CI configuration in `.github/workflows/build.yml`. For usage, see the [Pelican docs](https://docs.getpelican.com/en/stable/publish.html#site-generation).

## 📒 Content

Most of the project consists of my blog. The content (articles, images…) can be found in the `content` directory. The blog uses Markdown with a few extensions. The basic Pelican structure is a bit altered. Many pages generated by Pelican by default are disabled in the configuration. There are no categories, author pages, tags. Only three pages are in use: index, archives, article.

Unpublished articles are in `content/draft` directory. They're deleted in `.github/workflows/build.yml` before the site gets deployed, so they in fact never make it into production.

## 🎨 Theme

There is a custom theme in the `theme` directory. There's no intention to use the theme anywhere else, thus with a lot of things hardcoded. It turns the index page into my personal site, and the archives page (saved as `./blog/index.html`) into something one could call a true index page for the blog. Then there are individual article pages and that's it. The article template is in Czech for Czech articles, otherwise in English. The rest is in English exclusively.

The theme uses standard CSS and ECMAScript 5 for simplicity and resiliency.

## ⚙️ Plugins

For the personal site (the index template) to work properly, there are a few plugins injecting additional data to Pelican's context. They're prefixed with `home_` so they're easy to distinguish. They pick up static data from `content/data` or fetch it from the internet by external HTTP requests.

The `alternates` plugin looks for meta data ending with `-url` in the articles and provides a list of alternate places where the article has been published. As an example, `Zdrojak-URL: https://zdrojak.cz/my-article` would appear as an alternate in the article's meta data.

The `comments` plugin looks for meta data ending with `-comments` in the articles and provides a list of places where the article has been shared and where people can discuss it. As an example, `Twitter-Comments: https://twitter.com/honzajavorek/status/1a2b3c4d5` would appear in the `comments` list in the article's meta data.

The `custom_feed_meta` overwrites Atom feed's top-level meta data with values from configuration.

The `custom_transaction_id` plugin and related settings for translation URLs allow for translations of articles with backward-compatible URLs (independent slugs with no implicit language identifier in the URL).

The rest of the plugins are mostly minor automatic tweaks to the generated article markup.

## 📸 Adding Images

Drop them into the `content/images` directory and let the blog reload. If it's too large, it'll error with details. Resize large images to fit the constraints reported by the error messages. Ideally also run following to optimize images:

```
$ imagemin content/images/*.* --out-dir=content/images
```

The `imagemin` utility can be installed by ``npm install imagemin-cli --global``.

## 🇨🇿 Translations

To connect translations, add `Translation-ID` to their meta data with the same value, and set their `Lang` properly. The default language is `en`.

## 📚 Alternates

To document where the article has been re-published, add the URLs to the meta data as `<whatever>-URL` properties. E.g. `Zdrojak-URL`, `Medium-URL`, or `DevTo-URL`.

## 💬 Comments

To document where on social networks the article has been shared, add the URLs to the meta data as `<whatever>-Comments` properties. E.g. `Twitter-Comments`, `LinkedIn-Comments`, or `Facebook-Comments`. Links should appear under the article.

## 🖼 Open Graph Image

By default, the Open Graph image is set to my photo. To set a different image, add it to the `content/images` directory and set the `Image` meta data property in the article to the path to the image, e.g. `Image: images/foo.jpg`.

## 📦 Dependencies

The npm dependencies of the theme are managed in a standard way, but the `package.json` is inside the `theme` directory and the dependencies are saved as exact versions (see `.npmrc`) as [@dependabot](https://dependabot.com/) takes care of upgrading (see `.dependabot`). Python dependencies are using plain old `requirements.txt`, but it's not used as a lockfile. Only the top-level dependencies which are truly needed are written and locked there, with the resulting tree being left unmanaged. Again, [@dependabot](https://dependabot.com/) takes care of upgrading.

## 🚀 Deployment

Each commit to `master` runs a [GitHub Actions](https://github.com/features/actions) build which automatically deploys the site to [GitHub Pages](https://pages.github.com/). The configuration is in `.github/workflows/build.yml`.

As certain content on the homepage is dynamic, the site should be re-generated at least once a day. This is achieved using a scheduled workflow (see `.github/workflows/build.yml`).

## 📪 Domain

The site runs under custom domain `honzajavorek.cz`. The HTTPS is turned on in the GitHub Pages repository settings.

The domain's DNS is managed by [WEDOS](https://www.wedos.cz/). E-mail redirecting is done by [ImprovMX](https://improvmx.com/).

CSV export from WEDOS:

```
"";"název";"TTL";"typ";"data"
"";"";"3600";"A";"185.199.110.153"
"";"";"3600";"A";"185.199.111.153"
"";"";"3600";"A";"185.199.108.153"
"";"";"3600";"A";"185.199.109.153"
"";"";"300";"MX";"20 mx2.improvmx.com"
"";"";"300";"MX";"10 mx1.improvmx.com"
"";"prazeni";"3600";"CNAME";"honzajavorek.github.io"
"";"www";"3600";"CNAME";"honzajavorek.github.io"
```

## 👀 License

See [LICENSE](LICENSE). **TL;DR** is that the code is [MIT](LICENSE.MIT) and the content is _my precious_. If you wish to re-publish the texts or translate them, I'm usually fine with it, but let me know first.
