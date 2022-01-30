from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404

from mysite.settings import MEDIA_ROOT
from .models import Article
from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import MEDIA_URL
from .models import RegisterForm

# Create your views here.

def home(request):
    records = Article.objects.all()
    return render(request, 'home.html',{'records':records})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def article_details(request, pk):
    record = Article.objects.get(id=pk)
    return render(request, 'show_article.html', {'record':record})


def article_update(request, pk):
    if request.method == 'POST':        
        name = request.POST.get('ar_name')
        body = request.POST.get('ar_body')
        image = request.FILES['ar_image']
        fss = FileSystemStorage()
        print(fss.base_location)
        file = fss.save(image.name, image)
        file_url = fss.url(file)
        print(file_url)

        record = Article.objects.get(id=pk)
        record.name = name
        record.body = body
        record.image = file_url
        record.save()
        return render(request, 'update.html', {'record':record, 'message':'Records update successfully..'})
    else:    
        record = Article.objects.get(id=pk)
        fm = RegisterForm()
        return render(request, 'update.html', {'record':record,'form':fm})


def article_delete(request, pk):
    record = Article.objects.get(id=pk)
    record.delete()
    return redirect('home')


