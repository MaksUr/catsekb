from django.shortcuts import render
from constance import config


def index_view(request):
    return render(request, 'catsekb/index.html', context={'active_menu': 'index'})

def contacts_view(request):
    return render(request, 'catsekb/contacts.html', context={'active_menu': 'contacts', 'objects': config.CONTACTS_PAGE_CONTENT})

def help_us_view(request):
    return render(request, 'catsekb/help_us.html', context={'active_menu': 'help_us', 'object': config.HELP_US_PAGE_CONTENT })
