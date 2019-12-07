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
            -v ~/rep/sites/catsekb/postgres:/var/lib/postgresql/data \
            postgres:11.2
    ```
- запуск контейнера для локальной разработки c постгресс: 
    ```
    docker run \
        -ti \
        --rm \
        -p 8000:80 \ 
        --network=mw \ 
        -v ~/rep/sites/catsekb/secret_key.txt:/srv/secret_key.txt \ 
        -v ~/rep/sites/catsekb/vk_token.txt:/srv/vk_token.txt \
        -v ~/rep/sites/catsekb/db_key.txt:/srv/db_key.txt catsekb.ru:latest
    ```
- Создание бекапа
    ```
    docker exec \
        -i \
        catsekb.ru-postgres \
        pg_dump -c -h localhost -U catsekb catsekb | gzip > catsekb_04_03_2019.backup.gz
    ```

- Восстановление данных из бекапа: 
    ```
    docker exec \
        -i \
        catsekb.ru-postgres \
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

- docker:
    - установить докер по инструкции https://www.digitalocean.com/community/tutorials/docker-ubuntu-18-04-1-ru
    - создать виртуальную сеть `docker network create --driver bridge mw`

- для переноса образа на виртуалку я тупо использую архив с образом (TODO: разобраться как это можно сделать по-человески с docker-registry)
    ```
    docker build -t catsekb.ru:latest . && \
    docker save catsekb.ru:latest > catsekb.tar && \
    docker save postgres:11.2 > postgres.tar && \
    docker save nginx:1.15.12 > nginx.tar
    ```

- перенести файлы на виртуалку:
     -  `configs/nginx/catsekb.ru.conf` в `/srv/catsekb.ru/nginx/catsekb.ru.conf`
     -  `configs/systemd/*` в `/etc/systemd/system/`
     
     - `catsekb.tar` в `~/catsekb.tar`
     - `postgres.tar` в `~/postgres.tar`
     - `nginx.tar` в `~/nginx.tar`
     
     - `secret_key.txt` в `/srv/catsekb.ru/secret_key.txt` - секретный ключ в Django
     - `vk_token.txt` в `/srv/catsekb.ru/vk_token.txt` - токен для доступа к Api
     - `db_key.txt` в `/srv/catsekb.ru/db_key.txt` - пароль к postgres 

- разорхивировать образы в докер:
    ```
    docker load < ~/catsekb.tar && \
    docker load < ~/postgres.tar && \
    docker load < ~/nginx.tar && \
    rm ~/*.tar
    ```
    
- для автоматического перезапуска используется systemd (TODO: использовать docker-compose):
    - чтобы применить изменения в systemd: `systemctl daemon-reload`
    - включить systemd jobs:
        ```
        systemctl enable docker-catsekb.ru-postgres.service && \
        systemctl enable docker-catsekb.ru-project.service && \ 
        systemctl enable docker-catsekb.ru-nginx.service
        
        ```
    - перезапустить джобы:
        ```
        systemctl restart docker-catsekb.ru-postgres.service && \
        systemctl restart docker-catsekb.ru-project.service && \
        systemctl restart docker-catsekb.ru-nginx.service 
        
        ```

- добавление сертификатов с помощью certbot:
    - установка: https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx (п. 1, 2)
    - в nginx нужно удалить блок ssl 443 порт:
        ```
        server {
        listen 80;
        server_tokens off;
        server_name catsekb.ru;
    
        # For letsencrypt
        location /.well-known/acme-challenge/ {
            root /usr/share/nginx/catsekb.ru;
        }
    
        location /static/ {
            alias /srv/static/;
        }
    
        location / {
    
            proxy_pass http://catsekb.ru:80;
            proxy_redirect off;
            proxy_set_header Host $http_host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    
      }
      ```
    - `sudo letsencrypt certonly -a webroot --webroot-path=/srv/catsekb.ru/nginx/share/ -d catsekb.ru`
    - вернуть обратно конфиг nginx и перезапустить джоб nginx
    - возможные проблемы:
        - https://github.com/certbot/certbot/issues/5868 Решение:
            - удалил папку `/etc/letsencrypt/live/catsekb.ru` 
            запустил команду `certonly` снова. 
            Изменил путь systemd шном джобе на `/etc/letsencrypt/live/catsekb.ru-0001`  


- выключить nginx:
    - проверить занят ли 80 порт nginx-ом: `sudo lsof -i -P -n | grep LISTEN` 
    - отключить nginx:
        ```
        systemctl stop nginx.service
        systemctl disable nginx.service
        ```
