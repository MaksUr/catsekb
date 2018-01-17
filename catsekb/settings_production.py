DEBUG = False

ALLOWED_HOSTS = ['catsekb.ru']

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

with open('/etc/db_key.txt') as f:
    db_key = f.read().strip()

#settings for db on server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_catsekb',
        'PASSWORD': db_key,
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
