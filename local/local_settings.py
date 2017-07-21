from .settings import *
from django.conf.urls import include, url
import os

DEBUG = True
#TEMPLATE_DEBUG = DEBUG

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#      }
# }

ALLOWED_HOSTS = ['.bearfounders.com', '54.215.142.223', '127.0.0.1']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'userdb',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

if DEBUG:
   INTERNAL_IPS = ['127.0.0.1']
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'static')
   STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
   # try:
   #     import debug_toolbar
   #     MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
   #     INSTALLED_APPS += ('debug_toolbar',)
   #     DEBUG_TOOLBAR_URLS = [url(r'^__debug__/', include(debug_toolbar.urls)),]
   # except ImportError:
   #     pass

# TIME_ZONE = 'Asia/Krasnoyarsk'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
