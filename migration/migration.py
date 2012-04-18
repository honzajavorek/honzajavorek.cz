# -*- coding: utf-8 -*- #


import MySQLdb as db
import envoy
import os


posts_directory = os.path.join(os.path.dirname(__file__), '..', 'posts')


conn = db.connect(host='localhost', user='dev', passwd='dev', db='blog', charset='utf8', use_unicode=True)
cursor = conn.cursor()


cursor.execute('''
    SELECT a.title, a.slug, a.published_at, a.is_published AS is_published, a.content_html AS html, GROUP_CONCAT(DISTINCT t.name) AS tags
    FROM article AS a
    JOIN article_tag AS at ON a.id = at.article_id
    JOIN tag AS t ON t.id = at.tag_id
    GROUP BY a.id
''')


def row_to_article(row):

    return dict(
        title=row[0],
        slug=row[1],
        published_at=row[2],
        is_published=row[3],
        html=row[4],
        tags=row[5],
    )


for article in sorted(map(row_to_article, cursor.fetchall()), key=lambda article: article['published_at']):
    filename = ' '.join([str(article['published_at'].date()), article['slug']]) + '.md'

    published_at = article['published_at'].replace(second=0)

    pandoc_response = envoy.run('pandoc -f html -t markdown', data=article['html'].encode('utf8'))
    markdown = pandoc_response.std_out.decode('utf8').strip()

    tags = ', '.join(article['tags'].split(','))

    draft = False
    if not article['is_published']:
        draft = True
        filename = '_' + filename

    meta = (
        ('Title', article['title']),
        ('Date', published_at),
        ('Category', None),
        ('Tags', tags),
        ('Author', None),
        ('Status', 'draft' if draft else None),
    )

    content = ''
    for meta_tuple in meta:
        if meta_tuple[1]:
            content += '%s: %s\n' % meta_tuple
    content += '\n'
    content += markdown

    with open(os.path.join(posts_directory, filename), 'w') as f:
        f.write(content.encode('utf8'))


cursor.close()
conn.close()

