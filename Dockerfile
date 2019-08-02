FROM python:3.6.7-stretch

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
COPY static ./static
COPY manage.py ./
COPY gunicorn.conf.py ./

COPY docker-entrypoint.sh ./

ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
