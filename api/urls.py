from django.contrib import admin
from django.urls import path
from . import views
app_name = 'api'
urlpatterns = [
    path('create-cow', views.create_cow, name="create-cow"),
    path('cows/', views.get_cows, name="create-cow"),
    path('cows/<str:id>', views.get_cows, name="create-cow"),
    path('update-cow/<str:id>', views.update_cow, name="create-cow"),
    path('delete-cow/<str:id>', views.delete_cow, name="create-cow"),
]
