from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    #(r'^$', include('controle_ordem_servico.urls')),
    (r'^site_media/(.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT}
    ),    
    (r'^django_extensions/(.*)$', 'django.views.static.serve',
      {'document_root': settings.DJANGO_EXTENSIONS_MEDIA}
    )
)
