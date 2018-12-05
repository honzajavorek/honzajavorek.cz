#!/bin/bash

cd blog
pipenv install --dev
cd ..

cd home
pipenv install --dev
npm install
cd ..
