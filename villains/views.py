from django.shortcuts import render

# Create your views here.
def lista_viloes(request):
    return render(request, 'villains/lista_viloes.html')

# Luiz Enrique