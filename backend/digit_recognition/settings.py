"""
Django settings for digit_recognition project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"""
Runtime environment settings:
    DJANGO_SECRET_KEY: (str) 
    DJANGO_DEBUG_MODE: (boolean)
"""
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

if SECRET_KEY is None:
    SECRET_KEY = 'none'  # none
    print("> Secret Key is set to None.")
# raise Exception('No Secret Key')
else:
    print("> Loaded Secret Key from environment.")

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('DJANGO_DEBUG_MODE').lower() == "true":
    """
    default to false, do not give production 
    environment with debug = True
    """
    DEBUG = True
    print("> Django debug mode is True!")
else:
    DEBUG = False


# allow all incoming hosts
# IT IS NOT SAFE FOR PRODUCTION
def allow_all_hosts():
    if DEBUG is True:
        return '*'
    else:
        return


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]', '.vercel.app', '.herokuapp.com', 'compute.amazonaws.com'
                 # allow_all_hosts()  # NOT SAFE
                 ]

CORS_ORIGIN_WHITELIST = ['http://localhost:8080', 'http://localhost:8088', 'http://127.0.0.1:8080',
                         'http://127.0.0.1:8088', 'https://sof-106-project-frontend.vercel.app',
                         'https://sof106-project-backend.herokuapp.com', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digit_recognition.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'digit_recognition.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# This is for templates
STATIC_URL = '/static/'

# This is for urls.py (load the static files)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# For Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
