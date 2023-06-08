from . import views
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('detail/<int:id>/', views.detail, name="detail"),
]