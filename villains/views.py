from django.shortcuts import render
from .models import Villain
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import VillainForm
from django.urls import reverse_lazy

# Create your views here.
class VillainListView(ListView):
    model = Villain
    template_name = 'villains/lista_viloes.html'
    context_object_name = 'villains'

class VillainCreateView(CreateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_villain.html'
    success_url = reverse_lazy('lista_viloes')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['villains'] = True
        return contexto

class VillainUpdateView(UpdateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_villain.html'
    success_url = reverse_lazy('lista_viloes')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['villains'] = True
        return contexto

class VillainDeleteView(DeleteView):
    model = Villain
    template_name = 'villains/exclusao_villain.html'
    success_url = reverse_lazy('lista_viloes')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['villains'] = True
        return contexto

# Luiz Enrique