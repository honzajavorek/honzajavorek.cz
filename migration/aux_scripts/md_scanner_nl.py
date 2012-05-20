# -*- coding: utf-8 -*-


import sys
import os.path
from glob import glob
import re


directory = sys.argv[1].rstrip('/') # directory with md posts


re_nl = re.compile(r'[^\s]+\n[^\n]{8}')
re_allowed = re.compile(r'\n(\-|\>|\#|[a-zA-Z]+\:)')
re_repl = re.compile(r'\n[\t ]*')
re_img = re.compile(r'\n(\!\[[^\]]+\]\([^\)]+\))\s*([^\{])')


def repl(match):
    nl = match.group(0)
    if not re_allowed.search(nl):
        print repr(nl)
        return re_repl.sub(' ', nl)
    return nl


for filename in glob('%s/*.md' % directory):
    with open(filename) as f:
        contents = f.read().decode('utf-8')

    contents = re_nl.sub(repl, contents)
    contents = re_img.sub(r'\n\1\n\n\2', contents)

    with open(filename, 'w') as f:
        f.write(contents.encode('utf-8'))

