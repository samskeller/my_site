from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.staticfiles.templatetags.staticfiles import static

from .models import Book
from .models import Highlight

import re

class BooksHome(View):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all().order_by('-date_created')[:20]
        return render(request, 'books.html', {'books': books})

class BookHighlights(View):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.pop('book_id', None)
        book = Book.objects.get(id=book_id)
        highlights = Highlight.objects.filter(book_id=book_id).order_by('date_created')
        return render(request, 'highlights.html', {'highlights': highlights, 'book': book})
