from .base import *
import os
import dj_database_url

environ.Env.read_env(os.path.join(BASE_DIR, '.env.local'))

SECRET_KEY = env("SECRET_KEY", default="test_key")

DEBUG = env("DEBUG", default="True")

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="localhost,").split(",")

DATABASES = {
    "default":dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# Static files (served locally)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Local media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS").split(",")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("DJANGO_EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env("DJANGO_EMAIL_PORT", default=587)
EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'django_cache',
    }
}
