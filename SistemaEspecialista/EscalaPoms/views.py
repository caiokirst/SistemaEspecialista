from django.shortcuts import render, redirect

from .utils import *
from .models import *

#Todas as funções verificam se o método é post get
#Caso for post realiza o processamento adequado
#Caso for get renderiza a página correspondente

def login(request):
    
    if request.method == 'POST':
        return redirect('dashboard')

    return render(request,'EscalaPoms/login.html')

def cadastro(request):
    
    if request.method == 'POST':
        if validar_cpf(request.POST['cpf']):
            """"
            cpf = request.POST['cpf']
            nome = request.POST['nome']
            email = request.POST['email']
            senha = request.POST['senha']
            tipo_usuario = request.POST['tipo_usuario']
            """
            return redirect('login')    
        
        message = {
            'message': 'CPF inválido. Por favor, insira um CPF válido.'
        }
        return render(request, 'EscalaPoms:cadastro', message)
    

    return render(request, 'EscalaPoms/cadastro.html')

def escala(request):
    if request.method == 'POST':
       return redirect('dashboard')

    return render(request, 'EscalaPoms/escala.html')

def perfil(request):
    
    # cpf_logado = request.user.cpf
    # usuario = None

    # if Aluno.objects.filter(cpf=cpf_logado).exists():
    #     usuario = Aluno.objects.get(cpf=cpf_logado)
    # elif Treinador.objects.filter(cpf=cpf_logado).exists():
    #     usuario = Treinador.objects.get(cpf=cpf_logado)
    return render(request, 'EscalaPoms/perfil.html')

def dashboard(request):
    #aqui serão feitos os cálculos para gerar os gráficos e as informações que serão mostradas no dashboard
    return render(request, 'EscalaPoms/dashboard.html')

def relatorio(request):
    #aqui será feito o processamento para gerar os relatórios, somas e gráficos
    return render(request, 'EscalaPoms/relatorio.html')