from django.urls import path
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, book_increment, book_decrement, test, lib

app_name = 'p_library'

urlpatterns = [
    path('', lib),
    path('book_increment/', book_increment),
    path('book_decrement/', book_decrement),
    path('test/', test),
    path('author/create/', AuthorEdit.as_view(), name='author_create'),  
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/create_many/', author_create_many, name='author_create_many'),
    path('author_book/create_many/', books_authors_create_many, name='author_book_create_many'),
]