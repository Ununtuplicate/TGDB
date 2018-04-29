from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('login/', views.login, name="blog_login"),
    path('logout/', views.logout, name="blog_logout"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('save-session-data/', views.save_session_data, name="save_session_data"),
    path('access-session-data/', views.access_session_data, name="access_session_data"),
    path('delete-session-data/', views.delete_session_data, name="delete_session_data"),
    path('test-delete/', views.test_delete, name='test_delete'),
    path('test-session/', views.test_session, name='test_session'),
    path('feedback/', views.feedback, name='feedback'),
    re_path('category/(?P<category_slug>[\w-]+)/', views.post_by_category, name='post_by_category'),
    re_path('tag/(?P<tag_slug>[\w-]+)/', views.post_by_tag, name='post_by_tag'),
    re_path('(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]