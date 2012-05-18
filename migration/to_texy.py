# -*- coding: utf-8 -*- #


import MySQLdb as db
import envoy
import os


posts_directory = os.path.join(os.path.dirname(__file__), 'texy_posts')


conn = db.connect(host='localhost', user='dev', passwd='dev', db='blog', charset='utf8', use_unicode=True)
cursor = conn.cursor()


cursor.execute('''
    SELECT a.title, a.slug, a.published_at, a.is_published AS is_published, a.content_texy AS texy, GROUP_CONCAT(DISTINCT t.name) AS tags
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
        texy=row[4],
        tags=row[5],
    )


for article in sorted(map(row_to_article, cursor.fetchall()), key=lambda article: article['published_at']):
    filename = ' '.join([str(article['published_at'].date()), article['slug']]) + '.texy'
    content = article['texy']

    with open(os.path.join(posts_directory, filename), 'w') as f:
        f.write(content.encode('utf8'))


cursor.close()
conn.close()

