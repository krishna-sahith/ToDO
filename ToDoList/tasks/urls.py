from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('completed/', views.completed_tasks, name='completed_tasks'),  # View completed tasks
    path('mark_completed/<int:task_id>/', views.mark_completed, name='mark_completed'),  # Mark task as completed
    path('completed/delete/', views.delete_completed_tasks, name='delete_completed_tasks'),
    # Other URL patterns
]