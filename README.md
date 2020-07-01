# BeidaKTV
ktv song book search/input
tree mysite
mysite
├── catalog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-37.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   └── mystyle.css
└── templates
    ├── hello_world.html
    ├── singers.html
    └── songs.html

8 directories, 27 files

Setup venv:
	python3 -m venv myvenv
	source myvenv/bin/activate
	pip install Django==3.0.7
Test:
	python manage.py runserver
