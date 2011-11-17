from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^imprimir_cupom/(?P<ordem_codigo>\d+)$', 'controle_ordem_servico.views.imprimir_cupom'),
)
