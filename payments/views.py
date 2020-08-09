from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from yandex_checkout import Configuration, Payment
from catsekb.settings import YANDEX_MONEY_ACCOUNT_ID, YANDEX_MONEY_SECRET_KEY
from payments.forms import PaymentForm

Configuration.account_id = YANDEX_MONEY_ACCOUNT_ID
Configuration.secret_key = YANDEX_MONEY_SECRET_KEY


def payment_success_view(request):        
    return render(request, 'payments/payment_success_page.html')

def pay_view(request):    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment.create({
                "amount": {
                    "value": request.POST['amount'],
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": request.build_absolute_uri(reverse('payment_success'))
                },
                "capture": True,
                "description": "Тестовый заказ"
            })
            confirmation_url = payment.confirmation.confirmation_url
            return HttpResponseRedirect(confirmation_url)
    else:
        form = PaymentForm()
    return render(request, 'payments/pay_page.html', {'form': form})
