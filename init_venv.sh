#!/usr/bin/env bash

if [ ! -d "venv" ]; then
  virtualenv venv
fi
source venv/bin/activate

pip install poetry
poetry install
pip uninstall alicebot -y

./rebuild.sh
