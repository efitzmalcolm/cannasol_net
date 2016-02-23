from .base import *
import os

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'cannasol_net',
                'USER': 'cannasol_net',
                'PASSWORD': '85a35aed3e',
                'HOST': 'localhost',
                'PORT': '',
        }
}

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
