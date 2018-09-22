# django_test
django loan validator and manager.

## Instalation
Requirements:
 - [Python 2.7 +](https://www.python.org/)
 - [Django 1.11](https://www.djangoproject.com/)
 - [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/)
 
Just clone repository, install requirements and execute.
```
$ git clone https://github.com/hernannieto89/django_test 
$ cd django_test
$ pip install -r requirements.txt
$ python manage.py runserver
```

It is strongly recommended to install this application within a virtual environment.
For more information on virtual environments please refer to this [link](https://virtualenvwrapper.readthedocs.io/en/latest/).


## Usage

The following endpoints are available once the server is running:

### localhost:port/loans/
In this address we have a form for requesting loans.
All fields are mandatory.


### localhost:port/loans/manager
This address needs staff login. Staff users are created via:
```
$ python manage.py createsuperuser
```
Once logged in, all loan requests are listed alongside with an form for loan request edition.

## TODO
Add unit testing.
Improve loan request edition logic.
Improve UI, ie, bootstrap.