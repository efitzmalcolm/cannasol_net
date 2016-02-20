from .base import *

DEBUG = True
SECRET_KEY = 'e8033f7cd7'

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
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
