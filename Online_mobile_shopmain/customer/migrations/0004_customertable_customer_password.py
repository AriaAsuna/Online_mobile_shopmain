# Generated by Django 3.1.7 on 2021-03-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210325_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertable',
            name='customer_password',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
