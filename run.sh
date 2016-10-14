#! /bin/bash

set -xe

if [ -e /data/requirements.txt ]; then
  echo "Installing requirements to virtualenv /venv..."
  /venv/bin/pip install -r /data/requirements.txt
fi

echo "Running lambda-uploader with virtualenv /venv..."
exec lambda-uploader --virtualenv=/venv $@
