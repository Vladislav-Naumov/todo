from django.urls import path
from .views import (
    PostlistView,
    PostDeletView,
    PostCreateView,
    PostUpdateView,
)


urlpatterns = [
    path('', PostlistView.as_view(), name='posts_list'),
    path('<int:pk>/delete/', PostDeletView.as_view(), name='delete_posts'),
    path('<int:pk>/create/', PostCreateView.as_view(), name='create_posts'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update_posts'),
    ]