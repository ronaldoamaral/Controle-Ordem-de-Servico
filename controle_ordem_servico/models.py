# -*- coding: utf-8 -*-
import os
from django.db import models
import utils


class Cliente(models.Model):

    class Meta:        
        verbose_name_plural = 'Cliente'

    nome = models.CharField(verbose_name='Nome', max_length=200)
    telefone = models.CharField(verbose_name='Telefone', max_length=10, blank=True)
    endereco = models.CharField(verbose_name='Endereço', max_length=200, blank=True)
    
    def __unicode__(self):
        return self.nome

class ItemServico(models.Model):

    class Meta:        
    
        verbose_name_plural = 'Item Serviço'
        
    ordem = models.ForeignKey('OrdemServico')    
    tipo_item = models.CharField(
        verbose_name='Tipo do Item', 
        max_length = 20,
        choices=(
            ('relogio', 'Relogio'), 
            ('joia', 'Joia'), 
        ),
    )
    marca = models.CharField(verbose_name='Marca/Modelo', max_length=200)
    servico = models.CharField(verbose_name='Serviço', max_length=200)
    
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    
class OrdemServico(models.Model):

    class Meta:        
        verbose_name_plural = 'Ordem de Serviço'
        
    codigo = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente)
    data_entrada = models.DateField(auto_now_add=True )
    situacao = models.CharField(
        verbose_name='Situação', 
        max_length = 20,
        default='naoiniciado',
        choices=(
            ('naoiniciado', 'Não Iniciado'), 
            ('andamento', 'Em Andamento'), 
            ('pronto', 'Pronto'), 
            ('entregue', 'Entregue'), 
        ),
    )
    data_saida = models.DateField(null=True, blank=True)
    observacoes = models.CharField(verbose_name='Observações', max_length=200, null=True, blank=True)
    pago = models.CharField(
        verbose_name='Pago',
        max_length = 3,
        default = 'nao',
        choices=(
            ('nao', 'Não'),
            ('sim', 'Sim'),
        )
    )
    valor_total = models.DecimalField(max_digits=15, decimal_places=2)
    
    def constroi_cupom(self):
        item_servico_list = self.itemservico_set.all()  
        return utils.gerar_cupom(codigo=self.codigo, data=self.data_entrada, cliente=str(self.cliente.nome), valor_total=self.valor_total, observacoes=str(self.observacoes), itens=item_servico_list)
        
        
    def imprimir_cupom(self):
        cupom = open('/tmp/cupom.txt','w')
        cupom.write(self.constroi_cupom())
        cupom.close()
        import pdb;pdb.set_trace()
        os.system('lpr /tmp/cupom.txt')
        os.system('rm -f /tmp/cupom.txt')    
