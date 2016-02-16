#!/bin/bash
# Development of the site


DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)'/..'
pelican "$DIR/content" -o "$DIR/output" -r -s "$DIR/config/development.py" --debug
