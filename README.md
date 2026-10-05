# Quiz 3 - Django (Model → View → URL → Template)

Simple Django app that displays Student records from the database.

## Run locally
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate        # also adds 13 sample students
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/ (admin at /admin/).
