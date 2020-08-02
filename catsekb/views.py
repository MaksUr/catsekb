from constance import config
from django.shortcuts import render, get_object_or_404

from articles.models import Partner, PartnerEvent
from cats.models import AnimalVideo, Animal
from catsekb.view_functions import get_important_news, OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT, \
    ABOUT_MENU_ITEMS_BASE_CONTEXT


def index_view(request):
    context = {
        'active_menu': 'index',
        'extra_title': 'Главная страница',
        'important_news': get_important_news(),
        'main_video': AnimalVideo.objects.order_by('-created').filter(put_to_index_page=True),
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
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
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
    }
    return render(
        request,
        'catsekb/contacts.html',
        context=context
    )


def help_view(request):
    context = {
        'active_menu': 'help',
        'extra_title': 'Помощь приюту',
        'caption': 'Помощь приюту',
        'object': config.HELP_PAGE_CONTENT,
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
    }
    return render(
        request, 'catsekb/help.html',
        context=context
    )


def about_view(request):
    name = 'О фонде'
    context = {
        'active_menu': 'about',
        'extra_title': name,
        'caption': name,
        'object': config.ABOUT_PAGE_CONTENT,
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
    }
    return render(
        request, 'catsekb/about.html',
        context=context
    )


def documents_view(request):
    name = 'Документы'
    context = {
        'active_menu': 'about',
        'extra_title': name,
        'caption': name,
        'object': config.DOCUMENTS_PAGE_CONTENT,
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
    }
    return render(
        request, 'catsekb/documents.html',
        context=context
    )


def reports_view(request):
        name = 'Отчетность'
        context = {
            'active_menu': 'about',
            'extra_title': name,
            'caption': name,
            'object': config.REPORTS_PAGE_CONTENT,
            'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
            'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
        }
        return render(
            request, 'catsekb/reports.html',
            context=context
        )


def media_view(request):
    name = 'Сми о нас'
    context = {
        'active_menu': 'about',
        'extra_title': name,
        'caption': name,
        'object': config.MEDIA_PAGE_CONTENT,
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
    }
    return render(
        request, 'catsekb/media.html',
        context=context
    )


def partners_view(request):
    name = 'Наши партнеры'
    context = {
        'active_menu': 'partners',
        'extra_title': name,
        'caption': name,
        'object_list': Partner.objects.all().order_by('name'),
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
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
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
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
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
    }
    return render(
        request, 'catsekb/partner_event_detail_view.html',
        context=context
    )


def get_animal_guide_view(request):
    name = 'Взять животное из приюта'
    context = {
        'active_menu': 'our_animals',
        'extra_title': name,
        'caption': name,
        'object': config.GET_ANIMAL_GUIDE_PAGE_CONTENT,
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
    }
    return render(
        request, 'catsekb/get_animal_guide.html',
        context=context
    )


def new_animals_view(request):
    name = 'Новенькие'
    context = {
        'active_menu': 'our_animals',
        'extra_title': name,
        'caption': name,
        'about_menu_items': ABOUT_MENU_ITEMS_BASE_CONTEXT,
        'our_animals_menu_items': OUR_ANIMALS_MENU_ITEMS_BASE_CONTEXT,
        'new_animals': Animal.objects.filter(location_status='S', vk_album_id__isnull=False).order_by('-created')
    }
    return render(
        request, 'catsekb/new_animals.html',
        context=context
    )
