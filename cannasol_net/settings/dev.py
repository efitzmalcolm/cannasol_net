from .base import *

DEBUG = True
SECRET_KEY = 'e8033f7cd7'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cannasol_net',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
