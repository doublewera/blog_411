from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('feed/', views.feed, name='feed'),
    path('howto/', views.summary, name='summary'),
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'), name='logout'),
]
