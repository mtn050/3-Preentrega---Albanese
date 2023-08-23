from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def Cliente(request):
    return render(request, "cliente.html")

def Empleado(request):
    return render(request, "empleado.html")

def Compra(request):
  return render(request, "compra.html")
