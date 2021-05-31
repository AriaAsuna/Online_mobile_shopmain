from django.contrib import admin
from .models import ProductsTable
from embed_video.admin import AdminVideoMixin


# Register your models here.

class video(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(ProductsTable, video)
