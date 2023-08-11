# DJANGO PROJECT 'Cookie'

### Usage

Cookie is a website for reviewing and rating movies published on site. Admin users publish different movie titles with short synopsis for each movie,its director, list of genres and actors. Users can search for different movie titles, actors and directors.

### Technologies
* `Django`
* `PostgreSQL`
* `Bootstrap4`

### Project structure

Cookie uses `PostgreSQL` database and `Bootstrap4` for HTML templates

Cookie consists of two apps: 
- movies
- users

`movies` allows users to visit page for each movie, where they can read short synopsis of the movie,
see its actors, genres and director. Also users can see list of reviews for each movie and its average rating, as well as leave their own rating and review

`users` app manages registration, login and logout operations. Also this app manages operation of changing users info(username and email). `users` app also has CustomUser model.

### Installation

Clone repository, using command:
```
    git clone https://github.com/Andrew-157/dj_project_3
```
and go into directory 'dj_project_3'.

**Everything shown below assumes you are working from directory 'dj_project_3'**

Requirements:
```
    Django==4.2.4
    Pillow==10.0.0
    django-environ==0.10.0
    django-crispy-forms==2.0
    django-cleanup==8.0.0
    crispy-bootstrap4==2022.1
    django-taggit==4.0.0
    django-debug-toolbar==4.1.0
    psycopg2-binary==2.9.7
    autopep8==2.0.2
```

If you are using pipenv,run in the command line from directory where Pipfile is located:
```
    pipenv install
```

To activate environment using pipenv, run in the command line in the same directory:
```
    pipenv shell
```

You can also use file `requirements.txt` with pip.
Inside your activated virtual environment, run:
```
    pip install -r requirements.txt
```
For `Windows`
```
    pip3 install -r requirements.txt
```
For `Unix`-based systems

### Run project

**The following steps show how to run project locally(i.e., with DEBUG=True)**

Generate secret key, using the following code:
```python
    import secrets

    secret_key = secrets.token_hex(32)

    print(secret_key)
```

In directory 'cookie' create file .env(**do not forget to add it to .gitignore, if it is not there**) and add the following line:
```
    SECRET_KEY=<secret_key_you_generated>
```

Then you need to create PostgreSQL database (using pgAdmin or any other tool)
```SQL
    CREATE DATABASE <your_database_name>;
```

Next, go to .env and using credentials of your database, add the following lines:
```
    DB_NAME=<your_database_name>
    DB_USER=<your_database_user>
    DB_PASSWORD=<your_database_password>
    DB_HOST=<your_database_host>
    DB_PORT=<your_database_port>
```

After that, in command line run:
```
    python manage.py migrate
    python manage.py runserver
```

Go to your browser at the address: 'http://127.0.0.1:8000/', you should be able to see Cookie's index page.

### Admin site

If you want to visit admin site, run the following command:
```
    python manage.py createsuperuser
```

Enter credentials for your admin user, and visit 'http://127.0.0.1:8000/admin',
login using the same credentials you used when you created admin user.


### Testing

**Each app contains 'tests' directory with `__init__.py` and 3 modules(each module's name starts with 'test')**

**Tests for `Cookie` are written using Django's `TestCase`**

That means that each test module contains following import statement:
```python
    from django.test import TestCase
```
And each testing class is created like this:
```python
    class DirectorModelTest(TestCase):
        pass
```

If you want to run all tests available in the project, in the command line run:
```
    python manage.py test
```

**Cookie has over 100 tests written, so you may want to run only particular tests.**

The following commands will show how to run tests of app "movies" of "cookie" project.

To run tests for whole app, use this command:
```
    python manage.py test movies
```

To run only particular module from 'movies/tests', use this command:
```
    python manage.py test movies.tests.test_views
```

To run particular test class from 'movies/tests/test_views'(or any other module), use this command:
```
    python manage.py test movies.tests.test_views.ReviewMovieViewTest
```

To run particular test method(that is test itself,in fact) from any class in module 'movies/tests/test_views'(or any other module), use this command:
```
    python manage.py test personal.tests.test_views.ReviewMovieViewTest.test_correct_response_for_nonexistent_movie
```

## Inspiration

Main inspiration for `Cookie` comes from [IMDb](https://www.imdb.com/).