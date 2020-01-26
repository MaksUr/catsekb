from django.shortcuts import render
from constance import config
from catsekb.view_functions import get_important_news


def index_view(request):
    return render(
        request, 'catsekb/index.html',
        context={
            'active_menu': 'index',
            'extra_title': 'Главная страница',
            'important_news': get_important_news(),
        }
    )

def contacts_view(request):
    return render(
        request, 
        'catsekb/contacts.html', 
        context={
            'active_menu': 'contacts',
            'extra_title': 'Контакты',
            'objects': config.CONTACTS_PAGE_CONTENT
        }
    )

def help_us_view(request):
    return render(
        request, 'catsekb/help_us.html', 
        context={
            'active_menu': 'help_us',
            'extra_title': 'Помощь приюту',
            'object': config.HELP_US_PAGE_CONTENT,
            
        }
    )
