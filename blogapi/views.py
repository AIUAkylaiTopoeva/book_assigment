from rest_framework import generics 
from .models import Postapi
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView): 
    queryset = Postapi.objects.all() 
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Postapi.objects.all()
    serializer_class = PostSerializer