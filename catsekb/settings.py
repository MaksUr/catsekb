"""
Django settings for catsekb project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

with open(os.path.join(os.sep, 'srv', 'vk_token.txt')) as f:
        VK_TOKEN = f.read().strip()
# SECURITY WARNING: keep the secret key used in production secret!
try:
    with open(os.path.join(os.sep, 'srv', 'secret_key.txt')) as f:
        SECRET_KEY = f.read().strip()
except FileNotFoundError:
    SECRET_KEY = '1j(lfw54!y!f3u%&8%e*(m)@k=p&@2iphm53p$$li&8hy#@gwl'
    DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1']
else:
    DEBUG = False
    ALLOWED_HOSTS = ['catsekb.ru']

# Application definition

INSTALLED_APPS = [
    'cats.apps.CatsConfig',
    'articles.apps.ArticlesConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'catsekb.urls'

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

WSGI_APPLICATION = 'catsekb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
try:
    with open(os.path.join(os.sep, 'srv', 'db_key.txt')) as f:
        db_key = f.read().strip()
except FileNotFoundError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'catsekb',
            'USER': 'catsekb',
            'PASSWORD': db_key,
            'HOST': 'postgres',
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Yekaterinburg'  # TODO: set timezone

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.sep, 'srv', 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
