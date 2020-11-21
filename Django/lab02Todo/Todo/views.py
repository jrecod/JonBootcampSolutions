from django.shortcuts import render, reverse
from .models import TodoItem
from django.http import HttpResponseRedirect

def index(request):
    todo_items = TodoItem.objects.all()
    context = {
        'todo_items' : todo_items
    }
    return render(request, 'Todo/index.html', context)

def submit(request):
    task = request.POST['task']
    create_todo = TodoItem(task = task)
    create_todo.save()

    return HttpResponseRedirect(reverse('Todo:index'))


# request.POST = {
#     'task': user-input/input-value
#     'title': user-input/input-value
#     'urgency': user-input/input-value
# }

# request.POST['task'] = user-input
# request.POST['title'] = user-value