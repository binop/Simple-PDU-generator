from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('pdugen.views',
                       url(r'^list/$', 'list', name='list'),
                       url(r'^details/(?P<object_id>\d+)/$','details', name='details'),
                       url(r'^new/$','new', name='new'),
                       url(r'^remove/(?P<object_id>\d+)/$','remove', name='remove'),
                       )

urlpatterns += patterns('django.views.generic',
                        (r'^$', 'simple.redirect_to', {'url': '/pdugen/list/'}),
                        )
