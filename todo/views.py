from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse



from .models import ToDo


# Create your views here.
class IndexView(generic.ListView):
    model = ToDo
    template_name = 'todo/index.html'

def new(request):
    if 'description' in request.POST:
        
        todo = ToDo()
        todo.due_date = request.POST['date']
        todo.description = request.POST['description']
        todo.percent = request.POST['percentdone']
        todo.save()
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('todo:index'))
        
    else:
        return render(request, 'todo/new.html')


def edit(request, pk): 
    if request.method == 'POST':

        todo = ToDo.objects.get(id=pk)
        todo.due_date = request.POST['date']
        todo.description = request.POST['description']
        todo.percent = request.POST['percentdone']
        todo.save()

        return HttpResponseRedirect(reverse('todo:index'))
            
    else:  
        todo = ToDo.objects.get(id=pk)
        context = {
            'due_date': todo.due_date,
            'description':todo.description,
            'percent':todo.percent, #or percentdone?!
            'todo.id':pk
        }  
        return render(request, 'todo/edit.html', context) #HttpResponseRedirect(reverse('todo:edit')) #HttpResponse('could not find todo for this id') 

def imprint(request):
    return render(request, 'todo/imprint.html')


