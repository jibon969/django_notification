from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('notifications/', views.notifications, name="notifications"),
    path('delete-notifications/<int:id>/', views.delete_notifications, name="delete-notifications"),
]
