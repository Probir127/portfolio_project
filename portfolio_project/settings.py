import os
from pathlib import Path
import os 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# For development, you can use a simple key. For production, use environment variable
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Set to True for development, False for production
DEBUG = True

# Add localhost for development
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'probirdomain.com', 'www.probirdomain.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio_app',
]

MIDDLEWARE = [
    # IMPORTANT: WhiteNoise must be placed immediately after SecurityMiddleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- ADDED WhiteNoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_project.urls'

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

WSGI_APPLICATION = 'portfolio_project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Security settings - only enable these in production (when DEBUG = False)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'  # Changed to your timezone
USE_I18N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Render-specific Production Configuration
# ----------------------------------------
# This ensures that when deployed, the app will run in production mode
# and correctly handle static files and allowed hosts.
if 'RENDER' in os.environ:
    # 3. OVERRIDE DEBUG IN PRODUCTION
    #    This is a safeguard to ensure DEBUG is always False on Render
    DEBUG = False 

    # Set the host header based on the RENDER environment variable for security
    ALLOWED_HOSTS.append(os.environ.get('RENDER_EXTERNAL_HOSTNAME'))

    # Activate Django's WhiteNoise to serve static files correctly
    # Note: WhiteNoise middleware already added above.
    
    pass
