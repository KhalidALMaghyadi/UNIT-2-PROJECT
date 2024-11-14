from django.shortcuts import render,redirect
from django.http import  HttpRequest , HttpResponse 
from .models import Project

# Create your views here.

def new_add_view(request : HttpRequest):
    
    if request.method == "POST":
        new_data = Project(title=request.POST["title"],
                            description=request.POST["description"],
                            technology_use=request.POST["technology_use"], 
                            status=request.POST["status"],
                            image=request.FILES["image"],
                            date_created=request.POST["date_created"]
                        ) 
        new_data.save()
    return render(request,'project/new_project.html') 

def all_project_view(request : HttpRequest):
    projects = Project.objects.all()

    return render(request, 'project/all_projects.html', {'projects': projects})


def detail_project_view(request : HttpRequest , project_id):
   
    project= Project.objects.get(pk=project_id)

    return render(request, 'project/detail_project.html', {'project': project})




def update_project_view(request : HttpRequest ,project_id):

    project = Project.objects.get(pk=project_id)
    
    if request.method == "POST":
        
        project.title = request.POST.get("title")
        project.description = request.POST.get("description")
        project.status = request.POST.get("status")
        project.technology_use = request.POST.get("technology_use")
        project.date_created = request.POST.get("date_created")
        
        
        if 'image' in request.FILES:
            project.image = request.FILES["image"]

        
        project.save()
        return redirect('project:detail_project_view', project_id=project.id)
    return render (request , 'project/update_project.html', {"project":project})


# راح ارجعلها 
def delete_project_view(request: HttpRequest,project_id):
    
    project= Project.objects.get(pk=project_id)

    project.delete()

    return redirect('dashboard:dashboard_view')
