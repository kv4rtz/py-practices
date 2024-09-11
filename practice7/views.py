from django.http import HttpRequest
from django.shortcuts import render
from .models import Product

def get_home(req: HttpRequest):
    return render(req, 'p7_home.html')

def get_about(req: HttpRequest):
    return render(req, 'p7_about.html')

def get_products(req: HttpRequest):
    products = Product.objects.all()
    
    return render(req, 'p7_products.html', {
        "products": products
    })