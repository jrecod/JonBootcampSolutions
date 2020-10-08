from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from lab05Blog import localsettings
from .forms import BlogForm
from django.views.generic import CreateView
from django.utils import timezone
from .models import BlogPost
import django.contrib.auth







def index(request):
    context = {
        'message': 'Test Test Test'
    }
    return render(request, 'blogapp/index.html', context)
 
def register(request):
    if request.method == 'POST':

        # recaptcha_data = {
        #     'response': request.POST['g-recaptcha-response'],
        #     'secret': localsettings.recaptcha_secret_key
        # }
        # response = request.POST('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)

        # if (response.json()['success'] == False):
        #     message = 'invalid_recpatcha'
        #     return render(request, 'blogapp/register.html', {'message': message})

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password != retype_password:
            message = 'password_does_not_match'
            return render(request, 'blogapp/register.html', {'message': message})

        if User.objects.filter(username=username).exists():
            message = 'username_is_already_in_use'
            return render(request, 'blogapp/register.html', {'message': message})
        
        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('blogapp:profile'))
    return render (request, 'blogapp/register.html')

def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username'] #integrate email login 
        password = request.POST['password']
        user = django.contrib.auth.authenticate(username=username, password=password)
        print(user)
        if user is None:
            message = 'user_not_found'
        else:
            django.contrib.auth.login(request, user)
            next = request.GET.get('next', reverse('blogapp:profile'))
            return HttpResponseRedirect(next)
    return render(request, 'blogapp/login.html', {'message':message})


@login_required
def profile(request):
    # posts = BlogPost.objects.filter(user=request.user)
    posts = request.user.blog_posts.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blogapp/profile.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_created = timezone.now()
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('blogapp:profile'))
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'blogapp/create.html', context)

@login_required
def edit(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogapp:profile'))
    else:
        form = BlogForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'blogapp/edit.html', context)
        
@login_required
def posts(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blogapp/posts.html', context)

def details(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blogapp/details.html', context)
