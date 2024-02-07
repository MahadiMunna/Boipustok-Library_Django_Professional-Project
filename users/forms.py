from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','gender', 'street_address','city','postal_code', 'country','password1', 'password2' ]
    
    def save(self, commit=True):
        account_user = super().save(commit=False)
        if commit == True:
            account_user.save()
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
        
        UserAccount.objects.create(
            user = account_user,
            gender = gender,
            street_address = street_address,
            city = city,
            postal_code = postal_code,
            country = country,
        )
    
        return account_user

class EditProfile(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['gender'].initial = user_account.gender
                self.fields['street_address'].initial = user_account.street_address
                self.fields['city'].initial = user_account.city
                self.fields['postal_code'].initial = user_account.postal_code
                self.fields['country'].initial = user_account.country
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserAccount.objects.get_or_create(user=user)

            user_account.gender = self.cleaned_data['gender']
            user_account.street_address = self.cleaned_data['street_address']
            user_account.city = self.cleaned_data['city']
            user_account.postal_code = self.cleaned_data['postal_code']
            user_account.country = self.cleaned_data['country']
            
            user_account.save()

        return user