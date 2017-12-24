cd /d %~dp0
cd ../
call heroku run python manage.py migrate
call heroku run python manage.py loaddata ./backup/auth.json
call heroku run python manage.py loaddata ./backup/social_django.json
call heroku run python manage.py loaddata ./backup/app.json
