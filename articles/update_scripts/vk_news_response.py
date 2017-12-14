from os.path import join

from cats.update_scripts.all_update import open_json
from cats.update_scripts.downloader.bd_to_json import save_json
from catsekb.constants import VK_GROUP_ID

try:
    import requests
except ImportError:
    requests = None


JSON_NEWS = join('articles', 'articles_list', 'news.json')


def get_wall_news(group_id=VK_GROUP_ID, access_token=None):
    if requests is None or access_token is None:
        return open_json(JSON_NEWS)
    group_id = -1 * group_id
    news = requests.get(
        r'https://api.vk.com/method/wall.get', params={
            'owner_id': group_id,
            'count': 100,
            'extended': 0,
            'access_token': access_token
        }
    ).json()
    save_json(JSON_NEWS, news)
    return news


def get_post_by_id_list(posts_ids, token, group_id=VK_GROUP_ID):
    if requests is None:
        return None
    group_id = -1 * group_id
    s = str(group_id) + ','
    posts = s.join([str(p) for p in posts_ids])
    access_token = token
    news = requests.get(
        r'https://api.vk.com/method/wall.get', params={
            'posts': posts,
            'access_token': access_token
        }
    ).json()
    return news

