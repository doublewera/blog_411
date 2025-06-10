from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # путь в брауз, функция во views, имя для {% url %}
    path('',             views.main, name='mainpage'),
    path('howto/',       views.summary, name='summary'),
    path('myfetch/',     views.myfetch, name='myfetch'),
    path('multidata/',   views.multidata, name='multi_tbl_data'),
    path('multitable/',  views.mult, name='multi_tbl_name'),
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'), name='logout'),
    path('register/',    views.register, name='register'),
]
