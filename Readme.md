# Запуск проекта
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
- Восстановление данных из бекапа: 
    ```
    sudo docker exec \
        -i \
        catsekb.ru-postgres \
        psql -U catsekb -d catsekb < dump_name.sql
    ```


