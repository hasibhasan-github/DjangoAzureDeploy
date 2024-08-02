import os 
from .settings import *
from .settings import BASE_DIR 

SECRET_KEY = os.environ['SECRET']

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS = ['https://realtimechatazure-ayh3e7a2bmh9e2hc.southeastasia-01.azurewebsites.net']
DEBUG = False 


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}

# DATABASES = {
#     'default' : {
#         'ENGINE' : 'django.db.backends.postgresql',
#         'NAME' : parameters['dbname'],
#         'HOST' : parameters['host'],
#         'USER' : parameters['user'],
#         'PASSWORD' : parameters['password'],
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'realtimechatazure-database',
        'HOST': 'realtimechatazure-server.postgres.database.azure.com',
        'PORT': '5432',
        'USER': 'pqkphsxbke',
        'PASSWORD': '6yAvQUgvJG2yT9j$',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
