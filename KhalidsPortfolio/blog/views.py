from django.shortcuts import render,redirect 
from django.http import  HttpRequest , HttpResponse 
from . models import Blog

# Create your views here.
def new_blog_view(request : HttpRequest):
    if request.method == "POST":
        new_data = Blog(title=request.POST["title"],
                                content =request.POST["content"],
                                published_date =request.POST["published_date"], 
                                featured_image =request.FILES["featured_image"], 
                            ) 
        new_data.save()
    return render(request,'blog/new_blog.html') 

def all_blogs_view(request : HttpRequest):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs}) 

def blog_detail_view(request : HttpRequest , blog_id):
    
    blog = Blog.objects.get(pk=blog_id)
    related_blogs = Blog.objects.all()[:4]  
    context = {
        'blog': blog,
        'related_blogs': related_blogs,
    }
    return render(request, 'blog/blog_detail.html', context)
    # return render(request, 'blog/blog_detail.html', {'blog': blog})

     

def update_blog_view(request : HttpRequest , blog_id) :
    blog = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST.get("title")
        blog.content = request.POST.get("content")
        if 'featured_image' in request.FILES:
            blog.featured_image = request.FILES['featured_image']
        
        blog.save()
        return redirect('blog:blog_detail_view', blog_id=blog.id)

    return render(request, 'blog/update_blog.html', {'blog': blog})
 
def delete_blog_view(request : HttpRequest , blog_id):
     
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    return redirect('dashboard:dashboard_view')
