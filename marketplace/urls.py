from django.contrib import admin
from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name= "marketplace-home"),
]