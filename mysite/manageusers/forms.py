from django import forms
from django.core.exceptions import ValidationError

initials_choices =(
    ("1", "Mr"),
    ("2", "Mrs"),
    ("3", "Ms")
)

def validate_phone(value):    

    if value.isnumeric() == False:
        raise forms.ValidationError('please enter only numbers')


class Register(forms.Form):
    initials = forms.ChoiceField(choices = initials_choices)
    name = forms.CharField(max_length=100, label='Name')
    password = forms.CharField(max_length=30, widget = forms.PasswordInput, label='Password')
    matchpassword = forms.CharField(max_length=30, widget = forms.PasswordInput, label='Match password')
    email = forms.EmailField(max_length=50, label='Email')
    phone = forms.CharField(max_length=10,validators=[validate_phone], label='Phone')



    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        matchpass = cleaned_data.get('matchpassword')
        print(password)
        print(matchpass)

        if password and matchpass :
            if password != matchpass:
                raise ValidationError('Both passwords should match')


class Login(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
