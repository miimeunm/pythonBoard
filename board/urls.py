from . import views
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('add/', views.addForm, name="addForm"),
    path('edit/<int:id>', views.editForm, name="editForm"),
    path('delete/<int:id>', views.deleteForm, name="deleteForm"),
]