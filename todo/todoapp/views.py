from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import Todo
# Create your views here.
def homepage(request):
    todos = Todo.objects.all()
    return render(request, 'index1.html', {'todos':todos})

    # Сохранение данных в БД

def create(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')