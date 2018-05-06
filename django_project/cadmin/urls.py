from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path('post/update/(?P<pk>[\d]+)/', views.post_update, name='post_update'),
    re_path('post/delete/(?P<pk>[\d]+)/', views.post_delete, name='post_delete'),
    path('category/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    re_path('category/update/(?P<pk>[\d]+)/', views.category_update, name='category_update'),
    re_path('category/delete/(?P<pk>[\d]+)/', views.category_delete, name='category_delete'),
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/add/', views.tag_add, name='tag_add'),
    re_path('tag/update/(?P<pk>[\d]+)/', views.tag_update, name='tag_update'),
    re_path('tag/delete/(?P<pk>[\d]+)/', views.tag_delete, name='tag_delete'),
    path('account-info/', views.account_info, name='account_info'),
    path('activate/account/', views.activate_account, name='activate'),
    path('register/', views.register, name='register'),
    path('password-change-done/',
         auth_views.password_change_done,
         {'template_name': 'cadmin/password_change_done.html'},
         name="password_change_done"),
    path('password-change/', 
         auth_views.password_change,
         {'template_name': 'cadmin/password_change.html', 'post_change_redirect': 'password_change_done'},
         name='password_change'),
    path('', views.post_list, name="post_list"),
    path('accounts/login/', views.login, {'template_name': 'cadmin/login.html'}, name='login'),
    path('accounts/logout/', auth_views.logout, {'template_name': 'cadmin/logout.html'}, name='logout'),
    path('post/add/', views.post_add, name='post_add'),
]