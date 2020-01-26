from django.urls import path, include
from huskyekb_page.views import huskyekb_page_view

urlpatterns = [
    path('', huskyekb_page_view, name='huskyekb_page'),
]
