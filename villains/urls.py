from django.urls import path
from . import views

urlpatterns = [
    path('', views.VillainListView.as_view(), name='lista_viloes'),
    path('novo/', views.VillainCreateView.as_view()),
    path('<int:pk>/editar/', views.VillainUpdateView.as_view()),
    path('<int:pk>/deletar/', views.VillainDeleteView.as_view()),
]

# Luiz Enrique