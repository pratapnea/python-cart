from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=60, default="")
    subcategory = models.CharField(max_length=60, default="")
    price = models.IntegerField(default=0.0)
    description = models.CharField(max_length=300)
    published_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.name
