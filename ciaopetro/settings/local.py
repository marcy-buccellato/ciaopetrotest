from ciaopetro.settings.base import *


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '../blog/static')

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
