#!/bin/sh

# Set the APP_PORT environment variable if not already defined, defaulting to 8000
APP_PORT=${PORT:-8000}

# Change the current directory to /app/
cd /app/

# Start the Gunicorn server with the specified settings
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm moringaportal.wsgi:application --bind "0.0.0.0:${APP_PORT}"
