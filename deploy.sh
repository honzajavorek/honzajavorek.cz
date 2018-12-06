#!/bin/bash

set -e

# blog
cd blog
pipenv run deploy
cd ..

# home
cd home
pipenv run deploy
cd ..

# hotfixes
cp -r ./home/node_modules/fork-awesome/fonts ./_output/static/
cp -r ./.circleci ./_output/
ghp-import -m 'deploying' ./_output/
git push origin gh-pages:gh-pages --force
