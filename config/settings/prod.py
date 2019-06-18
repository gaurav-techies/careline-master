"""
Prod Function Configurations

- Use Amazon's S3 for storing static files and uploaded media
- Use mailgun to send emails
- Use Redis for cache

- Use sentry for error logging
"""

from datetime import datetime
from datetime import timedelta

import requests
import credstash

from .base import *  # noqa
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend


DEBUG = False

# Admin URL path for obfuscating the admin interface
WAGTAIL_URLKEY = credstash.getSecret('ADMIN_URL_PATH', table='prod')

ENVIRONMENT_NAME = "Prod server"
ENVIRONMENT_COLOR = "#fadb0c"
ENVIRONMENT_ADMIN_SELECTOR = "grp-header"

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = credstash.getSecret('DJANGO_SECRET_KEY', table='prod')

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DSN = credstash.getSecret('DJANGO_SENTRY_DSN', table='prod')
RAVEN_CONFIG = {
    'dsn': credstash.getSecret('DJANGO_SENTRY_DSN', table='prod'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}

WEBSITE_DOMAIN = credstash.getSecret('DJANGO_WEBSITE_DOMAIN', table='prod')

# SECURITY CONFIGURATION
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/ref/middleware/#module-django.middleware.security
# and https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#run-manage-py-check-deploy

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = credstash.getSecret('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', table='prod')
SECURE_CONTENT_TYPE_NOSNIFF = credstash.getSecret('DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', table='prod')
SECURE_BROWSER_XSS_FILTER = False
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
CSRF_USE_SESSIONS = True

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts

ALLOWED_HOSTS_LIST = []

# This grabs AWS Internal ip then appends to allowed hosts
EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.01).text
except requests.exceptions.RequestException:
    pass
if EC2_PRIVATE_IP and not DEBUG:
    ALLOWED_HOSTS_LIST.append(EC2_PRIVATE_IP)

# EXTRA_TEST_ALLOWED_HOST = ['ec2-34-240-106-107.eu-west-1.compute.amazonaws.com']
ALLOWED_HOSTS = [credstash.getSecret('DJANGO_WEBSITE_DOMAIN', table='prod'),
                credstash.getSecret('EXTERNAL_ELB_ENDPOINT', table='prod'),
                 EC2_PRIVATE_IP]
# END SITE CONFIGURATION

INSTALLED_APPS += ['gunicorn']

INSTALLED_APPS = ['collectfast', ] + INSTALLED_APPS

# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['storages', ]

S3_USE_SIGV4 = True
AWS_DEFAULT_ACL = None
AWS_STORAGE_BUCKET_NAME = credstash.getSecret('DJANGO_S3_CDN_AWS_STORAGE_BUCKET_NAME', table='prod')
AWS_S3_REGION_NAME = credstash.getSecret('AWS_DEFAULT_REGION', table='prod')
AWS_ACCESS_KEY_ID = credstash.getSecret('DJANGO_S3_CDN_AWS_ACCESS_KEY_ID', table='prod')
AWS_SECRET_ACCESS_KEY = credstash.getSecret('DJANGO_S3_CDN_AWS_SECRET_ACCESS_KEY', table='prod')

# Tell django-storages the domain to use to refer to static files.
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# Serve from cloudfront
CLOUDFRONT_DOMAIN = credstash.getSecret('CLOUDFRONT_CDN_URL', table='prod')
CLOUDFRONT_ID = credstash.getSecret('CLOUDFRONT_CDN_ID', table='prod')

AWS_S3_CUSTOM_DOMAIN = CLOUDFRONT_DOMAIN # to make sure the url that the files are served from this domain

todaysDate = datetime.now() + timedelta(days=1)
formatedFutureDate = todaysDate.strftime("%Y-%m-%d %H:%M:%S")

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    # 'Expires': formatedFutureDate,
}

AWS_IS_GZIPPED = True

# Static Assets
STATICFILES_LOCATION = 'assets'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# Media Assets
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

AWS_PRELOAD_METADATA = True

# COMPRESSOR
# ------------------------------------------------------------------------------
COMPRESS_STORAGE = STATICFILES_STORAGE = 'custom_storages.StaticStorage'
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = credstash.getSecret('COMPRESS_ENABLED', table='prod')

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = 'connect@catholiccare.org'
AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

ANYMAIL = {
    "MAILGUN_API_KEY": credstash.getSecret('DJANGO_MAILGUN_API_KEY', table='prod'),
    "MAILGUN_SENDER_DOMAIN": credstash.getSecret('DJANGO_MAILGUN_SERVER_NAME', table='prod'),  # your Mailgun domain, if needed
}

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': credstash.getSecret('DJANGO_DBENGINE', table='prod'),
        'NAME': credstash.getSecret('DJANGO_DBNAME', table='prod'),
        'USER': credstash.getSecret('DJANGO_DBUSER', table='prod'),
        'PASSWORD': credstash.getSecret('DJANGO_DBPASS', table='prod'),
        'HOST': credstash.getSecret('DJANGO_DBHOST', table='prod'),
        'PORT': credstash.getSecret('DJANGO_DBPORT', table='prod'),
    }
}

