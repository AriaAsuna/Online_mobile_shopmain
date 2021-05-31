from django.db import models

# Create your models here.


class EmployeesTable(models.Model):
    employee_full_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(auto_created=True, primary_key=True)
    employee_email = models.CharField(max_length=50)
    employee_address = models.CharField(max_length=50)
    Join_date = models.DateField()
