# -*- coding: utf-8 -*-


import sys
import os.path
from glob import glob
import re
import requests


texy_directory = sys.argv[1].rstrip('/') # directory with texy posts
md_directory = sys.argv[2].rstrip('/') # directory with markdown posts
images_directory = os.path.join(md_directory, 'images')


re_texy_image = re.compile(r'\[[\<\>\*][ x\?0-9]+[\<\>\*]\]')
re_texy_embed = re.compile(r'\[[\<\>\*][^\]]+[\<\>\*]\]')
re_texy_ext = re.compile(r'\.texy$')
re_md_image = re.compile(r'\!\[[^\]]+\]\(http[^\)]+\)')
re_md_image_url = re.compile(r'\!\[image\]\(([^\)]+)\)')
re_texy_image_float = re.compile(r'([\*\<\>])\]$')
re_texy_image_number = re.compile(r'^\[[^0-9]+([0-9]+)')


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

                match = re_md_image_url.match(md_image)
                url = match.group(1)
                print '\tURL: %s' % url

                r = requests.get(url)
                _, ext = r.headers['content-type'].split('/')
                ext = 'jpg' if ext == 'jpeg' else ext

                match = re_texy_image_number.search(texy_image)
                number = match.group(1)

                image_filename = os.path.join(images_directory, str(number) + '.' + ext)
                image_basename = os.path.basename(image_filename)
                print '\tFILE: %s' % image_basename

                if not os.path.isfile(image_filename):
                    with open(image_filename, 'w') as f:
                        f.write(r.content)
                    print '\t(DOWNLOADED)'
                else:
                    print '\t(PRESENT)'

                match = re_texy_image_float.search(texy_image)
                float_dir_char = match.group(1)
                float_dir = ''
                if float_dir_char == '<':
                    float_dir = '{: .left }'
                elif float_dir_char == '>':
                    float_dir = '{: .right }'
                print '\tFLOAT: %s' % float_dir

                new_md_image = u'![obrázek](images/%s)%s' % (image_basename, float_dir)
                with open(md_filename, 'w') as f:
                    md_contents = re.sub(re.escape(md_image), new_md_image, md_contents)
                    f.write(md_contents.encode('utf-8'))

            except IndexError:
                print '\tBad index: %s' % texy_image

            print ''

# ![image](http://blog.javorek.net/image/131/){: .left }