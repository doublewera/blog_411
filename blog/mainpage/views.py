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
