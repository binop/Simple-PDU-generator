from django.conf.urls.defaults import include, patterns
from django.contrib import admin
from django.conf import settings


admin.autodiscover()
urlpatterns = patterns(
    '',
    (r'^pdugen/', include('pdugen.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += patterns('django.views.generic',
                        (r'^$', 'simple.redirect_to', {'url': '/pdugen/list/'}),
                        )
