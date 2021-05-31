# Generated by Django 3.1.7 on 2021-03-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Table',
            fields=[
                ('customer_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_full_name', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_location', models.CharField(max_length=50)),
                ('customer_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]