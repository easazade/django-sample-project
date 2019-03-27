from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def home(request: HttpRequest):
    return render(request, 'jobs/home.html')


def some(request: HttpRequest):
    return HttpResponse()
