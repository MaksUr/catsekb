from os.path import join

from cats.update_scripts.downloader.bd_to_json import save_json
from catsekb.constants import VK_GROUP_ID

try:
    import requests
except ImportError:
    requests = None


def get_wall_news(group_id=VK_GROUP_ID):
    group_id = -1 * group_id
    access_token = input('token <<')
    news = requests.get(
        r'https://api.vk.com/method/wall.get', params={
            'owner_id': group_id,
            'count': 100,
            'extended': 0,
            'access_token': access_token
        }
    ).json()
    save_json(join('articles', 'articles_list', 'news.json'), news)
    return news


def get_post_by_id_list(posts_ids, group_id=VK_GROUP_ID):
    group_id = -1 * group_id
    s = str(group_id) + ','
    posts = s.join(posts_ids)
    access_token = input('token <<')
    news = requests.get(
        r'https://api.vk.com/method/wall.get', params={
            'posts': posts,
            'access_token': access_token
        }
    ).json()
    save_json(join('articles', 'articles_list', 'news2.json'), news)
    return news

