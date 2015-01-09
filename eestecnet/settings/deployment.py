from secret import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER
ALLOWED_HOSTS = ['.eestec.net',]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11212',
        }
}

CACHE_MIDDLEWARE_ALIAS="default"
CACHE_MIDDLEWARE_SECONDS=30
CACHE_MIDDLEWARE_KEY_PREFIX=""

EMAIL_HOST="localhost"
EMAIL_PORT = 25
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'