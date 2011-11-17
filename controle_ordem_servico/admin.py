from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from models import OrdemServico
from models import Cliente
from models import ItemServico

class ItemServicoInline(admin.TabularInline):
    model = ItemServico
    extra = 1
    

class OrdemServicoAdmin(ForeignKeyAutocompleteAdmin, admin.ModelAdmin):
    class Media:
        js = ("/site_media/js/ordem_servico.js",)
        
    list_display = ('codigo', 'cliente', 'data_entrada','situacao', 'data_saida','valor_total')
    list_filter = ('situacao', 'data_entrada')
    search_fields = ('cliente__nome','codigo',)   
    date_hierarchy = 'data_entrada'
    related_search_fields = { 
                'cliente': ('nome',),
        }

    inlines = [ItemServicoInline]
    fieldsets = (
        ('None', {
            'fields': ('cliente', 'situacao', 'observacoes', )
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
