from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.


class HomeTodoView(TemplateView):
    template_name = 'home.html'
