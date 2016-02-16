#!/usr/bin/env python
# Creation of a new article


import os
import sys
from datetime import datetime, timedelta

from slugify import slugify


DIR = os.path.dirname(os.path.realpath(__file__))
POSTS_DIR = os.path.join(DIR, '../content/')

# Read title
title = input('Article title? ').strip()
if not title:
    sys.exit('Error: No title provided.')

# Prepare file name
slug = slugify(title)
pub_date = datetime.now() + timedelta(hours=2)
file_name = '{:%Y-%m-%d}_{}.md'.format(pub_date, slug)

# Prepare file content
template = 'Title: {}\nDate: {:%Y-%m-%d %H:%M:%S}\n\n'
file_content = template.format(title, pub_date)

# Write file content
path = os.path.join(POSTS_DIR, file_name)
with open(path, 'w') as f:
    f.write(file_content)
print('File created: {}'.format(path))
