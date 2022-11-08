from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Project, Review, Tag
from .form import ProjectForm
# Create your views here.



def projects(request):
    projects=Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project/projects.html', context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    print('projectobj: ', projectobj)
    print("tags: ", tags)
    return render(request, 'project/single-project.html', {'project': projectobj, 'tags': tags})


def createProject(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect("projects")
        
    
    context = {"form": form}
    return render(request, 'project/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return  redirect("projects")
        
    
    context = {"form": form}
    return render(request, 'project/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    
    context = {'object': project}
    return render(request, "project/delete_template.html", context)