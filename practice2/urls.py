from django.http import HttpResponse
from django.urls import path
from .views import get_hello, get_library

urlpatterns = [
    path('', get_hello),
    path('library/library', get_library)
]

