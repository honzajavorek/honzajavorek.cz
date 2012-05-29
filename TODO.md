
- Handle redirects from the original blog to the new one.
    ( https://github.com/honzajavorek/maplegarden/blob/master/honza/maplegarden/app/presenters/FeedPresenter.php )
    - http://blog.javorek.net/comments/feed/ - $url = 'http://javorove-listky.disqus.com/latest.rss';
    - http://blog.javorek.net/feed/ - $url = sprintf('http://javorove-listky.disqus.com/%s/latest.rss', str_replace('-', '_', $slug));

- migrate disqus: http://javorove-listky.disqus.com/admin/tools/migrate/
- feed - redirect to the new address permanently, feeds/mail for comments (dsq-subscribe)

Later:
- plain ie/print style
- move videos from my KaniiniLM YouTube account to my honzajavorek accounts (YouTube or Vimeo) and search/replace their codes in posts
- about me: minimalist, short, brief, list of profiles I actively use (github, linkedin, ...), follow me on twitter
