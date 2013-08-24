
import re
import os


if __name__ == '__main__':
    url_map = {}
    slug_map = {}
    filenames = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    for filename in filenames:
        basename, ext = os.path.splitext(filename)
        if ext == '.md':
            date, slug = basename.split('_', 1)
            print date, slug
            url_map['http://honzajavorek.cz/blog/' + slug] = filename
            slug_map[slug] = date

    def repl(match):
        url = match.group(0)
        try:
            print 'REPL: (|filename|' + url_map[url], ' <= ', url
            return '(|filename|' + url_map[url]
        except KeyError:
            print 'ERROR: ' + url
            return url

    def repl2(match):
        slug = match.group(1)[:-3]
        print 'REPL: ', slug_map[slug], '_', slug, ' <= ', slug
        return slug_map[slug] + '_' + slug

    for filename in url_map.values():
        print filename
        with open(filename, 'r') as f:
            content = f.read()

        content = re.sub(r'\(/?images/([^\)]+)\)', r'(|filename|/images/\1)', content)
        content = re.sub(r'\(/?files/([^\)]+)\)', r'(|filename|/files/\1)', content)

        content = re.sub(r'\((http://honzajavorek.cz/blog/[^\)#]+)', repl, content)
        content = re.sub(re.escape(r'\d{4}\-\d{2}\-\d{2}\_') + r'([^\)#]+)', repl2, content)
        content = re.sub(r'(\d{4}\-\d{2}\-\d{2}\_[^\)#]+)', r'\1.md', content)

        with open(filename, 'w') as f:
            f.write(content)
