from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PessoaForm
from django.shortcuts import redirect

# Create your views here.
@login_required
def home(request):
    return render(request, 'portofolio/home.html')

def pessoas_list(request):
    return render(request, 'portofolio/pessoal/pessoas/pessoa_list.html')

def pessoas_form(request):
    if request.method == "GET":
        form = PessoaForm()
        return render(request, 'portofolio/pessoal/pessoas/pessoa_form.html', {'form': form})
    else:
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/portofolio/pessoas/list/')

def pessoas_delete(request):
    return
