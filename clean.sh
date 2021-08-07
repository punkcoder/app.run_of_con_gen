rm db.sqlite3
rm -rf runbook/migrations/

./manage.py makemigrations runbook && ./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 8001