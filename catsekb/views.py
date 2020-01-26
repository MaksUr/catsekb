from django.shortcuts import render
from django.urls import reverse_lazy
from constance import config
from catsekb.view_functions import get_important_news

PROJECT_MENU_ITEMS_CONTEXT = {
    'projects_menu_items': [
        {'caption': 'CatsEkb', 'url': reverse_lazy('catsekb_page')},
        {'caption': 'HaskyEkb', 'url': '#'},
        {'caption': 'Rotvodom', 'url': '#'},
    ]
}

def index_view(request):
    context={
        'active_menu': 'index',
        'extra_title': 'Главная страница',
        'important_news': get_important_news(),
    }
    context.update(PROJECT_MENU_ITEMS_CONTEXT)
    return render(
        request, 'catsekb/index.html',
        context=context
    )

def contacts_view(request):
    context={
        'active_menu': 'contacts',
        'extra_title': 'Контакты',
        'object': config.CONTACTS_PAGE_CONTENT
    }
    context.update(PROJECT_MENU_ITEMS_CONTEXT)
    return render(
        request, 
        'catsekb/contacts.html', 
        context=context
    )

def help_us_view(request):
    context={
        'active_menu': 'help_us',
        'extra_title': 'Помощь приюту',
        'object': config.HELP_US_PAGE_CONTENT,
    }
    context.update(PROJECT_MENU_ITEMS_CONTEXT)
    return render(
        request, 'catsekb/help_us.html', 
        context=context
    )
