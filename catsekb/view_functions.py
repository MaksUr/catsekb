from os.path import join

from django.core.exceptions import FieldError
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from articles.article_constants import ARTICLES_DEFAULT_MAPPING, ARTICLE_FIND_CAT_ID, CAPTION, \
    ARTICLE_VERBOSE_NAME_PLURAL, ARTICLE_TITLE, ARTICLE_TEXT, NEWS_IMPORTANT
from articles.models import Article, News
from cats.cats_constants import PRIVATE_GROUP, ANIMAL_LOCATION_STATUS, \
    ANIMAL_CREATED, GALLERY_DEFAULT_ITEMS_COUNT
from cats.models import Group, Animal
from cats.query import ANIMAL_QUERY_KEYS
from catsekb.constants import SHOW, GET_PAR_KEY_FILTER, URL_NAME_FIND_CAT, \
    URL_NAME_SUBJECTS_FEED, DJ_ID, FOLDER
from catsekb.settings import BASE_DIR

ABOUT_MENU_ITEMS_BASE_CONTEXT = [
    {'caption': 'О фонде', 'url': reverse_lazy('about')},
    {'caption': 'Документы', 'url': reverse_lazy('documents')},
    {'caption': 'Отчеты', 'url': reverse_lazy('reports')},
    {'caption': 'Сми о нас', 'url': reverse_lazy('media')},
]

OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT = [
    {'caption': 'Взять животное из приюта', 'url': reverse_lazy('get_animal_guide')},
    {'caption': 'CatsEkb', 'url': reverse_lazy('catsekb_page')},
    {'caption': 'HuskyEkb', 'url': reverse_lazy('huskyekb_page')},
    {'caption': 'Rotvodom', 'url': reverse_lazy('rotvodom_page')},
    {'caption': 'Новенькие', 'url': reverse_lazy('new_animals')}
]

CATSEKB_MENU_ITEMS_CONTEXT = [
    {'url': reverse_lazy('cats_in_shelter'), 'caption': 'Ищут дом'},
    {'url': reverse_lazy('cats_all'), 'caption': 'Все котики'},
    {'url': reverse_lazy('cats_in_home'), 'caption': 'Пристроены'},
    {'url': reverse_lazy('cats_dead'), 'caption': 'На радуге'},
]

HUSKYEKB_MENU_ITEMS_CONTEXT = [
    {'url': reverse_lazy('husky_in_shelter'), 'caption': 'Ищут дом'},
    {'url': reverse_lazy('husky_all'), 'caption': 'Все хаски'},
    {'url': reverse_lazy('husky_in_home'), 'caption': 'Пристроены'},
    {'url': reverse_lazy('husky_dead'), 'caption': 'На радуге'},
]

ROTVODOM_MENU_ITEMS_CONTEXT = [
    {'url': reverse_lazy('rotv_in_shelter'), 'caption': 'Ищут дом'},
    {'url': reverse_lazy('rotv_all'), 'caption': 'Все ротвейлеры'},
    {'url': reverse_lazy('rotv_in_home'), 'caption': 'Пристроены'},
    {'url': reverse_lazy('rotv_dead'), 'caption': 'На радуге'},
]

PROJECT_GROUPS_MAPPING = {
    'catsekb': CATSEKB_MENU_ITEMS_CONTEXT,
    'huskyekb': HUSKYEKB_MENU_ITEMS_CONTEXT,
    'rotvodom': ROTVODOM_MENU_ITEMS_CONTEXT,
    'main': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
}


