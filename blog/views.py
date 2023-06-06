from django.shortcuts import render
from .models import Author, Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def nova(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog-home')

    context = {
        'form': form
    }

    return render(request, 'blog/nova.html', context)

def editar(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog-home')

    context = {
        'form': form,
        'post_id': pk,
    }

    return render(request, 'blog/edita.html', context)

def deletar(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('blog-home')
