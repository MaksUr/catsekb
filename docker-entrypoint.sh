#!/usr/bin/env bash
set -e

# Создание статичных файлов
python /catsekb.ru/manage.py collectstatic --clear --noinput

# Миграция должна запускаться в отдельном процессе, иначе контейнер может отвалиться во время миграции и все сломается.
python /catsekb.ru/manage.py migrate

exec gunicorn -c ./gunicorn.conf.py catsekb.wsgi:application
