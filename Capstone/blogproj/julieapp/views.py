from django.shortcuts import render, redirect, reverse, get_object_or_404
from blogapp.models import BlogPost, Category
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .forms import BlogForm

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('here')
            login(request, user)
            messages.info(request, f"You are now logged in as {username}. Welcome back!")
            next = request.GET.get('next', reverse('julieapp:dashboard'))
            return HttpResponseRedirect(next)
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'julieapp/login.html') 

@login_required
def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('julieapp:login'))

@login_required
def dashboard(request):
    posts = BlogPost.objects.all().order_by('-date_created')
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')        
    categories = Category.objects.all()
    if search !='' or category!='':
        posts = posts.filter(Q(title__icontains=search)
                             & Q(categories__name__icontains=category))
    context = {
        'posts': posts,
        "search": search,
        "categories": categories,
        "selected_category": category,
    }
    return render(request, 'julieapp/dashboard.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            print('here')
            post = form.save()
            return HttpResponseRedirect(reverse('julieapp:dashboard'))
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'julieapp/create.html', context)

@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method =='POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('julieapp:dashboard'))
    else:
        form = BlogForm(instance=post)
    context = {
        'form': form,
        'post_to_delete': post,
    }
    return render(request, 'julieapp/edit.html', context)

@login_required
def delete_post(request, post_id):
    post_to_delete = get_object_or_404(BlogPost, id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect(reverse('julieapp:dashboard'))