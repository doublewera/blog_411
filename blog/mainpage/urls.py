from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('feed/', views.feed, name='feed'),
    path('howto/', views.summary, name='summary'),
    path('login/', views.loginme, name='login'),
]