from django.db import models

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

    class Meta:
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"
    
    def __str__ (self):
        return self.titulo

class resposta(models.Model):
    pergunta = models.ForeignKey(enquete, on_delete=models.CASCADE)
    resp = models.TextField()

    def __str__(self):
        return self.resp
    
    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"