from django.shortcuts import render, redirect
from django.http import JsonResponse

def mult(request):
    return render(
        request,               # так будет всегда
        'mainpage/multi.html',  # путь к шаблону
        # здесь будут данные!
    )

def multidata(request):
    # content-Type: JSON
    return JsonResponse({
        'my_size': 25
    })

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
import random
# '/myfetch/?count=6&maxval=10'
def myfetch(request):
    print(request.GET)  # {'count': ['6'], 'maxval': ['10']}
    context = {
        'questions': []
    } #                    ['6']           '6'
    if 'count' in request.GET:
        print('MAXVAL: ', request.GET['maxval'])
        print('MAXVAL: ', request.GET['count'])
        #  Создать такое количество вопросов, которе записано в count
        for i in range(0, int(request.GET['count'])):
            # 'maxval': ['10']
            # Каждый пример содержит два слагаемых, каждое из которых не больше maxval
            a = random.randint(2, int(request.GET['maxval']))
            b = random.randint(2, int(request.GET['maxval']))    
            context['questions'].append((a, b))
        return JsonResponse(context)
    print('Контекст перед рендерингом страницы: ', context)
    return render(
        request,
        'mainpage/myfetch.html',
        context
    )

def checker(request):
    import json
    #print(request.POST)
    print(request.body)
    request_str = request.body.decode('utf-8')
    print(request_str)
    user_answer = json.loads(request_str)
    print(user_answer)
    return check_answers(user_answer)

def check_answers(answers):
    #answers = {
    #    'i=0q=5+10': "15",  #==>> 'i=0', '5+10' ==>> '5', '10'
    #    'i=1q=3+3':  "6",
    #    'i=2q=2+2':   "7",
    #}
    correct = {}
    for name in answers:
        ind, q = name.split('q=')
        a, b = q.split('+')
        a = int(a)
        b = int(b)
        correct[name] = str(a+b) == answers[name]
    print('Проверка завершена!', correct)
    return JsonResponse(correct)
    correct = {
        'i=0q=5+10': True,
        'i=1q=3+3':  True,
        'i=2q=2+2':  False,
    }

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
