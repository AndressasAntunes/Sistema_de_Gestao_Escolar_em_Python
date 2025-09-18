from django.urls import path
from . import views

app_name = "alunos"

urlpatterns = [
    path("", views.lista_alunos, name="lista_alunos"),
    path("novo/", views.criar_aluno, name="criar_aluno"),
]