from django.contrib import admin
from .models import Villain

# Register your models here.
@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ('codinome', 'poder_principal', 'cidade', 'historia', 'criado_em')
    list_filter = ('cidade',)
    search_fields = ('codinome', 'cidade')
    readonly_fields = ('criado_em',)

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome',),
        }),
        ('Informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia', 'imagem'),
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',),
            'classes': ('collapse',),
        })
    )