#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --noinput

gunicorn project.wsgi:application --bind 0.0.0.0:8000 --timeout 7200