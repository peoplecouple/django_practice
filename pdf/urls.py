from django.urls import path
from . import views

app_name="pdf"
urlpatterns = [
    path('', views.index, name="index"),
]