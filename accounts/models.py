from django.db import models

from django.urls import path 
from .views import SignUpView

urlpatterns = [
path("signup/", SignUpView.as_view(), name="signup"),
]