from django import forms

class PaymentForm(forms.Form):
    amount = forms.IntegerField(label='Сумма платежа', min_value = 1)
