from django.shortcuts import render_to_response
from django.template import RequestContext
from controle_ordem_servico.models import OrdemServico


def imprimir_cupom(request, ordem_codigo):
    ordem_servico = OrdemServico.objects.get(codigo=ordem_codigo)    
    ordem_servico.imprimir_cupom()
   
    return render_to_response(
        'imprimir_cupom.html',
        context_instance=RequestContext(request)
    )
        

    


