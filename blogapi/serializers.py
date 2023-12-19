from rest_framework import serializers 
from .models import Postapi

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        fields = (
            "id","author", "title", "body", "created_at",)
        model = Postapi