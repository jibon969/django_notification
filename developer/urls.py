from django.urls import path
from . import views


urlpatterns = [
    path('developer-document/', views.developer_document, name="developer-document"),
    path('add-developer-document/', views.add_developer_document, name="add-developer-document"),
    path('update-developer-document/<int:id>/', views.update_developer_document, name="update-developer-document"),
    path('delete-developer-document/<int:id>/', views.delete_developer_document, name="delete-developer-document"),
]
