from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# function based vieuw

def home(request):
    return HttpResponse('Hello home')
