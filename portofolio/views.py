from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .forms import PessoaForm
from .forms import ProfessorForm
from .forms import EscolaForm
from .forms import UniversidadeForm
from .forms import CursoForm
from .forms import CadeiraForm

from .models import Pessoa
from .models import Professor
from .models import Escola
from .models import Universidade
from .models import Curso
from .models import Cadeira

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
        return redirect('/portofolio/pessoas/list/')

@login_required
def pessoas_delete(request, id):
    pessoa = Pessoa.objects.get(pk=id)
    pessoa.delete()
    return redirect('/portofolio/pessoas/list/')

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
        return redirect('/portofolio/professores/list/')
    
@login_required
def professores_delete(request, id):
    professor = Professor.objects.get(pk=id)
    professor.delete()
    return redirect('/portofolio/professores/list/')

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
            form = EscolaForm(request.POST)
        else:
            escola = Escola.objects.get(pk=id)
            form = EscolaForm(request.POST, instance=escola)
        if form.is_valid():
            form.save()
        return redirect('/portofolio/escolas/list/')
    
@login_required
def escolas_delete(request, id):
    escola = Escola.objects.get(pk=id)
    escola.delete()
    return redirect('/portofolio/escolas/list/')

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
            form = UniversidadeForm(request.POST)
        else:
            universidade = Universidade.objects.get(pk=id)
            form = UniversidadeForm(request.POST, instance=universidade)
        if form.is_valid():
            form.save()
        return redirect('/portofolio/universidades/list/')

@login_required
def universidades_delete(request, id):
    universidade = Universidade.objects.get(pk=id)
    universidade.delete()
    return redirect('/portofolio/universidades/list/')

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
        return redirect('/portofolio/cursos/list/')
    
@login_required
def cursos_delete(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('/portofolio/cursos/list/')

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
        return redirect('/portofolio/cadeiras/list/')
    
@login_required
def cadeiras_delete(request, id):
    cadeira = Cadeira.objects.get(pk=id)
    cadeira.delete()
    return redirect('/portofolio/cadeiras/list/')

