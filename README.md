# Backend

Sample App

<img src="https://img.shields.io/badge/code%20style-black-000000.svg" _target="https://github.com/ambv/black" alt="Black code style"></img>


## Backend Setup Instructions

- Fork and Clone the repo using
```
$ git clone https://github.com/alokknight/Backend.git
```
- Change Branch to `backend` using
```
$ git checkout backend
```
- Setup Virtual environment
```
$ python -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Make migrations using
```
$ python manage.py makemigrations
```
- Migrate Database
```
$ python manage.py migrate
```
- Create a superuser
```
$ python manage.py createsuperuser
```
- Run server using
```
$ python manage.py runserver
```
