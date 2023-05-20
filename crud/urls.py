from django.urls import path

from .views import (
    ToDoListView, 
    ToDoCreateView, 
    ToDoDeleteView, 
    ToDoUpdateView, 
    ToDoDetailView
    )

urlpatterns = [
    path('todos/', ToDoListView.as_view()),
    path('create-todo/', ToDoCreateView.as_view()),
    path('update-view/<int:pk>/', ToDoUpdateView.as_view()),
    path('delete-view/<int:pk>/', ToDoDeleteView.as_view()),
    path('todo-detail/<int:pk>/', ToDoDetailView.as_view())
]

