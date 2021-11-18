from django.contrib import admin
from .models import Category, Author, Genre, Publisher, Book, Reviews

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Reviews)