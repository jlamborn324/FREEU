from django.contrib import admin
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name= "marketplace-home"),
    path('itempost/<int:pk>/', PostDetailView.as_view(), name= "itempost-detail"),
    path('itempost/new/', PostCreateView.as_view(), name= "itempost-create"),
] 