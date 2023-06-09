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

    path('universidades/', views.universidades_form, name='universidades_insert'), # get and post req. for insert operation
    path('universidades/list/', views.universidades_list, name='universidades_list'), # get req. to retrieve and display all records
    path('universidades/update/<int:id>', views.universidades_form, name='universidade_update'), # get and post req. for update operation
    path('universidades/delete/<int:id>', views.universidades_delete, name='universidade_delete'), # get req. to delete operation

    path('cursos/', views.cursos_form, name='cursos_insert'), # get and post req. for insert operation
    path('cursos/list/', views.cursos_list, name='cursos_list'), # get req. to retrieve and display all records
    path('cursos/update/<int:id>', views.cursos_form, name='curso_update'), # get and post req. for update operation
    path('cursos/delete/<int:id>', views.cursos_delete, name='curso_delete'), # get req. to delete operation

    path('cadeiras/', views.cadeiras_form, name='cadeiras_insert'), # get and post req. for insert operation
    path('cadeiras/list/', views.cadeiras_list, name='cadeiras_list'), # get req. to retrieve and display all records
    path('cadeiras/update/<int:id>', views.cadeiras_form, name='cadeira_update'), # get and post req. for update operation
    path('cadeiras/delete/<int:id>', views.cadeiras_delete, name='cadeira_delete'), # get req. to delete operation
]