from django.shortcuts import render
from django.views import generic

from .models import Post

class PostListView(generic.ListView):
    model = Post
    template_name = 'blogapp/home.html'

class PostDetailView(generic.DetailView): 
    model = Post
    template_name = "blogapp/post-detail.html"

class PostCreateView(generic.CreateView): 
    template_name = "post_new.html" 
    fields = ["title", "author", "body"]