from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_list')
