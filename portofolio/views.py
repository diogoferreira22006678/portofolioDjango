from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import os 
from datetime import datetime
from django.http import FileResponse
from django.conf import settings

from .forms import PessoaForm
from .forms import ProfessorForm
from .forms import EscolaForm
from .forms import UniversidadeForm
from .forms import CursoForm
from .forms import CadeiraForm
from .forms import ProjetoForm
from .forms import LinguagemForm
from .forms import ExperienciaProfissionalForm
from .forms import AptidaoForm
from .forms import TecnologiaForm
from .forms import TipoTecnologiaForm
from .forms import TipoAptidaoForm
from .forms import TipoProjetoForm

from .models import Pessoa
from .models import Professor
from .models import Escola
from .models import Universidade
from .models import Curso
from .models import Cadeira
from .models import Projeto
from .models import Linguagem
from .models import ExperienciaProfissional
from .models import Aptidao
from .models import Tecnologia
from .models import TipoTecnologia
from .models import TipoAptidao
from .models import TipoProjeto

# Create your views here.
@login_required
def home(request):
    return render(request, 'portofolio/home.html')

@login_required
def pessoas_list(request):

    context = {'pessoas_list': Pessoa.objects.all()}

    return render(request, 'portofolio/pessoal/pessoas/pessoa_list.html', context)

@login_required
def pessoas_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PessoaForm()
        else:
            pessoa = Pessoa.objects.get(pk=id)
            form = PessoaForm(instance=pessoa)
        return render(request, 'portofolio/pessoal/pessoas/pessoa_form.html', {'form': form})
    else:
        if id == 0:
            form = PessoaForm(request.POST)
        else:
            pessoa = Pessoa.objects.get(pk=id)
            form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
        return redirect('/backend/pessoas/list/')

@login_required
def pessoas_delete(request, id):
    pessoa = Pessoa.objects.get(pk=id)
    pessoa.delete()
    return redirect('/backend/pessoas/list/')

@login_required
def professores_list(request):
    
    context = {'professores_list': Professor.objects.all()}
    
    return render(request, 'portofolio/pessoal/professores/professor_list.html', context)

@login_required
def professores_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProfessorForm()
        else:
            professor = Professor.objects.get(pk=id)
            form = ProfessorForm(instance=professor)
        return render(request, 'portofolio/pessoal/professores/professor_form.html', {'form': form})
    else:
        if id == 0:
            form = ProfessorForm(request.POST)
        else:
            professor = Professor.objects.get(pk=id)
            form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
        return redirect('/backend/professores/list/')
    
@login_required
def professores_delete(request, id):
    professor = Professor.objects.get(pk=id)
    professor.delete()
    return redirect('/backend/professores/list/')

@login_required
def escolas_list(request):
        
        context = {'escolas_list': Escola.objects.all()}
        
        return render(request, 'portofolio/educacao/escolas/escola_list.html', context)

@login_required
def escolas_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EscolaForm()
        else:
            escola = Escola.objects.get(pk=id)
            form = EscolaForm(instance=escola)
        return render(request, 'portofolio/educacao/escolas/escola_form.html', {'form': form})
    else:
        if id == 0:
            form = EscolaForm(request.POST, request.FILES)
        else:
            escola = Escola.objects.get(pk=id)
            form = EscolaForm(request.POST, instance=escola)
        if form.is_valid():
            form.save()
        return redirect('/backend/escolas/list/')
    
@login_required
def escolas_delete(request, id):
    escola = Escola.objects.get(pk=id)
    escola.delete()
    return redirect('/backend/escolas/list/')

@login_required
def universidades_list(request):
            
            context = {'universidades_list': Universidade.objects.all()}
            
            return render(request, 'portofolio/educacao/universidades/universidade_list.html', context)

