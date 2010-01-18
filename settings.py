import os
 
PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Lukasz Szpak', 'lukasz.szpak@binop.com'),
    ('Kuba Janoszek', 'kuba@binop.com')
)
MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = PROJECT_ROOT+'/db/pdugen.db' 

SITE_ID = 1

MEDIA_URL = '/static/'
MEDIA_ROOT = PROJECT_ROOT+'/static/'

TEMPLATE_DIRS = (
    PROJECT_ROOT+'/templates/'
)

SECRET_KEY = '631_@-*2!50$p9(3(5j8&u%^cnd%i8(o$teha765lnts7c0(2='

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'Simple-PDU-generator.urls'

INSTALLED_APPS = (
    'pdugen', 

    #'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    #'django.contrib.admin',
    )

try:
    from local_settings import *
except ImportError:
    pass
