# -*- coding: utf-8 -*-

def gerar_cupom(codigo=None, data=None, cliente=None, valor_total=None, observacoes=None, itens=None):
    data_entrada = "%(dia)d/%(mes)d/%(ano)d" % {'dia': data.day, 'mes':data.month, 'ano': data.year}
    cupom_string = """
==========================================
         XXXX   XXX      XXXX      XXXX  
==========================================      
           Ordem de Servico
------------------------------------------
Codigo: %(codigo)d         Data: %(data)s 
Cliente: %(cliente)s 
------------------------------------------
Servico                           Valor R$        
------------------------------------------
""" % {'codigo':codigo, 'data':data_entrada, 'cliente':cliente}
                             
    for  item in itens:
        cupom_string = cupom_string + " %(servico)s                %(valor).2f \n" % {'servico': str(item.servico), 'valor':item.valor}
         
    cupom_string = cupom_string + """
------------------------------------------
         TOTAL R$: %.2f
------------------------------------------""" % valor_total
    cupom_string = cupom_string + """
OBSERVACOES:  %s """ % str(observacoes)

    cupom_string = cupom_string + """
        
        
==========================================





"""

    return cupom_string
