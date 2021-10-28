from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('task/<int:id>', views.task, name='task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('new_task/', views.new_task, name='new_task'),
]