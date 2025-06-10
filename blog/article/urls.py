from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='feed'),
    path('new/', views.new_article, name='new_article'),
    path('last_posts/', views.new_blog_posts),
    path('<int:uid>/', views.get_my_blog_posts, name='article'),
]