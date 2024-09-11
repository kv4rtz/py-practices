from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from practice4.models import Book

def get_info(req: HttpRequest):
    book = Book.objects.get(id=1)
    
    return render(req, 'base.html', {
        'book': book
    })
    
def get_author(req: HttpRequest):
    book_author = Book.objects.filter(author__name='А. С. Пушкин')
    
    return render(req, 'author.html', {
        'book_author': book_author
    })
    
def get_anything_author(req: HttpRequest):
    book_author = Book.objects.filter(author__name='Н. В. Гоголь')
    
    return render(req, 'author.html', {
        'anything_author': book_author
    })
    
def get_publisher(req: HttpRequest):
    book_publisher = Book.objects.filter(publishers__name='Просвящение')
    
    return render(req, 'publisher.html', {
        "book": book_publisher
    })