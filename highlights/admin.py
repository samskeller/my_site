from django.contrib import admin

from .models import Book
from .models import Highlight

class BookAdmin(admin.ModelAdmin):
# title = models.CharField(max_length=100)
# author = models.CharField(max_length=100)
# subtitle = models.CharField(max_length=100)
# google_books_id = models.CharField(max_length=100)
# thumbnail_url = models.URLField()
    list_display = ('id', 'title', 'author', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

class HighlightAdmin(admin.ModelAdmin):
# book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='highlights')
# text = models.TextField()
# page_number = models.IntegerField()
    list_display = ('id', 'book', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

admin.site.register(Book, BookAdmin)
admin.site.register(Highlight, HighlightAdmin)
