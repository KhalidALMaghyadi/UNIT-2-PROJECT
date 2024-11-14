from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from project .models import Project 
from blog .models import Blog
# Create your views here.

def dashboard_view(request:HttpRequest):
    context = {}
    
    section = request.GET.get('section', 'projects')  
    
    if section == 'projects':
        context['items'] = Project.objects.all()
        context['section'] = 'projects'
    
    elif section == 'blogs':
        context['items'] = Blog.objects.all()
        context['section'] = 'blogs'
    

    return render(request, 'dashboard/dashboard.html', context)
