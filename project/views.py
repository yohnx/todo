from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.

@login_required
def projects(request):
    projects = Project.objects.filter(created_by = request.user)
    return render(request, "project/projects.html", {
        'projects': projects
    })

@login_required
def project(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, "project/project.html", {
        'project': project
    })

@login_required
def add(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    if name:
        Project.objects.create(name=name, description=description, created_by=request.user)
        return redirect("/projects")
    else:
        print("Error occurred")
    return render(request, "project/add.html")

@login_required
def edit(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            project.name = name
            project.description = description
            project.save()

            return redirect('/projects/')
    return render(request, "project/edit.html", {
        'project': project
    })
        
@login_required
def delete(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk=pk)
    project.delete()
    return redirect('/projects/')


