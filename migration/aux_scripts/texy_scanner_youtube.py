# -*- coding: utf-8 -*-


import sys
import os.path
from glob import glob
import re
import requests


texy_directory = sys.argv[1].rstrip('/') # directory with texy posts


re_texy_embed = re.compile(r'\[\*\s+http[^\*]+\*\]')


for texy_filename in glob('%s/*.texy' % texy_directory):
    with open(texy_filename) as f:
        texy_contents = f.read().decode('utf-8')

    texy_embeds = re_texy_embed.findall(texy_contents)

    if texy_embeds:
        texy_basename = os.path.basename(texy_filename)
        print '%s' % texy_basename

        for i, texy_embed in enumerate(texy_embeds):
            print '\t%s' % texy_embed.encode('utf-8')
            print ''
