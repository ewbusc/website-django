An easy-to-edit version of our website over at ewbusc.org. WIP

To set up:

1. Install Python 3 
1. (recommended) Set up a [virtual environment](https://docs.python.org/3/library/venv.html)
1. `pip install -r {PROJECTDIR}/requirements.txt` 
1. `python manage.py migrate` 
1. `python manage.py collectstatic` 
1. (recommended) `cp sample_db.sqlite3 db.sqlite3` (sample_db.sqlite3 contains a database preinitialized with all of the named blocks used by the website)

To run:

*. `python manage.py runserver`
