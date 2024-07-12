"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k=w$!7-+r6&olr4g*5form5(2t^8nbc!6iqx2c-jmz5sia+3@('

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['192.168.43.26', 'localhost', '127.0.0.1', '10.0.2.2']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'dj_rest_auth',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'accounts',
    'delivery'
]


SITE_ID = 1

REST_USE_JWT = True

# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
from decouple import config

# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = '4717f94cec3cd8'
# EMAIL_HOST_PASSWORD = 'eb16e50accf9f4'
# EMAIL_PORT = '2525'
# EMAIL_USE_TLS: False
# EMAIL_USE_SSL: False

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='sandbox.smtp.mailtrap.io')
EMAIL_PORT = config('EMAIL_PORT', default='2525')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='5dabe6d3b1c10c')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='cd6ccb78fd894d')



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
    
]

ROOT_URLCONF = 'settings.urls'

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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'delivery',
#         'USER':'root',
#         'PASSWORD':'',
#         'HOST':'localhost',
#         'PORT':'3306',
#     }
# }

# SILENCED_SYSTEM_CHECKS = ["models.W036"]
# SILENCED_SYSTEM_CHECKS = ["models.W043"]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




REST_AUTH = {
    'SESSION_LOGIN': False,
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'auth',
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_SECURE': True,
    # 'JWT_AUTH_HTTPONLY': True,
    # 'JWT_AUTH_SAMESITE': 'None',
}

AUTH_USER_MODEL = 'accounts.CustomUser'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ),
}

APPEND_SLASH = False

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),  # Set a longer access token lifetime (e.g., 1 year)
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=365),  # Set a longer refresh token lifetime (e.g., 1 year)
    'SLIDING_TOKEN_LIFETIME': timedelta(days=365),  # Set a longer sliding token lifetime (e.g., 1 year)
    'ROTATE_REFRESH_TOKENS': False,  # Disable token rotation
}

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# import firebase_admin
# from firebase_admin import credentials

# # Replace 'path/to/serviceAccountKey.json' with the path to your Firebase service account key file
# cred = credentials.Certificate('path/to/serviceAccountKey.json')
# firebase_admin.initialize_app(cred)

# # Add your Firebase Web API Key here
# FIREBASE_WEB_API_KEY = 'your_firebase_web_api_key_here'

TWILIO_ACCOUNT_SID = 'ACe55b7e7f1a57bde1a005381bf489dc68'
TWILIO_AUTH_TOKEN = 'fc66c06efa616e354f15496fe070304a'
TWILIO_VERIFY_SERVICE_SID = 'VA3345b8155a5d9e9accbf65362be5e868'
TWILIO_PHONE_NUMBER = '+12183072487'
