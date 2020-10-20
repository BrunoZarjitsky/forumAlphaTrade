from django.shortcuts import render
from random import randint
from .models import *

# Create your views here.

def Index(request):
    enquetes = enquete.objects.all()
    print(enquetes[0].tipo.all())
    return render(request, "index.html", {"background": "background"+str(randint(1,3))+".jpg"})