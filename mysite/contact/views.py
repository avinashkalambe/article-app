from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from .models import Contacts


# Create your views here.
class ContactView(View):
    form_class = ContactForm
    template = 'contactus.html'
    

    def get(self, request, *args, **kargs):
        form = self.form_class()
        return render(request, self.template , {'form': form})


    def post(self, request,*args, **kargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                n_form = form.save(commit= False)
                attachment = request.FILES.get('attachment')
                file = request.FILES.get('file')
                n_form.attachment = attachment
                n_form.file = file
                n_form.save()
            except Exception as e:
                print('Error in saving data', e)
            form = self.form_class()
            return render(request, self.template , {'form': form, 'message': 'Thank you.. We will get back to you..'})
        
        return render(request, self.template , {'form': form})



class ContactDataView(View):
    template = 'messages.html'

    def get(self, request):
        data = Contacts.objects.all()
        return render(request, self.template , {'data': data})

    
class ContactDelete(View):
    template = 'messages.html'
    
    def get(self, request, *args, **kargs):                
        record = Contacts.objects.get(**kargs)
        record.delete()
        data = Contacts.objects.all()
        return render(request, self.template , {'data': data})