from django import forms
from User.models import Player

class SignUpFOrm(forms.Form):
    username =  forms.CharField(max_length=65)
    first_name = forms.CharField(max_length=56)
    last_name= forms.CharField(max_length=665)
    email = forms.EmailField(help_text='required')
    phone = forms.CharField(help_text="optional")
    country = forms.CharField(help_text='optional')
    city = forms.CharField(help_text='optional')


    class Meta:
        model = Player
        fields = (
            'username', 'first_name', 'last_name', 'email', 'phone', 'country',  'city', 'team_id')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
