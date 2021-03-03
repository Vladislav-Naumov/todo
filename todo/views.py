from django.shortcuts import render
from .models import TodoItem
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy



# Create your views here.

class TodolistView(ListView):
    model = TodoItem
    template_name = 'todo.html'


class TodoDeletView(DeleteView):
    model = TodoItem
    template_name = 'delete_todo.html'
    success_url = reverse_lazy('todo')


class TodoCreateView(CreateView):
    model = TodoItem
    template_name = 'create_todo.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('todo')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoUpdateView(UpdateView):
    model = TodoItem
    fields = ('title', 'body')
    template_name = 'update_todo.html'
    success_url = reverse_lazy('todo')

