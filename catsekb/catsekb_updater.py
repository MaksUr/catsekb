from articles.update_scripts.article_updater import update_articles
from articles.update_scripts.news_updater import update_news_from_vk
from cats.update_scripts.all_update import update_all_animals_from_vk


def all_update():
    update_all_animals_from_vk()
    update_news_from_vk()
    update_articles()
