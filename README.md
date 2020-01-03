# honzajavorek.cz

[Honza Javorek](https://github.com/honzajavorek)'s personal site and blog. Powered by [Pelican](https://docs.getpelican.com/), a static site generator written in Python.

## 📒 Content

Most of the project consists of my blog. The content (articles, images…) can be found in the `content` directory. The blog uses Markdown with a few extensions. The basic Pelican structure is a bit altered. Many pages generated by Pelican by default are disabled in the configuration. There are no categories, author pages, tags. Only three pages are in use: index, archives, article.

Unpublished articles are in `content/draft` directory. They're deleted in `now.sh` before the site gets deployed, so they in fact never make it into production.

## 🎨 Theme

There is a custom theme in the `theme` directory. There's no intention to use the theme anywhere else, thus with a lot of things hardcoded. It turns the index page into my personal site, and the archives page (saved as `./blog/index.html`) into something one could call a true index page for the blog. Then there are individual article pages and that's it. The article template is in Czech for Czech articles, otherwise in English. The rest is in English exclusively.

The theme uses standard CSS and ECMAScript 5 for simplicity and resiliency.

## ⚙️ Plugins

For the personal site (the index template) to work properly, there are a few plugins injecting additional data to Pelican's context. They're prefixed with `home_` so they're easy to distinguish. They pick up static data from `content/data` or fetch it from the internet by external HTTP requests.

The `alternates` plugin looks for meta data ending with `-url` in the articles and provides a list of alternate places where the article has been published. As an example, `Zdrojak-URL: https://zdrojak.cz/my-article` would appear as an alternate in the article's meta data.

The `custom_feed_meta` overwrites Atom feed's top-level meta data with values from configuration.

The `custom_transaction_id` plugin and related settings for translation URLs allow for translations of articles with backward-compatible URLs (independent slugs with no implicit language identifier in the URL).

The rest of the plugins are mostly minor automatic tweaks to the generated article markup.

## 🇨🇿 Translations

To connect translations, add `Translation-ID` to their meta data with the same value, and set their `Lang` properly. The default language is `en`.

## 📚 Alternates

To document where the article has been re-published, add the URLs to the meta data as `<whatever>-URL` properties. E.g. `Zdrojak-URL`, `Medium-URL`, or `DevTo-URL`.

## 🖼 Open Graph Image

By default, the Open Graph image is set to my photo. To set a different image, add it to the `content/images` directory and set the `Image` meta data property in the article to the path to the image, e.g. `Image: images/foo.jpg`.

## 📦 Dependencies

The npm dependencies are managed in a standard way, but saved as exact versions (see `.npmrc`) as [@dependabot](https://dependabot.com/) takes care of upgrading (see `.dependabot`). Python dependencies are using plain old `requirements.txt`, but it's not used as a lockfile. Only the top-level dependencies which are truly needed are written and locked there, with the resulting tree being left unmanaged. Again, [@dependabot](https://dependabot.com/) takes care of upgrading.

## 🚀 Deployment

Currently the site uses [ZEIT Now](https://zeit.co/) as a backend. The configuration is in the `now.json` file. A `@now/static-build` with a Bash-based builder is used. The Bash script is in the `now.sh` file. There's a GitHub integration, which automatically deploys branches for previews. The `master` branch is considered production and aliases to the `honzajavorek.cz` domain.

Because Pelican works better with an absolute `SITEURL` set but ZEIT Now doesn't provide it to the static build Bash script, it needs to be fetched manually for the preview builds with randomly generated base URLs. This is achieved by inspecting GitHub deployments and their target URLs through GitHub API. It's a few lines inside the `publishconf.py`. Hopefully this can be simplified one day (see [relevant monologue](https://spectrum.chat/zeit/now/getting-domain-from-within-now-static-build~fd24fe27-36a4-4641-96d1-5e73aedbb9ef)).

As certain content on the homepage is dynamic, the site should be re-generated at least once a day. This is achieved using a [GitHub Actions](https://github.com/features/actions) scheduled workflow (see `.github`).

## 📪 Domain

The domain's DNS is managed by ZEIT. E-mail redirecting is done by [ImprovMX](https://improvmx.com/):

```
$ now dns add honzajavorek.cz '@' MX mx1.improvmx.com 10
$ now dns add honzajavorek.cz '@' MX mx2.improvmx.com 20
```

## 👀 License

See [LICENSE](LICENSE). **TL;DR** is that the code is [MIT](LICENSE.MIT) and the content is _my precious_. If you wish to re-publish the texts or translate them, I'm usually fine with it, but let me know first.
