#!/bin/bash

set -e

cd blog
pipenv run deploy
cd ..

cd home
cp -r ./node_modules/fork-awesome/fonts ../_output/static/  # hotfix
pipenv run deploy
cd ..

ghp-import -m 'deploying' ./_output/
git push origin gh-pages:gh-pages --force
