# from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.book_list),
    # path('subpage.html', views.book_detail),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.RegistationView.as_view(),
         name='registration'),
    path("<str:slug>/", views.BookDetailView.as_view(), name="book_detail"),
]
