#!/bin/bash

# Installation
npm install --prefix=./theme
python3 -m venv ./venv
./venv/bin/pip install -r requirements.txt

# Build
rm -r ./content/drafts
./venv/bin/pelican --settings=publishconf.py --debug --fatal warnings
