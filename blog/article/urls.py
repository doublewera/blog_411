from django.urls import path
from . import views

urlpatterns = [
    #path('1/', views.article, name='article'),
    path('<int:uid>/', views.get_my_blog_posts, name='from_bd')
]