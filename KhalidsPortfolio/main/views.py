from django.shortcuts import render,redirect

from django.http import HttpRequest , HttpResponse
from blog.models import Blog
# Create your views here.


def home_view(request:HttpRequest):
    blogs = Blog.objects.all()[:2] 
    
    return render (request , 'main/home.html' , {'blogs': blogs})   