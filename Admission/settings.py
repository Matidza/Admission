from pathlib import Path
import os
#import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-0^suq@5g&!0#n)7%=wd6=@h2i1yc4a%2q)qqpd_jf&jn3w_vok')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = [
    'admission.up.railway.app',
    'localhost',
    '127.0.0.1',
    'admission-6phv.onrender.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://admission.up.railway.app',
    'https://admission-6phv.onrender.com',
    'http://localhost',
    'http://127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admit',
    'school',
    'application',
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

ROOT_URLCONF = 'Admission.urls'

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
                'application.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'Admission.wsgi.application'

# Database
# Production database connection using environment variable
'''   '''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'wYLaHcnRtQyduiqwWZhGmPvvdhuXBKXH',
        'HOST': 'yamanote.proxy.rlwy.net',
        'PORT': '52241',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

#import dj_database_url

#DATABASES = {
#  'default': dj_database_url.parse(os.environ['Aiven'], conn_max_age=600)
#}


#DATABASES = {
#    'default': dj_database_url.parse(os.environ.get('AIVEN'), conn_max_age=600)
#}

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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Used for `collectstatic` in production

STATICFILES_DIRS = [BASE_DIR / 'static']  # Ensure this points to your 'static' folder
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'admissions.django@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your_email_password')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
