from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('blog/new/', views.new_blog_view, name='new_blog_view'),
    path('blog/all/', views.all_blogs_view, name='all_blogs_view'),
    path('blog/<blog_id>/detail', views.blog_detail_view, name='blog_detail_view'),
    path('blog/<blog_id>/update/', views.update_blog_view, name='update_blog_view'),
    path('blog/<blog_id>/delete/', views.delete_blog_view, name='delete_blog_view'),
 ]