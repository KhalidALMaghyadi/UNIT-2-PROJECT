from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path('project/new/', views.new_add_view, name='new_add_view'),
    path('project/all/', views.all_project_view, name='all_project_view'),
    path('project/<project_id>/detail/', views.detail_project_view , name='detail_project_view'),
    path('project/<project_id>/update/', views.update_project_view, name='update_project_view'),
    path('project/<project_id>/delete/', views.delete_project_view, name='delete_project_view'),
    # path('project/search/' , views.search_plant_view, name="search_plant_view"),
 ]