from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cannasol.net',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}