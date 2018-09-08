# Personal website powered by Django
This is a personal website I built for myself that's powered by Django. Certainly you could do a lot of this without a full-fledged web framework like Django, but where's the fun in that?

## Running locally
This project requires Python 3.6 or above and PostgreSQL
1. Register for an API Key from Google Books
1. Create a virtual environment with the right Python 3.6+ version: `virtualenv --python <path_to_python> venv`
1. Run `pip install -r my_site/project_requirements.txt`
1. Create an `__init__.py` in the `my_site/settings/` directory and fill out like so:
```
from .local_dev import *

SECRET_KEY = <some_random_and_long_string>

DATABASES['default']['PASSWORD'] = <your_database_password>

GOOGLE_BOOKS_API_KEY = <your_google_books_api_key>
```
1. Run the migrations: `python manage.py migrate`
1. Run the application: `python manage.py runserver`
1. Access the application at `http://localhost:8000`
