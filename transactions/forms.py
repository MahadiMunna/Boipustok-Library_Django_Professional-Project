from django import forms
from .models import Transaction

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
        ]
    def clean_amount(self):
        min_deposit_amount = 100
        max_deposit_amount = 100000
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        elif amount > max_deposit_amount:
            raise forms.ValidationError(
                f'You are able to deposit maximum {max_deposit_amount} $'
            )

        return amount
