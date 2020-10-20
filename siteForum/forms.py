from django import forms
from .models import *

class RespostaForm(forms.ModelForm):

    class Meta:
        model = "resposta"
        fields = ("pergunta", "resp")