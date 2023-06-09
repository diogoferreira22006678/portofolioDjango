#Urls.py
from django.urls import path
from . import views

app_name = 'portofolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.pessoas_form, name='pessoas_insert'), # get and post req. for insert operation
    path('pessoas/list/', views.pessoas_list, name='pessoas_list'), # get req. to retrieve and display all records
    path('pessoas/update/<int:id>', views.pessoas_form, name='pessoa_update'), # get and post req. for update operation
    path('pessoas/delete/<int:id>', views.pessoas_delete, name='pessoa_delete'),
]