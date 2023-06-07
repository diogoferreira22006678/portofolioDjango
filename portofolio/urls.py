#Urls.py
from django.urls import path
from . import views

app_name = 'portofolio'

urlpatterns = [
    path('', views.home, name='portfolio-home'),
]