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
    articles = models.Article.objects.all()
    article_paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    context = {
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


from . import forms
from django.contrib import auth
def loginme(request):
    if request.method == 'POST':
        user_form = forms.UserLoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = auth.authenticate(
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                return redirect('/')
            return redirect('login')
    else:
        user_form = forms.UserLoginForm()
    return render(
        request,
        'user/login.html',
        {
            'user_form': user_form
        })
