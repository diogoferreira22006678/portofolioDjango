from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .forms import PessoaForm
from .forms import ProfessorForm
from .forms import EscolaForm

from .models import Pessoa
from .models import Professor
from .models import Escola

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
