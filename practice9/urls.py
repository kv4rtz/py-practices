from django.urls import path
from .views import get_book_detail

urlpatterns = [
    path('book/<int:pk>/', get_book_detail, name='book_detail'),
]

