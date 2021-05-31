from django.db import models
from customer.models import CustomerTable
# Create your models here.

class Payment(models.Model):
    payment_id = models.IntegerField(auto_created=True, primary_key=True)
    customer_id =models.ForeignKey(CustomerTable, on_delete=models.CASCADE)
