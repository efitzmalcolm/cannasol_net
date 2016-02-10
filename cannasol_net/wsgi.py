import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cannasol_net.settings.heroku")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
