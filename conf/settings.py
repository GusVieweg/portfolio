"""
Django settings for template project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Load environment variables
# ============================================
# Environment variables should NEVER be placed in this configuration file. Instead,
# they should be saved locally on your computer and/or server and imported. I tend
# to save these values in the .env file (note the '.' at the beginning marks the file
# as hidden but does not affect the ability to read in the file).

try:
    cwd = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(cwd, '.env')) as f:
        for line in f:
            stmt = line.split('=', 1)
            os.environ.setdefault(stmt[0], stmt[1].rstrip())
except IOError:
    pass


# Project Base
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#root-urlconf
# https://docs.djangoproject.com/en/1.9/ref/settings/#wsgi-application

ROOT_URLCONF = 'apps.home.urls'
WSGI_APPLICATION = 'conf.wsgi.application'


# Debugging
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#debugging
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-TEMPLATE_DEBUG
#
# The following will automatically determine whether the code run should be in debug
# mode or not. This assumes we are hosting on WebFaction. If instead we were hosting
# on something like openshift, perhaps we would check for the variable OPENSHIFT instead

DEBUG = 'WEBFACTION' not in os.environ


# Security (Secret Key)
# ============================================
# SECURITY WARNING: keep the secret key used in production secret!
# This is important since if someone gets access to this, they get access to essentially
# everything. Thus, keep this hidden in our .env file. If we are in debug mode, we just # randomly create one.

if DEBUG:
    import random
    SECRET_KEY = '%030x' % random.randrange(16**30)
else:
    SECRET_KEY = os.environ.get('SECRET_KEY', '')


# Allowed Hosts
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#allowed-hosts
#
# Determines what hosts our application should run on. This limiting of domains
# helps prevent things like CSRF attacks.

ALLOWED_HOSTS = []
if DEBUG:
    ALLOWED_HOSTS.append('*')
else:
    ALLOWED_HOSTS.append('.josh-potter.com')


# Application Definition
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-INSTALLED_APPS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'foundation',
    'apps.base',
    'apps.home',
    'apps.blog',
    'apps.projects',
]


# Middleware Classes
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#middleware-classes

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Database
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portfolio',
        'USER': os.environ.get('DATABASE_USER', 'jrpotter'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
    }
}


# Templates
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# Password Validation
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# ============================================
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ============================================
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.environ.get('STATIC_ROOT', '')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'vendor'),
)


# Administrators
# ============================================
# https://docs.djangoproject.com/en/1.9/ref/settings/#admins

ADMINS = (
    ('jrpotter', 'jrpotter2112@gmail.com'),
)


# Email
# ============================================
# https://docs.djangoproject.com/en/1.7/ref/settings/#email

EMAIL_HOST_USER = 'jrpotter'
EMAIL_HOST = 'smtp.webfaction.com'
SERVER_EMAIL = 'support@josh-potter.com'
DEFAULT_FROM_EMAIL = 'support@josh-potter.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
