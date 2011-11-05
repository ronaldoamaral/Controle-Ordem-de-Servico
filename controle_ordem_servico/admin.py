from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from models import OrdemServico
from models import Cliente
from models import ItemServico

class ItemServicoInline(admin.TabularInline):
    model = ItemServico
    extra = 1
    

class OrdemServicoAdmin(ForeignKeyAutocompleteAdmin, admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'data_entrada','situacao', 'data_saida','valor_total')
    list_filter = ('situacao',)
    search_fields = ('cliente__nome','numero',)   
    
    related_search_fields = { 
                'cliente': ('nome',),
        }

    inlines = [ItemServicoInline]
    fieldsets = (
        ('None', {
            'fields': ('numero','cliente', 'situacao', 'observacoes', )
        }),
        ('Dados Entrega',{
            'fields':('pago', 'valor_total',) 
        }),
    )


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','endereco')
    search_fields = ('nome',)


admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(Cliente, ClienteAdmin)
