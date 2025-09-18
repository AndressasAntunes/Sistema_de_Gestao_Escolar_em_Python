from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField("Nome", max_length=100)
    sobrenome = models.CharField("sobrenome", max_length=100)
    data_nascimento = models.DateField("Data de nascimento")
    curso = models.CharField("Curso", max_length=100)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

class Meta:
    ordering = ["sobrenome", "nome"]

def __str__(self):
    return f"{self.nome} {self.sobrenome}"

    
