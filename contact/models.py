from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    query = models.CharField(max_length=600)