#!/bin/bash

set -e

cd blog
pipenv run lint
cd ..

cd home
pipenv run lint
cd ..
