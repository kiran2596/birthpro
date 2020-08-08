from django.db import models
from django.urls import reverse

# Create your models here.

class Birthwish(models.Model):
    name = models.CharField(max_length=256,unique=True)
    message = models.CharField(max_length=256)
    images = models.ImageField(upload_to='pic',blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("birthday:viewlist")





