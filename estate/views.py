from django.shortcuts import render
from .models import *

def index(request):
    projects = Projects.objects.all()
    values = value.objects.all()[0:3]
    vlogs = vlog.objects.all()[0:3]
    const = {
        'value':values,
        'vlog':vlogs,
        'projects':projects,
    }
    return render(request,'index.html',const)


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def download(request):
    return render(request,'download.html')


def apointment(request):
    return render(request,'apointment.html')
