
from django.db import models
from customer.models import CustomerTable
from products.models import ProductsTable
# Create your models here.


class cart_table(models.Model):
    customer_id = models.ForeignKey(CustomerTable, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductsTable, on_delete=models.CASCADE)
    cart_id = models.IntegerField(auto_created=True, primary_key=True)
    total_iteams = models.IntegerField()
    total_price = models.IntegerField()
