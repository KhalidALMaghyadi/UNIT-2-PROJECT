from django.shortcuts import render,redirect 
from django.http import  HttpRequest , HttpResponse 
from . models import Blog

# Create your views here.
def new_blog_view(request : HttpRequest):
    new_data = Blog(title=request.POST["title"],
                            content =request.POST["content "],
                            published_date =request.POST["published_date "], 
                            featured_image =request.FILES["featured_image "], 
                        ) 
    new_data.save()
    return render(request,'blog/new_project.html') 

def all_blogs_view(request : HttpRequest):
    pass 

def blog_detail_view(request : HttpRequest , blog_id):
    pass 

def update_blog_view(request : HttpRequest , blog_id) :
    pass 

def delete_blog_view(request : HttpRequest , blog_id):
    pass 