from django.http import HttpResponse
from django.urls import path
from .views import get_info, get_author, get_anything_author, get_publisher

urlpatterns = [
    path('', get_info),
    path('author/', get_author),
    path('anything/author', get_anything_author),
    path('publisher/', get_publisher)
]

