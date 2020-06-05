
from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('contact/', views.contact)
]
