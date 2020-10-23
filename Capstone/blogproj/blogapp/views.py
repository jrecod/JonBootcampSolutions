from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import BlogPost, Category
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    categories = Category.objects.all()
    for category in categories:
        print(category.id)
    print(categories)
    context = {
        'categories': categories
    }
    return render(request, 'blogapp/home.html', context)

def category(request, path_name):
    category = Category.objects.get(path_name=path_name)
    posts = category.blog_posts.all()
    # posts = BlogPost.objects.filter(category_id=category_id)
    context = {
        'posts' : posts
    }
    return render(request, 'blogapp/category.html', context)

def blog_post(request, post_id):
    pass 

def about_me(request):
    pass

