from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('add/', views.car_create, name='car_create'),
    path('edit/<int:pk>/', views.car_update, name='car_update'),
    path('delete/<int:pk>/', views.car_delete, name='car_delete'),
    path('upload/', views.upload_csv, name='upload_csv'),
]
