from django.urls import include, path

from .views import BooksHome
from .views import BookHighlights

app_name = 'highlights'
urlpatterns = [
    path(r'', BooksHome.as_view(), name="books_list"),
    path(r'/<int:book_id>', BookHighlights.as_view(), name='book_highlights'),
]
