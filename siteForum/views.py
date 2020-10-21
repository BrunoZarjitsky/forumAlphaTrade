from django.shortcuts import render
from random import randint
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import *

# Create your views here.

def Index(request):
    enquetes = enquete.objects.all()
    # print(enquetes[0].tipo.all())
    enquetesLista = []
    emAlta = [{"enquete": enquetes[0], "qtdRespostas": 0}, {"enquete": enquetes[1], "qtdRespostas": 0}, {"enquete": enquetes[2], "qtdRespostas": 0}]
    emAltaPlacehold = [0, 0, 0]
    for i in enquetes:
        qtdRespostas = len(resposta.objects.filter(pergunta=i))
        print(qtdRespostas)
        if qtdRespostas >= emAltaPlacehold[0]:
            emAltaPlacehold[0] = qtdRespostas
            emAlta[2] = emAlta[1]
            emAlta[1] = emAlta[0]
            emAlta[0] = {"enquete": i, "qtdRespostas": qtdRespostas}
        enquetesLista.append({"enquete": i, "qtdRespostas": qtdRespostas})
    ultimas = enquetesLista[0:20][::-1]
    return render(request, "index.html", {"background": "background"+str(randint(1,3))+".jpg", "ultimas": ultimas,
                                            "emAlta": emAlta})

def Enquetes(request):
    enquetes = enquete.objects.all()
    titulo = "Todas as enquetes"
    enquetesLista = []
    for i in enquetes:
        qtdRespostas = len(resposta.objects.filter(pergunta=i))
        enquetesLista.append({"enquete": i, "qtdRespostas": qtdRespostas})
    return render(request, "enquetes.html", {"background": "background"+str(randint(1,3))+".jpg", 
                                            "enquetesLista": enquetesLista, "titulo": titulo,})


def EnqueteDetalhe(request, id):
    enqueteDet = enquete.objects.get(id = id)
    pergunta = enquete.objects.get(id=id)
    respostas = resposta.objects.filter(pergunta=pergunta)
    print(request.POST)
    if request.method == "POST":
        if "aval" in request.POST:
            print("\n\n\n\n\n\n")
        form = RespostaForm(pergunta=pergunta, dono=request.user, author=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')
    else:
        form = RespostaForm()
    return render(request, "enqueteDetalhe.html", {"background": "background"+str(randint(1,3))+".jpg",
                                                    "enqueteDet": enqueteDet, "form": form, "respostas": respostas,
                                                    })

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("Index")
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def minhasEnquetes(request):
    enquetes = enquete.objects.filter(dono=request.user)
    titulo = "Minhas enquetes"
    enquetesLista = []
    for i in enquetes:
        qtdRespostas = len(resposta.objects.filter(pergunta=i))
        enquetesLista.append({"enquete": i, "qtdRespostas": qtdRespostas})
    return render(request, "enquetes.html", {"background": "background"+str(randint(1,3))+".jpg", "enquetesLista": enquetesLista,
                                            "titulo": titulo, })

def minhasRespostas(request):
    res = resposta.objects.filter(dono=request.user)
    return render(request, "respostas.html", {"background": "background"+str(randint(1,3))+".jpg", "respostasLista": res})

def novaEnquete(request):
    if request.method == "POST":
        form = NovaEnquete(dono=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')
    else:
        form = NovaEnquete()
    return render(request, "novaEnquete.html", {"background": "background"+str(randint(1,3))+".jpg",
                                                "form": form,})