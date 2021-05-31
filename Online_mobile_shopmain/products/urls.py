from django.urls import path
from . import views
from .views import video


urlpatterns = [
    path('', video),

    path('product/', views.product, name='product'),
    path('search/', views.search, name='search'),
]

