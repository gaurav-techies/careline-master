"""
Local settings

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .base import *  # noqa

from boto.s3.connection import OrdinaryCallingFormat
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

WAGTAIL_URLKEY = os.environ.get('ADMIN_URL_PATH')

INSTALLED_APPS += ['sslserver', ]

# Admin URL path for obfuscating the admin interface
# ADMIN_URL_PATH=os.environ.get('ADMIN_URL_PATH')

ENVIRONMENT_NAME = "Local server"
ENVIRONMENT_COLOR = "#1dc022"
ENVIRONMENT_ADMIN_SELECTOR = "grp-header"

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = os.environ.get('DJANGO_SECRET_KEY', default='CHANGEME!!!')
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DJANGO_DBENGINE"),
        'NAME': os.environ.get("DJANGO_DBNAME"),
        'USER': os.environ.get("DJANGO_DBUSER"),
        'PASSWORD': os.environ.get("DJANGO_DBPASS"),
        'HOST': os.environ.get("DJANGO_DBHOST"),
        'PORT': os.environ.get("DJANGO_DBPORT"),
    }
}
# ALTER USER django CREATEDB;


# Mail settings
# ------------------------------------------------------------------------------

DEFAULT_FROM_EMAIL = os.environ.get("DJANGO_DEFAULT_FROM_EMAIL"),

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("DJANGO_MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": os.environ.get("DJANGO_MAILGUN_SERVER_NAME"),  # your Mailgun domain, if needed
}

# Mailserver configuration
EMAIL_HOST = os.environ.get('DJANGO_MAILGUN_SMTP_OUT')
EMAIL_PORT = 25
EMAIL_HOST_USER = os.environ.get('DJANGO_MAILGUN_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_MAILGUN_PASSWORD')

# Email address used as sender (From field).
SERVER_EMAIL = os.environ.get('DJANGO_SERVER_EMAIL')


# CACHING
# ------------------------------------------------------------------------------
REDIS_LOCATION = os.environ.get("REDIS_LOCATION")
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_LOCATION,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    }
}

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['debug_toolbar',]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1', '10.0.0.11', '10.0.0.10', '172.20.10.2', '10.0.0.19', ]

ALLOWED_HOSTS = ['dev.carelineapp.org', '10.0.0.11', '10.0.0.42', '10.0.0.10', 'c5ef9f07.ngrok.io', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'django_extensions',
]

# # # TESTING
# # # ------------------------------------------------------------------------------
# # TEST_RUNNER = 'django.test.runner.DiscoverRunner'
#

MEDIA_URL = '/media/'

########## CELERY
INSTALLED_APPS += ['taskapp.celery.CeleryConfig']
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', default='django://')
if CELERY_BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL

BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_BROKER_URL')

CELERY_SEND_TASK_ERROR_EMAILS = True
ADMINS = (
    (os.environ.get('DJANGO_ADMIN_NAME'), os.environ.get('DJANGO_ADMIN_EMAIL')),
)

# In development, all tasks will be executed locally by blocking until the task returns
CELERY_ALWAYS_EAGER = False
CELERY_TRACK_STARTED = True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_EVENT_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CELERY_SEND_TASK_ERROR_EMAILS = True
ADMINS = (
    ('Matt', 'matt.millen@icloud.com'),
)
########## END CELERY

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------


### DJANGO AXES CONFIG
# AXES_LOGIN_FAILURE_LIMIT = 3
# AXES_LOCK_OUT_AT_FAILURE = True
# AXES_USE_USER_AGENT = True
# AXES_VERBOSE = True
# AXES_REVERSE_PROXY_HEADER = False
# AXES_DISABLE_SUCCESS_ACCESS_LOG = False
# AXES_DISABLE_ACCESS_LOG = False


# for s3
THUMBNAIL_FORCE_OVERWRITE = True
MAPS_API = os.environ.get("MAPS_API_KEY")
BASE_URL = "https://dev.careline.app"

WEBSITE_DOMAIN = os.environ.get('DJANGO_WEBSITE_DOMAIN')
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = os.environ.get('DJANGO_ADMIN_EMAIL')

AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION')

ADMIN_URL_PATH = os.environ.get('ADMIN_URL_PATH')

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.elasticsearch5',
        'URLS': [os.environ.get('ES_DOMAIN')],
        'INDEX': 'wagtail',
        'TIMEOUT': 5,
        'OPTIONS': {},
        'INDEX_SETTINGS': {},
    }
}

WAGTAIL_AUTO_UPDATE_PREVIEW = True

DSN = os.environ.get('DJANGO_SENTRY_DSN')
RAVEN_CONFIG = {
    'dsn': os.environ.get('DJANGO_SENTRY_DSN'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}


LOGIN_REDIRECT_URL = os.environ.get('LOGIN_REDIRECT_URL')

SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS')

ACCOUNTS_URL = os.environ.get('ZOHO_ACCOUNTS_URL')
CLIENT_ID = os.environ.get('ZOHO_CLIENT_ID')
CLIENT_SECRET = os.environ.get('ZOHO_SECRET_ID')
REFRESH_TOKEN = os.environ.get('ZOHO_REFRESH_TOKEN')
API_DOMAIN = os.environ.get('ZOHO_API_DOMAIN')
ACCOUNT_ID = os.environ.get('ZOHO_ACCOUNT_USER_ID')

# Bitly link API integration
BITLY_LOGIN = os.environ.get('BITLY_LOGIN')
BITLY_API_KEY = os.environ.get('BITLY_API_KEY')
BITLY_ACCESS_TOKEN = os.environ.get('BITLY_ACCESS_TOKEN')

BITLY_TIMEOUT = 5

# Twilio API integration
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

CDN_DOMAIN = os.environ.get('CDN_DOMAIN')

# Auth0 Config
#certificate_text = os.environ.get('AUTH_CERT').encode()
certificate_text ='-----BEGIN CERTIFICATE-----\n' + os.environ.get('AUTH_CERT') + '\n-----END CERTIFICATE-----' #os.environ.get('AUTH_CERT').encode()
#certificate = load_pem_x509_certificate(certificate_text, default_backend())
certificate = load_pem_x509_certificate(str.encode(certificate_text), default_backend())
default_publickey = certificate.public_key()

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_auth0.authentication.Auth0JSONWebTokenAuthentication',
    ),
}

AUTH0 = {
    'CLIENTS': {
        'default': {
            'AUTH0_CLIENT_ID': os.environ.get('AUTH_ID'),
            'AUTH0_ALGORITHM': 'RS256',
            'PUBLIC_KEY': default_publickey
        }
    },
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # default prefix used by djangorestframework_jwt
    'AUTHORIZATION_EXTENSION': False,  # default to False
    'USERNAME_FIELD': 'email'
}


AWS_ACCESS_KEY = os.environ.get("SNS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("SNS_ACCESS_SECRET")
SCARFACE_REGION_NAME = os.environ.get("SNS_REGION_NAME")
PUSH_APPLE = os.environ.get("PUSH_ARN_APPLE")

# SCARFACE_REGION_NAME =
# SCARFACE_LOGGING_ENABLED =
# SCARFACE_PLATFORM_STRATEGIES =
# SCARFACE_MESSAGE_TRIM_LENGTH =