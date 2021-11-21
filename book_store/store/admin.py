from django.contrib import admin
from .models import Category, Author, Genre, Publisher, Book, Reviews, CartProduct, Cart, Order, Customer, Notification

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Reviews)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Notification)
