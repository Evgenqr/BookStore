from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list),
    path('subpage.html', views.book_detail),
    
]
