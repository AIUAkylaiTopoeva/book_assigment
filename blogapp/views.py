from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer

class PostListView(generic.ListView):
    model = Post
    template_name = 'blogapp/home.html'

class PostDetailView(generic.DetailView): 
    model = Post
    template_name = "blogapp/post-detail.html"

class PostCreateView(generic.CreateView): 
    model = Post
    template_name = "blogapp/post_new.html" 
    fields = ["title", "author", "body"]

class PostUpdateView(generic.UpdateView):  
    model = Post
    template_name = "blogapp/post_edit.html" 
    fields = ["title", "body"]

class PostDeleteView(generic.DeleteView): 
    model = Post
    template_name = "blogapp/post_delete.html" 
    success_url = reverse_lazy("home")


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer