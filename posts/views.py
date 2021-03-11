from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


# Create your views here.

class PostlistView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts_list.html'
    login_url = 'login'


class PostDeletView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_posts.html'
    success_url = reverse_lazy('posts_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_posts.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('posts_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'update_posts.html'
    success_url = reverse_lazy('posts_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
