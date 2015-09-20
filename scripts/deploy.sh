#!/bin/bash
# Publishing of the site


DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
DIR_OUTPUT="$DIR/../output"


# Compile Pelican blog - Javorové lístky
DIR_BLOG="$DIR/../blog"
DIR_BLOG_OUTPUT="$DIR_OUTPUT/blog"

touch "$DIR_BLOG/content"  # prevent caching
pelican "$DIR_BLOG/content" -o "$DIR_BLOG_OUTPUT" -s "$DIR_BLOG/conf/production.py"

# Remove unnecessary stuff
rm -rf \
    "$DIR_BLOG_OUTPUT/author" \
    "$DIR_BLOG_OUTPUT/category" \
    "$DIR_BLOG_OUTPUT/tag" \
    "$DIR_BLOG_OUTPUT/feeds" \
    "$DIR_BLOG_OUTPUT/tags.html" \
    "$DIR_BLOG_OUTPUT/authors.html" \
    "$DIR_BLOG_OUTPUT/categories.html"


# Compile Pelican blog - Pražení
DIR_PRAZENI="$DIR/../prazeni"
DIR_PRAZENI_OUTPUT="$DIR_OUTPUT/prazeni"

"$DIR_PRAZENI/scripts/import.sh" # archivation of prazeni.tumblr.com
touch "$DIR_PRAZENI/content"  # prevent caching
pelican "$DIR_PRAZENI/content" -o "$DIR_PRAZENI_OUTPUT" -s "$DIR_PRAZENI/conf/production.py"

# Remove unnecessary stuff
rm -rf \
    "$DIR_PRAZENI_OUTPUT/author" \
    "$DIR_PRAZENI_OUTPUT/category" \
    "$DIR_PRAZENI_OUTPUT/tag" \
    "$DIR_PRAZENI_OUTPUT/feeds" \
    "$DIR_PRAZENI_OUTPUT/tags.html" \
    "$DIR_PRAZENI_OUTPUT/authors.html" \
    "$DIR_PRAZENI_OUTPUT/categories.html"

# Deploy to GitHub Pages
ghp-import -p "$DIR_OUTPUT"
