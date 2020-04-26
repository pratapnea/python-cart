from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    published_date = models.DateField()