# CACHING
# ------------------------------------------------------------------------------

REDIS_LOCATION = '{0}://{1}/{2}'.format('redis', credstash.getSecret('ELASTICACHE_ENDPOINT', table='prod'), 0)
# Heroku URL does not pass the DB number, so we parse it in
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

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

########## CELERY
INSTALLED_APPS += ['taskapp.celery.CeleryConfig']
CELERY_BROKER_URL = credstash.getSecret('CELERY_BROKER_URL', table='prod')
if CELERY_BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL

BROKER_URL = '{0}://{1}'.format('redis', credstash.getSecret('ELASTICACHE_ENDPOINT', table='prod'))
CELERY_RESULT_BACKEND = '{0}://{1}'.format('redis', credstash.getSecret('ELASTICACHE_ENDPOINT', table='prod'))

CELERY_SEND_TASK_ERROR_EMAILS = True
ADMINS = (
    (credstash.getSecret('DJANGO_ADMIN_NAME', table='prod'), credstash.getSecret('DJANGO_ADMIN_EMAIL', table='prod')
))

# In development, all tasks will be executed locally by blocking until the task returns
# CELERY_ALWAYS_EAGER = False
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
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = credstash.getSecret('DJANGO_ADMIN_EMAIL', table='prod')


WAGTAIL_PASSWORD_MANAGEMENT_ENABLED = False
WAGTAIL_PASSWORD_RESET_ENABLED = False
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'matt.millen@icloud.com'
WAGTAILADMIN_NOTIFICATION_USE_HTML = True

WAGTAIL_ENABLE_UPDATE_CHECK = False

# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.search.backends.elasticsearch5',
#         'URLS': [credstash.getSecret('ES_DOMAIN', table='prod')],
#         'INDEX': 'wagtail',
#         'TIMEOUT': 5,
#         'OPTIONS': {
#            'use_ssl': True,
#            'verify_certs': False,
#         },
#         'INDEX_SETTINGS': {},

#     }
# }

LOGIN_REDIRECT_URL = credstash.getSecret('LOGIN_REDIRECT_URL', table='prod')

# ZOHO API CREDS
ACCOUNTS_URL = credstash.getSecret('ZOHO_ACCOUNTS_URL', table='prod')
CLIENT_ID = credstash.getSecret('ZOHO_CLIENT_ID', table='prod')
CLIENT_SECRET = credstash.getSecret('ZOHO_SECRET_ID', table='prod')
REFRESH_TOKEN = credstash.getSecret('ZOHO_REFRESH_TOKEN', table='prod')
API_DOMAIN = credstash.getSecret('ZOHO_API_DOMAIN', table='prod')
ACCOUNT_ID = credstash.getSecret('ZOHO_ACCOUNT_USER_ID', table='prod')


# Bitly link API integration
BITLY_LOGIN = credstash.getSecret('BITLY_LOGIN', table='prod')
BITLY_API_KEY = credstash.getSecret('BITLY_API_KEY', table='prod')
BITLY_ACCESS_TOKEN = credstash.getSecret('BITLY_ACCESS_TOKEN', table='prod')
BITLY_TIMEOUT = 5

# Twilio API integration
TWILIO_ACCOUNT_SID = credstash.getSecret('TWILIO_ACCOUNT_SID', table='prod')
TWILIO_AUTH_TOKEN = credstash.getSecret('TWILIO_AUTH_TOKEN', table='prod')

CDN_DOMAIN = credstash.getSecret('CDN_DOMAIN', table='prod')

# Auth0 Config

certificate_text = credstash.getSecret('AUTH_CERT', table='prod').encode()
certificate = load_pem_x509_certificate(certificate_text, default_backend())
default_publickey = certificate.public_key()

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_auth0.authentication.Auth0JSONWebTokenAuthentication',
    ),
}

AUTH0 = {
    'CLIENTS': {
        'default': {
            'AUTH0_CLIENT_ID': credstash.getSecret('AUTH_ID', table='prod'),
            'AUTH0_ALGORITHM': 'RS256',
            'PUBLIC_KEY': default_publickey
        }
    },
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # default prefix used by djangorestframework_jwt
    'AUTHORIZATION_EXTENSION': False,  # default to False
    'USERNAME_FIELD': 'email'
}

SCARFACE_AWS_ACCESS_KEY = credstash.getSecret('SNS_ACCESS_KEY', table='prod')
SCARFACE_AWS_SECRET_ACCESS_KEY = credstash.getSecret('SNS_ACCESS_SECRET', table='prod')
SCARFACE_REGION_NAME = credstash.getSecret('SNS_REGION_NAME', table='prod')
PUSH_APPLE = credstash.getSecret('PUSH_ARN_APPLE', table='prod')
