# app.run_of_con_gen


Setup and run assuming that you have python3 and virtualenv installed.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations && ./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 8001
```

Navigate the browser to the admin to update data:
```
http://localhost:8001/admin/
```

Get a CSV file of the run dock and save the file:
```
http://localhost:8001/runbook/schedule/
````

Import into google:
* Go to sheets.
* Click on File
* Click on Import
* Click upload
* Select the file from the previous step
* Set import location to replace current sheet
* Click import
* Select all of the data in the sheet
* Click on DATA menu and sort by column A
* ...
* Profit


If you are going to run this anywhere other than you localhost you need to go into /defcon_runbook/settings.py and change the SECRET_KEY variable.  But this is a tool designed for local use.... so have fun with that.
