import os
from .common import *
import dj_database_url

DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'corsheaders',
    'djoser',
    'django_admin_listfilter_dropdown',
    'storages',
    'anymail',
    'core',
    'hymnbook',
    'members',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['mcec-backend-4755c92403d9.herokuapp.com']

CORS_ALLOWED_ORIGINS = [
    "https://cantosmcec.vercel.app",
    "https://cantosmcec.com"
]



DATABASES = {
    'default': dj_database_url.config()
}

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": os.environ.get('MAILGUN_API_KEY'),
    "MAILGUN_SENDER_DOMAIN": os.environ.get('MAILGUN_SENDER_DOMAIN'),  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "from@cantosmcec.com"  # if you don't already have this in settings
SERVER_EMAIL = "mailgun@cantosmcec.com"  # ditto (default from-email for Django errors)

# EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
# EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
# EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
# EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
# EMAIL_USE_TLS = True

DOMAIN = 'cantosmcec.vercel.app'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
STORAGES = {
    "default": {"BACKEND": "mcec.custom_storage.MediaStorage"},
    "staticfiles": {"BACKEND": "mcec.custom_storage.StaticStorage"}
}
