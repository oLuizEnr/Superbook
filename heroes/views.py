from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero

# Create your views here.
def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

def lista_herois(request):
    herois = Hero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"herois": herois})