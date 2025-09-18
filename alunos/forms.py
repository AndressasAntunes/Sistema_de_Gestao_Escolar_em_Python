from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "sobrenome", "data_nascimento", "curso"]

    