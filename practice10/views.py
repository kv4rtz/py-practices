from django.shortcuts import render, redirect
from django.http import HttpRequest
from practice7.models import Product
from django.db.models import Q

def search_product(req: HttpRequest):
    if (req.method == 'GET'):
        search = req.GET['search']
        products = Product.objects.filter(Q(title__icontains=search) | Q(price__icontains=search))

        return render(req, 'p7_products.html', {
            'products': products
        })
    
    return redirect('home')
