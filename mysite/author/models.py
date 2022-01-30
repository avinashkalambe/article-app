from django.db import models
from django.urls import reverse
# Create your models here.
class Author(models.Model):    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def get_absolute_url(self):
        return reverse('author_create')


    def __str__(self):
        return self.name