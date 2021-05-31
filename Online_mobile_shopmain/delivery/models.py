from django.db import models
from products.models import ProductsTable


# Create your models here.

class Delivery(models.Model):
    product_id = models.ForeignKey(ProductsTable, on_delete=models.CASCADE)
    delivery_id = models.IntegerField(auto_created=True, primary_key=True)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    time = models.DateTimeField()
