from django.shortcuts import render,redirect

from django.http import HttpRequest , HttpResponse
from blog.models import Blog
# Create your views here.


def home_view(request:HttpRequest):
    
    return render (request , 'main/home.html')   


def about_me_view(request:HttpRequest):
    return render (request , 'main/about_me.html')


def resume_view(request:HttpRequest):
    return render (request , 'main/resume.html')