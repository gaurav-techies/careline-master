"""

Django settings for carelineapp project.



For more information on this file, see

https://docs.djangoproject.com/en/dev/topics/settings/



For the full list of settings and their values, see

https://docs.djangoproject.com/en/dev/ref/settings/

"""

# System libraries

from __future__ import unicode_literals
import os
import environ
import raven
# Django modules
from django.contrib import messages
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()
# import uuid
# UUID4 is random!
# my_uuid = uuid.uuid4()
# ROOT_DIR = environ.Path()-1
# APPS_DIR = ROOT_DIR.path('carelineapp')
# ON Local Only
ROOT_DIR = environ.Path()

APPS_DIR = ROOT_DIR.path('carelineapp')

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) - 1 # This is your Project Root
#
# APPS_DIR = os.path.join(ROOT_DIR, '')

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "django.contrib.sitemaps",
    'users',
]
THIRD_PARTY_APPS = [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.api.v2',
    'wagtail.contrib.settings',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.frontend_cache',
    'wagtailmetadata',
    'wagtailfontawesome',
    'widget_tweaks',
    'rest_framework_jwt',
    'rest_framework_auth0',

]

# Apps specific for this project go here.
LOCAL_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'api',
    # custom users app
    'carelineapp',
    'leads',
    'sms_messaging',
    'modelcluster',
    'taggit',
    # 'el_pagination',
    'cachalot',
    'raven.contrib.django.raven_compat',
    'condensedinlinepanel',
    # 'import_export',
    # 'wagtail_personalisation',
    # 'experiments',
    # 'wagtailembedder',
    'django_user_agents',
    'wagtail_feeds',
    'wagtail_2fa',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django.contrib.humanize',
    'scarface',
    'push'

]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'wagtail_2fa.middleware.VerifyUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = os.environ.get('DJANGO_DEBUG', False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = os.environ.get('DJANGO_DEFAULT_FROM_EMAIL',
                                    default='carelineapp <noreply@carelineapp.co>')
EMAIL_SUBJECT_PREFIX = os.environ.get('DJANGO_EMAIL_SUBJECT_PREFIX', default='[carelineapp]')
SERVER_EMAIL = os.environ.get('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# Anymail with Mailgun
INSTALLED_APPS += ['anymail', ]
ANYMAIL = {
    'MAILGUN_API_KEY': os.environ.get('DJANGO_MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': os.environ.get('DJANGO_MAILGUN_SENDER_DOMAIN')
}
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""Matt Millen""", 'matt.millen@icloud.com'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-gb'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            # str(os.path.join(APPS_DIR, 'templates')),
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'builtins': [],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'wagtail.contrib.settings.context_processors.settings',
                # 'wagtailmenus.context_processors.wagtailmenus',
                # 'leads.context_processors.global_settings',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATIC_ROOT = str(os.path.join(ROOT_DIR, 'assets'))
STATIC_ROOT = str(ROOT_DIR('assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/assets/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS = [
#     str(os.path.join(ROOT_DIR, 'assets/carelineapp'))
# ]
STATICFILES_DIRS = [
    # str(APPS_DIR.path('assets/carelineapp')),
    str(APPS_DIR.path('assets/carelineapp')),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# MEDIA_ROOT = str(os.path.join(APPS_DIR, 'media'))
MEDIA_ROOT = str(ROOT_DIR('media'))

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

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

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
AUTH_USER_MODEL = 'users.User'
# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# django-compressor
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['compressor']
STATICFILES_FINDERS += ['compressor.finders.CompressorFinder']

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
FEEDER_KEY = os.environ.get('FEEDER_API_KEY_VALUE')

# Wagtail Site Name
WAGTAIL_SITE_NAME = 'carelineapp'
# Wagtail settings

WAGTAILSEARCH_RESULTS_TEMPLATE = 'utils/tags/search/search_results.html'

DATE_INPUT_FORMATS = ('%Y-%m-%d %H:%i:%s')

# see http://developer.yahoo.com/performance/rules.html#expires
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

AWS_S3_OBJECT_PARAMETERS = {
    'Cache-Control': 'max-age=86400',
}
AWS_IS_GZIPPED = True

PHONENUMBER_DEFAULT_REGION = "AU"
PHONENUMBER_DB_FORMAT = "NATIONAL"

# Set this to the 'related_name' attribute used on the ParentalKey field
# WAGTAILMENUS_FLAT_MENU_ITEMS_RELATED_NAME = "footer"
# WAGTAILMENUS_DEFAULT_FLAT_MENU_TEMPLATE = 'home/menus/footer_menu.html'

WAGTAIL_USAGE_COUNT_ENABLED = True

WAGTAIL_ENABLE_UPDATE_CHECK = False

AWS_PRELOAD_METADATA = True

BS_SIZE = 'sm'

STREAMFIELDS = '__all__'
EXCLUDE_STREAMFIELDS = []

# Set this to the 'related_name' attribute used on the ParentalKey field
# WAGTAILMENUS_MAIN_MENU_ITEMS_RELATED_NAME = "custom_menu_items"

# Use the 'related_name' attribute you used on your custom model's ParentalKey field
# WAGTAILMENUS_FLAT_MENU_ITEMS_RELATED_NAME = "custom_footer_menu_items"


# CRM


# Blog Settings
# BLOG_PAGINATION_PER_PAGE = 10 #(Default 10) Set to change the number of blogs per page. Set to None to disable (useful if using your own pagination implementation).


# CORS_ORIGIN_WHITELIST = (
#     'carelineapp.com.au',
# )
#
# CSRF_TRUSTED_ORIGINS = (
#     'carelineapp.com.au',
# )
#
# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )
#
# CORS_ALLOW_METHODS = (
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# )
#
# CORS_ORIGIN_WHITELIST = (
#     'carelineapp.com.au',
# )

SCARFACE_LOGGING_ENABLED = True
