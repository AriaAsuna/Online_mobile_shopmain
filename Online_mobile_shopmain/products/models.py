from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


class ProductsTable(models.Model):
    product_name = models.CharField(max_length=50)
    product_intro = models.TextField()
    product_id = models.IntegerField(auto_created=True, primary_key=True)
    product_details = models.TextField()
    product_price = models.IntegerField()
    product_release_date = models.DateTimeField()
    image = models.ImageField(upload_to="img/")
    product_link = EmbedVideoField()

    def __str__(self):
        return self.product_name
