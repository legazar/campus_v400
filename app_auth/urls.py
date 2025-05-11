from django.urls import path
from .views import login_blog,register_blog,logout_blog

urlpatterns = [
    path('',login_blog,name='login_blog'),
    path('register',register_blog,name = 'register_blog'),
    path('logout',logout_blog,name = 'logout_blog'),
]
