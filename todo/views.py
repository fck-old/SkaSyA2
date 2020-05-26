from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import ToDo


# Create your views here.
class IndexView(generic.ListView):
    model = ToDo
    template_name = 'todo/index.html'

def new(request):
    return render(request, 'todo/new.html')

def edit(request):
    return render(request, 'todo/edit.html')

def imprint(request):
    return render(request, 'todo/imprint.html')
