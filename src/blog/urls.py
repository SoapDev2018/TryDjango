from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_post_list_view, name='allposts'),
    path('new/', views.blog_post_create_view, name='create'),
    path('<str:slug>/', views.blog_post_detail_view, name='detail'),
    path('<str:slug>/edit', views.blog_post_update_view, name='update'),
    path('<str:slug>/delete', views.blog_post_delete_view, name='detail'),
]