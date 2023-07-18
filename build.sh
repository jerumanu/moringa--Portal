#!/usr/bin/env bash

set -o errexit  # exit on error
cd /home/jerumanu/Projects/moringa--Portal/app
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate