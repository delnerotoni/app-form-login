from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#Página inicial
def home(request):
    return render(request, 'home.html')

#Formulário de Cadastro dos usuários
def create(request):
    return render(request, 'create.html')

#Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senhas diferentes!'
        data['class'] = 'alert-danger'

    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(1)
        data['msg'] = 'Usuário cadastrado com sucesso!!'
        data['class'] = 'alert-success'

    return render(request, 'create.html',data)


#Formulário do painel de login
def painel(request):
    return render(request, 'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'

        return render(request,'painel.html', data)

#Página Inicial do Dashboard
def dashboard(request):
    return render(request,'dashboard/home.html')

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')


