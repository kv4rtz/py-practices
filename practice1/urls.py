from django.http import HttpResponse
from django.urls import path
from .views import get_privet

urlpatterns = [
    path('', lambda req: HttpResponse("Hello World")),
    path('privet/', get_privet)
]
