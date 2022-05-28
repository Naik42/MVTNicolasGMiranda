from django.http import HttpResponse
from django.shortcuts import render
from usuarios.models import Familiares
import datetime
# Create your views here.


def inicio(request):
    return render (request , "index.html")



def familia(request):
    familiares = Familiares.objects.all()
    datos = {"datos" : familiares}

    return render( request , "familiares.html", datos)


def altaF(request):
    familiar = Familiares(nombre = "Nahuel" , edad=30, nacimiento = "1992-1-17")
    familiar.save()
    familiar = Familiares(nombre = "Gloria" , edad=49, nacimiento = "1973-1-17")
    familiar.save()
    familiar = Familiares(nombre = "Alma" , edad=19, nacimiento = "2003-4-17")
    familiar.save()

    return HttpResponse("Alta efectuada")