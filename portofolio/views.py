from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PessoaForm
from django.shortcuts import redirect
from .models import Pessoa

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
