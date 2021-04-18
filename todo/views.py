from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def todo_lists(request):
    todos = Todo.objects.all()
    context = {
        "todo_lists": todos
    }
    # return HttpResponse("Hello world!")
    # return render(request, 'todo/todo_lists.html')
    return render(request, 'todo/todo_lists.html', context)