from .base import *
import os
import dj_database_url
environ.Env.read_env(os.path.join(BASE_DIR, '.env.local'))

DEBUG = False

DATABASES = {
    "default":dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}


# Static files (served locally)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Local media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ALLOWED_HOSTS = env(ALLOWED_HOSTS)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'django_cache',
    }
}
