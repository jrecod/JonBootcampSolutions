from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Book
import json

def index(request):
    context = {
        'message': 'TEST TEST TEST'
    }
    return render(request, 'Libraryapp/index.html', context)

def search(request):
    books = Book.objects.all()
    text = request.GET.get('text', '')
    if text != '':
        books = Book.objects.filter(Q(title__icontains=text))
    page = request.GET.get('page', 1)
    books_per_page = 5
    pagintor = Paginator(books, books_per_page)
    books = pagintor.page(page)
    books_data = []
    for book in books:
        books_data.append({
            'title': book.title,
            'author': book.author,
            'image': book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language,
        })

    return JsonResponse({'books': books_data})
