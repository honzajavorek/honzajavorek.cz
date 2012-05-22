# -*- coding: utf-8 -*-


import sys
import os.path
from glob import glob
import re


directory = sys.argv[1].rstrip('/') # directory with md posts


re_link = re.compile(r'')


for filename in glob('%s/*.md' % directory):
    with open(filename) as f:
        contents = f.read().decode('utf-8')

    contents = contents.replace('twitter.com/littlemaple', 'twitter.com/honzajavorek')

    with open(filename, 'w') as f:
        f.write(contents.encode('utf-8'))

