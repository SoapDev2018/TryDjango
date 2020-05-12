from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_post_list_view, name='allposts'),
    path('<str:slug>/', views.blog_post_detail_view, name='detail'),
    path('<str:slug>/edit', views.blog_post_update_view, name='update'),
    path('<str:slug>/delete', views.blog_post_delete_view, name='detail'),
]