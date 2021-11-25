from django.shortcuts import render
from django import views
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .models import Book, Customer
from .forms import LoginForm, RegistrationForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/index.html', {'books': books})


# def book_detail(request):
#     books = Book.objects.all()
#     return render(request, 'store/subpage.html', {'books': books})


class BaseView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class BookDetailView(views.generic.DetailView):
    model = Book
    temlate_name = 'store/subpage.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'book'


class LoginView(views.View):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'store/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'store/login.html', context)


class RegistationView(views.View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'store/registration.html', context)

    def post(serlf, request, *ergs, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(user=new_user,
                                    phone=form.cleaned_data['phone'],
                                    address=form.cleaned_data['address'])

            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'store/registration.html', context)
