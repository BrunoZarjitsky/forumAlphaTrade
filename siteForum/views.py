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
        if qtdRespostas >= emAltaPlacehold[0]:
            emAltaPlacehold[0] = qtdRespostas
            emAlta[2] = emAlta[1]
            emAlta[1] = emAlta[0]
            emAltaPlacehold[1] = emAlta[1]["qtdRespostas"]
            emAltaPlacehold[2] = emAlta[2]["qtdRespostas"]
            emAlta[0] = {"enquete": i, "qtdRespostas": qtdRespostas}
        elif qtdRespostas >= emAltaPlacehold[1]:
            emAltaPlacehold[1] = qtdRespostas
            emAlta[2] = emAlta[1]
            emAltaPlacehold[2] = emAlta[2]["qtdRespostas"]
            emAlta[1] = {"enquete": i, "qtdRespostas": qtdRespostas}
        elif qtdRespostas >= emAltaPlacehold[2]:
            emAltaPlacehold[2] = qtdRespostas
            emAlta[2] = {"enquete": i, "qtdRespostas": qtdRespostas}
        enquetesLista.append({"enquete": i, "qtdRespostas": qtdRespostas})
        print(emAltaPlacehold)
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
    respostas = resposta.objects.filter(pergunta=pergunta).order_by("-id")
    principal = 0
    if len(respostas) != 0 :
        principal = {"resp": respostas[0].resp, "dono": respostas[0].dono, "id": respostas[0].id, "likes": 0}
        principalPlacehold = 0
    respostasLikes = []
    for i in respostas:
        qtd = len(avaliacaoResp.objects.filter(resp=i))
        if qtd > principalPlacehold:
            principal = {"resp": i.resp, "dono": i.dono, "id": i.id, "likes": qtd}
            principalPlacehold = qtd
        respostasLikes.append({"resp": i.resp, "dono": i.dono, "id": i.id, "likes": qtd})
    if principal in respostasLikes:
        respostasLikes.remove(principal)
    if request.method == "POST":
        if "aval" in request.POST:
            # print(resposta.objects.get(id=request.POST["aval"]).dono == request.user)
            form2 = avalPos(resp=resposta.objects.get(id=request.POST["aval"]), data=request.POST, dono=request.user)
            donos = []
            for i in avaliacaoResp.objects.filter(resp = resposta.objects.get(id=request.POST["aval"])):
                donos.append(str(i.dono))
            if ((str(request.user) not in donos) and (str(request.user) != "AnonymousUser") and (form2.is_valid())):
                print("aaaaaaaaaaaaaaaaaaaaa")
                form2.save()
                return redirect("EnqueteDetalhe", id)
            else:
                return redirect("EnqueteDetalhe", id)
        else:
            form = RespostaForm(pergunta=pergunta, dono=request.user, author=request.user, data=request.POST)
            if form.is_valid():
                form.save()
            return redirect('Index')
    form = RespostaForm()
    return render(request, "enqueteDetalhe.html", {"background": "background"+str(randint(1,3))+".jpg",
                                                    "enqueteDet": enqueteDet, "form": form, "respostas": respostasLikes,
                                                    "avalPos": avalPos, "principal": principal})

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