"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import environ
import datetime
from decouple import config
from pathlib import Path
env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config("DEBUG")
DEBUG = True


ALLOWED_HOSTS = ['alokyoutubeapi.herokuapp.com','127.0.0.1','localhost']


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_yasg",
    "django_filters",
    "corsheaders",
    # 'django_q',
    "django_celery_beat",
]


LOCAL_APPS = [
    "authentication",
    "social_auth",
    # Your stuff: custom apps go here
    'search',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ os.path.join(BASE_DIR, "templates") ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# # Database
# # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
        "name": config('DB_NAME'),##database
        "host": config('DB_HOST'),
        "username": config('DB_USER'),##username
        "password": config('DB_PASSWORD'),##password of that database user
        "authMechanism": "SCRAM-SHA-1",
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         "CLIENT": {
#         "name": env('DB_NAME',default='mlapis'),##database
#         "host": env('DB_HOST',default='mongodb://alokpatel885:alokpatel885@cluster0-shard-00-00.redg6.mongodb.net:27017,cluster0-shard-00-01.redg6.mongodb.net:27017,cluster0-shard-00-02.redg6.mongodb.net:27017/mlapis?ssl=true&replicaSet=atlas-11t00w-shard-0&authSource=admin&retryWrites=true&w=majority'),
#         "username": env('DB_USER',default='alokpatel885'),##username
#         "password": env('DB_PASSWORD',default='alokpatel885'),##password of that database user
#         "authMechanism": "SCRAM-SHA-1",
#         },
#     }
# }
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# Q_CLUSTER = {
#     'name': config('DB_NAME'),
#     'workers': 8,
#     'timeout': 10,
#     'retry': 10,
#     'queue_limit': 100,
#     # 'mongo': {
#     #         'host': 'localhost',
#     #         'port': 27017
#     # }
#     'mongo': {
#         "host": config('DB_HOST'),
#     }
# }

# Q_CLUSTER = {
#     'name': 'django_q_django',
#     'workers': 8,
#     'recycle': 500,
#     'timeout': 60,
#     'compress': True,
#     'save_limit': 250,
#     'queue_limit': 500,
#     'cpu_affinity': 1,
#     'label': 'Django Q',
#     'redis': {
#         'host': 'clustercfg.coderpaparedis.oxkdmz.memorydb.us-west-2.amazonaws.com',
#         'port': 6379,
#         'password': '',
#         'db': 0, }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "NON_FIELD_ERRORS_KEY": "error",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
# Your stuff...
# ------------------------------------------------------------------------------

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
}

STATIC_URL = "/static/"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')


EMAIL_USE_TLS       = True
EMAIL_HOST          = "smtp.gmail.com"
EMAIL_PORT          = 587
EMAIL_HOST_USER     = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "authentication.User"



# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = "redis://localhost:6379/0"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# CELERY_TASK_TRACK_STARTED = True


django_heroku.settings(locals(),staticfiles=False)

YOUTUBE_DATA_API_KEY = config('YOUTUBE_DATA_API_KEY')
# YOUTUBE_DATA_API_KEY2 = config('YOUTUBE_DATA_API_KEY2')
# YOUTUBE_DATA_API_KEY3 = config('YOUTUBE_DATA_API_KEY3')