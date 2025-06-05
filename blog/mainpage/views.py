from django.shortcuts import render, redirect

def main(request):
    return render(
        request,               # так будет всегда
        'mainpage/main.html',  # путь к шаблону
        # здесь будут данные!
    )

from article import models
from django.core.paginator import Paginator
def feed(request):
    if request.user.is_authenticated:
         user = request.user
    articles = models.Article.objects.all()
    article_paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    context = {
        'user': user,
        'posts': article_paginator.get_page(page)
    }
    return render(
        request,               # так будет всегда
        'mainpage/feed.html',  # путь к шаблону
        context
    )

def summary(request):
    return render(
        request,               # так будет всегда
        'mainpage/summary.html',  # путь к шаблону
        # здесь будут данные!
    )
def myfetch(request):
    return render(
        request,
        'mainpage/myfetch.html'
    )

from . import forms
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            auth.login(request, new_user)
            return redirect('/')
    else:
        user_form = forms.UserRegistrationForm()
    return render(
        request,
        'user/register.html',
        {
            'form': user_form
        })
