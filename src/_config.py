# -*- coding: utf-8 -*-


site.url = 'http://blog.javorek.net'


# Blog

blog = controllers.blog
blog.enabled = True

blog.path = ''
blog.name = u'Javorové lístky'
blog.description = 'Sepisuje Honza Javorek'
blog.timezone = "Europe/Prague"
blog.posts_per_page = 5

blog.auto_permalink.enabled = True
blog.auto_permalink.path = ':blog_path/:title'

blog.disqus.enabled = True
blog.disqus.name = "littlemaple"

blog.custom_index = False

blog.post_excerpts.enabled = True
blog.post_excerpts.word_length = 100

