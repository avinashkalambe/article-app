from django.db import models


# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    phone = models.CharField(blank=True, max_length=12 )
    attachment = models.ImageField(upload_to= 'images/', blank=True, null= True)
    file = models.FileField(upload_to='docs/', blank=True, null=True )

    def __str__(self) :
        return self.name
