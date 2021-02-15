from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    # print(dir(request.user))
    # print(request.user.email_user)
    produtos = Produto.objects.all()
    if str(request.user) == 'AnonymousUser':
        status = 'Usuário não logado.'
    else:
        status = f'Usuário {request.user.username}, logado com sucesso.'

    context = {'curso': 'Programação web com o Django',
               'outro': 'API rest full com Django REST Framework',
               'produtos': produtos,
               'status': status,
               }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id_prod):
    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id_prod)
    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('error500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
