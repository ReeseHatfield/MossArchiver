#!/bin/bash

if [ "$1" != "--link" ] || [ -z "$2" ]; then
  echo "Error: bad arguments"
  echo "Usage: ./archive --link [link]"
  exit 1
fi


if [ ! -d "venv" ]; then
  echo "couldn't find venv"
  echo "creaing virtual env"

  python3 -m venv venv

  if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment."
    exit 1
  fi

fi

source "venv/bin/activate"

# may not need requiremnts, came from my template
echo "Installing requirements..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
  echo "Failed to install dependencies."
  deactivate
  exit 1
fi

python3 src/main.py "$2"
