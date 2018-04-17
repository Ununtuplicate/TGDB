from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('category/(?P<category_slug>[\w-]+)/', views.post_by_category, name='post_by_category'),
    re_path('tag/(?P<tag_slug>[\w-]+)/', views.post_by_tag, name='post_by_tag'),
    re_path('(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]