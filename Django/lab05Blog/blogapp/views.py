from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from lab05Blog import localsettings
from .forms import BlogForm
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
    return render(request, 'blogapp/profile.html')

@login_required
def create(request):
    model = BlogPost
    # if request.method == 'POST':
    #     form = BlogForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()
    #         return HttpResponseRedirect(reverse('blogapp:profile'))
    # else:
    #     form = BlogForm()
    # context = {
    #     'form': form
    # }
    # return render(request, 'blogapp/create.html', context)
    