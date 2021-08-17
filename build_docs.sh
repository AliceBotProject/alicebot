#!/usr/bin/env bash

python build_rst.py
cd docs_build || exit
rm -rf _build
make markdown
cd ..
rm -rf ./docs/api
mv ./docs_build/_build/markdown ./docs/api
yarn docs:build
