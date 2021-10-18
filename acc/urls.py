from django.urls import path, include
from . import views

app_name = "acc"
urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),
    path('signup', views.user_signup, name="user_signup"),
    path('profile', views.user_profile, name="user_profile"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete"),
    path('assign', views.assign)

]