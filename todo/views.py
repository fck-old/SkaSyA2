from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'todo/index.html')

def new(request):
    return render(request, 'todo/new.html')

def edit(request):
    return render(request, 'todo/edit.html')

def imprint(request):
    return render(request, 'todo/imprint.html')
