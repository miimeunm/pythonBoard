from . import views
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
]
