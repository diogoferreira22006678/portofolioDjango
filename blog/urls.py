from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('nova/', views.nova, name='blog-nova'),
    path('editar/<int:pk>/', views.editar, name='blog-editar'),
    path('deletar/<int:pk>/', views.deletar, name='blog-deletar'),
]