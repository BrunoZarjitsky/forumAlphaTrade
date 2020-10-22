from django import forms
from .models import *

class RespostaForm(forms.ModelForm):
    def __init__(self, **kwargs):
        self.pergunta = kwargs.pop('pergunta', None)
        self.author = kwargs.pop('author', None)
        self.dono = kwargs.pop('dono', None)
        super(RespostaForm, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(RespostaForm, self).save(commit=False)
        obj.pergunta = self.pergunta
        obj.author = self.author
        obj.dono = self.dono
        if commit:
            obj.save()
        return obj

    class Meta:
        model = resposta
        fields = ("resp",)
        exclude = ("pergunta", )


class NovaEnquete(forms.ModelForm):

    def __init__(self, **kwargs):
        self.dono = kwargs.pop("dono", None)
        super(NovaEnquete, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(NovaEnquete, self).save(commit=False)
        obj.dono = self.dono
        if commit:
            obj.save()
        return obj

    class Meta:
        model = enquete
        fields = ("titulo", "descricao", "tipo")


class avalPos(forms.ModelForm):

    def __init__(self, **kwargs):
        self.aval = 1
        self.resp = kwargs.pop("resp", None)
        self.dono = kwargs.pop("dono", None)
        super(avalPos, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(avalPos, self).save(commit=False)
        obj.resp = self.resp
        obj.dono = self.dono
        obj.aval = 1
        if commit:
            obj.save()
        return obj

    class Meta:
        model = avaliacaoResp
        exclude = ("aval", "resp")
    
class perfilForm(forms.ModelForm):

    def __init__(self, **kwargs):
        self.usuario = kwargs.pop("usuario", None)
        super(perfilForm, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(perfilForm, self).save(commit=False)
        obj.usuario = self.usuario
        if commit:
            obj.save()
        return obj

    class Meta:
        model = perfil
        exclude = ("usuario",)