#!/bin/bash

set -e

cd blog
pipenv install --dev
cd ..

cd home
pipenv install --dev
npm install
cd ..
