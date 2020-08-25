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

from catsekb import settings
from catsekb import views
from cats.views import AnimalDetailView
from articles.views import NewsFeedListView, ResultsFeedListView

urlpatterns = [
    path('', include('articles.urls')),
    path('', views.index_view, name='index'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('help/', views.help_view, name='help'),
    path('about/', views.about_view, name='about'),
    path('documents/', views.documents_view, name='documents'),
    path('reports/', views.reports_view, name='reports'),
    path('help/sms/', views.sms_help_view, name='sms_help'),
    path('media/', views.media_view, name='media'),
    path('results/', ResultsFeedListView.as_view(), name='results'),
    path('needs/', views.needs_view, name='needs'),
    path('plans/', views.plans_view, name='plans'),
    path('partners/', views.partners_view, name='partners'),
    path('news/', NewsFeedListView.as_view(), name='news'),
    path('partners/<int:pk>', views.partner_detail_view, name='partner_detail'),
    path('event/<int:pk>', views.partner_event_detail_view, name='partner_event_detail'),
    path('get-animal-guide/', views.get_animal_guide_view, name='get_animal_guide'),
    path('new-animals/', views.new_animals_view, name='new_animals'),
    path('catsekb/', include('catsekb_page.urls')),
    path('huskyekb/', include('huskyekb_page.urls')),
    path('rotvodom/', include('rotvodom_page.urls')),
    path('payments/', include('payments.urls')),
    path('pets/', include('cats.urls')),
    path('admin/', admin.site.urls),
    path('<project:project>/pets/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),  #  TODO: сделать нормально
] + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
