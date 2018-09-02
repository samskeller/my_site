from django.db import models

from common.models import BaseModel
from .utils import query_google_books

class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    google_books_id = models.CharField(max_length=100)
    thumbnail_url = models.URLField()

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)

    def save(self, *args, **kwargs):
        if not self.google_books_id:
            google_books_response = query_google_books(self.title, self.author)
            self.google_books_id = google_books_response['id']
            self.thumbnail_url = google_books_response['volumeInfo']['imageLinks']['thumbnail']

        super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Highlight(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='highlights')
    text = models.TextField()
    page_number = models.IntegerField()

    def __str__(self):
        return 'Highlight {} on Book {}'.format(self.pk, self.book.pk)

    class Meta:
        verbose_name = 'Highlight'
        verbose_name_plural = 'Highlights'
