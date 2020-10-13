from django.core.management.base import BaseCommand
from Libraryapp.models import Book
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        # print('hello world')
        # Books.objects.all()
        response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_mountain_goat/master/4%20Django/labs/books.json')
        data = response.json()
        # print(data)
        for books_data in data['books']:
            author = books_data['author']
            country = books_data['country']
            image = books_data['image']
            language = books_data['language']
            url = books_data['url']
            pages = books_data['pages']
            title = books_data['title']
            year = books_data['year']
            books = Book(author=author, country=country, image=image, language=language, url=url, pages=pages, title=title, year=year)
            books.save()