from django.contrib import admin
from .models import Hero

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'historia', 'criado_em', 'email_contato']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real',)
        }),
        ('informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia',)
        }),
        ('Dados de Registro', {
            'fields': ('criado_em', 'email_contato')
        }),
    )
    readonly_fields = ['criado_em']

# Luiz Enrique