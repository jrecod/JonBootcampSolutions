from django.shortcuts import render, redirect, reverse
from blogapp.models import BlogPost, Category
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .forms import BlogForm


def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            print('here')
            post = form.save()
            return HttpResponseRedirect(reverse('blogapp:home'))
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'julieapp/create.html', context)

def edit_post(request):
    pass

def delete_post(request):
    pass

def dashboard(request):
    pass

def login_request(request): #add recapcha
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('here')
            login(request, user)
            messages.info(request, f"You are now logged in as {username}. Welcome back!")
            next = request.GET.get('next', reverse('blogapp:home'))
            return HttpResponseRedirect(next)
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'julieapp/login.html') 

def logout_request(request):
    logout(request)
    messages.info(request, "Goodbye Jullie!")
    return redirect('blogapp:home')