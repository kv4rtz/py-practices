from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def get_hello(req: HttpRequest):
    return render(req, 'index.html', {
        "title": "Hello"
    })
    
def get_library(req: HttpRequest):
    return render(req, 'library.html', {
        'book': 'Отцы и дети'
    })