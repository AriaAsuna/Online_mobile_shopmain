from django.db import models

# Create your models here.


class CustomerTable(models.Model):
    customer_full_name = models.CharField(max_length=100)
    customer_password = models.TextField()
    customer_id = models.IntegerField(auto_created=True, primary_key=True)
    customer_email = models.EmailField()
    customer_date = models.DateField(auto_now_add=True)

