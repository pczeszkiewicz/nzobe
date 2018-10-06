#!/usr/bin/env bash
echo "Apply database migrations"
python manage.py migrate --run-syncdb
echo "Starting server"
gunicorn nozbe_pczeszkiewicz.wsgi --log-file -
