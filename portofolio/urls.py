#Urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portofolio'

urlpatterns = [

    path('backend/', views.home, name='home'),
    
    path('backend/pessoas/', views.pessoas_form, name='pessoas_insert'), # get and post req. for insert operation
    path('backend/pessoas/list/', views.pessoas_list, name='pessoas_list'), # get req. to retrieve and display all records
    path('backend/pessoas/update/<int:id>', views.pessoas_form, name='pessoa_update'), # get and post req. for update operation
    path('backend/pessoas/delete/<int:id>', views.pessoas_delete, name='pessoa_delete'), # get req. to delete operation

    path('backend/professores/', views.professores_form, name='professores_insert'), # get and post req. for insert operation
    path('backend/professores/list/', views.professores_list, name='professores_list'), # get req. to retrieve and display all records
    path('backend/professores/update/<int:id>', views.professores_form, name='professor_update'), # get and post req. for update operation
    path('backend/professores/delete/<int:id>', views.professores_delete, name='professor_delete'), # get req. to delete operation

    path('backend/escolas/', views.escolas_form, name='escolas_insert'), # get and post req. for insert operation
    path('backend/escolas/list/', views.escolas_list, name='escolas_list'), # get req. to retrieve and display all records
    path('backend/escolas/update/<int:id>', views.escolas_form, name='escola_update'), # get and post req. for update operation
    path('backend/escolas/delete/<int:id>', views.escolas_delete, name='escola_delete'), # get req. to delete operation

    path('backend/universidades/', views.universidades_form, name='universidades_insert'), # get and post req. for insert operation
    path('backend/universidades/list/', views.universidades_list, name='universidades_list'), # get req. to retrieve and display all records
    path('backend/universidades/update/<int:id>', views.universidades_form, name='universidade_update'), # get and post req. for update operation
    path('backend/universidades/delete/<int:id>', views.universidades_delete, name='universidade_delete'), # get req. to delete operation

    path('backend/cursos/', views.cursos_form, name='cursos_insert'), # get and post req. for insert operation
    path('backend/cursos/list/', views.cursos_list, name='cursos_list'), # get req. to retrieve and display all records
    path('backend/cursos/update/<int:id>', views.cursos_form, name='curso_update'), # get and post req. for update operation
    path('backend/cursos/delete/<int:id>', views.cursos_delete, name='curso_delete'), # get req. to delete operation

    path('backend/cadeiras/', views.cadeiras_form, name='cadeiras_insert'), # get and post req. for insert operation
    path('backend/cadeiras/list/', views.cadeiras_list, name='cadeiras_list'), # get req. to retrieve and display all records
    path('backend/cadeiras/update/<int:id>', views.cadeiras_form, name='cadeira_update'), # get and post req. for update operation
    path('backend/cadeiras/delete/<int:id>', views.cadeiras_delete, name='cadeira_delete'), # get req. to delete operation

    path('backend/projetos/', views.projetos_form, name='projetos_insert'), # get and post req. for insert operation
    path('backend/projetos/list/', views.projetos_list, name='projetos_list'), # get req. to retrieve and display all records
    path('backend/projetos/update/<int:id>', views.projetos_form, name='projeto_update'), # get and post req. for update operation
    path('backend/projetos/delete/<int:id>', views.projetos_delete, name='projeto_delete'), # get req. to delete operation

    path('backend/linguagens/', views.linguagens_form, name='linguagens_insert'), # get and post req. for insert operation
    path('backend/linguagens/list/', views.linguagens_list, name='linguagens_list'), # get req. to retrieve and display all records
    path('backend/linguagens/update/<int:id>', views.linguagens_form, name='linguagem_update'), # get and post req. for update operation
    path('backend/linguagens/delete/<int:id>', views.linguagens_delete, name='linguagem_delete'), # get req. to delete operation

    path('backend/experiencias-profissionais/', views.experiencias_profissionais_form, name='experiencias_profissionais_insert'), # get and post req. for insert operation
    path('backend/experiencias-profissionais/list/', views.experiencias_profissionais_list, name='experiencias_profissionais_list'), # get req. to retrieve and display all records
    path('backend/experiencias-profissionais/update/<int:id>', views.experiencias_profissionais_form, name='experiencia_profissional_update'), # get and post req. for update operation
    path('backend/experiencias-profissionais/delete/<int:id>', views.experiencias_profissionais_delete, name='experiencia_profissional_delete'), # get req. to delete operation

    path('backend/aptidoes/', views.aptidoes_form, name='aptidoes_insert'), # get and post req. for insert operation
    path('backend/aptidoes/list/', views.aptidoes_list, name='aptidoes_list'), # get req. to retrieve and display all records
    path('backend/aptidoes/update/<int:id>', views.aptidoes_form, name='aptidao_update'), # get and post req. for update operation
    path('backend/aptidoes/delete/<int:id>', views.aptidoes_delete, name='aptidao_delete'), # get req. to delete operation

    path('backend/interesses/', views.interesses_form, name='interesses_insert'), # get and post req. for insert operation
    path('backend/interesses/list/', views.interesses_list, name='interesses_list'), # get req. to retrieve and display all records
    path('backend/interesses/update/<int:id>', views.interesses_form, name='interesse_update'), # get and post req. for update operation
    path('backend/interesses/delete/<int:id>', views.interesses_delete, name='interesse_delete'), # get req. to delete operation

    path('backend/tecnologias/', views.tecnologias_form, name='tecnologias_insert'), # get and post req. for insert operation
    path('backend/tecnologias/list/', views.tecnologias_list, name='tecnologias_list'), # get req. to retrieve and display all records
    path('backend/tecnologias/update/<int:id>', views.tecnologias_form, name='tecnologia_update'), # get and post req. for update operation
    path('backend/tecnologias/delete/<int:id>', views.tecnologias_delete, name='tecnologia_delete'), # get req. to delete operation

    path('backend/tipo-tecnologias/', views.tipo_tecnologias_form, name='tipo_tecnologias_insert'), # get and post req. for insert operation
    path('backend/tipo-tecnologias/list/', views.tipo_tecnologias_list, name='tipo_tecnologias_list'), # get req. to retrieve and display all records
    path('backend/tipo-tecnologias/update/<int:id>', views.tipo_tecnologias_form, name='tipo_tecnologia_update'), # get and post req. for update operation
    path('backend/tipo-tecnologias/delete/<int:id>', views.tipo_tecnologias_delete, name='tipo_tecnologia_delete'), # get req. to delete operation

    path('backend/tipo-aptidoes/', views.tipo_aptidoes_form, name='tipo_aptidoes_insert'), # get and post req. for insert operation
    path('backend/tipo-aptidoes/list/', views.tipo_aptidoes_list, name='tipo_aptidoes_list'), # get req. to retrieve and display all records
    path('backend/tipo-aptidoes/update/<int:id>', views.tipo_aptidoes_form, name='tipo_aptidao_update'), # get and post req. for update operation
    path('backend/tipo-aptidoes/delete/<int:id>', views.tipo_aptidoes_delete, name='tipo_aptidao_delete'), # get req. to delete operation

    path('backend/tipo-projetos/', views.tipo_projetos_form, name='tipo_projetos_insert'), # get and post req. for insert operation
    path('backend/tipo-projetos/list/', views.tipo_projetos_list, name='tipo_projetos_list'), # get req. to retrieve and display all records
    path('backend/tipo-projetos/update/<int:id>', views.tipo_projetos_form, name='tipo_projeto_update'), # get and post req. for update operation
    path('backend/tipo-projetos/delete/<int:id>', views.tipo_projetos_delete, name='tipo_projeto_delete'), # get req. to delete operation

    # Frontend urls
    path('download/', views.download_file, name='download_file'),
    path('', views.index, name='index'),
    path('studies/', views.studies, name='studies'),
    path('discipline/<int:id>', views.discipline, name='discipline'),
    path('skills/', views.skills, name='skills'),
    path('interests/', views.interests, name='interests'),
    path('project<int:id>', views.project, name='project'),
    path('web/', views.web, name='web'),
    path('page_details/', views.page_details, name='page_details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)