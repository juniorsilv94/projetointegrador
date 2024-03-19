from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.matricula = request.POST.get('matricula')
    novo_usuario.curso = request.POST.get('curso')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.nome_do_professor = request.POST.get('nome_do_professor')
    novo_usuario.codigo = request.POST.get('codigo')
    novo_usuario.disciplina = request.POST.get('disciplina')
    novo_usuario.save()
    
