#!/usr/bin/env bash

python build_rst.py
cd docs_build || exit
make markdown
cd ..
rm -rf ./docs/api
mv ./docs_build/_build/markdown ./docs/api
yarn docs:build
