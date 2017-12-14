from django.core.exceptions import FieldError
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from os.path import join

from articles.article_constants import ARTICLES_DEFAULT_MAPPING, ARTICLE_FIND_CAT_ID, CAPTION, NEWS_VERBOSE_NAME_PLURAL, \
    ARTICLE_VERBOSE_NAME_PLURAL, ARTICLE_TITLE, ARTICLE_TEXT
from articles.models import Article
from cats.cats_constants import GROUP_INSTANCE_ALL_ID, GROUP_INSTANCE_SHELTER_ID, \
    GROUP_INSTANCE_HOME_ID, GROUP_INSTANCE_DEAD_ID, GROUP_MAPPING, PRIVATE_GROUP, ANIMAL_LOCATION_STATUS
from cats.models import Group
from catsekb.constants import SHOW, GET_PAR_KEY_FILTER, URL_NAME_ANIMALS, URL_NAME_FIND_CAT, URL_NAME_NEWS_FEED, \
    URL_NAME_SUBJECTS_FEED, DJ_ID, FOLDER
from catsekb.settings import BASE_DIR


def create_or_update_default_articles():

    for art_id in ARTICLES_DEFAULT_MAPPING:
        fp = join(BASE_DIR, ARTICLES_DEFAULT_MAPPING[art_id][FOLDER])
        try:
            f = open(fp, 'r')
            t = f.read()
        except (OSError, IOError):
            f = open(fp, 'w')
            t = ''
        Article.objects.get_or_create(
            id=art_id, defaults={
                DJ_ID: art_id,
                ARTICLE_TITLE: ARTICLES_DEFAULT_MAPPING[art_id][CAPTION],
                ARTICLE_TEXT: t
            }
        )


def get_objects_from_query(model_cls, query, show_permission=False, order_by=None):
    """

    :type order_by: str
    :type model_cls: django.db.models.Model | articles.models.Article | articles.models.Animal| articles.models.Group 
    :type show_permission: bool
    :type query: dict
    """
    if show_permission is False:
        query[SHOW] = True
    try:
        if order_by is not None:
            res = model_cls.objects.filter(**query).order_by(order_by)
        else:
            res = model_cls.objects.filter(**query)
    except FieldError:
        raise Http404("Запрос неверный")
    return res


def get_group(group_id, show_permission=False):
    if group_id in GROUP_MAPPING:
        if show_permission is False and group_id in PRIVATE_GROUP:
            raise Http404('Нет прав для просмотра данной группы.')
        return Group.get_group_with_certain_settings(name=GROUP_MAPPING[group_id]['name'],
                                                     group_id=group_id,
                                                     description=GROUP_MAPPING[group_id]['description'])
    else:
        query = dict()
        query['id'] = group_id
        if show_permission is False:
            query['show'] = True
        res = get_object_or_404(Group, **query)
        return res


def get_default_group_list(show_permission=False):
    default_group_list = list()
    default_group_list.append(get_group(group_id=GROUP_INSTANCE_ALL_ID, show_permission=show_permission))
    default_group_list.append(get_group(group_id=GROUP_INSTANCE_SHELTER_ID, show_permission=show_permission))
    default_group_list.append(get_group(group_id=GROUP_INSTANCE_HOME_ID, show_permission=show_permission))
    if show_permission:
        default_group_list.append(get_group(group_id=GROUP_INSTANCE_DEAD_ID, show_permission=show_permission))
    return default_group_list


def get_base_context(active_menu, extra_title, show_permission=False):
    default_group_list = get_default_group_list(show_permission=show_permission)
    user_group_list = get_objects_from_query(model_cls=Group, query=dict(), show_permission=show_permission)

    animal_filter_url = dict()
    animal_filter_url['caption'] = 'Поиск'
    animal_filter_url['url'] = "{url}?{key}=1&{shelter_key}={shelter_value}".format(
        url=reverse(URL_NAME_ANIMALS),
        key=GET_PAR_KEY_FILTER,
        shelter_key=ANIMAL_LOCATION_STATUS,
        shelter_value=GROUP_INSTANCE_SHELTER_ID
    )

    helpful_info_list = list()
    find_cat_url = dict()
    find_cat_url['caption'] = ARTICLES_DEFAULT_MAPPING[ARTICLE_FIND_CAT_ID][CAPTION]
    find_cat_url['url'] = reverse(URL_NAME_FIND_CAT)
    news = dict()
    news['caption'] = NEWS_VERBOSE_NAME_PLURAL
    news['url'] = reverse(URL_NAME_NEWS_FEED)
    articles = dict()
    articles['caption'] = ARTICLE_VERBOSE_NAME_PLURAL
    articles['url'] = reverse(URL_NAME_SUBJECTS_FEED)
    helpful_info_list.append(find_cat_url)
    helpful_info_list.append(news)
    helpful_info_list.append(articles)

    context = {
        'group_list': [animal_filter_url] + default_group_list + list(user_group_list),
        'helpful_info_list': helpful_info_list,
        'active_menu': active_menu,
        'extra_title': extra_title,
    }
    return context


