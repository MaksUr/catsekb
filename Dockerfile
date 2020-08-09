# Frontend
# Копипаста из Dockerfile_front
# TODO: убрать копипасту, сделать чтобы этот файл запускал команды из файла Dockerfile_front
FROM node:11

WORKDIR /front
COPY static/catsekb/package.json .
COPY static/catsekb/yarn.lock .
RUN yarn
COPY static/catsekb/gulpfile.js ./gulpfile.js
COPY static/catsekb/app ./app
RUN node node_modules/gulp/bin/gulp.js build

# Django
FROM python:3.7-stretch

RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-dev libsystemd-dev gettext

WORKDIR /catsekb.ru
COPY requirements.txt ./
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


WORKDIR /var/log/gunicorn/
RUN touch error.log
RUN touch access.log

VOLUME /srv/

WORKDIR /catsekb.ru

COPY catsekb ./catsekb
COPY articles ./articles
COPY cats ./cats
COPY catsekb_page ./catsekb_page
COPY huskyekb_page ./huskyekb_page
COPY rotvodom_page ./rotvodom_page
COPY payments ./payments
# Всю папку static копировать не нужно, нужно копировать только dist/
COPY static/admin ./static/admin
COPY --from=0 /front/dist ./static/catsekb/dist
COPY templates ./templates
COPY manage.py ./
COPY gunicorn.conf.py ./

COPY docker-entrypoint.sh ./

ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
