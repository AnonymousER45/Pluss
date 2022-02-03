"""
Django settings for Pluscrown project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'is=)o)(94qb1vy9fmhjk3snuh1uwb1z(59fy_15v)7o+2t$ph+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','Swaraj.pythonanywhere.com','www.pluscrown.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Apps
    'Ecom',
    'Accounts',

    # Framework,
    'rest_framework',
    'Api',
    'import_export',

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

ROOT_URLCONF = 'Pluscrown.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                    'staticfiles': 'django.templatetags.static',
                 },
        },
    },
]

WSGI_APPLICATION = 'Pluscrown.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT= os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'Pluscrown/static'),

]


#### media files(photo,logos)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/uploads/'

AUTH_USER_MODEL = 'Accounts.Customer'

RESETPASSWORD_URL = "www.google.com"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

SENDSMS_BACKEND = 'sendsms.backends.console.SmsBackend'

JWT_AUTH = {
'JWT_ENCODE_HANDLER':
'rest_framework_jwt.utils.jwt_encode_handler',

'JWT_DECODE_HANDLER':
'rest_framework_jwt.utils.jwt_decode_handler',

'JWT_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_payload_handler',

'JWT_PAYLOAD_GET_USER_ID_HANDLER':
'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

'JWT_RESPONSE_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_response_payload_handler',

'JWT_GET_USER_SECRET_KEY': None,
'JWT_PUBLIC_KEY': None,
'JWT_PRIVATE_KEY': None,
'JWT_ALGORITHM': 'HS256',
'JWT_VERIFY': True,
'JWT_VERIFY_EXPIRATION': True,
'JWT_LEEWAY': 0,
'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
'JWT_AUDIENCE': None,
'JWT_ISSUER': None,

'JWT_ALLOW_REFRESH': False,
'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=2),

'JWT_AUTH_HEADER_PREFIX': 'JWT',
'JWT_AUTH_COOKIE': None,

}
