from django.db import models

from common.models import BaseModel
from .google_books_utils import query_google_books, get_thumbnail

class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    google_books_id = models.CharField(max_length=100, blank=True)
    thumbnail = models.ImageField(blank=True)

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)

    def save(self, *args, **kwargs):
        if not self.google_books_id:
            # Query the Google Books API for the book
            google_books_response = query_google_books(self.title, self.author)
            self.google_books_id = google_books_response['id']
            if 'subtitle' in google_books_response['volumeInfo']:
                self.subtitle = google_books_response['volumeInfo']['subtitle']

            # Retrieve and save the thumbnail
            [filename, file] = get_thumbnail(google_books_response)
            self.thumbnail.save(filename, file)

        super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Highlight(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='highlights')
    text = models.TextField()

    def __str__(self):
        return 'Highlight {} on Book {}'.format(self.pk, self.book.pk)

    class Meta:
        verbose_name = 'Highlight'
        verbose_name_plural = 'Highlights'
