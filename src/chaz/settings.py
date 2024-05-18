"""
 ___________________ 
< SET ALL THE THINGZ >
 ------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""
import os
import logging

from datetime import timedelta

from kombu import Queue

######################################################################
# 🌶️ SPICY WARNING ‼️
# SENTRY TELEMETRY
SENTRY_SEND_TELEMETRY = os.getenv("SENTRY_SEND_TELEMETRY", "False").lower() in ("true", "1", "t")
######################################################################

if SENTRY_SEND_TELEMETRY:
    import sentry_sdk

    SENTRY_DSN = os.getenv("SENTRY_DSN")
    if not SENTRY_DSN:
        raise ValueError("Must set SENTRY_DSN if using SENTRY_SEND_TELEMETRY")

    SENTRY_SAMPLE_RATE = float(os.getenv("SENTRY_SAMPLE_RATE", "1.0"))

    sentry_sdk.init(
        SENTRY_DSN,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=SENTRY_SAMPLE_RATE,
    )

#Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv('SECRET_KEY')

SHITS_VALID_YO = ['t', '1', 'yeet', 'true', 'yee', 'yes', 'duh', 'yesdaddy', 'ok']

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

if os.getenv("FORCE_SECURE", "False").lower() in ("true", "1", "t"):
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(',')
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000000
DJANGO_WEB_MAX_REQUESTS = 3000
DJANGO_WEB_TIMEOUT = 15

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'durin',
    'django_celery_results',
    'django_celery_beat',
    'drf_yasg',
    "storages",
    'the_thing',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'chaz.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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
#                'reactor.context_processors.side_bar',
            ],
        },
    },
]

WSGI_APPLICATION = 'chaz.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'ATOMIC_REQUESTS': False,
        'CONN_MAX_AGE': 0,
        'OPTIONS': {
            'MAX_CONNS': 20,
            'REUSE_CONNS': 10
        }
     }
 }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True


SESSION_EXPIRE_SECONDS = int(os.getenv('SESSION_EXPIRE_SECONDS', '3600'))
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

###########################################################
# LOGGING STUFFZ
###########################################################

# Logging Configuration
# Get loglevel from env
LOGLEVEL = os.getenv('LOG_LEVEL', 'info').upper()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": LOGLEVEL,
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": LOGLEVEL,
            "propagate": False,
        },
    },
}


########################################################################
# Celery Stuffz
########################################################################
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# CELERY_BROKER_HEARTBEAT = 0
# BROKER_HEARTBEAT = 0
# CELERY_BROKER_HEARTBEAT_CHECKRATE = 0.5
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Chicago'
CELERY_PREFETCH_MULTIPLIER = 1
CELERY_IMPORTS = ('the_thing.tasks',)
CELERY_RESULT_EXTENDED = True

# CELERY_ALWAYS_EAGER = True
CELERY_TASK_RESULT_EXPIRES = 120  # 1 mins
CELERYD_MAX_TASKS_PER_CHILD = 1500
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_ACKS_LATE = False
CELERY_CREATE_MISSING_QUEUES = True
CELERY_TASK_DEFAULT_QUEUE = "chaz"
CELERY_QUEUES = (
    Queue(
        'chaz'
    )
)

CELERY_TASK_ROUTES  = {
    'the_thing.tasks.*': {'queue': 'chaz'}
}

###########################################################################################
# Rest API STUFFz
###########################################################################################
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_PERMISSION_CLASSES': (
      'rest_framework.permissions.IsAuthenticated',
    ),
    "DEFAULT_THROTTLE_RATES": {"user_per_client": "120/min"},
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'durin.auth.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication', 
    )

}

DEFAULT_TOKEN_TTL = int(os.getenv("DEFAULT_TOKEN_TTL", "30"))


REST_DURIN = {
        "DEFAULT_TOKEN_TTL": timedelta(minutes=DEFAULT_TOKEN_TTL),
        "TOKEN_CHARACTER_LENGTH": 64,
        "USER_SERIALIZER": None,
        "AUTH_HEADER_PREFIX": "Token",
        "TOKEN_CACHE_TIMEOUT": 60,
        "REFRESH_TOKEN_ON_LOGIN": False,
        "AUTHTOKEN_SELECT_RELATED_LIST": ["user"],
        "API_ACCESS_CLIENT_NAME": None,
        "API_ACCESS_EXCLUDE_FROM_SESSIONS": False,
        "API_ACCESS_RESPONSE_INCLUDE_TOKEN": False,
}

# Enable CORS for all domains
if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_HOSTS",  '*').split(" ")
else:
    CORS_ORIGIN_ALLOW_ALL = os.getenv("CORS_ORIGIN_ALLOW_ALL", "False").lower() in SHITS_VALID_YO
    CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = True
CSRF_HEADER_NAME="HTTP_CSRFTOKEN"

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    }
}

###########################################################
# STATIC FILE STUFFZ
# (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
###########################################################
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "staticfiles"),)

# YOU THINK YOU DID SOMETHING STUPID... Youre proably right 🫰👉
try:
    LOCAL_SETTINGS
except NameError:
    try:
        from chaz.settings_local import *
    except ImportError:
        pass
