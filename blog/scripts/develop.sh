#!/bin/bash
# Development of the site


DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
BLOG_DIR="$DIR/.."

pelican "$BLOG_DIR/content" -o "$BLOG_DIR/../output" -r -s "$BLOG_DIR/conf/development.py" --debug
