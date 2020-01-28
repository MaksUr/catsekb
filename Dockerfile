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
COPY static ./static
COPY templates ./templates
COPY manage.py ./
COPY gunicorn.conf.py ./

COPY docker-entrypoint.sh ./

ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
