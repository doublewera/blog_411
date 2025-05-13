from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('howto/', views.summary, name='summary'),
]