def create_or_update_default_articles():

    for art_id in ARTICLES_DEFAULT_MAPPING:
        fp = join(BASE_DIR, ARTICLES_DEFAULT_MAPPING[art_id][FOLDER])
        try:
            f = open(fp, 'r', encoding='UTF-8')
            t = f.read()
        except (OSError, IOError):
            f = open(fp, 'w', encoding='UTF-8')
            t = ''
        f.close()
        article, created = Article.objects.get_or_create(
            id=art_id, defaults={
                DJ_ID: art_id,
                ARTICLE_TITLE: ARTICLES_DEFAULT_MAPPING[art_id][CAPTION],
                ARTICLE_TEXT: t
            }
        )
        if created is False:
            article.__setattr__(ARTICLE_TITLE, ARTICLES_DEFAULT_MAPPING[art_id][CAPTION])
            article.__setattr__(ARTICLE_TEXT, t)
            article.save()


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
    GROUP_MAPPING = {
        'all': {
            'name': 'Все котики',
            'description': 'Все животные которые попали к нам в приют.',
        },
        'H': {
            'name': 'Пристроены',
            'description': 'Они обрели свой дом',
        },
        'S': {
            'name': 'Ищут дом',
            'description': '_'
        },
        'D': {
            'name': 'На радуге',
            'description': 'Пусть земля им будет пухом, они всегда останутся в наших сердцах.',
        },
    }
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


def get_important_news():
    kwargs = {
        SHOW: True,
        NEWS_IMPORTANT: True,
    }
    # TODO: check if not found
    res = News.objects.filter(**kwargs).order_by('-created').first()
    return res


def get_last_articles(count):
    kwargs = {
        SHOW: True,
    }
    res = Article.objects.filter(**kwargs).exclude(**{'id__in': list(ARTICLES_DEFAULT_MAPPING)}).order_by('?')[:count]
    return res


def get_base_catsekb_context(active_menu, extra_title, project=None):
    project = project or 'main'
    default_group_list = PROJECT_GROUPS_MAPPING[project]

    animal_filter_url = dict()
    animal_filter_url['caption'] = 'Поиск'
    animal_filter_url['url'] = "{url}?{key}=1".format(
        url=reverse('animal_list'),
        key=GET_PAR_KEY_FILTER,
        shelter_key=ANIMAL_LOCATION_STATUS,
    )

    helpful_info_list = list()
    find_cat_url = dict()
    find_cat_url['caption'] = ARTICLES_DEFAULT_MAPPING[ARTICLE_FIND_CAT_ID][CAPTION]
    find_cat_url['url'] = reverse(URL_NAME_FIND_CAT)
    articles = dict()
    articles['caption'] = ARTICLE_VERBOSE_NAME_PLURAL
    articles['url'] = reverse(URL_NAME_SUBJECTS_FEED)
    helpful_info_list.append(find_cat_url)
    # helpful_info_list.append(news)
    helpful_info_list.append(articles)

    context = {
        'group_list': default_group_list + [animal_filter_url],
        'projects_menu_items': default_group_list,  # TODO: убрать костыль
        'helpful_info_list': helpful_info_list,
        'active_menu': active_menu,
        'extra_title': extra_title,
    }
    return context


def filter_animals_query(query):
    res = {key: query[key] for key in query if key in ANIMAL_QUERY_KEYS}
    return res


def get_animals_from_query(query, show_permission=False):
    """

    :rtype: QueryDict
    :type show_permission: bool
    :type query: dict
    """
    query = filter_animals_query(query)
    res = get_objects_from_query(
        model_cls=Animal, query=query, show_permission=show_permission, order_by=ANIMAL_CREATED
    )
    return res


def get_shelter_animals(show_permission, project=None, count=GALLERY_DEFAULT_ITEMS_COUNT):
    query = {ANIMAL_LOCATION_STATUS: 'S'}
    if project is not None:
        query['project'] = project
    shelter_animals = get_animals_from_query(
        query=query, show_permission=show_permission
    ).order_by('?')
    return shelter_animals[:count], len(shelter_animals)


def get_home_animals_count(project=None):
    query = {ANIMAL_LOCATION_STATUS: 'H'}
    if project is not None:
        query['project'] = project
    return get_animals_from_query(
        query, show_permission=True
    ).count()
