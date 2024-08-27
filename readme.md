# SDAcademy - PythonRemoteCZ23 - Hollymovies project

## Installation and setup

```bash
pip install django
```

```bash
pip freeze > requirements.txt
```

Create Django project:
```bash
django-admin startproject hollymovies .
```

## Project structure
- hollymovies - settings of our project
  - `__init__.py` - necessary to make this directory as module
  - `asgi.py` - we will not use it
  - `settings.py` - setting of our project
  - `urls.py` - in this file we define url path in our project
  - `wsgi.py` - we will not use it

## Run server
Default on port 8000:
```bash
python manage.py runserver
```

We can change port number:
```bash
python manage.py runserver 8001
```

## Start new application
```bash
python manage.py startapp viewer
```
- viewer - our first application
  - migrations - directory with migrations scripts (changes in database schema)
  - `__init__.py` - necessary to make this directory as module
  - `admin.py` - setting of administration panel
  - `apps.py` - setting of the application - we don't need to change it
  - `models.py` - IMPORTANT - includes definition of models in database
  - `tests.py` - includes tests
  - `views.py` - IMPORTANT - includes views (business logic)
 
## Registration of new application
In file `./holymovies/settings.py` add application to the list `INSTALLED_APPS`

## Tips for Final project
- for team work:
  - one member of the team creates project
  - this member creates git repository and share with other members (settings -> Collaborators -> Add people...)
  - other members makes git clone
  - all members must have same settings of indentation in Pycharm
- in the path of project files should not be spaces nor diacritics
- all installed modules must be in same version for all team members (file requirements.txt)
  ```bash
  pip freeze > requirements.txt
  ```
- `settings.py` - move SECRET_KEY to file ignored by git
- working with GIT:
  - from `master` create new branch `develop` 
  - from `develop` create new branches for new features/tests/...
  - if all changes in working branch has been done, merge changes to `develop`
  - in branch `develop` run tests
  - if all tests passes merge all changes to `master`
  - in `master` don't make any changes, just merge