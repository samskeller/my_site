from django.urls import include, path

from .views import BooksHome

app_name = 'highlights'
urlpatterns = [
    path(r'', BooksHome.as_view(), name="books_list"),
]

