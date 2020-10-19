from django.shortcuts import render
from random import randint

# Create your views here.

def Index(request):
    return render(request, "index.html", {"background": "background"+str(randint(1,3))+".jpg"})