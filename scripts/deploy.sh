#!/bin/bash
# Publishing of the site


DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
DIR_OUTPUT="$DIR/../output"


# Compile Pelican site
touch "$DIR/content"  # prevent caching
pelican "$DIR/content" -o "$DIR_OUTPUT" -s "$DIR/config/production.py"

# Remove unnecessary stuff
rm -rf \
    "$DIR_OUTPUT/author" \
    "$DIR_OUTPUT/category" \
    "$DIR_OUTPUT/drafts" \
    "$DIR_OUTPUT/tag" \
    "$DIR_OUTPUT/feeds" \
    "$DIR_OUTPUT/tags.html" \
    "$DIR_OUTPUT/authors.html" \
    "$DIR_OUTPUT/categories.html"


# Deploy to GitHub Pages
ghp-import -p "$DIR_OUTPUT"
