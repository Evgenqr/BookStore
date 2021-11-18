from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/index.html', {'books': books})


def book_detail(request):
    books = Book.objects.all()
    return render(request, 'store/subpage.html', {'books': books})
