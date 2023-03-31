Title: Notion as a replacement for Pocket
Image: images/screenshot-2023-03-26-at-16-13-57.png
Lang: en
HackerNews-Comments: https://news.ycombinator.com/item?id=35394677

I know [Notion](https://www.notion.so/) exists, but until now I didn't pay much attention to it.
With my recent transition from social media and [Pocket](https://getpocket.com/) to good old RSS feeds, I've been looking for a way to save random internet articles to a single feed, which I could then put to my RSS reader.

I had a hunch that Notion could help me with that (and perhaps with other stuff, too!) so I've finally found some time to properly play with it.
And indeed, it can really work as a replacement for Pocket, with a little bit of coding.

![Notion as a replacement for Pocket]({static}/images/screenshot-2023-03-26-at-16-13-57.png)

The problem with Pocket is that there is no good way how to get the articles out of it:

-   It has RSS feeds, but they only contain 30 items.
    That is a fact which I not only observed, but also confirmed with their support.
-   It has [data export](https://getpocket.com/export), but I'd need to somehow scrape that.
-   It has an API, but it's 3-legged OAuth 2.0, which means it requires user interaction.
    Such APIs are useless for unattended personal automation.

So I tried Notion:

-   I've made a Notion page with a "database".
-   I've installed Notion on my phone and I've added their [Web Clipper](https://addons.mozilla.org/en-US/firefox/addon/notion-web-clipper/) to my browser.
    At this point I had a place where to put links and an easy way to put them there from all my devices.
-   I've looked at their API and I was very pleasantly surprised!
    It has amazing docs.
    It has an unrivaled approach to auth.
    Everything is very well explained.
    If I want access only to my own data, I just click at the right buttons to get my "integration" created, I get an API token and I can do anything I want with it.
-   I've struggled a bit with a step where I was supposed to share the page with my "integration", because I've been following a tutorial which was based on outdated UI.
    Without this step the "integration" doesn't see the page and can't access the data.
    It took me a while to figure it out, but I like that the permissions are so fine-grained!
-   In a very short time I've been able to write a [Python script](https://github.com/honzajavorek/honzajavorek.cz/blob/a762d2a548dca6f5437930d0c2a10358198e7ac9/blog/reading.py), which uses [notion-sdk-py](https://github.com/ramnes/notion-sdk-py) and [python-feedgen](https://github.com/lkiesow/python-feedgen).
    It reads the links and generates RSS.
    The core of the program has exactly 15 lines.
-   I use GitHub Actions to generate the file once in a few days and publish it to GitHub Pages.
    I've added the URL of my RSS to [NetNewsWire](https://netnewswire.com/).
    Done!

Now I can browse the internet and easily send random articles to my RSS reader.
As a bonus, I have the history in my Notion.
With reader mode ([Firefox](https://support.mozilla.org/en-US/kb/firefox-reader-view-clutter-free-web-pages), [Safari](https://support.apple.com/guide/safari/hide-ads-when-reading-sfri32632/mac)), the reading is as comfortable as in Pocket.

![Screenshot nastavení přístupu do Notion API]({static}/images/screenshot-2023-03-31-at-16-07-01-notion-the-all-in-one-workspace-for-your-notes-tasks-wikis-and-databases.png){: .img-thumbnail }
Notion API auth setup

Besides using Notion for storing links to read, I'll probably move my notes there, too.
I'm not satisfied with Apple Notes and I think Notion might be better fit even for some stuff I use Trello for.
I really like:

-   The flexibility about what you can put there.
-   Combination of text and machine-readable data.
-   Ease of use of their API.
    I can invent all sorts of personal automations like this.
    It feels like my data is there for me to work with, it's not a hostage to their walled garden.
-   They even [have AI now](https://www.youtube.com/watch?v=0DIn0Ws9yTE)!

I'm curious about what else I can build on top of this all.
A page with my personal to-do or with bookmarks related to vacation planning might be a good beginning to get a grip of the UI, but the tool feels much, much more powerful!

**Bonus:** When doing some research, I stumbled upon these two additional links: [notion-into-sqlite](https://github.com/FujiHaruka/notion-into-sqlite) and [apple-notes-to-sqlite](https://datasette.io/tools/apple-notes-to-sqlite).
