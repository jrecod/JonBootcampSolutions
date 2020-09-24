from django.shortcuts import render
from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.all()
    context = {
        'todo_items' : todo_items
    }
    return render(request, 'Todo/index.html', context)
# Create your views here.
