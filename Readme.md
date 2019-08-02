# Запуск проекта
build образа с помощью докера: `docker build -t catsekb.ru:latest .`
запуск контейнера: `docker run -ti --rm -p 8000:80 -v ~/rep/sites/catsekb/vk_token.txt:/srv/vk_token.txt -v ~/rep/sites/catsekb/db.sqlite3:db.sqlite3 catsekb.ru:latest`
docker run -ti --rm -p 8000:80 -v ~/rep/sites/catsekb/vk_token.txt:/srv/vk_token.txt catsekb.ru:latest
