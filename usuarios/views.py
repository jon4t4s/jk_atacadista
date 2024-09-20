from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django
from .models import Item
from django.urls import reverse

#####################################################################################################################################################################

def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'usuarios/home.html')
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'E-mail ou senha inválidos!'})

#####################################################################################################################################################################

def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
        
    else:
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        first_name = request.POST.get('nome')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'usuarios/cadastro.html', {'error_message': 'Usuário já existente!'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return render(request, 'usuarios/cadastro.html')

#####################################################################################################################################################################

def home(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/home.html')
    else:
        return render(request, 'usuarios/login.html', {'error_message': 'Cara, tá dificil em'})

#####################################################################################################################################################################

def lancar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'usuarios/lancar.html')
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Sem comentarios'})
    else:
        item = Item()
        item.nome_aluno = request.user.first_name
        item.item = request.POST.get('item')

        item_verificado = Item.objects.filter(item = item.item).first()

        if item_verificado:
            return render(request, 'usuarios/lancar.html', {'error_message': 'Item já cadastrado!'})
        else:
            item.save()
            messages.success(request, 'Item adicionado com sucesso!')
            return render(request, 'usuarios/lancar.html') #------EDITEI O DEF LANCAR, APAGEUI TUDO QUE A GENTE NÃO IA USAR, DEIXANDO APENAS 0 BASICO------#

#####################################################################################################################################################################

def alterar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_item = Item.objects.filter(nome_aluno=request.user.first_name)
            dicionario_item = {'lista_item': lista_item}
            return render(request, 'usuarios/alterar.html', dicionario_item)
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Tenta só mais uma vez.'})

#####################################################################################################################################################################

def excluir_verificacao(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_item = Item.objects.get(pk=pk)
            dicionario_item = {'lista_item': lista_item}
            return render(request, 'usuarios/excluir.html', dicionario_item)
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Assim não da ne patrão'})

#####################################################################################################################################################################

def excluir(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated:
            item_selecionada = Item.objects.get(pk=pk)
            item_selecionada.delete()
            messages.success(request, 'Item excluído sucesso!')
            return HttpResponseRedirect(reverse('alterar'))
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Quantas vezes tenho que falar?'})

#####################################################################################################################################################################

def editar_verificacao(request, pk):
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_item = Item.objects.get(pk=pk)
            dicionario_item = {'lista_item':lista_item}
            return render(request, 'usuarios/editar.html', dicionario_item)
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Ai você me quebra...'})

#####################################################################################################################################################################

def editar(request, pk):
    if request.method == "POST":
        if request.user.is_authenticated:
            item = request.POST.get('item')
            Item.objects.filter(pk=pk).update(item = item)
            messages.success(request, 'Item Alterado com sucesso!')
            return HttpResponseRedirect(reverse('alterar'))
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Tem que logar pow'})

#####################################################################################################################################################################

def visualizar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            lista_item = Item.objects.filter(nome_aluno=request.user.first_name)
            dicionario_item = {'lista_item': lista_item}
            return render(request, 'usuarios/visualizar.html', dicionario_item)
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Cara, acho que você errou alguma coisa.'})
    else:
        item = request.POST.get('item')
        if item == "Todos os itens":
            lista_item = Item.objects.filter(nome_aluno=request .user.first_name)
            dicionario_item = {'lista_item': lista_item}
            return render(request, 'usuarios/visualizar.html', dicionario_item)
        else:
            lista_item = Item.objects.filter(nome_aluno=request .user.first_name, item=item)
            dicionario_item_filtradas = {"lista_item": lista_item}
            return render(request, 'usuarios/visualizar.html', dicionario_item_filtradas)

#####################################################################################################################################################################

def logout(request):
    if request.user.is_authenticated:
        logout_django(request)
        return render(request, 'usuarios/login.html')
    else:
        return render(request, 'usuarios/login.html', {'error_message': 'Vamos tentar de novo?'})

#####################################################################################################################################################################

def sobre(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/sobre.html')
    else:
        return render(request, 'usuarios/login.html', {'error_message': 'Tem certeza que acessou sua conta?'})

#####################################################################################################################################################################

def perfil(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/perfil.html')
    else:
        return render(request, 'usuarios/login.html', {'error_message': 'Tem algo de errado!'})

#####################################################################################################################################################################

def contato(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/contato.html')
    else:
        if request.user.is_authenticated:
            nome = request.POST.get('nome', '')
            email = request.POST.get('email', '')
            mensagem = request.POST.get('mensagem', '')
            mensagem = "Nome: " + (nome or '') + " | Email: " + (email or '') + " | Mensagem: " + (mensagem or '')
            messages.success(request, 'Formulário Enviado')
            return render(request, 'usuarios/contato.html')
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Você não acessou sua conta ainda!'})   