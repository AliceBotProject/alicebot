#!/usr/bin/env bash

function build_install() {
  rm -rf dist
  poetry build
  for file in ./dist/*.whl; do
    pip install --upgrade --no-deps --force-reinstall "$file"
  done
}

build_install

for floder in ./packages/*/; do
  cd "$floder" || exit
  build_install
  cd ..
done
