#!/bin/bash

python3 -m venv ./venv
./venv/bin/pip install -r requirements.txt

rm -r ./content/drafts
./venv/bin/pelican --settings=publishconf.py --debug --fatal warnings

rm -r \
    ./output/theme/fork-awesome/less \
    ./output/theme/fork-awesome/scss \
    ./output/theme/fork-awesome/css/v5-compat*.* \
    ./output/theme/fork-awesome/*.md \
    ./output/theme/fork-awesome/*.json
