# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list),
    # path('subpage.html', views.book_detail),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegistationView.as_view(),
         name='registration'),
    path("<str:slug>/", views.BookDetailView.as_view(), name="book_detail"),
]
