from django.shortcuts import render
from django.http import HttpRequest
from .models import Book

def get_books(req: HttpRequest):
    books = Book.objects.all()

    return render(req, 'books.html', {
        "books": books
    })