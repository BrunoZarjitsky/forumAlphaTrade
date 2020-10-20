from django.shortcuts import render
from random import randint
from .models import *

# Create your views here.

def Index(request):
    enquetes = enquete.objects.all()
    print(enquetes[0].tipo.all())
    ultimas = enquetes.order_by("-id")[0:20]
    return render(request, "index.html", {"background": "background"+str(randint(1,3))+".jpg", "ultimas": ultimas})

def Enquetes(request):
    enquetesLista = enquete.objects.all()
    return render(request, "enquetes.html", {"background": "background"+str(randint(1,3))+".jpg", 
                                            "enquetesLista": enquetesLista})

def EnqueteDetalhe(request, id):
    enqueteDet = enquete.objects.get(id = id)
    return render(request, "enqueteDetalhe.html", {"background": "background"+str(randint(1,3))+".jpg",
                                                    "enqueteDet": enqueteDet,})