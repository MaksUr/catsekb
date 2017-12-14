from articles.models import News
from articles.update_scripts.article_updater import ArticleText
from articles.update_scripts.vk_news_response import get_wall_news
from cats.updater import RESPONSE

try:
    import requests
except ImportError:
    requests = None


def get_video_url_from_video_attach(video_attach):
    # TODO: implement
    return video_attach.get('image') or ''


def get_media_from_attachments(attachments):
    res = ''
    for att in attachments:
        if att.get('photo'):
            res += att['photo']['src'] + '/n'
        if att.get('video'):
            res += get_video_url_from_video_attach(att['video']) + '/n'


def get_text_from_post(post):
    if post.get('text') is not None:
        text = post['text']
    else:
        text = ''
    if text.get('attachments') is not None:
        text += get_media_from_attachments(text.get('attachments'))
    return text


def get_date_from_post(post):
    pass


def update_or_create_news(post):
    post_id = post.get('id')
    if post_id is None:
        return None
    text = get_text_from_post(post)
    text = ArticleText(text).get_text()
    defaults = {
        'text': text,
        'created': get_date_from_post(post),
        'vk_album_id': post_id
    }
    News.objects.get_or_create(id=post_id, defaults=defaults)


def update_news_from_vk():
    news = get_wall_news()
    if news is None:
        return None
    try:
        news_list = news[RESPONSE]
    except (KeyError):
        return None
    for post in news_list:
        if isinstance(post, dict):
            update_or_create_news(post)