@login_required
def universidades_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UniversidadeForm()
        else:
            universidade = Universidade.objects.get(pk=id)
            form = UniversidadeForm(instance=universidade)
        return render(request, 'portofolio/educacao/universidades/universidade_form.html', {'form': form})
    else:
        if id == 0:
            form = UniversidadeForm(request.POST, request.FILES)
        else:
            universidade = Universidade.objects.get(pk=id)
            form = UniversidadeForm(request.POST, instance=universidade)
        if form.is_valid():
            form.save()
        return redirect('/backend/universidades/list/')

@login_required
def universidades_delete(request, id):
    universidade = Universidade.objects.get(pk=id)
    universidade.delete()
    return redirect('/backend/universidades/list/')

@login_required
def cursos_list(request):

    context = {'cursos_list': Curso.objects.all()}

    return render(request, 'portofolio/educacao/cursos/curso_list.html', context)

@login_required
def cursos_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CursoForm()
        else:
            curso = Curso.objects.get(pk=id)
            form = CursoForm(instance=curso)
        return render(request, 'portofolio/educacao/cursos/curso_form.html', {'form': form})
    else:
        if id == 0:
            form = CursoForm(request.POST)
        else:
            curso = Curso.objects.get(pk=id)
            form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
        return redirect('/backend/cursos/list/')
    
