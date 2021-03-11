from django.urls import path

from .views import HomeTodoView

urlpatterns = (
    path('', HomeTodoView.as_view(), name='home'),
)
