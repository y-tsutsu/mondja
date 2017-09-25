#!/bin/sh
python manage.py migrate
python manage.py loaddata ./backup/auth.json
python manage.py loaddata ./backup/social_django.json
python manage.py loaddata ./backup/app.json
