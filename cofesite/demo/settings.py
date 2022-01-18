import os
import  dj_database_url
import django_heroku
import psycopg2
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj'
ALLOWED_HOSTS = ['https://rishi-restaurant.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
    'django_summernote',
    'ckeditor',
    

    'core',
    'userprofile',
    'blogs'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 ],
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
TIME_INPUT_FORMATS = ('%I:%M%p',)
USE_I18N = True
USE_L10N = False
USE_TZ = True


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ACCOUNT_ADAPTER = 'userprofile.views.MyAccountAdapter'
ACCOUNT_FORMS = {'signup': 'userprofile.forms.MyCustomSignupForm'}


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_1',
        'USER': 'postgres',
        'PASSWORD': 'hariharan',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

if ENVIRONMENT == 'production':
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
ACCOUNT_EMAIL_VERIFICATION = 'none'
STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFileStorage '
#LOGIN_REDIRECT_URL = {% url 'account:dashboard' %}
#LOGIN_REDIRECT_URL = '/'

django_heroku.settings(locals())
