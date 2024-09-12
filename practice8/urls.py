from django.urls import path
from .views import get_books
from django.http import HttpResponse

urlpatterns = [
    path('', get_books),
    path('test/', lambda req: HttpResponse("test"), name='test')
]

