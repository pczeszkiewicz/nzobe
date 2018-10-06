#!/usr/bin/env bash
echo "Apply database migrations"
python manage.py migrate --run-syncdb
echo "Starting server"
gunicorn nozbe.wsgi --log-file -
