from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request,'Enviado Com Sucesso!')
        form = ContatoForm()

    else:
      messages.error(request, 'Erro ao enviar')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            messages.success(request,'Produto Salvo Parsa.')

            form = ProdutoModelForm()
        else:
            messages.error(request, 'ih rapaz deu erro')
    else:
            form = ProdutoModelForm()
    context = {
                'form': form
        }
    return render(request, 'produto.html', context)