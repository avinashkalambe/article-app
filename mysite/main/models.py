from ast import mod
from asyncio.windows_events import NULL
from dataclasses import fields
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):

    name = models.CharField(max_length=30)
    body = models.TextField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self) :
        return self.name


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']


