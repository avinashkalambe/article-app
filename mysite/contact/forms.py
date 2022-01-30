from .models import Contacts
from django.forms import ModelForm, ValidationError


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'


    def clean_phone(self):
        cleaned_data = super().clean()
        f_phone = cleaned_data.get('phone')
        print('inside phone clean')
        if f_phone.isnumeric() == False :
            raise ValidationError('all chars should be numbers')

        return f_phone
