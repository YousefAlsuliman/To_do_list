from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("toggle/<int:task_id>/", views.toggle_complete, name="toggle_complete"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    
]
