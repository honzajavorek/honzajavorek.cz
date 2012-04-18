
# Migration

MySQL dump of my former blog (self-made engine) and migration Python script. This migration guide is for Ubuntu Linux in 6 simple steps. It's remainder for me in case I would forget how to run these tools on my computer.

1. Install Pandoc. `apt-get install pandoc`
2. Install all Pythonic requirements. `pip install -r requirements.txt`
3. Load SQL dump (`migration_data.sql`) into your local MySQL database. Script uses this configuration: `connect(host='localhost', user='dev', passwd='dev', db='blog', charset='utf8', use_unicode=True)`. Adjust it as you want.
4. Run the script. `python migration.py`
5. Script should read data from MySQL, convert it into Markdown articles by Pandoc (ignores Texy! version, converts directly from HTML) and write all article into the `posts` directory.
6. Drafts are prefixed by underscore (`_`). Such prefixed files are ignored in `posts` directory by Git.
