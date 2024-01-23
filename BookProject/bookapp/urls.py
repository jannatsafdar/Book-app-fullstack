from django.urls import path
from .views import book_list, book_detail, index

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
]