@login_required
def cursos_delete(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('/backend/cursos/list/')

@login_required
def cadeiras_list(request):

    context = {'cadeiras_list': Cadeira.objects.all()}

    return render(request, 'portofolio/educacao/cadeiras/cadeira_list.html', context)

@login_required
def cadeiras_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CadeiraForm()
        else:
            cadeira = Cadeira.objects.get(pk=id)
            form = CadeiraForm(instance=cadeira)
        return render(request, 'portofolio/educacao/cadeiras/cadeira_form.html', {'form': form})
    else:
        if id == 0:
            form = CadeiraForm(request.POST)
        else:
            cadeira = Cadeira.objects.get(pk=id)
            form = CadeiraForm(request.POST, instance=cadeira)
        if form.is_valid():
            form.save()
        return redirect('/backend/cadeiras/list/')
    
@login_required
def cadeiras_delete(request, id):
    cadeira = Cadeira.objects.get(pk=id)
    cadeira.delete()
    return redirect('/backend/cadeiras/list/')

@login_required
def  projetos_list(request):

    context = {'projetos_list': Projeto.objects.all()}

    return render(request, 'portofolio/trabalhos/projetos/projeto_list.html', context)

@login_required
def projetos_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProjetoForm()
        else:
            projecto = ProjetoForm.objects.get(pk=id)
            form = ProjetoForm(instance=projecto)
        return render(request, 'portofolio/trabalhos/projetos/projeto_form.html', {'form': form})
    else:
        if id == 0:
            form = ProjetoForm(request.POST, request.FILES)
        else:
            projecto = Projeto.objects.get(pk=id)
            form = ProjetoForm(request.POST, instance=projecto)
        if form.is_valid():
            form.save()
        return redirect('/backend/projetos/list/')
    
@login_required
def projetos_delete(request, id):
    projecto = Projeto.objects.get(pk=id)
    projecto.delete()
    return redirect('/backend/projetos/list/')

@login_required
def  linguagens_list(request):
    
        context = {'linguagem_list': Linguagem.objects.all()}
    
        return render(request, 'portofolio/trabalhos/linguagens/linguagem_list.html', context)

@login_required
def linguagens_form(request, id=0):
    print(request.method, id)
    if request.method == "GET":
        if id == 0:
            form = LinguagemForm()
        else:
            linguagem = Linguagem.objects.get(pk=id)
            form = LinguagemForm(instance=linguagem)
        return render(request, 'portofolio/trabalhos/linguagens/linguagem_form.html', {'form': form})
    else:
        if id == 0:
            form = LinguagemForm(request.POST)
        else:
            linguagem = Linguagem.objects.get(pk=id)
            form = LinguagemForm(request.POST, instance=linguagem)
        if form.is_valid():
            form.save()
        return redirect('/backend/linguagens/list/')
    
@login_required
def linguagens_delete(request, id):
    linguagem = Linguagem.objects.get(pk=id)
    linguagem.delete()
    return redirect('/backend/linguagens/list/')

@login_required
def experiencias_profissionais_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ExperienciaProfissionalForm()
        else:
            experiencia_profissional = ExperienciaProfissional.objects.get(pk=id)
            form = ExperienciaProfissionalForm(instance=experiencia_profissional)
        return render(request, 'portofolio/trabalhos/experiencias_profissionais/experiencia_profissional_form.html', {'form': form})
    else:
        if id == 0:
            form = ExperienciaProfissionalForm(request.POST)
        else:
            experiencia_profissional = ExperienciaProfissional.objects.get(pk=id)
            form = ExperienciaProfissionalForm(request.POST, instance=experiencia_profissional)
        if form.is_valid():
            form.save()
        return redirect('/backend/experiencias-profissionais/list/')
    
@login_required
def experiencias_profissionais_delete(request, id):
    experiencia_profissional = ExperienciaProfissional.objects.get(pk=id)
    experiencia_profissional.delete()
    return redirect('/backend/experiencias-profissionais/list/')

@login_required
def experiencias_profissionais_list(request):
    
    context = {'experiencias_profissionais_list': ExperienciaProfissional.objects.all()}

    return render(request, 'portofolio/trabalhos/experiencias_profissionais/experiencia_profissional_list.html', context)

@login_required
def aptidoes_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AptidaoForm()
        else:
            aptidao = Aptidao.objects.get(pk=id)
            form = AptidaoForm(instance=aptidao)
        return render(request, 'portofolio/sobre/aptidoes/aptidao_form.html', {'form': form})
    else:
        if id == 0:
            form = AptidaoForm(request.POST)
        else:
            aptidao = Aptidao.objects.get(pk=id)
            form = AptidaoForm(request.POST, instance=aptidao)
        if form.is_valid():
            form.save()
        return redirect('/backend/aptidoes/list/')
    
@login_required
def aptidoes_delete(request, id):
    aptidao = Aptidao.objects.get(pk=id)
    aptidao.delete()
    return redirect('/backend/aptidoes/list/')

@login_required
def aptidoes_list(request):
        
    context = {'aptidoes_list': Aptidao.objects.all()}

    return render(request, 'portofolio/sobre/aptidoes/aptidao_list.html', context)

@login_required
def tecnologias_form(request):
    if request.method == "GET":
        form = TecnologiaForm()
        return render(request, 'portofolio/sobre/tecnologias/tecnologia_form.html', {'form': form})
    else:
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/backend/tecnologias/list/')
    
@login_required
def tecnologias_delete(request, id):
    tecnologia = Tecnologia.objects.get(pk=id)
    tecnologia.delete()
    return redirect('/backend/tecnologias/list/')

@login_required
def tecnologias_list(request):

    context = {'tecnologias_list': Tecnologia.objects.all()}

    return render(request, 'portofolio/sobre/tecnologias/tecnologia_list.html', context)

@login_required
def tipo_tecnologias_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TipoTecnologiaForm()
        else:
            tipo_tecnologia = TipoTecnologia.objects.get(pk=id)
            form = TipoTecnologiaForm(instance=tipo_tecnologia)
        return render(request, 'portofolio/tipos/tipo_tecnologias/tipo_tecnologia_form.html', {'form': form})
    else:
        if id == 0:
            form = TipoTecnologiaForm(request.POST)
        else:
            tipo_tecnologia = TipoTecnologia.objects.get(pk=id)
            form = TipoTecnologiaForm(request.POST, instance=tipo_tecnologia)
        if form.is_valid():
            form.save()
        return redirect('/backend/tipo-tecnologias/list/')
    
@login_required
def tipo_tecnologias_delete(request, id):
    tipo_tecnologia = TipoTecnologia.objects.get(pk=id)
    tipo_tecnologia.delete()
    return redirect('/backend/tipo-tecnologias/list/')

@login_required
def tipo_tecnologias_list(request):
    
        context = {'tipo_tecnologias_list': TipoTecnologia.objects.all()}
    
        return render(request, 'portofolio/tipos/tipo_tecnologias/tipo_tecnologia_list.html', context)

@login_required
def tipo_aptidoes_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TipoAptidaoForm()
        else:
            tipo_aptidao = TipoAptidao.objects.get(pk=id)
            form = TipoAptidaoForm(instance=tipo_aptidao)
        return render(request, 'portofolio/tipos/tipo_aptidoes/tipo_aptidao_form.html', {'form': form})
    else:
        if id == 0:
            form = TipoAptidaoForm(request.POST)
        else:
            tipo_aptidao = TipoAptidao.objects.get(pk=id)
            form = TipoAptidaoForm(request.POST, instance=tipo_aptidao)
        if form.is_valid():
            form.save()
        return redirect('/backend/tipo-aptidoes/list/')
    
@login_required
def tipo_aptidoes_delete(request, id):
    tipo_aptidao = TipoAptidao.objects.get(pk=id)
    tipo_aptidao.delete()
    return redirect('/backend/tipo-aptidoes/list/')

@login_required
def tipo_aptidoes_list(request):
        
            context = {'tipo_aptidoes_list': TipoAptidao.objects.all()}
        
            return render(request, 'portofolio/tipos/tipo_aptidoes/tipo_aptidao_list.html', context)

@login_required
def tipo_projetos_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TipoProjetoForm()
        else:
            tipo_projeto = TipoProjeto.objects.get(pk=id)
            form = TipoProjetoForm(instance=tipo_projeto)
        return render(request, 'portofolio/tipos/tipo_projetos/tipo_projeto_form.html', {'form': form})
    else:
        if id == 0:
            form = TipoProjetoForm(request.POST)
        else:
            tipo_projeto = TipoProjeto.objects.get(pk=id)
            form = TipoProjetoForm(request.POST, instance=tipo_projeto)
        if form.is_valid():
            form.save()
        return redirect('/backend/tipo-projetos/list/')
    
@login_required
def tipo_projetos_delete(request, id):
    tipo_projeto = TipoProjeto.objects.get(pk=id)
    tipo_projeto.delete()
    return redirect('/backend/tipo-projetos/list/')

@login_required
def tipo_projetos_list(request):

    context = {'tipo_projetos_list': TipoProjeto.objects.all()}

    return render(request, 'portofolio/tipos/tipo_projetos/tipo_projeto_list.html', context)

def index(request):

    pessoa = Pessoa.objects.get(nome='Diogo', sobrenome='Ferreira')

    return render(request, 'front/index.html', {'pessoa': pessoa})

def download_file(request):
    # Retrieve the file path or file object
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')
    
    # Open the file using FileResponse
    file = open(file_path, 'rb')
    
    # Create a FileResponse object with appropriate headers
    response = FileResponse(file)
    
    # Set the content type and headers for file download
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    response['Content-Type'] = 'application/pdf'
    
    return response


def studies(request):

    pessoa = Pessoa.objects.get(nome='Diogo', sobrenome='Ferreira')

    escolas = Escola.objects.filter(pessoa_id=pessoa.id)

    for escola in escolas:
        escola.inicio = escola.inicio.strftime("%Y")
        escola.fim = escola.fim.strftime("%Y")

    universidades = Universidade.objects.filter(pessoa_id=pessoa.id)
    for universidade in universidades:
        universidade.inicio = universidade.inicio.strftime("%Y")
        universidade.fim = universidade.fim.strftime("%Y")
        current_year = datetime.now().year

        if universidade.fim > current_year.__str__():
            universidade.fim = "Presente"
        
    return render(request, 'front/studies.html', {'pessoa': pessoa, 'escolas': escolas, 'universidades': universidades})





