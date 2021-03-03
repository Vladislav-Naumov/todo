from django.urls import path
from .views import (
    TodolistView,
    TodoDeletView,
    TodoCreateView,
    TodoUpdateView,

)


urlpatterns = [
    path('', TodolistView.as_view(), name='todo'),
    path('<int:pk>/delete/', TodoDeletView.as_view(), name='delete_todo'),
    path('<int:pk>/create/', TodoCreateView.as_view(), name='create_todo'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='update_todo'),
    ]