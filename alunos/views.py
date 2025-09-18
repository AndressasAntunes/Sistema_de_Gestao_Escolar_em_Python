from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos/lista_alunos.html", {"alunos": alunos})

def criar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_alunos")
        
    else:
        form = AlunoForm()
        return render(request, "alunos/criar_aluno.html", {"form: form"})
  
