from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'fully functional ecommerce website'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'fully functional ecommerce website'
    }
]


def projects(request):
    page = "Projects"
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'project/projects.html', context)


def project(request, pk):
    projectobj = None
    for i in projectsList:
        if i['id'] == pk:
            projectobj = i
    return render(request, 'project/single-project.html', {'project': projectobj})