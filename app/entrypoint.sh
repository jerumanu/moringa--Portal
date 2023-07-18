#!/bin/bash
APP_PORT=${PORT:-8000}
CD /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm moringaportal.wsgi:application --bind "0.0.0.0:${APP_PORT}"
