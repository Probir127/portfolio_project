from pathlib import Path
import os 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 1. READ THE SECRET_KEY FROM THE ENVIRONMENT
#    (Provide a default only for local development)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-YOUR_RANDOM_SECRET_KEY')

# 2. SET DEBUG TO READ FROM THE ENVIRONMENT
#    (Defaults to True for local development)
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom App: Add your portfolio application here
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


# Database
# For a small project, SQLite is fine.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# (default settings omitted for brevity)

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka' # Set to your local time zone
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# Configuration for serving static files in production
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Location where collectstatic puts files

# Collect static files from all app static directories
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Configure WhiteNoise to serve compressed static files
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Media files configuration (for uploaded images like profile_pic.jpg)
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
