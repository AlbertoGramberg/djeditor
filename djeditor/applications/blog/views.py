from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
#
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/lista.html"
    context_object_name = "lista_blogs"
  


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/detalle.html"



class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog/add.html"
    fields = ('__all__')
    success_url = '/'


