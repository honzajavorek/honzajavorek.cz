# -*- coding: utf-8 -*-


import sys
import os.path
from glob import glob
import re


directory = sys.argv[1].rstrip('/') # directory with md posts


re_file = re.compile(r'javorek\.net\/file\/')


for filename in glob('%s/*.md' % directory):
    with open(filename) as f:
        contents = f.read().decode('utf-8')

    files = re_file.findall(contents)
    if files:
        print filename
        print files
        print


