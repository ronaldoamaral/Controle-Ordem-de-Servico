from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from models import OrdemServico
from models import Cliente
from models import ItemServico

def imprimir_cupom(OrdemServicoAdmin, request, queryset):
    for obj in queryset:
        obj.imprimir_cupom()


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
    actions = [imprimir_cupom]
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
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if form.data.has_key('imprimir'):
            self.obj_para_imprimir = obj

    def add_view(self, request, form_url='', extra_context=None):
        response = super(OrdemServicoAdmin, self).add_view(request, form_url, extra_context)
        if hasattr(self, 'obj_para_imprimir'):
            self.obj_para_imprimir.imprimir_cupom()
            del self.obj_para_imprimir
        return response

    def change_view(self, request, object_id, extra_context=None):
        response = super(OrdemServicoAdmin, self).change_view(request, object_id, extra_context)
        if hasattr(self, 'obj_para_imprimir'):
            self.obj_para_imprimir.imprimir_cupom()
            del self.obj_para_imprimir
        return response       
   
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','endereco')
    search_fields = ('nome',)


admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(Cliente, ClienteAdmin)
