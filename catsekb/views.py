from constance import config
from django.shortcuts import render, get_object_or_404

from articles.models import Partner, PartnerEvent
from cats.models import AnimalVideo
from catsekb.view_functions import get_important_news, PROJECT_MENU_ITEMS_CONTEXT


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
        'active_menu': 'about',
        'extra_title': 'О проекте',
        'caption': 'О проекте',
        'object': config.ABOUT_PAGE_CONTENT,
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request, 'catsekb/about.html',
        context=context
    )


def partners_view(request):
    context = {
        'active_menu': 'partners',
        'extra_title': 'Наши партнеры',
        'caption': 'Наши партнеры',
        'object_list': Partner.objects.all().order_by('name'),
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request, 'catsekb/partners.html',
        context=context
    )


def partner_detail_view(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    context = {
        'active_menu': 'partners',
        'extra_title': partner.name,
        'caption': 'Наши партнеры',
        'object': partner,
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request, 'catsekb/partner_detail_view.html',
        context=context
    )


def partner_event_detail_view(request, pk):
    partner_event = get_object_or_404(PartnerEvent, pk=pk)
    context = {
        'active_menu': 'partners',
        'extra_title': partner_event.title,
        'caption': 'Наши партнеры',
        'object': partner_event,
        'projects_menu_items': PROJECT_MENU_ITEMS_CONTEXT,
    }
    return render(
        request, 'catsekb/partner_event_detail_view.html',
        context=context
    )
