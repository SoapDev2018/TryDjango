from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_post_list_view, name='allposts'),
    path('<str:slug>/', views.blog_post_detail_view, name='detail'),
]