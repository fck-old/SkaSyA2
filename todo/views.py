from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ToDo

class IndexView(generic.ListView):
    model = ToDo
    template_name = 'todo/index.html'
    ordering = ['-pk']

def new(request):
    if request.method == 'POST':
        todo = ToDo()
        todo.due_date = request.POST['date']
        todo.description = request.POST['description']
        todo.percent = request.POST['percentdone']
        try:
            if todo.description == '':
                raise Exception('empty')
            todo.save()
        except:
            context = {
                'due_date': request.POST['date'],
                'description': request.POST['description'],
                'percent': request.POST['percentdone'],
                'error': True
            }
            return render(request, 'todo/new.html', context)
        else:
            return HttpResponseRedirect(reverse('todo:index'))
    else:
        return render(request, 'todo/new.html')


def edit(request, pk): 
    if request.method == 'POST':
        todo = get_object_or_404(ToDo, id=pk)
        todo.due_date = request.POST['date']
        todo.description = request.POST['description']
        todo.percent = request.POST['percentdone']
        try:
            if todo.description == '':
                raise Exception('empty')
            todo.save()
        except:
            context = {
                'due_date': request.POST['date'],
                'description': request.POST['description'],
                'percent': request.POST['percentdone'],
                'error': True
            }
            return render(request, 'todo/edit.html', context)
        else:
            return HttpResponseRedirect(reverse('todo:index'))

    else:  
        todo = get_object_or_404(ToDo, id=pk)
        return render(request, 'todo/edit.html', todo.__dict__)


def delete(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(ToDo, id=pk)
        todo.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def imprint(request):
    return render(request, 'todo/imprint.html')
