from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from project .models import Project 
from blog .models import Blog
from contact.models import ContactMessage
# Create your views here.

def dashboard_view(request:HttpRequest):
    # context = {}

    # section = request.GET.get('section', 'projects')
    # context['section'] = section

    # # Get the search query from the request
    # search_query = request.GET.get('search', '')
    # context['search_query'] = search_query

    # # Check if 'search' parameter exists and has at least 2 characters
    # if 'search' in request.GET and len(search_query) >= 2:
    #     if section == 'projects':
    #         # Filter projects based on the search query in the title
    #         items = Project.objects.filter(title__icontains=search_query)
       
    #     elif section == 'blogs':
    #         # Filter blogs based on the search query in the title
    #         items = Blog.objects.filter(title__icontains=search_query)
       
    #     elif section == 'contacts':
    #         context['items'] = ContactMessage.objects.all()
       
    #     else:
    #         items = []
   
    # else:
    #     # If no valid search query, return all items or an empty list
    #     if section == 'projects':
    #         items = Project.objects.all()
    #     elif section == 'blogs':
    #         items = Blog.objects.all()
    #     else:
    #         items = []

    # # Add items to the context
    # context['items'] = items

    section = request.GET.get('section', 'projects')
    search_query = request.GET.get('search', '')  # Get the search query (if any)
    context = {'section': section, 'search_query': search_query}

    if section == 'projects':
        items = Project.objects.all()
        if search_query:
            items = items.filter(title__icontains=search_query)
        context['items'] = items

    # Handle Blogs Section
    elif section == 'blogs':
        items = Blog.objects.all()
        if search_query:
            items = items.filter(title__icontains=search_query)
        context['items'] = items

    # Handle Contacts Section
    elif section == 'contacts':
        items = ContactMessage.objects.all()
        if search_query:
            items = items.filter(name__icontains=search_query)
        context['items'] = items
    

    return render(request, 'dashboard/dashboard.html', context)
