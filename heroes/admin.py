from django.contrib import admin
from .models import Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('codinome', 'cidade', 'criado_em')
    search_fields = ('codinome', 'nome_real', 'cidade')
    readonly_fields = ('criado_em',)

    fieldsets = (
    ('Identidade Secreta', {
    'fields': ('codinome', 'nome_real'),
    }),
    ('Informações Gerais', {
    'fields': ('poder_principal', 'cidade', 'email_contato', 'historia', 'imagem'),
    }),
    ('Dados de Registro', {
    'fields': ('criado_em',),
    'classes': ('collapse',),
    }),
    )