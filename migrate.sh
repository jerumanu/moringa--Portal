#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL="jeru.koech200@gmail.com"}

cd /app/

opt/venv/python manage.py migrate --noinput

opt/venv/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
