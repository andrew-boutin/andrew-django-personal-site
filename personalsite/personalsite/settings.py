"""Django settings for personalsite project."""
import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Determine if running on production or development
HOSTNAME = socket.gethostname()

if HOSTNAME == 'personal-site':
    DEBUG = False

    with open('/etc/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
else:
    DEBUG = True
    SECRET_KEY = 'wvnp@@jq+(@(+e!x6^kfv^=^xwmdr4+lp$=m@3#(9_sa^@2_a9'

ALLOWED_HOSTS = ['45.55.204.169']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'main',
]

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

ROOT_URLCONF = 'personalsite.urls'

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

WSGI_APPLICATION = 'personalsite.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Static files have to be somewhere besides /static/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# For security enhancements
# Prevent browsers rom guessing content types to prevent users maliciously overriding it
SECURE_CONTENT_TYPE_NOSNIFF = True

# Block potential XXS attacks
SECURE_BROWSER_XSS_FILTER = True

# Protect CSRF token from client side JavaScript
CSRF_COOKIE_HTTPONLY = True

# Protect Copyright data from being used in an Iframe
X_FRAME_OPTIONS = 'DENY'

# Admins who should be emailed about site errors that occur
ADMINS = (
    ('Andrew Boutin', 'andrew.w.boutin@gmail.com'),
)

# People who get specific notifications like broken link emails
MANAGERS = (
    ('Andrew Boutin', 'andrew.w.boutin@gmail.com'),
)

