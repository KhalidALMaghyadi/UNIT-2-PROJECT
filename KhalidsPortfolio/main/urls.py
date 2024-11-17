from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/me/', views.about_me_view, name='about_me_view'),
    path('resume/' ,views.resume_view , name='resume_view'),
]