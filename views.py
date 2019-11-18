from django.shortcuts import render, get_object_or_404
from pessoa.models import *


# Create your views here.
def listarPessoas(request):
    context = {}
    pessoas = Pessoa.objects.all()
    pessoafotos = PessoaFoto.objects.all()
    context['pessoas'] = pessoas
    context['pessoafotos'] = pessoafotos

    return render(request, 'listarpessoas.html', context)


def descricao_pessoa(request, id):
    descricao = get_object_or_404(Pessoa, pk=id)
    descricao1 = get_object_or_404(PessoaFoto, pk=id)
    return render(request, 'descricao_pessoa.html', {'descricao': descricao,
                                                     'descricao1': descricao1})
