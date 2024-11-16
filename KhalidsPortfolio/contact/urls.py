from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('contact/all/', views.all_messages_view, name='all_messages_view'),
    path('contact/<message_id>/delete/', views.delete_message_view, name='delete_message_view'),
]