from django.shortcuts import render
from django.urls import reverse_lazy
from constance import config
from catsekb.view_functions import get_important_news
from cats.models import AnimalVideo

PROJECT_MENU_ITEMS_CONTEXT = [
    {'caption': 'CatsEkb', 'url': reverse_lazy('catsekb_page')},
    {'caption': 'HuskyEkb', 'url': reverse_lazy('huskyekb_page')},
    {'caption': 'Rotvodom', 'url': '#'},
]


def index_view(request):
    context = {
        'active_menu': 'index',
        'extra_title': 'Главная страница',
        'important_news': get_important_news(),
        'main_video': AnimalVideo.objects.order_by('-created').filter(put_to_index_page=True),
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request, 'catsekb/index.html',
        context=context
    )


def contacts_view(request):
    context = {
        'active_menu': 'contacts',
        'extra_title': 'Контакты',
        'object': config.CONTACTS_PAGE_CONTENT,
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request,
        'catsekb/contacts.html',
        context=context
    )


def help_us_view(request):
    context = {
        'active_menu': 'help_us',
        'extra_title': 'Помощь приюту',
        'caption': 'Помощь приюту',
        'object': config.HELP_US_PAGE_CONTENT,
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request, 'catsekb/help_us.html',
        context=context
    )


def about_view(request):
    context = {
        # 'active_menu': 'help_us',
        'extra_title': 'О проекте',
        'caption': 'О проекте',
        'object': config.ABOUT_PAGE_CONTENT,
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request, 'catsekb/about.html',
        context=context
    )
