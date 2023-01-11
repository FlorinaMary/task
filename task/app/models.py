from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 200)
    category = models.CharField(max_length  = 200)
    price  = models.DecimalField(max_digits = 100, decimal_places=2)
    desc = models.CharField(max_length  = 200)

    def __str__(self):
         return self.title

