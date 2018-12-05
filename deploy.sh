#!/bin/bash

set -e

cd blog
pipenv run deploy
cd ..

cd home
pipenv run deploy
cp -r ./node_modules/fork-awesome/fonts ../_output/static/  # hotfix
cd ..

ghp-import -m 'deploying' ./_output/
git push origin gh-pages:gh-pages --force
