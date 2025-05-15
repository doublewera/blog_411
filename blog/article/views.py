from django.shortcuts import render

def article(request):
    context = {
        'title': 'Веселенький заголовочек',
        'text':  'Интересный рассказ',
    }
    return render(
        request,
        'article/page.html',
        context
    )
