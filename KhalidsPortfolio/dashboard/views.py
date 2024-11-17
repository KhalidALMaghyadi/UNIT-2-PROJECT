from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from project .models import Project 
from blog .models import Blog
from contact.models import ContactMessage
# Create your views here.

def dashboard_view(request:HttpRequest):
    
    section = request.GET.get('section', 'projects')
    search_query = request.GET.get('search', '')  # Get the search query (if any)
    context = {'section': section, 'search_query': search_query}

    if section == 'projects':
        items = Project.objects.all()
        if search_query:
            items = items.filter(title__icontains=search_query)
        context['items'] = items

    elif section == 'blogs':
        items = Blog.objects.all()
        if search_query:
            items = items.filter(title__icontains=search_query)
        context['items'] = items

    elif section == 'contacts':
        items = ContactMessage.objects.all()
        if search_query:
            items = items.filter(name__icontains=search_query)
        context['items'] = items
    

    return render(request, 'dashboard/dashboard.html', context)
