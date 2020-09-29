from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortenedURL
import string
import random

def index(request):
    shortened_urls = ShortenedURL.objects.all()
    context = {
        'shortened_urls': shortened_urls
    }
    return render(request, 'shortenapp/index.html', context)

def save(request):
    long_url = request.POST['long_url']
    length = 5
    code_char = string.ascii_letters + string.digits
    code_char = list(code_char)
    code = ""
    while len(code) < length:
        code += random.choice(code_char)
    short_url = ShortenedURL(url=long_url, code=code)
    print(code)
    short_url.save()
    return HttpResponseRedirect(reverse('shortenapp:index'))

def url_redirector(request, code):
    url = ShortenedURL.objects.get(code=code)
    url.counter += 1
    url.save()
    return redirect(url.url)

