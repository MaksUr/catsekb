from django.urls import path
from payments import views

urlpatterns = [
    path('succes/', views.payment_success_view, name='payment_success'),
    path('pay/', views.pay_view, name='pay'),
]
