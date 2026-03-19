from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.get_all_clients, name='clients'),
    path('new_client/', views.add_client, name='new_client'),
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
    path('toggle_client_status/<int:client_id>/', views.toggle_client_status, name='deactivate_client')
    ]