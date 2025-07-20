from .base import *
import os
environ.Env.read_env(os.path.join(BASE_DIR, '.env.local'))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (served locally)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Local media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


USE_S3 = False

if USE_S3:
    AWS_ACCESS_KEY_ID = env("S3_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("S3_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = "localhost:9444/ui/mesh"
    AWS_S3_ENDPOINT_URL = env("S3_ENDPOINT_URL")
    AWS_S3_USE_SSL = False
    AWS_S3_URL_PROTOCOL = "http:"

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "bucket_name": AWS_STORAGE_BUCKET_NAME,
                "custom_domain": AWS_S3_CUSTOM_DOMAIN,
                "endpoint_url": AWS_S3_ENDPOINT_URL,
                "use_ssl": False,
            },
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
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
