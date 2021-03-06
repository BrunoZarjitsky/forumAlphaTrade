from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tipo(models.Model):
    tipoChoice = (
        ("Python", "Python"),
        ("Django", "Django"),
        ("Html", "Html"),
        ("CSS", "CSS"),
        ("Linux", "Linux"),
        ("Bootstrap", "Bootstrap"),
        ("FontAwesome", "FontAwesome"),
    )
    tipo = models.CharField(max_length=50, choices=tipoChoice)

    def __str__(self):
        return self.tipo

class enquete(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(default="")
    tipo = models.ManyToManyField(tipo, blank=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True, null=True)

    class Meta:
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"
    
    def __str__ (self):
        return self.titulo

class resposta(models.Model):
    pergunta = models.ForeignKey(enquete, on_delete=models.CASCADE)
    resp = models.TextField(verbose_name="Resposta")
    dono = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True, null=True)

    def __str__(self):
        return self.resp
    
    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"

class avaliacaoResp(models.Model):
    aval = models.IntegerField()
    resp = models.ForeignKey(resposta, on_delete=models.CASCADE)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True, null=True)

    def __str__(self):
        return str(self.aval)+ " " +str(self.resp.resp)

class perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True, null=True)
    nomeCompleto = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    foto = models.FileField(blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    mostrarNome = models.BooleanField()
    mostrarEmail = models.BooleanField()
    mostrarFoto = models.BooleanField()
    mostrarNascimento = models.BooleanField()

    def __str__(self):
        return str(self.nomeCompleto) + ", " + str(self.usuario)