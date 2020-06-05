from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse


# Create your views here.
# function based vieuw

def home(request):
    return FileResponse(open('myapp/1.jpg','rb'))


def about(request):
    return HttpResponse('<h1> about page</h1>')


def contact(request):
    return HttpResponse('<p1> hello i''m joury and yazen </p1>')

def what_is_my_ip(request):
    return JsonResponse({'ip':'123456789'})
