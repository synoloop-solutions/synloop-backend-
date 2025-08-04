from .base import *
import os
import dj_database_url
print("production")
environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))

DEBUG = False

SECRET_KEY = env("SECRET_KEY", default="test_key")

DATABASES = {
    'default': dj_database_url.config(
        engine='django.db.backends.postgresql',
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
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
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",")

CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS").split(",")

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'django_cache',
    }
}
