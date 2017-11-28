from django.shortcuts import render


def contact_view(request):
    context = dict()
    return render(request, 'catsekb/contact.html', context)


def info_view(request):
    context = dict()
    return render(request, 'catsekb/info.html', context)
