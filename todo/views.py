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
    
    
    

"""
    try:
        
    except (KeyError, Description.DoesNotExist):
        return render(request, 'todo/new.html')
    else:
        return HttpResponse('test')
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
"""
    
    

def edit(request):
    return render(request, 'todo/edit.html')

def imprint(request):
    return render(request, 'todo/imprint.html')
