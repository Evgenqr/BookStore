from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Category, Author, Genre, Publisher, Book, Reviews, CartProduct, Cart, Order, Customer, Notification, ImageGalery


class ImageGalleryInline(GenericTabularInline):
    model = ImageGalery
    readonly_fields = ('image_url',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline]


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Reviews)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Notification)
admin.site.register(ImageGalery)
