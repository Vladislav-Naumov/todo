from django.shortcuts import render
from .models import TodoItem
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class TodolistView(LoginRequiredMixin, ListView):
    model = TodoItem
    template_name = 'todo.html'
    login_url = 'login'



class TodoDeletView(LoginRequiredMixin, DeleteView):
    model = TodoItem
    template_name = 'delete_todo.html'
    success_url = reverse_lazy('todo')
    login_url = 'login'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoItem
    template_name = 'create_todo.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('todo')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoItem
    fields = ('title', 'body')
    template_name = 'update_todo.html'
    success_url = reverse_lazy('todo')
    login_url = 'login'
