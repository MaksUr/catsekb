"""catsekb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from articles.views import NewsFeedListView, AnimalVideoListView
from catsekb import settings
from catsekb.views import index_view, contacts_view, help_us_view

urlpatterns = [
    path('', include('articles.urls')),
    path('', index_view, name='index'),
    path('contacts/', contacts_view, name='contacts'),
    path('help_us/', help_us_view, name='help_us'),
    path('catsekb/', include('catsekb_page.urls')),
    path('huskyekb/', include('huskyekb_page.urls')),
    path('rotvodom/', include('rotvodom_page.urls')),
    path('pets/', include('cats.urls')),
    path('admin/', admin.site.urls),
] + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
