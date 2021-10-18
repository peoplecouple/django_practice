
from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<num>', views.detail, name="detail" ),
    path('create', views.create, name="create" ),
    path('delete/<conid>', views.delete, name="delete"),
    path('update/<conid>', views.update, name="update"),
    path('create_reply/<conid>', views.create_reply, name="create_reply"),
    path('delete_reply/<conid>/<num>', views.delete_reply, name="delete_reply"),
    path('up/<conid>', views.up, name="up"),
    path('cancel/<conid>', views.cancel, name="cancel")

] 
