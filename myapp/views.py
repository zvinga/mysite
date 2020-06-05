from django.shortcuts import render
from django.http import HttpResponse, FileResponse


# Create your views here.
# function based vieuw

def home(request):
    return FileResponse(open('myapp/1.jpg','rb'))


def about(request):
    return HttpResponse('<h1> about page</h1>')


def contact(request):
    return HttpResponse('<p1> hello i''m joury and yazen </p1>')
