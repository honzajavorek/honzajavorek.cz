import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *


DELETE_OUTPUT_DIRECTORY = True
SIMPLE_ANALYTICS = True
SITEURL = 'https://honzajavorek.cz'

# On CI the git checkout resets every file's mtime each run, which would
# invalidate the whole content cache (see pelicanconf.py). Hash file contents
# instead of mtime so the persisted cache/ dir survives across CI runs.
CHECK_MODIFIED_METHOD = 'md5'
