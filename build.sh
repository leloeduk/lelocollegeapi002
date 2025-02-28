#!/usr/bin/env bash
# exit on error
set -o errexit

pip install freeze -r requirements.txt

pip manage.py collectstatic --no-input
pip manage.py migrate
