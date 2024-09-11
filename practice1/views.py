from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def get_privet(req):
    return HttpResponse('Привет')