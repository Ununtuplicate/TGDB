from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('post/add/', views.post_add, name='post_add'),
]