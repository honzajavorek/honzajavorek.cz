# -*- coding: utf-8 -*-


import sys
import os.path
from glob import glob
import re


directory = sys.argv[1].rstrip('/') # directory with md posts


re_link = re.compile(r'http://blog\.javorek\.net[^\s\)\]]+')
re_old_link = re.compile(r'http://blog\.javorek\.net/[\d\/]{10}/[^\s\)]+')
re_slug = re.compile(r'blog\.javorek\.net\/(\d{4}/\d{2}/\d{2}/)?([\w\-]+)(/.*)?')


def repl(match):
    link = match.group(0)
    if re_old_link.match(link):
        print '\t[old] ' + link
    else:
        print '\t[new] ' + link
    slug_match = re_slug.search(link)
    if slug_match:
        slug = slug_match.group(2)
        print '\t[slug] ' + slug

        if slug == 'feed':
            print '\t[feed] ' + link
            new_link = 'http://honzajavorek.cz/blog/feed.xml'
            print '\t[result] ' + new_link
            print
            return new_link

        elif slug == 'wp-content':
            filename = link.replace('http://blog.javorek.net/wp-content/', '')
            path = os.path.join(directory, 'images', filename)
            new_link = 'files/' + filename
            print '\t[wp content] ' + new_link

            if not os.path.isfile(path):
                print '\t[missing file]'
            else:
                print '\t[result] ' + new_link
                print
                return new_link
        else:
            link = 'http://honzajavorek.cz/blog/' + slug
            print '\t[result] ' + link
            print
            return link
    else:
        print '\t[missing slug]'
    print '\t[result] ' + link
    print
    return link


for filename in glob('%s/*.md' % directory):
    with open(filename) as f:
        contents = f.read().decode('utf-8')

    contents = re_link.sub(repl, contents)

    with open(filename, 'w') as f:
        f.write(contents.encode('utf-8'))

