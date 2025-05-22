from django.shortcuts import render

def article(request):
    context = {  # Это словарь контекста, он целиком передается в страницу-шаблон
        'posts': [ # Это список, в нем содержится много постов, которые блоггер запостил в блог
            {  # Это первый словарь, он содержит информацию о первом посте 
                'title': 'Веселенький заголовочек',
                'text':  'Интересный рассказ',
            }, # Это запятая, она разделяет элементы списка
            {  # Это второй словарь, он содержит информацию о первом посте
                'title': 'Грустненький заголовочек',
                'text':  'Студенты плохо помнят списки и словари',
            }, # Это запятая, она разделяет элементы списка
            {  # Это второй словарь, он содержит информацию о первом посте
                'title': 'Теперь изучаем циклы в шаблонах',
                'text':  '{% for elem in spisok %}',
            }
        ]
    }
    return render(
        request,
        'article/page.html',
        context
    )

from datetime import datetime
from . import models
def get_my_blog_posts(request, uid):
    print('Я получил', uid)
    context = {  # Это словарь контекста, он целиком передается в страницу-шаблон
        'posts': models.Article.objects.filter(
            user_id=uid
        )
    }
    return render(
        request,
        'article/page.html',
        context
    )
