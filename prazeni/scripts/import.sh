#!/bin/bash
# Archivation of prazeni.tumblr.com


DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PRAZENI_DIR="$DIR/.."

# API key - https://www.tumblr.com/oauth/apps (OAuth Consumer Key)
pelican-import --tumblr \
    -o "$PRAZENI_DIR/content" \
    -m markdown \
    --blogname=prazeni \
    "$PRAZENI_TUMBLR_API_KEY"

git add -A "$PRAZENI_DIR/content"
git commit -m "Automatic archivation of prazeni.tumblr.com."
git push origin HEAD
