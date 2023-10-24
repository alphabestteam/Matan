from django.urls import path
from .views import ListBooks, RetrieveUpdateDestroyBook

urlpatterns = [
    path('api/books/', ListBooks.as_view(), name='book-list'),
    path('api/books/<int:pk>/', RetrieveUpdateDestroyBook.as_view(), name='book-detail'),
]
