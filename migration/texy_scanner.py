# -*- coding: utf-8 -*-


import sys
import os.path
from glob import glob
import re


texy_directory = sys.argv[1].rstrip('/') # directory with texy posts
md_directory = sys.argv[2].rstrip('/') # directory with markdown posts


re_texy_image = re.compile(r'\[[\<\>\*][ 0-9]+[\<\>\*]\]')
re_texy_embed = re.compile(r'\[[\<\>\*][^\]]+[\<\>\*]\]')
re_texy_ext = re.compile(r'\.texy$')
re_md_image = re.compile(ur'\!\[[^\]]+\]\([^\)]+\)')


for texy_filename in glob('%s/*.texy' % texy_directory):
    with open(texy_filename) as f:
        texy_contents = f.read().decode('utf-8')

    texy_images = re_texy_image.findall(texy_contents)

    if texy_images:
        texy_basename = os.path.basename(texy_filename)
        md_basename = re_texy_ext.sub('.md', texy_basename)
        md_filename = os.path.join(md_directory, md_basename)

        print ('%s → %s' % (texy_basename, md_basename))
        with open(md_filename) as f:
            md_contents = f.read().decode('utf-8')

        md_images = re_md_image.findall(md_contents)

        for i, texy_image in enumerate(texy_images):
            try:
                md_image = md_images[i]
                print '\t%s → %s' % (texy_image.encode('utf-8'), md_image.encode('utf-8'))
            except IndexError:
                print '\tBad index: %s' % texy_image
        print '\n'

# ![image](http://blog.javorek.net/image/131/){: .left }