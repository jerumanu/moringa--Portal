#!/bin/sh

# Set the value of DJANGO_SUPERUSER_EMAIL environment variable, defaulting to "jeru.koech200@gmail.com"
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"jeru.koech200@gmail.com"}

# Change the current directory to /app/
cd /app/

# Activate the virtual environment
source /opt/venv/bin/activate

# Run database migrations
python manage.py migrate --noinput

# Create a superuser with the specified email address if one doesn't exist
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

# Deactivate the virtual environment
# deactivate
