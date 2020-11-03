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
    posts = category.blog_posts.all().order_by('-date_created')
    context = {
        'posts' : posts,
        'category': category,
    }
    return render(request, 'blogapp/category.html', context)

def blog_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    categories = Category.objects.all()
    for category in categories:
        print(category.id)
    print(categories)
    context = {
        'post' : post,
        'categories' : categories,
    }
    return render(request, 'blogapp/blogPost.html', context)

def about_me(request):
   return render(request, 'blogapp/about.html')

