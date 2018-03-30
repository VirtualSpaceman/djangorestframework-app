#!/bin/bash
pip3 install virtualenv --user
virtualenv venv
venv/bin/pip3 install -r requirements.txt --no-cache-dir
bash -c "source ./venv/bin/activate; exec /bin/bash -i"