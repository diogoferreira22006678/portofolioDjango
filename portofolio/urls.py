#Urls.py
from django.urls import path
from . import views

app_name = 'portofolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.pessoas_form, name='pessoas_insert'), # get and post req. for insert operation
    path('pessoas/list/', views.pessoas_list, name='pessoas_list'), # get req. to retrieve and display all records
    path('pessoas/update/<int:id>', views.pessoas_form, name='pessoa_update'), # get and post req. for update operation
    path('pessoas/delete/<int:id>', views.pessoas_delete, name='pessoa_delete'), # get req. to delete operation

    path('professores/', views.professores_form, name='professores_insert'), # get and post req. for insert operation
    path('professores/list/', views.professores_list, name='professores_list'), # get req. to retrieve and display all records
    path('professores/update/<int:id>', views.professores_form, name='professor_update'), # get and post req. for update operation
    path('professores/delete/<int:id>', views.professores_delete, name='professor_delete'), # get req. to delete operation

    path('escolas/', views.escolas_form, name='escolas_insert'), # get and post req. for insert operation
    path('escolas/list/', views.escolas_list, name='escolas_list'), # get req. to retrieve and display all records
    path('escolas/update/<int:id>', views.escolas_form, name='escola_update'), # get and post req. for update operation
    path('escolas/delete/<int:id>', views.escolas_delete, name='escola_delete'), # get req. to delete operation
]