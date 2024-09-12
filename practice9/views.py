from django.shortcuts import render
from django.http import HttpRequest
from practice8.models import Book

def get_book_detail(req: HttpRequest, pk: int):
    book = Book.objects.get(id=pk)

    return render(req, 'detail_book.html', {
        "book": book
    })