#!/bin/bash
# Development of the site


DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PRAZENI_DIR="$DIR/.."

pelican "$PRAZENI_DIR/content" -o "$PRAZENI_DIR/../output" -r -s "$PRAZENI_DIR/conf/development.py" --debug
