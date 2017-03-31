"""
Django settings for api_backend project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from datetime import datetime, timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3!*33lw7lf!_hdbq-)#k27b!^&(xkr%#e0n+17cqf)tk%-6@gq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'rest_framework_jwt',
    'api_app.apps.ApiAppConfig',
    'corsheaders',
    'django_ses',
    'adminplus',

]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_backend.urls'
CORS_ORIGIN_ALLOW_ALL = True


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

WSGI_APPLICATION = 'api_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'picam',
        # 'USER': 'nguyen',
        # 'PASSWORD': 'helloworld',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'picam',
        'USER': 'cornjob',
        'PASSWORD': 'pipipipi',
        'HOST': 'sketchflow.cp1gdmsejpup.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    
    }
}

AUTH_USER_MODEL = 'api_app.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'django.contrib.auth.backends.AuthenticationBackend',
)


# Password validation
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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_ROOT = "/home/ec2-user/api_backend/api_backend/static/"


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',

    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',

    ),

    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.AllowAny',
       'rest_framework.permissions.IsAuthenticated',
       'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),

    'TEST_REQUEST_DEFAULT_FORMAT': 'json'

}

# Default JWT preferences
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

    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
    'rest_framework_jwt.utils.jwt_get_username_from_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': timedelta(days=1),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

DJOSER = {
    # 'DOMAIN': 'frontend.com',
    # 'SITE_NAME': 'Frontend',
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_VALIDATORS': [],
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'SERIALIZERS': {},
    'SERIALIZERS': {
        'activation': 'djoser.serializers.ActivationSerializer',
        # 'login': 'djoser.serializers.LoginSerializer',
        'login': 'api_app.serializers.UserLoginSerializer',
        'password_reset': 'djoser.serializers.PasswordResetSerializer',
        'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        'set_password': 'djoser.serializers.SetPasswordSerializer',
        'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        'set_username': 'djoser.serializers.SetUsernameSerializer',
        'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
        'user_registration': 'djoser.serializers.UserRegistrationSerializer',
        'user': 'api_app.serializers.UserSerializer',
        'token': 'djoser.serializers.TokenSerializer',
    },
}

##Normal SMTP
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # Host for sending e-mailS
# EMAIL_HOST = 'smtp.gmail.com'
# # Port for sending e-mail.
# EMAIL_PORT = 587
# # Optional SMTP authentication information for EMAIL_HOST.
# EMAIL_HOST_USER = 'khanhnguyen19101989@gmail.com'
# EMAIL_HOST_PASSWORD = ''

##SSL with SES SMTP setting
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
# EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'AKIAJMFZR4TKDEUF5JLQ'
# EMAIL_HOST_PASSWORD = 'ApbBh5FTUy8HR8kSTLyZ/Avm7nSiGNWlIJONngeCo4ro'
# DEFAULT_FROM_EMAIL = 'khanhnguyen19101989@gmail.com'
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False

##Using aws web service
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = 'AKIAI4E6TASIAIKIR3MA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'
DEFAULT_FROM_EMAIL = 'khanhnguyen19101989@gmail.com'
