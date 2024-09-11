from django.urls import path
from .views import get_home, get_about, get_products

urlpatterns = [
    path('', get_home),
    path('about/', get_about),
    path('products/', get_products)
]

