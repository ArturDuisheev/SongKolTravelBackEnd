#!/bin/sh

sudo python manage.py makemigrations
sudo python manage.py migrate

gunicorn core.wsgi:application --bind 0.0.0.0:8000 --access-logfile -
