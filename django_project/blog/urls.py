from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.index, name='blog_index'),
]