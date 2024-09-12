from django.urls import path
from .views import get_home, get_about, get_products, get_product_detail

urlpatterns = [
    path('', get_home, name='home'),
    path('about/', get_about, name='about'),
    path('products/', get_products, name='products'),
    path('products/<int:pk>', get_product_detail, name='detail_product'),
]

