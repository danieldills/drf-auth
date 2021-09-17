# Davee's Django Rest API Template

## Author: Davee Sok

## Links & Resources

- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Create Custom User Model](https://testdriven.io/blog/django-custom-user-model/)

## Overview/ Motivation

Starting up a Django api can be time consuming. This template is meant to get up and running fast. Once all the wiring is done, you can make modifications to your models and tests as needed.

## Tools & Dependencies

- Django
- Django Rest Framework
- Black
- Docker
- psycopg2-binary

## Getting Started

### 1. Clone down repo and install dependencies

```iterm
poetry shell
poetry install
```

### 2. Create a New Secret Key by running the following command in the terminal:

```iterm
python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```

### 3. Add new key to settings.py line 23

```python
SECRET_KEY = "django-insecure-INSERT_NEW_SECRET_KEY_HERE"
```

### 4. App folder currently named "Concert". Replace this with your app name

- These steps will change the app name and all occurences of "Concert"
- Do a global search of "Concert" and replace all occurences with your new app name
  - (For this step your app name needs to be a capital word) ex Concert -> Blog
  - Make sure to select "Match Case" option. [Aa]
  - (There will only be 36 matches. If you see 42, you didn't check your case)
- The following steps requires a lowercase version of your app name(4 places you have to change)
  - Replace "Concert" folder name
  - In app.py - line 6, make sure name variable is lowercase
  - In project/urls.py, fix urlpatterns on line 19 to use lowercase
  - In project/settings.py check INSTALLED_APPS to make sure your app name is lowercased

### 5a. If you want to run with docker, run the following commands:

```iterm
docker-compose up
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

### 5b. If you want to run in just the terminal, run the following commands:

```iterm
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Notes

This project makes use of a custom user that over writes django's default user model. When you create new models that need to reference user as a foreign key, you need to make the following changes:

```python
# Old Way

from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

# ----------------------------------- New Way -----------------------------------

from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

```

In your tests, you would still use get_user_model()

### Commands To Know

```python
poetry export -f requirements.txt -o requirements.txt --without-hashes
docker-compose up
docker-compose -d
docker-compose down
docker-compose logs
docker-compose up --build
```
