from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hi_view(request):
    return HttpResponse("Hi from Django!")