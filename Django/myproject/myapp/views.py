from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel
def index(request):
    blog_posts = MyModel.objects.order_by('-date_published')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'myapp/index.html', context)
# Create your views here.

# def index(request):
#     return HttpResponse('hello world!')