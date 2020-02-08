# Запуск проекта локально с помощью с докера
- build образа с помощью докера: `docker build -t catsekb.ru:latest .`
- запуск контейнера для локальной разработки: `docker run -ti --rm -p 8000:80 -v ~/rep/sites/catsekb/vk_token.txt:/srv/vk_token.txt -v ~/rep/sites/catsekb/db.sqlite3:/catsekb.ru/db.sqlite3 catsekb.ru:latest`
- для взаимодействия постгресса и проекта, нужно создать сеть: `docker network create --driver bridge mw`
- запуск контейнера с постгресс для локальной разработки:
    ```
    sudo docker run \
            --rm \
            --name catsekb.ru-postgres \
            -e POSTGRES_NAME=catsekb \
            -e POSTGRES_USER=catsekb \
            -e POSTGRES_PASSWORD=PSWD \
            --network=mw \
            -v /srv/catsekb.ru/postgres:/var/lib/postgresql/data \
            postgres:11.2
    ```
- запуск контейнера для локальной разработки c постгресс:
    ```
    docker run \
        -ti \
        --rm \
        -p 8000:80 \
        --network=mw \
        -v /srv/catsekb.ru/secret_key.txt:/srv/secret_key.txt \
        -v /srv/catsekb.ru/vk_token.txt:/srv/vk_token.txt \
        -v /srv/catsekb.ru/db_key.txt:/srv/db_key.txt catsekb.ru:latest
    ```
- Создание бекапа
    ```
    docker exec \
        -i \
        postgres \
        pg_dump -c -h localhost -U catsekb catsekb | gzip > catsekb_04_03_2019.backup.gz
    ```

- Восстановление данных из бекапа:
    ```
    docker exec \
        -i \
        postgres \
        psql -U catsekb -d catsekb < dump_name.sql
    ```

# Запуск проекта на виртуальной машине.

## Настройка виртуалки

- Для запуска, необходимо установить образ `ubuntu-18.04-server-amd64.iso` на виртуалку
(например стандартный менеджер виртуальных машин в ubuntu)
- из дополнительных возможностей установить только ssh сервер
- установить загрузчик GRUB (без этого не запустилось)
- после установки в файле `/etc/ssh/sshd_config` разкоментировать строку `PasswordAuthentication yes`
- перезапустить ssh сервис: `service ssh restart`
- для того чтобы подключить по ssh к виртуальке, можно узнать адрес, который назначается: `ip address show`

## Первоначальная настройка.

- установить `docker-compose`

- для переноса образа на виртуалку я тупо использую архив с образом (TODO: разобраться как это можно сделать по-человески с docker-registry)
    ```
    docker build -t catsekb.ru:latest . && \
    docker save catsekb.ru:latest > catsekb.tar
    ```

- перенести файлы на виртуалку:
     -  `configs/nginx/nginx.conf` в `/srv/catsekb.ru/nginx/nginx.conf`
     - `catsekb.tar` в `~/catsekb.tar`
     - `secret_key.txt` в `/srv/catsekb.ru/secret_key.txt` - секретный ключ в Django
     - `vk_token.txt` в `/srv/catsekb.ru/vk_token.txt` - токен для доступа к Api
     - `db_key.txt` в `/srv/catsekb.ru/db_key.txt` - пароль к postgres

- разорхивировать образы в докер:
    ```
    docker load < ~/catsekb.tar && \
    rm ~/*.tar
    ```

- для автоматического перезапуска используется docker-compose:
    - `docker-compose up`


- выключить nginx:
    - проверить занят ли 80 порт nginx-ом: `sudo lsof -i -P -n | grep LISTEN`
    - отключить nginx:
        ```
        systemctl stop nginx.service
        systemctl disable nginx.service
        ```

## Сертификаты

[Инструкция](https://miki725.com/docker/crypto/2017/01/29/docker+nginx+letsencrypt.html)

Первичная настройка:
```
docker run -it --rm \
      -v /srv/catsekb.ru/certs:/etc/letsencrypt \
      -v /srv/catsekb.ru/certs-data:/data/letsencrypt \
      deliverous/certbot \
      certonly \
      --webroot --webroot-path=/data/letsencrypt \
      -d xn--80aegc1blqbj1c4c.xn--p1ai -d www.xn--80aegc1blqbj1c4c.xn--p1ai
```

Обновление сертификата:
```
docker run -t --rm \
      -v /srv/catsekb.ru/certs:/etc/letsencrypt \
      -v /srv/catsekb.ru/certs-data:/data/letsencrypt \
      deliverous/certbot \
      renew \
      --webroot --webroot-path=/data/letsencrypt
$ docker-compose kill -s HUP nginx
```

# Frontend

Установка зависимостей `yarn`
Сборка `node node_modules/gulp/bin/gulp.js  build`  # TODO: Переписать gulp на webpack

## Docker
`cd static/catsekb/`
`docker build -t happy_house_front:latest .`
`docker run --rm -v ~/rep/sites/catsekb/static/catsekb/:/share happy_house_front:latest cp -r /dist /share`
